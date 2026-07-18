# Stretch — Is the state really Markov?

Add a locked door and a key to Gridworld. The door acts like a wall until the
key has been collected; afterward it can be crossed. Location alone now fails
to predict the result of entering the door.

Redesign the state as `((row, col), has_key)` and update reset, transition,
rendering, and rollout. Demonstrate two transitions that start at the same
location and take the same action but differ because `has_key` differs. Then
explain in 3–5 sentences why the expanded state restores the Markov property.

The exercise is complete when the key can be collected, possession persists,
the locked/unlocked door behaves correctly, terminal rules still work, and the
demonstration makes the state-aliasing problem visible. Do not add a learning
algorithm; the challenge is modeling the environment correctly.
