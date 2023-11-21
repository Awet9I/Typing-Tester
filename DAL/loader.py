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
    if len(data) != 0:
        # loop the list containing all data, return a dict object
        for obj in data:
            all_data.append(obj)

        cleaned_data_list = [clean_text_in_dict(dic) for dic in all_data]
        return cleaned_data_list
    return all_data


def drop_table():
    db.drop_table()
