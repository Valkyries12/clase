#Ejercicio 11.10.2. Escribir un programa, llamado cp.py, que copie todo el contenido de un archivo (sea de texto o binario) a otro, de modo que quede exactamente igual.

def cp(archivo, copia):
    """ Copia el contenido de un archivo a otro especificado """
    texto = None
    try:
        with open(archivo) as f:
            texto = f.readlines()
        with open(copia, "w") as f:
            for linea in texto:
                lineas = linea
                f.writelines(lineas)
    except FileNotFoundError:
        print("El archivo no existe")

cp("lorem.txt", "copia_lorem2.txt")