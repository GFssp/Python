import sys
import turtle

def border(t, screen_x, screen_y):
    """(Turtle, int, int)
    Draws a border around the canvas in red"""
    t.penup()
    t.home()
    t.forward(screen_x / 2)
    t.right(90)
    t.forward(screen_y / 2)
    t.setheading(180)
    t.pencolor('red')
    t.pendown()
    t.pensize(10)
    for distance in screen_x, screen_y, screen_x, screen_y:
        t.penup()
        t.home()

def square(t, size, color):
    t.pencolor(color)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)

def main():
    screen = turtle.Screen()
    screen.title('Square Demo')
    screen_x, screen_y = screen.screensize()
    t = turtle.Turtle()

    border(t, screen_x, screen_y)
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    t.pensize(3)
    for i, color in enumerate(colors):
        square(t, (screen_y / 2) / 10 * (i+1), color)

    print('Hit any key to exit')
    dummy = input()

if __name__ == '__main__':
    main()
