"""Week 2 starter project: define and inspect a deterministic Gridworld MDP."""

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
        self.rows, self.cols = rows, cols
        self.start, self.goal, self.pit = start, goal, pit
        self.walls = set(walls)
        self.step_reward = step_reward
        self.goal_reward = goal_reward
        self.pit_reward = pit_reward

        # TODO (Exercise 1): validate dimensions, locations, and no overlaps.
        # TODO (Exercise 1): create a collection of all non-wall states.
        self.states = None
        self.state = None
        self.done = False

    def _in_bounds(self, state):
        # TODO (Exercise 1): return whether (row, col) lies on the board.
        raise NotImplementedError

    def reset(self):
        # TODO (Exercise 1): restore start state, clear done, and return state.
        raise NotImplementedError

    def render(self):
        # TODO (Exercise 1): print a text map, showing A at the agent position.
        raise NotImplementedError

    def transition(self, state, action):
        """Return (next_state, reward, done) without changing self.state."""
        # TODO (Exercise 2): validate state/action and apply movement rules.
        raise NotImplementedError

    def step(self, action):
        # TODO (Exercise 2): reject post-terminal moves, apply transition,
        # update self.state/self.done, and return the transition result.
        raise NotImplementedError


def rollout(env, policy, max_steps=50):
    """Return (trajectory, terminated), safely stopping long loops."""
    # TODO (Exercise 3): reset, follow policy, and record transition tuples.
    raise NotImplementedError


def print_transition_table(env):
    # TODO (Exercise 3): print every action result from each nonterminal state.
    raise NotImplementedError


# TODO (Exercise 3): map states to actions along one safe route to the goal.
SAFE_POLICY = {}


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
