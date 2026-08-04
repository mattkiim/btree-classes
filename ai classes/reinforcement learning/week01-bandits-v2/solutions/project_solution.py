"""Week 1 reference solution: build and investigate a mystery-button machine."""

from random import Random


class Bandit:
    """A machine with several arms (buttons) that return rewards (points)."""

    def __init__(self, typical_rewards, reward_spread=1.0, seed=None):
        self.typical_rewards = list(typical_rewards)
        self.number_of_arms = len(self.typical_rewards)

        # if self.number_of_arms == 0:
        #     raise ValueError("A bandit needs at least one arm.")
        # if reward_spread < 0:
        #     raise ValueError("reward_spread cannot be negative.")

        self.reward_spread = reward_spread
        self.randomizer = Random(seed)

    def pull(self, arm):
        # if not isinstance(arm, int):
        #     raise TypeError("The arm must be an integer.")
        # if arm < 0 or arm >= self.number_of_arms:
        #     raise ValueError(
        #         f"Choose an arm from 0 through {self.number_of_arms - 1}."
        #     )

        typical_reward = self.typical_rewards[arm]
        reward = self.randomizer.gauss(typical_reward, self.reward_spread)
        return reward


def try_every_arm(bandit, pulls_per_arm):
    """Return one list of observed rewards for each arm."""
    # if not isinstance(pulls_per_arm, int) or pulls_per_arm <= 0:
    #     raise ValueError("pulls_per_arm must be a positive integer.")

    all_rewards = []

    for arm in range(bandit.number_of_arms):
        rewards_for_this_arm = []

        for _ in range(pulls_per_arm):
            reward = bandit.pull(arm)
            rewards_for_this_arm.append(reward)

        all_rewards.append(rewards_for_this_arm)

    return all_rewards


def average(numbers):
    """Return the ordinary arithmetic average of a non-empty list."""
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    # These values describe the environment. A future learning agent would not
    # be allowed to read them directly.
    TYPICAL_REWARDS = [2.0, 5.0, 3.0]

    bandit = Bandit(
        typical_rewards=TYPICAL_REWARDS,
        reward_spread=1.0,
        seed=7,
    )

    print("Number of arms:", bandit.number_of_arms)
    print("First pull of arm 1:", round(bandit.pull(1), 2))
    print("Second pull of arm 1:", round(bandit.pull(1), 2))

    print("\nTrying every arm five times:")
    results = try_every_arm(bandit, pulls_per_arm=5)

    for arm, rewards in enumerate(results):
        rounded_rewards = [round(reward, 2) for reward in rewards]
        print(f"Arm {arm}")
        print("  observed rewards:", rounded_rewards)
        print("  average reward:  ", round(average(rewards), 2))
