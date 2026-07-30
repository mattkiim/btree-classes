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
    │   ├── ... (as many exercises as the topic needs)
    │   └── project.py
    ├── solutions/
    │   └── project_solution.py
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

### `exercises/exerciseN.md`
A **progressive build sequence**, not a collection of unrelated problems.
Choose the number of core exercises that creates meaningful implementation
checkpoints; do not force every topic into exactly three. Each exercise should
extend the previous one's code/environment, culminating in `project.py`.
Typically, the sequence should:
- scaffold the core environment or data structure;
- implement the core algorithm against that scaffold;
- when the topic warrants it, extend, compare, visualize, or stress-test the
  implementation in one or more later exercises.

Two exercises may be sufficient for a tightly connected topic, while a topic
with multiple substantial algorithms may need three or more.
- Each `exerciseN.md` should state: objective, starter guidance (not full
  starter code — that belongs in `project.py`), and what a working
  submission demonstrates

### `exercises/project.py`
The **starter code file** students actually work in, corresponding to the
combined result of all core exercises for that week. Contains:
- Class/function scaffolding with `# TODO` markers matching the exercise
  steps, ordered so earlier exercises' TODOs appear before later ones
- Enough structure that students aren't starting from a blank file, but
  not so much that the exercises become fill-in-the-blank trivia
- A `if __name__ == "__main__":` block that runs experiments and produces
  plots, matching the pattern used in `week01-bandits`

### `solutions/project_solution.py`
The **cumulative reference solution** for that week's core exercises. Contains:
- A complete implementation of every TODO in `exercises/project.py`, preserving
  the starter file's public class names, function signatures, and experiment
  structure so the two files are easy to compare
- Brief comments at the important algorithmic steps, without turning every
  line into an explanation
- A runnable `if __name__ == "__main__":` demonstration matching the starter
  project
- No answers to the optional stretch exercise unless the instructor explicitly
  requests stretch solutions

### `solutions/inline_exercises.md`
The **instructor-facing answer key** for every small inline exercise in
`lecture.md`. It should:
- use the same exercise numbers and order as the lecture;
- give the expected answer, calculation, or observation, plus a brief reason;
- distinguish predictions from results that depend on randomness or experiment
  settings;
- stay out of `lecture.md` so the student-facing lecture can be distributed
  without answers.

When a week uses a variable number of exercises, the one solution file still
covers all core exercises in their stated progression. Keep solutions out of
the `exercises/` directory so instructors can distribute starter materials
without accidentally including answers.

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
- Be gradeable/completable independently of the core exercise sequence

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
- Every `solutions/project_solution.py` should run end-to-end as a sanity check
  before materials are considered complete. The corresponding
  `exercises/project.py` must retain its student-facing TODOs.
- Every numbered inline exercise in `lecture.md` should have a matching entry
  in `solutions/inline_exercises.md`.
- Core solution files are instructor-facing. Do not place answers directly in
  `exercises/project.py` or `stretch/exercise.md`.

## Teaching style and pacing

Assume students know Python fundamentals, but do not assume they know the
mathematics or technical language of reinforcement learning.

- **Prefer plain language.** Avoid jargon when an ordinary word communicates
  the idea accurately. When a technical term is necessary, explain the idea in
  familiar language first, introduce the term second, and continue connecting
  the term to that explanation.
- **Distinguish literal and technical meanings.** If a word such as “state,”
  “action,” “value,” “reward,” “policy,” or “environment” has both an everyday
  meaning and a specific meaning in reinforcement learning, say explicitly
  which meaning is being used. Give a concrete example of both meanings when
  that would prevent confusion.
- **Make code map to the explanation.** Present code in the same order as the
  English explanation. Use names and small abstractions that represent the
  concepts students have just learned. A student who reads a sentence and then
  the corresponding code should be able to point to where that idea appears.
- **Choose understandable abstractions.** Introduce classes, functions, and
  data structures because they make the example easier to reason about, not
  merely because they are conventional in professional implementations.
  Explain what each abstraction represents before extending it.
- **Do not use math as a prerequisite.** Build intuition with concrete
  examples, tables, traces, drawings, or repeated observations before using a
  formula. If a formula is useful, define every symbol in plain language and
  connect each part to code or a worked numerical example.
- **Keep a topic backlog.** When a useful idea would overload the current
  lesson, put it in a clearly labeled “Later” or “Topic backlog” note instead
  of teaching it immediately. Briefly say why the idea matters and when the
  course will return to it. Do not let the backlog interrupt the current
  learning goal.
- **Teach one conceptual step at a time.** Do not rush to a complete algorithm
  or formal framework. Let students predict, run, inspect, and explain one
  small behavior before adding the next idea.
- **Use pedagogical examples.** Examples should isolate the concept being
  taught, use small numbers or short traces that can be checked by hand, and
  make the expected observation clear. Add complexity only after the simple
  version is understood.
- **Limit each week's core project.** The project should apply the few ideas
  developed during that week, not preview several later weeks at once. Move
  nonessential extensions to the topic backlog or the optional stretch
  exercise.

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
