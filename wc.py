#Ejercicio 11.10.4. Escribir un programa, llamado wc.py que reciba un archivo, lo procese e imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.

def wc(archivo):
    """ imprime cuantas lineas, palabras y caracteres tiene el archivo  """
    try:
        with open(archivo) as f:
            texto = f.readlines()
            lineas = len(texto)
            caracteres = 0
            palabras = 0
            for linea in texto:
                lista_linea = linea.split()
                palabras += len(lista_linea)
                for palabra in lista_linea:
                    caracteres += len(palabra)
            print(f"Lineas: {lineas}, Palabras: {palabras}, Caracteres: {caracteres}")

    except FileNotFoundError:
        print("El archivo no existe")

wc("lorem.txt")