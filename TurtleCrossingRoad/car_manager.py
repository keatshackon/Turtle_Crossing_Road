from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
COLORS = ["Black", "red", "orange", "purple", "blue", "green"]


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y_cor = random.randint(-250, 250)
            new_car.goto(300, random_y_cor)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
