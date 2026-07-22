# Deep Reinforcement Learning for High School Students — Syllabus

**Format:** 14 weeks, one unit per week  
**Approach:** Environment-first — students train agents, visualize behavior,
and explain results through controlled experiments.  
**Prerequisites:** Reinforcement Learning through model-free control and Deep
Learning through PyTorch optimization. Students should understand Q-learning,
neural networks, and backpropagation.

---

## Week 1 — From Tables to Neural Networks
- **Concepts:** limits of Q-tables, function approximation, generalization
- **Environment:** CartPole
- **Activity:** compare a discretized Q-table with a small Q-network
- **Deliverable:** baselines and an explanation of why approximation helps

## Week 2 — Deep Q-Networks
- **Concepts:** Q-networks, TD targets, epsilon-greedy exploration, minibatches
- **Environment:** CartPole
- **Activity:** implement the core DQN training loop in PyTorch
- **Deliverable:** trained agent with reward and loss curves

## Week 3 — Stabilizing DQN
- **Concepts:** replay buffers, target networks, correlated data, moving targets
- **Environment:** CartPole
- **Activity:** remove one stabilizing component at a time
- **Deliverable:** ablation of replay and target-network configurations

## Week 4 — Better Value-Based Agents
- **Concepts:** Double DQN, dueling networks, prioritized replay, overestimation
- **Environment:** LunarLander or Acrobot
- **Activity:** add one DQN improvement and compare with the baseline
- **Deliverable:** controlled learning-curve experiment across seeds

## Week 5 — Visual Observations
- **Concepts:** preprocessing, CNN encoders, frame stacking, motion information
- **Environment:** a small pixel-based game
- **Activity:** train from images and inspect the input pipeline
- **Deliverable:** policy demo and sample processed observations

## Week 6 — Policy Gradients
- **Concepts:** stochastic policies, log probabilities, returns, REINFORCE
- **Environment:** CartPole
- **Activity:** implement REINFORCE and compare its behavior with DQN
- **Deliverable:** trained policy and variance analysis across seeds

## Week 7 — Baselines and Advantage
- **Concepts:** variance reduction, value baselines, advantage, entropy bonuses
- **Environment:** CartPole or LunarLander
- **Activity:** add a learned baseline and measure stability
- **Deliverable:** REINFORCE-with-baseline experiment

## Week 8 — Actor-Critic Methods
- **Concepts:** actor and critic roles, bootstrapping, shared encoders
- **Environment:** LunarLander
- **Activity:** implement a synchronous actor-critic agent
- **Deliverable:** policy and value-learning diagnostics

## Week 9 — Continuous Control
- **Concepts:** continuous actions, Gaussian policies, bounds, exploration scale
- **Environment:** Pendulum
- **Activity:** output and train a continuous action distribution
- **Deliverable:** rollout and action-distribution plots

## Week 10 — Proximal Policy Optimization
- **Concepts:** policy ratios, clipped objectives, update epochs, trust regions
- **Environment:** LunarLander or Pendulum
- **Activity:** implement compact PPO and verify against a library version
- **Deliverable:** learning curves and implementation comparison

## Week 11 — Tuning and Diagnosing PPO
- **Concepts:** rollout length, clipping, entropy, value loss, reproducibility
- **Environment:** reuse Week 10
- **Activity:** run a small controlled hyperparameter study
- **Deliverable:** evidence-based tuning recommendation

## Week 12 — Self-Play and Multi-Agent Learning
- **Concepts:** non-stationary opponents, self-play, opponent pools
- **Environment:** a simple two-player competitive game
- **Activity:** train against current and historical agent versions
- **Deliverable:** tournament matrix across checkpoints

## Week 13 — Reliable and Responsible Deep RL
- **Concepts:** reward hacking, distribution shift, evaluation, seed sensitivity,
  compute cost, reporting failures
- **Environment:** a task with an exploitable reward
- **Activity:** discover a shortcut and redesign the reward or evaluation
- **Deliverable:** failure analysis and revised evaluation protocol

## Week 14 — Final Project
- **Concepts:** baselines, experiment design, ablations, uncertainty
- **Environment:** student's choice
- **Activity:** apply and evaluate a deep-RL method on a new task
- **Deliverable:** reproducible code, trained policy, demo, and report

---

## Core Tools
- **PyTorch** — neural networks and optimization
- **Gymnasium** — training and evaluation environments
- **Stable-Baselines3** — reference implementations
- **NumPy and Matplotlib** — analysis and visualization
- **Google Colab or a GPU environment** — recommended for pixel observations

## Experimental Standards
- Compare against a baseline and change one major factor at a time.
- Separate training returns from evaluation returns.
- Report multiple seeds, variability, and failures.
- Save configurations and checkpoints needed to reproduce results.
- Inspect agent behavior through rollouts, not only reward numbers.

## Structural Notes
- Weeks 2–5 form the value-based arc; Weeks 6–11 form the policy-optimization
  arc; Week 12 introduces multi-agent learning.
- Begin with small environments so students can debug before spending
  significant compute.
- This course assumes prior tabular RL and neural-network knowledge instead of
  reteaching either foundation.
