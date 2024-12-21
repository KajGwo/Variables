###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("white")
# Create the turtle



## Draw figures

figures.draw_square(100)

figures.pen.penup()
figures.pen.goto(-1000, 100)
figures.pen.pendown()

figures.draw_square(100)

figures.draw_rectangle(200, 100)

figures.pen.penup()
figures.pen.goto( 100, 100)
figures.pen.pendown()

figures.draw_rectangle(200, 100)

figures.draw_triangle(200)

figures.pen.penup()
figures.pen.goto( 300, 100)
figures.pen.pendown()

figures.draw_triangle(200)



# Hide the turtle and finish
figures.pen.hideturtle()
window.mainloop()








