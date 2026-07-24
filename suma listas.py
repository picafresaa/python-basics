def pedir_numero_elementos():
    n = int(input("Numero de elementos en cada lista:"))
    while n <= 0:
        print("Error, debe ser positivo")
        n = int(input("Numero de elementos en cada lista:"))
    return n


def leer_lista(n, nombre_lista):
    lista = []
    print(f"Elementos de la {nombre_lista}:", end="")
    for i in range(n):
        num = int(input(f"Elemento {i+1}:"))
        lista.append(num)
    return lista


def sumar_listas(lista1, lista2):
    suma = []
    for i in range(len(lista1)):
        suma.append(lista1[i] + lista2[i])
    return suma


def main():
    print("Valores faltantes", end="")

    n = pedir_numero_elementos()
    lista1 = leer_lista(n, "lista 1")
    lista2 = leer_lista(n, "lista 2")
    suma = sumar_listas(lista1, lista2)

    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Suma de listas: {suma}")


main()