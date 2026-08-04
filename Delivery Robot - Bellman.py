n = int(input("Enter number of states: "))
goal = int(input("Enter delivery state: "))

gamma = float(input("Enter discount factor: "))

V = [0.0] * n

for iteration in range(20):

    newV = V.copy()

    for state in range(n):

        if state == goal:
            newV[state] = 10
        else:
            next_state = min(state + 1, n - 1)
            reward = -1

            newV[state] = reward + gamma * V[next_state]

    V = newV

print("\nState Value Function:")

for i in range(n):
    print("State", i, "=", round(V[i], 2))
