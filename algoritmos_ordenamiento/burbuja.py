def burbuja(lista:list):
    """ devuelve una lista ordenada de menor a mayor mediante metodo burbuja  """
    vector = lista
    for i in range(0, len(vector)-1):
        for j in range(0, len(vector)-1):
            if vector[j] > vector[j+1]:
                tmp = vector[j+1]
                vector[j+1] = vector[j]
                vector[j] = tmp
    return vector

numeros = [10,5,8,1,3,15,2]
print(f"Lista desordenada {numeros}" )
print(f"Lista ordenada {burbuja(numeros)}")
