import random

agents = int(input("Enter number of representatives: "))
episodes = int(input("Enter episodes: "))

Q = [0.0] * agents
count = [0] * agents

epsilon = 0.2

for episode in range(episodes):

    if random.random() < epsilon:
        agent = random.randrange(agents)
    else:
        agent = Q.index(max(Q))

    handling_time = random.randint(2, 15)

    reward = -handling_time

    count[agent] += 1

    Q[agent] += (reward - Q[agent]) / count[agent]

print("\nAgent Values:")

for i in range(agents):
    print("Agent", i + 1, "=", round(Q[i], 2))

print("\nBest Assignment: Agent", Q.index(max(Q)) + 1)
