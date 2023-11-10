import sqlite3


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
print(result)


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
