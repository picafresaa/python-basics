def matriz(renglones, columnas):
    matriz = []
    for r in range (renglones):
        lista = []
        for c in range (columnas):
            dato = int(input(f"Matriz[{r+1}][{c+1}]:"))
            lista.append(dato)
        matriz.append(lista)
    return matriz
    
def muestra_matriz(matriz):
    reng = len(matriz)
    col = len(matriz[0])
    for ren in range (reng):
        for co in range(col):
            print(matriz[ren][co], end = " ")
        print()
        
def pares_por_renglon(matriz):
    reng = len(matriz)
    col = len(matriz[0])
    
    for r in range(reng):
        contador = 0
        for c in range(col):
            if matriz[r][c] % 2 == 0:
                contador += 1
        print(f"{contador}")

def main():
    print("Cantidad de pares  por renglon en una matriz")
    print("Datos de la matriz:")
    reng = int(input("Cantidad de renglones: "))
    col = int(input("Cantidad de columnas: "))
    mat = matriz(reng, col)
    print(f"Matriz de {reng} x {col}:")
    matfinal = muestra_matriz(mat)
    
    print("Total de pares por renglon: ")
    pares = pares_por_renglon(mat)
    #print(mat)
    
main()