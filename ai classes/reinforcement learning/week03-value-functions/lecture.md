# Week 3 — Value Functions and Bellman Equations

## Learning objectives

By the end of class, students can:

- distinguish immediate reward, return, state-value, and action-value;
- explain how the discount factor changes the importance of future rewards;
- apply the Bellman expectation equation to a fixed policy;
- compute and visualize a policy's values on the Week 2 Gridworld.

## Hook: which square would you rather stand on?

Look at the Gridworld without moving an agent. Is a square beside the goal
automatically good? What if the policy usually steps toward the pit? Is the
start square worth one number, or does its quality depend on how the agent will
behave afterward?

Reward describes one transition. Today we want a prediction of the whole
future under a particular policy.

## From rewards to returns

Suppose an episode produces rewards $R_1,R_2,R_3,\ldots$. Its **return** from
time $t$ is the discounted total

$$
G_t=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots,
$$

where the **discount factor** $0\leq\gamma\leq1$ controls how strongly later
rewards count. With $\gamma=0$, only the next reward matters. Values near one
make long-term consequences important.

For rewards `[-1, -1, 10]` and $\gamma=0.9$,

$$
G_0=-1+0.9(-1)+0.9^2(10)=6.2.
$$

Discounting can represent impatience or uncertainty about a distant future. It
also helps continuing problems have finite values. In our terminating world,
it lets us tune short-term versus long-term planning.

### Inline exercise 1

Compute the same return with $\gamma=0$, $0.5$, and $1$. Which choice most
strongly prefers eventually reaching the goal?

## A policy can be stochastic

Last week a policy mapped each state to one action. More generally,
$\pi(a\mid s)$ is the probability of taking action $a$ in state $s$. A random
policy gives each of our four actions probability $0.25$.

```python
def random_policy(env):
    probability = 1.0 / len(ACTIONS)
    return {
        state: {action: probability for action in ACTIONS}
        for state in env.states
        if state not in env.terminal_states
    }
```

The policy is not part of the Gridworld. We can evaluate several policies on
one unchanged environment.

## State-value and action-value

The **state-value function** of a policy is its expected return starting in a
state and then following that policy:

$$
v_\pi(s)=\mathbb{E}_\pi[G_t\mid S_t=s].
$$

The **action-value function** fixes the first action, then follows the policy:

$$
q_\pi(s,a)=\mathbb{E}_\pi[G_t\mid S_t=s,A_t=a].
$$

“Expected” matters. A random policy can produce different trips from the same
square, but its value averages over those possibilities. A value is always
relative to a policy: changing behavior can change a state's value without
changing the map.

We define terminal-state values as zero because the reward for entering a
terminal state was already received on the transition.

### Inline exercise 2

Can $q_\pi(s,\text{RIGHT})$ be high while $v_\pi(s)$ is low? Describe a policy
that makes this happen.

## First estimate: sample complete episodes

We can estimate a value by taking many rollouts and averaging their returns.

```python
def sample_return(env, policy, start, gamma=0.9, max_steps=200, seed=None):
    rng = np.random.default_rng(seed)
    state = start
    total = 0.0
    discount = 1.0

    for _ in range(max_steps):
        choices = list(policy[state])
        probabilities = [policy[state][a] for a in choices]
        action = rng.choice(choices, p=probabilities)
        state, reward, done = env.transition(state, action)
        total += discount * reward
        discount *= gamma
        if done:
            break
    return total
```

This method requires no equation solving, but a few samples can be misleading.
The result also depends on the safety cutoff if the policy can wander for a
long time.

### Inline exercise 3

Estimate the start value with 10, 100, and 10,000 rollouts. How does the
estimate's stability change?

## The one-step recursive idea

Return has a useful recursive form:

$$
G_t=R_{t+1}+\gamma G_{t+1}.
$$

So a state's value equals its expected next reward plus the discounted value
of where it lands. This is the **Bellman expectation equation**:

$$
v_\pi(s)=\sum_a\pi(a\mid s)\sum_{s',r}
p(s',r\mid s,a)[r+\gamma v_\pi(s')].
$$

Our Gridworld is deterministic, so each state-action pair has just one next
state and reward. The inner sum becomes one model lookup:

```python
def q_from_v(env, state, action, values, gamma):
    next_state, reward, done = env.transition(state, action)
    future = 0.0 if done else values[next_state]
    return reward + gamma * future

def bellman_backup(env, policy, state, values, gamma):
    return sum(
        probability * q_from_v(env, state, action, values, gamma)
        for action, probability in policy[state].items()
    )
```

A **backup** updates a prediction using successor predictions. This is not yet
learning from experience: it uses the complete transition model we built.

## Live coding: iterative policy evaluation

The equation refers to values we do not know. Start every value at zero, apply
the equation repeatedly, and watch information spread backward from the
terminal rewards.

```python
def evaluate_policy(env, policy, gamma=0.9, theta=1e-8):
    values = {state: 0.0 for state in env.states}
    deltas = []

    while True:
        delta = 0.0
        for state in env.states:
            if state in env.terminal_states:
                continue
            old = values[state]
            values[state] = bellman_backup(
                env, policy, state, values, gamma
            )
            delta = max(delta, abs(old - values[state]))
        deltas.append(delta)
        if delta < theta:
            return values, deltas
```

The threshold $\theta$ is a tolerance, not a target value. When the largest
change is tiny, another sweep would barely alter any state.

### Inline exercise 4

Print the start value after every sweep. Why does it not jump immediately to
its final value?

## Visualizing the value landscape

```python
def value_array(env, values):
    grid = np.full((env.rows, env.cols), np.nan)
    for state, value in values.items():
        grid[state] = value
    return grid

grid = value_array(world, values)
plt.imshow(grid, cmap="coolwarm")
plt.colorbar(label="State value")
for (row, col), value in values.items():
    plt.text(col, row, f"{value:.1f}", ha="center", va="center")
plt.title("Value of the random policy")
plt.show()
```

A heatmap is a prediction map, not a reward map. Ordinary squares can have
very different values even though their immediate movement cost is the same.

## Hand-checking one state

Take the square immediately above the goal, `(3, 4)`. List the result of all
four actions, look up each successor's current value, and average the four
one-step targets. This manual backup should equal the code's next update for a
random policy.

Checking one carefully chosen state is often better debugging than staring at
an entire heatmap.

## Wrap-up discussion

- Why is value attached to both a state and a policy?
- What information does $q_\pi(s,a)$ contain that $v_\pi(s)$ averages away?
- Why is the terminal state's value zero even though reaching the goal pays 10?
- How do sampling and Bellman evaluation answer the same question differently?
- What does a negative value mean in a world with a positive goal?

## Next week

Today the policy was fixed. Next week, we will replace its average over actions
with a maximum, use values to improve behavior, and compare value iteration
with policy iteration.

## Common misconceptions to watch for

- “Value and reward are synonyms.” Reward is immediate; value predicts a
  discounted sequence of rewards.
- “A state has one true value.” Its value depends on the policy and gamma.
- “Discounting means later rewards disappear.” They count less when
  $\gamma<1$; they do not vanish after one step.
- “Terminal value should be 10.” The transition into the goal pays 10; adding a
  terminal value of 10 would count it again.
- “Bellman iteration simulates episodes.” It queries the model for every action
  and performs backups; no trajectory is sampled.
- “One sweep must be exact.” Each sweep propagates information farther through
  the state graph.
