"""
REVIEW 80, the web seat: a post hoc check, written after the sealed run of retraction_rows_math.py (0fc1197a5).
That run printed the difference cos(2 pi/7) - (1 - 2 sin(pi/7)^2) unreduced, as -cos(2*pi/7) + sin(3*pi/14), where its
header expected it to hold exactly.  This file asks sympy whether that difference is zero, by `equals` and by expanding
both trigonometric functions in terms of exp(i pi/14).  It is post hoc: the expectation (zero) is the sealed one.

Usage: retraction_rows_math_posthoc_1.py
"""
import sympy as sp

d = sp.cos(2 * sp.pi / 7) - (1 - 2 * sp.sin(sp.pi / 7) ** 2)
print('P1  the difference, as sympy prints it: %s' % sp.simplify(d))
print('P1  equals(0): %s' % d.equals(0))
print('P1  rewritten in exp and expanded: %s' % sp.simplify(sp.expand(d.rewrite(sp.exp))))
print('P1  sin(3 pi/14) - cos(2 pi/7), equals(0): %s' % (sp.sin(3 * sp.pi / 14) - sp.cos(2 * sp.pi / 7)).equals(0))
