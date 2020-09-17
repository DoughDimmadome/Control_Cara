from Central import leerValor,leerNombre
from pathindex import mainPath, name
from omxplayer import OMXPlayer

def display():
    movo = leerNombre()
    
    if movo == 1 or movo == 2 or movo == 3 or movo == 4 or movo == 5 or movo == 6 or movo == 7 or movo == 8 or movo == 9 or movo == 10 or movo == 11 or movo == 12 or movo == 14 or movo == 15 or movo == 16 or movo == 17 or movo == 18 or movo == 19 or movo == 20 or movo == 21 or movo == 22 or movo == 23 or movo == 24:
        OMXPlayer ( movo , args=['--adev hdmi','--layer 1','--loop']) 
    
    if movo == 9 or movo == 10 or movo == 11 or movo == 12 or movo == 13 or movo == 14:
        OMXPlayer (movo , args=['--adev hdmi','--layer 2','--loop']) 
