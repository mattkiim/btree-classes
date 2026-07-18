# Exercise 2 — Make an epsilon-greedy learner

## Objective

Implement an agent that balances exploration and exploitation and learns
sample-average action values.

## Starter guidance

Continue in `project.py` and complete the Exercise 2 TODOs.

- `choose_action` should explore with probability `epsilon` and otherwise select
  randomly among all actions tied for the largest estimate.
- `update` should increment the selected action's count and use the incremental
  sample-average formula.
- `run_bandit` should connect environment and agent for the requested steps and
  return rewards and actions.

Test `epsilon=0` and `epsilon=1`. Print estimates and counts after a run. Explain
why an estimate may still differ from its true mean.

## A working submission demonstrates

- both exploration and exploitation occur as intended;
- only the selected action is updated each step;
- estimates are sample averages;
- a complete interaction loop produces one action and reward per step.
