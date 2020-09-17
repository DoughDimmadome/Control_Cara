#aqui van los paths generales y el individual de cada video.
from Central import leerValor,darNombre

mainPath = 'D:\rFreelance\rLaPolla\rControl_Cara\rcaras\rCARAS temporales\r'
name = ['IDLEg','ALEGRIA','ALEGRIAJ','ALEGRIAK','SORPRESA','SORPRESAJ','SORPRESAK' ]

def asignar():
    index = leerValor()
    darNombre(mainPath + name[index] + '.mp4')
