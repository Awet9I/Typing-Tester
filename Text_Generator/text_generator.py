import json
from transformers import pipeline
import string
from num2words import num2words
import re
import time


# Function to filter out unwanted characters
def filter_text(text):
    pattern = r"\d+"

    # Define a string containing all valid letters
    valid_letters = (
        string.ascii_letters + "," + "'" + "?" + "-" + "*" + "!" + ";" + "()" + '""'
    )

    # Split the text into words
    words = text.split()
    # char if char in valid_letters else char.replace(".", ". ")for char in word
    # Filter the text to keep only valid letters and spaces
    filtered_words = []
    for word in words:
        filtered_word = "".join(char for char in word if char in valid_letters)

        number = re.match(pattern, filtered_word)
        if number:
            in_word = num2words(number)
            filtered_word.replace(number, in_word)
        filtered_words.append(filtered_word)
    filtered_text = " ".join(filtered_words)
    return filtered_text


def generator(phrase: str, num_word):
    phrase_cap = phrase.capitalize()
    # start = time.time()
    # Load the GPT-2 model pipeline
    model = pipeline("text-generation", model="gpt2")
    generated_text = ""
    # num_word is number of words to generate
    while len(generated_text) < num_word:  # control loop with number of words
        # Generate text
        sentence = model(
            phrase_cap + generated_text,
            do_sample=True,
            top_k=50,
            temperature=0.9,
            max_length=num_word - len(generated_text),  # Adjust max_length
        )

        if len(sentence) == 0:
            break

        generated_text += sentence[0]["generated_text"]
        # end = time.time()
        # tootal = end - start
        # print(tootal)

    filtered_text = filter_text(generated_text)

    return filtered_text


"""if __name__ == "__main__":
    generator("Sommer day", 50)
# print(filtered_text)
"""
