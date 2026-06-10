"""B149 -- is B89's posited family the COMPLETE solution variety of the SL(4) defining ideal?

B89 (frontier/B89_sl4_symbolic_M4L) PROVED, exact-symbolic over Q(w) (w = primitive cube root of unity), that on an
explicit 4-parameter family the figure-eight bundle longitude satisfies M^4 = L (degree = rank). But B89's family()
*posits* the parametrization (the rank-drop locus t11 = w*t22 and a specific R-block) and verifies the identity ON it;
the tests only show B73's sampled numerical reps gauge onto it. Nothing there proves the posited family is the COMPLETE
solution variety of the defining ideal for the A-spectrum {1,1,w,w^2}. There could be other components -- same
A-spectrum, not covered -- where M^4 = L is unchecked. In particular B89 gauge-fixes Q = t[0:2,2:4] = I_2 assuming Q
invertible (the dense slice); the det Q = 0 stratum is silently excluded.

This module is the pyenv/pure-sympy core (no Sage): it builds the defining ideal for a GENERIC t, runs the consistency
gate (B89's family lies in V(I)), re-asserts the M^4 = L identity, and provides the MB7 algebra_rank reducibility
filter. The actual ideal decomposition (minimal_associated_primes over Q(w)) lives in decompose.py (sage-python) and is
serialized to decomposition.json; the per-component M^4 = L verdict there is by exact ideal membership (symbolic),
EXHIBITED -- not asserted.

THE DEFINING IDEAL (ground truth, no gauge choice). With A = diag(1,1,w,w^2) (A^3 = I, A^-2 = A), a figure-eight
bundle rep (A,t) satisfies the collapsed monodromy relation t A^-2 t A = A^-1 t A t, equivalent (a_k^3 = 1) to
(a_j - a_i^-1) * S_ij = 0 with S = t A t. This forces S_ij = 0 off the pattern
allowed = {(0,0),(0,1),(1,0),(1,1),(2,3),(3,2)} -- 10 quadratics in the 16 entries of t. (Same construction as B89's
ideal_residuals(), lifted to a generic t.)

Standalone character-variety mathematics; no physics. B89's proof itself is untouched -- this refines its scope.
"""
from __future__ import annotations

import importlib.util
import pathlib

import sympy as sp

w = sp.symbols("w")                                  # omega; reduce mod w^2 + w + 1 = 0
_MIN = sp.Poly(w**2 + w + 1, w)

ALLOWED = frozenset({(0, 0), (0, 1), (1, 0), (1, 1), (2, 3), (3, 2)})


def red(e):
    """Reduce a scalar expression in w modulo w^2 + w + 1."""
    e = sp.expand(e)
    try:
        return sp.rem(sp.Poly(e, w), _MIN).as_expr()
    except sp.PolynomialError:
        return e


def redM(M):
    return M.applyfunc(red)


def A_mat():
    return sp.diag(1, 1, w, w**2)


def generic_t():
    # NOTE: entries named x{i}{j}, NOT t{i}{j} -- B89's family() uses free params named t12,t21,t22, so t-named
    # position symbols would collide on substitution in the consistency gate (a name clash the gate is designed to catch).
    return sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"x{i}{j}"))


def defining_ideal_generators(t=None):
    """The 10 off-pattern entries of S = t A t (A^-2 = A). Generators of the defining ideal I over Q(w)."""
    if t is None:
        t = generic_t()
    A = A_mat()
    S = redM(t * A * t)
    gens = [red(sp.expand(S[i, j])) for i in range(4) for j in range(4) if (i, j) not in ALLOWED]
    return gens, t


