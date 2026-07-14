"""Shared E6 root-system / Weyl-orbit BFS and grading utilities.

Factored out of test_b572_eleven_clauses.py, test_b573_global_bridge.py, and
test_b574_offprincipal.py (L69, hygiene batch): all three files independently
re-implemented (a) the E6 Cartan matrix, (b) the simple-reflection BFS that
walks out the 27-weight orbit of the fundamental rep from the highest weight
(column 0 of the inverse Cartan matrix), and — in test_b574 — (c) the same
BFS pattern generating the 72-root system from the 6 simple roots, plus small
Cartan-form grading/Counter idioms built on top of an orbit. This module is
the single source of truth for all of that; the three test files import from
it instead of copy-pasting the BFS.

No behavior change: every routine below reproduces the original inline
computation verbatim (same reflection formula, same seeds, same dedup-by-
coordinate-tuple BFS), just parameterized so it can be shared.
"""
from collections import Counter

import sympy as sp

# The E6 Cartan matrix, Bourbaki node order 1..6 (node 4 is the trivalent node).
C6 = sp.Matrix([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
                [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]])

RANK = 6


def simple_reflect(v, j, C=C6, n=RANK):
    """Reflect the column vector v in the j-th simple root: only coordinate j
    changes, v[j] -> v[j] - sum_i C[i, j] * v[i]. The formula used inline in
    all three original files.
    """
    pj = sum(C[i, j] * v[i] for i in range(n))
    u = sp.Matrix(v)
    u[j] = v[j] - pj
    return u


def weyl_orbit(seeds, C=C6, n=RANK):
    """BFS the Weyl-group orbit of one seed vector, or a list of seed
    vectors, under the n simple reflections encoded by the Cartan matrix C.
    Returns the orbit as a list of sympy column Matrices, de-duplicated by
    coordinate tuple (same "seen" dedup the original inline loops used).
    """
    if isinstance(seeds, sp.MatrixBase):
        seeds = [seeds]
    seen = {tuple(v): sp.Matrix(v) for v in seeds}
    frontier = list(seeds)
    while frontier:
        new = []
        for v in frontier:
            for j in range(n):
                u = simple_reflect(v, j, C, n)
                tu = tuple(u)
                if tu not in seen:
                    seen[tu] = u
                    new.append(u)
        frontier = new
    return list(seen.values())


def fundamental_coweight_orbit(node=0, C=C6, n=RANK):
    """The Weyl orbit of the node-th fundamental coweight (column `node` of
    C^-1). At node 0 for E6 this is the 27-dimensional minuscule orbit of the
    fundamental (27) representation, in weight coordinates.
    """
    return weyl_orbit(C.inv()[:, node], C=C, n=n)


def root_system(C=C6, n=RANK):
    """BFS the full root system from the n simple roots (unit vectors) — 72
    roots for E6.
    """
    simple_roots = [sp.Matrix([1 if i == j else 0 for i in range(n)]) for j in range(n)]
    return weyl_orbit(simple_roots, C=C, n=n)


def weyl_vector(C=C6, n=RANK):
    """rho, the sum of the fundamental coweights (sum of the columns of C^-1)."""
    Ginv = C.inv()
    return sum([Ginv[:, j] for j in range(n)], sp.zeros(n, 1))


def cartan_ip(x, y, C=C6):
    """The C-twisted bilinear form x^T C y, as a scalar sympy expression."""
    return (sp.Matrix(x).T * C * sp.Matrix(y))[0, 0]


def highest_root(roots):
    """The highest root: the maximal coordinate-sum root among the positive
    roots (all coordinates >= 0). Unique for an irreducible root system.
    """
    pos = [r for r in roots if all(c >= 0 for c in r)]
    return max(pos, key=lambda r: sum(r))


def height_grading(vectors, ref, C=C6):
    """Counter of the rational C-height sp.Rational(cartan_ip(v, ref, C)) over
    v in vectors — e.g. the principal height w.r.t. rho.
    """
    return Counter(sp.Rational(cartan_ip(v, ref, C)) for v in vectors)


def sl2_grading(vectors, theta, C=C6):
    """Counter of the integer sl2(theta)-weight int(2*<v,theta>/<theta,theta>)
    over v in vectors — the grading under the sl2-triple built on theta.
    """
    denom = cartan_ip(theta, theta, C)
    return Counter(int(2 * cartan_ip(v, theta, C) / denom) for v in vectors)


def coordinate_charge(vectors, index=0):
    """Counter of the raw index-th coordinate of each vector (e.g. a U(1)
    coweight charge read directly off weight coordinates, no Cartan form).
    """
    return Counter(sp.Rational(sp.Matrix(v)[index]) for v in vectors)
