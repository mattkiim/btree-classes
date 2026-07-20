# Week 2 Inline Exercise Solutions

## Exercise 1 — A Markov state

One suitable state is `(row, column, shield_available)`, where the last field is
a Boolean. Location alone aliases two situations with different futures: the
same attack may be harmless before the shield is used and damaging afterward.
The next-state and reward distribution therefore cannot be predicted from
location and action alone.

## Exercise 2 — Predicting transitions

`transition((0, 0), "UP", ...)` returns `((0, 0), -1, False)`. The candidate
position is outside the board, so the agent stays put and pays the step cost.

`transition((3, 4), "DOWN", ...)` returns `((4, 4), 10, True)`. The move enters
the goal and ends the episode.

## Exercise 3 — Recognizing a wall collision

For example, set the action at `(0, 0)` to `"UP"`. Every trajectory entry then
has the same current and next state:

```text
((0, 0), "UP", -1, (0, 0))
```

The repeated unchanged state, repeated `-1` reward, and failure to reach
`done=True` before `max_steps` reveal the problem without a picture.
