def tail(archivo, n:int):
    """ imprime las n últimas lineas  """
    try:
        with open(archivo) as f:
            texto = f.readlines()
            for i in range(len(texto)-n, len(texto)):
                print(texto[i])
    except FileNotFoundError:
        print("El archivo no existe")

tail("lorem.txt", 1)