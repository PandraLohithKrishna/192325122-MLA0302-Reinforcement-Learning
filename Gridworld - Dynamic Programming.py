n = int(input("Enter grid size: "))

goal_r, goal_c = map(int, input("Enter goal row column: ").split())

V = [[0.0] * n for i in range(n)]

gamma = 0.9

actions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

for iteration in range(30):

    newV = [row[:] for row in V]

    for r in range(n):
        for c in range(n):

            if (r, c) == (goal_r, goal_c):
                continue

            values = []

            for dr, dc in actions:

                nr = max(0, min(n - 1, r + dr))
                nc = max(0, min(n - 1, c + dc))

                values.append(-1 + gamma * V[nr][nc])

            newV[r][c] = max(values)

    V = newV

print("\nGrid Values:")

for row in V:
    print([round(x, 2) for x in row])
