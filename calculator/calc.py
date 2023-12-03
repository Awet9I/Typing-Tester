import time
import sys
import math


def calculator(text):
    final_result = {}
    result = timer()
    time_elapsed, user_text = list(result.items())[0]
    # tokonized_user_input = user_text.split()
    # tokonized_text = text.split()
    accuracy = calculate_jaccard_similarity(user_text, text)
    final_result[time_elapsed] = round(accuracy)
    return final_result


def calculate_jaccard_similarity(user_input, saved_text):
    # Tokenize the input and saved text into words
    user_words = set(user_input.split())
    saved_words = set(saved_text.split())

    # Calculate Jaccard Similarity
    intersection = len(user_words.intersection(saved_words))
    union = len(user_words.union(saved_words))

    if union == 0:
        similarity = 0.0  # Handle the case of an empty set
        return 0
    else:
        similarity = intersection / union

    return similarity * 100.0  # Convert to percentage


def timer():
    result = {}
    # Initialize a variable to store the start time

    start_time = None

    # Initialize a variable to set the timeout (in seconds)
    timeout_seconds = 10

    # Record the start time when the user starts typing
    # input("Start typing when ready...")  # Prompt the user to start typing
    start_time = time.time()

    # Capture user input as a complete line
    user_input = ""
    while True:
        line = sys.stdin.readline()  # Read a complete line

        if not line:  # Check for EOF (End of File)
            break

        user_input += line
        time_elapsed = time.time() - start_time
        # Check for a timeout (no input for the specified time)
        if time_elapsed > timeout_seconds:
            time_re = round(time_elapsed, 2)
            text = line
            result[time_re] = text
            return result
