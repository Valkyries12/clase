#Ejercicio 11.10.1. Escribir un programa, llamado head que reciba un archivo y un número N e imprima las primeras N líneas del archivo.

def head(archivo, n:int):
    """ Imprime las primeras n lineas del archivo  """
    try:
        with open(archivo) as f:
            for i in range(n):
                linea = f.readline()
                print(linea)
    except FileNotFoundError:
        print("El archivo no existe")

head("lorem.txt", "e")
