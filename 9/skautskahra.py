# Úkolem je vytvořit známou skautskou hru „Kdo? S kým? Co dělali?“. Hra se hráče zeptá postupně na
# různé otázky, například „Kdo?“, „S kým?“, „Co dělali?“, „Kde?“, „Kdy?“, a nakonec „Proč?“, s tím, že
# mu umožní na jednu otázku odpovědět vícekrát a všechny odpovědi si uloží. Na závěr pak hra z každé
# sady odpovědí vybere náhodně jednu odpověď a z takto vybraných odpovědí složí větu, kterou vypíše
# uživateli. Seznam otázek by mělo být možné změnit na jednom místě bez zásahu do logiky programu.
import random

otazky = "Kdo?", "S kym?", "Co delali?", "Kde?", "Kdy?", "Proc?"
kolikrat_se_zeptat = 4

def vytvor_slovnik(seznam_otazek, pocet_odpovedi):
    otazky_a_odpovedi = {}
    for otazka in seznam_otazek:
        otazky_a_odpovedi.setdefault(otazka,[])

    for otazka in seznam_otazek:
        for polozit_otazku_vickrat in range(kolikrat_se_zeptat):
            odpoved = input(otazka)
            otazky_a_odpovedi[otazka].append(odpoved)
    return otazky_a_odpovedi

def vypis_vetu(seznam_otazek, seznam_odpovedi):
    for otazka in seznam_otazek:
        print(random.choice(seznam_odpovedi[otazka]), end=" ")

odpovedi = vytvor_slovnik(otazky, kolikrat_se_zeptat)
vypis_vetu(otazky, odpovedi)
