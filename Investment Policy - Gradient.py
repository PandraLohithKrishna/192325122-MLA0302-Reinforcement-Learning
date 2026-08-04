import random

actions = ["Stock", "Bond"]

weights = [0.5, 0.5]

alpha = float(input("Enter learning rate: "))
episodes = int(input("Enter number of episodes: "))

for episode in range(episodes):

    total = sum(weights)

    probabilities = [w / total for w in weights]

    action = random.choices([0, 1], weights=probabilities)[0]

    if action == 0:
        reward = random.uniform(-2, 5)
    else:
        reward = random.uniform(0, 2)

    weights[action] += alpha * reward

    weights[action] = max(0.01, weights[action])

print("\nFinal Policy:")

total = sum(weights)

for i in range(2):
    print(actions[i], ":", round(weights[i] / total, 3))
