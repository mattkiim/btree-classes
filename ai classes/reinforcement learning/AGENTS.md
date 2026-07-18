# AGENTS.md — RL Course Materials

This repo contains lecture and exercise materials for a high-school
Reinforcement Learning course, organized environment-first: every topic is
taught through a Python environment students can run, modify, and extend.

This file tells an AI agent (Claude Code or similar) how to generate,
extend, or edit materials in this repo so that all topics stay consistent
in structure, tone, and difficulty progression.

---

## Repo layout

```
/
├── AGENTS.md
├── syllabus.md
└── weekNN-topic-slug/
    ├── lecture.md
    ├── exercises/
    │   ├── exercise1.md
    │   ├── exercise2.md
    │   ├── exercise3.md
    │   └── project.py
    └── stretch/
        └── exercise.md
```

Each topic (one per week in the syllabus) gets its own top-level directory,
named `weekNN-topic-slug` (zero-padded week number + short kebab-case
topic name), e.g. `week01-bandits`, `week07-sarsa-qlearning`,
`week13-ppo`.

---

## File-by-file spec

### `lecture.md`
The full class content for that topic — equivalent in scope to the Week 1
bandits lesson plan already in this repo. Should include:
- Learning objectives
- A hook / discussion opener that doesn't require code
- Concept explanations, building vocabulary incrementally
- Live-coding walkthrough(s) with complete, runnable code blocks
- **Small inline sub-exercises** embedded directly in the lecture
  (1–2 line prompts like "modify X and predict what happens" or
  "try running this with k=20 — what changes?") — these are for
  in-class pacing, not graded work, and don't need their own files
- Discussion prompts for wrap-up
- A short preview of the next topic
- A "common misconceptions to watch for" section for the instructor

### `exercises/exercise1.md`, `exercise2.md`, `exercise3.md`
A **progressive build sequence** — not three unrelated problems. Each
exercise should extend the previous one's code/environment, culminating in
`project.py`. Concretely:
- `exercise1.md` — scaffold the core environment or data structure for
  the topic (e.g., "implement the bandit environment class")
- `exercise2.md` — implement the core algorithm against that scaffold
  (e.g., "implement epsilon-greedy agent, run it, plot results")
- `exercise3.md` — extend or stress-test it (e.g., "compare 3 exploration
  strategies," "test non-stationary rewards," "add a second algorithm to
  compare against")
- Each `exerciseN.md` should state: objective, starter guidance (not full
  starter code — that belongs in `project.py`), and what a working
  submission demonstrates

### `exercises/project.py`
The **starter code file** students actually work in, corresponding to the
combined result of exercises 1–3. Contains:
- Class/function scaffolding with `# TODO` markers matching the exercise
  steps (so `exercise1.md`'s TODOs live at the top, `exercise3.md`'s near
  the bottom)
- Enough structure that students aren't starting from a blank file, but
  not so much that the exercises become fill-in-the-blank trivia
- A `if __name__ == "__main__":` block that runs experiments and produces
  plots, matching the pattern used in `week01-bandits`

### `stretch/exercise.md`
One **optional, harder, self-contained** exercise — not required to
complete the core project, aimed at students who finish early or want a
challenge. Should:
- Not require its own starter file unless the task is substantial enough
  to need one (if so, add `stretch/starter.py` following the same
  convention as `project.py`)
- Often previews a concept from a *later* week (e.g., Week 1's stretch
  exercise on decaying epsilon previews adaptive exploration; Week 7's
  stretch exercise might preview function approximation)
- Be gradeable/completable independently of exercises 1–3

---

## Generation guidelines

- **Match the Week 1 materials as the reference implementation** for tone,
  depth, and formatting (`week01-bandits/lecture.md` and its exercises,
  once scaffolded into this structure, are canonical examples).
- **Anchor environments** (see `syllabus.md`) should be reused across
  topics wherever the syllabus calls for it — don't introduce a new
  environment when an anchor env already fits.
- Keep exercises **environment-first**: students should always be running
  and observing an environment, not just filling in isolated functions.
- Math should scale with the syllabus — early topics (bandits, MDPs,
  Bellman equations) can include light formalism in `lecture.md`; later
  topics (DQN, PPO) should lean on runnable code and empirical
  observation over derivation, unless the instructor specifically
  requests a math-heavy version (as with the bandit regret-bound
  discussion already produced for Week 1).
- Every `project.py` should run end-to-end with **all TODOs
  implemented** as a sanity check before being committed — i.e. generate
  and privately verify a solved version, then strip it back down to the
  TODO'd starter version for the actual file in this repo.
- Do not include solved/answer versions of `project.py` in this repo
  unless a topic directory explicitly has a `solutions/` subfolder
  requested by the instructor — keep the repo student-facing by default.

---

## Topic list (week → directory slug)

| Week | Topic | Directory |
|---|---|---|
| 1 | What is RL? (Multi-armed bandits) | `week01-bandits` |
| 2 | Markov Decision Processes | `week02-mdps` |
| 3 | Value functions and Bellman equations | `week03-value-functions` |
| 4 | Bellman optimality and dynamic programming | `week04-dynamic-programming` |
| 5 | Monte Carlo methods | `week05-monte-carlo` |
| 6 | Temporal-difference learning | `week06-td-learning` |
| 7 | Model-free control: SARSA and Q-learning | `week07-sarsa-qlearning` |
| 8 | Exploration | `week08-exploration` |
| 9 | Function approximation | `week09-function-approximation` |
| 10 | Deep Q-learning | `week10-dqn` |
| 11 | Policy gradients | `week11-policy-gradients` |
| 12 | Actor-critic methods | `week12-actor-critic` |
| 13 | Modern policy optimization: PPO and trust regions | `week13-ppo` |
| 14 | Imitation learning, offline RL, dataset shift | `week14-imitation-offline-rl` |
| 15 | Safety, partial observability, evaluation, final projects | `week15-safety-final-projects` |

---

## Setup / running materials

```bash
pip install numpy matplotlib gymnasium stable-baselines3
```

Each `project.py` should be runnable standalone:

```bash
python weekNN-topic-slug/exercises/project.py
```

## Do Not
- Don't rename or restructure `weekNN-topic-slug` directories once created
  — the syllabus and any student-facing links depend on stable paths.
- Don't put full worked solutions directly in `exercises/project.py` or
  `stretch/exercise.md` — those files are student-facing starter code.
- Don't introduce new third-party dependencies beyond `numpy`,
  `matplotlib`, `gymnasium`, and `stable-baselines3` without flagging it,
  since not all students may have easy install access mid-class.