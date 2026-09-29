"""
Step 7.  The gluing sum, with the per-factor truncation done CORRECTLY.

THE BUG IN STEP 3/4/6
---------------------
A factor J_D(a,b,c) = (-q^{1/2})^{-b} I^G(b-c, a-b) can have a strictly
NEGATIVE minimal degree (the prefactor shifts down by b).  If one factor of the
product starts at x^{-20} and another at x^{+20}, then computing BOTH only up
to x^{Xmax} loses every contribution to the product between x^{Xmax-20} and
x^{Xmax}.  That is exactly why m015/m006/m007/m009 appeared to depend on which
edge weight was set to zero: different charts put the negative shifts on
different factors.  m004 was unaffected (its factors never go negative), which
is why it matched the literature anyway.

THE FIX
-------
Lemma 3.6 of arXiv:1208.1663 gives the EXACT minimal degree of I_Delta (verified
in step 2), hence the exact minimal degree d_j of each factor J_j.  Write
J_j = x^{d_j} F_j with F_j in Z[[x]] of minimal degree 0.  The whole term is

        x^{D(k)} * prod_j F_j ,      D(k) = 2*sum_i k_i + sum_j d_j

so to know the term through x^{Xmax} it suffices to know each F_j - and the
running product - through x^{Xmax - D(k)}, which is >= 0 exactly on the
lattice points we keep.  Every truncation is then non-negative and safe.
"""
import sys, json, itertools
import snappy
from tet_index import I_delta, s_str, s_mul, s_add, s_shift, s_trunc, s_eq, sgn
from step3_manifold_index import IG, edge_rows, abc, delta_x

X = int(sys.argv[1]) if len(sys.argv) > 1 else 30
CUT = X - 6


def J_mindeg(a, b, c):
    """exact minimal x-degree of J_D(a,b,c)"""
    return -b + delta_x(b - c, a - b)


def J_normalised(a, b, c, budget):
    """F = x^{-d} J_D(a,b,c), known through x^{budget}.  Minimal degree 0."""
    d = J_mindeg(a, b, c)
    # J = (-1)^b x^{-b} I^G(b-c, a-b);  F = x^{-d} J = (-1)^b x^{-b-d} I^G(...)
    sh = -b - d
    s = I_delta(a - b, b - c, budget - sh)     # I^G(m,e) = I_delta(e,m)
    return {k + sh: sgn(b) * v for k, v in s.items() if k + sh <= budget}


def region(edges, n, free, order, Xmax, box):
    keep, maxabs = [], 0
    for kk in itertools.product(range(-box, box + 1), repeat=len(free)):
        k = [0] * n
        for idx, i in enumerate(free):
            k[i] = kk[idx]
        D = 2 * sum(k) + sum(J_mindeg(*t) for t in abc(edges, n, k, order))
        if D <= Xmax:
            keep.append((tuple(k), D))
            maxabs = max(maxabs, max(abs(v) for v in kk) if kk else 0)
    return keep, maxabs


def index_zero(name, Xmax, order=(0, 1, 2), zero_edge=0, box=None, verbose=False):
    M, n, r, edges, colsums = edge_rows(name)
    assert r == 1 and set(colsums) == {2}, "1-cusped, standard edge data expected"
    free = [i for i in range(n) if i != zero_edge]
    rank = len(free)
    if box is None:
        box = {1: 300, 2: 60, 3: 26, 4: 16, 5: 11}[rank]
    keep, maxabs = region(edges, n, free, order, Xmax, box)
    assert box - maxabs >= box // 3, f"widen the box: outermost |k|={maxabs}, box={box}"
    tot = {}
    for k, D in keep:
        budget = Xmax - D                      # >= 0 by construction
        prod = {0: 1}
        for t in abc(edges, n, list(k), order):
            prod = s_mul(prod, J_normalised(*t, budget=budget), budget)
        tot = s_add(tot, s_shift(prod, D, Xmax))
    if verbose:
        print(f"      {len(keep)} lattice points, outermost |k|={maxabs}, box +-{box}")
    return tot, len(keep), maxabs


if __name__ == "__main__":
    print("=" * 78)
    print(f"STEP 7: corrected gluing sum, to q^{CUT//2}")
    print("=" * 78)

    print("\n[1] m004 against the published GHRS series (regression test):")
    ghrs = {0:1, 2:-2, 4:-3, 6:2, 8:8, 10:18, 12:18, 14:14, 16:-12, 18:-52, 20:-106}
    s, npts, mx = index_zero("m004", X, verbose=True)
    ok = {k: v for k, v in s_trunc(s, 20).items() if v} == {k: v for k, v in ghrs.items() if v}
    print(f"    {s_str(s, CUT)}")
    print(f"    matches GHRS through q^10: {ok}")

    print("\n[2] Edge-choice independence (the test that failed before the fix):")
    for name in ["m004", "m003", "m006", "m007", "m009", "m015", "m016", "m017", "m019", "m022"]:
        M, n, r, edges, cs = edge_rows(name)
        sers = [index_zero(name, X, zero_edge=z)[0] for z in range(n)]
        same = all(s_eq(sers[0], t, CUT) for t in sers)
        print(f"    {name}: {n} choices, all agree through q^{CUT//2}: {same}")
        if not same:
            for z, t in enumerate(sers):
                print(f"       z={z}: {s_str(t, CUT)}")

    print("\n[3] Cyclic-order independence (snappy (z,z',z'') vs the reversed triple):")
    for name in ["m004", "m015", "m022"]:
        a = index_zero(name, X, order=(0, 1, 2))[0]
        b = index_zero(name, X, order=(0, 2, 1))[0]
        print(f"    {name}: agree: {s_eq(a, b, CUT)}")

    print("\n[4] The control table:")
    table = {}
    for name in ["m004", "m003", "m006", "m007", "m009", "m015", "m016",
                 "m017", "m019", "m022", "m023", "m026"]:
        M = snappy.Manifold(name)
        if M.num_cusps() != 1:
            print(f"    {name}: skipped ({M.num_cusps()} cusps)")
            continue
        s, npts, mx = index_zero(name, X)
        table[name] = {str(k): v for k, v in sorted(s_trunc(s, CUT).items())}
        print(f"    {name:5s} n={M.num_tetrahedra()} vol={float(M.volume()):.7f} "
              f"H1={M.homology()}  ({npts} pts)")
        print(f"          {s_str(s, CUT)}")
    sigs = {}
    for k, v in table.items():
        sigs.setdefault(json.dumps(v), []).append(k)
    print(f"\n    {len(table)} manifolds -> {len(sigs)} DISTINCT series:  "
          f"{[v for v in sigs.values()]}")
    json.dump(table, open("step7_table.json", "w"), indent=1)
