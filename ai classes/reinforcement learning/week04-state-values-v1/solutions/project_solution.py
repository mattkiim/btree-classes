"""Week 4 reference solution: evaluate a fixed Gridworld policy."""


class Gridworld:
    """The deterministic three-by-three environment from Week 3."""

    def __init__(self):
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
        self.terminal_rewards = {
            (0, 2): 10,
            (2, 2): -10,
        }
        self.step_reward = -1
        self.state = self.start_state
        self.done = False

    def reset(self, start_state=None):
        if start_state is None:
            start_state = self.start_state

        self.state = start_state
        self.done = start_state in self.terminal_rewards
        return self.state

    def is_inside(self, state):
        row, column = state
        return 0 <= row < self.rows and 0 <= column < self.columns

    def move(self, action):
        if action not in self.action_changes:
            raise ValueError(f"Unknown action: {action}")

        row_change, column_change = self.action_changes[action]
        row, column = self.state
        candidate_state = (row + row_change, column + column_change)

        if (
            self.is_inside(candidate_state)
            and candidate_state not in self.wall_states
        ):
            self.state = candidate_state

        return self.state

    def step(self, action):
        if self.done:
            raise RuntimeError("Episode is finished. Call reset().")

        next_state = self.move(action)
        reward = self.terminal_rewards.get(next_state, self.step_reward)
        self.done = next_state in self.terminal_rewards
        return next_state, reward, self.done


FIXED_POLICY = {
    (0, 0): "right",
    (0, 1): "right",
    (1, 0): "up",
    (1, 2): "up",
    (2, 0): "up",
    (2, 1): "left",
}


def choose_action(policy, state):
    """Return the action assigned to a state."""
    return policy[state]


def follow_policy(world, policy, start_state):
    """Follow a policy from one state and return its episode history."""
    state = world.reset(start_state)
    history = []

    while not world.done:
        action = choose_action(policy, state)
        next_state, reward, done = world.step(action)
        history.append((state, action, next_state, reward))
        state = next_state

    return history


def calculate_returns(history):
    """Match each visited state to its future reward total."""
    future_total = 0
    returns_by_state = {}

    for state, action, next_state, reward in reversed(history):
        future_total = reward + future_total
        returns_by_state[state] = future_total

    return returns_by_state


def evaluate_policy(world, policy):
    """Calculate the exact value of every open state under a policy."""
    values = {}

    for row in range(world.rows):
        for column in range(world.columns):
            state = (row, column)

            if state in world.wall_states:
                continue

            if state in world.terminal_rewards:
                values[state] = 0
                continue

            history = follow_policy(world, policy, state)
            returns = calculate_returns(history)
            values[state] = returns[state]

    return values


def print_value_map(world, values):
    """Print values in the same arrangement as the Gridworld."""
    for row in range(world.rows):
        cells = []

        for column in range(world.columns):
            state = (row, column)

            if state in world.wall_states:
                cells.append("  #")
            else:
                cells.append(f"{values[state]:3}")

        print(" ".join(cells))


if __name__ == "__main__":
    gridworld = Gridworld()
    values = evaluate_policy(gridworld, FIXED_POLICY)
    print_value_map(gridworld, values)
