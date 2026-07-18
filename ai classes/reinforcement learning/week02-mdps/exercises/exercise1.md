# Exercise 1 — Define the Gridworld

## Objective

Represent a 5×5 navigation problem as explicit states, actions, walls, and
terminal locations.

## Starter guidance

Open `project.py` and complete the Exercise 1 TODOs.

- Validate that start, goal, pit, and walls are in bounds.
- Ensure those special locations do not overlap.
- Build `states` from every in-bounds position except walls.
- Implement `reset` so a new episode always begins consistently.
- Implement `render` using `A`, `S`, `G`, `P`, `#`, and `.`. Keep rendering
  separate from transition logic.

Try changing one wall and confirm the state count and rendering both change.

## A working submission demonstrates

- the map has exactly the intended occupiable states;
- invalid or overlapping map features are rejected;
- reset restores the start and clears termination;
- the text rendering agrees with the stored map.
