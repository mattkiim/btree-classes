# AI Courses for High School Students

Project-first courses that teach AI through experiments students can run,
modify, and explain.

## Learning paths

```mermaid
flowchart LR
    ML[Machine Learning] --> DL[Deep Learning] --> DRL[Deep Reinforcement Learning]
    RL[Reinforcement Learning] --> DRL
    GAI[Game AI]
```

- [Machine Learning](ai%20classes/machine%20learning/syllabus.md) covers data,
  evaluation, gradient descent, classical models, and neural-network basics.
- [Deep Learning](ai%20classes/deep%20learning/syllabus.md) builds on ML with
  PyTorch, CNNs, transformers, and generative models.
- [Reinforcement Learning](ai%20classes/reinforcement%20learning/syllabus.md) is
  a separate path covering agents, environments, value functions, and control.
- [Deep Reinforcement Learning](ai%20classes/deep%20reinforcement%20learning/syllabus.md)
  combines the Deep Learning and Reinforcement Learning paths.
- [Game AI](ai%20classes/game%20ai/syllabus.md) is a separate course covering
  navigation, behavior systems, adversarial search, and procedural generation.

## How to use a weekly unit

For implemented units such as `week01-bandits`, use the materials in this
order:

1. Follow `lecture.md` for concepts and guided code examples.
2. Read each `exercises/exerciseN.md` in numerical order.
3. Complete the corresponding `TODO` markers in `exercises/project.py`.
4. Run the project and interpret its output or plots.
5. Check your work against `solutions/` after attempting the exercises.
6. Try `stretch/exercise.md` for an optional challenge.

The lecture should be understandable on its own. `project.py` is the cumulative
student workspace for applying the lecture, not required advance reading.
