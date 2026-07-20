# Exercise 2 — Evaluate the policy with Bellman updates

## Objective

Compute the complete state-value function for the fixed policy, derive
action-values, and visualize the result.

## Starter guidance

Continue in `project.py` and complete the Exercise 2 TODOs.

- Implement `q_from_v` as one reward plus the discounted value of the next
  state. A transition into a terminal state has no future term.
- In `evaluate_policy`, repeatedly sweep over every nonterminal state and apply
  the Bellman expectation equation.
- Keep terminal values at zero and stop when the largest change in a sweep is
  smaller than `theta`.
- Plot the final values as a heatmap. Mark walls distinctly and annotate each
  occupiable cell with its value.
- Compare the Bellman value of the start state with the sampling estimate from
  Exercise 1. Explain why they may not be exactly equal.

Try `gamma=0`, `0.5`, `0.9`, and `0.99`. Predict which setting makes distant
rewards matter most before generating the plots.

## A working submission demonstrates

- state-values and action-values have distinct, correct meanings;
- each Bellman sweep uses the transition model and policy probabilities;
- iteration stops by measured convergence, not a guessed sweep count;
- the heatmap, sampling check, and written interpretation agree.
