"""Week 2 reference solution: define and inspect a deterministic Gridworld."""

ACTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}


class Gridworld:
    def __init__(
        self,
        rows=5,
        cols=5,
        start=(0, 0),
        goal=(4, 4),
        pit=(4, 3),
        walls=((0, 3), (1, 1), (1, 3), (2, 1), (3, 2), (3, 3)),
        step_reward=-1,
        goal_reward=10,
        pit_reward=-10,
    ):
        if rows <= 0 or cols <= 0:
            raise ValueError("rows and cols must be positive")
        self.rows, self.cols = rows, cols
        self.start, self.goal, self.pit = start, goal, pit
        self.walls = set(walls)
        self.step_reward = step_reward
        self.goal_reward = goal_reward
        self.pit_reward = pit_reward

        locations = [start, goal, pit, *self.walls]
        if any(not self._in_bounds(location) for location in locations):
            raise ValueError("all locations must be in bounds")
        if len({start, goal, pit}) != 3:
            raise ValueError("start, goal, and pit must be distinct")
        if {start, goal, pit} & self.walls:
            raise ValueError("walls cannot overlap start, goal, or pit")

        self.states = {
            (row, col)
            for row in range(rows)
            for col in range(cols)
            if (row, col) not in self.walls
        }
        self.state = None
        self.done = False

    def _in_bounds(self, state):
        return 0 <= state[0] < self.rows and 0 <= state[1] < self.cols

    def reset(self):
        self.state = self.start
        self.done = False
        return self.state

    def render(self):
        for row in range(self.rows):
            symbols = []
            for col in range(self.cols):
                location = (row, col)
                if location == self.state:
                    symbol = "A"
                elif location == self.start:
                    symbol = "S"
                elif location == self.goal:
                    symbol = "G"
                elif location == self.pit:
                    symbol = "P"
                elif location in self.walls:
                    symbol = "#"
                else:
                    symbol = "."
                symbols.append(symbol)
            print(" ".join(symbols))

    def transition(self, state, action):
        """Return (next_state, reward, done) without changing self.state."""
        if state not in self.states or state in (self.goal, self.pit):
            raise ValueError("state must be a nonterminal Gridworld state")
        if action not in ACTIONS:
            raise ValueError(f"unknown action: {action}")
        dr, dc = ACTIONS[action]
        candidate = (state[0] + dr, state[1] + dc)
        if not self._in_bounds(candidate) or candidate in self.walls:
            candidate = state
        reward = (
            self.goal_reward if candidate == self.goal
            else self.pit_reward if candidate == self.pit
            else self.step_reward
        )
        return candidate, reward, candidate in (self.goal, self.pit)

    def step(self, action):
        if self.state is None:
            raise RuntimeError("call reset before step")
        if self.done:
            raise RuntimeError("episode is over; call reset")
        self.state, reward, self.done = self.transition(self.state, action)
        return self.state, reward, self.done


def rollout(env, policy, max_steps=50):
    """Return (trajectory, terminated), safely stopping long loops."""
    state = env.reset()
    trajectory = []
    for _ in range(max_steps):
        if state not in policy:
            raise KeyError(f"policy has no action for state {state}")
        action = policy[state]
        next_state, reward, done = env.step(action)
        trajectory.append((state, action, reward, next_state))
        state = next_state
        if done:
            return trajectory, True
    return trajectory, False


def print_transition_table(env):
    for state in sorted(env.states):
        if state in (env.goal, env.pit):
            continue
        outcomes = {action: env.transition(state, action) for action in ACTIONS}
        print(state, outcomes)


SAFE_POLICY = {
    (0, 0): "RIGHT", (0, 1): "RIGHT", (0, 2): "DOWN",
    (1, 2): "DOWN", (2, 2): "RIGHT", (2, 3): "RIGHT",
    (2, 4): "DOWN", (3, 4): "DOWN",
}


if __name__ == "__main__":
    world = Gridworld()
    world.reset()
    world.render()

    trajectory, terminated = rollout(world, SAFE_POLICY)
    print("\nSafe-policy trajectory:")
    for transition_record in trajectory:
        print(transition_record)
    print("terminated:", terminated)
    print("total reward:", sum(item[2] for item in trajectory))

    print("\nTransition table:")
    print_transition_table(world)
