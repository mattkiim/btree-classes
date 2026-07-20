# Exercise 2 — Implement policy iteration

## Objective

Alternate policy evaluation and greedy improvement until the policy is stable.

## Starter guidance

Continue in `project.py` and complete the Exercise 2 TODOs.

- Begin with the provided deterministic policy.
- Evaluate it to convergence, improve it, and repeat.
- Save a copy of the value table after each outer iteration for visualization.
- Stop only when improvement makes no changes, with `max_iterations` as a
  defensive limit.
- Roll out the final policy from the start and verify that it terminates.

Print the policy after every improvement. Identify at least one state whose
preferred action changes because of a consequence more than one step away.

## A working submission demonstrates

- evaluation and improvement alternate in the correct order;
- the stability test compares policies rather than values;
- the final policy reaches the goal while avoiding the pit;
- stored history shows how the solution changes across iterations.
