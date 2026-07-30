# Week 1 — Build a Button-and-Coin Bandit

## Goal

This week, we will build a Python machine with three buttons. Behind each
button is a small collection of coins. When someone presses a button, the
machine picks one of that button's coins and returns the points written on it.

By the end of the week, you will be able to:

- describe a choice-and-response interaction in ordinary language;
- connect the words **agent**, **environment**, **action**, and **reward** to
  that interaction;
- use a list of coins to represent the possible results of one button;
- implement a multi-armed bandit as a Python class;
- run a written plan of button choices and record what happened.

The project ends with a working environment. A person still decides which
buttons to try.

## Start away from the computer

Imagine a machine with three buttons. Behind each button are four hidden coins:

```text
button 0:  1, 1, 1, 7
button 1:  3, 3, 3, 3
button 2:  0, 2, 4, 6
```

To press a button:

1. Choose and press a button.
2. The machine randomly picks one coin from behind that button.
3. The machine returns the points written on the coin.
4. The coin remains available for the next press.

Keeping the coin available matters. The possible rewards stay the same on
every turn.

Before writing code, discuss:

- Which button would you press first?
- Which button is the most predictable?
- Which button can give the largest reward?
- Could two people follow the same choices and finish with different scores?

These questions have different answers. “Largest possible reward” and “most
predictable reward” do not mean the same thing.

### Inline exercise 1

A student chooses button 0 and receives `1`. List every reward that could
appear the next time the student chooses button 0.

## Ordinary words and course words

Reinforcement learning uses some familiar words in specific ways.

### The person and the machine

In ordinary language:

```text
person chooses a button → machine returns points
```

In reinforcement-learning language:

```text
agent chooses an action → environment returns a reward
```

Both lines describe the same event.

- The **agent** is the chooser. This week, the agent is a person.
- The **environment** is what receives the choice and responds. The
  button-and-coin machine is the environment.
- The **action** is the choice sent to the environment. The button number is
  the action.
- The **reward** is the number returned by the environment.

In ordinary language, “reward” often means a prize. In reinforcement learning,
**reward** is a technical name for the returned number. A reward can be
positive, zero, or negative.

### Why “bandit” and “arm”?

An old nickname for a slot machine is a “one-armed bandit.” The field still
uses that name:

- one button is called an **arm**;
- choosing a button is called **pulling an arm**;
- the whole machine is called a **multi-armed bandit**.

We will sometimes say “button” when explaining an idea and `arm` when matching
the code.

### Inline exercise 2

In a game, a player chooses `jump`. The game returns `-2` points.

Name the agent, environment, action, and reward. Explain why `-2` is still
called a reward.

## Represent one button with a list

A Python list can stand for the coins behind one button:

```python
# Store the four reward coins behind button 0.
button_0_coins = [1, 1, 1, 7]

# Look at the reward written on the first coin.
first_coin = button_0_coins[0]

# Show that reward.
print(first_coin)
```

This prints:

```text
1
```

The list does not choose a coin by itself. It only stores the possibilities.

### Inline exercise 3

Change the list to `[2, 2, 5]`. Before running the code, predict what
`button_0_coins[0]` will return. Does that line make a random choice?

## Let Python choose a coin

Python's `Random` class can choose one item from a list:

```python
# Import Python's random-choice tool.
from random import Random

# Create a repeatable random-number generator.
randomizer = Random(7)

# Store the reward coins behind one button.
reward_coins = [1, 1, 1, 7]

# Choose one coin from the list.
reward = randomizer.choice(reward_coins)

# Show the chosen coin's reward.
print(reward)
```

Read this line:

```python
# Choose one item from reward_coins and store it in reward.
reward = randomizer.choice(reward_coins)
```

The repeated `1` coins are intentional. Three of the four coins contain `1`,
so receiving `1` is more common than receiving `7`.

The number `7` passed to `Random` is a **seed**. The same seed repeats the same
sequence of choices. This helps us debug: if two runs behave differently, we
can check whether the code changed rather than wondering whether luck changed.

The seed does not make every choice identical. It makes the whole sequence
repeatable.

### Inline exercise 4

Compare these two lists:

```python
# Three coins show 1, so 1 should appear more often.
first_coins = [1, 1, 1, 7]

# Each possible reward appears once.
second_coins = [1, 3, 5, 7]
```

Which coin list should produce `1` more often? Which coin list has more
different possible rewards?

## Put all the buttons in one machine

Our machine needs a list for each button. That gives us a list of lists:

```python
# Each inner list holds the coins for one button.
all_reward_coins = [
    [1, 1, 1, 7],  # Button 0
    [3, 3, 3, 3],  # Button 1
    [0, 2, 4, 6],  # Button 2
]
```

The outside list is the machine. Each inside list is one button's collection
of reward coins.

```text
all_reward_coins
├── [1, 1, 1, 7]  ← button 0
├── [3, 3, 3, 3]  ← button 1
└── [0, 2, 4, 6]  ← button 2
```

