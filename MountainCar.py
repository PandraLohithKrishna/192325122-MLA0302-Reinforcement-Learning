import gymnasium as gym

episodes = int(input("Enter number of episodes: "))

env = gym.make("MountainCar-v0", render_mode="human")

for episode in range(episodes):

    state, info = env.reset()

    total_reward = 0

    for step in range(200):

        position = state[0]
        velocity = state[1]

        # Simple policy
        if velocity > 0:
            action = 2
        else:
            action = 0

        state, reward, terminated, truncated, info = env.step(action)

        total_reward += reward

        if terminated or truncated:
            break

    print("Episode:", episode + 1,
          "Reward:", total_reward)

env.close()
