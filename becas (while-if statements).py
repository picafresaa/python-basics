#Total de puntos de un juego
#Fernanda Sánchez Estudillo
#09 de marzo 2026

#Entrada: puntos
#Salida: Suma de los puntos

#Caso de prueba 1:
#Tipo de beca: 1
#Tipo de beca: 2
#Tipo de beca: 3
#0
#total inscritos beca tipo 1: 1, que representa el 33.33%
#total inscritos beca tipo 2: 1, que representa el 33.33%
#total inscritos beca tipo 3: 1, que representa el 33.33%


def main():
    print("Teclee el tipo de beca, para finalizar marque 0")
    print("1) Becas Benito Juárez")
    print("2) Jóvenes Escribiendo el futuro")
    print("3) Jóvenes Construyendo el futuro")
    
    num_beca = int(input())
    cont_1 = 0
    cont_2 = 0
    cont_3 = 0
    total_becarios = 0
    
    while num_beca != 0:
        if num_beca == 1:
            print("Tipo de beca: 1")
            cont_1 = cont_1 + 1
            total_becarios = total_becarios + 1
            num_beca = int(input())
            
        elif num_beca == 2:
            print("Tipo de beca: 2")
            cont_2 = cont_2 + 1
            total_becarios = total_becarios + 1
            num_beca = int(input())
            
        elif num_beca == 3:
            print("Tipo de beca: 3")
            cont_3 = cont_3 + 1
            total_becarios = total_becarios + 1
            num_beca = int(input())
            
            
        else:
            print("El número debe estar entre 1 y 3")
            num_beca = int(input())
            
    perc_1 = (cont_1 / total_becarios) * 100
    perc_2 = (cont_2 / total_becarios) * 100
    perc_3 = (cont_3 / total_becarios) * 100
            
    print (f"Total de inscritos para beca tipo 1: {cont_1}, que representa el {perc_1:.2f}%")
    print (f"Total de inscritos para beca tipo 2: {cont_2}, que representa el {perc_2:.2f}%")
    print (f"Total de inscritos para beca tipo 3: {cont_3}, que representa el {perc_3:.2f}%")
    
main()
    
    