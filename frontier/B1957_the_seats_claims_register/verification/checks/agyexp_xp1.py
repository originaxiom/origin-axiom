"""agy-exp's X-P1 results (its branch at 50ad00d61, lane agy-exp-later): what main computes of them.  Nothing of the seat's is run.
 Q1  C3i's equation (2), as X-P1 restates it: with e_ij the matrix units of End(4), Q = p e12 + r e23 + p e34 + f e41 has
     Q^2 = p r (e13 + e24) + p f (e31 + e42), with no scalar term and no division by f.
 Q2  the norm law it states for H with H^2 = 0: (I + H)^n = I + n H, so |(I + H)^n x|^2 = |x|^2 + 2n Re<x, Hx> + n^2 |Hx|^2; it
     equals |x|^2 + n^2 |Hx|^2 exactly when Re<x, Hx> = 0 (X-P1 gives it on its test state)."""
import sympy as sp
p, r, f, n = sp.symbols("p r f n")
E = lambda i, j: sp.Matrix(4, 4, lambda a, b: 1 if (a, b) == (i - 1, j - 1) else 0)
Q = p * E(1, 2) + r * E(2, 3) + p * E(3, 4) + f * E(4, 1)
target = p * r * (E(1, 3) + E(2, 4)) + p * f * (E(3, 1) + E(4, 2))
print("Q1: Q^2 - [p r (e13 + e24) + p f (e31 + e42)] = 0: %s; Q^2's trace (scalar part) %s" % ((Q * Q - target).expand() == sp.zeros(4), sp.simplify((Q * Q).trace())))
H = sp.Matrix([[0, 1], [0, 0]]); I2 = sp.eye(2)
print("Q2: (I + H)^5 = I + 5H: %s; on x = (0, 1): |(I+H)^n x|^2 = %s; on x = (1, 1): %s (Re<x, Hx> = %s)"
      % ((I2 + H) ** 5 == I2 + 5 * H, sp.expand(((I2 + n * H) * sp.Matrix([0, 1])).norm() ** 2), sp.expand(((I2 + n * H) * sp.Matrix([1, 1])).T * ((I2 + n * H) * sp.Matrix([1, 1])))[0], (sp.Matrix([1, 1]).T * H * sp.Matrix([1, 1]))[0]))
