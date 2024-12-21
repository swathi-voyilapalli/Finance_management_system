import psycopg2

def init_budget_db():
    conn = psycopg2.connect(database="finance",
            user="postgres",
            password="123456789",
            host="127.0.0.1",
            port="5432")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS budgets (user_id TEXT, category TEXT, liimit REAL)''')
    conn.commit()
    conn.close()

def set_budget(user_id, category, limit):
    conn = psycopg2.connect(database="finance",
            user="postgres",
            password="123456789",
            host="127.0.0.1",
            port="5432")
    c = conn.cursor()
    c.execute("INSERT INTO budgets (user_id, category, liimit) VALUES (%s, %s, %s)", (user_id, category, limit))
    print("\nBudget Set Successfully!")
    conn.commit()
    conn.close()
