import psycopg2

def generate_report(user_id):
    conn = psycopg2.connect(database="finance",
            user="postgres",
            password="123456789",
            host="127.0.0.1",
            port="5432")
    c = conn.cursor()
    c.execute("SELECT type, SUM(amount) FROM transactions WHERE user_id=%s GROUP BY type", (user_id,))
    report = c.fetchall()
    for i in report:
        print("\nTransaction Type:"+i[0])
        print("\nAmount:"+str(i[1]))
    conn.close()
    return report
