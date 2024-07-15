import turtle

# Create a turtle screen and turtle object
screen = turtle.Screen()
t = turtle.Turtle()

# Function to draw a square
def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.left(120)

# Set starting position for the square
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw the square
draw_square()

# Set starting position for the triangle
t.penup()
t.goto(50, 0)
t.pendown()

# Draw the triangle
draw_triangle()

# Hide turtle and display result
t.hideturtle()
screen.mainloop()
