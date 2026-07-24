def cuenta_lineas(archivo):
    # contar líneas y caracteres del poema
    contador = 0
    caracter = 0 
    for linea in archivo:
        contador += 1
        caracter += len(linea)
    return contador, caracter
    


def main():
    archivo = open("poema.txt", "r", encoding = "utf-8")
    poema = archivo.read()
    print(poema)
    archivo.close()
    
    archivo = open("poema.txt", "r", encoding = "utf-8")
    num_lineas, num_caracter = cuenta_lineas(archivo)
    print (f"El poema tiene {num_lineas} lineas y {num_caracter}")
    archivo.close()
main()