

def mv(archivo, destino):
    """ Mueve el archivo seleccionado hacia otra ubicacion """
    try:
        texto = None
        with open(archivo) as f:
            texto = f.readlines()
    except IOError:
        print("El archivo no existe")
    try:
        with open(destino, "w") as f:
            texto_movido = f.writelines(texto)
            print(texto_movido)
    except:
        print("Algo ha fallado :(")

mv("lorem.txt", "carpeta/texto-mv.txt")