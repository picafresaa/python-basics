#Total de puntos de un juego
#Fernanda Sánchez Estudillo
#A01735803
#09 de marzo 2026

#Entrada: puntos
#Salida: Suma de los puntos

#Caso de prueba 1:
#Tiro: C 
#Tiro: L
#Tiro: l
#f
#total de tiros L: 2
#total de tiros c: 1
#total de tiros n: 0
#total de tiros: 3
#puntaje final: 5

def main():
    print(" Contador de tipos de tiros en juego de basquetbol")
    print("Teclea los tipos de tiros realizados (Presione F para terminar)")
    tiro = input(("N) Normal, L) libre o C) de campo: "))
    campo = 0
    libre = 0
    normal = 0
    cantidad_tiros = 0

    while (tiro != "F") and (tiro != "f"):
        if (tiro == "N") or (tiro == "n"):
            print("tiro: N")
        
            normal = normal + 2
            cantidad_tiros += 1
            tiro = input()
        
        
        elif (tiro == "C") or (tiro == "c"):
            print("tiro: C")
        
            campo = campo + 3
            cantidad_tiros += 1
            tiro = input()
        
        elif (tiro == "L") or (tiro == "l"):
            print("tiro: L")
            libre = libre + 1
            cantidad_tiros += 1
            tiro = input()
        
        else:
            print("Número inválido, intente de nuevo")
            tiro = input()
        
    print(f"Total de puntos de tiros normales: {normal}")
    print(f"Total de puntos de tiros libres: {libre}")
    print(f"Total de puntos de tiros de campo: {campo}")
 
    total_final = libre + normal + campo


    print(f"el total de tiros fueron: {cantidad_tiros}")
    print(f"El total final de puntos es de: {total_final} ")

main()

   