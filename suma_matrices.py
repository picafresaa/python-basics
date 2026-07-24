def matriz(renglones, columnas):
    matriz = []
    for r in range(renglones):
        lista = []
        for c in range(columnas):
            dato = int(input(f"Matriz[{r+1}][{c+1}]:"))
            lista.append(dato)
        matriz.append(lista)
    return matriz
    
def muestra_matriz(matriz):
    reng = len(matriz)
    col = len(matriz[0])
    for r in range(reng):
        for c in range(col):
            print(matriz[r][c], end=" ")
        print()
        
def suma_columnas(matriz):
    reng = len(matriz)
    col = len(matriz[0])
    
    lista_sumas = []
    
    for c in range(col):
        suma = 0
        for r in range(reng):
            suma += matriz[r][c]
        lista_sumas.append(suma)
        
    return lista_sumas

def main():
    print("Suma de columnas de una matriz")
    print("Datos de la matriz:")
    
    reng = int(input("Numero de renglones: "))
    while reng < 1:
        print("Error, el número debe ser mayor o igual a 1")
        reng = int(input("Numero de renglones: "))
        
    col = int(input("Numero de columnas: "))
    while col < 1:
        print("Error, el número debe ser mayor o igual a 1")
        col = int(input("Numero de columnas: "))
    
    mat = matriz(reng, col)
    
    print(f"Matriz de {reng} x {col}:")
    muestra_matriz(mat)
    
    suma = suma_columnas(mat)
    print(f"Suma de valores por columna: {suma}")

main()