"""import sqlite3


    try:
        conn = sqlite3.connect("text_storage.db")
    except ConnectionError as e:
        print(e)


    cur = conn.cursor()
    table_name = "Text"
    check_table_query = (
        f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
    )
    cur.execute(check_table_query)

    result = cur.fetchone()
    print(result)"""


    # key_bytes = key_str.encode("utf-8")

    # Convert the list of values to a string representation
    # value_str = " ".join(map(str, value))

""" client = base.Client(("localhost", 11211))
    value_bytes = value.encode("utf-8")
        client.set(key_str, value_bytes)

        res = client.get("1")
        encoding = "utf-8"
        decoded = res.decode(encoding)
        words = decoded.split()
        filtered_words = []
        for word in words:
            filtered_word = "".join(char for char in word if char != " ")
            filtered_words.append(filtered_word)
        filtered_text = " ".join(filtered_words)
        # Encode the value as UTF-8 bytes

        print(filtered_text)
"""
"""def insert_text_process(phrase, word_count):
        database = r"C:\Users\awet0\OneDrive\ACIT\ACIT4420-1 23H Problem-solving with scripting\Project\TypingTester\text_storage.db"

        # create a database connection
        conn = create_connection(database)
        with conn:
            result_queue = multiprocessing.Queue()
            process = multiprocessing.Process(target=generator, args=(result_queue,))
            process.start()
            # create a new project
            data = generator(phrase, word_count)
            # text_len = len(data.encode("utf-8"))
            text_id = insert_text_data(conn, data, phrase, word_count)
            # print(text_id)
            # result_queue.put("Text generation and insertion complete")
            return text_id"""

"""
    for key, value, phrase, word_count in obj.items():
                text = {}
                key_str = str(key)
                text[key_str] = [value, phrase, word_count]

        with open("../test1.txt", "a", encoding="utf8") as file:
            file.write(json.dumps(all_data) + "\n")

        # Create an empty list to store the dictionaries
        data_list = []
        with open("../test1.txt", "r", encoding="utf8") as file:
            for line in file:
                data = json.loads(line)
                data_list.append(data)
                
                



                import time
import sys

# Initialize a variable to store the start time
start_time = None

# Initialize a variable to set the timeout (in seconds)
timeout_seconds = 2  # Adjust this value as needed

# Record the start time when the user starts typing
# input("Start typing when ready...")  # Prompt the user to start typing
start_time = time.time()

# Capture user input as a complete line
user_input = ""
while True:
    line = sys.stdin.readline()  # Read a complete line

    if not line:  # Check for EOF (End of File)
        break

    user_input += line
    time_elapsed = time.time() - start_time
    # Check for a timeout (no input for the specified time)
    if time_elapsed > timeout_seconds:
        print("User has finished typing.")
        break

print(f"User input: {user_input}")
print(f"User input: {time_elapsed:.2f}")
            
                
                
                """