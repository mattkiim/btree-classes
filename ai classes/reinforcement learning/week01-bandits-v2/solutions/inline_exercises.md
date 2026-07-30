# Week 1 Inline Exercise Solutions

## Exercise 1 — Name the parts

- The game character is the **agent** because it makes the choice.
- The game is the **environment** because it receives the choice and responds.
- `left` is the **action**.
- `-1` is the **reward**.

Yes, `-1` is still called a reward. In ordinary speech, “reward” often means
something good. In reinforcement learning, it is the technical name for the
number the environment returns.

## Exercise 2 — Read the predictable code

The output is:

```text
2
-2.0
```

The first line says that the machine has two buttons. The second says that
choosing the button in position `1` returns negative two points.

## Exercise 3 — Change the spread

The rewards from `noisy` will be more spread out because its
`reward_spread` is `3.0` instead of `0.2`.

Both arms still have a typical reward of `5.0`. The spread changes how far
individual results tend to be from 5; it does not change the center.

## Exercise 4 — Compare two records

Person B's list gives more confidence because it records six tries instead of
two. In Person A's list, each unusual result has a large effect on the
average. Person B has more evidence that results on both sides of 5 balance
out.

More observations do not prove the typical reward with certainty, but they
usually give a more stable picture.
