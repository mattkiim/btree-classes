# Week 6 Inline Exercise Solutions

## Exercise 1 — Build a one-step target

For the ordinary transition, the target is:

```text
-1 + 6 = 5
```

For the terminal transition, the target is just `10`. No future estimate is
added after the episode ends.

## Exercise 2 — Move partway toward a target

The current estimate is `2`, the target is `8`, and the gap is `6`. Moving
one-quarter of the gap changes the estimate by `1.5`:

```text
new estimate = 2 + 1.5 = 3.5
```

## Exercise 3 — The first successful episode

At the first step, `(0, 1)` still has estimate `0`, so the starting target is:

```text
-1 + 0 = -1
```

Later in the same episode, entering the goal moves `(0, 1)` toward `10`. A
future episode can then use that improved next-state estimate when updating
the start.

## Exercise 4 — Compare update timing

The Week 5 learner waits until the episode ends because it needs the complete
return. The Week 6 learner updates immediately because its target uses one
reward and the next state's current estimate. The Week 6 target is available
after one transition, but it can be inaccurate while the next estimate is
still inaccurate.

## Exercise 5 — Read update counts

The start is visited in every episode, so it has `1000` updates. The goal-side
state is visited only during the `511` goal episodes. The trap-side states are
visited only during the `489` trap episodes. A count describes visits and
updates, not how good a state is.
