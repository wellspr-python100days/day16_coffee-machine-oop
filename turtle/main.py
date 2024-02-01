from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("goldenrod")
for _ in range(0, 4):
    t.forward(100)
    t.left(90)

screen = Screen()

print(screen.canvheight)
screen.exitonclick()