# Game AI for High School Students — Syllabus

**Format:** 14 weeks, one unit per week  
**Approach:** Game-first — every concept is introduced by building an agent,
opponent, or world system students can play against and inspect.  
**Prerequisite:** Comfortable with functions, classes, loops, and collections
in Python. No machine-learning background is required.

---

## Week 1 — What Makes a Game Agent Intelligent?
- **Concepts:** agents, observations, actions, goals, game loops, deterministic
  versus stochastic behavior
- **Game:** grid-based collect-and-avoid game
- **Activity:** replace random movement with a rule-based agent
- **Deliverable:** playable game with a baseline agent and behavior log

## Week 2 — Navigation and Graph Search
- **Concepts:** graphs, state spaces, breadth-first search, path reconstruction
- **Game:** maze navigation
- **Activity:** implement BFS and visualize its explored frontier
- **Deliverable:** shortest-path agent with a search visualization

## Week 3 — Heuristic Search with A*
- **Concepts:** path cost, heuristics, admissibility, speed versus optimality
- **Game:** weighted tile map with terrain costs
- **Activity:** compare BFS, Dijkstra's algorithm, and A* on the same maps
- **Deliverable:** comparison using path length and expanded nodes

## Week 4 — Steering and Movement
- **Concepts:** vectors, seek, flee, arrive, separation, combined behaviors
- **Game:** top-down pursuit arena
- **Activity:** create smooth movement for an agent and a small flock
- **Deliverable:** visual demo of at least three steering behaviors

## Week 5 — Finite-State Machines
- **Concepts:** states, transitions, conditions, timers, debugging state changes
- **Game:** guard patrol with chase and search modes
- **Activity:** build and visualize a guard's finite-state machine
- **Deliverable:** guard with patrol, chase, search, and return states

## Week 6 — Behavior Trees
- **Concepts:** selectors, sequences, conditions, actions, reusable behaviors
- **Game:** the Week 5 guard arena
- **Activity:** rebuild and extend the guard with a behavior tree
- **Deliverable:** behavior-tree agent and comparison with the state machine

## Week 7 — Utility-Based AI
- **Concepts:** considerations, scoring, weighted decisions, response curves
- **Game:** survival simulation with hunger, safety, and resources
- **Activity:** design utilities that produce understandable priorities
- **Deliverable:** utility agent with an on-screen decision explanation

## Week 8 — Adversarial Search
- **Concepts:** game trees, minimax, terminal utilities, optimal opponents
- **Game:** Tic-Tac-Toe
- **Activity:** implement minimax and test against random and human players
- **Deliverable:** opponent that cannot lose from the initial position

## Week 9 — Alpha-Beta Pruning
- **Concepts:** pruning, search depth, evaluation functions, move ordering
- **Game:** Connect Four
- **Activity:** add alpha-beta pruning and compare nodes searched
- **Deliverable:** depth-limited opponent with a heuristic evaluator

## Week 10 — Monte Carlo Tree Search
- **Concepts:** selection, expansion, simulation, backpropagation, exploration
- **Game:** Connect Four or a small custom strategy game
- **Activity:** compare MCTS and minimax under equal time limits
- **Deliverable:** MCTS opponent with strength-versus-budget plots

## Week 11 — Procedural Content Generation
- **Concepts:** randomness, seeds, constraints, reachability, content metrics
- **Game:** dungeon or platform-level generator
- **Activity:** generate maps and automatically reject unplayable ones
- **Deliverable:** reproducible generator with validity and variety measures

## Week 12 — Multi-Agent Coordination
- **Concepts:** shared goals, roles, communication, formations, emergence
- **Game:** cooperative resource-collection arena
- **Activity:** coordinate agents through shared blackboard information
- **Deliverable:** team behavior compared with an uncoordinated baseline

## Week 13 — Believable and Fair Game AI
- **Concepts:** imperfect information, reaction time, difficulty adjustment,
  predictability, fairness, player experience
- **Game:** revisit a prior opponent or guard system
- **Activity:** create several fair and enjoyable difficulty levels
- **Deliverable:** playtest report supported by behavior and outcome metrics

## Week 14 — Final Project
- **Concepts:** system design, evaluation, iteration, communication
- **Game:** student's choice
- **Activity:** combine at least two course techniques in a playable prototype
- **Deliverable:** demo, source code, architecture diagram, and evaluation

---

## Core Tools
- **Python** — agent logic and experiments
- **Pygame** — lightweight games and visual debugging
- **NumPy** — vectors, grids, and measurements
- **Matplotlib** — search and evaluation plots

## Structural Notes
- Weeks 2–3, 5–7, and 8–10 form connected arcs in navigation, decision
  systems, and adversarial planning.
- Keep internal decisions visible: show search frontiers, current states,
  utility scores, and selected tree branches.
- This course focuses on designed and search-based intelligence, not agents
  that learn through reinforcement.
