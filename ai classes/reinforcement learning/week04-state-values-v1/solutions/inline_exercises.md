# Week 4 Inline Exercise Solutions

## Exercise 1 — Follow a fixed policy

Starting at `(2, 1)`, the visited states are:

```text
(2, 1), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2)
```

The actions are left, up, up, right, and right. The last state is terminal, so
the policy does not supply another action there.

## Exercise 2 — Add future rewards

The return from the beginning is:

```text
-1 + -1 + -1 + 10 = 7
```

Immediately before the final action, only the reward `10` remains, so the
return is `10`.

## Exercise 3 — Work backward

The backward loop calculates:

```text
10, 9, 8
```

Matched back to forward states, the returns are:

```text
A: 8
B: 9
C: 10
```

Each earlier state includes one additional `-1` step.

## Exercise 4 — Value requires a policy

Different policies can choose different actions from `(0, 0)`. One may reach
the goal quickly, another may wander, and another may reach the trap. Those
routes have different future reward totals, so the policy is part of the state
value's meaning.

## Exercise 5 — Equal values from different states

The policy moves directly into the goal from both `(0, 1)` and `(1, 2)`. Each
state therefore has exactly one remaining reward, `10`, even though the states
have different coordinates.
