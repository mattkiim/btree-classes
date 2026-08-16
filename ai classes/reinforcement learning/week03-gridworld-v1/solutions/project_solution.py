"""Week 3 reference solution: build a small Gridworld environment."""


class Gridworld:
    """A deterministic three-by-three movement environment."""

    def __init__(self):
        # Store the board shape, barriers, and action meanings.
        self.rows = 3
        self.columns = 3
        self.start_state = (0, 0)
        self.wall_states = {(1, 1)}
        self.action_changes = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

        # Store rewards for ending states and ordinary movement.
        self.terminal_rewards = {
            (0, 2): 10,
            (2, 2): -10,
        }
        self.step_reward = -1

        # Start the first episode.
        self.state = self.start_state
        self.done = False

    def reset(self):
        """Start a new episode and return its first state."""
        self.state = self.start_state
        self.done = False
        return self.state

    def is_inside(self, state):
        """Return whether a state is inside the board."""
        row, column = state
        return (
            0 <= row < self.rows
            and 0 <= column < self.columns
        )

    def move(self, action):
        """Apply boundaries and walls, then return the resulting state."""
        if action not in self.action_changes:
            raise ValueError(f"Unknown action: {action}")

        row_change, column_change = self.action_changes[action]
        row, column = self.state
        candidate_state = (
            row + row_change,
            column + column_change,
        )

        if (
            self.is_inside(candidate_state)
            and candidate_state not in self.wall_states
        ):
            self.state = candidate_state

        return self.state

    def step(self, action):
        """Apply one action and return state, reward, and episode status."""
        if self.done:
            raise RuntimeError("Episode is finished. Call reset().")

        next_state = self.move(action)
        reward = self.terminal_rewards.get(
            next_state,
            self.step_reward,
        )
        self.done = next_state in self.terminal_rewards
        return next_state, reward, self.done


def run_episode(world, actions):
    """Run a fixed action list and return its transitions and reward."""
    state = world.reset()
    history = []
    total_reward = 0

    for action in actions:
        next_state, reward, done = world.step(action)
        history.append((state, action, next_state, reward))
        total_reward += reward
        state = next_state

        if done:
            break

    return history, total_reward


if __name__ == "__main__":
    gridworld = Gridworld()
    planned_actions = ["right", "down", "right", "left"]

    episode_history, episode_reward = run_episode(
        gridworld,
        planned_actions,
    )

    for transition in episode_history:
        print(transition)

    print("total reward:", episode_reward)
    print("episode done:", gridworld.done)
