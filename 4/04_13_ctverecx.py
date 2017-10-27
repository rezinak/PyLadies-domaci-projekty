# Pomocí cyklů for a příkazu if napiš program, který z jednotlivých 'X' a mezer vypíše:
# X X X X X X
# X         X
# X         X
# X         X
# X X X X X X

for pocetradku in range(5):
    if pocetradku == 0 or pocetradku == 4:
        for pocetX in range(6):
            print(" X ", end = "")
        print()

    else:
        print(" X              X ")
