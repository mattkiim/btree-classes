# Exercise 1 — Improve a policy with one-step lookahead

## Objective

Use a value table and the Gridworld model to compare actions and construct a
greedy policy.

## Starter guidance

Open `project.py` and complete the Exercise 1 TODOs.

- Implement `action_value` using one transition, its reward, and the next
  state's value.
- Implement `greedy_actions`. Return every maximizing action so ties remain
  visible and are not silently broken by dictionary order.
- Complete `policy_evaluation` for a deterministic policy.
- Complete `improve_policy` and report whether any state's action changed.

Inspect the four action-values beside the goal, beside the pit, and against a
wall. Explain each ranking using the model.

## A working submission demonstrates

- one-step lookahead handles terminal transitions without double-counting;
- greedy actions maximize predicted return, not immediate reward alone;
- ties are identified deliberately;
- policy evaluation and improvement are separate operations.
