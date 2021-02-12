import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Move the turtle with keypress
# Create and move the cars
# Detect collision with car
# Detect when turtle reaches the other side
# Create a Score Board

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Every code written inside the while loop will refresh every 0.1 second
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with car
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()


screen.exitonclick()