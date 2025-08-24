import turtle

# Create a screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()

# Draw a triangle
for _ in range(3):
    t.forward(100)  # Move forward 100 pixels
    t.left(120)     # Turn 120 degrees

# Keep the window open
screen.mainloop()
