from pymongo import MongoClient

def connect():
    try:
        conn = MongoClient("mongodb://localhost:27017/")
        print("Connected to MongoDB successfully!")
        return conn["mydatabase"]["customers"]
    except Exception as err:
        print(f"Error: {err}")
        return None




def insert_data(conn, name, address):
    try:
        conn.insert_one({"name": name, "address": address})
        print("Data inserted successfully!")
    except Exception as err:
        print(f"Error: {err}")

def select_data(conn):
    try:
        result = conn.find({}, {"_id": 0})
        return result
    except Exception as err:
        print(f"Error: {err}")
        return None
    
def main():
    conn = connect()
    if conn is None:
        return

    # insert_data(conn, "John", "Highway 21")
    # insert_data(conn, "Peter", "Lowstreet 4")
    # insert_data(conn, "Amy", "Apple st 652")
    # insert_data(conn, "Hannah", "Mountain 21")
    # insert_data(conn, "Michael", "Valley 345")
    result = select_data(conn)
    for row in result:
        print(row)
    
if __name__ == "__main__":
    main()