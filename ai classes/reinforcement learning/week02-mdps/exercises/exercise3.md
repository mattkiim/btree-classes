# Exercise 3 — Run and audit policies

## Objective

Use the finished MDP to execute a policy, record a trajectory, and systematically
inspect the model for mistakes.

## Starter guidance

Complete the Exercise 3 TODOs in `project.py`.

- `rollout` resets the environment, asks the policy for one action per state,
  and records `(state, action, reward, next_state)`.
- Stop on termination or at `max_steps` so loops are safe.
- Fill in `SAFE_POLICY` with a route from start to goal that avoids the pit.
- Implement `print_transition_table` for all actions in every nonterminal state.

Run both the safe policy and a deliberately bad policy. Report the terminal
state, number of steps, and total reward for each.

## A working submission demonstrates

- a trajectory accurately records environment interaction;
- the safe policy reaches the goal without relying on hidden state;
- loops are bounded by `max_steps`;
- transition-table inspection covers walls, boundaries, and terminal entries.
