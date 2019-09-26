import csv

PATH = "registros.csv"

def leer_csv(path):
    """ lee un archivo en formato csv e imprime  """
    try:
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file)
            for fila in csv_reader:
                print(f"{fila[0]:30} {fila[1]:5} {fila[2]:45} {fila[3]:20} {fila[4]:20} {fila[5]:45} {fila[6]:5}")
    except FileNotFoundError:
        print("El archivo no existe")

leer_csv(PATH)