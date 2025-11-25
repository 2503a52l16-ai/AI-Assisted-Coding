import mysql.connector

def fetch_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="charansai1234@",
        database="testdb"
    )

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name FROM users")

    rows = cursor.fetchall()
    return rows

if __name__ == "__main__":
    data = fetch_data()
    print(data)
