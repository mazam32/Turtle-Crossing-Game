import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun= player.go_up, key= "Up")

game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.start_moving()
    for cars in car_manager.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    if player.is_at_finish_line():
        player.go_to_starting_position()
        car_manager.increase_speed()
        scoreboard.increase_level()
    
    time.sleep(0.1)
    screen.update()


screen.exitonclick()