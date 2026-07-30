# Exercise 1 — Build Predictable Buttons

## What you are building

You will make the first version of the mystery-button machine. Each button will
always return the same reward.

In reinforcement-learning vocabulary, the machine is the **environment**, a
button number is an **action**, and the points returned are the **reward**.

## Work in small steps

Open `project.py`. Work only on TODOs marked `Exercise 1`.

### Step 1: remember the rewards

In `Bandit.__init__`, store `typical_rewards` on the object:

```python
self.typical_rewards = list(typical_rewards)
```

We make a new list so the `Bandit` object keeps its own record.

### Step 2: count the buttons

Set `self.number_of_arms` to the length of that list. Remember that **arm** is
the bandit word for a button.

### Step 3: return one button's reward

In `pull`, use `arm` as a list position. Store the chosen value in a clearly
named variable, then return it.

For Exercise 1, do not use randomness yet. If arm `1` has a typical reward of
`5.0`, pulling it should return exactly `5.0`.

### Step 4: predict, then run

Before running the file, complete this table:

| Code | Your predicted output |
|---|---|
| `bandit.number_of_arms` | |
| `bandit.pull(0)` | |
| `bandit.pull(1)` | |
| `bandit.pull(1)` again | |

Run the file and compare the output with your predictions.

## A working submission shows

- the object remembers all three typical rewards;
- `number_of_arms` is `3`;
- valid arm numbers return the corresponding rewards;
- you can explain how `pull(arm)` maps a choice to a result.

## Leave for later

Do not add random rewards or a choosing strategy yet. Those changes are easier
to understand after the predictable version works.
