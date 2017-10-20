# Napiš program, který vypíše čísla od jedné do 100, ale:
# • Pokud je číslo dělitelné třemi, napíše místo něj „bum”.
# • Pokud je číslo dělitelné pěti, napíše místo něj „bác”.
# • Pokud je číslo dělitelné pěti i třemi zároveň, napíše místo toho „bum-bác”.

for i in range(101):
    if i % 5 == 0 and i % 3 == 0:
        print("bum bac")
    elif i % 3 == 0:
        print("bum")
    elif i % 5 == 0:
        print("bac")
    else:
        print(i)
