def encode(mensaje):
    nuevo_str = "" 
    for caracter in mensaje: #Ve cada elemento del mensaje
        numero = ord(caracter) #Convierte a número
        nuevo_str += str(numero) + " " #Concatena el número convertido a string con un espacio
    return nuevo_str


def vyc(nombre):
    vocales = ""
    consonantes = ""
    for letra in nombre:
        if letra in "aeiouAEIOU":
            vocales += letra
        else: 
            consonantes += letra
    print(f"Vocales: {vocales}")
    print(f"Consonantes: {consonantes}")    


def escondidas(cadena, letra):
    resultado = ""
    for caracter in cadena:
        if caracter != letra:
            resultado += "*"
        else:
            resultado += caracter
    return resultado

def rfc(apellidopat, apellidomat, nombre, year, mes, dia):
    pat = apellidopat[:2].upper()
    mat = apellidomat[:1].upper()
    nom = nombre[:1].upper()
    rfc = pat + mat + nom + year[-2:] + mes + dia
    return rfc


def main():
    print("Actividad 19: Strings")
    print("Menú de opciones:")
    print("1. Codificar mensaje")
    print("2. Vocales/consonantes")
    print("3. Esconde letras")
    print("4. Genera RFC")   
    print("5. Salir")

    menu = int(input("Selecciona una opción: "))
    while menu < 1 or menu > 5:
        print("Error, opción no válida. Intenta de nuevo.")
        menu = int(input("Selecciona una opción: "))
    if menu == 1:
        print("Por favor, ingresa el mensaje a codificar: ")
        mensaje = input()
        opcion1 = encode(mensaje)
        print(f"Codificación del mensaje: \n mensaje: {mensaje}")
        print(f"Codificación: {opcion1}")

    elif menu == 2:
        print("Vocales y consonantes en un nombre\nPor favor, ingrese un nombre: ")
        nombre = input("Teclea un nombre: ")
        voccon = vyc(nombre)

    elif menu == 3:
        cadena = input("Ingresa tu texto: ")
        letra = input("Ingresa la letra a mostrar: ")
        oculto = escondidas(cadena, letra)
        print(f"Texto original: {cadena}")
        print(f"Texto solo mostrando la letra'{letra}': {oculto}")


    elif menu == 4:
        apellidopat = input("Ingresa tu apellido paterno: ")
        apellidomat = input("Ingresa tu apellido materno: ")
        nombre = input("Ingresa tu nombre: ")
        year = input("Ingresa tu año de nacimiento (4 dígitos): ")
        mes = input("Ingresa tu mes de nacimiento (2 dígitos): ")
        dia = input("Ingresa tu día de nacimiento (2 dígitos): ")
        rfc_resultado = rfc(apellidopat, apellidomat, nombre, year, mes, dia)
        print(f"Tu RFC es: {rfc_resultado}")

    elif menu == 5:
        print("Saliendo del programa. ¡Hasta luego!")

main()  