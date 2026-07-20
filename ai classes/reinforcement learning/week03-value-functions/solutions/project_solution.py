"""Week 3 reference solution: evaluate a fixed policy on Gridworld."""

import matplotlib.pyplot as plt
import numpy as np


ACTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}


class Gridworld:
    """The deterministic Gridworld introduced in Week 2."""

    def __init__(self):
        self.rows, self.cols = 5, 5
        self.start, self.goal, self.pit = (0, 0), (4, 4), (4, 3)
        self.walls = {(0, 3), (1, 1), (1, 3), (2, 1), (3, 2), (3, 3)}
        self.states = [
            (row, col)
            for row in range(self.rows)
            for col in range(self.cols)
            if (row, col) not in self.walls
        ]
        self.terminal_states = {self.goal, self.pit}

    def transition(self, state, action):
        """Return (next_state, reward, done) without changing the world."""
        if state not in self.states or state in self.terminal_states:
            raise ValueError("state must be a nonterminal Gridworld state")
        if action not in ACTIONS:
            raise ValueError(f"unknown action: {action}")
        dr, dc = ACTIONS[action]
        candidate = (state[0] + dr, state[1] + dc)
        valid = (
            0 <= candidate[0] < self.rows
            and 0 <= candidate[1] < self.cols
            and candidate not in self.walls
        )
        next_state = candidate if valid else state
        reward = 10 if next_state == self.goal else -10 if next_state == self.pit else -1
        return next_state, reward, next_state in self.terminal_states


def random_policy(env):
    """Return {state: {action: probability}} for nonterminal states."""
    probability = 1.0 / len(ACTIONS)
    return {
        state: {action: probability for action in ACTIONS}
        for state in env.states
        if state not in env.terminal_states
    }


def sample_action(action_probabilities, rng):
    actions = list(action_probabilities)
    probabilities = [action_probabilities[action] for action in actions]
    return str(rng.choice(actions, p=probabilities))


def sample_return(env, policy, start_state, gamma=0.9, max_steps=200, seed=None):
    """Sample one discounted return following policy from start_state."""
    if start_state in env.terminal_states:
        return 0.0
    rng = np.random.default_rng(seed)
    state = start_state
    total = 0.0
    discount = 1.0
    for _ in range(max_steps):
        action = sample_action(policy[state], rng)
        state, reward, done = env.transition(state, action)
        total += discount * reward
        discount *= gamma
        if done:
            break
    return total


def q_from_v(env, state, action, values, gamma):
    """Compute q_pi(s, a) from a current state-value table."""
    next_state, reward, done = env.transition(state, action)
    return reward + gamma * (0.0 if done else values[next_state])


def evaluate_policy(env, policy, gamma=0.9, theta=1e-8, max_sweeps=10_000):
    """Return (values, deltas) from iterative Bellman expectation updates."""
    values = {state: 0.0 for state in env.states}
    deltas = []
    for _ in range(max_sweeps):
        delta = 0.0
        for state in env.states:
            if state in env.terminal_states:
                continue
            old_value = values[state]
            values[state] = sum(
                probability * q_from_v(env, state, action, values, gamma)
                for action, probability in policy[state].items()
            )
            delta = max(delta, abs(old_value - values[state]))
        deltas.append(delta)
        if delta < theta:
            return values, deltas
    raise RuntimeError("policy evaluation did not converge")


def plot_values(env, values, title="Value of the random policy"):
    grid = np.full((env.rows, env.cols), np.nan)
    for state, value in values.items():
        grid[state] = value
    color_map = plt.get_cmap("coolwarm").copy()
    color_map.set_bad("black")
    plt.imshow(np.ma.masked_invalid(grid), cmap=color_map)
    plt.colorbar(label="State value")
    for (row, col), value in values.items():
        plt.text(col, row, f"{value:.1f}", ha="center", va="center")
    plt.title(title)
    plt.tight_layout()


if __name__ == "__main__":
    world = Gridworld()
    policy = random_policy(world)
    values, deltas = evaluate_policy(world, policy, gamma=0.9)

    samples = [
        sample_return(world, policy, world.start, gamma=0.9, seed=seed)
        for seed in range(1_000)
    ]
    print("Bellman start value:", round(values[world.start], 3))
    print("Sampled start value:", round(float(np.mean(samples)), 3))
    print("Bellman sweeps:", len(deltas))

    plot_values(world, values)
    plt.show()
