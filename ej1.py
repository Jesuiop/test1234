
nombre = input ("Introduce tu nombre: ")
#comentario de conflicto linea
'''
comentario
de nose
muchas lineas
'''
valor=8
def hola(nombre_recibido):
    
    if valor < 4:
        print("Hola")
    elif valor >=4 and valor < 9:
        print("Adios")
    print("Hola mundo " + nombre_recibido)
    return 1
hola(nombre)