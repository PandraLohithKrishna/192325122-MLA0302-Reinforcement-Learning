import random

prices = list(map(int, input("Enter stock prices separated by space: ").split()))

actions = ["Buy", "Sell", "Hold"]

Q1 = [[0.0] * 3 for i in prices]
Q2 = [[0.0] * 3 for i in prices]

alpha = 0.1
gamma = 0.9
epsilon = 0.2

episodes = int(input("Enter training episodes: "))

for episode in range(episodes):

    for state in range(len(prices) - 1):

        if random.random() < epsilon:
            action = random.randint(0, 2)
        else:
            q = [Q1[state][a] + Q2[state][a] for a in range(3)]
            action = q.index(max(q))

        change = prices[state + 1] - prices[state]

        if action == 0:
            reward = change
        elif action == 1:
            reward = -change
        else:
            reward = 0

        if random.random() < 0.5:

            best = Q1[state + 1].index(max(Q1[state + 1]))

            target = reward + gamma * Q2[state + 1][best]

            Q1[state][action] += alpha * (
                target - Q1[state][action]
            )

        else:

            best = Q2[state + 1].index(max(Q2[state + 1]))

            target = reward + gamma * Q1[state + 1][best]

            Q2[state][action] += alpha * (
                target - Q2[state][action]
            )

print("\nLearned Trading Policy:")

for state in range(len(prices) - 1):

    q = [Q1[state][a] + Q2[state][a] for a in range(3)]

    print("Price", prices[state], "->", actions[q.index(max(q))])
