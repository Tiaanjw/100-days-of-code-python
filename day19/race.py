from turtle import Turtle, Screen
import random

# turtle = Turtle()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
track_end = int(SCREEN_WIDTH / 2) - 20

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

def setup_turtles(colors):
    track_width = SCREEN_HEIGHT / 2
    lane_width = track_width / len(colors)
    start_lane = -abs(int(SCREEN_HEIGHT / 2)) + int((track_width / 2))
    start_x_coord = -abs(int(SCREEN_WIDTH / 2)) + 20
    for color in colors:
        start_lane += lane_width
        new_turtle = Turtle("turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(start_x_coord, start_lane)
        turtles.append(new_turtle)

def start_race():
    setup_turtles(colors)

    user_bet = screen.textinput(title="Make your bet",prompt=f"Which turtle will win the race ({', '.join(colors)})?")
    if user_bet:
        race_on = True

    while race_on:
        # print("race on")
        for turtle in turtles:
            print("Turtle")
            turtle.forward(random.randint(0, 10))
            x = turtle.position()[0]
            print(f"x = {x}")
            if x >= track_end:
                race_on = False
                winning_color = turtle.color()[0]

    if user_bet == winning_color:
        print(f"The winner is {winning_color}, you won the bet")
    else:
        print(f"The winner is {winning_color}, you lost the bet")


start_race()

screen.exitonclick()