import sys

# setting path
sys.path.append("..")

from Text_Generator.text_generator import generator
import sqlite3
import random
import multiprocessing


# create db connection
def create_connection(dbfile):
    conn = None
    try:
        conn = sqlite3.connect(dbfile)
    except ConnectionError as e:
        print(e)

    return conn


def insert_text_process(result_queue):
    database = r"C:\Users\awet0\OneDrive\ACIT\ACIT4420-1 23H Problem-solving with scripting\Project\TypingTester\text_storage.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        data = generator("Summer day", 300)
        text_len = len(data.encode("utf-8"))
        text_id = insert_text_data(conn, data, text_len)
        # print(text_id)
        result_queue.put("Text generation and insertion complete")
        return text_id


def insert_text_data(conn, text, text_len):
    cur = conn.cursor()
    sql = """ INSERT INTO Text(text,length)
              VALUES(?,?) """

    cur = conn.cursor()
    cur.execute(sql, [text, text_len])
    conn.commit()

    # lastrowid attribute of the Cursor object to return the generated
    return cur.lastrowid


# Insert data to database query
def create_table(conn):
    sql_create_text_table = """ CREATE TABLE IF NOT EXISTS Text (
                                        text text NOT NULL,
                                        length text
                                    ); """

    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(sql_create_text_table)
        except ConnectionError as e:
            print(e)


# fetch data
def db_query_all():
    database = r"C:\Users\awet0\OneDrive\ACIT\ACIT4420-1 23H Problem-solving with scripting\Project\TypingTester\text_storage.db"

    # create a database connection
    conn = create_connection(database)
    # everytime you query a text from the db, inser a new text. but it should run in the background
    # insert_text()

    text = {}

    result_queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=insert_text_process, args=(result_queue,))
    process.start()

    with conn:
        cur = conn.cursor()
        table_name = "Text"
        check_table_query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
        cur.execute(check_table_query)

        result = cur.fetchone()
        if result:
            sql = f"SELECT ROWID, * FROM Text"

            cur.execute(sql)

            conn.commit()
            data = cur.fetchall()
            if data == []:
                insert_text_process()
            for item in data:
                id_value, data_value, value_len = item
                text[id_value] = data_value
            return text
        else:
            create_table(conn)
            # insert_text_data()
