"""Week 1 reference solution: multi-armed bandit environment."""

from random import Random

import matplotlib.pyplot as plt


class Bandit:
    """A button machine that samples a reward from the chosen arm."""

    def __init__(self, mean_rewards, reward_std=1.0, seed=None):
        self.mean_rewards = list(mean_rewards)
        self.number_of_arms = len(self.mean_rewards)
        self.reward_std = reward_std
        self.randomizer = Random(seed)

    def pull(self, arm):
        mean_reward = self.mean_rewards[arm]
        reward = self.randomizer.gauss(mean_reward, self.reward_std)
        return reward


def sample_every_arm(bandit, samples_per_arm):
    """Return one list of sampled rewards for every arm."""
    all_samples = []

    for arm in range(bandit.number_of_arms):
        samples_for_this_arm = []

        for _ in range(samples_per_arm):
            reward = bandit.pull(arm)
            samples_for_this_arm.append(reward)

        all_samples.append(samples_for_this_arm)

    return all_samples


def average(numbers):
    """Return the ordinary average of a non-empty list."""
    return sum(numbers) / len(numbers)


def plot_standard_deviations():
    """Show how standard deviation changes rewards around the same mean."""
    mean_reward = 5.0
    standard_deviations = [0.5, 1.0, 2.0]
    figure, axes = plt.subplots(1, 3, figsize=(12, 3.5), sharey=True)

    for axis, standard_deviation in zip(axes, standard_deviations):
        randomizer = Random(7)
        samples = [
            randomizer.gauss(mean_reward, standard_deviation)
            for _ in range(2_000)
        ]
        axis.hist(samples, bins=35, color="teal", alpha=0.75)
        axis.axvline(mean_reward, color="black", linewidth=2)
        axis.axvline(
            mean_reward - standard_deviation,
            color="coral",
            linestyle="--",
        )
        axis.axvline(
            mean_reward + standard_deviation,
            color="coral",
            linestyle="--",
        )
        axis.set_title(f"standard deviation = {standard_deviation}")
        axis.set_xlabel("sampled reward")

    axes[0].set_ylabel("number of samples")
    plt.tight_layout()


if __name__ == "__main__":
    predictable = Bandit([2.0, 5.0, 3.0], reward_std=0.0, seed=7)
    predictable_samples = sample_every_arm(predictable, samples_per_arm=3)
    print("Predictable test:", predictable_samples)

    bandit = Bandit([2.0, 5.0, 3.0], reward_std=1.0, seed=7)
    samples = sample_every_arm(bandit, samples_per_arm=100)

    for arm, arm_samples in enumerate(samples):
        print(f"Arm {arm}")
        print("  first five:", [round(value, 2) for value in arm_samples[:5]])
        print("  average:   ", round(average(arm_samples), 2))

    plot_standard_deviations()
    plt.show()
