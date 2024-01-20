from turtle import Screen
from player import Player
from score_board import ScoreBoard
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=650)
screen.tracer(0)

timmy = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(timmy.go_up, "Up")

screen.onkey(timmy.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision car with player
    for car in car_manager.all_cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect Success Of player
    if timmy.is_at_finish_line():
        timmy.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
