# Week 3 Inline Exercise Solutions

## Exercise 1 — Discounted returns

For rewards `[-1, -1, 10]`:

- $\gamma=0$: $-1$
- $\gamma=0.5$: $-1+0.5(-1)+0.5^2(10)=1$
- $\gamma=1$: $-1-1+10=8$

$\gamma=1$ gives the eventual goal reward the greatest weight. This does not
mean it always gives every successful route the same return: extra undiscounted
step costs still make longer routes worse.

## Exercise 2 — High action-value, low state-value

Yes. Suppose `RIGHT` heads toward the goal, but the policy selects it only 1%
of the time and usually chooses actions that hit walls or head toward the pit.
Fixing the first action to `RIGHT` can give a high $q_\pi(s,\text{RIGHT})$ while
the policy-weighted average $v_\pi(s)$ remains low.

## Exercise 3 — Number of rollouts

Ten rollouts usually produce a visibly noisy estimate that changes greatly
between random seeds. One hundred is steadier, and 10,000 should be much more
stable and close to the expected value. The sampling error typically shrinks
in proportion to $1/\sqrt{n}$, so using 100 times as many rollouts reduces the
typical error by about a factor of 10, not 100.

The exact estimates depend on the seed, and a finite `max_steps` can introduce
cutoff bias if many episodes have not terminated.

## Exercise 4 — Values spreading across sweeps

The first sweep begins with successor values at zero. Each backup can use only
the value information currently available, so effects from terminal rewards
must propagate through predecessor states over repeated sweeps. In-place
updates may carry information through several states in one sweep, depending
on iteration order, but they still do not generally solve every mutually
dependent Bellman equation immediately.
