import sqlite3
import main as gen
import random
from threading import Thread
import multiprocessing
from pymemcache.client import base


# create db connection
def create_connection(dbfile):
    conn = None
    try:
        conn = sqlite3.connect(dbfile)
    except ConnectionError as e:
        print(e)

    return conn


# Insert data to database query
def create_text(conn, text, text_len):
    cur = conn.cursor()
    sql = """ INSERT INTO Text(text,length)
              VALUES(?,?) """

    cur = conn.cursor()
    cur.execute(sql, [text, text_len])
    conn.commit()

    # lastrowid attribute of the Cursor object to return the generated
    return cur.lastrowid


# insert data
def insert_text(result_queue):
    database = r"C:\Users\awet0\OneDrive\ACIT\ACIT4420-1 23H Problem-solving with scripting\Project\TypingTester\tutorial.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        data = gen.filtered_text
        text_len = len(data.encode("utf-8"))
        text_id = create_text(conn, data, text_len)
        print(text_id)
        result_queue.put("Text generation and insertion complete")
        return text_id


# fetch data
def db_query():
    # everytime you query a text from the db, inser a new text. but it should run in the background
    # insert_text()
    text = {}
    print("Starting background task...")
    result_queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=insert_text, args=(result_queue,))
    process.start()
    print("Main thread is carrying on...")
    random_id = random.randint(1, 4)

    database = r"C:\Users\awet0\OneDrive\ACIT\ACIT4420-1 23H Problem-solving with scripting\Project\TypingTester\tutorial.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        sql = f"SELECT text FROM Text WHERE rowid={random_id}"
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        data = cur.fetchall()

        text[random_id] = data

    return text


def main():
    client = base.Client(("localhost", 11211))

    data = db_query()
    key = str(list(data.keys())[0])
    values = list(data.values())[0]
    # Convert the list of values to a string representation
    value_str = " ".join(map(str, values))

    # Encode the value as UTF-8 bytes
    value_bytes = value_str.encode("utf-8")
    client.set(key, value_bytes)

    print(client.get(key))


if __name__ == "__main__":
    main()
