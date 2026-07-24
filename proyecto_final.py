# Memorama Matemático
# Miércoles 29 de abril de 2026
# A01735803. Fernanda Sánchez Estudillo. IDM.

def main():
    
    """ Función principal main donde se contienen las demás funciones """
    
    nombre = input("Bienvenid@ al Memorama. Teclea tu nombre: >u< ")
    
    
    def crear_tablero():
        
        """ Crea el tablero del memorama de 6x6, emparejando cada problema
        matemático con su debido resultado """
        
        problemas = [
            "Raíz de 144", "7^2", "15 * 6", "100 / 4", "9^2", "Raíz de 81",
            "30% de 250", "$500 con 20% desc.", "150 + 10%", "(5+3)*2^2",
            "200+IVA 16%", "25% de 80", "0.00045 científica",
            "2.5e3 normal", "Prob. 1/4", "Pend.(1,2)-(3,6)",
            "Prom.10,8,6,6", "x+2=10"
        ] #Lista de elementos 1

        resultados = [
            "12", "49", "90", "25", "81", "9",
            "75", "400", "165", "32", "232", "20",
            "4.5x10^-4", "2500", "0.25", "2",
            "7.5", "8"
        ] #Lista de elementos 2

        cartas = []
        ids = []
        id_par = 0

        for i in range(len(problemas)):
            id_par = i + 1

            cartas.append(problemas[i]) # Se añaden a la lista el elemento "i" de la lista problemas a la lista cartas
            #con un ID determinado.
            ids.append(id_par)

            cartas.append(resultados[i])# Se añaden a la lista el elemento "i" de la lista resultados a la lista cartas
            #con un ID determinado.
            
            # Se hace esto para poder determinar un ID que coincida cuando las cartas sean correctas.
            
            ids.append(id_par)
            # Se añade la lista "ids" los IDs de las cartas

        tablero = []
        tablero_ids = []

        indice = 0

        for i in range(6): 
            fila = [] # Se abre la lista fila
            fila_ids = [] # Se abre la lista que guarda los IDs

            for j in range(6): # Se usa un for anidado, formato usado para listas de listas.
                fila.append(cartas[indice]) # Se añaden a "fila" el elemento "indice" de la lista resultados a la lista
                #cartas, para que cada "carta" se guarde en un espacio del tablero
                fila_ids.append(ids[indice]) 
                indice = indice + 1

            tablero.append(fila)
            tablero_ids.append(fila_ids)

        return tablero, tablero_ids

    def crear_visible():
        
        """ Crea la versión visible del tablero, marcando el número de filas, columnas,
        divisiones del cada carta, título del juego y la interfaz de usuario, mostrando
        las X correspondientes de cada carta """
        
        visible = []

        for i in range(6):
            fila = []

            for j in range(6):
                fila.append("X")

            visible.append(fila)

        return visible
    

    def mostrar(tablero):
        
        """ Función que crea la interfaz de usuario, el formato que el usuario verá a la hora de
        jugar el memorama, donde recibe el parámetro tablero, variable que se retornó en la función
        crear_tablero(), donde se definieron los ids de cada carta """
        
        print()
        print("  ° - .   Memorama Matemático  ° - .")
        print("\n             0                      1                   2                   3                   4                   5")
        print("-----" * 27)

        for i in range(len(tablero)):
            print(f"{i} |", end="")

            for j in range(len(tablero[i])):
                contenido = str(tablero[i][j])

                if len(contenido) > 20:
                    contenido = contenido[:20]

                print(f"{contenido:20}|", end="")

            print()
            print("-----" * 27)

        print()

    def tablero_completo(visible):
         
        """Verifica si todas las cartas del tablero ya
        fueron descubiertas, devolviendo 1 si está completo y 0 si aún quedan cartas ocultas.
        recibe como parámetro la variable "visible", utilizada anteriormente en la función
        crear_visible()"""
        
        completo = 1

        for i in range(len(visible)):
            for j in range(len(visible[i])):
                if visible[i][j] == "X":
                    completo = 0

        return completo

    def calcular_puntos(id_par):
        
        """Da la cantidad de puntos según el id
        del par encontrado: 2 puntos para los primeros 6 pares (los más sencillos),
        4 para los siguientes (intermedio) 6 y 5 para los últimos (avanzado)"""
        
        if id_par <= 6:
            return 2
        elif id_par <= 12:
            return 4
        else:
            return 5
        

    def frase_acierto(contador):
        
        """ Esta función muestra frases "random" al usuario en caso de encontrar un par correcto """
        
        frases = [
            "¡Increíble, sigue así! :)",
            "Le ganaste a Carl Friedrich Gauss :o, príncipe de las matemáticas",
            "¡Excelente! :3 ",
            "¡Eres muy buen@! :)",
            "¡Muy bien! :)",
            "¡Eso! Lo estás logrando :D"
            "¡Albert Einstein revivió, eres tú!"
        ]

        if contador >= len(frases):
            posicion = contador - len(frases)
        else:
            posicion = contador
        return frases[posicion]


    """ Inicia la función final "main", donde ahora se tendrá acceso a que el usuario tecleé sus intentos.
    Dependiendo de las cartas que seleccione, será el mensaje que recibirá y se determinará si el par es correcto y se queda
    desplegada durante el resto del juego o, en cambio, se "voltea" la carta y se intenta nuevamente """
    tablero, tablero_ids = crear_tablero()
    visible = crear_visible()

    puntos = 0
    contador_aciertos = 0

    while tablero_completo(visible) == 0:
        mostrar(visible)
        print(f"Puntaje actual: {puntos}")

        fila1 = int(input("Selecciona la fila de la primera carta (0 a 5): "))
        col1 = int(input("Selecciona la columna de la primera carta (0 a 5): "))

        if fila1 >= 0 and fila1 <= 5 and col1 >= 0 and col1 <= 5:

            if visible[fila1][col1] == "X":
                visible[fila1][col1] = tablero[fila1][col1]
                mostrar(visible)

                fila2 = int(input("Selecciona la fila de la segunda carta (0 a 5): "))
                col2 = int(input("Selecciona la columna de la segunda carta (0 a 5): "))

                if fila2 >= 0 and fila2 <= 5 and col2 >= 0 and col2 <= 5:

                    if visible[fila2][col2] == "X":
                        visible[fila2][col2] = tablero[fila2][col2]
                        mostrar(visible)

                        id_par1 = tablero_ids[fila1][col1]
                        id_par2 = tablero_ids[fila2][col2]

                        if id_par1 == id_par2:
                            puntos = puntos + calcular_puntos(id_par1)
                            contador_aciertos = contador_aciertos + 1
                            print(f"{frase_acierto(contador_aciertos)}")

                        else:
                            print("¡No es un par! Intenta de nuevo.")
                            visible[fila1][col1] = "X"
                            visible[fila2][col2] = "X"

                    else:
                        print("Ya seleccionaste esa carta, por favor selecciona otra carta :D")
                        visible[fila1][col1] = "X"

                else:
                    print("Número inválido. Ingresa valores entre 0 y 5.")
                    visible[fila1][col1] = "X"

            else:
                print("Esa carta ya fue volteada, selecciona otra :D")

        else:
            print("Número inválido. Ingresa valores entre 0 y 5 :3")
            
            

    print(f"¡Felicidades! {nombre} :D")
    print(f"Completaste el tablero con {puntos} puntos.")


main()