"""Week 6 reference solution: update state values after every step."""

from random import Random


class Gridworld:
    """The deterministic three-by-three environment from earlier weeks."""

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


def one_step_target(reward, next_value, done):
    """Build a learning target from one reward and the next estimate."""
    if done:
        return reward

    return reward + next_value


class StepValueAgent:
    """Follow the Week 5 policy and update values after each transition."""

    def __init__(self, learning_rate=0.1, seed=None):
        self.action_choices = {
            (0, 0): ("right", "down"),
            (0, 1): ("right",),
            (1, 0): ("down",),
            (1, 2): ("up",),
            (2, 0): ("right",),
            (2, 1): ("right",),
        }
        self.randomizer = Random(seed)
        self.learning_rate = learning_rate
        self.values = {
            state: 0.0
            for state in self.action_choices
        }
        self.counts = {
            state: 0
            for state in self.action_choices
        }

    def choose_action(self, state):
        """Choose an action from the fixed branching policy."""
        choices = self.action_choices[state]

        if len(choices) == 1:
            return choices[0]

        return self.randomizer.choice(choices)

    def learn(self, state, reward, next_state, done):
        """Move one state estimate partway toward a one-step target."""
        if done:
            next_value = 0.0
        else:
            next_value = self.values[next_state]

        target = one_step_target(reward, next_value, done)
        gap = target - self.values[state]
        change = self.learning_rate * gap
        self.values[state] += change
        self.counts[state] += 1
        return target


def run_episode(world, agent):
    """Run one episode and update the agent after every step."""
    state = world.reset()
    history = []
    total_reward = 0

    while not world.done:
        action = agent.choose_action(state)
        next_state, reward, done = world.step(action)

        # Learn now, without waiting for the rest of the episode.
        agent.learn(state, reward, next_state, done)

        history.append((state, action, next_state, reward))
        total_reward += reward
        state = next_state

    return history, total_reward


def train(world, agent, number_of_episodes):
    """Run episodes and record the changing start-state estimate."""
    episode_rewards = []
    start_value_history = []

    for _ in range(number_of_episodes):
        history, total_reward = run_episode(world, agent)
        episode_rewards.append(total_reward)
        start_value_history.append(agent.values[world.start_state])

    return episode_rewards, start_value_history


def plot_learning(start_value_history):
    """Plot the step-updated estimate after each completed episode."""
    import matplotlib.pyplot as plt

    episodes = range(1, len(start_value_history) + 1)
    plt.figure(figsize=(10, 5))
    plt.plot(episodes, start_value_history, color="teal", linewidth=2)
    plt.axhline(
        -2,
        color="coral",
        linestyle="--",
        label="long-run value under the policy",
    )
    plt.title("Step-by-step estimate of the starting state")
    plt.xlabel("completed episode")
    plt.ylabel("estimated future reward")
    plt.legend()
    plt.tight_layout()


if __name__ == "__main__":
    gridworld = Gridworld()
    agent = StepValueAgent(learning_rate=0.1, seed=7)

    rewards, start_values = train(
        gridworld,
        agent,
        number_of_episodes=1000,
    )

    print("goal episodes:", rewards.count(9))
    print("trap episodes:", rewards.count(-13))
    print("start updates:", agent.counts[(0, 0)])
    print("start value:  ", round(agent.values[(0, 0)], 2))
    print("goal-side value:", round(agent.values[(0, 1)], 2))
    print("trap-side value:", round(agent.values[(1, 0)], 2))

    plot_learning(start_values)

    import matplotlib.pyplot as plt

    plt.show()
