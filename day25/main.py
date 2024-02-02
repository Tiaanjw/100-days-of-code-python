import pandas
from turtle import Turtle, Screen, shape

image = "blank_states_img.gif"
screen = Screen()
screen.setup(height=491, width=725)
screen.title("U.S States Game")
screen.addshape(image)
shape(image)

states_data = pandas.read_csv("50_states.csv")

def show_state(state, x, y):
    turtle = Turtle()
    turtle.penup()
    turtle.hideturtle()
    turtle.color("black")
    turtle.goto(x, y)
    turtle.write(state)

states_guessed = []

while len(states_guessed) < states_data.count().iloc[0]:
    user_input = screen.textinput(f"Guess the state ({len(states_guessed)}/{states_data.count().iloc[0]})", "What's another state name?")

    if user_input is None:
        missing_states = []
        for state in states_data.state:
            if state not in states_guessed:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        exit()
    user_input = user_input.lower()

    states_list = states_data.state.str.lower().to_list()

    if user_input in states_list:
        state_data = states_data[states_data.state.str.lower() == user_input]
        show_state(str(state_data.state.values[0]), state_data.x.iloc[0], state_data.y.iloc[0])

        if user_input not in states_guessed:
            states_guessed.append(state_data.state.values[0])


screen.exitonclick()
