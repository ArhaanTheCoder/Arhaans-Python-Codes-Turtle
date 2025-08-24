import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Arhaan's Turtle Tutorial")
screen.bgcolor("lightblue")  # optional, sets background color

# Create a turtle
my_turtle = turtle.Turtle()
my_turtle.pensize(3)  # optional, makes the line thicker
my_turtle.speed(1)    # turtle speed: 1 (slow) to 10 (fast)

# Draw a square
for _ in range(4):
    my_turtle.forward(100)  # makes the turtle draw 100 pixels for one side - changeable
    my_turtle.right(90)     # turns the turtle 90 degrees to the right

# Keep the window open until closed
turtle.done()

