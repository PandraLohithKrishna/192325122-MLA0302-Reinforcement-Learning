import random

n = 5

dirt = []
obstacles = []

d = int(input("Enter number of dirt cells: "))
for i in range(d):
    r, c = map(int, input("Enter dirt row column: ").split())
    dirt.append((r, c))

o = int(input("Enter number of obstacles: "))
for i in range(o):
    r, c = map(int, input("Enter obstacle row column: ").split())
    obstacles.append((r, c))

actions = [(-1,0), (1,0), (0,-1), (0,1)]
names = ["Up", "Down", "Left", "Right"]

state = (0, 0)
reward = 0

print("\nRobot starts at:", state)

while dirt:
    action = random.randint(0, 3)

    nr = state[0] + actions[action][0]
    nc = state[1] + actions[action][1]

    if 0 <= nr < n and 0 <= nc < n:
        new_state = (nr, nc)

        if new_state in obstacles:
            reward -= 1
            print("Obstacle! Reward = -1")
        else:
            state = new_state

            if state in dirt:
                reward += 1
                dirt.remove(state)
                print("Cleaned dirt at", state, "Reward = +1")

    print("Action:", names[action], "Position:", state)

print("\nAll dirt cleaned")
print("Total Reward:", reward)
