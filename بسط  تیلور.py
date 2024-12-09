import math
def gaussian_pdf(x, mean, std_dev):
    return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mean) / std_dev) ** 2)
def taylor_expansion_cdf(x, mean, std_dev, degree):
    taylor_sum = 0
    for n in range(degree + 1):
        taylor_term = ((x - mean) ** n) / (math.factorial(n) * (std_dev ** n)) * gaussian_pdf(mean, mean, std_dev)
        taylor_sum += taylor_term
    return 0.5 * (1 + taylor_sum)
def probability_less_than_75(means, std_devs, degree=10):
    x = 75
    probabilities = []
    for mean in means:
        for std_dev in std_devs:
            prob = taylor_expansion_cdf(x, mean, std_dev, degree)
            probabilities.append((mean, std_dev, prob))
    return probabilities
if __name__ == "__main__":
    means = [15, 30, 45]
    std_devs = [1, 2, 5]
    
    probabilities = probability_less_than_75(means, std_devs)
    for mean, std_dev, prob in probabilities:
        print(f" Average:{mean}, standard deviation: {std_dev},Probability less than 75:  {prob:.4f}")