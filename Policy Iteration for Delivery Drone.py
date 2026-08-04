n = int(input("Enter grid size: "))

goal_r, goal_c = map(int, input("Enter goal row column: ").split())

gamma = 0.9

V = [[0 for j in range(n)] for i in range(n)]

actions = [(-1,0), (1,0), (0,-1), (0,1)]
names = ["Up", "Down", "Left", "Right"]

for iteration in range(20):

    newV = [row[:] for row in V]

    for r in range(n):
        for c in range(n):

            if (r, c) == (goal_r, goal_c):
                continue

            values = []

            for dr, dc in actions:
                nr = max(0, min(n-1, r + dr))
                nc = max(0, min(n-1, c + dc))

                reward = 10 if (nr, nc) == (goal_r, goal_c) else -1

                values.append(reward + gamma * V[nr][nc])

            newV[r][c] = max(values)

    V = newV

print("\nOptimal Policy:")

for r in range(n):
    for c in range(n):

        if (r, c) == (goal_r, goal_c):
            print("G", end="\t")
            continue

        values = []

        for dr, dc in actions:
            nr = max(0, min(n-1, r + dr))
            nc = max(0, min(n-1, c + dc))
            values.append(V[nr][nc])

        print(names[values.index(max(values))], end="\t")

    print()
