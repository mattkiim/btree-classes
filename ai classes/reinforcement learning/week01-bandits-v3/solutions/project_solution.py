"""Week 1 reference solution: build a bandit from buttons and reward coins."""

from random import Random


class Bandit:
    """A machine whose buttons have different collections of reward coins."""

    def __init__(self, reward_coins, seed=None):
        if not reward_coins:
            raise ValueError("A bandit needs at least one arm.")
        if any(not coins for coins in reward_coins):
            raise ValueError("Every arm needs at least one reward coin.")

        self.reward_coins = reward_coins
        self.number_of_arms = len(reward_coins)
        self.randomizer = Random(seed)

    def pull(self, arm):
        if not isinstance(arm, int):
            raise TypeError("The arm must be an integer.")
        if arm < 0 or arm >= self.number_of_arms:
            raise ValueError(
                f"Choose an arm from 0 through {self.number_of_arms - 1}."
            )

        coins_for_this_arm = self.reward_coins[arm]
        reward = self.randomizer.choice(coins_for_this_arm)
        return reward


def run_plan(bandit, planned_arms):
    """Run the planned arms in order and return the observed rewards."""
    rewards = []

    for arm in planned_arms:
        reward = bandit.pull(arm)
        rewards.append(reward)

    return rewards


def show_report(name, planned_arms, rewards):
    """Print one completed plan in button-machine language."""
    print(name)
    print("  buttons chosen:", planned_arms)
    print("  points returned:", rewards)
    print("  total points:   ", sum(rewards))


if __name__ == "__main__":
    REWARD_COINS = [
        [1, 1, 1, 7],  # Arm 0: usually 1, sometimes 7
        [3, 3, 3, 3],  # Arm 1: always 3
        [0, 2, 4, 6],  # Arm 2: several possible rewards
    ]

    plans = {
        "Try each arm": [0, 1, 2, 0, 1, 2],
        "Repeat arm 1": [1, 1, 1, 1, 1, 1],
    }

    for name, planned_arms in plans.items():
        # A fresh bandit makes each plan start from the same random sequence.
        bandit = Bandit(REWARD_COINS, seed=7)
        rewards = run_plan(bandit, planned_arms)
        show_report(name, planned_arms, rewards)
        print()
