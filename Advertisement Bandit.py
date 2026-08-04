import random
import math

ads = int(input("Enter number of advertisements: "))
runs = int(input("Enter number of users: "))

true_ctr = []

for i in range(ads):
    p = float(input("Enter CTR probability for Ad " + str(i+1) + ": "))
    true_ctr.append(p)

epsilon = 0.1

# Epsilon Greedy
count = [0] * ads
value = [0.0] * ads
clicks1 = 0

for t in range(runs):

    if random.random() < epsilon:
        ad = random.randrange(ads)
    else:
        ad = value.index(max(value))

    click = 1 if random.random() < true_ctr[ad] else 0

    count[ad] += 1
    value[ad] += (click - value[ad]) / count[ad]
    clicks1 += click

# UCB
count = [0] * ads
value = [0.0] * ads
clicks2 = 0

for t in range(1, runs + 1):

    if 0 in count:
        ad = count.index(0)
    else:
        ucb = [
            value[i] + math.sqrt(2 * math.log(t) / count[i])
            for i in range(ads)
        ]
        ad = ucb.index(max(ucb))

    click = 1 if random.random() < true_ctr[ad] else 0

    count[ad] += 1
    value[ad] += (click - value[ad]) / count[ad]
    clicks2 += click

# Thompson
alpha = [1] * ads
beta = [1] * ads
clicks3 = 0

for t in range(runs):

    samples = [
        random.betavariate(alpha[i], beta[i])
        for i in range(ads)
    ]

    ad = samples.index(max(samples))

    click = 1 if random.random() < true_ctr[ad] else 0

    if click:
        alpha[ad] += 1
    else:
        beta[ad] += 1

    clicks3 += click

print("\nEpsilon-Greedy CTR:", clicks1 / runs)
print("UCB CTR:", clicks2 / runs)
print("Thompson CTR:", clicks3 / runs)
