# Week 4 — Bellman Optimality and Dynamic Programming

## Learning objectives

By the end of class, students can:

- distinguish evaluating a policy from finding an optimal policy;
- use one-step lookahead to improve a policy;
- implement and explain policy iteration and value iteration;
- compare convergence histories and visualize an optimal policy.

## Hook: can a map solve itself?

Last week we answered, “How good is this fixed policy?” Suppose the complete
Gridworld model is available and computation is cheap. Can we use it to find
the best behavior without trying routes in the live environment?

Imagine placing a number in every square. If all neighboring numbers were
already correct, how would you choose the next move? The circular problem is
that good actions depend on good values, while optimal values depend on good
actions. Dynamic programming resolves that circle through repeated updates.

## From policy value to optimal value

The **optimal state-value function** is the best value achievable by any
policy:

$$
v_*(s)=\max_\pi v_\pi(s).
$$

The optimal action-value asks what happens if we first take $a$ and then act
optimally:

$$
q_*(s,a)=\mathbb{E}[R_{t+1}+\gamma v_*(S_{t+1})\mid s,a].
$$

For our deterministic world, one-step lookahead is direct:

```python
def action_value(env, state, action, values, gamma):
    next_state, reward, done = env.transition(state, action)
    future = 0.0 if done else values[next_state]
    return reward + gamma * future
```

If `values` were optimal, choosing the action with the largest result would be
optimal too.

### Inline exercise 1

At a state where LEFT gives `-1 + 0.9(5)` and RIGHT gives
`-1 + 0.9(7)`, which is greedy? Would the choice change if RIGHT immediately
entered a terminal state and paid `+4`?

## Bellman expectation versus Bellman optimality

Last week's Bellman expectation backup averaged actions using a fixed policy:

$$
v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a).
$$

The **Bellman optimality equation** chooses the best action:

$$
v_*(s)=\max_a\sum_{s',r}p(s',r\mid s,a)
[r+\gamma v_*(s')].
$$

On this deterministic map:

```python
best_value = max(
    action_value(env, state, action, values, gamma)
    for action in ACTIONS
)
```

The difference between an average and a maximum is the key change. Expectation
asks what the current policy will do; optimality asks what the best policy
could do.

## Greedy policy improvement

Given $v_\pi$, create a new policy by choosing the action with the greatest
one-step lookahead:

$$
\pi'(s)\in\arg\max_a[r+\gamma v_\pi(s')].
$$

The **policy improvement theorem** says this greedy policy is at least as good
as the old policy. If no action changes, the policy is stable and optimal.

```python
def greedy_actions(env, state, values, gamma):
    scores = {
        action: action_value(env, state, action, values, gamma)
        for action in ACTIONS
    }
    best = max(scores.values())
    return [a for a, score in scores.items() if np.isclose(score, best)]
```

There can be several equally good actions. Code should recognize ties even if
the displayed deterministic policy selects only the first one.

### Inline exercise 2

Find a square on the map where two shortest safe routes are possible. Should
two implementations that choose different tied actions be considered wrong?

## Algorithm 1: policy iteration

**Policy iteration** alternates two phases:

1. Evaluate the current policy until its values converge.
2. Improve the policy greedily using those values.
3. Stop when improvement changes no action.

```python
def policy_iteration(env, policy, gamma=0.9, theta=1e-8):
    history = []
    while True:
        values, sweeps = policy_evaluation(env, policy, gamma, theta)
        history.append(values.copy())

        new_policy = {}
        stable = True
        for state in env.decision_states:
            new_policy[state] = greedy_actions(
                env, state, values, gamma
            )[0]
            if new_policy[state] != policy[state]:
                stable = False

        policy = new_policy
        if stable:
            return values, policy, history
```

Each outer iteration may contain many evaluation sweeps. Saying “policy
iteration took four iterations” does not mean it performed only four passes
over the states.

### Inline exercise 3

Initialize every state to choose `UP`. Predict which region of the map will
change first after one evaluate-improve cycle.

## Algorithm 2: value iteration

Do we need to finish evaluating each temporary policy? **Value iteration**
combines partial evaluation and improvement into a single optimality backup:

```python
def value_iteration(env, gamma=0.9, theta=1e-8):
    values = {state: 0.0 for state in env.states}
    history = []

    while True:
        delta = 0.0
        for state in env.decision_states:
            old = values[state]
            values[state] = max(
                action_value(env, state, action, values, gamma)
                for action in ACTIONS
            )
            delta = max(delta, abs(old - values[state]))
        history.append(values.copy())
        if delta < theta:
            break

    policy = {
        state: greedy_actions(env, state, values, gamma)[0]
        for state in env.decision_states
    }
    return values, policy, history
```

Values are updated in place here, so states later in a sweep can use new
information. A two-array version is also valid and may need a different number
of sweeps.

### Inline exercise 4

Replace `history.append(values.copy())` with `history.append(values)`. What
surprising result appears when old frames are plotted, and why?

## Watching convergence

Starting from zero, terminal rewards first affect adjacent states. Later
backups carry that information across the map. Displaying selected snapshots
makes the process visible:

```python
fig, axes = plt.subplots(1, 4, figsize=(16, 4))
indices = [0, 1, min(3, len(history) - 1), len(history) - 1]
for ax, index in zip(axes, indices):
    plot_value_policy(ax, env, history[index], title=f"Sweep {index + 1}")
plt.tight_layout()
plt.show()
```

An animation can update one image and its text labels for every history entry.
The important data structure is the history of independent snapshots; the
display format can be static frames or animation.

## Comparing the algorithms fairly

Both algorithms should converge to the same optimal values, within numerical
tolerance. Their deterministic policies can differ where actions tie.

A useful comparison records:

- number of outer policy-improvement rounds;
- number of policy-evaluation sweeps;
- number of value-iteration sweeps;
- total state backups;
- final start-state value and rollout return.

Wall-clock time on this tiny map is too noisy to be very informative. Also,
one policy-iteration outer loop is much more expensive than one value-iteration
sweep.

## What dynamic programming assumes

These methods use the environment's complete model: for every state and
action, they can query possible next states, rewards, and probabilities. They
also sweep over all states. This is feasible for our small Gridworld, but not
for a robot with a huge or unknown world.

The next methods in the course will learn values from sampled experience
instead of exhaustively consulting a known model.

## Wrap-up discussion

- What single operation changes policy evaluation into value iteration?
- Why can a greedy improvement use consequences far beyond one step?
- How can two different policies both be optimal?
- Why must histories contain copies of value tables?
- When would dynamic programming be impossible even though an MDP exists?

## Next week

Dynamic programming planned with a perfect model. Next week, Monte Carlo
methods will estimate values from complete sampled episodes in Blackjack, where
we do not enumerate and sweep through a transition model.

## Common misconceptions to watch for

- “Greedy means choose the largest immediate reward.” Greedy improvement uses
  reward plus the successor's discounted value.
- “The maximum is taken over next states.” The agent maximizes over actions;
  stochastic next states are averaged according to environment probabilities.
- “Policy iteration and value iteration must return identical arrows.” Tied
  optimal actions may produce different but equally valuable policies.
- “Fewer outer iterations means less computation.” A policy-iteration round
  can contain many full evaluation sweeps.
- “A one-step backup only plans one step ahead.” Successor values already
  summarize later consequences.
- “Dynamic programming learns by trial and error.” It plans by repeatedly
  querying a known model.
