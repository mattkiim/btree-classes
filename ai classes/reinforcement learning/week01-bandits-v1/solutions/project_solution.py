"""Week 1 reference solution: multi-armed bandits and epsilon-greedy learning."""

import matplotlib.pyplot as plt
import numpy as np


class Bandit:
    """A stationary Gaussian multi-armed bandit."""

    def __init__(self, means, reward_std=1.0, seed=None):
        self.means = np.asarray(means, dtype=float)
        if self.means.ndim != 1 or self.means.size == 0:
            raise ValueError("means must be a non-empty one-dimensional sequence")
        if reward_std <= 0:
            raise ValueError("reward_std must be positive")
        self.reward_std = float(reward_std)
        self.rng = np.random.default_rng(seed)

    @property
    def n_actions(self):
        return len(self.means)

    def step(self, action):
        if not isinstance(action, (int, np.integer)) or not 0 <= action < self.n_actions:
            raise ValueError("action must be a valid arm index")
        return float(self.rng.normal(self.means[action], self.reward_std))


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
        if self.rng.random() < self.epsilon:
            return int(self.rng.integers(len(self.estimates)))
        best_actions = np.flatnonzero(self.estimates == self.estimates.max())
        return int(self.rng.choice(best_actions))

    def update(self, action, reward):
        self.counts[action] += 1
        step_size = 1.0 / self.counts[action]
        self.estimates[action] += step_size * (reward - self.estimates[action])


def run_bandit(means, epsilon, steps, reward_std=1.0, seed=0):
    """Return arrays of rewards and actions from one independent run."""
    env = Bandit(means, reward_std, seed)
    agent = EpsilonGreedyAgent(env.n_actions, epsilon, seed + 1)
    rewards = np.empty(steps)
    actions = np.empty(steps, dtype=int)
    for step in range(steps):
        action = agent.choose_action()
        reward = env.step(action)
        agent.update(action, reward)
        actions[step], rewards[step] = action, reward
    return rewards, actions


def compare_strategies(means, epsilons, steps=500, runs=100, reward_std=1.0):
    """Return {epsilon: mean cumulative-reward curve}."""
    curves = {}
    for epsilon in epsilons:
        cumulative_rewards = []
        for run in range(runs):
            rewards, _ = run_bandit(
                means, epsilon, steps, reward_std, seed=10_000 * run
            )
            cumulative_rewards.append(np.cumsum(rewards))
        curves[epsilon] = np.mean(cumulative_rewards, axis=0)
    return curves


def plot_comparison(means, curves, steps):
    for epsilon, curve in curves.items():
        plt.plot(curve, label=f"epsilon={epsilon}")
    plt.plot(
        np.arange(1, steps + 1) * np.max(means),
        linestyle="--",
        label="oracle",
    )
    plt.title("Greedy and epsilon-greedy bandit strategies")
    plt.xlabel("Step")
    plt.ylabel("Mean cumulative reward")
    plt.legend()
    plt.tight_layout()


if __name__ == "__main__":
    ARM_MEANS = np.array([-0.2, 0.0, 0.5, 1.0, 0.7])
    EPSILONS = [0.0, 0.1, 0.3]
    STEPS = 500
    RUNS = 100

    curves = compare_strategies(ARM_MEANS, EPSILONS, STEPS, RUNS)
    plot_comparison(ARM_MEANS, curves, STEPS)
    plt.show()
