import random
from turtle import Turtle, Screen

is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput("Make a bet!", "Which turtle will win the race? Choose a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

# finish line
finish_line = Turtle("square")
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(230, 0)
finish_line.showturtle()
finish_line.shapesize(12, .4)

# Turtle 1: Kleon: red
# Turtle 2: Manmak: purple
# Turtle 3: Babak: blue
# Turtle 4: Jaxcor: orange
# Turtle 5: Beeeeeeeeeee: yellow
# Turtle 6: Kaey: green

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_input:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_game_on = False
            # returns the color of the turtle?
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_input:
                print(f"You've won! The {winning_turtle} turtle won the race!")
            else:
                print(f"You've lost! The {winning_turtle} turtle won the race!")
        random_num = random.randint(0, 10)
        turtle.forward(random_num)


screen.exitonclick()

