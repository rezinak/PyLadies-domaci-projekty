# Napiš program, který simuluje tuto hru:
# První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka. Potom hází další hráč,
# dokud nepadne šestka i jemu. Potom hází hráč třetí a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky
# potřeboval nejvíc hodů. (V případě shody vyhraje ten, kdo házel dřív.)
# Program by měl vypisovat všechny hody a nakonec napsat, kdo vyhrál.
from random import randrange


hozeno = []
hod = None
cislohrace = 0
pokusyhracu = []

for pocethracu in range(4):
    cislohrace = (cislohrace + 1)
    while hod != 6:
        hod = randrange(1,7)
        hozeno.append(hod)
    print("Hrac", cislohrace, "hodil cisla", hozeno, "\n", "Sestka padla na", len(hozeno), "pokus.")
    pokusyhracu.append(len(hozeno))
    hod = None
    hozeno = []

nejvyssi = max(pokusyhracu)
vitez = pokusyhracu.index(nejvyssi)
print("Vyhral hrac cislo", vitez + 1)
