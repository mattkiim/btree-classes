# Optional Stretch — Turn the Bandit into a Playable Game

The core project runs a plan written before the rewards appear. In this
optional extension, let a person choose the next arm after seeing earlier
results.

Write:

```python
def play_by_hand(bandit, number_of_turns):
    ...
```

On each turn:

1. Show the valid arm numbers.
2. Ask for an arm with `input`.
3. Pull that arm.
4. Show the returned reward and current total.
5. Record the arm and reward.

Return both records after the final turn.

Handle an invalid arm by explaining the valid choices and asking again. An
invalid attempt should not use up a turn.

After playing ten turns, answer:

- Which arm did you try first, and why?
- Did a reward cause you to change your next choice?
- Did you spend turns learning about different arms?
- Did you repeat an arm that looked promising?

## Vocabulary preview

Trying different arms to learn what they can do is later called
**exploration**. Using an arm that currently looks promising is later called
**exploitation**.

These names describe choices you may make while playing. Building an automatic
choosing rule belongs to a later lesson.
