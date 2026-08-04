import random

episodes = int(input("Enter number of customers: "))

total_return = 0

for episode in range(episodes):

    churn_probability = float(
        input("Enter churn probability for customer "
              + str(episode + 1) + ": ")
    )

    if random.random() < churn_probability:
        reward = -1
    else:
        reward = 1

    total_return += reward

value = total_return / episodes

print("\nEstimated Policy Value:", round(value, 2))

if value > 0:
    print("Policy performs well")
else:
    print("Policy needs improvement")
