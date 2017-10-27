
cislo = int(input("Zadej cele cislo:"))
prvociso = True

for n in range(2, cislo - 1):
    delitelne = cislo % n == 0
    if delitelne:
        #print("NENI PRVOCISLO")
        prvociso = False
        break
if prvociso == True:
    print("PRVOCISLO")
else:
    print("NENI PRVOCISLO")
