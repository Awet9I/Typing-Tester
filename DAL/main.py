import json
from transformers import pipeline
import string

# Load the GPT-2 model pipeline
model = pipeline("text-generation", model="gpt2")


# Function to filter out unwanted characters
def filter_text(text):
    # Define a string containing all valid letters
    valid_letters = (
        string.ascii_letters + "," + "'" + "?" + "-" + "*" + "!" + ";" + "()" + '""'
    )

    # Split the text into words
    words = text.split()

    # Filter the text to keep only valid letters and spaces
    filtered_words = []
    for word in words:
        filtered_word = "".join(
            # also adds space after every period (.), but this sometimes causes a problem
            char if char in valid_letters else char.replace(".", ". ")
            for char in word
        )
        filtered_words.append(filtered_word)

    filtered_text = " ".join(filtered_words)
    return filtered_text


generated_text = ""
# 300 is number of words
while len(generated_text) < 300:  # Adjust max_length as needed
    # Generate text
    sentence = model(
        "Work hard" + generated_text,
        do_sample=True,
        top_k=50,
        temperature=0.9,
        max_length=300 - len(generated_text),  # Adjust max_length
    )

    if len(sentence) == 0:
        # print(sentence)
        break

    generated_text += sentence[0]["generated_text"]

# numbers to exclude by filter
numbers_to_exclude = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
filtered_text = filter_text(generated_text)
for number in numbers_to_exclude:
    filtered_text = filtered_text.replace(number, "")


# print(filtered_text)
with open("../test1.txt", "a", encoding="utf8") as file:
    file.write(json.dumps(filtered_text) + "\n")


with open("../test1.txt", "r", encoding="utf8") as file:
    for line in file:
        data = json.loads(line)

# print(data)
