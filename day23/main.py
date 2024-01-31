import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

DIFFICULTY = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
carmanager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if random.randint(0, 10) < DIFFICULTY:
        carmanager.spawn_car()

    carmanager.move_cars()

    if player.ycor() > 280:
        player.reset_player()
        scoreboard.level_up()
        carmanager.increase_speed()

    if carmanager.colided(player):
        game_is_on = False
        scoreboard.show_game_over()
    
screen.exitonclick()
        
