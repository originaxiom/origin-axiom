"""B1957, check 4: agy-002's gates 0 and 1 (its endgame branch), on main's own code.  No data; none of its code is run.
G0: the one-loop slopes; the Pati-Salam slopes from the field content; the matching weights (3/5, 2/5); its benchmark B0.2
    (in sm_rge.py).  G1: Riley's generators and the cusp; the maximal cusp; the 27 of E6; the corridor's slope; why the
    determinant's phase does not run at one and two loops; the scale obstruction as a scaling statement."""
import itertools, pathlib, sys
from fractions import Fraction as Fr
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def slopes_sm(ng=3, nh=1):
    b1 = Fr(4, 3) * ng + Fr(1, 10) * nh; b2 = -Fr(22, 3) + Fr(4, 3) * ng + Fr(1, 6) * nh; b3 = -11 + Fr(4, 3) * ng
    return b1, b2, b3


def slopes_ps(ng=3, bidoublets_complex=1, h421=1, h412=1):
    """SU(4) x SU(2)_L x SU(2)_R: b = -(11/3) C2(G) + (2/3) sum over Weyl fermions T(R) + (1/3) sum over complex scalars T(R)"""
    T4 = Fr(1, 2); T2 = Fr(1, 2)
    f4 = ng * (2 * T4 + 2 * T4); f2l = ng * (4 * T2); f2r = ng * (4 * T2)            # (4,2,1) + (4bar,1,2) per generation
    s4 = h421 * 2 * T4 + h412 * 2 * T4; s2l = bidoublets_complex * 2 * T2 + h421 * 4 * T2; s2r = bidoublets_complex * 2 * T2 + h412 * 4 * T2
    return (-Fr(11, 3) * 4 + Fr(2, 3) * f4 + Fr(1, 3) * s4, -Fr(11, 3) * 2 + Fr(2, 3) * f2l + Fr(1, 3) * s2l, -Fr(11, 3) * 2 + Fr(2, 3) * f2r + Fr(1, 3) * s2r)


def matching_weights():
    """Y = T3R + (B - L)/2 on one generation's 16, GUT-normalised: 1/g1^2 = w2/g2R^2 + w4/g4^2"""
    states = []                                                                  # (T3R, B-L) of the right-handed and left-handed fields
    for bl, n in ((Fr(1, 3), 3), (-1, 1)):
        for _ in range(n):
            states += [(0, bl), (0, bl), (Fr(1, 2), bl), (-Fr(1, 2), bl)]         # the doublet (T3R = 0, twice) and the two right-handed states
    trY2 = sum((t + b / 2) ** 2 for t, b in states); trT2 = sum(t * t for t, b in states); trB2 = sum((b / 2) ** 2 for t, b in states)
    return trT2 / trY2, trB2 / trY2, trY2


def riley():
    w = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2                                # zeta_6
    A = sp.Matrix([[1, 1], [0, 1]]); Bm = sp.Matrix([[1, 0], [w, 1]])
    comm = A * Bm.inv() * A.inv() * Bm                                           # [A, B^-1]
    rel = sp.simplify(comm * A - Bm * comm)
    Lw = sp.simplify(Bm.inv() * A * Bm * A ** -2 * Bm * A * Bm.inv())
    return rel, Lw, sp.simplify(w ** 2 - w + 1)


def e6_27():
    R = set()
    for i, j in itertools.combinations(range(8), 2):
        for si in (2, -2):
            for sj in (2, -2):
                v = [0] * 8; v[i] = si; v[j] = sj; R.add(tuple(v))
    for s in itertools.product((1, -1), repeat=8):
        if s.count(-1) % 2 == 0: R.add(s)
    # one 27: the roots whose colour weight is that of one state of the triplet: (r1, r2, r3) in {(2,0,0)+..., (1,-1,-1), (0,-2,-2)}
    t27 = [r for r in R if (r[0], r[1], r[2]) in ((2, 0, 0), (1, -1, -1), (0, -2, -2))]
    out = {}
    for r in t27:
        q = -3 * Fr(2, 3) * Fr(r[0] + r[1] + r[2], 2)                            # the U(1) charge, normalised to 1 on the 16
        d3 = sum(1 for k in (3, 4, 5) if r[k] != 0); d2 = sum(1 for k in (6, 7) if r[k] != 0)
        kind = "vector of SO(6)" if (d3, d2) == (1, 0) else "vector of SO(4)" if (d3, d2) == (0, 1) else "spinor" if abs(r[3]) == 1 else "singlet"
        out.setdefault((int(q), kind), 0); out[(int(q), kind)] += 1
    return len(t27), out


if __name__ == "__main__":
    print("G0: one-loop slopes from the content: SM %s; Pati-Salam with three generations, one complex bidoublet and scalars (4,2,1) + (4,1,2): %s; without those two scalars: %s"
          % (tuple(str(x) for x in slopes_sm()), tuple(str(x) for x in slopes_ps()), tuple(str(x) for x in slopes_ps(h421=0, h412=0))))
    w2, w4, trY2 = matching_weights(); print("G0: the matching weights from Y = T3R + (B - L)/2 on a generation: 1/g1^2 = (%s)/g2R^2 + (%s)/g4^2" % (w2, w4))
    import sm_rge
    tc = sm_rge.t_crit((0.5, 0.6, 1.0, 0.9, 0.1), 2); print("G0: its benchmark B0.2 on main's own two-loop running from the primary source: t = %.12f against its 7.578626559317 (%.1e)" % (tc, abs(tc - 7.578626559317)))
    rel, Lw, z = riley()
    print("G1: zeta_6^2 - zeta_6 + 1 = %s; [A, B^-1] A - B [A, B^-1] = %s; the longitude word = %s" % (z, rel.tolist(), Lw.tolist()))
    import snappy
    M = snappy.Manifold("m004"); M.set_displacement if False else None
    areas = M.cusp_areas(); nb = M.cusp_neighborhood(); nb.set_displacement(nb.stopping_displacement(0), 0)
    print("G1: m004: volume %.16f; 2 Cl_2(pi/3) = %.16f; the maximal cusp: area %.10f (2 sqrt 3 = %.10f), volume %.10f (sqrt 3 = %.10f); cusp shape %s" % (M.volume(), float(2 * sp.N(sp.im(sp.polylog(2, sp.exp(sp.I * sp.pi / 3))), 20)), nb.volume(0) * 2, 2 * 3 ** 0.5, nb.volume(0), 3 ** 0.5, M.cusp_info(0)["shape"]))
    n, br = e6_27(); print("G1: one 27 inside E8's roots: %d weights, by U(1) charge and kind: %s" % (n, dict(sorted(br.items()))))
    b4, b2l, b2r = slopes_ps(); print("G1: delta_b = b_2 - b_4 = %s; 22 delta_b / 67 = %s (the corridor's slope over pi)" % (b2l - b4, 22 * (b2l - b4) / 67))
    print("G1: the determinant's phase: with beta_Y = P(H_u, H_d) Y, d ln det Y / dt = Tr P, and the trace of a word of length at most 3 in two Hermitian matrices is real (its conjugate is the reversed word, a cyclic rotation); so arg det does not run at one and two loops for any Yukawas, and zero at the Pati-Salam scale stays zero")
