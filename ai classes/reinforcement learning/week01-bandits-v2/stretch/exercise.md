# Optional Stretch — Let a Person Choose the Arms

The core project tries every arm in order. For this optional activity, let a
person choose the next arm while the program keeps the record.

Write this function:

```python
def play_by_hand(bandit, number_of_turns):
    ...
```

On each turn:

1. Print the rewards observed so far.
2. Ask the player for an arm number with `input`.
3. Pull that arm.
4. Print the new reward.
5. Save the chosen arm and reward.

Return both lists when the turns are finished.

After playing, answer:

- Did you try every arm?
- When did you repeat an arm that looked good?
- Did one surprising reward change your next choice?

## Vocabulary preview

Trying different arms to learn about them will later be called
**exploration**. Repeating an arm that currently looks good will later be
called **exploitation**.

These are preview words only. You do not need to build an automatic choosing
strategy this week.
