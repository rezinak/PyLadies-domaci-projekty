# Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec

from random import randrange
from ai import tah_pocitace

pole = "-" * 20

def cislovani(pole):
    for i in range(1, len(pole) + 1):
        print(i % 10, end="")
    print()

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

vysledek = vyhodnot(pole)

# Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o) a vrátí
# "Vrátí herní pole s daným symbolem umístěným na danou pozici"

def tah(pole, cislo_policka, symbol):
    return pole[:cislo_policka - 1] + symbol + pole[cislo_policka:]

# Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče, na kterou pozici chce hrát,
# a vrátí herní pole se zaznamenaným tahem hráče.

def tah_hrace(pole):
    while True:
        try:
            zadanecislo = input("Napis cislo pole, na ktere chces hrat: ")
            vybrana_pozice = int(zadanecislo)
        except KeyboardInterrupt:
            print()
            print("SRABE!!!!")
            exit()
        except ValueError:
            print("Nezadals cislo!")
            continue

        print()
        if vybrana_pozice > len(pole):
            print("Zadals cislo vyssi, nez je hraci pole. Zkus to lip!")
        elif vybrana_pozice <= 0:
            print("Zadals zaporne cislo nebo nulu, zkus to lip!")
        elif pole[vybrana_pozice - 1] == "x" or pole[vybrana_pozice - 1] == "o":
            print("Policko uz je obsazene, musis jinam!")
        else:
            pole = tah(pole, vybrana_pozice, "x")
            cislovani(pole)
            print(pole)
            return pole

# Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici, na kterou hrát, a vrátí
# herní pole se zaznamenaným tahem počítače.

# def tah_pocitace(pole):
#     while True:
#         # ----------herni strategie pocitace -------------------
#         hledame = None
#         for k in ["o-o", "-oo", "oo-", "x-x", "-xx", "xx-", "-x-", "o--", "--o"]:
#             if k in pole:
#                 hledame = k
#                 break
#         if hledame:
#             vybrana_pozice = pole.index(hledame) + hledame.index("-") + 1
#         else:
#             vybrana_pozice = randrange(1, 21)
#
#
#         if pole[vybrana_pozice - 1] == "-":
#             pole = tah(pole, vybrana_pozice, "o")
#             #print(pole)
#             return pole

# Napiš funkci piskvorky1d, která vytvoří řetězec s herním polem a střídavě volá funkce tah_hrace a
# tah_pocitace, dokud někdo nevyhraje nebo nedojde k remíze.
# Nezapomeň kontrolovat stav hry po každém tahu

def piskvorky1d(pole):
    vysledek = "-"
    while vysledek == "-":
        pole = tah_hrace(pole) #HUMAN
        vysledek = vyhodnot(pole)
        if vysledek != "-":
            break
        pole = tah_pocitace(pole) #AI
        print(pole)
        print()
        vysledek = vyhodnot(pole)
    if vysledek == "x":
        print("Vyhrals! Konec hry!")
    elif vysledek == "o":
        print("Pocitac vyhral! Konec hry!")
    else:
        print("Remiza! Konec hry!")
#piskvorky1d(pole)
