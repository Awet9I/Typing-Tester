# test_calculator.py
import sys

sys.path.append("..")
from calculator import calc


def test_calculator_with_same_text():
    # Test when user input and saved text are the same
    user_input = "This is a test."
    saved_text = "This is a test."

    result = calc.calculate_jaccard_similarity(user_input, saved_text)

    # The Jaccard similarity of the same text should be 100%
    assert result == 100.0


def test_calculator_with_different_text():
    # Test when user input and saved text are different
    user_input = "This is a test."
    saved_text = "this is a test."

    result = calc.calculate_jaccard_similarity(user_input, saved_text)

    # The Jaccard similarity of different text should be less than 100%
    assert result == 60.0


def test_calculator_with_empty_text():
    # Test when one of the texts is empty
    user_input = "This is a test."
    saved_text = ""

    result = calc.calculate_jaccard_similarity(user_input, saved_text)

    # The Jaccard similarity with an empty text should be 0%
    assert result == 0.0


# Add more test cases as needed
