import sys
import json

# setting path
# sys.path.append("")

# from dbquery import db_query_all, insert_text_data
from DAL import dbquery as db

all_data = []


# Function to clean the text within a dictionary
def clean_text_in_dict(dic):
    cleaned_dict = {}
    value_list = []
    key, value = list(dic.items())[0]
    for item in value:
        cleaned_value = item.replace(r"\"", '"')
        cleaned_value2 = cleaned_value.replace(r"\'", "'")
        value_list.append(cleaned_value2)
    cleaned_dict[key] = value_list
    return cleaned_dict


def insert_data(phrase, word_count):
    res = db.insert_text_data(phrase, word_count)
    if res:
        filtered_text = clean_text_in_dict(res)
        return filtered_text
    else:
        obj = {}
        return obj


def fetch_data():
    global all_data

    data = db.db_query_all()
    if len(data) == 0:
        return all_data
    # loop the list containing all data, return a dict object
    for obj in data:
        all_data.append(obj)

    cleaned_data_list = [clean_text_in_dict(dic) for dic in all_data]
    return cleaned_data_list

    # Now, cleaned_data_list contains all the dictionaries with cleaned text
    """for dic_item in cleaned_data_list:
        print(dic_item)
"""


"""
if __name__ == "__main__":
    main()"""


""" data = json.loads(line)
            str_dump = json.dumps(data)
            # Remove backslashes before double quotes
            filtered_text1 = str_dump.replace(r"\"", '"')

            # Remove backslashes before single quotes
            filtered_text = filtered_text1.replace(r"\'", "'")
            dic_item = json.loads(filtered_text)

            print(dic_item)
"""
