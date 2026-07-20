# Exercise 1 — Describe and sample a fixed policy

## Objective

Represent a stochastic policy on the Week 2 Gridworld and use rollouts to
estimate what that policy is worth from selected states.

## Starter guidance

Open `project.py` and complete the Exercise 1 TODOs.

- Finish the pure `transition` model using the same rules as Week 2.
- Complete `random_policy`, which assigns equal probability to all four actions
  in every nonterminal state.
- Implement `sample_action` and `sample_return`. The return must discount each
  later reward by another factor of `gamma`.
- Estimate the start state's value from many sampled episodes. Use
  `max_steps` so a wandering policy cannot run forever.

Before running the code, calculate the return of rewards `[-1, -1, 10]` when
`gamma=0.9`. Compare that calculation with your loop.

## A working submission demonstrates

- the policy probabilities are valid distributions;
- actions are sampled according to the policy rather than chosen greedily;
- rewards are discounted in the correct order;
- repeated rollouts give a plausible but noisy estimate of state value.
