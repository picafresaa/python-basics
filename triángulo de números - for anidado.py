def main():
    print("Triángulo de números")
    limite = int(input("Límite: "))
    
    for renglon in range (1, limite+1):
        for columna in range (1, renglon+1):
            print(renglon, end =" ")
        print()
        
main()