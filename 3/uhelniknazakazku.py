from turtle import forward, left, exitonclick

pocetstran = int(input("Zadej, kolik stran ma mit  viceuhelnik: "))
strana = 20
vnitrniuhel = 180*(1-2/pocetstran)
vnejsiuhel = 180 - vnitrniuhel

for uhelnik in range(pocetstran):
    forward(strana)
    left(vnejsiuhel)

exitonclick()
