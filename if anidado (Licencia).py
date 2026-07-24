#Programa tramite licencia

print("Programa de licencia")
edad = int(input("Ingresa tu edad: "))
if (edad < 0):
    print("Respuesta incorrecta, el número debe ser positivo")
else:
    id_oficial = input("¿Tienes identificacion oficial (s/n)? ")
    if (id_oficial != "s") and (id_oficial != "n"):
        print("Respuesta incorrecta, teclee sólo s o n")
    else:
        if (id_oficial == "s") and (edad >= 18):
            print("Trámite de licencia concedido")
        else:
            print("No cumple con requisitos") 