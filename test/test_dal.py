from unittest.mock import patch, Mock
import sys

sys.path.append("..")
from DAL import loader


@patch("DAL.dbquery.insert_text_data")
def test_insert_data_with_mock_data(mock_insert_data):
    # Define mock data
    mock_data = {"1": ["mock_text", "mock_phrase", "50"]}

    # Set up the mock behavior of insert_text_data
    mock_insert_data.return_value = mock_data

    # Call the insert_data function
    result = loader.insert_data("mock_phrase", 50)

    # Assert that the result matches the mock data
    assert result == mock_data


@patch("DAL.dbquery.db_query_all")
def test_fetch_data_with_mock_data(mock_db_query_all):
    # Define mock database results
    mock_data = [{"1": ["mock_text", "mock_phrase", "50"]}]

    # Set up the mock behavior of db_query_all
    mock_db_query_all.return_value = mock_data

    # Call the fetch_data function
    result = loader.fetch_data()

    # Assert that the result matches the mock data
    assert result == mock_data
