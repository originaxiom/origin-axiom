"""B337 -- structure (XOR) ordering: the deepest form of the ratio-vs-magnitude wall (Chat-2, probed).

Chat-2: the hierarchy arc only tested the SYMMETRIC configuration (three generations = one seed cycled
by the commensurator Z/3). The untested configuration is MULTIPLICITY -- three DISTINCT metallic seeds
(m=1,2,3). We probed it. The result is a structural theorem, not a value:

  STRUCTURE (XOR) ORDERING. A single symmetric object (Z/3-related copies, shared arithmetic Q(sqrt-3))
  gives E6 + a DEMOCRATIC (degenerate) spectrum -- structure, no ordering. Distinct seeds (different
  trace fields) give an ORDERED spectrum but NO shared E6 -- ordering, no structure. The SAME condition
  (the shared arithmetic = the Z/3 symmetry) that forces the structure is what forbids the ordering.
  No single STATIC configuration has both.

VERIFIED:
  single object  (B324 omega-circulant): |eig|^2 = {52,1,1} -> DEGENERATE (one heavy, two equal light).
  multiplicity   (overlap tr(A_i A_j^-1), seeds 1,2,3) = [[2,3,6],[3,2,3],[6,3,2]]: eigenvalues
                 {10.2,-4,-0.2}, ratios 1:0.39:0.019 -> ORDERED (three distinct).

The two hard questions (both bite honestly):
  (a) Is {1,2,3} forced? NO. B125 arithmeticity selects {1,2} (a two-element selector), NOT {1,2,3};
      m=3 is non-arithmetic. The three-seed ansatz relocates the arbitrariness (which seeds?), it does
      not remove it.
  (b) Does structure survive? NO. The seeds have distinct hyperbolic trace fields (m=1 Q(sqrt-3)->E6,
      m=2 Q(i), m=3 deg>=4, B125) -> no single shared E6 -> the gauge group / sin^2=3/8 / cascade,
      which came from m=1's Z/3 symmetry, are LOST.

CAVEAT (B325): both overlaps are tr(A_i A_j^-1), NOT the physical E6-cubic mass matrix; the
structure-vs-ordering TENSION is the robust content, independent of the overlap-vs-mass caveat.
Firewalled; the escape (a FLOW connecting symmetric-UV to ordered-IR) is Attack C. Nothing to CLAIMS.
"""
import sympy as sp

W = sp.exp(2 * sp.I * sp.pi / 3)
_g = sp.Matrix([[0, -1], [1, -1]])
_a0 = sp.Matrix([[1, 1], [0, 1]])
_b0 = sp.Matrix([[1, 0], [W, 1]])


def A(m):
    """metallic monodromy R^m L^m = [[1+m^2, m],[m,1]], trace m^2+2, monodromy disc m^2(m^2+4)."""
    return sp.Matrix([[1 + m * m, m], [m, 1]])


def single_object_spectrum():
    """B324: three Z/3-conjugate generations; overlap magnitudes are degenerate {52,1,1}."""
    a = [sp.simplify(_g**i * _a0 * _g**(-i)) for i in range(3)]
    b = [sp.simplify(_g**i * _b0 * _g**(-i)) for i in range(3)]
    M = sp.Matrix(3, 3, lambda i, j: sp.trace(a[i] * b[j].inv()))
    mags2 = sorted([round(abs(complex(e))**2) for e in M.eigenvals()], reverse=True)
    return mags2                                   # [52, 1, 1] -> degenerate


def multiplicity_overlap(seeds=(1, 2, 3)):
    return sp.Matrix(3, 3, lambda i, j: (A(seeds[i]) * A(seeds[j]).inv()).trace())


def multiplicity_spectrum(seeds=(1, 2, 3)):
    M = multiplicity_overlap(seeds)
    ev = sorted([float(e) for e in M.eigenvals()], key=lambda x: -abs(x))
    return ev                                       # [10.2, -4, -0.2] -> ordered


def is_ordered(ev, tol=1e-3):
    mags = sorted([abs(e) for e in ev], reverse=True)
    return mags[0] - mags[1] > tol and mags[1] - mags[2] > tol


def metallic_disc(m):
    return m * m * (m * m + 4)                       # 5, 32, 117 for m=1,2,3


def seeds_not_forced():
    """B125: arithmeticity selects {1,2}, not {1,2,3}; m=3 non-arithmetic."""
    arithmetic = {1: True, 2: True, 3: False}
    return set(m for m, ok in arithmetic.items() if ok) == {1, 2}   # != {1,2,3}


def distinct_hyperbolic_fields():
    """B125 invariant trace fields: Q(sqrt-3), Q(i), deg>=4 -> distinct -> no shared E6."""
    return ["Q(sqrt-3)", "Q(i)", "deg>=4"]          # all distinct


if __name__ == "__main__":
    print("single object |eig|^2 :", single_object_spectrum(), "-> democratic (degenerate)")
    ev = multiplicity_spectrum()
    print("multiplicity eig      :", [round(e, 2) for e in ev], " ordered:", is_ordered(ev))
    print("metallic discs        :", [metallic_disc(m) for m in (1, 2, 3)], "(distinct, != -15)")
    print("{1,2,3} forced?       :", not seeds_not_forced(), "(arithmeticity selects {1,2})")
    print("shared E6?            :", len(set(distinct_hyperbolic_fields())) == 1,
          "(distinct fields", distinct_hyperbolic_fields(), "-> structure LOST)")
    print("=> STRUCTURE (XOR) ORDERING: no single static configuration has both.")
