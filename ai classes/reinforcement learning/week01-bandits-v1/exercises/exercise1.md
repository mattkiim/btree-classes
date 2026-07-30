# Exercise 1 — Build the bandit

## Objective

Implement the environment that turns a chosen arm into a noisy reward.

## Starter guidance

Open `project.py` and complete the Exercise 1 TODOs in `Bandit`.

- Store arm means as a one-dimensional NumPy array.
- Reject an empty list and a non-positive reward standard deviation.
- In `step`, validate the action and sample from the selected arm's normal
  distribution using the provided random generator.
- Run the file and sample every arm several times. Random samples need not equal
  the means, but sample averages should move toward them.

Do not expose the true means to the agent; they belong to the environment.

## A working submission demonstrates

- the number of actions is correct;
- valid actions produce numeric, noisy rewards;
- invalid actions give a useful error;
- identical seeds reproduce identical reward sequences.
