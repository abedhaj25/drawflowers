import turtle   #import turtle

def draw_petal():  #function just draws a flower petal or a parallelogram
        turtle.forward(30) #moves forward 30 steps
        turtle.right(45)   #turns right 45 degrees
        turtle.forward(30)
        turtle.right(135)
        turtle.forward(30)
        turtle.right(45)
        turtle.forward(30)
        turtle.right(135)


def draw_flower(): #draws four petals to make a flower
    turtle.left(45) #turns left 45 degrees
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)

def draw_flower_and_advance(): #moves the head of the turlte to make space
    draw_flower()
    turtle.right(90)
    turtle.up()      #raise the turtle head so it moves without drawing
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down() #puts it back down

def draw_flower_bed(): #draw 3 flowers
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()


if __name__ == '__main__' :
    turtle.speed(0)  #speeds up the procces
    draw_flower_bed() #calls function
    turtle.done()