# High-School Reinforcement Learning Syllabus

**Format:** ~15-30 weeks, 1-2 units per week \
**Approach:** Each week/lession involves training or evaluating a policy. 

---

## Week 1 — What is RL?
- **Concepts:** agents, actions, rewards, exploration vs. exploitation
- **Environment:** custom multi-armed bandit simulator (no state, just action → reward)
- **Activity:** build a bandit one arm at a time, then sample and visualize its rewards
- **Deliverable:** working multi-armed bandit environment + short observations about reward noise

## Week 2 — Markov Decision Processes
- **Concepts:** states, actions, transitions, rewards, the Markov property
- **Environment:** hand-built 5x5 Gridworld (walls, goal, pit)
- **Activity:** students define the MDP themselves in code (states, transition function, reward function)
- **Deliverable:** working Gridworld MDP class

## Week 3 — Value Functions and Bellman Equations
- **Concepts:** state-value and action-value functions, the Bellman expectation equation
- **Environment:** same Gridworld
- **Activity:** hand-compute values for a few states, verify with code; visualize as a heatmap
- **Deliverable:** value heatmap for a fixed policy

## Week 4 — Bellman Optimality and Dynamic Programming
- **Concepts:** optimal value function, policy iteration, value iteration
- **Environment:** same Gridworld
- **Activity:** animate value/policy convergence frame by frame
- **Deliverable:** implementation of policy iteration and value iteration, compared side by side

## Week 5 — Monte Carlo Methods
- **Concepts:** episodic learning, first-visit vs. every-visit MC, sample-based value estimation
- **Environment:** Blackjack (Gymnasium)
- **Activity:** estimate the value function of a fixed blackjack policy from simulated episodes
- **Deliverable:** MC-estimated value function, compared to known optimal strategy

## Week 6 — Temporal-Difference Learning
- **Concepts:** TD(0), bootstrapping, MC vs. TD tradeoffs
- **Environment:** FrozenLake (slippery)
- **Activity:** compare MC and TD value estimates on the same environment
- **Deliverable:** short comparison report/plot: convergence speed and variance

## Week 7 — Model-Free Control: SARSA and Q-learning
- **Concepts:** on-policy vs. off-policy control, SARSA, Q-learning
- **Environment:** CliffWalking
- **Activity:** train both algorithms, visualize learned paths near the cliff
- **Deliverable:** side-by-side policy visualization + discussion of why they differ

<!-- ## Week 8 — Exploration (optional)
- **Concepts:** epsilon-greedy, decaying epsilon, UCB, optimistic initialization
- **Environment:** CliffWalking
- **Activity:** hold the algorithm fixed, vary only exploration strategy
- **Deliverable:** experiment write-up on exploration strategy vs. performance

## Week 9 — Function Approximation (optional)
- **Concepts:** why tables break down, linear function approximation, feature representations (e.g. tile coding)
- **Environment:** MountainCar
- **Activity:** implement linear value-function approximation by hand
- **Deliverable:** working approximated Q-function that solves MountainCar -->

## Week 10 — Deep Q-Learning
- **Concepts:** neural network function approximators, experience replay, target networks
- **Environment:** CartPole (core), LunarLander (stretch)
- **Activity:** implement or adapt a DQN, train on CartPole
- **Deliverable:** trained CartPole agent + training curve

## Week 11 — Policy Gradients
- **Concepts:** direct policy optimization, REINFORCE, variance reduction (baselines)
- **Environment:** CartPole (revisited)
- **Activity:** implement REINFORCE, compare training dynamics to DQN on the same env
- **Deliverable:** trained policy-gradient agent + reflection on DQN vs. policy gradient differences

## Week 12 — Actor-Critic Methods
- **Concepts:** combining value and policy learning, advantage estimation
- **Environment:** LunarLander or Pendulum
- **Activity:** implement a basic actor-critic agent
- **Deliverable:** trained actor-critic agent + comparison to Week 11 results

## Week 13 — Modern Policy Optimization: PPO and Trust Regions
- **Concepts:** trust regions, clipped objectives, why PPO is stable
- **Environment:** LunarLander / BipedalWalker (via Stable-Baselines3)
- **Activity:** use SB3 to train PPO, focus on hyperparameters and interpreting training curves (not from-scratch implementation)
- **Deliverable:** tuned PPO run + short hyperparameter sensitivity report

<!-- ## Week 14 — Imitation Learning, Offline RL, and Dataset Shift (optional)
- **Concepts:** behavior cloning, distributional shift, learning from fixed datasets
- **Environment:** custom toy navigation/driving env with scripted "expert" trajectories
- **Activity:** train a behavior-cloned policy, deliberately induce and observe dataset shift failures
- **Deliverable:** behavior cloning demo + written analysis of a failure mode -->

## Week 15 — Safety, Partial Observability, Evaluation, and Final Projects
- **Concepts:** reward hacking, partial observability, evaluation methodology
- **Environment:** student's choice (any Gymnasium env, or a safety-focused variant of a prior env)
- **Activity:** final project — apply a method from the course, or investigate a safety/robustness question
- **Deliverable:** final project presentation/report

---

## Core Packages
- **Gymnasium** — standardized environments (Blackjack, FrozenLake, CliffWalking, MountainCar, CartPole, LunarLander, BipedalWalker)
- **Custom environments** — Gridworld and bandits, hand-built for full transparency in early units
- **Stable-Baselines3** — for PPO in Week 13
- **Matplotlib** — value heatmaps, training curves, rendered rollouts throughout
