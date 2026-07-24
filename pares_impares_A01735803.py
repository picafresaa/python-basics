#Fernanda Sánchez Estudillo
#A01735803
#19 de febrero de 2026

print("programa para clasificar números pares e impares positivos y negativos")
print("por favor, ingresa un número entero")

num = int(input("Escribe el número entero aquí: "))
mod = num % 2

if num < 0 and mod == 0:
    print("El número es un par negativo")
    
elif num >= 0 and mod == 0:
    print("El número es un par positivo")
    
elif num >= 0 and mod !=0:
    print("El número es un impar positivo")
    
elif num <= 0 and mod != 0:
    print("El número es un impar negativo")
    
else: print("Por favor ingresa un valor entero")