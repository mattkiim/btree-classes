# Stretch — When does policy evaluation converge?

The Bellman expectation update usually converges quickly in this small world,
but its speed depends on the discount factor and update style.

Add an option for **in-place** updates (new values are used immediately during
the same sweep) and **two-array** updates (an entire sweep reads only the old
values). For each style, record the largest value change after every sweep for
`gamma=0.5`, `0.9`, and `0.99`. Plot change versus sweep number on a logarithmic
y-axis.

Your submission is complete when both methods converge to nearly the same final
values, the plot contains all six labeled curves, and a short paragraph
explains how gamma and update order affect convergence. Also test `gamma=1.0`:
report what happens and explain why episodic termination matters. This previews
the convergence questions behind dynamic programming.
