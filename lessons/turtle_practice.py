
# b: Turtle = Turtle()
# b.speed(100)
# b.color("green")
# b.penup()
# b.forward(50)
# b.pendown()
# b.begin_fill()
# b.right(50)
# b.forward(300)
# b.left(140)
# i = 0
# if i < 6:
#     order: list[None] = [b.forward(230), b.left(90), b.forward(193), b.left(130), b.forward(300), b.right(130)]
#     while i < 6:
#         order[i]
#         i += 1
#     b.end_fill()
#     b.forward(500)
    # b.begin_fill()
    # while i >= 0:
    #     order[i]
    #     i -= 1
    # b.end_fill()
# b.forward(230)
# b.left(90)
# b.forward(193)
# b.left(130)
# b.forward(300)
# b.right(130)

# b.begin_fill()
# b.right(130)
# b.forward(300)
# b.left(130)
# b.forward(193)
# b.left(90)
# b.forward(230)
# b.end_fill()

def trees(t: Turtle, number: int, x_one: int, x_two: int, y_one: int, y_two: int) -> None:
    """Inserts a certain number tress in a particular area."""
    # t: Turtle = Turtle()
    t.right(90)
    t.speed(100)
    ti = 0
    tii = 0
    while tii < number:
        if tii < number // 2:
            x = randint(-x_two, -x_one)
            y = randint(y_one, y_two)
        else:
            x = randint(x_one, x_two)
            y = randint(y_one, y_two)
        while ti < 2:
            t.color("brown")
            t.penup()
            t.goto(x, y)
            t.pendown()
            i = 0
            d: float = 5.0
            if ti % 2 == 0:
                t.left(90)
            else:
                t.left(260)
            t.forward(50)
            if ti % 2 == 0:
                t.left(100)
            else:
                t.right(100)
            while i < 25:
                t.color("black")
                d *= 1.05
                t.forward(d)
                if ti % 2 == 0:
                    t.left(170)
                else:
                    t.right(170)
                t.forward(0.9848 * d)
                if ti % 2 == 0:
                    t.right(170)
                else:
                    t.left(170)
                i += 1
            ti += 1
        t.left(10)
        tii += 1
        ti = 0


from turtle import Turtle, colormode, done
b: Turtle = Turtle()
b.color("green")
b.penup()
b.forward(50)
b.pendown()
b.begin_fill()
b.right(50)
b.forward(300)
b.left(140)
i = 0
if i < 6:
    order: list[None] = [b.forward(230), b.left(90), b.forward(193), b.left(130), b.forward(300), b.right(130)]
    while i < 6:
        order[i]
        i += 1
    b.end_fill()
    b.forward(500)
    order: list[None] = [b.right(130), b.forward(300), b.left(130), b.forward(193), b.left(90), b.forward(230)]
    i = 0
    b.begin_fill()
    while i < 6:
        order[i]
        i -= 1
    b.end_fill()
# t: Turtle = Turtle()
# t. speed(100)
# t.left(90)
# t.forward(200)
# t.left(100)
# i = 0
# d = 5
# while i < 50:
#     d *= 1.05
#     t.forward(d)
#     t.left(170)
#     t.forward(0.9848 * d)
#     t.right(170)
#     i += 1
# i = 0
# d = 5
# t.left(260)
# t.forward(190)
# t.right(100)
# while i < 50:
#     d *= 1.05
#     t.forward(d)
#     t.right(170)
#     t.forward(0.9848 * d)
#     t.left(170)
#     i += 1

from random import randint
c: Turtle = Turtle()
c.color("black")
size: list[int] = [5, 10, 20]
aa = 0
c. left(90)
while 0 < 3:
    c.penup()
    c.goto(randint(-250, 250), randint(110, 150))
    c.pendown()
    a = 0
    while a < randint(4, 6):
        c.circle(size[randint(0, 2)], 180)
        c.left(180)
        a += 1

# m: Turtle = Turtle()
# iii = 0
# while iii < 3:
#     m.penup()
#     m.goto(randint(-250, 250), 95)
#     m.pendown()
#     iiii = 0
#     while iiii < 3:
#         m.forward(40)
#         m.left(120)
#         iiii += 1
#     # m.left(15)
#     iii += 1

# b: Turtle = Turtle()
# b.penup()
# b.forward(50)
# b.pendown()
# b.right(50)
# b.forward(300)
# b.left(140)
# b.forward(230)
# b.left(90)
# b.forward(193)
# b.left(130)
# b.forward(300)
# b.right(130)
# b.forward(500)
# b.right(130)
# b.forward(300)
# b.left(130)
# b.forward(193)
# b.left(90)
# b.forward(230)
# b.right(180)
# b.forward(325)
# b.right(90)
# b.forward(500)
# b.right(90)
# b.forward(95)
# b.right(90)
# b.forward(193)
# b.right(90)
# b.forward(95)
# b.left(90)
# b.forward(115)
# b.left(90)
# b.forward(95)

# m: Turtle = Turtle()
# m.goto(0, 0)
# m.forward(40)
# m.left(120)
# m.forward(40)
# m.left(120)
# m.forward(40)
# m.left(135)

# c: Turtle = Turtle()
# c. left(90)
# c.circle(10, 180)
# c.left(180)
# c.circle(20, 180)
# c.left(180)
# c.circle(10, 180)
# c.left(180)
# c.circle(5, 180)


# tu: Turtle = Turtle()
# tu.circle(18, 360)
# tu.left(180)
# tu.circle(5, 360)
# tu.left(215)
# side_length = 20
# i = 0
# while (i < 25):
#     side_length *= 0.93
#     tu.forward(side_length)
#     tu.left(60)
#     i += 1

done()