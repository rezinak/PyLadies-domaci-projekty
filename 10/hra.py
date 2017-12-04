import pyglet
import math

window = pyglet.window.Window()
obrazek = pyglet.image.load("had.png")
obrazek2 = pyglet.image.load("had2.png")
had = pyglet.sprite.Sprite(obrazek)
had2 = pyglet.sprite.Sprite(obrazek2)
rychlost = 0

print("lezu do smycky")



def zpracuj_text(text):
    global rychlost
    if text == "r":
        had.x = 0
    elif text == "q":
        rychlost -= 10
    elif text == "w":
        rychlost += 10
    had.x += 10
    print(text)

def vykresli():
    window.clear()
    had.draw()

def klik(x, y, tlacitko, mod):
        had.x = x
        had.y = y
window.push_handlers(on_text=zpracuj_text,on_draw=vykresli, on_mouse_press = klik)

def tik(cas):
    had.x += cas * rychlost
    had.y =  had.y + 20 + math.sin(had.x /5) * 20


def zmen(cas):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)

def zmen_zpatky(cas):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.2)

pyglet.clock.schedule_interval(tik, 1/30)
pyglet.clock.schedule_once(zmen, 0.2)

pyglet.app.run()
print("uz nejsem ve smycce")
