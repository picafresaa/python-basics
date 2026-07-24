def crea_matriz(renglones, columnas):
    matriz = []
    
    for ren in range(renglones):
        lista = []
        for col in range (columnas):
            dato = int(input(f"Matriz[{ren}][{col}]: "))
            lista.append(dato)
        matriz.append(lista)
    return matriz
    
    
    
def muestra_matriz(matriz):
    renglones = len(matriz)
    columnas = len(matriz[0])
    
    for ren in range(renglones):
        for col in range(columnas):
            print(matriz[ren][col], end = " ")
        print()
    print(matriz)
            
            
            
def main():
    renglones = int(input("numero renglones:"))
    columnas = int(input("numero columnas:"))
    

    mat = crea_matriz(renglones, columnas)
    muestra_matriz(mat)
    
       
    
    
    
main()