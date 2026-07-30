# Exercise 2 — Run a Plan and Keep a Record

## Objective

Use the completed `Bandit` in an interaction loop. A written plan supplies the
actions, and your function records the rewards.

## Starter guidance

Continue in `project.py` and complete the TODOs marked `Exercise 2`.

### Checkpoint 1: start the record

In `run_plan`, create an empty list named `rewards`.

At this point:

```text
planned_arms contains what the person chose
rewards contains what the machine returned
```

### Checkpoint 2: run each action

For each `arm` in `planned_arms`:

1. call `bandit.pull(arm)`;
2. store the returned value in `reward`;
3. append `reward` to `rewards`.

Return the finished list after the loop.

### Checkpoint 3: inspect two plans

The starter runs these plans on fresh bandits:

```python
try_each_arm = [0, 1, 2, 0, 1, 2]
repeat_arm_one = [1, 1, 1, 1, 1, 1]
```

Before running them, answer:

- Which rewards are possible for each plan?
- Which plan is more predictable?
- Does either plan react to the rewards it receives?

Then run the file. Record the action list, reward list, and total for both
plans. Describe one thing the result confirms and one thing that surprised
you.

## A working submission demonstrates

- there is one recorded reward for every planned action;
- the action order is preserved;
- each plan starts with a fresh bandit using the same seed;
- the report clearly separates actions from rewards;
- you can explain why a fixed plan is not a learning program.

## Leave for later

Do not compare plans using a single run and declare a winner. Comparing choice
rules fairly requires ideas that belong in a later lesson.
