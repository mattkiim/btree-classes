"""Week 1 starter project: build and investigate a mystery-button machine."""

from random import Random


class Bandit:
    """A machine with several arms (buttons) that return rewards (points)."""

    def __init__(self, typical_rewards, reward_spread=1.0, seed=None):
        # TODO (Exercise 1): Make a list of the typical rewards and store it.
        # TODO (Exercise 1): Count the arms and store the count.
        pass

        # This setup is provided. Exercise 2 will use both values.
        self.reward_spread = reward_spread
        self.randomizer = Random(seed)

    def pull(self, arm):
        # TODO (Exercise 1): Look up this arm's typical reward.
        #
        # For Exercise 1, return that value directly.
        # TODO (Exercise 2): Replace the predictable result with a reward from
        # self.randomizer.gauss(typical_reward, self.reward_spread).
        raise NotImplementedError


def try_every_arm(bandit, pulls_per_arm):
    """Return one list of observed rewards for each arm."""
    # TODO (Exercise 2): Build a list of lists by trying each arm several times.
    raise NotImplementedError


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
