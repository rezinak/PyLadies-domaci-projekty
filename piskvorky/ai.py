
from random import randrange
pole = "-" * 20

def tahni (pole, cislo_policka, symbol):
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]

def tah_pocitace(pole, symbol='o'):
    tahy = ["a-a", "-aa", "aa-", "b-b", "-bb", "bb-", "-b-", "a--", "--a"]
    strategie = []

    if symbol == 'x':
        oponent = 'o'
    else:
        oponent = 'x'

    for tah in tahy:
        tah = tah.replace('a', symbol)
        tah = tah.replace('b', oponent)
        strategie.append(tah)

    while True:
        hledame = None
        for k in strategie:
            if k in pole:
                hledame = k
                break

        if hledame:
            vybrana_pozice = pole.index(hledame) + hledame.index("-")
        else:
            vybrana_pozice = randrange(20)

        if pole[vybrana_pozice] == '-':
            return tahni(pole, vybrana_pozice, symbol)
