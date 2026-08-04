import random

destination = int(input("Enter destination position: "))
position = 0

safe_moves = 0
steps = 0

print("\nCar starts at position 0")

while position < destination:

    traffic = random.choice(["Green", "Red"])

    print("\nTraffic Light:", traffic)

    if traffic == "Green":
        position += 1
        safe_moves += 1
        print("Car moves to:", position)

    else:
        print("Car stops")

    steps += 1

print("\nDestination reached!")
print("Total Steps:", steps)
print("Safe Moves:", safe_moves)
print("Policy: Move on Green, Stop on Red")
