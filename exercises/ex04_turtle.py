"""EX04 - Swimming in a waterfall."""

__author__ = "730394746"

from random import randint
from turtle import Turtle, colormode, done
colormode(255)


def grass(b: Turtle, x: float, y: float) -> None:
    """Makes triangles based on given starting point to become grass."""
    b.color("green")
    b.penup()
    b.goto(x, y)
    b.pendown()
    b.begin_fill()
    # [b.forward(230), b.left(90), b.forward(193), b.left(130), b.forward(300), b.right(130)]
    if x >= 0:  # Triangle is created based on which side of the origin it is placed
        b.right(50)
        b.forward(300)
        b.left(140)
        b.forward(230)
        b.left(90)
        b.forward(193)
        b.left(130)
        b.forward(300)
        b.right(130)
    else:
        b.left(50)
        b.forward(300)
        b.right(140)
        b.forward(230)
        b.right(90)
        b.forward(193)
        b.right(130)
        b.forward(300)
        b.left(130)
    b.end_fill()


def rectangle(r: Turtle, side_one: int, side_two: int, x: float, y: float, color: str) -> None:
    """Draws a rectangle based on requested color and size at specified location."""
    r.color(color)
    r.penup()
    r.goto(x, y)
    r.pendown()
    r.begin_fill()
    i = 0
    while i < 4:
        if i % 2 == 0:
            r.forward(side_one)
        else:
            r.forward(side_two)
        r.left(90)
        i += 1
    r.end_fill()


def mountains(m: Turtle, x_start: int, x_end: int, y: float, number: int) -> None:
    """Draws requested number of mountains randomly within a range of x and at a specific y."""
    m.color("purple")
    iii = 0
    while iii < number:
        m.penup()
        m.goto(randint(x_start, x_end), y)
        m.pendown()
        m.begin_fill()
        iiii = 0
        while iiii < 3:
            m.forward(40)
            m.left(120)
            iiii += 1
        # m.left(15)
        iii += 1
        m.end_fill()


def clouds(c: Turtle, x: int, y_start: int, y_end: int, number: int) -> None:
    """Inserts select number of clouds randomly sized randomly within a certain area."""
    c.color("black")
    size: list[int] = [5, 10, 20]  # Used to randomly size the cloud by inserting a random size puff. Allows for variety within the clouds placed
    aa = 0
    c. left(90)
    while aa < number:
        c.penup()
        c.goto((x + 120), randint(y_start, y_end))  # Helps space out the clouds so they are randomly placed but still evently distributed throughout the sky
        x += 120
        c.pendown()
        a = 0
        while a < randint(3, 5):
            c.circle(size[randint(0, 2)], 180)
            c.left(180)
            a += 1
        aa += 1


def turtles(tu: Turtle, color: str, x_start: int, x_end: int, y_start: int, y_end: int) -> None:
    """Inserts turtles with specific colored masks (heads) in a certain area."""
    tu.pencolor("black")
    tu.penup()
    tu.goto(randint(x_start, x_end), randint(y_start, y_end))
    tu.pendown()
    tu.fillcolor("green")
    tu.begin_fill()
    tu.circle(18, 360)
    tu.end_fill()
    tu.left(180)
    tu.fillcolor(color)
    tu.begin_fill()
    tu.circle(5, 360)
    tu.end_fill()
    tu.left(215)
    side_length: float = 20.0
    i = 0
    while (i < 25):
        side_length *= 0.93
        tu.forward(side_length)
        tu.left(60)
        i += 1


def main() -> None:
    """Main loop that combines all the components and creates a scenery with a waterfall, mountains, clouds, and turtles swimming in the water."""
    bob: Turtle = Turtle()
    rectangle(bob, 485, 230, -243, -230, "blue")
    grass(bob, 50, 0)
    grass(bob, -50, 0)
    rectangle(bob, 486, 95, -243, 0, "brown")
    rectangle(bob, 100, 95, -50, 0, "blue")
    mountains(bob, -243, 200, 95, 20)
    clouds(bob, -243, 120, 180, 4)
    i = 0
    while i < 4:
        bob.right(90)
        turtles(bob, color[i], -80, 80, -170, -30)
        i += 1
    done()


color: list[str] = ["red", "blue", "purple", "orange"]  # Used to assign various colors to the heads of the turtles to resemble the different colored masks of the ninja turtles

if __name__ == "__main__":  # Allows for program to run as a module and import into other modules 
    main()  