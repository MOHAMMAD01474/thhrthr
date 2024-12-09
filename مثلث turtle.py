0import turtle
def draw_triangle(x1, y1, x2, y2, x3, y3):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.done()
x1, y1 = map(int, input("Coordinates of the first point (x1, y1): ").split()) # 0,0
x2, y2 = map(int, input("Coordinates of the first point (x2, y2): ").split()) # 100,0
x3, y3 = map(int, input("Coordinates of the first point (x3, y3): ").split()) # 50 , 100
draw_triangle(x1, y1, x2, y2, x3, y3)
