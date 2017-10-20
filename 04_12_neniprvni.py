# Pomocí cyklu for a příkazu if napiš program, který vypíše následující řádky. Funkci print volej pouze
# uvnitř v cyklu:
# první řádek
# není první
# není první
# není první

for radek in range(4):
    if radek == 0:
        print("Prvni radek")
    else:
        print("neni prvni")
