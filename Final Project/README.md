# U.S. States Game

This project is an interactive Python game that educates users about U.S. geography by challenging them to identify all 50 U.S. states. The game uses the Turtle graphics library to display a map, and the player is prompted to guess the names of the states. The game tracks correct guesses, displays the state names on the map, and keeps a list of any states the player misses.

## Video Demonstration

[Watch the Video](https://youtu.be/yi-SrrnkMgQ)

`Date: August 25, 2024`

## Project Description

### Overview

The U.S. States Game is designed to be an educational tool that makes learning U.S. geography engaging and fun. The game prompts players to guess the names of the states on a blank U.S. map. Correct guesses are marked on the map, and the player’s progress is tracked throughout the game.

### How the Game Works

1. **Interactive Map**: The game loads a blank map of the United States using Turtle graphics.
2. **User Interaction**: Players are prompted to type in the name of a state. If the input matches a state that hasn't been guessed yet, the state's name is displayed at its correct coordinates on the map.
3. **Score Tracking**: The game keeps count of how many states the player has correctly identified. The player's score is displayed in the game window's title bar.
4. **Exit and Summary**: If the player chooses to exit before identifying all 50 states, a CSV file is generated that lists the states they missed. This file allows the player to review and study the states they were unable to recall.

### Files Included

#### `main.py`

This is the main script of the project that controls the entire game. Here’s what this script does:

- **Setting Up the Game**:
  - The script begins by loading the map image (`blank_states_img.gif`) and setting it as the Turtle shape.
  - It loads the state data from a CSV file (`50_states.csv`), which includes the names of the states and their corresponding x and y coordinates on the map.
  
- **Game Loop**:
  - The script enters a loop where it continuously prompts the player to input the name of a state.
  - When a correct guess is made, the Turtle moves to the state’s coordinates and writes the state’s name on the map.
  - The player’s score increases with each correct guess.
  - If the player types "Exit," the game ends and exits the loop.

- **Saving Missing States**:
  - After the player exits the game, the script compares the list of guessed states with the full list of states.
  - It generates a list of states that were not guessed and saves this list in a new CSV file named `missing_states.csv`.

#### `50_states.csv`

This CSV file contains the data for all 50 U.S. states. It has three columns:

- **state**: The name of each state.
- **x**: The x-coordinate on the map where the state’s name should be displayed.
- **y**: The y-coordinate on the map where the state’s name should be displayed.

The coordinates are crucial for accurately placing the state names on the map when a correct guess is made.

#### `missing_states.csv`

This CSV file is generated by the game when the player exits. It contains a list of states that the player did not correctly identify during the game. This file has one column:

- **missing_state**: The name of each state that was missed.

This file serves as a study guide for the player, helping them to learn the states they were unable to recall during gameplay.

### Explanation of Functions in `main.py`

The `main.py` script is the core of the U.S. States Game, containing several functions that handle different aspects of the game. Below is a detailed explanation of each function in the script:

#### `1. setup_screen()`

**Purpose:**

- This function sets up the game screen using the Turtle graphics library.

**What it does:**

- Initializes a `Screen` object from the Turtle library.
- Sets the window title to "U.S. States Game".
- Loads a GIF image (`blank_states_img.gif`) that serves as the map background and sets it as the shape of the Turtle object.
- Returns the `Screen` object for further use in the game.

#### `2. setup_turtle()`

**Purpose:**

- This function sets up a Turtle object for writing the names of the states on the screen.

**What it does:**

- Creates a Turtle object named `typer_turtle`.
- Lifts the pen up so that the Turtle can move around without drawing lines (`penup()`).
- Hides the Turtle cursor using `hideturtle()` to make the text appear without the turtle icon.
- Returns the configured `Turtle` object for writing the state names.

#### `3. get_state_coordinates(state_name, states_data)`

**Purpose:**

- This function retrieves the x and y coordinates of a specific state from the dataset.

**What it does:**

- Filters the `states_data` DataFrame to find the row that matches the provided `state_name`.
- Extracts the x and y coordinates from the corresponding columns.
- Returns the coordinates as a tuple `(x_cor, y_cor)`.

#### `4. save_missing_states(state_list, correct_guesses)`

**Purpose:**

- This function saves the list of states that were not guessed by the player into a CSV file.

**What it does:**

- Compares the `state_list` (all states) with `correct_guesses` (states guessed by the player) to find the states - that were missed.
- Creates a dictionary with the missed states.
- Converts the dictionary into a DataFrame.
- Writes the DataFrame to a CSV file named `missing_states.csv`.

#### `5. play_game(states_data, state_list)`

**Purpose:**

- This function orchestrates the gameplay by continuously prompting the user to guess states until they either guess all 50 states or choose to exit.

**What it does:**

- Sets up the screen and turtle `using setup_screen()` and `setup_turtle().`
- Initializes the `correct_guesses` list to keep track of states that have been guessed and the `score` counter.
- Enters a loop where the player is prompted to guess a state name.
- If the player types "Exit," the loop breaks, ending the game.
- For each correct guess, the state’s name is displayed on the map at its corresponding coordinates, and the - score is incremented.
- Once the game ends, either by completion or by exit, the list of missed states is saved using - `save_missing_states()`.

#### `6. main()`

**Purpose:**

- This is the entry point of the program, responsible for loading the data and starting the game.

**What it does:**

- Loads the `50_states.csv` file into a DataFrame using pandas.
- Extracts the list of state names from the DataFrame.
- Calls the `play_game()` function to start the game, passing the states data and the list of state names.

### How to Run the Project

To run this project, ensure you have Python installed on your computer, along with the necessary libraries (Turtle and pandas). Follow these steps:

1. Download or clone the project repository.
2. Ensure all the files (`main.py`, `50_states.csv`, and `blank_states_img.gif`) are in the same directory.
3. Run the `main.py` script using a Python interpreter.
4. The game window will open, and you can start playing by typing in the names of U.S. states.