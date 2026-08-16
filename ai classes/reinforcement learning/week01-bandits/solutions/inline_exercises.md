# Week 1 Inline Exercise Solutions

## Exercise 1 — A familiar game

- The player is the **agent** because the player makes the choice.
- The game is the **environment** because it receives the choice and responds.
- Pressing jump is the **action**.
- The `100` points are the **reward**.

The character may carry out the jump, but the player is the chooser in this
description. Accept “the character” as the agent if the example is explicitly
reframed so the character chooses for itself.

## Exercise 2 — Deterministic rewards

The results are `4.0`, `-1.0`, and `-1.0`. The repeated action has the same
result because this version is deterministic.

`-1.0` is still a reward because **reward** is the reinforcement-learning name
for the number returned by the environment. It does not have to be pleasant or
positive.

## Exercise 3 — Standard deviation

The button with standard deviation `0.2` is more predictable because its
rewards gather more tightly around `5.0`.

The button with standard deviation `3.0` can still return a value close to
`5.0`. A larger standard deviation spreads the distribution; it does not
forbid values near the mean.

## Exercise 4 — Sample size

Person B's record gives stronger evidence because it contains six observations
instead of two. Each unusually high or low reward has less influence on the
larger record.

Neither record proves that the button's mean is exactly `5`. Random samples can
agree with the true mean by luck, and even six observations leave uncertainty.
