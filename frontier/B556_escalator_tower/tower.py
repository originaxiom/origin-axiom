#!/usr/bin/env python3
"""B556 — the escalator tower T(M) = [[M,M],[M^2,M]].

VERIFIED FACTS (see tests/test_b556.py):
  - T(F) = M4 verbatim (F = golden Fibonacci matrix); = B517's intertwining
    coupling [[F,C],[D,F]] with (C,D) = (F, F^2).
  - iterating T doubles the field degree 2 -> 4 -> 8 -> 16 -> 32, every
    charpoly irreducible; Perron follows lambda_{n+1} = lambda_n(1+sqrt lambda_n).
The TOWER READING (physics ladder, self-similar continuation) is a HYPOTHESIS;
rungs >= 2 use a canonical-but-CHOSEN iteration rule. Lit-gate before novelty.
"""
import numpy as np, sympy as sp
x = sp.Symbol('x')
def T(M): return sp.Matrix(sp.BlockMatrix([[M, M], [M*M, M]]))
F = sp.Matrix([[1, 1], [1, 0]])

if __name__ == '__main__':
    M = F
    print(f"{'rung':>4} {'size':>6} {'deg':>4} {'irred':>6} {'Perron':>14}")
    for n in range(5):
        cp = M.charpoly(x).as_expr()
        deg = sp.Poly(cp, x).degree()
        irr = (len(sp.factor_list(cp)[1]) == 1 and sp.factor_list(cp)[1][0][1] == 1)
        pf = max(abs(e) for e in np.linalg.eigvals(np.array(M.tolist(), float)))
        print(f"{n:>4} {M.shape[0]:>6} {deg:>4} {str(irr):>6} {pf:>14.9f}")
        if n < 4:
            M = T(M)
    print("\nlambda-law lambda_{n+1} = lambda_n(1+sqrt lambda_n):")
    lam = (1+np.sqrt(5))/2
    for n in range(5):
        print(f"  lambda_{n} = {lam:.9f}")
        lam = lam*(1+np.sqrt(lam))
