"""Week 4 starter project: solve Gridworld with dynamic programming."""

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
        return [s for s in self.states if s not in self.terminal_states]

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
    # TODO (Exercise 1): return the one-step Bellman target for this action.
    raise NotImplementedError


def greedy_actions(env, state, values, gamma, atol=1e-10):
    """Return a list containing every action tied for the maximum."""
    # TODO (Exercise 1): calculate all action-values and preserve ties.
    raise NotImplementedError


def policy_evaluation(env, policy, gamma=0.9, theta=1e-8):
    """Evaluate a deterministic {state: action} policy."""
    # TODO (Exercise 1): perform Bellman expectation sweeps to convergence.
    raise NotImplementedError


def improve_policy(env, policy, values, gamma=0.9):
    """Return (greedy_policy, stable), breaking ties by ACTIONS order."""
    # TODO (Exercise 1): greedily improve every decision state and determine
    # whether the supplied policy was already stable.
    raise NotImplementedError


def policy_iteration(env, initial_policy, gamma=0.9, theta=1e-8,
                     max_iterations=100):
    """Return (values, policy, history, evaluation_sweeps)."""
    # TODO (Exercise 2): alternate evaluation and improvement. Store copied
    # value dictionaries in history and count all evaluation sweeps.
    raise NotImplementedError


def value_iteration(env, gamma=0.9, theta=1e-8, max_sweeps=10_000):
    """Return (values, greedy_policy, history)."""
    # TODO (Exercise 3): apply optimality sweeps, save copied snapshots, stop
    # at theta, and extract one greedy action per state.
    raise NotImplementedError


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
    # TODO (Exercise 3): draw a heatmap with numeric values, wall markers,
    # terminal labels, and optional action arrows.
    raise NotImplementedError


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
