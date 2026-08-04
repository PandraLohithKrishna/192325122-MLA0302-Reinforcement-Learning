import random

settings = ["Low", "Medium", "High"]

Q = [0.0, 0.0, 0.0]
count = [0, 0, 0]

epsilon = float(input("Enter epsilon: "))
runs = int(input("Enter number of production runs: "))

for run in range(runs):

    if random.random() < epsilon:
        action = random.randint(0, 2)
    else:
        action = Q.index(max(Q))

    if action == 0:
        quality = random.randint(50, 75)

    elif action == 1:
        quality = random.randint(70, 90)

    else:
        quality = random.randint(60, 100)

    reward = quality

    count[action] += 1

    Q[action] += (
        reward - Q[action]
    ) / count[action]

print("\nMachine Setting Values:")

for i in range(3):
    print(settings[i], "=", round(Q[i], 2))

print("\nBest Setting:", settings[Q.index(max(Q))])
