from turtle import forward
from turtle import left
from turtle import exitonclick
from turtle import penup
from turtle import pendown
from math import sqrt

stranactverce = int(input("Zadej stranu ctverce: "))
def domek_o_strane(stranactverce):
    #CTVEREC
    for stranaCtverce in range(4):
        forward(stranactverce)
        left(-90)

    #STRECHA
    left(45)
    forward(sqrt(2)*stranactverce/2)
    left(-90)
    forward(sqrt(2)*stranactverce/2)

    #UHLOPRICKY
    left(-90)
    forward(sqrt(2)*stranactverce)

    penup()
    left(-135)
    forward(stranactverce)
    pendown()

    left(-135)
    forward(sqrt(2)*stranactverce)

    exitonclick()
domek_o_strane(stranactverce)
