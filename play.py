import sys

# setting path
# sys.path.append("..")

from DAL import loader


play = True
session_data = []
phrases = ["summer flower", "work hard"]


def input_handler():
    global play
    print("Choose Phrase to generate text!")
    while play:
        user_input = input()
        if user_input == "Q":
            play = False
        else:
            found = user_input in phrases
            if found:
                for data in session_data:
                    key, value = list(data.items())[0]
                    if value[1] == user_input:
                        print(value[0])


def main():
    global play
    global session_data

    while play:
        session_data = loader.fetch_data()
        print("Welcome to Typing Test!")
        if len(session_data) == 0:
            phrase = input("Choose Phrase!")
            word_count = input("Choose number of words")
            res = loader.insert_data(phrase, word_count)
            if res:
                print("Data added")
            else:
                print("Something went wrong data not added!")

        else:
            input_handler()


if __name__ == "__main__":
    main()
