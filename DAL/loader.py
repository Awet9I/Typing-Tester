import sys
import json

# setting path
sys.path.append("..")

from dbquery import db_query_all


# Function to clean the text within a dictionary
def clean_text_in_dict(dic):
    cleaned_dict = {}
    for key, value in dic.items():
        cleaned_value = value.replace(r"\"", '"')
        cleaned_value2 = cleaned_value.replace(r"\'", "'")
        cleaned_dict[key] = cleaned_value2
    return cleaned_dict


def main():
    data = db_query_all()

    for key, value in data.items():
        text = {}
        key_str = str(key)
        text[key_str] = value

        with open("../test1.txt", "a", encoding="utf8") as file:
            file.write(json.dumps(text) + "\n")

    # Create an empty list to store the dictionaries
    data_list = []
    with open("../test1.txt", "r", encoding="utf8") as file:
        for line in file:
            data = json.loads(line)
            data_list.append(data)
    cleaned_data_list = [clean_text_in_dict(dic) for dic in data_list]

    # Now, cleaned_data_list contains all the dictionaries with cleaned text
    """for dic_item in cleaned_data_list:
        print(dic_item)
"""


if __name__ == "__main__":
    main()


""" data = json.loads(line)
            str_dump = json.dumps(data)
            # Remove backslashes before double quotes
            filtered_text1 = str_dump.replace(r"\"", '"')

            # Remove backslashes before single quotes
            filtered_text = filtered_text1.replace(r"\'", "'")
            dic_item = json.loads(filtered_text)

            print(dic_item)
"""
