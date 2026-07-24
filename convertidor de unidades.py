print("Programa para convertir una medida a centimetros")


def pies_a_cm(pies):
    cmpies = pies*30.48
    return cmpies
    
def pulgadas_a_cm(inches):
    cmin = inches * 2.54
    return cmin

def yardas_a_cm(yards):
    cmyd = yards * 91.44
    return cmyd

def main():
    print("1. Pies a cm")
    print("2. Pulgadas a cm")
    print("3. Yardas a cm")
    
    opcion = int(input("introduce una opción: "))
    numero = float(input("introduce la cantidad: "))
    
    if numero <=0:
        print("error en valor, la cantidad debe ser mayor que cero")
    else:
        print("Cálculo: ")

    
    pies_finales = pies_a_cm(numero)
    pulgadas_finales = pulgadas_a_cm(numero)
    yardas_finales = yardas_a_cm(numero)
    
    if opcion == 1:
        print(f"{numero} pies equivalen a {pies_finales:.2f} cm")
    elif opcion == 2:
        print(f"{numero} pulgadas equivalen a {pulgadas_finales:.2f} cm")
    elif opcion == 3:
        print(f"{numero} yardas equivalen a {yardas_finales:.2f} cm")
    else:
        print("Error en opción, debe ser un número entre 1 y 3")
        
main()

