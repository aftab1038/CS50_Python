import turtle
import pandas

def setup_screen():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    gif_shape = "blank_states_img.gif"
    screen.addshape(gif_shape)
    turtle.shape(gif_shape)
    return screen

def setup_turtle():
    typer_turtle = turtle.Turtle()
    typer_turtle.penup()
    typer_turtle.hideturtle()
    return typer_turtle

def get_state_coordinates(state_name, states_data):
    state_data = states_data[states_data.state == state_name]
    x_cor = int(state_data["x"])
    y_cor = int(state_data["y"])
    return x_cor, y_cor

def save_missing_states(state_list, correct_guesses):
    missing_states = [state for state in state_list if state not in correct_guesses]
    missing_states_dict = {"missing_state": missing_states}
    missing_states_df = pandas.DataFrame(missing_states_dict)
    missing_states_df.to_csv("missing_states.csv")

def play_game(states_data, state_list):
    screen = setup_screen()
    typer_turtle = setup_turtle()
    correct_guesses = []
    score = 0

    while score < 50:
        guess_state_popup = screen.textinput(
            title=f"Guess the State ({score}/50)",
            prompt="What's another state's name?"
        )

        if guess_state_popup.title() == "Exit":
            break

        if guess_state_popup.title() in state_list and guess_state_popup.title() not in correct_guesses:
            x_cor, y_cor = get_state_coordinates(guess_state_popup.title(), states_data)
            typer_turtle.goto(x_cor, y_cor)
            typer_turtle.pendown()
            typer_turtle.write(guess_state_popup.title())
            typer_turtle.penup()
            correct_guesses.append(guess_state_popup.title())
            score += 1

    save_missing_states(state_list, correct_guesses)
    screen.exitonclick()

def main():
    states_data = pandas.read_csv("50_states.csv")
    state_list = states_data["state"].to_list()
    play_game(states_data, state_list)

if __name__ == "__main__":
    main()
