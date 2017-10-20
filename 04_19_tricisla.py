# Napiš program, který se zeptá na 3 čísla a zjistí, jestli je jejich součet větší než 10.
# Funguje? Do Gitu s tím!

soucet = 0
cisloktisku = ""
for i in range(3):
    zadanecislo = int(input("zadej cislo: "))
    cisloktisku = cisloktisku + " " + str(zadanecislo)
    soucet = soucet + zadanecislo
print("Zadana cisla", cisloktisku)
#print("Soucet cisel", soucet)
if soucet > 10:
    print("Soucet cisel je", soucet, ". To je vic nez 10.")
else:
    print("Soucet cisel je", soucet, ". To je min nez 10.")
