# Week 4 Inline Exercise Solutions

## Exercise 1 — Greedy one-step lookahead

LEFT has value $-1+0.9(5)=3.5$ and RIGHT has value
$-1+0.9(7)=5.3$, so RIGHT is greedy.

If RIGHT instead enters a terminal state and pays `+4`, its value is exactly 4:
there is no discounted future value after termination. It still beats LEFT's
3.5, so the choice remains RIGHT.

## Exercise 2 — Tied shortest routes

At `(4, 1)`, both `UP` and `LEFT` begin a shortest safe route. The two routes
rejoin at `(3, 0)` after `UP, LEFT` or `LEFT, UP`, respectively.

Implementations choosing different tied actions are both correct. Their arrows
can differ while their action values and returns are equal.

## Exercise 3 — Improving an all-UP policy

The clearest first change is next to the goal: at `(3, 4)`, `DOWN` receives
`+10` immediately and is better than continuing to move up. States near the pit
also have direct evidence for avoiding it. Because policy evaluation is run to
convergence before improvement, the subsequent greedy pass considers every
state; “first” describes where useful terminal information originates, not an
order in which the improvement loop is required to visit states.

## Exercise 4 — Aliased history entries

Every element of `history` refers to the same mutable dictionary. Later updates
change the object seen through all earlier entries, so plotting old frames
shows identical copies of the final values instead of convergence over time.
`values.copy()` creates an independent snapshot for each sweep.
