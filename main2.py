import turtle

turtle.Screen().bgcolor("green")
sc=turtle.Screen()
sc.setup(100,100)

turtle.title("rectangle")
boared=turtle.Turtle()
boared.fillcolor("black")
boared.forward(100)


boared.left(120)
boared.forward(100)

boared.left(120)
boared.forward(100)

boared.penup()
boared.right(150)
boared.forward(50)

boared.pendown()
boared.right(90)

boared.forward(100)
boared.right(120)

boared.forward(100)
boared.right(120)

boared.forward(100)
boared.right(90)
boared.end_fill()
turtle.done()