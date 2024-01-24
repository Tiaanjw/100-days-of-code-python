from turtle import Turtle, Screen
import random
import colorgram

def set_random_color(turtle):
    R = random.random()
    G = random.random()
    B = random.random()
    turtle.color(R,G,B)

def draw_shapes(turtle):
    for angles in range(3,10):
        angles_degrees = 360/angles
        set_random_color(turtle)
        for _ in range(angles):
            turtle.forward(50)
            turtle.right(angles_degrees)

def draw_random_walk(turtle):    
    distance = 20
    
    turtle.pensize(5)
    for _ in range(100):
        angle = random.choice([0, 90, 180, 270])
        set_random_color(turtle)
        turtle.setheading(angle)
        turtle.forward(distance)
        
def draw_spirograph(turtle, size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        set_random_color(turtle)
        turtle.circle(100);
        turtle.setheading(turtle.heading() + size_of_gap)
        
def draw_hirst_painting(turtle, h_dots, v_dots):
    colors = colorgram.extract('spot_painting.png', 30)
    colors_list = []
    for color in colors:
        colors_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
    del colors_list[0:2]
    
    width = 400
    height = 400
    h_steps = int(height / h_dots)
    v_steps = int(width / v_dots)
    
    turtle.penup()
    turtle.hideturtle()
    turtle.pensize(10)
    
    for v_position in range(0, height, h_steps):
        for h_position in range(0, width, v_steps):
            turtle.color(random.choice(colors_list))
            turtle.setposition(h_position, v_position)
            turtle.dot()
    
timmy = Turtle()
timmy.shape("turtle")
timmy.speed(0)
screen = Screen()
screen.colormode(255)

# draw_shapes(timmy)
# draw_random_walk(timmy)
# draw_spirograph(timmy, 10)
draw_hirst_painting(timmy, 10, 10)

screen.exitonclick()