def pies_a_cm (pies):
    pies = int(input())
    cmpies= pies * 30.48
    return cmpies

    
    

    
    
def main():
    opcion = int(input("Elija convertir 1 - pies, 2 - pulgadas o 3 - yardas a cm: "))
    piescm = pies_a_cm(pies)
    pulgadas = in_a_cm(inches)
    yardas = yrd_a_cm(yards)
    
    if opcion == 1:
        print(f" Pies a cm = {pies_a_cm:.2f}")
        
    elif opcion == 2:
        print(f"pulgadas a cm = {in_a_cm:.2f}")
        
    elif opcion == 3:
        print(f"Yardas a cm = {in_a_cm:.2f}")
    
    else:
        print("Error, vuelva a intentarlo")
        
main() 