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


# Insert data to database query
def create_table(conn, phrase, word_count):
    sql_create_text_table = """ CREATE TABLE IF NOT EXISTS Text (
                                        text text NOT NULL,
                                        phrase text NOT NULL,
                                        wordCount text
                                    ); """

    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(sql_create_text_table)
            res = c.execute("SELECT name FROM sqlite_master")
            is_created = res.fetchone()
            if is_created:
                text = generator(phrase, word_count)
                sql = """ INSERT INTO Text(text,phrase,word_count)
                VALUES(?,?,?) """

                c.execute(sql, [text, phrase, word_count])
                conn.commit()

                # lastrowid attribute of the Cursor object to return the generated
                if c.lastrowid:
                    obj = {}
                    obj[c.lastrowid] = [text, phrase, word_count]
                    return obj

        except ConnectionError as e:
            print(e)


def insert_text_data(phrase, word_count):
    database = r"C:\Users\awet0\OneDrive\ACIT\ACIT4420-1 23H Problem-solving with scripting\Project\TypingTester\text_storage.db"
    # create a database connection
    conn = create_connection(database)
    cur = conn.cursor()
    with conn:
        cur = conn.cursor()
        table_name = "Text"
        check_table_query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
        cur.execute(check_table_query)

        result = cur.fetchone()
        if result:
            text = generator(phrase, word_count)
            sql = """ INSERT INTO Text(text,phrase,wordCount)
                VALUES(?,?,?) """

            cur.execute(sql, [text, phrase, word_count])
            conn.commit()

            # lastrowid attribute of the Cursor object to return the generated
            if cur.lastrowid:
                obj = {}
                obj[cur.lastrowid] = [text, phrase, word_count]
                return obj

        else:
            res = create_table(conn, phrase, word_count)
            return res


# fetch data
def db_query_all():
    database = r"C:\Users\awet0\OneDrive\ACIT\ACIT4420-1 23H Problem-solving with scripting\Project\TypingTester\text_storage.db"

    # create a database connection
    conn = create_connection(database)
    # everytime you query a text from the db, inser a new text. but it should run in the background
    # insert_text()

    all_text = []

    with conn:
        cur = conn.cursor()
        """table_name = "Text"
        check_table_query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
        cur.execute(check_table_query)

        result = cur.fetchone()
        if result:"""

        table_name = "Text"
        check_table_query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
        cur.execute(check_table_query)
        res = cur.fetchone()
        print(res)
        if res:
            # fetch with id includeded in the result
            sql = f"SELECT ROWID, * FROM Text"
            cur.execute(sql)

            conn.commit()
            data = cur.fetchall()
            # if data == []:
            # insert_text_data()
            for item in data:
                text = {}
                id_value, data_value, phrase, word_count = item
                text[id_value] = [data_value, phrase, word_count]
                all_text.append(text)
            return all_text
        else:
            return all_text
        # else:
        # create_table(conn)
        # insert_text_data()
