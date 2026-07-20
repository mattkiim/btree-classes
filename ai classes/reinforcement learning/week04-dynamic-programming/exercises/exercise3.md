# Exercise 3 — Compare value iteration and policy iteration

## Objective

Implement value iteration, visualize convergence, and compare its work and
result with policy iteration.

## Starter guidance

Complete the Exercise 3 TODOs in `project.py`.

- In each value-iteration sweep, set a state's value to the largest one-step
  action-value.
- Record a full value-table snapshot after every sweep and stop when the
  largest change is below `theta`.
- Extract a deterministic greedy policy after values converge.
- Implement the plotting helper so selected snapshots show values and policy
  arrows. Use it to create a frame-by-frame view or a `matplotlib` animation.
- Compare the final policies, start-state values, number of outer iterations,
  and number of state backups. Explain why iteration counts alone are not a
  fair measure of work.

Optional stress test: change `gamma` or move one wall, then predict which parts
of the policy will change before rerunning both algorithms.

## A working submission demonstrates

- the Bellman optimality backup uses a maximum over actions;
- convergence is measured numerically and histories contain independent
  snapshots rather than repeated references to one dictionary;
- both algorithms produce equally valuable start behavior (ties may differ);
- the comparison distinguishes sweeps, evaluations, and state backups.
