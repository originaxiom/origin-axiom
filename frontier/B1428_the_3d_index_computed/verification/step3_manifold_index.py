"""SUPERSEDED AS A DRIVER, KEPT AS A LIBRARY. Its uniform truncation lost terms when one
factor of the product starts at a negative power of q^{1/2}; step7_fixed_gluing.py is the
corrected driver and imports the helpers below. See FINDINGS section "the bug".
"""
"""
Step 3.  The 3D index I_T(0,0)(q) of an ideal triangulation, from SnapPy data.

GLUING RULE USED  (Garoufalidis-Hodgson-Rubinstein-Segerman, as written out in
E. McQuire's AMSI/VRS report Def. 4.1.1, and equivalent to Garoufalidis
arXiv:1208.1663 eq. (2.6)):

    J_D(a,b,c) = (-q^{1/2})^{-b} I^G(b-c, a-b)          [cyclically invariant in (a,b,c)]

    I_N(0)(q) = sum_{k in Z^n, r of the k_i set to 0}  q^{sum_i k_i}  prod_j J_D(a_j(k),b_j(k),c_j(k))

where n = #tetrahedra = #edges, r = #cusps, k_i is an integer weight on edge
class i, and a_j(k), b_j(k), c_j(k) are the total weights on the three pairs of
opposite edges of tetrahedron j.  Those three numbers are read straight off
SnapPy's  M.gluing_equations(form='log')  edge rows: entry (i, 3j+t) is the
number of edges of tetrahedron j in opposite-pair t that are glued to edge
class i.  (Column sums are all 2, which is the consistency check.)

I^G is the Garoufalidis-convention tetrahedron index (arXiv:1208.1663 eq. 1.2);
in the PROMPT's convention I^P(m,e) = I^G(e,m).
"""
import json, sys
import snappy
from tet_index import I_delta, s_str, s_mul, s_add, s_shift, s_scal, s_trunc, s_eq, sgn

XW = 60          # internal working precision, in x = q^{1/2} exponents


def IG(m, e, Xmax):
    return I_delta(e, m, Xmax)


def delta_x(m, e):
    """Lemma 3.6 of arXiv:1208.1663, in x-units (= 2*delta).  Verified in step 2."""
    p = lambda t: max(0, t)
    return p(m) * p(m + e) + p(-m) * p(e) + p(-e) * p(-e - m) + max(0, m, -e)


def J_delta(a, b, c, Xmax):
    """(-q^{1/2})^{-b} I^G(b-c, a-b);  (-q^{1/2})^{-b} = (-1)^b x^{-b}"""
    s = IG(b - c, a - b, Xmax + b)
    return s_scal(s_shift(s, -b, Xmax), sgn(b))


def J_mindeg(a, b, c):
    return -b + delta_x(b - c, a - b)


def edge_rows(name):
    M = snappy.Manifold(name) if isinstance(name, str) else name
    n = M.num_tetrahedra()
    r = M.num_cusps()
    G = [list(map(int, row)) for row in M.gluing_equations(form='log')]
    edges = G[:n]                      # first n rows are the edge equations
    assert len(edges[0]) == 3 * n
    # consistency: every column must sum to 2
    colsums = [sum(row[c] for row in edges) for c in range(3 * n)]
    return M, n, r, edges, colsums


def abc(edges, n, k, order):
    """(a_j,b_j,c_j) for each tetrahedron j given edge weights k (len n).
       order is a permutation of (0,1,2) applied to snappy's (z,z',z'') triple."""
    out = []
    for j in range(n):
        t = [sum(k[i] * edges[i][3 * j + s] for i in range(n)) for s in range(3)]
        out.append((t[order[0]], t[order[1]], t[order[2]]))
    return out


def index_zero(name, Xmax, order=(0, 1, 2), zero_edge=0, box=None, verbose=True):
    M, n, r, edges, colsums = edge_rows(name)
    assert r == 1, "this driver handles 1-cusped manifolds (rank-1 redundancy)"
    free = [i for i in range(n) if i != zero_edge]
    rank = len(free)

    # ---- choose a box: all lattice points whose TERM MIN-DEGREE <= Xmax,
    #      verified to sit strictly inside the scanned box.
    if box is None:
        box = 12 if rank <= 2 else 6
    keep = []
    boundary_bad = 0
    import itertools
    for kk in itertools.product(range(-box, box + 1), repeat=rank):
        k = [0] * n
        for idx, i in enumerate(free):
            k[i] = kk[idx]
        tri = abc(edges, n, k, order)
        D = 2 * sum(k) + sum(J_mindeg(*t) for t in tri)
        if D <= Xmax:
            keep.append((tuple(k), D))
            if max(abs(x) for x in kk) >= box - 1:
                boundary_bad += 1
    if verbose:
        print(f"   lattice points with term min-degree <= x^{Xmax}: {len(keep)}"
              f"   (box +-{box}, points touching the box rim: {boundary_bad})")
    if boundary_bad:
        raise RuntimeError("box too small -- contributing points reach the rim")

    total = {}
    for k, D in keep:
        tri = abc(edges, n, list(k), order)
        term = {0: 1}
        for t in tri:
            term = s_mul(term, J_delta(*t, Xmax=Xmax), Xmax)
        term = s_shift(term, 2 * sum(k), Xmax)      # q^{sum k_i} = x^{2 sum k_i}
        if term and min(term) != D:
            # Lemma 3.6 predicts the min degree of each factor; the product can
            # cancel, so only flag if it is SMALLER than predicted (a real bug)
            if min(term) < D:
                raise RuntimeError(f"min-degree bound violated at k={k}: {min(term)} < {D}")
        total = s_add(total, term)
    return total, n, r, edges, colsums, len(keep)


if __name__ == "__main__":
    XMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 30      # x-exponent => q^{XMAX/2}
    results = {}
    print("=" * 78)
    print(f"STEP 3: 3D index at the trivial boundary class (m,e)=(0,0), to q^{XMAX//2}")
    print("=" * 78)

    for name in ["m004", "m003", "m015"]:
        print(f"\n### {name}")
        M, n, r, edges, colsums = edge_rows(name)
        print(f"   tets={n} cusps={r} vol={M.volume()}  edge-eqn column sums={colsums}"
              f"  (all 2? {set(colsums) == {2}})")
        for order, lab in [((0, 1, 2), "(z,z',z'') as given"), ((0, 2, 1), "(z,z'',z') reversed")]:
            try:
                ser, *_rest, npts = index_zero(name, XMAX, order=order, verbose=False)
            except RuntimeError as ex:
                print(f"   order {lab}: FAILED: {ex}")
                continue
            # report only through a safe cut
            cut = XMAX - 6
            print(f"   order {lab}:  {s_str(ser, cut)}")
            results[f"{name}|{lab}"] = {str(k): v for k, v in sorted(s_trunc(ser, cut).items())}

    json.dump(results, open("step3_raw.json", "w"), indent=1)
    print("\n(raw coefficients dumped to step3_raw.json)")
