import json
from transformers import pipeline
import string
from num2words import num2words
import re
import time

# Candidat Number: 653

######## Text generator module #########


# Function to filter out unwanted characters
def filter_text(text):
    pattern = r"\d+"
    try:
        # Define a string containing all valid letters
        valid_letters = (
            string.ascii_letters + "," + "'" + "?" + "-" + "*" + "!" + ";" + "()" + '""'
        )

        # Split the text into words
        words = text.split()
        # Filter the text to keep only valid letters and spaces
        filtered_words = []
        for word in words:
            number = re.match(pattern, word)
            if number:
                print(number.string)
                in_word = num2words(number.string)
                word = in_word

            filtered_word = "".join(char for char in word if char in valid_letters)

            filtered_words.append(filtered_word)
        filtered_text = " ".join(filtered_words)
        return filtered_text
    except (TypeError, ValueError, NameError) as e:
        print(e)


def generator(phrase: str, num_word):
    phrase_cap = phrase.capitalize()
    try:
        # Load the GPT-2 model pipeline
        model = pipeline("text-generation", model="gpt2")
        generated_text = ""
        # num_word is number of words to generate
        while len(generated_text) < int(num_word):  # control loop with number of words
            # Generate text
            sentence = model(
                phrase_cap + generated_text,
                do_sample=True,
                top_k=50,
                temperature=0.9,
                max_length=int(num_word) - len(generated_text),  # Adjust max_length
            )

            if len(sentence) == 0:
                break

            generated_text += sentence[0]["generated_text"]

        filtered_text = filter_text(generated_text)

        return filtered_text
    except ValueError as e:
        print(e)
