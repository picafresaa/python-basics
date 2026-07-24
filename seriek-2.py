#Total de puntos de un juego
#Fernanda Sánchez Estudillo
#A01735803
#09 de marzo 2026

#Entrada: puntos
#Salida: Suma de los puntos

# Caso de prueba 1:
# n = 10
# 10 1.5497677311665408
# 100 1.6349839001848923
# 1000 1.6439345666815615
# 10000 1.6448340718480652


def serie(n):
    cont_k = 1
    suma = 0

    while cont_k <= n:
        suma = suma + 1/(cont_k**2)
        cont_k = cont_k + 1

    return(suma)

def main():
    n = 10
    
    while n <= 10000:
        result = serie(n)
        print(f"{n} {result}")
        n = n * 10
        
main()