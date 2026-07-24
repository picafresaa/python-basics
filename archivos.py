def main():
    archivo = open("nombre.txt", "r", encoding = "utf-8")
    nombre = archivo.read()
    print(nombre)
    archivo.close()
    
main()