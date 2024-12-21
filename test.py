import unittest
import psycopg2


DB_CONFIG = {"database":"finance",
        "user":"postgres",
        "password":"123456789",
        "host":"127.0.0.1",
        "port":"5432"          
}

def connect_db():
    return psycopg2.connect(**DB_CONFIG)

def register_user(username, password):
    with connect_db() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, password))
                conn.commit()
            except psycopg2.IntegrityError:
                conn.rollback()
                raise ValueError("User already exists.")

def authenticate_user(username, password):
    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT password FROM users WHERE username = %s;", (username,))
            result = cursor.fetchone()
            return result is not None and result[0] == password

class TestUserFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the database table for tests
        with connect_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    DROP TABLE IF EXISTS users;
                    CREATE TABLE users (
                        username VARCHAR PRIMARY KEY,
                        password VARCHAR NOT NULL
                    );
                """)
                conn.commit()

    def test_register_user(self):
        # Test user registration
        register_user("testuser", "password123")
        self.assertTrue(authenticate_user("testuser", "password123"))

    def test_register_duplicate_user(self):
        # Test registering a duplicate user
        register_user("testuser", "password123")
        with self.assertRaises(ValueError): 
            register_user("testuser", "newpassword")

    def test_authenticate_invalid_user(self):
        # Test authenticating with a non-existent user
        self.assertFalse(authenticate_user("nonexistent", "password123"))

    def test_authenticate_incorrect_password(self):
        # Test authenticating with an incorrect password
        register_user("testuser", "password123")
        self.assertFalse(authenticate_user("testuser", "wrongpassword"))

if __name__ == '__main__':
    unittest.main()
