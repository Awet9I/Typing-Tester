import pytest
import sys

sys.path.append("..")
from Text_Generator import text_generator as gen
from transformers import pipeline

model = pipeline("text-generation", model="gpt2")


# Define the test function
@pytest.mark.parametrize(
    "input_param1, input_param2",
    [
        ("Input value ", "10"),
    ],
)
def test_generator(input_param1, input_param2):
    generated_text = gen.generator(input_param1, input_param2)
    assert generated_text.strip() != ""


@pytest.mark.parametrize(
    "input_param1, expected_output",
    [
        ("Input value 1", "Input value "),
        ("Input value @", "Input value "),
        # Add more test cases if needed
    ],
)
def test_text_filter(input_param1, expected_output):
    filtered_text = gen.filter_text(input_param1)
    assert filtered_text == expected_output
