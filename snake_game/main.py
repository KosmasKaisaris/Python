from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
       food.refresh()
       snake.extend()
       scoreboard.increase_score()


    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()




  #
  # #Detect collision with food
  #   if snake.head.distance(food) < 15:
  #      food.refresh()
  #      snake.extend()
  #      scoreboard.increase_score()
  #
  #
  #   # Detect collision with wall
  #   if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
  #       game_is_on = False
  #       scoreboard.game_over()
  #
  #   # Detect collision with tail
  #   for segment in snake.segments:
  #       if segment == snake.head:
  #           pass
  #       elif snake.head.distance(segment) < 10:
  #           game_is_on = False
            scoreboard.game_over()


# square1 = Turtle(shape="square")
# square1.color("white")
# square2 = Turtle(shape="square")
# square2.color("white")
# square2.goto(x=-20, y=0)
# square3 = Turtle(shape="square")
# square3.color("white")
# square3.goto(x=-40, y=0)


screen.exitonclick()