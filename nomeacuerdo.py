def cuadrado(t, longitud):
    for i in range(4):
        t.forward(longitud)
        t.left(90)

bob = turtle.Turtle()

# Configuración
bob.pencolor("blue")
bob.pensize(3)

# Primer cuadrado
cuadrado(bob, 50)

# Segundo cuadrado
bob.penup()
bob.goto(100, 0)
bob.pendown()
cuadrado(bob, 50)

# Tercer cuadrado
bob.penup()
bob.goto(200, 0)
bob.pendown()
cuadrado(bob, 50)

turtle.done()