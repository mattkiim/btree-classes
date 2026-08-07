# Optional Stretch — Play the Bandit by Hand

The core project samples every arm in order. In this stretch, a person chooses
the next arm after seeing earlier rewards.

Implement:

```python
def play_by_hand(bandit, number_of_turns):
    ...
```

On each turn:

1. Show the valid arm numbers.
2. Ask for an arm number with `input`.
3. Pull that arm.
4. Show the returned reward and current total.
5. Save the arm and reward.

Return `(chosen_arms, rewards)` after the final turn. If an arm number is
invalid, explain the valid range and ask again without using up a turn.

## Predictable test first

Use this input so the first test has exact results:

```python
bandit = Bandit([2.0, 5.0, 3.0], reward_std=0.0, seed=7)
arms, rewards = play_by_hand(bandit, number_of_turns=3)
```

Sample keyboard input:

```text
0
2
1
```

Sample output:

```text
Choose an arm (0-2): 0
Reward: 2.0 | Total: 2.0
Choose an arm (0-2): 2
Reward: 3.0 | Total: 5.0
Choose an arm (0-2): 1
Reward: 5.0 | Total: 10.0
```

Expected returned values:

```python
arms == [0, 2, 1]
rewards == [2.0, 3.0, 5.0]
```

After the predictable test passes, change `reward_std` to `1.0` and play ten
turns. The exact rewards will vary.

## Reflection

- Which arm did you try first, and why?
- Did one reward change your next choice?
- Did you try every arm before repeating one?
- Why would another player need the same seed for an exact comparison?

Trying different arms to learn about them will later be called
**exploration**. Repeating an arm that looks promising will later be called
**exploitation**. These are preview words; an automatic choosing rule belongs
to a later lesson.
