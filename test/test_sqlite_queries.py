import sqlite3
from unittest.mock import Mock, patch
import pytest

# Candidat Number: 653
### Tests functions in dbquery module ####


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


@pytest.mark.parametrize(
    "query, expected_result",
    [
        (
            "SELECT * FROM Text",
            [
                {"1": ["mock_text", "mock_phrase", "50"]},
                {"2": ["mock_text2", "mock_phrase2", "50"]},
            ],
        ),
    ],
)
@patch("sqlite3.connect")
def test_execute_query(mock_connect, query, expected_result):
    # Create a mock SQLite connection
    mock_connection = Mock()
    mock_connect.return_value = mock_connection

    # Mock the cursor and fetchall method
    mock_cursor = mock_connection.cursor.return_value
    mock_cursor.fetchall.return_value = expected_result

    # Call the query function with the mock connection
    result = execute_query(mock_connection, query)

    # Assert that the query was executed correctly and the result is as expected
    assert result == expected_result
