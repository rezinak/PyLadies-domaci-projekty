animals = ["pes", "kocka", "kralik", "had"]

# 1. Napiš funkci, která vypíše jména domácích zvířat, která jsou kratší než 5 písmen.

def shorter_than():
    for animal in animals:
        if len(animal) < 5:
            print(animal)

# 2. Napiš funkci, která vypíše jména domácích zvířat, která začínají na k.

def begins_with():
    for animal in animals:
        if animal[0] == "k":
            print(animal)

# 3. Napiš funkci, která dostane slovo a zjistí, jestli je v seznamu domácích zvířat.
def find_animal(looking_for):
    return looking_for in animals

# 4. Napiš funkci, která dostane dva seznamy jmen zvířat a vrátí tři seznamy:
# (a) zvířata, která jsou v obou seznamech,
# (b) zvířata, která jsou v jen prvním seznamu,
# (c) zvířata, která jsou v jen druhém seznamu.

animals2 = ["pes", "kralik", "sklipkan", "ovecka"]

def sort_Lists(list1, list2):
    both = []
    only_In_First = []
    only_In_Second = []

    for zvire in list1:
        if zvire not in list2:
            only_In_First.append(zvire)
        elif zvire in list2:
            both.append(zvire)

    for zvire in list2:
        if zvire not in list1:
            only_In_Second.append(zvire)
    return both, only_In_First, only_In_Second

sort_Lists(animals, animals2)

# 5. Napiš program, který seřadí seznam domácích zvířat podle abecedy.
animals.sort()

# 6. Had byl pyšný na to, že je v abecedě první. Dokud nepřiletěla "andulka".
# Abys hada uklidnila, vytvoř funkci, která zvířata seřadí podle abecedy, ale bude ignorovat první písmeno
# (t.j. vrátí ["had", "pes", "andulka", "kočka", "králík"]).
animals.append("andulka")

def sort_by_second_char(seznam):
    for zvire in animals:
        def second_char(zvire):
            return zvire[1]
    seznam.sort(key=second_char)
    return seznam
