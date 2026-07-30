"""Week 1 starter project: build a bandit from buttons and reward coins."""

from random import Random


class Bandit:
    """A machine whose buttons have different collections of reward coins."""

    def __init__(self, reward_coins, seed=None):
        # TODO (Exercise 1): Store the list of coins behind each button.
        # TODO (Exercise 1): Count the arms.
        # TODO (Exercise 1): Create a Random object using seed.
        pass

    def pull(self, arm):
        # TODO (Exercise 1): Select this arm's coin list.
        # TODO (Exercise 1): Randomly choose and return one reward from it.
        raise NotImplementedError


def run_plan(bandit, planned_arms):
    """Run the planned arms in order and return the observed rewards."""
    # TODO (Exercise 2): Collect one reward for every arm in planned_arms.
    raise NotImplementedError


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
