from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)
    
def move_back():
    turtle.back(10)

def turn_left():
    turtle.left(10)
    
def turn_right():
    turtle.right(10)
    
def start_etch_sketch():
    screen.onkey(move_forward, "Up")
    screen.onkey(move_back, "Down")
    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")
    screen.onkey(turn_right, "Right")
    screen.onkey(screen.reset, "c")

    screen.listen()
    
start_etch_sketch()

screen.exitonclick()