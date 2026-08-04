states = ["A", "B", "C", "Goal"]

rewards = {
    "A": 0,
    "B": 2,
    "C": 0,
    "Goal": 5
}

policy = {
    "A": "B",
    "B": "C",
    "C": "Goal"
}

gamma = float(input("Enter discount factor (example 0.9): "))

V = {s: 0 for s in states}

iterations = int(input("Enter number of iterations: "))

for i in range(iterations):
    newV = V.copy()

    for state in policy:
        next_state = policy[state]
        newV[state] = rewards[next_state] + gamma * V[next_state]

    V = newV

print("\nState Value Function:")

for state in states:
    print(state, "=", round(V[state], 2))
