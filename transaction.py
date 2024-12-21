import psycopg2

def init_transaction_db():
    conn = psycopg2.connect(database="finance",
            user="postgres",
            password="123456789",
            host="127.0.0.1",
            port="5432")
    
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (user_id TEXT, type TEXT, amount REAL, category TEXT, date TEXT)''')
    conn.commit()
    conn.close()

def add_transaction(user_id, transaction_type, amount, category, date):
    conn = psycopg2.connect(database="finance",
            user="postgres",
            password="123456789",
            host="127.0.0.1",
            port="5432")
    c = conn.cursor()
    c.execute("INSERT INTO transactions (user_id, type, amount, category, date) VALUES (%s, %s, %s, %s, %s)",
              (user_id, transaction_type, amount, category, date))
    conn.commit()

def get_transactions(user_id):
    conn = psycopg2.connect(database="finance",
            user="postgres",
            password="123456789",
            host="127.0.0.1",
            port="5432")
    c = conn.cursor()
    c.execute("SELECT * FROM transactions WHERE user_id=%s", (user_id,))
    transactions = c.fetchall()
    conn.close()
    return transactions
