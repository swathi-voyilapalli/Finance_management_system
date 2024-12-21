import psycopg2

def init_db():
    
    conn = psycopg2.connect(database="finance",
            user="postgres",
            password="123456789",
            host="127.0.0.1",
            port="5432")
    
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT)''')
    print("Table Created")
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = psycopg2.connect(database="finance",
            user="postgres",
            password="123456789",
            host="127.0.0.1",
            port="5432")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
    except psycopg2.IntegrityError:
        print("Username already exists.")
    conn.close()

def authenticate_user(username, password):
    conn = psycopg2.connect(database="finance",
            user="postgres",
            password="123456789",
            host="127.0.0.1",
            port="5432")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None
