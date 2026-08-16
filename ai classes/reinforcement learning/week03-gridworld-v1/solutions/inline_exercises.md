# Week 3 Inline Exercise Solutions

## Exercise 1 — Read a state tuple

The bottom row and middle column is `(2, 1)`. The first number, `2`, gives the
row. The second number, `1`, gives the column.

## Exercise 2 — Predict blocked movement

Each test starts at `(0, 1)`:

1. `"down"` results in `(0, 1)` because `(1, 1)` is a wall.
2. `"left"` results in `(0, 0)` because that square is open.
3. `"up"` results in `(0, 1)` because `(-1, 1)` is outside the board.

A blocked action leaves the state unchanged.

## Exercise 3 — Read a transition

For `(2, 0) + "right" → (2, 1)`:

- the state is `(2, 0)`;
- the action is `"right"`;
- the next state is `(2, 1)`.

The transition is the complete change connecting those parts.

## Exercise 4 — Reach a terminal state

From `(0, 1)`, `"right"` enters the goal at `(0, 2)`. The method returns:

```python
((0, 2), 10, True)
```

Another action before `reset()` raises a `RuntimeError`. The `done` value says
that the current episode has ended.

## Exercise 5 — Compare two routes

Route A, `right, right`, ends at the goal `(0, 2)`:

```text
-1 + 10 = 9
```

Route B, `down, down, right, right`, ends at the trap `(2, 2)`:

```text
-1 + -1 + -1 + -10 = -13
```

The final action receives the terminal reward instead of the ordinary step
reward, so Route A has one `-1` and Route B has three.
