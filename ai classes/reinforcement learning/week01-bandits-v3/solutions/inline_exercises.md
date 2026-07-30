# Week 1 Inline Exercise Solutions

## Exercise 1 — Keep the coin available

The next reward can be `1` or `7`. The first coin remains available, so the
coin list is still `[1, 1, 1, 7]`. Receiving `1` once does not remove any
possibility from the next turn.

## Exercise 2 — Name the interaction

- The player is the **agent**.
- The game is the **environment**.
- `jump` is the **action**.
- `-2` is the **reward**.

In ordinary speech, a reward often sounds positive. In reinforcement learning,
“reward” is the technical name for the number returned by the environment, so
negative two still counts.

## Exercise 3 — Read a list position

The result is `2` because position `0` contains the first item. The line does
not make a random choice; it always reads position `0`.

This distinction prepares students to see that randomness enters only when
the code calls `randomizer.choice`.

## Exercise 4 — Repeated coins

`first_coins` should produce `1` more often because three of its four entries
are `1`. `second_coins` has more different possible rewards: `1`, `3`, `5`,
and `7`.

The exact rewards in a short run depend on the seed and luck. “More often”
describes a pattern expected across many choices, not a guarantee for every
few choices.

## Exercise 5 — Follow one arm

`bandit.pull(1)` selects the second inner list:

```python
[3, 3, 3, 3]
```

Every possible return value is `3`. Randomly choosing a coin has no visible
effect when every coin shows the same number.

## Exercise 6 — Separate actions and rewards

One valid plan is `[0, 1, 2, 0]`. Many other answers are possible as long as
`0`, `1`, and `2` each appear at least once.

`planned_arms` represents the actions. The `rewards` list records the values
returned by the environment. The precise rewards depend on the bandit's seed.
