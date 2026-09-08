# High-School Reinforcement Learning Syllabus

**Format:** Approximately 15–30 weeks, depending on whether each unit takes
one or two class meetings.

**Assumed background:** Python fundamentals; no prior reinforcement-learning
or mathematics background.

**Approach:** Build an environment first, inspect its behavior, and then add
one learning idea at a time. Code, small examples, and observable results come
before formal notation.

---

## Course throughline

The first six weeks form two matching sequences:

```text
Bandit environment → bandit agent

Gridworld environment → exact values → episode learning → step learning
```

The same small examples are reused across several weeks. This makes it easier
to see what each new method changes without also learning a new environment.

## Week 1 — Build a Multi-Armed Bandit

- **Concepts:** environment, action, reward, random samples, mean, and reward spread
- **Environment:** a three-button bandit that returns coins
- **Activity:** build deterministic buttons first, then improve them so rewards can vary
- **Deliverable:** a working bandit environment and graphs of sampled rewards
- **Materials:** `week01-bandits`

## Week 2 — Train an Agent on the Bandit

- **Concepts:** agent memory, reward estimates, exploration, exploitation, and a training loop
- **Environment:** the Week 1 bandit
- **Activity:** record rewards, estimate each button, and let an agent choose buttons automatically
- **Deliverable:** a trained bandit agent with estimate and action-count graphs
- **Materials:** `week02-bandit-agent-v1`

## Week 3 — Build a Gridworld Environment

- **Concepts:** state, action, transition, terminal state, episode, and reset
- **Environment:** a deterministic three-by-three Gridworld with a wall, goal, and trap
- **Activity:** represent locations, apply movement rules, and record complete paths
- **Deliverable:** a Gridworld that returns next state, reward, and an ending signal
- **Materials:** `week03-gridworld-v1`

## Week 4 — Understand State Values

- **Concepts:** fixed policy, immediate reward, return, expected future reward, and state value
- **Environment:** the Week 3 Gridworld
- **Activity:** follow one deterministic policy, calculate returns backward, and evaluate every open state
- **Deliverable:** an exact state-value map for a fixed policy
- **Materials:** `week04-state-values-v1`

## Week 5 — Learn State Values from Complete Episodes

- **Concepts:** return samples, value estimates, sample counts, complete-episode learning, and Monte Carlo learning
- **Environment:** the same Gridworld with a policy that can take one of two routes
- **Activity:** collect complete episodes and average the observed returns for each visited state
- **Deliverable:** a state-value learner and a graph of its starting-state estimate
- **Materials:** `week05-state-value-learning-v1`

## Week 6 — Learn State Values After Each Step

- **Concepts:** one-step target, learning rate, update gap, temporal-difference learning, and bootstrapping
- **Environment:** the same Gridworld and branching policy
- **Activity:** update a state immediately using one reward and the next state's current estimate
- **Deliverable:** a step-by-step value learner and a comparison with complete-episode learning
- **Materials:** `week06-step-value-learning-v1`

## Week 7 — Learn Action Values and Improve a Policy

- **Concepts:** state-action value, choosing among movements, exploratory choice, and Q-learning
- **Environment:** the same Gridworld
- **Activity:** store one estimate for each state-action pair and use those estimates to improve movement choices
- **Deliverable:** a Gridworld agent that learns a route to the goal
- **Planned materials:** `week07-action-values-qlearning`

## Week 8 — Investigate Exploration

- **Concepts:** exploration rate, decaying exploration, optimistic starting estimates, and fair comparisons
- **Environment:** the Week 7 Gridworld agent
- **Activity:** keep Q-learning fixed while changing only the exploration rule
- **Deliverable:** comparison graphs and a short evidence-based explanation of the results
- **Planned materials:** `week08-exploration`

## Week 9 — Compare SARSA and Q-Learning

- **Concepts:** learning from the action actually taken versus the best-looking next action
- **Environment:** CliffWalking
- **Activity:** train both agents, inspect their learned routes, and connect differences to their update targets
- **Deliverable:** side-by-side route and reward comparisons
- **Planned materials:** `week09-sarsa-qlearning`

## Week 10 — Replace a Table with Function Approximation

- **Concepts:** limits of lookup tables, features, prediction from features, and generalization
- **Environment:** MountainCar
- **Activity:** replace a state-action table with a small linear prediction function
- **Deliverable:** a value approximation that can represent many related states
- **Planned materials:** `week10-function-approximation`

## Week 11 — Deep Q-Learning

- **Concepts:** neural-network value estimates, experience replay, and a separate target network
- **Environment:** CartPole, with LunarLander as an optional extension
- **Activity:** train a DQN and inspect how replay and target updates affect its learning curve
- **Deliverable:** a trained CartPole agent and a documented training graph
- **Planned materials:** `week11-dqn`

## Week 12 — Learn a Policy Directly

- **Concepts:** policy probabilities, sampled actions, policy gradients, and reward-weighted updates
- **Environment:** CartPole revisited
- **Activity:** implement REINFORCE and compare its behavior with the Week 11 value-based agent
- **Deliverable:** a trained policy and a focused comparison with DQN
- **Planned materials:** `week12-policy-gradients`

## Week 13 — Combine a Policy and a Value Estimate

- **Concepts:** actor, critic, baseline, and advantage as “better or worse than expected”
- **Environment:** LunarLander or Pendulum
- **Activity:** let one component choose actions while another evaluates them
- **Deliverable:** a basic actor-critic agent and an explanation of both components' jobs
- **Planned materials:** `week13-actor-critic`

## Week 14 — Use PPO and Evaluate Training Carefully

- **Concepts:** limiting policy changes, clipped updates, hyperparameters, evaluation runs, and random seeds
- **Environment:** LunarLander or another suitable continuous-control task
- **Activity:** train PPO with Stable-Baselines3 and vary one setting at a time
- **Deliverable:** a reproducible PPO experiment with learning and evaluation graphs
- **Planned materials:** `week14-ppo-evaluation`

## Week 15 — Safety, Partial Information, and Final Projects

- **Concepts:** reward hacking, incomplete observations, distribution shift, and reliable evaluation
- **Environment:** a prior environment or another approved Gymnasium environment
- **Activity:** investigate a learning method or a safety and evaluation question
- **Deliverable:** a final project, demonstration, and evidence-backed reflection
- **Planned materials:** `week15-safety-final-projects`

---

## Optional extension units

If the course runs longer than 15 weeks, useful extensions include:

- first-visit versus every-visit Monte Carlo learning;
- eligibility traces and multi-step targets;
- imitation learning and behavior cloning;
- offline reinforcement learning and dataset shift;
- partial observability and memory;
- reward design and reward hacking;
- multi-agent environments;
- additional time for final-project experiments and presentations.

## Core packages

- **Python standard library** — early bandit and Gridworld implementations
- **Matplotlib** — distributions, value maps, learning curves, and comparisons
- **Gymnasium** — CliffWalking, MountainCar, CartPole, and later environments
- **NumPy** — arrays and numerical operations when table size grows
- **Stable-Baselines3** — PPO and selected later-course comparisons

The early weeks intentionally avoid requiring Gymnasium or deep-learning
packages. They are introduced only when the environment or method benefits
from them.
