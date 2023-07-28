import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    Wilson = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    Wilson.shape('turtle')
    # Set your turtle's speed using .speed(2)
    Wilson.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    Wilson.color('green')
    Wilson.pencolor('blue')
    # Move your turtle forward using .forward(100)
    for i in range(4):
        Wilson.forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
        Wilson.left(90)

    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    Wilson.goto(200, 100)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    Wilson.begin_fill()
    Wilson.circle(70, steps=20)
    Wilson.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    Wilson.goto(100,-200)
    Wilson.begin_fill()
    for i in range(4):
        Wilson.forward(150)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
        Wilson.left(90)
    Wilson.end_fill()

    Wilson.goto(30, 100)
    Wilson.begin_fill()
    Wilson.circle(100, steps=20)
    Wilson.end_fill()
    Wilson.goto(-400, 30)
    Wilson.begin_fill()
    for i in range(4):
        Wilson.forward(300)
        Wilson.left(90)
    Wilson.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
