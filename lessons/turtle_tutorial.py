"""Learning to use turtle."""


from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.color(99, 204, 250)
leo.penup()
leo.goto(-100, -60)
leo.pendown()
leo.speed(10)
leo.hideturtle()

i: int = 0
side_length: float = 300.0
leo.begin_fill()
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i += 1
leo.end_fill()
i = 0


from turtle import Turtle, colormode, done
bob: Turtle = Turtle()
bob.color("black")
bob.penup()
bob.goto(-100, -60)
bob.pendown()
bob.speed(25)

while (i < 150):
    side_length *= 0.97
    bob.forward(side_length)
    bob.left(120.5)
    i += 1

quit()