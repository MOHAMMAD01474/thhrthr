import turtle
import random

def draw_coral(num_particles, start_x, start_y):
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Coral Reef Simulation")
    screen.setup(width=1200, height=1200)

    coral = turtle.Turtle()
    coral.hideturtle()
    coral.speed(999)
    coral.color("cyan")
    coral.penup()
    
    x, y = start_x, start_y  
    positions = [(x, y)]
    
    for _ in range(num_particles):
        growing = True
        
        while growing:
            rand = random.random()
            if rand < 0.40: 
                x_new = 0.31 * x - 0.53 * y + 0.89
                y_new = -0.46 * x - 0.29 * y + 1.04
            elif rand < 0.55: 
                x_new = 0.31 * x - 0.08 * y + 0.22
                y_new = -0.15 * x - 0.45 * y + 0.34
            else:  
                x_new = 0.55 * y + 0.01
                y_new = -0.69 * x - 0.20 * y + 0.38
            
            if -590 < x_new < 590 and -590 < y_new < 590:
                for pos in positions:
                    if abs(x_new - pos[0]) <= 10 and abs(y_new - pos[1]) <= 10:
                        coral.goto(x_new, y_new)
                        coral.pendown()
                        coral.dot(3, "cyan")
                        coral.penup()
                        positions.append((x_new, y_new))
                        growing = False
                        break
            x, y = x_new, y_new
    screen.exitonclick()

num_particles = 10000000
start_x = float(input("Enter the starting x-coordinate: "))  
start_y = float(input("Enter the starting y-coordinate: "))  

draw_coral(num_particles, start_x, start_y)
