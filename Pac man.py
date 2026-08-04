import random

states = int(input("Enter number of grid positions: "))

food = int(input("Enter food position: "))
ghost = int(input("Enter ghost position: "))

Q = [[0.0, 0.0] for i in range(states)]

alpha = 0.1
gamma = 0.9
epsilon = 0.2

episodes = int(input("Enter episodes: "))

for episode in range(episodes):

    state = 0

    while state != food:

        if random.random() < epsilon:
            action = random.randint(0, 1)
        else:
            action = Q[state].index(max(Q[state]))

        if action == 0:
            next_state = max(0, state - 1)
        else:
            next_state = min(states - 1, state + 1)

        if next_state == food:
            reward = 10

        elif next_state == ghost:
            reward = -10

        else:
            reward = -1

        Q[state][action] += alpha * (
            reward
            + gamma * max(Q[next_state])
            - Q[state][action]
        )

        if next_state == ghost:
            break

        state = next_state

print("\nLearned Q-Table:")

for i in range(states):
    print(i, Q[i])