Now we can turn that representation into a class:

```python
# Import the tool that will choose reward coins.
from random import Random


# Define what a button-and-coin Bandit remembers and does.
class Bandit:
    # Set up a new machine with its reward coins and optional seed.
    def __init__(self, reward_coins, seed=None):
        # Remember the coins behind every arm.
        self.reward_coins = reward_coins

        # Count the inner lists to find the number of arms.
        self.number_of_arms = len(reward_coins)

        # Give this machine its own repeatable random chooser.
        self.randomizer = Random(seed)

    # Pull one arm and return one of its reward coins.
    def pull(self, arm):
        # Find the list of coins behind the chosen arm.
        coins_for_this_arm = self.reward_coins[arm]

        # Choose one coin from that list.
        reward = self.randomizer.choice(coins_for_this_arm)

        # Return the points on the coin.
        return reward
```

Follow one call through the code:

```python
# Create the three-button machine.
bandit = Bandit(
    reward_coins=[
        [1, 1, 1, 7],
        [3, 3, 3, 3],
        [0, 2, 4, 6],
    ],
    seed=7,
)

# Choose arm 2.
# The pull method will choose from [0, 2, 4, 6].
reward = bandit.pull(2)

# Show the returned reward.
print(reward)
```

The person supplies the `2`. The `Bandit` uses `2` to select the third inner
list, chooses one coin, and returns its value.

### Inline exercise 5

For the bandit above, which coin list can `bandit.pull(1)` choose from? List
every possible value it can return.

## Run a written plan

So far, we have typed one choice at a time. A list can store a plan:

```python
# Plan six button choices before seeing any rewards.
planned_arms = [0, 1, 2, 0, 1, 2]
```

We can run that plan with a function:

```python
# Run each planned choice and return the rewards.
def run_plan(bandit, planned_arms):
    # Start with no recorded rewards.
    rewards = []

    # Read one arm at a time from the plan.
    for arm in planned_arms:
        # Ask the bandit for that arm's reward.
        reward = bandit.pull(arm)

        # Add the observed reward to our record.
        rewards.append(reward)

    # Return the complete record.
    return rewards
```

Now use it:

```python
# Create a fresh machine.
bandit = Bandit(
    reward_coins=[
        [1, 1, 1, 7],
        [3, 3, 3, 3],
        [0, 2, 4, 6],
    ],
    seed=7,
)

# Write the choices we want to test.
my_plan = [0, 1, 2, 0, 1, 2]

# Run the plan and save each returned reward.
rewards = run_plan(bandit, my_plan)

# Show the choices and what happened.
print("actions:", my_plan)
print("rewards:", rewards)

# Add the rewards to find the final score.
print("total:", sum(rewards))
```

The plan is not learning. It is fixed before any reward appears. A future
agent will use past rewards to decide its next action.

### Inline exercise 6

Write a four-turn plan that tries every arm at least once. Which part of the
code represents the actions? Which part records the rewards?

## Project checkpoints

The starter project follows the same order as the lecture:

1. Store the reward coins inside `Bandit`.
2. Count the arms.
3. Implement `pull` with `randomizer.choice`.
4. Implement `run_plan` with a loop.
5. Run two plans and describe what happened.

After each checkpoint, predict an output before running the code. If the output
surprises you, trace one value through the lists before changing anything.

## Topic backlog — intentionally saved for later

- **Automatic choosing:** This week, a person writes the plan. Later, the agent
  will choose actions in code.
- **Exploration and exploitation:** These names describe trying uncertain
  choices and using choices that look promising. We will introduce them when
  the program is ready to make decisions.
- **Averages and expected reward:** Later, we will summarize many results.
  This week, the coins let us inspect possible rewards directly.
- **Probability:** Repeated coins make some outcomes more common. We do not
  need probability notation to build the environment.
- **Changing situations:** A bandit presents the same buttons each turn. Next
  week, the environment will have a location that changes after an action.

## Wrap-up

First answer with button-machine language. Then translate to the course words.

- What does the person send to the machine?
- What does the machine send back?
- Why does `[1, 1, 1, 7]` contain three copies of `1`?
- What does the outside list represent?
- What does one inside list represent?
- What job belongs to `Bandit.pull`?
- Why is a written plan not yet a learning agent?

## Next week

The bandit offers the same buttons after every action. Next week, we will build
a small world where an action changes the agent's location. That changing
location will introduce the technical meaning of **state**.

## Common misunderstandings to watch for

- **“An arm is a body part in the code.”** Here, “arm” is the field's name for
  one available button.
- **“Reward means the result must be good.”** Reward is the returned number,
  including zero or a negative number.
- **“The bandit chooses an arm.”** The bandit responds. The person supplies the
  arm number.
- **“`choice` removes a coin.”** `randomizer.choice` reads an item without
  changing the list, so the same coin remains available next time.
- **“A repeated value is a typo.”** Repeated coins make that value more common.
- **“A seed makes every reward the same.”** A seed repeats a sequence; values
  within that sequence can differ.
