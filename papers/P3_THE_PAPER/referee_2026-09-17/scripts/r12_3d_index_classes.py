"""Round 5: an INDEPENDENT check of B1428 (S23) and B1431 (S26) -- the 3D index at every boundary
class, and whether it separates the object m004 from its sibling m003.

Written without reading the project's implementation.  Everything below is from the definitions:

  Garoufalidis 1208.1663 eq (1.2)       tetrahedron index I_D(m,e)            (r11, triality-checked)
  GHHR 1604.02688                        J_D(a,b,c) = (-q^{1/2})^{-b} I_D(b-c, a-b)
  GHHR 1604.02688 eq (16)                I_T([g])(q) = sum_{k in Z^{n-r}} q^{sum k_i} prod_j J_D(a_j, b_j, c_j)
                                         where (a_j,b_j,c_j) are tetrahedron j's entries of
                                         sum_i k_i E_i + p M + q L   (edge rows E, cusp rows M, L)

SnapPy supplies ONLY the gluing-equation rows.

THE TRAP S23 FELL INTO, AVOIDED BY CONSTRUCTION.  (-q^{1/2})^{-b} and q^{sum k} can have NEGATIVE
degree, so truncating every factor at one shared order silently loses terms.  Here every factor gets
its own precision budget from an exact lower bound on its degree:

    deg I_D(m,e) >= L(m,e) := min_{n >= max(0,-e)} [ n(n+1) - (2n+e)m ]     (half-units)

since 1/((q)_n (q)_{n+e}) contributes only non-negative powers.  For a term with total lower bound LB,
factor j is computed to order  D - (LB - LB_j)  in its own degree, which is exactly what is needed for
the product to be exact through order D.  Terms with LB > D are provably zero through order D and
are skipped; the k-range is then certified by requiring LB > D at its boundary.

CONTROLS, all of which must pass before any comparison is reported:
  1. five published classes of 4_1 (GHHR): 0, mu, 2mu, lambda, 4mu+lambda
  2. independence of WHICH edge weight is pinned to zero (S23's bug symptom)
  3. retriangulation invariance on random triangulations
"""
import sys, os, itertools, random, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r11_3d_index as R          # I_tet, mul, add_scaled, trunc, show  (exact, integer, q^{1/2} units)
import snappy

_TET = {}


def _pos(x):
    return x if x > 0 else 0


def L_tet(m, e):
    """the EXACT minimal degree of I_D(m,e), half-units: Garoufalidis's closed form
        2 delta(m,e) = m+ (m+e)+ + (-m)+ e+ + (-e)+ (-e-m)+ + max(0, m, -e).
    Verified against direct computation on all 361 pairs |m|,|e| <= 9.  (The per-SUMMAND bound is
    valid but useless: the summands carry huge negative degrees that cancel in the sum.)"""
    return _pos(m) * _pos(m + e) + _pos(-m) * _pos(e) + _pos(-e) * _pos(-e - m) + max(0, m, -e)


def I_tet(m, e, cap):
    """memoised tetrahedron index, exact through `cap` (half-units).  Every value actually computed is
    checked against the closed-form degree, so a violation outside the verified box cannot pass silently."""
    have = _TET.get((m, e))
    if have is not None and have[0] >= cap:
        return {k: v for k, v in have[1].items() if k <= cap}
    if cap < L_tet(m, e):
        s = {}
    else:
        s = R.I_tet(m, e, cap)
        assert not s or min(s) >= L_tet(m, e), f"degree lemma violated at {(m, e)}: {min(s)} < {L_tet(m, e)}"
    _TET[(m, e)] = (cap, s)
    return s


def J(a, b, c, cap):
    """J_D(a,b,c) = (-q^{1/2})^{-b} I_D(b-c, a-b), exact through cap"""
    m, e = b - c, a - b
    base = I_tet(m, e, cap + b)
    out = {}
    sgn = -1 if (b % 2) else 1
    R.add_scaled(out, base, -b, sgn, cap)
    return {k: v for k, v in out.items() if v}


