# Week 1 — What Is Reinforcement Learning?

## Learning objectives

By the end of class, students can:

- identify an agent, actions, and rewards in a problem;
- explain exploration and exploitation in their own words;
- implement a multi-armed bandit and an epsilon-greedy agent;
- use repeated trials and plots to compare policies fairly.

## Hook: which button would you press?

Imagine three unlabeled buttons. Every press awards a random number of points,
and you get 100 presses. How would you decide which button to use?

Discuss: Is it ever sensible to press a button that currently looks worse? What
information would you record? What does “best” mean when rewards are random?

## The reinforcement-learning loop

Reinforcement learning (RL) studies how an **agent** learns through interaction.
At each step, the agent observes a situation, chooses an **action**, and receives
a numerical **reward** from the **environment**. The agent's rule for choosing
actions is its **policy**.

In a bandit there is only one situation, so we omit state:

1. Agent selects an arm (action).
2. Environment samples its reward.
3. Agent updates what it believes about that arm.
4. Repeat.

The unknown mean reward of arm $a$ is $q_*(a)$. The agent estimates it with
$Q(a)$. After choosing an arm $N(a)$ times, its sample-average estimate is

$$
Q(a)=\frac{\text{sum of observed rewards from }a}{N(a)}.
$$

An equivalent one-step update is

$$
Q(a) \leftarrow Q(a) + \frac{1}{N(a)}(R-Q(a)).
$$

The difference $R-Q(a)$ is a prediction error: positive means the reward was
better than expected.

### Inline exercise

Suppose an arm's estimate is 4 after two pulls and its next reward is 7. Compute
the new estimate before running any code.

## Live coding: the environment

```python
import numpy as np

class Bandit:
    def __init__(self, means, reward_std=1.0, seed=None):
        self.means = np.asarray(means, dtype=float)
        self.reward_std = reward_std
        self.rng = np.random.default_rng(seed)

    @property
    def n_actions(self):
        return len(self.means)

    def step(self, action):
        if not 0 <= action < self.n_actions:
            raise ValueError("invalid action")
        return self.rng.normal(self.means[action], self.reward_std)

bandit = Bandit([0.0, 0.4, 1.0], seed=7)
print([round(bandit.step(2), 2) for _ in range(5)])
```

The best arm does not win every pull. RL must learn from noisy evidence.

### Inline exercise

Change `reward_std` to `0.1`, then `3.0`. Predict which setting makes learning
harder, and explain why.

## Exploration versus exploitation

A greedy policy always chooses the largest current estimate. It **exploits**
what it knows, but an unlucky early sample can trap it. An epsilon-greedy policy
usually exploits and sometimes **explores**:

- with probability $\epsilon$, choose a random action;
- otherwise, choose an action with the largest estimate.

When estimates tie, choose randomly among the tied actions. Always choosing the
first maximum creates a hidden preference for arm 0.

```python
class EpsilonGreedyAgent:
    def __init__(self, n_actions, epsilon=0.1, seed=None):
        self.epsilon = epsilon
        self.q = np.zeros(n_actions)
        self.counts = np.zeros(n_actions, dtype=int)
        self.rng = np.random.default_rng(seed)

    def choose_action(self):
        if self.rng.random() < self.epsilon:
            return int(self.rng.integers(len(self.q)))
        best = np.flatnonzero(self.q == self.q.max())
        return int(self.rng.choice(best))

    def update(self, action, reward):
        self.counts[action] += 1
        self.q[action] += (reward - self.q[action]) / self.counts[action]
```

### Inline exercise

Run with `epsilon=0`, `0.1`, and `1`. Describe the policy represented by each
extreme before looking at its reward.

## A single experiment

```python
def run_episode(means, epsilon, steps=500, seed=0):
    env = Bandit(means, seed=seed)
    agent = EpsilonGreedyAgent(len(means), epsilon, seed=seed + 1)
    rewards = []
    for _ in range(steps):
        action = agent.choose_action()
        reward = env.step(action)
        agent.update(action, reward)
        rewards.append(reward)
    return np.asarray(rewards), agent

rewards, agent = run_episode([0.0, 0.4, 1.0], 0.1)
print("estimates:", np.round(agent.q, 2))
print("counts:", agent.counts)
print("total reward:", round(rewards.sum(), 1))
```

One run can be lucky. A fair comparison uses the same bandit settings, many
independent seeds, and an average across runs.

## Comparing strategies

```python
import matplotlib.pyplot as plt

means = [-0.2, 0.0, 0.5, 1.0, 0.7]
for epsilon in [0.0, 0.1, 0.3]:
    curves = []
    for run in range(100):
        rewards, _ = run_episode(means, epsilon, steps=500, seed=run * 10)
        curves.append(np.cumsum(rewards))
    plt.plot(np.mean(curves, axis=0), label=f"epsilon={epsilon}")

plt.xlabel("Step")
plt.ylabel("Mean cumulative reward")
plt.legend()
plt.tight_layout()
plt.show()
```

The oracle benchmark always chooses the true best arm. It is not a learnable
policy—the agent is not told the means—but it shows what perfect knowledge could
earn. **Regret** is the reward lost compared with that benchmark.

### Inline exercise

Try 20 arms or only 20 steps. Does the best epsilon change? State a hypothesis
before running the experiment.

## Wrap-up discussion

- Why can greedy beat epsilon-greedy briefly but lose over a longer horizon?
- Why does cumulative reward keep rising even for a poor policy?
- What must stay fixed for a fair comparison?
- Where do you see this explore/exploit tension outside games?

## Next week

Bandits have actions and rewards but no changing state. Next week, the agent
moves through a Gridworld. Actions change the state, and future consequences
become part of a formal Markov Decision Process.

## Common misconceptions to watch for

- “The best arm always gives the largest reward.” It only has the largest mean.
- “Exploration is wasted.” It buys information that can improve later choices.
- “Epsilon is the fraction of actions that are wrong.” Random exploration can
  still select the best arm.
- “A higher curve from one seed proves an algorithm is better.” Compare many
  runs and report variability.
- “The oracle is a greedy learner.” The oracle knows hidden means; a greedy
  learner uses uncertain estimates.
