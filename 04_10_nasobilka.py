# Napiš program, který vypíše „tabulku“ s násobilkou:
# 0 0 0 0 0
# 0 1 2 3 4
# 0 2 4 6 8
# 0 3 6 9 12
# 0 4 8 12 16
# Funguje? Dej to do Gitu!

for radek in range(5):
    for cislo in range(5):
        print(cislo * radek, " ", end="")
    print()

# multiplicator = 0
# nasobeneCislo = 0
# for pocetRadku in range(5):
#     nasobeneCislo = 0
#     for naRadek in range(5):
#         print(nasobeneCislo * multiplicator, " ", end="")
#         nasobeneCislo = nasobeneCislo + 1
#     multiplicator = multiplicator + 1
#     print("")
