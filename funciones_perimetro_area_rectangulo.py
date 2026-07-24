def areaRect(largo, ancho):
    area = largo * ancho
    return(area)

def perimetroRect(largo, ancho):
    perimetro = (2 * largo)+ (2 * ancho)
    return(perimetro)

def main():
    largo = float(input("ingrese el largo (cm): "))
    ancho = float(input("ingrese el ancho (cm): "))
    print("Escoja si quiere calcular perimetro o area (teclee p/a)")
    eleccion = input()
    
    if (eleccion == "a"):
        area = areaRect(largo, ancho)
        print(f"area = {area:.2f}")
        
    elif (eleccion == "p"):
        perimetro = perimetroRect(largo, ancho)
        print(f"Perímetro = {perimetro:.2f}")
        
    else:
        print(f"letra no válida, intente de nuevo")
        
main()
    

