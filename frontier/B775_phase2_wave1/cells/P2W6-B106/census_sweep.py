"""P2W6-B106 -- the rank-n Fix(T_1^2) A-spectrum census, EXHAUSTIVE over F_p-rational spectra.

Run with sage-python (Singular back end; the pyenv sympy Buchberger walls on the same ideal).

For each multiset {a_1..a_n} in (F_p^*)^n with prod a_i = 1 (i.e. every F_p-rational SL(n)
spectrum), compute the dimension of the IRREDUCIBLE stratum of the bundle variety

    (*)  A t A^-2 t A = t A t ,   A = diag(a),   gauge: t[row,:] = (1,...,1)

  I = <(*)> : det(t)^inf : f_S^inf  for every proper nonempty S c {1..n},
  f_S = a generic linear form in the entries of det(t)*B that move S  (B = A^-2 t A t^-1).

Since every A-invariant subspace of a diag(distinct) A is a coordinate subspace, f_S != 0 for
all S is EXACTLY irreducibility when the a_i are distinct, and is NECESSARY (hence the
dimension is an UPPER bound for the irreducible stratum) when they are not.  So dim <= 1
EXCLUDES a fixed-spectrum (Dehn-filling) component at that spectrum: such a component has
2-dimensional moduli and 4 gauge directions, of which this gauge fixes exactly 4.

The dimension is maximised over the n choices of gauge row (equivalently over the n cyclic
positions of the spectrum), so the only residual genericity assumption is that SOME row of t
is nowhere zero.
"""
import itertools
import json
import sys
import time

from sage.all import GF, PolynomialRing, diagonal_matrix, matrix


def setup(n, p, spec, gauge_row=0):
    a = [int(x) for x in spec]
    F = GF(p)
    nv = n * n - n
    R = PolynomialRing(F, ['t%d' % i for i in range(nv)], order='degrevlex')
    tv = list(R.gens())

    def tt(i, j):
        if i == gauge_row:
            return R(1)
        ii = i - 1 if i > gauge_row else i
        return tv[ii * n + j]

    M = matrix(R, n, n, [tt(i, j) for i in range(n) for j in range(n)])
    eqs = []
    for i in range(n):
        for j in range(n):
            s = R(0)
            for k in range(n):
                pr = 1
                for l in range(n):
                    if l != k:
                        pr = pr * a[l] * a[l] % p
                c = (a[i] * a[j] - pow(a[k], 3, p)) * pr % p
                s += R(int(c)) * tt(i, k) * tt(k, j)
            if s != 0:
                eqs.append(s)
    ai = [pow(x, p - 2, p) for x in a]
    A = diagonal_matrix(R, [R(int(x)) for x in a])
    A2i = diagonal_matrix(R, [R(int(ai[i] * ai[i] % p)) for i in range(n)])
    Bnum = A2i * M * A * M.adjugate()
    forms = []
    for r in range(1, n):
        for S in itertools.combinations(range(n), r):
            Ss = set(S)
            forms.append(sum(R(int(1 + (7 * i + 5 * j) % (p - 1))) * Bnum[i, j]
                             for j in Ss for i in range(n) if i not in Ss))
    return R, eqs, forms, M


def census_dim(n, p, spec, gauge_row=0):
    R, eqs, forms, M = setup(n, p, spec, gauge_row)
    I = R.ideal(eqs)
    if I.dimension() < 0:
        return -1
    I = I.saturation(R.ideal(M.det()))[0]
    for f in forms:
        if I.dimension() < 0:
            return -1
        I = I.saturation(R.ideal(f))[0]
    return int(I.dimension())


def sweep(n, p, gauges=None):
    gauges = list(range(n)) if gauges is None else gauges
    seen, rows = set(), []
    t0 = time.time()
    for tup in itertools.product(range(1, p), repeat=n - 1):
        last = pow(1, 1, p)
        pr = 1
        for x in tup:
            pr = pr * x % p
        last = pow(pr, p - 2, p)
        ms = tuple(sorted(tup + (last,)))
        if ms in seen:
            continue
        seen.add(ms)
        d = max(census_dim(n, p, ms, g) for g in gauges)
        rows.append({"spec": list(ms), "dim": d, "distinct": len(set(ms)) == n})
    return {"n": n, "p": p, "n_spectra": len(rows), "sec": float(round(time.time() - t0, 1)),
            "gauges": gauges,
            "jump": sorted([r for r in rows if r["dim"] >= 2], key=lambda r: -r["dim"]),
            "hist": {str(d): sum(1 for r in rows if r["dim"] == d)
                     for d in sorted({r["dim"] for r in rows})}}


if __name__ == "__main__":
    jobs = json.loads(sys.argv[1]) if len(sys.argv) > 1 else [[3, 13], [4, 13], [4, 17]]
    out = []
    for n, p in jobs:
        r = sweep(n, p)
        out.append(r)
        print(json.dumps(r), flush=True)
    json.dump(out, open(sys.argv[2] if len(sys.argv) > 2 else "census_sweep.json", "w"))
    print("SWEEP-DONE")
