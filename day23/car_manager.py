from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self) -> None:
        pass
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.setheading(180)
        car.goto(280, random.randint(-250, 250))
        car.color(random.choice(COLORS))
        self.cars.append(car)

    def increase_speed(self):
        self.cars_speed += 5

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - self.cars_speed, car.ycor())

            if car.xcor() < - 280:
                car.hideturtle()
                self.cars.remove(car)

    def colided(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True
        
        return False