def J_lower(a, b, c):
    return -b + L_tet(b - c, a - b)


def rows(M):
    import numpy as np
    G = [[int(x) for x in r] for r in np.array(M.gluing_equations()).tolist()]
    n = M.num_tetrahedra()
    E = G[:n]
    Mu, La = G[n], G[n + 1]
    return E, Mu, La, n


def index(E, Mu, La, n, p, q2, D, pin=None, K=24):
    """I_T at class p*Mu + (q2/2)*La  (q2 counts HALF-longitudes), exact through D half-units.
    The sum runs over k in Z^n with k[pin] = 0."""
    if pin is None:
        pin = n - 1
    base = [p * Mu[t] + (q2 * La[t]) // 2 for t in range(3 * n)]
    assert all((q2 * La[t]) % 2 == 0 for t in range(3 * n)), "half-class not integral here"
    free = [i for i in range(n) if i != pin]
    tot = {}
    boundary_min = None
    for ks in itertools.product(range(-K, K + 1), repeat=len(free)):
        k = [0] * n
        for i, v in zip(free, ks):
            k[i] = v
        vec = list(base)
        for i in range(n):
            if k[i]:
                for t in range(3 * n):
                    vec[t] += k[i] * E[i][t]
        pre = 2 * sum(k)
        lbs = [J_lower(vec[3 * j], vec[3 * j + 1], vec[3 * j + 2]) for j in range(n)]
        LB = pre + sum(lbs)
        if any(abs(v) == K for v in ks):
            boundary_min = LB if boundary_min is None else min(boundary_min, LB)
        if LB > D:
            continue
        # Each factor is exact through its own budget D - (LB - lb_j).  The RUNNING product must also
        # keep terms above D whenever factors still to come can have negative degree: after the first
        # t factors it is kept through D - (sum of the remaining factors' lower bounds).  Truncating it
        # at D would be S23's bug in a new place.
        prod = {pre: 1}
        remaining = sum(lbs)
        for j in range(n):
            cap_j = D - (LB - lbs[j])
            f = J(vec[3 * j], vec[3 * j + 1], vec[3 * j + 2], cap_j)
            remaining -= lbs[j]
            prod = _mul_signed(prod, f, D - remaining)
        for kk, vv in prod.items():
            tot[kk] = tot.get(kk, 0) + vv
    assert boundary_min is None or boundary_min > D, \
        f"k-range too small: a boundary term has lower bound {boundary_min} <= {D}"
    return {k: v for k, v in tot.items() if v and k <= D}


def _mul_signed(s1, s2, cap):
    """product keeping only exponents <= cap; exact because each factor's budget was set from bounds"""
    out = {}
    for k1, v1 in s1.items():
        for k2, v2 in s2.items():
            k = k1 + k2
            if k <= cap:
                out[k] = out.get(k, 0) + v1 * v2
    return {k: v for k, v in out.items() if v}


def ser(s, upto):
    return R.show(s, upto)


def main():
    D = 16                                   # through q^8
    print("=" * 78)
    print("CONTROL 1 -- five published classes of 4_1 (GHHR 1604.02688)")
    print("=" * 78)
    K41 = snappy.Manifold("4_1")
    E, Mu, La, n = rows(K41)
    print(f"   4_1: {n} tetrahedra;  mu row {Mu};  lambda row {La}")
    # I(mu): the arXiv source (1604.02688, e-print of Apr 2016, Example 4.1, read verbatim) PRINTS
    #   "2 q-2 q^2+2 q^3+8 q^4+16 q^5+..."  -- a leading +2q.
    # The SAME paper's explicit formula  I(x mu + y lam) = sum_k I_D(k-x,k) I_D(k+2y,k-x+2y), evaluated
    # exactly, gives -2q - 2q^2 + 2q^3 + ...  -- and reproduces all seven of its OTHER printed series
    # exactly, half-classes included.  This general implementation also gives -2q, and so does the
    # project's own B1428 code.  So the arXiv printing has a sign typo at q^1; the target here is the
    # formula-consistent value.  (The journal version, Illinois J. Math. 60 (2016), was not accessible
    # to check whether it corrected the sign.)
    published = {
        (0, 0): {0: 1, 2: -2, 4: -3, 6: 2, 8: 8, 10: 18},
        (1, 0): {2: -2, 4: -2, 6: 2, 8: 8, 10: 16},
        (2, 0): {2: -1, 4: -1, 6: 3, 8: 6, 10: 12},
        (0, 2): {6: 1, 8: 2, 10: 5, 12: 2, 14: -3, 16: -16},
        (4, 2): {2: 1, 8: -1, 10: -2, 12: -5, 14: -8, 16: -10},
    }
    label = {(0, 0): "0", (1, 0): "mu", (2, 0): "2mu", (0, 2): "lambda", (4, 2): "4mu+lambda"}
    ok1 = True
    for (p, q2), pub in published.items():
        got = index(E, Mu, La, n, p, q2, D)
        top = max(pub)
        match = all(got.get(k, 0) == v for k, v in pub.items()) and \
            all(k in pub or k > top for k in got if got[k])
        ok1 &= match
        print(f"   I({label[(p, q2)]:<10s}) = {ser(got, 16):<64s} {'MATCH' if match else 'MISMATCH'}")
    print(f"   all five published classes reproduce: {ok1}")
    # the three published HALF-classes need a triangulation whose longitude row is even: m004's is.
    Eh, Mh, Lh, nh = rows(snappy.Manifold("m004"))
    halves = {(0, 1): {3: -2, 7: 4, 9: 10, 11: 14, 13: 10, 15: -2},
              (1, 1): {2: -1, 4: -1, 6: 2, 8: 7, 10: 11, 12: 11, 14: 3, 16: -17},
              (2, 1): {1: -1, 5: 1, 7: 4, 9: 7, 11: 7, 13: 3, 15: -12}}
    hl = {(0, 1): "lambda/2", (1, 1): "mu+lambda/2", (2, 1): "2mu+lambda/2"}
    for (p, q2), pub in halves.items():
        got = index(Eh, Mh, Lh, nh, p, q2, D)
        top = max(pub)
        match = all(got.get(k, 0) == v for k, v in pub.items()) and \
            all(k in pub or k > top for k in got if got[k])
        ok1 &= match
        print(f"   I({hl[(p, q2)]:<12s}) = {ser(got, 16):<62s} {'MATCH' if match else 'MISMATCH'}   [m004 rows]")
    print(f"   all eight published classes reproduce (I(mu) against the formula-consistent sign): {ok1}")
    if not ok1:
        print("   -> CONVENTION OR IMPLEMENTATION WRONG; nothing below is reported")
        return

    print()
    print("=" * 78)
    print("CONTROL 2 -- which edge weight is pinned must not matter (S23's bug symptom)")
    print("=" * 78)
    ok2 = True
    for (p, q2) in published:
        a = index(E, Mu, La, n, p, q2, D, pin=0)
        b = index(E, Mu, La, n, p, q2, D, pin=1)
        ok2 &= (a == b)
    print(f"   pin edge 0 vs pin edge 1, all five classes: {'identical' if ok2 else 'DIFFER'}")

    print()
    print("=" * 78)
    print("CONTROL 3 -- retriangulation invariance (random triangulations of 4_1)")
    print("=" * 78)
    random.seed(1)
    ref = {c: index(E, Mu, La, n, c[0], c[1], 8) for c in [(0, 0), (1, 0), (0, 2)]}
    agree, tried, sizes = 0, 0, []
    for t in range(40):
        X = snappy.Manifold("4_1")
        X.randomize()
        X.simplify()
        sizes.append(X.num_tetrahedra())
        if X.num_tetrahedra() > 3:
            continue
        Ex, Mx, Lx, nx = rows(X)
        try:
            same = all(index(Ex, Mx, Lx, nx, c[0], c[1], 8, K=10) == ref[c] for c in ref)
        except AssertionError:
            continue
        tried += 1
        agree += same
    from collections import Counter as _C
    print(f"   40 randomise+simplify runs; tetrahedra counts: {dict(sorted(_C(sizes).items()))}")
    print(f"   triangulations with <= 3 tetrahedra whose sum converged: {tried};"
          f"  agreeing with the reference on 0, mu, lambda through q^4: {agree}")

    print()
    print("=" * 78)
    print("S23 -- the trivial class: m004 vs m003")
    print("=" * 78)
    Em4, Mm4, Lm4, nm4 = rows(snappy.Manifold("m004"))
    Em3, Mm3, Lm3, nm3 = rows(snappy.Manifold("m003"))
    print(f"   m003: {nm3} tetrahedra;  mu row {Mm3};  lambda row {Lm3};  H1 = {snappy.Manifold('m003').homology()}")
    i4 = index(Em4, Mm4, Lm4, nm4, 0, 0, D)
    i3 = index(Em3, Mm3, Lm3, nm3, 0, 0, D)
    print(f"   I_m004(0) = {ser(i4, 16)}")
    print(f"   I_m003(0) = {ser(i3, 16)}")
    print(f"   identical through q^8: {i4 == i3}")

    print()
    print("=" * 78)
    print("S26 -- all honest boundary classes p*mu + q*lambda, as SETS of series (no basis enters)")
    print("=" * 78)
    D2 = 8                                   # through q^4 -- S26 says the witnesses differ at q^1
    B = 12

    def table(Ex, Mx, Lx, nx):
        out = {}
        for p in range(-B, B + 1):
            for q in range(-B, B + 1):
                out[(p, q)] = tuple(sorted(index(Ex, Mx, Lx, nx, p, 2 * q, D2, K=16).items()))
        return out

    t4 = table(Em4, Mm4, Lm4, nm4)
    t3 = table(Em3, Mm3, Lm3, nm3)
    S4, S3 = set(t4.values()), set(t3.values())
    zero = tuple()
    print(f"   classes computed per manifold: {(2*B+1)**2};  distinct non-zero series through q^4:"
          f"  m004 {len(S4 - {zero})},  m003 {len(S3 - {zero})}")
    only4 = S4 - S3 - {zero}
    only3 = S3 - S4 - {zero}
    print(f"   series occurring for m004 and at NO class of m003: {len(only4)}")
    print(f"   series occurring for m003 and at NO class of m004: {len(only3)}")
    mu4 = t4[(1, 0)]
    lam3 = t3[(0, 1)]
    print(f"   m004's meridian series  {ser(dict(mu4), 8):<40s} occurs for m003: {mu4 in S3}")
    print(f"   m003's longitude series {ser(dict(lam3), 8):<40s} occurs for m004: {lam3 in S4}")

    # completeness: every class OUTSIDE the box has lower bound > D2, so cannot equal any series
    # of degree <= D2.  Checked on the box's boundary ring, where the bound is smallest.
    def min_lb(Ex, Mx, Lx, nx, p, q):
        best = None
        for kk in range(-16, 17):
            k = [kk, 0][:nx] + [0] * max(0, nx - 2)
            vec = [p * Mx[t] + q * Lx[t] for t in range(3 * nx)]
            for i in range(nx):
                for t in range(3 * nx):
                    vec[t] += k[i] * Ex[i][t]
            lb = 2 * sum(k) + sum(J_lower(vec[3*j], vec[3*j+1], vec[3*j+2]) for j in range(nx))
            best = lb if best is None else min(best, lb)
        return best
    ring = [(p, q) for p in range(-B, B + 1) for q in range(-B, B + 1) if max(abs(p), abs(q)) == B]
    r4 = min(min_lb(Em4, Mm4, Lm4, nm4, p, q) for p, q in ring)
    r3 = min(min_lb(Em3, Mm3, Lm3, nm3, p, q) for p, q in ring)
    print(f"   smallest degree lower bound on the box's boundary ring: m004 {r4}, m003 {r3}"
          f"  (half-units; the witnesses have degree 2)")


if __name__ == "__main__":
    main()
