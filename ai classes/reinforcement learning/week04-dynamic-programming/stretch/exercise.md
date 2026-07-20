# Stretch — Add slippery actions

Make Gridworld stochastic: the intended action occurs with probability `0.8`,
while the two perpendicular actions each occur with probability `0.1`. Replace
the deterministic model result with a list of
`(probability, next_state, reward, done)` outcomes. Combine duplicate outcomes
when a wall or boundary makes several actions land in the same state.

Update action-value calculations, policy evaluation, policy iteration, and
value iteration to take probability-weighted sums. Compare the deterministic
and slippery optimal policies, especially near the pit. Visualize both and
explain why a longer route can become optimal when actions are unreliable.

The exercise is complete when outcome probabilities sum to one, expected
returns include every outcome, both algorithms agree on optimal value, and a
short analysis identifies at least one risk-sensitive policy change. This
previews the stochastic environments used later in the course.
