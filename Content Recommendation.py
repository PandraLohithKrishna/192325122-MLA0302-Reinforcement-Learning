import random

contents = int(input("Enter number of contents: "))
runs = int(input("Enter number of recommendations: "))

epsilon = float(input("Enter epsilon value: "))

true_rewards = []

for i in range(contents):
    value = float(
        input("Enter success probability for Content "
              + str(i + 1) + ": ")
    )

    true_rewards.append(value)

Q = [0.0] * contents
count = [0] * contents

total_reward = 0

for t in range(runs):

    # Exploration
    if random.random() < epsilon:
        action = random.randrange(contents)

    # Exploitation
    else:
        action = Q.index(max(Q))

    reward = (
        1 if random.random() < true_rewards[action]
        else 0
    )

    count[action] += 1

    Q[action] += (
        reward - Q[action]
    ) / count[action]

    total_reward += reward

print("\nEstimated Content Values:")

for i in range(contents):
    print("Content", i + 1, "=", round(Q[i], 3))

print("\nTotal Reward:", total_reward)
print("Best Content:", Q.index(max(Q)) + 1)
