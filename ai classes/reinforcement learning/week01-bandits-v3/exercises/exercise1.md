# Exercise 1 — Build the Button-and-Coin Machine

## Objective

Implement a `Bandit` that stores the reward coins behind several buttons and
returns one coin value from the chosen button.

The machine is the **environment**. The arm number passed to `pull` is the
**action**. The number returned by `pull` is the **reward**.

## Starter guidance

Open `project.py` and complete the TODOs marked `Exercise 1`.

### Checkpoint 1: store the coins

In `Bandit.__init__`:

1. Store `reward_coins` on the object.
2. Count the inner lists and store the result as `number_of_arms`.
3. Create the random chooser with the provided `seed`.

Before continuing, print `bandit.number_of_arms`. For the provided machine, you
should predict `3`.

### Checkpoint 2: pull one arm

In `Bandit.pull`:

1. Use `arm` to select one inner list.
2. Use `self.randomizer.choice` to choose one reward from that list.
3. Return the reward.

Test one arm at a time. Every result from arm 1 should be `3`, while arm 0 can
return either `1` or `7`.

### Checkpoint 3: repeat the same sequence

Create two bandits with the same coins and seed. Pull the same arms from both.
Their reward sequences should match.

## A working submission demonstrates

- the machine reports three available arms;
- every reward comes from the chosen arm's list;
- repeated coins make an outcome appear more often without special code;
- matching seeds and actions reproduce the same reward sequence;
- you can explain the input and output of `pull` in ordinary language.

## Leave for later

Do not make the bandit choose an arm. Its job is to respond to an arm number.
A person will provide the choices.
