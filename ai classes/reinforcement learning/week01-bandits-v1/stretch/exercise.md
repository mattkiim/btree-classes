# Stretch — Decaying epsilon

Fixed epsilon keeps exploring forever. Design a schedule that starts with broad
exploration and gradually exploits more often.

Implement an epsilon-greedy agent whose epsilon at step $t$ is, for example,

$$
\epsilon_t = \max(0.01, 1 / \sqrt{t+1}).
$$

Compare it with the best fixed epsilon from Exercise 3 over 2,000 steps and at
least 100 independent runs. Plot mean cumulative reward and mean cumulative
regret. Label the schedule clearly and report whether its advantage changes
between the first 100 and last 500 steps.

Your submission is complete when the schedule uses the current step (without
peeking at true arm means), the comparison is repeated and fair, both plots are
labeled, and a short paragraph explains one benefit and one risk of decaying
exploration. This previews adaptive exploration later in the course.
