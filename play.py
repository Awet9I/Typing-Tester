import sys

# setting path
# sys.path.append("..")

from DAL import loader


play = True
session_data = []
phrases = ["summer flower", "work hard", "programing is fun"]


def input_handler():
    global play
    global session_data
    print("Choose Phrase to generate text!")
    while play:
        user_input = input()
        if user_input == "Q":
            play = False
        else:
            found = user_input in phrases
            if found:
                word_count = input("choose number of words to generate")
                for data in session_data:
                    key, value = list(data.items())[0]
                    if value[1] == user_input and value[2] == word_count:
                        print(value[0])

                print("There is no text by this phrase")
                word_count = input(
                    "choose the number of words to generate by this phrase"
                )
                is_gen = loader.insert_data(user_input, word_count)
                if is_gen:
                    session_data.append(is_gen)
                    key, value = list(is_gen.items())[0]
                    print(value[1])
                else:
                    print("text is not generated")


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
