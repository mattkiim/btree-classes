"""Week 2 reference solution: train an agent on a multi-armed bandit."""

from random import Random

import matplotlib.pyplot as plt


class Bandit:
    """The multi-armed bandit environment built in Week 1."""

    def __init__(self, mean_rewards, reward_std=1.0, seed=None):
        self.mean_rewards = list(mean_rewards)
        self.number_of_arms = len(self.mean_rewards)
        self.reward_std = reward_std
        self.randomizer = Random(seed)

    def pull(self, arm):
        mean_reward = self.mean_rewards[arm]
        return self.randomizer.gauss(mean_reward, self.reward_std)


class BanditAgent:
    """An agent that learns sample-average rewards and explores occasionally."""

    def __init__(
        self,
        number_of_arms,
        exploration_rate=0.1,
        seed=None,
    ):
        self.counts = [0] * number_of_arms
        self.total_rewards = [0.0] * number_of_arms
        self.estimates = [0.0] * number_of_arms
        self.exploration_rate = exploration_rate
        self.randomizer = Random(seed)

    def learn(self, arm, reward):
        self.counts[arm] += 1
        self.total_rewards[arm] += reward
        self.estimates[arm] = (
            self.total_rewards[arm] / self.counts[arm]
        )

    def choose_action(self):
        # Give every arm one sample before comparing estimates.
        for arm, count in enumerate(self.counts):
            if count == 0:
                return arm

        # Explore occasionally.
        if self.randomizer.random() < self.exploration_rate:
            return self.randomizer.randrange(len(self.counts))

        # Otherwise choose an arm tied for the largest estimate.
        best_estimate = max(self.estimates)
        best_arms = [
            arm
            for arm, estimate in enumerate(self.estimates)
            if estimate == best_estimate
        ]
        if len(best_arms) == 1:
            return best_arms[0]
        return self.randomizer.choice(best_arms)


def train(bandit, agent, number_of_steps):
    """Train the agent and return actions, rewards, and estimate snapshots."""
    actions = []
    rewards = []
    estimate_history = []

    for _ in range(number_of_steps):
        arm = agent.choose_action()
        reward = bandit.pull(arm)
        agent.learn(arm, reward)

        actions.append(arm)
        rewards.append(reward)
        estimate_history.append(agent.estimates.copy())

    return actions, rewards, estimate_history


def plot_training(estimate_history, counts, hidden_means):
    """Plot estimate changes and the final number of pulls per arm."""
    colors = ["teal", "coral", "goldenrod"]
    figure, axes = plt.subplots(1, 2, figsize=(12, 4))
    steps = range(1, len(estimate_history) + 1)

    for arm, color in enumerate(colors):
        arm_estimates = [snapshot[arm] for snapshot in estimate_history]
        axes[0].plot(
            steps,
            arm_estimates,
            color=color,
            label=f"arm {arm} estimate",
        )
        axes[0].axhline(
            hidden_means[arm],
            color=color,
            linestyle="--",
            alpha=0.65,
        )

    axes[0].set_title("Estimated rewards during training")
    axes[0].set_xlabel("training step")
    axes[0].set_ylabel("estimated reward")
    axes[0].legend()

    axes[1].bar(range(len(counts)), counts, color=colors)
    axes[1].set_title("How often each arm was selected")
    axes[1].set_xlabel("arm")
    axes[1].set_ylabel("number of pulls")
    axes[1].set_xticks(range(len(counts)))

    plt.tight_layout()


if __name__ == "__main__":
    HIDDEN_MEANS = [2.0, 5.0, 3.0]

    bandit = Bandit(HIDDEN_MEANS, reward_std=1.0, seed=7)
    agent = BanditAgent(
        number_of_arms=bandit.number_of_arms,
        exploration_rate=0.1,
        seed=7,
    )

    actions, rewards, history = train(
        bandit,
        agent,
        number_of_steps=500,
    )

    print("counts:   ", agent.counts)
    print("estimates:", [round(value, 2) for value in agent.estimates])
    print("best arm: ", max(range(len(agent.estimates)), key=agent.estimates.__getitem__))
    print("total reward:", round(sum(rewards), 2))

    plot_training(history, agent.counts, HIDDEN_MEANS)
    plt.show()
