from os import remove

def mv(archivo, destino):
    """ Mueve el archivo seleccionado hacia otra ubicacion """
    try:
        texto = None
        with open(archivo) as f:
            texto = f.readlines()
        with open(destino, "w") as f:
            texto_movido = f.writelines(texto)
            print(texto_movido)
            remove(archivo)
        print("El archivo se ha movido satisfactoriamente")
    except FileNotFoundError:
        print("El archivo no existe")
    

mv("lorem.txt", "carpeta/lorem-mv.txt")