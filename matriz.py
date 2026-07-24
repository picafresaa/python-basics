def crea_matriz(ren,col):
    matriz = []
    for r in range(ren):
        lista = []
        for c in range (col):
            #solicitar número
            numero = int(input("Número: "))
            lista.append(numero)
        matriz.append(lista)
    print(matriz)


def muestra_matriz(matriz):
    num_ren = len(matriz)
    num_col = len(matriz[0])
    for r in range (0, num_ren):
        for c in range (0, num_col):
            print(matriz[r][c], end = " ")
        print()
    


#crea_matriz(2,3)
muestra_matriz([[1,2,3],[4,5,6]])