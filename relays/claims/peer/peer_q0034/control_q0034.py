#!/usr/bin/env python3
"""Failing control for Q0034 peer note: replaces Q_J with non-anticommuting unit quaternion (3/5)Q_I + (4/5)Q_J."""
import sys
import sympy as sp
import verify_q0034 as V


def main():
    qi = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    qj_tilted = sp.Rational(3, 5) * qi + sp.Rational(4, 5) * sp.Matrix([[0, 1], [-1, 0]])
    qk = qi * sp.Matrix([[0, 1], [-1, 0]])
    std_basis = (qi, sp.Matrix([[0, 1], [-1, 0]]), qk)

    def ad_mat(g):
        gi = g.inv()
        return sp.Matrix(
            3,
            3,
            lambda r, c: sp.simplify(sp.re(sp.expand((g * std_basis[c] * gi * std_basis[r].H).trace() / 2))),
        )

    bdy = [("a", 1), ("b", 1), ("a", -1), ("b", -1)]
    punc_tilted = V.group_cohomology([], {"a": ad_mat(qi), "b": ad_mat(qj_tilted)}, bdy_word=bdy)
    holds = (punc_tilted["H1_par"] == 0)
    print("CONTROL: non-Q8 tilted pair gives H1_par = %d (expected 0 under Q8 claim); holds=%s"
          % (punc_tilted["H1_par"], holds))
    return 0 if holds else 1


if __name__ == "__main__":
    sys.exit(main())
