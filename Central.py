from multiprocessing import Process, Lock
from codigo_caras import init

mutex = Lock()
videomax = 1
mov = 1

def leerValor():
    with mutex:
        return videomax

def escribirValor(sacagawea):
    with mutex:
        videomax= sacagawea

def leerNombre():
    with mutex:
        return mov

def darNombre(movie):
    with mutex:
        mov = movie


"""
def main():
    if __name__ == "__main__":
            init()
            while True:

            pass
"""