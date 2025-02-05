import pymysql

def connect():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="MYSQL",
            database="mydatabase"
        )
        print("Connected to MySQL successfully!")
        return conn
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return None

def create_database():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="MYSQL"
        )
        conn.cursor().execute("CREATE DATABASE IF NOT EXISTS mydatabase")
        conn.close()
    except pymysql.MySQLError as err:
        print(f"Error: {err}")

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")
    cursor.close()

def insert_data(conn, name, address):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", (name, address))
    conn.commit()
    cursor.close()

def select_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()
    cursor.close()
    return result

def main():
    create_database()
    conn = connect()
    if conn is None:
        return

    create_table(conn)
    insert_data(conn, "John", "Highway 21")
    insert_data(conn, "Peter", "Lowstreet 4")
    insert_data(conn, "Amy", "Apple st 652")
    insert_data(conn, "Hannah", "Mountain 21")
    insert_data(conn, "Michael", "Valley 345")
    result = select_data(conn)
    for row in result:
        print(row)

    conn.close()

if __name__ == "__main__":
    main()