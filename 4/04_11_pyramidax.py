# Napiš program, který postupně z jednotlivých 'X' vypíše:
# X
# X X
# X X X
# X X X X
# Funguje? Do Gitu s tím!
for pocetradek in range(1, 5):
    #for pocetx in range(1):
    print(pocetradek * " X")

print("jeste jinak:")
for pocetradek in range(1,5):
    for pocetx in range (pocetradek):
        pocetx = "X" * pocetradek
        print(" X", end = "")
    print()
