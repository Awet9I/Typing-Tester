import sys
from calculator import calc
from DAL import loader


def extract_phrases(session_data):
    return [value[1] for data in session_data for key, value in data.items()]


def final_result_calculator(test_text):
    res = calc.calculator(test_text)
    time_elapsed, accuracy = list(res.items())[0]
    minute = time_elapsed / 60
    remaining_seconds = time_elapsed % 60

    time_units = [("minute", minute), ("second", remaining_seconds)]
    time_units = [(unit, round(value)) for unit, value in time_units if value >= 1]

    time_str = " ".join(
        f"{value} {unit + 's'*(value != 1)}" for unit, value in time_units
    )

    print(f"\n ### Your accuracy is {accuracy}% and your time is {time_str} ###\n")


def handle_user_input(phrases, session_data, word_counts):
    while True:
        print("####### Choose Phrase to generate text! ####### \n")
        for item in phrases:
            print(f"[{item}]")
        user_input = input("\nType your choice: ").strip()

        if user_input.upper() == "Q":
            break
        elif user_input == "S":
            print("\nsaving to file")
        elif user_input in phrases:
            print(f"\n {word_counts}")
            word_count = input("\nChoose number of words to generate: ").strip()
            data = next(
                (
                    value[0]
                    for data in session_data
                    for key, value in data.items()
                    if value[1] == user_input and value[2] == word_count
                ),
                None,
            )

            if data:
                print("\n### Start typing and press Enter when you finish ###\n")
                test_text = data
                print(f"\n{test_text}\n")
                final_result_calculator(test_text)
            else:
                print(
                    f"\n####### No text found for phrase '{user_input}' with word count '{word_count}' #######\n"
                )
                generate_text = input(
                    f"Do you want to generate text for '{user_input}' with a different word count? (Y/N): "
                ).strip()

                if generate_text.upper() == "Y":
                    is_gen = loader.insert_data(user_input, word_count)

                    if is_gen:
                        session_data.append(is_gen)
                        key, value = list(is_gen.items())[0]
                        test_text = value[0]
                        print(f"\n{test_text}\n")
                        final_result_calculator(test_text)
                    else:
                        print("\n####### Text is not generated #######\n")
                else:
                    print("\n####### Text generation canceled #######\n")
        else:
            print("\n####### There is no text by this phrase #######\n")
            phrases.append(user_input)
            word_count = input(
                "If you like to generate new text, choose the number of words to generate by this phrase: "
            ).strip()
            is_gen = loader.insert_data(user_input, word_count)
            if is_gen:
                session_data.append(is_gen)
                key, value = list(is_gen.items())[0]
                test_text = value[0]
                print(f"\n{test_text}\n")
                final_result_calculator(test_text)
            else:
                print("\n####### Text is not generated #######\n")


def main():
    print(
        "\n######################## Welcome to Typing Tester! ###########################\n"
    )
    print("                 ####### Enter 'Q' to quit the test #######\n")

    play = True
    phrases = []
    session_data = []
    word_counts = ["10", "50", "100", "200", "300"]
    while play:
        session_data = loader.fetch_data()
        phrases = extract_phrases(session_data)

        if not session_data:
            print("                 ####### Choose Phrase to generate text ####### \n")
            if phrases:
                for item in phrases:
                    print(f"[{item}]")
            else:
                print(
                    "\n#### You don't have saved phrases, choose any phrase such as 'python is fun' ###\n"
                )

            user_input = input("\nType your choice: ").strip()

            if user_input.upper() == "Q":
                play = False
                break

            phrases.append(user_input)
            print(f"\n {word_counts}")
            word_count = input("\nChoose number of words!: ").strip()

            if word_count == "Q":
                play = False
                break

            res = loader.insert_data(user_input, word_count)

            if res:
                session_data.append(res)
                key, value = list(res.items())[0]
                test_text = value[0]
                print(f"\n{test_text}\n")
                final_result_calculator(test_text)
            else:
                print("### Something went wrong, data not added! ### \n")
        else:
            handle_user_input(phrases, session_data, word_counts)


if __name__ == "__main__":
    main()
