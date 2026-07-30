# Exercise 2 — Add Variation and Record What Happens

## What you are changing

The predictable machine always returns the same reward. Now each arm will
return values near its typical reward.

You will also try every arm several times and save what happened.

## Part 1: make rewards vary

Continue in `project.py` with the TODOs marked `Exercise 2`.

The starter already creates:

```python
self.randomizer = Random(seed)
```

In `pull`, replace the predictable reward with:

```python
reward = self.randomizer.gauss(typical_reward, self.reward_spread)
```

Read this line as:

> Make a reward near this arm's typical reward, using this amount of spread.

Run the program. Pulling arm `1` twice should now usually produce two different
numbers.

Set `reward_spread` to `0.0` and run it again. Explain why the results stop
changing.

## Part 2: try every arm

Complete `try_every_arm`.

Use this exact order:

1. Start an empty list named `all_rewards`.
2. For each arm, start an empty list named `rewards_for_this_arm`.
3. Pull that arm `pulls_per_arm` times.
4. Append each reward to `rewards_for_this_arm`.
5. After finishing one arm, append its list to `all_rewards`.
6. Return `all_rewards`.

The nesting has a meaning:

```text
all_rewards
├── rewards from arm 0
├── rewards from arm 1
└── rewards from arm 2
```

For three arms and four pulls per arm, the result should contain three inner
lists, each with four numbers.

## Part 3: read the evidence

The provided code prints the rewards and the average for each arm.

Answer in three or four sentences:

1. Which arm seems to give the highest rewards?
2. What observations support your answer?
3. Could one unusually high reward mislead you?
4. Why is trying each arm several times more useful than trying it once?

## A working submission shows

- rewards vary when `reward_spread` is greater than zero;
- the same seed repeats the same sequence;
- every arm is tried the requested number of times;
- you can connect each inner list to one arm;
- your explanation refers to several observations, not just the largest one.

## Leave for later

The program still does not decide which arm to pull. A person tells it to try
every arm. Automatic choice is a later topic.
