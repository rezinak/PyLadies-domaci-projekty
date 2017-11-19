import piskvorky

def test_tah_na_prazdne_pole():
    pole = piskvorky.tah_pocitace(piskvorky.pole)
    assert len(pole) == 20
    assert pole.count("x") == 0
    assert pole.count('-') == 19
