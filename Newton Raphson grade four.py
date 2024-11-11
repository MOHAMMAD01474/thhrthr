def newton_raphson(c, initial_guess, tolerance=1e-7, max_iterations=1000):
    def f(x):
        return x**4 - c

    def f_prime(x):
        return 4 * x**3

    x = initial_guess
    for _ in range(max_iterations):
        x_new = x - f(x) / f_prime(x)
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new

    raise ValueError("Newton-Raphson method did not converge")


c = 10
initial_guess = 1.0  
root = newton_raphson(c, initial_guess)

print("The root of the equation x^4 - {} = 0 is equal to: {}".format(c, root))
