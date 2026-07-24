import turtle

#modificar el programa para que sea un ciclo

def cuadrado(tortuga, longitud):
    for i in range(4):
        tortuga.forward(longitud)
        tortuga.left(90)
        
def main():
    bob = turtle.Turtle()
    figura(bob)
    cuadrado(bob, 40)
    cuadrado(bob, 100)
    cuadrado(bob, 180)

 
def figura(turtle):                 
    for i in range(5):
       turtle.forward(50)           
       turtle.right(144)
       
import turtle

def cuadrado(t, longitud):
    for i in range(4):
        t.forward(longitud)
        t.left(90)

bob = turtle.Turtle()

bob.pencolor("blue")
bob.pensize(3)

cuadrado(bob, 50)

bob.penup()
bob.goto(100, 0)
bob.pendown()
cuadrado(bob, 100)

bob.penup()
bob.goto(200, 0)
bob.pendown()
cuadrado(bob, 150)

turtle.done()
main()