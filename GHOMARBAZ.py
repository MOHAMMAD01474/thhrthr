import random
def gambler_ruin(initial_funds, goal, num_trials, win_prob=0.5):
    """
    Simulating the gambler's bankruptcy problem.
    :param initial_funds: Gambler's initial funds
    :param goal: monetary goal
    :param num_trials: Number of simulation times
    :param win_prob: Probability of winning a game round
    :return: The probability of reaching the goal
    """
    successes = 0
    for _ in range(num_trials):
        funds = initial_funds
        while funds > 0 and funds < goal:
            if random.random() < win_prob:
                funds += 1  
            else:
                funds -= 1  

        if funds >= goal:
            successes += 1
    return successes / num_trials
initial_funds = 10
goal = 20
num_trials = 10000

probability_of_success = gambler_ruin(initial_funds, goal, num_trials)
print("Probability of reaching the goal:", probability_of_success)