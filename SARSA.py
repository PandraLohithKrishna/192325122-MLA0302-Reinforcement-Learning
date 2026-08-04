import random

states = int(input("Enter number of rooms: "))
goal = states - 1

Q = [[0.0, 0.0] for i in range(states)]

alpha = 0.1
gamma = 0.9
epsilon = 0.2

episodes = int(input("Enter episodes: "))

def choose_action(state):

    if random.random() < epsilon:
        return random.randint(0, 1)

    return Q[state].index(max(Q[state]))

for episode in range(episodes):

    state = 0
    action = choose_action(state)

    while state != goal:

        if action == 0:
            next_state = max(0, state - 1)
        else:
            next_state = min(goal, state + 1)

        reward = 10 if next_state == goal else -1

        next_action = choose_action(next_state)

        Q[state][action] += alpha * (
            reward
            + gamma * Q[next_state][next_action]
            - Q[state][action]
        )

        state = next_state
        action = next_action

print("\nLearned Q-Table:")

for i in range(states):
    print("Room", i, Q[i])
