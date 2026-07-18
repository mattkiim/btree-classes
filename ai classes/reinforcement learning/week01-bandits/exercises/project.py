"""Week 1 starter project: multi-armed bandits and epsilon-greedy learning."""

import matplotlib.pyplot as plt
import numpy as np


class Bandit:
    """A stationary Gaussian multi-armed bandit."""

    def __init__(self, means, reward_std=1.0, seed=None):
        # TODO (Exercise 1): validate and store means and reward_std.
        # TODO (Exercise 1): create self.rng with np.random.default_rng(seed).
        pass

    @property
    def n_actions(self):
        # TODO (Exercise 1): return the number of arms.
        raise NotImplementedError

    def step(self, action):
        # TODO (Exercise 1): validate action, then sample its noisy reward.
        raise NotImplementedError


class EpsilonGreedyAgent:
    def __init__(self, n_actions, epsilon=0.1, seed=None):
        if n_actions <= 0:
            raise ValueError("n_actions must be positive")
        if not 0.0 <= epsilon <= 1.0:
            raise ValueError("epsilon must be between 0 and 1")
        self.epsilon = epsilon
        self.estimates = np.zeros(n_actions, dtype=float)
        self.counts = np.zeros(n_actions, dtype=int)
        self.rng = np.random.default_rng(seed)

    def choose_action(self):
        # TODO (Exercise 2): explore or randomly break a tie among best estimates.
        raise NotImplementedError

    def update(self, action, reward):
        # TODO (Exercise 2): update count and incremental sample average.
        raise NotImplementedError


def run_bandit(means, epsilon, steps, reward_std=1.0, seed=0):
    """Return arrays of rewards and actions from one independent run."""
    # TODO (Exercise 2): create environment and agent and run their loop.
    raise NotImplementedError


def compare_strategies(means, epsilons, steps=500, runs=100, reward_std=1.0):
    """Return {epsilon: mean cumulative-reward curve}."""
    # TODO (Exercise 3): repeat runs and average cumulative reward by step.
    raise NotImplementedError


def plot_comparison(means, curves, steps):
    # TODO (Exercise 3): plot every curve and the oracle benchmark.
    # Include a title, axis labels, legend, and tight_layout().
    raise NotImplementedError


if __name__ == "__main__":
    ARM_MEANS = np.array([-0.2, 0.0, 0.5, 1.0, 0.7])
    EPSILONS = [0.0, 0.1, 0.3]
    STEPS = 500
    RUNS = 100

    curves = compare_strategies(ARM_MEANS, EPSILONS, STEPS, RUNS)
    plot_comparison(ARM_MEANS, curves, STEPS)
    plt.show()
