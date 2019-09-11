def cat(archivo):
    """ imprime el contenido del archivo  """
    try:
        with open(archivo) as f:
            texto = f.readlines()
            for linea in texto:
                print(linea)
    except FileNotFoundError:
        print("No se ha encontrado el archivo")

cat("lorem.txt")