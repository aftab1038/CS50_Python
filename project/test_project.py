import pytest
from unittest.mock import patch
import pandas as pd
import project  

@pytest.fixture
def setup_states_data():
    data = {
        "state": ["California", "Texas", "New York"],
        "x": [100, 200, 300],
        "y": [100, 200, 300]
    }
    states_data = pd.DataFrame(data)
    state_list = ["California", "Texas", "New York"]
    return states_data, state_list

def test_get_state_coordinates(setup_states_data):
    states_data, _ = setup_states_data

    x, y = project.get_state_coordinates("California", states_data)
    assert (x, y) == (100, 100)

    x, y = project.get_state_coordinates("Texas", states_data)
    assert (x, y) == (200, 200)

@patch('project.turtle.Screen')
@patch('project.turtle.Turtle')
def test_play_game(mock_turtle, mock_screen, setup_states_data):
    states_data, state_list = setup_states_data

    mock_screen_instance = mock_screen.return_value
    mock_screen_instance.textinput.side_effect = ["California", "Texas", "Exit"]

    mock_turtle_instance = mock_turtle.return_value
    project.play_game(states_data, state_list)

    assert mock_turtle_instance.write.call_count == 2
    mock_screen_instance.textinput.assert_any_call(title="Guess the State (0/50)", prompt="What's another state's name?")
    mock_screen_instance.textinput.assert_any_call(title="Guess the State (1/50)", prompt="What's another state's name?")

def test_save_missing_states(tmpdir, setup_states_data):
    _, state_list = setup_states_data
    correct_guesses = ["California"]

    missing_states_csv = tmpdir.join("missing_states.csv")

    with patch("pandas.DataFrame.to_csv") as mock_to_csv:
        project.save_missing_states(state_list, correct_guesses)
        mock_to_csv.assert_called_once_with("missing_states.csv")

    project.save_missing_states(state_list, correct_guesses)

    missing_states_df = pd.read_csv("missing_states.csv", index_col=0)  
    expected_df = pd.DataFrame({"missing_state": ["Texas", "New York"]})

    pd.testing.assert_frame_equal(missing_states_df.reset_index(drop=True), expected_df)
