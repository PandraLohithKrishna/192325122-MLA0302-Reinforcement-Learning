n = int(input("Enter number of locations: "))
goal = int(input("Enter pickup location (0 to n-1): "))

gamma = 0.9

V = [0.0] * n

for iteration in range(20):

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
    print("Location", i, "=", round(V[i], 2))

print("\nOptimal Policy:")

for state in range(n):

    if state == goal:
        print(state, ": Pickup")
    elif state < goal:
        print(state, ": Move Right")
    else:
        print(state, ": Move Left")
