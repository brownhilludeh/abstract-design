import turtle
from turtle import *

# def flower():
#     pensize(2)
#     speed(10)
#     for i in range(150):
#         circle(190-i, 90)
#         left(90)
#         circle(190-i, 90)
#         left(45)

# flower()
# mainloop()

def flower():
    pensize(2)
    speed(100)
    bgcolor('yellow')
    color('red')
    for i in range(100):
        circle(140-i, 90)
        left(90)
        circle(120-i, 90)
        left(60)

flower()
# mainloop()
hideturtle()
