# Exercise 2 — Implement the MDP rules

## Objective

Implement the transition and reward functions, then connect them to a stateful
`step` method.

## Starter guidance

Complete the Exercise 2 TODOs in `project.py`.

- `transition(state, action)` must not mutate the environment.
- A boundary or wall collision returns the same state with the ordinary step
  cost.
- Entering the goal or pit returns its special reward and `done=True`.
- `step(action)` applies that model to `self.state` and refuses moves after the
  episode ends.

Manually test a boundary, a wall, an ordinary move, entry into the goal, and
entry into the pit. Write down expected triples before running each test.

## A working submission demonstrates

- every state-action pair has a predictable result;
- rewards depend on the resulting transition;
- pure transition queries do not move the live agent;
- terminal behavior is enforced consistently.
