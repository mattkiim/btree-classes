# Exercise 3 — Compare exploration strategies

## Objective

Run a controlled, repeated experiment comparing greedy and epsilon-greedy
agents, then communicate the result with a plot and short interpretation.

## Starter guidance

Complete the Exercise 3 TODOs in `project.py`.

- For each epsilon and run, create a fresh environment and agent.
- Use many runs so luck in one reward sequence does not decide the conclusion.
- Compute mean cumulative reward at every step.
- Plot `epsilon=0.0`, `0.1`, and `0.3` together with the oracle benchmark
  `step * max(means)`.
- Save or inspect the plot, then write 4–6 sentences: Which policy wins early?
  Which wins late? How does noise affect confidence? Why is the oracle higher?

Optional stress test: repeat with 20 arms or a larger reward standard deviation.

## A working submission demonstrates

- strategies are compared under matching conditions;
- results are averaged over independent runs;
- axes, legend, and title make the plot understandable;
- conclusions refer to evidence in the plot rather than one anecdotal run.
