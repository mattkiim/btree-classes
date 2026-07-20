"""Week 3 starter project: evaluate a fixed policy on Gridworld."""

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
        # TODO (Exercise 1): validate inputs and apply the Week 2 movement,
        # collision, reward, and terminal rules.
        raise NotImplementedError


def random_policy(env):
    """Return {state: {action: probability}} for nonterminal states."""
    # TODO (Exercise 1): assign equal probability to every action.
    raise NotImplementedError


def sample_action(action_probabilities, rng):
    # TODO (Exercise 1): sample one action using the supplied probabilities.
    raise NotImplementedError


def sample_return(env, policy, start_state, gamma=0.9, max_steps=200, seed=None):
    """Sample one discounted return following policy from start_state."""
    # TODO (Exercise 1): generate a rollout and accumulate discounted rewards.
    raise NotImplementedError


def q_from_v(env, state, action, values, gamma):
    """Compute q_pi(s, a) from a current state-value table."""
    # TODO (Exercise 2): use one model transition and bootstrap if nonterminal.
    raise NotImplementedError


def evaluate_policy(env, policy, gamma=0.9, theta=1e-8, max_sweeps=10_000):
    """Return (values, deltas) from iterative Bellman expectation updates."""
    # TODO (Exercise 2): initialize values, perform in-place sweeps, record the
    # largest change each sweep, and stop when it is below theta.
    raise NotImplementedError


def plot_values(env, values, title="Value of the random policy"):
    # TODO (Exercise 2): create and annotate a heatmap; display walls clearly.
    raise NotImplementedError


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
