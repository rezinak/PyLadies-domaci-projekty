# Pomocí cyklů for a parametru end pro print napiš program, který postupně z jednotlivých 'X' vypíše:
# X X X X X
# X X X X X
# X X X X X
# X X X X X
# X X X X X
# „Z jednotlivých 'X'“ znamená, že nepoužiješ např. print('X X X X X').
# Jak pojmenuješ proměnnou cyklu? A tu druhou?
for pocetRadku in range (5):
    for naRadek in range(5):
        print(" X ", end = "")
    print("")
