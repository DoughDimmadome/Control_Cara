from pynput import keyboard
from Central import escribirValor

#joystick izquierdo
def alegria():
    escribirValor(1)

def alegramayor():
    escribirValor(2)

def alegriamenor():
    escribirValor(3)

def sorpresa():
    escribirValor(4)

def sorpresamayor():
    escribirValor(5)

def sorpresamenor():
    escribirValor(6)

def desprecio():
    escribirValor(7)

def despreciomayor():
    escribirValor(8)

def despreciomenor():
    escribirValor(9)

def enojo():
    escribirValor(10)

def enojomayor():
    escribirValor(11)

def enojomenor():
    escribirValor(12)

def triztesa():
    escribirValor(13)

def triztesamayor():
    escribirValor(14)

def triztesamenor():
    escribirValor(15)

def miedo():
    escribirValor(16)

def miedomayor():
    escribirValor(17)

def miedomenor():
    escribirValor(18)

def disgusto():
    escribirValor(19)

def disgustomayor():
    escribirValor(20)

def disgustomenor():
    escribirValor(21)

def satisfaccion():
    escribirValor(22)

def satisfaccionmayor():
    escribirValor(23)

def satisfaccionmenor():
    escribirValor(24)

#joystick derecho
def extasis():
    escribirValor(25)

def reflexivo():
    escribirValor(26)

def muerto():
    escribirValor(27)

def confusion():
    escribirValor(28)

def incertidumbre():
    escribirValor(29)

def masVerguenza():
    escribirValor(30)

def verguenza():
    escribirValor(31)

def frustracion():
    escribirValor(32)





def on_press(key):
    try:
        if key.char == 'd':
            alegria()
        
        
        
    except AttributeError:
        print('GhAAAAAAAA')


# def on_release(key):
#on_release=on_release

def init():
    with keyboard.GlobalHotKeys({
            'a': triztesa,
            'w': disgusto,
            'd': alegria,
            's': desprecio,
            'w+a': miedo,
            'w+a+j': miedomayor,
            'w+a+k': miedomenor,
            'w+d': satisfaccion,
            's+a': enojo,
            's+d': sorpresa,
            '<up>': extasis,
            }) as h:
        h.join()
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()

"""
# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
"""

