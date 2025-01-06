import turtle
import random
import math

# Ask the user for the number of triangles, squares, and rectangles
num_triangles = int(input("Enter the number of triangles: "))
num_squares = int(input("Enter the number of squares: "))
num_rectangles = int(input("Enter the number of rectangles: "))

# Calculate the area of shapes
triangle_area = num_triangles * (0.5 * (30 * 30))  # Example area for an equilateral triangle with side length 30
square_area = num_squares * (20 * 20)              # Example area for a square with side length 20
rectangle_area = num_rectangles * (20 * 10)        # Example area for a rectangle with width 20 and height 10

# Calculate the total area and double it for the big shape
total_area = triangle_area + square_area + rectangle_area
big_shape_area = 2 * total_area

# Define the dimensions of the big shape (assuming it's a rectangle)
big_shape_width = math.sqrt(big_shape_area)
big_shape_height = big_shape_area / big_shape_width

wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.bgcolor("white")
wn.tracer(0)

class Shape:
    def __init__(self, shape_type, speed):
        self.shape_type = shape_type
        self.speed = speed
        self.turtle = turtle.Turtle(shape=shape_type)
        self.turtle.penup()
        self.turtle.goto(random.uniform(-big_shape_width/2, big_shape_width/2), random.uniform(-big_shape_height/2, big_shape_height/2))
        self.turtle.speed(speed)
        self.count = 0

    def move(self):
        x = self.turtle.xcor() + random.uniform(-self.speed, self.speed)
        y = self.turtle.ycor() + random.uniform(-self.speed, self.speed)
        if abs(x) < big_shape_width / 2 and abs(y) < big_shape_height / 2:
            self.turtle.goto(x, y)
        else:
            self.turtle.goto(self.turtle.xcor() - random.uniform(-self.speed, self.speed), self.turtle.ycor() - random.uniform(-self.speed, self.speed))

    def transform(self, shape_type):
        self.turtle.shape(shape_type)
        self.shape_type = shape_type

class Triangle(Shape):
    def __init__(self, speed):
        super().__init__("triangle", speed)

class Square(Shape):
    def __init__(self, speed):
        super().__init__("square", speed)

class Rectangle(Shape):
    def __init__(self, speed):
        super().__init__("square", speed)
        self.turtle.shapesize(stretch_wid=1, stretch_len=2)

def check_collision(shape1, shape2):
    return shape1.turtle.distance(shape2.turtle) < 20

def remove_shape(shape):
    shape.turtle.hideturtle()
    shape.turtle.clear()
    shape.turtle.penup()
    shape.turtle.goto(1000, 1000)  # move shape off screen

# Create shapes
shapes = []
for _ in range(num_triangles):
    shapes.append(Triangle(random.randint(5, 20)))
for _ in range(num_squares):
    shapes.append(Square(random.randint(5, 20)))
for _ in range(num_rectangles):
    shapes.append(Rectangle(random.randint(5, 20)))

# Move shapes within the big shape and check for collisions
while len(shapes) > 1:
    for shape in shapes:
        shape.move()
    
    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            if check_collision(shapes[i], shapes[j]):
                print(f"Collision between {shapes[i].shape_type} and {shapes[j].shape_type}")
                shapes[i].count += 1
                if shapes[i].count >= shapes[j].count:
                    shapes[j].transform(shapes[i].shape_type)
                    shapes[i].count += shapes[j].count
                    remove_shape(shapes[j])
                    shapes.pop(j)
                else:
                    shapes[i].transform(shapes[j].shape_type)
                    shapes[j].count += shapes[i].count
                    remove_shape(shapes[i])
                    shapes.pop(i)
                break
    
    wn.update()

# Find the winning shape
winning_shape = shapes[0] if shapes else None
if winning_shape:
    print(f"Only one shape left! The winner is: {winning_shape.shape_type} with {winning_shape.count} collisions")

# Draw the winning shape in the center
if winning_shape:
    wn.clearscreen()
    wn.bgcolor("white")
    winning_shape.turtle.goto(0, 0)
    winning_shape.turtle.showturtle()
    print(f"The winning shape is: {winning_shape.shape_type}")

wn.mainloop()