def _load_b89():
    root = pathlib.Path(__file__).resolve().parents[2]
    path = root / "frontier" / "B89_sl4_symbolic_M4L" / "probe.py"
    spec = importlib.util.spec_from_file_location("b89probe", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def b89_family_lies_in_variety():
    """CONSISTENCY GATE: every generic-ideal generator vanishes when t is B89's posited family -> the lifted ideal is
    the same object B89 proved on. (Any decomposition must recover B89's family as a sub-locus of a component.)"""
    b89 = _load_b89()
    A, _A2, tfam, _params = b89.family()
    gens, t = defining_ideal_generators()
    subs = {t[i, j]: tfam[i, j] for i in range(4) for j in range(4)}
    for g in gens:
        v = red(sp.expand(sp.numer(sp.together(g.subs(subs)))))
        if sp.expand(v) != 0:
            return False
    return True


def m4_equals_l_on_b89_family():
    """Re-assert B89's exact M^4 = L identity on its family (holds, det t)."""
    b89 = _load_b89()
    return b89.m4_equals_l_identity()


def q_zero_forces_reducible():
    """EXHIBITED reducibility: on the Q = t[0:2,2:4] = 0 stratum, A and t are block-lower-triangular, so span(e2,e3)
    is invariant under A, t, t^-1, and hence B = A^-2 t A t^-1 -- the rep <A,B> is REDUCIBLE. We exhibit it by showing
    the top-right 2x2 block (rows 0,1 x cols 2,3) of A, t, and B*det all vanish for a generic Q=0 monodromy.
    (So every component of the rankQ0 stratum is reducible -- MB7-filtered, not a genuine figure-eight bundle rep;
    the M^4=L 'violations' the decomposition flags there are on this reducible locus.)"""
    A = A_mat()
    A2 = sp.diag(1, 1, w**2, w)
    # generic block-lower-triangular t (Q = 0): top-right 2x2 block is zero
    syms = sp.symbols("a b c d  e f g h  p q r s")
    P = sp.Matrix([[syms[0], syms[1]], [syms[2], syms[3]]])
    R = sp.Matrix([[syms[4], syms[5]], [syms[6], syms[7]]])
    T = sp.Matrix([[syms[8], syms[9]], [syms[10], syms[11]]])
    t = sp.Matrix(sp.BlockMatrix([[P, sp.zeros(2, 2)], [R, T]]))
    u = t.adjugate()                                   # t^-1 = u/det ; B*det = A^-2 t A u
    Bdet = redM(A2 * t * A * u)
    topright = lambda M: [M[i, j] for i in (0, 1) for j in (2, 3)]
    return (all(v == 0 for v in topright(A))
            and all(v == 0 for v in topright(t))
            and all(sp.expand(red(v)) == 0 for v in topright(Bdet)))


def algebra_rank(A, B, tol=1e-9):
    """MB7 reducible-locus filter (numeric): dim of the associative algebra generated by {I,A,B} (Burnside: the rep is
    irreducible iff this equals n^2 = 16). Used in decompose.py to separate reducible loci from genuine bundle reps."""
    import numpy as np

    n = A.shape[0]
    words = [np.eye(n, dtype=complex), np.asarray(A, dtype=complex), np.asarray(B, dtype=complex)]
    frontier = [words[1], words[2]]
    for _ in range(n * n + 2):
        mat = np.array([m.flatten() for m in words])
        if np.linalg.matrix_rank(mat, tol=tol) == n * n:
            return n * n
        new = [G @ M for M in frontier for G in (words[1], words[2])]
        words += new
        frontier = new
    mat = np.array([m.flatten() for m in words])
    return int(np.linalg.matrix_rank(mat, tol=tol))


def main():
    print("B149 -- completeness of the SL(4) {1,1,w,w^2} defining ideal (is B89's family the whole variety?)\n")
    gens, _ = defining_ideal_generators()
    print(f"  defining ideal I: {len(gens)} quadratic generators in 16 entries of t (over Q(w))")
    gate = b89_family_lies_in_variety()
    print(f"  consistency gate -- B89's posited family lies in V(I):  {gate}")
    holds, det = m4_equals_l_on_b89_family()
    print(f"  B89 identity re-check  [A,B] = -(1/det t) mu^4 on the family:  {holds}   (det t = {det})")
    print(f"  Q=0 forces reducible (EXHIBITED: span(e2,e3) invariant under A,t,B):  {q_zero_forces_reducible()}")
    print("\n  OUTCOME (a), from the stratified decomposition (decompose.py) + exact-over-F_p Burnside classification")
    print("  (classify_fp.py): the ONLY stratum carrying IRREDUCIBLE reps is rank-Q=2 = B89's family, where M^4=L holds")
    print("  (exact ideal membership). Every M^4=L violation in V(I) is on a REDUCIBLE (MB7) or VACUOUS (det t=0) locus.")
    print("  => B89's family is the COMPLETE component of irreducible bundle reps; M^4=L is unconditional on it.")
    print("  See decomposition.json (symbolic component structure) + irreducibility_fp.json (exact F_p classification).")
    return 0 if (gate and holds) else 1


if __name__ == "__main__":
    raise SystemExit(main())
