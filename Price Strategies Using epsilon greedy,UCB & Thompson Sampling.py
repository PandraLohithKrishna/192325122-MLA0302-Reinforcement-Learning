import random
import math

prices = [10, 20, 30]
success = [0.8, 0.5, 0.3]

n = int(input("Enter number of pricing decisions: "))
epsilon = float(input("Enter epsilon value: "))

# Epsilon Greedy
count = [0] * 3
value = [0.0] * 3
revenue1 = 0

for t in range(n):

    if random.random() < epsilon:
        arm = random.randint(0, 2)
    else:
        arm = value.index(max(value))

    sale = 1 if random.random() < success[arm] else 0
    reward = prices[arm] * sale

    count[arm] += 1
    value[arm] += (reward - value[arm]) / count[arm]
    revenue1 += reward

# UCB
count = [0] * 3
value = [0.0] * 3
revenue2 = 0

for t in range(1, n + 1):

    if 0 in count:
        arm = count.index(0)
    else:
        ucb = [
            value[i] + math.sqrt(2 * math.log(t) / count[i])
            for i in range(3)
        ]
        arm = ucb.index(max(ucb))

    sale = 1 if random.random() < success[arm] else 0
    reward = prices[arm] * sale

    count[arm] += 1
    value[arm] += (reward - value[arm]) / count[arm]
    revenue2 += reward

# Thompson Sampling
alpha = [1] * 3
beta = [1] * 3
revenue3 = 0

for t in range(n):

    samples = [
        random.betavariate(alpha[i], beta[i])
        for i in range(3)
    ]

    arm = samples.index(max(samples))

    sale = 1 if random.random() < success[arm] else 0
    revenue3 += prices[arm] * sale

    if sale:
        alpha[arm] += 1
    else:
        beta[arm] += 1

print("\nEpsilon-Greedy Revenue:", revenue1)
print("UCB Revenue:", revenue2)
print("Thompson Sampling Revenue:", revenue3)

revenues = [revenue1, revenue2, revenue3]
names = ["Epsilon-Greedy", "UCB", "Thompson Sampling"]

print("Best Strategy:", names[revenues.index(max(revenues))])
