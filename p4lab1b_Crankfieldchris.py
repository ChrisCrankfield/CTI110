import turtle

# Create a turtle screen and turtle object
screen = turtle.Screen()
t = turtle.Turtle()

# Function to draw initials
def draw_initials():
    t.pensize(5)
    t.pencolor("green")
    
    # Draw first initial 'C'
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    t.circle(50, -180)
    t.penup()
    
    # Move to draw second initial 'C'
    t.goto(50, 0)
    t.pendown()
    t.circle(50, -180)

# Draw initials
draw_initials()

# Hide turtle and display result
t.hideturtle()
screen.mainloop()

