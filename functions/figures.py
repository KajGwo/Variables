import turtle


pen = turtle.Turtle()
pen.speed(50) 


def draw_square(length):
   for i in range(4):
    pen.forward(length)
    pen.right(90)
    
   

     
def draw_rectangle(l, w):
    pen.forward(l) 
    pen.left(90) 

    pen.forward(w) 
    pen.left(90) 

    pen.forward(l)
    pen.left(90) 
  
    pen.forward(w) 
    pen.left(90) 


def draw_triangle(lenght):
    num = 0
    while num < 3:
        pen.forward(lenght)
        pen.right(120)
        num += 1

      
      








