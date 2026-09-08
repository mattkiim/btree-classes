"""Week 5 reference solution: learn state values from complete episodes."""

from random import Random


class Gridworld:
    """The deterministic three-by-three environment from Week 3."""

    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.start_state = (0, 0)
        self.wall_states = {(1, 1)}
        self.action_changes = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }
        self.terminal_rewards = {
            (0, 2): 10,
            (2, 2): -10,
        }
        self.step_reward = -1
        self.state = self.start_state
        self.done = False

    def reset(self):
        self.state = self.start_state
        self.done = False
        return self.state

    def is_inside(self, state):
        row, column = state
        return 0 <= row < self.rows and 0 <= column < self.columns

    def move(self, action):
        if action not in self.action_changes:
            raise ValueError(f"Unknown action: {action}")

        row_change, column_change = self.action_changes[action]
        row, column = self.state
        candidate_state = (row + row_change, column + column_change)

        if (
            self.is_inside(candidate_state)
            and candidate_state not in self.wall_states
        ):
            self.state = candidate_state

        return self.state

    def step(self, action):
        if self.done:
            raise RuntimeError("Episode is finished. Call reset().")

        next_state = self.move(action)
        reward = self.terminal_rewards.get(next_state, self.step_reward)
        self.done = next_state in self.terminal_rewards
        return next_state, reward, self.done


class StateValueAgent:
    """Follow a small branching policy and average observed returns."""

    def __init__(self, seed=None):
        # The start has two choices; every later choice is fixed.
        self.action_choices = {
            (0, 0): ("right", "down"),
            (0, 1): ("right",),
            (1, 0): ("down",),
            (1, 2): ("up",),
            (2, 0): ("right",),
            (2, 1): ("right",),
        }
        self.randomizer = Random(seed)

        # Keep the same average ingredients used for bandit arms in Week 2.
        states = self.action_choices
        self.counts = {state: 0 for state in states}
        self.total_returns = {state: 0.0 for state in states}
        self.values = {state: 0.0 for state in states}

    def choose_action(self, state):
        """Choose from the policy's allowed actions at one state."""
        choices = self.action_choices[state]

        if len(choices) == 1:
            return choices[0]

        return self.randomizer.choice(choices)

    def learn_from_episode(self, history):
        """Use one complete episode to update each visited state's value."""
        future_total = 0

        for state, action, next_state, reward in reversed(history):
            future_total = reward + future_total
            self.counts[state] += 1
            self.total_returns[state] += future_total
            self.values[state] = (
                self.total_returns[state] / self.counts[state]
            )


def run_episode(world, agent):
    """Collect one episode, then let the agent learn from it."""
    state = world.reset()
    history = []
    total_reward = 0

    while not world.done:
        action = agent.choose_action(state)
        next_state, reward, done = world.step(action)
        history.append((state, action, next_state, reward))
        total_reward += reward
        state = next_state

    agent.learn_from_episode(history)
    return history, total_reward


def train(world, agent, number_of_episodes):
    """Run complete episodes and record the changing start-state estimate."""
    episode_rewards = []
    start_value_history = []

    for _ in range(number_of_episodes):
        history, total_reward = run_episode(world, agent)
        episode_rewards.append(total_reward)
        start_value_history.append(agent.values[world.start_state])

    return episode_rewards, start_value_history


def plot_learning(start_value_history):
    """Plot the learned start-state value after each episode."""
    # Import the plotting tool only when a graph is requested.
    import matplotlib.pyplot as plt

    episodes = range(1, len(start_value_history) + 1)
    plt.figure(figsize=(10, 5))
    plt.plot(episodes, start_value_history, color="teal", linewidth=2)
    plt.axhline(
        -2,
        color="coral",
        linestyle="--",
        label="average of the two possible returns",
    )
    plt.title("Learned value of the starting state")
    plt.xlabel("completed episode")
    plt.ylabel("estimated future reward")
    plt.legend()
    plt.tight_layout()


if __name__ == "__main__":
    gridworld = Gridworld()
    agent = StateValueAgent(seed=7)

    rewards, start_values = train(
        gridworld,
        agent,
        number_of_episodes=200,
    )

    print("goal episodes:", rewards.count(9))
    print("trap episodes:", rewards.count(-13))
    print("start count:  ", agent.counts[(0, 0)])
    print("start value:  ", round(agent.values[(0, 0)], 2))
    print("unvisited count:", agent.counts[(1, 2)])

    plot_learning(start_values)

    import matplotlib.pyplot as plt

    plt.show()
