import random

agents = int(input("Enter number of representatives: "))
episodes = int(input("Enter number of simulations: "))

values = [0.0] * agents
counts = [0] * agents

for episode in range(episodes):

    agent = random.randint(0, agents - 1)

    handling_time = random.randint(2, 10)

    reward = -handling_time

    counts[agent] += 1

    values[agent] += (reward - values[agent]) / counts[agent]

print("\nEstimated Values:")

for i in range(agents):
    print("Representative", i + 1, "=", round(values[i], 2))

best = values.index(max(values))

print("\nBest Representative:", best + 1)
