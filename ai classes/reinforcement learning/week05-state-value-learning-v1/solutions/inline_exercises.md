# Week 5 Inline Exercise Solutions

## Exercise 1 — Two possible episodes

Choosing `"right"` at `(0, 0)` leads to the goal route with return `9`.
Choosing `"down"` leads to the trap route with return `-13`.

The later actions are fixed, so the first choice determines the entire route.

## Exercise 2 — Average the two returns

If the two routes occur equally often, the long-run average start return is:

```text
(9 + -13) / 2 = -2
```

This does not predict that any individual episode will return `-2`. Each
episode still returns either `9` or `-13`.

## Exercise 3 — Returns along the trap route

The forward rewards are `-1, -1, -1, -10`. Working backward gives running
totals:

```text
-10, -11, -12, -13
```

Matched to forward states:

```text
(0, 0): -13
(1, 0): -12
(2, 0): -11
(2, 1): -10
```

## Exercise 4 — Update an average

The old total is `3 × 5 = 15`. Adding the new return gives `15 + -1 = 14`.
The new count is `4`, so the new estimate is:

```text
14 / 4 = 3.5
```

## Exercise 5 — Zero can mean no evidence

The count for `(1, 2)` is zero, so its displayed estimate of `0.0` is only an
initial placeholder. The episodes starting at `(0, 0)` never visit that state.
It would be incorrect to claim that sampled experience proved its value is
zero.
