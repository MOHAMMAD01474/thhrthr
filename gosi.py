import turtle
import math
def gaussian_cdf(x, mean, std_dev):
    return 0.5 * (1 + math.erf((x - mean) / (std_dev * math.sqrt(2))))
def draw_gaussian_cdfs(x, means, std_devs, lower_bound, upper_bound):
    screen = turtle.Screen()
    screen.setworldcoordinates(lower_bound, 0, upper_bound, 1)
    screen.title("Gaussian Cumulative Distribution Functions")
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    step = (upper_bound - lower_bound) / 1000
    for mean in means:
        for std_dev in std_devs:
            x_val = lower_bound
            y_val = gaussian_cdf(x_val, mean, std_dev)
            my_turtle.penup()
            my_turtle.goto(x_val, y_val)
            my_turtle.pendown()
            while x_val <= upper_bound:
                y_val = gaussian_cdf(x_val, mean, std_dev)
                my_turtle.goto(x_val, y_val)
                x_val += step
            y_at_10 = gaussian_cdf(10, mean, std_dev)
            my_turtle.penup()
            my_turtle.goto(10, y_at_10)
            my_turtle.pendown()
            my_turtle.dot(5, "red")
    turtle.done()
if __name__ == "__main__":
    means = [15, 30, 45]
    std_devs = [1, 2, 5]
    lower_bound = -50
    upper_bound = 50
    draw_gaussian_cdfs(10, means, std_devs, lower_bound, upper_bound)
