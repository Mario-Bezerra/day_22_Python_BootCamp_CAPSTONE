import time
from turtle import Screen
from player import Player
from car_factory import CarManager
from scoreboard import Scoreboard

# creating the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

# calling objects
player1 = Player()
car = CarManager()
level = Scoreboard()

# scree listening
screen.listen()
screen.onkey(player1.move_up,"Up")


# game on action
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for piece in car.all_cars:
        if player1.distance(piece) < 20 :
            game_is_on = False
            level.game_over()
    if player1.ycor() > 280:
        player1.back_to_origin()
        car.increase_speed()
        level.increase_level()


screen.exitonclick()
