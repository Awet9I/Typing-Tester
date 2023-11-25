import sys

sys.path.append("../plotter.py")

import pytest
from plotter import plot_results
import matplotlib.pyplot as plt

# Sample data that mimics the expected structure
valid_data = [
    {"1": ["work hard", "50", "80", "3"]},
    {"2": ["work smart", "100", "100", "5"]},
    {"3": ["work smart", "300", "70", "70"]},
]


# Test with valid data
def test_plot_results_with_valid_data():
    try:
        plot_results(valid_data)
        assert True  # Test passes if no exception is raised
    except Exception:
        assert False  # Test fails if any exception is raised


# Test with empty data
def test_plot_results_with_empty_data(capsys):
    plot_results([])
    captured = capsys.readouterr()
    assert captured.out.strip() == "No result to plot!"


# Test with invalid data structure
def test_plot_results_with_invalid_data():
    with pytest.raises(TypeError):  # Assuming TypeError for this example
        plot_results({["not", "valid", "data"]})


# Optional: Test with no data (None)
def test_plot_results_with_no_data(capsys):
    plot_results(None)
    captured = capsys.readouterr()
    assert captured.out.strip() == "No result to plot!"
