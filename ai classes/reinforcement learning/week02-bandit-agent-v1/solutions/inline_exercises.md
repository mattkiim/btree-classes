# Week 2 Inline Exercise Solutions

## Exercise 1 — Hidden environment information

The method reads `bandit.mean_rewards`, which reveals the environment's hidden
answer. The agent should learn only from the arms it chose and the rewards it
received. Otherwise, the program is selecting with perfect knowledge rather
than training.

## Exercise 2 — Update an estimate

The old rewards total `10.0`. After receiving `5.0`:

- count: `3`;
- total reward: `15.0`;
- estimate: `15.0 / 3 = 5.0`.

Only the selected arm's three records should change.

## Exercise 3 — Try an untested arm

The method returns arm `1`. Its count is zero, so the initial-testing rule takes
priority over the current estimates. The estimate `0.0` means “no evidence” for
this arm, not “known to be bad.”

## Exercise 4 — Exploration or exploitation

1. Choosing arm 2 because it has the largest estimate is **exploitation**.
2. Randomly choosing arm 0 instead is **exploration**.
3. Choosing an untested arm is also **exploration** because it gathers missing
   information.

The initial-testing rule guarantees exploration, while `exploration_rate`
continues occasional exploration afterward.

## Exercise 5 — Uneven estimate movement

Arm 0 is selected fewer times than arm 1. Each new reward therefore represents
a larger fraction of all evidence about arm 0 and can move its average more.
Arm 1 has many more samples, so one additional reward usually has a smaller
effect on its estimate.
