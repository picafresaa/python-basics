#Fernanda Sánchez Estudillo
#A01735803
#19 de febrero de 2026

print("programa para indicar un tipo de triángulo")
print("Por favor ingrese números enteros positivos, de lo contrario arrojará error")

x = int(input("Digite el lado x: "))
y = int(input("Digite el lado y: "))
z = int(input("Digite el lado z: "))

if (x <= 0 or y <= 0 or z <= 0):
    print("por favor mande un número positivo")

elif (x == y and x == z and y == z):
    print("Es un triángulo equilátero")

elif (x == y or x == z or y == z):
    print("Es un triángulo isósceles")

elif (x != y and x != z and y!=z):
    print("es un triángulo escaleno")

else:
    print("Datos no válidos, deben ser positivos y cumplir con las condiciones")
