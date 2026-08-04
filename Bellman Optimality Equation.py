n = int(input("Enter number of states: "))
goal = int(input("Enter goal state: "))

V = [0.0] * n

gamma = 0.9

for iteration in range(30):

    newV = V.copy()

    for state in range(n):

        if state == goal:
            newV[state] = 10
            continue

        left = max(0, state - 1)
        right = min(n - 1, state + 1)

        left_value = -1 + gamma * V[left]
        right_value = -1 + gamma * V[right]

        newV[state] = max(left_value, right_value)

    V = newV

print("\nOptimal State Values:")

for i in range(n):
    print("State", i, "=", round(V[i], 2))

print("\nOptimal Path:")

state = 0

while state != goal:

    print(state, end=" -> ")

    if state < goal:
        state += 1
    else:
        state -= 1

print(goal)
