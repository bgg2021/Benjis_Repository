import turtle

# Make sure you run each one individually.  The screen clear will mess the snowflake/pinwheel up.

#Turtle Recursion (25pts)

#1)  Using the turtle library, create the H fractal pattern according to the file shown in the data folder. (10pts)

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
my_turtle.pensize(3)
my_turtle.speed(0)

def h_tree (x, y, length, depth, color, thickness):
    my_turtle.color(color)
    my_turtle.pensize(thickness)

    my_turtle.setheading(0)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.forward(length)
    my_turtle.right(90)
    my_turtle.forward(length)
    pos1 = my_turtle.pos()
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(0)
    my_turtle.forward(length)
    my_turtle.left(90)
    my_turtle.forward(length)
    pos2 = my_turtle.pos()
    my_turtle.penup()

    my_turtle.setheading(180)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.forward(length)
    my_turtle.right(90)
    my_turtle.forward(length)
    pos3 = my_turtle.pos()
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(180)
    my_turtle.forward(length)
    my_turtle.left(90)
    my_turtle.forward(length)
    pos4 = my_turtle.pos()
    my_turtle.penup()

    if depth > 0:
        h_tree(pos1[0], pos1[1], length / 2, depth - 1, color, thickness - 0.5)
        h_tree(pos2[0], pos2[1], length / 2, depth - 1, color, thickness - 0.5)
        h_tree(pos3[0], pos3[1], length / 2, depth - 1, color, thickness - 0.5)
        h_tree(pos4[0], pos4[1], length / 2, depth - 1, color, thickness - 0.5)


h_tree(0, 0, 160, 3, "black", 4)

my_screen.clear()


#2)  Using the turtle library, create any of the other recursive patterns in the data folder. 
#  Challenge yourself to match your pattern as closely as you can to the image.  (10pts)
#  Note:  The Koch snowflake shows step by step building of the fractal.  
#  The rectangle fractal example shows 4 possible drawings of the same fractal (choose any one)


def snowflake(x, y, depth, length, color, thickness):
    my_turtle.color(color)
    my_turtle.pensize(thickness)

    my_turtle.setheading(0)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.forward(length)
    my_turtle.penup
    pos1 = my_turtle.pos()

    my_turtle.setheading(60)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.forward(length)
    my_turtle.penup
    pos2 = my_turtle.pos()

    my_turtle.setheading(120)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.forward(length)
    my_turtle.penup
    pos3 = my_turtle.pos()

    my_turtle.setheading(180)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.forward(length)
    my_turtle.penup
    pos4 = my_turtle.pos()

    my_turtle.setheading(240)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.forward(length)
    my_turtle.penup
    pos5 = my_turtle.pos()

    my_turtle.setheading(300)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.forward(length)
    my_turtle.penup
    pos6 = my_turtle.pos()

    if depth > 0:
        snowflake(pos1[0], pos1[1], depth - 1, length / 3, color, thickness - 0.5)
        snowflake(pos2[0], pos2[1], depth - 1, length / 3, color, thickness - 0.5)
        snowflake(pos3[0], pos3[1], depth - 1, length / 3, color, thickness - 0.5)
        snowflake(pos4[0], pos4[1], depth - 1, length / 3, color, thickness - 0.5)
        snowflake(pos5[0], pos5[1], depth - 1, length / 3, color, thickness - 0.5)
        snowflake(pos6[0], pos6[1], depth - 1, length / 3, color, thickness - 0.5)

snowflake(0, 0, 3, 230, "black", 3)

my_screen.clear()

#3)  Create your own work of recursive art with a repeating pattern of your making (or choose another one from the files).  
#  It must be a repeated pattern using recursion (not just loops). Snowflakes, trees, and spirals are a common choice.  
#  Play around and have fun with it.  (5pt)

def pinwheel (x, y, depth, length, color, thickness):
    my_turtle.color(color)
    my_turtle.pensize(thickness)

    my_turtle.setheading(0)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.forward(length)
    my_turtle.right(30)
    my_turtle.forward(length)
    my_turtle.penup()
    pos1 = my_turtle.pos()

    my_turtle.setheading(90)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.forward(length)
    my_turtle.right(30)
    my_turtle.forward(length)
    my_turtle.penup()
    pos2 = my_turtle.pos()

    my_turtle.setheading(180)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.forward(length)
    my_turtle.right(30)
    my_turtle.forward(length)
    my_turtle.penup()
    pos3 = my_turtle.pos()

    my_turtle.setheading(270)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.forward(length)
    my_turtle.right(30)
    my_turtle.forward(length)
    my_turtle.penup()
    pos4 = my_turtle.pos()

    if depth > 0:
        pinwheel(pos1[0], pos1[1], depth - 1, length / 3, color, thickness - 0.5)
        pinwheel(pos2[0], pos2[1], depth - 1, length / 3, color, thickness - 0.5)
        pinwheel(pos3[0], pos3[1], depth - 1, length / 3, color, thickness - 0.5)
        pinwheel(pos4[0], pos4[1], depth - 1, length / 3, color, thickness - 0.5)

pinwheel(0, 0, 3, 100, "green", 2)


#  General expectations for all problems
#  Give all your fractals a depth of at least 4.  (Don't make programs that take forever though)  
#  Ensure the recursive drawing is contained on the screen (at whatever size you set it).
#  All three recursive drawings can be on the same program.  Just use screen.clear() between problems.  Alternately, you could draw to three different screen objects.
#  Run your turtles at max speed.
#  Have fun!
 
#  Resource to help you out >>> https://docs.python.org/3.3/library/turtle

my_screen.exitonclick()