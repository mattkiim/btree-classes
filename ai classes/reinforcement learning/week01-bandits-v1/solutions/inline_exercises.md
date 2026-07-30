# Week 1 Inline Exercise Solutions

## Exercise 1 — Incremental estimate

The next count is 3, so

$$
Q \leftarrow 4+\frac{1}{3}(7-4)=5.
$$

This is also the average of three rewards: the first two had a total of 8, and
the new reward raises the total to 15.

## Exercise 2 — Reward noise

`reward_std=3.0` makes learning harder. Samples from different arms overlap
more, so a high observation is weaker evidence that an arm's true mean is high.
With `reward_std=0.1`, estimates usually separate the arms after fewer pulls.

## Exercise 3 — Epsilon extremes

- `epsilon=0` is greedy: it never deliberately explores, although random
  tie-breaking initially gives untried arms some chance.
- `epsilon=0.1` explores on 10% of decisions and otherwise acts greedily.
- `epsilon=1` chooses uniformly at random on every decision; estimates are
  updated but never used to select an action.

## Exercise 4 — More arms or fewer steps

There is no universal best epsilon; the result should be averaged across many
seeds. A reasonable hypothesis is that 20 arms increases the need to explore,
while a 20-step horizon makes exploration more expensive because there is
little time to benefit from what it discovers. Thus the best tested epsilon
may move upward with more arms but downward with fewer steps. Noise, gaps
between arm means, and the epsilon values being compared can change the result.
