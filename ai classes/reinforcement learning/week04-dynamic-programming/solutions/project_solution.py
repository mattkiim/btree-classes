"""Week 4 reference solution: solve Gridworld with dynamic programming."""

import matplotlib.pyplot as plt
import numpy as np


ACTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}
ARROWS = {"UP": "↑", "DOWN": "↓", "LEFT": "←", "RIGHT": "→"}


class Gridworld:
    """The deterministic 5x5 Gridworld used in Weeks 2 and 3."""

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

    @property
    def decision_states(self):
        return [state for state in self.states if state not in self.terminal_states]

    def transition(self, state, action):
        if state not in self.states or state in self.terminal_states:
            raise ValueError("state must be a nonterminal Gridworld state")
        if action not in ACTIONS:
            raise ValueError(f"unknown action: {action}")
        dr, dc = ACTIONS[action]
        candidate = (state[0] + dr, state[1] + dc)
        in_bounds = 0 <= candidate[0] < self.rows and 0 <= candidate[1] < self.cols
        next_state = candidate if in_bounds and candidate not in self.walls else state
        reward = 10 if next_state == self.goal else -10 if next_state == self.pit else -1
        return next_state, reward, next_state in self.terminal_states


def action_value(env, state, action, values, gamma):
    next_state, reward, done = env.transition(state, action)
    return reward + gamma * (0.0 if done else values[next_state])


def greedy_actions(env, state, values, gamma, atol=1e-10):
    """Return a list containing every action tied for the maximum."""
    scores = {
        action: action_value(env, state, action, values, gamma)
        for action in ACTIONS
    }
    best_score = max(scores.values())
    return [
        action for action, score in scores.items()
        if np.isclose(score, best_score, atol=atol)
    ]


def policy_evaluation(env, policy, gamma=0.9, theta=1e-8):
    """Evaluate a deterministic {state: action} policy."""
    values = {state: 0.0 for state in env.states}
    sweeps = 0
    while True:
        sweeps += 1
        delta = 0.0
        for state in env.decision_states:
            old_value = values[state]
            values[state] = action_value(env, state, policy[state], values, gamma)
            delta = max(delta, abs(old_value - values[state]))
        if delta < theta:
            return values, sweeps


def improve_policy(env, policy, values, gamma=0.9):
    """Return (greedy_policy, stable), breaking ties by ACTIONS order."""
    improved = {
        state: greedy_actions(env, state, values, gamma)[0]
        for state in env.decision_states
    }
    stable = all(improved[state] == policy[state] for state in env.decision_states)
    return improved, stable


def policy_iteration(env, initial_policy, gamma=0.9, theta=1e-8,
                     max_iterations=100):
    """Return (values, policy, history, evaluation_sweeps)."""
    policy = initial_policy.copy()
    history = []
    total_evaluation_sweeps = 0
    for _ in range(max_iterations):
        values, sweeps = policy_evaluation(env, policy, gamma, theta)
        total_evaluation_sweeps += sweeps
        history.append(values.copy())
        policy, stable = improve_policy(env, policy, values, gamma)
        if stable:
            return values, policy, history, total_evaluation_sweeps
    raise RuntimeError("policy iteration did not stabilize")


def value_iteration(env, gamma=0.9, theta=1e-8, max_sweeps=10_000):
    """Return (values, greedy_policy, history)."""
    values = {state: 0.0 for state in env.states}
    history = []
    for _ in range(max_sweeps):
        delta = 0.0
        for state in env.decision_states:
            old_value = values[state]
            values[state] = max(
                action_value(env, state, action, values, gamma)
                for action in ACTIONS
            )
            delta = max(delta, abs(old_value - values[state]))
        history.append(values.copy())
        if delta < theta:
            policy = {
                state: greedy_actions(env, state, values, gamma)[0]
                for state in env.decision_states
            }
            return values, policy, history
    raise RuntimeError("value iteration did not converge")


def rollout(env, policy, start=None, max_steps=100):
    """Return transition records from a deterministic policy."""
    state = env.start if start is None else start
    trajectory = []
    for _ in range(max_steps):
        if state in env.terminal_states:
            break
        action = policy[state]
        next_state, reward, done = env.transition(state, action)
        trajectory.append((state, action, reward, next_state))
        state = next_state
        if done:
            break
    return trajectory


def plot_value_policy(ax, env, values, policy=None, title=""):
    grid = np.full((env.rows, env.cols), np.nan)
    for state, value in values.items():
        grid[state] = value
    color_map = plt.get_cmap("coolwarm").copy()
    color_map.set_bad("black")
    ax.imshow(np.ma.masked_invalid(grid), cmap=color_map)
    for (row, col), value in values.items():
        if (row, col) == env.goal:
            label = "G"
        elif (row, col) == env.pit:
            label = "P"
        else:
            label = f"{value:.1f}"
        if policy and (row, col) in policy:
            label += "\n" + ARROWS[policy[(row, col)]]
        ax.text(col, row, label, ha="center", va="center")
    ax.set_title(title)
    ax.set_xticks(range(env.cols))
    ax.set_yticks(range(env.rows))


if __name__ == "__main__":
    world = Gridworld()
    initial = {state: "UP" for state in world.decision_states}

    pi_values, pi_policy, pi_history, pi_sweeps = policy_iteration(world, initial)
    vi_values, vi_policy, vi_history = value_iteration(world)

    pi_path = rollout(world, pi_policy)
    vi_path = rollout(world, vi_policy)
    print("Policy iteration: outer iterations =", len(pi_history),
          "evaluation sweeps =", pi_sweeps)
    print("Value iteration: sweeps =", len(vi_history))
    print("Start values:", round(pi_values[world.start], 4),
          round(vi_values[world.start], 4))
    print("Path lengths:", len(pi_path), len(vi_path))

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    plot_value_policy(axes[0], world, pi_values, pi_policy, "Policy iteration")
    plot_value_policy(axes[1], world, vi_values, vi_policy, "Value iteration")
    plt.tight_layout()
    plt.show()
