"""B1987 (main, 2026-11-25; data-free): the unweighted unfolding W+ = P_L + P_R (and W+- with inverses) on each orbit of the
moves over the common point on the cusp's leaf mod 27, 81, 125 and 343: undamped modes (|eigenvalue| = 2) with their
arguments, the slowest decay below 2, and W+-'s gap below its top. numpy eigenvalues. See ../CARD.md.
    python3 -B listen5.py > listen5_run.txt"""
import numpy as np, cmath, time
from itertools import product
def orbs(N, p):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N); R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    pts = [v for v in product(range(0, N, p), repeat=3) if (v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2]) % N == 0]
    seen, out = set(), []
    for v in pts:
        if v in seen: continue
        o, s, st = [v], {v}, [v]
        while st:
            u = st.pop()
            for f in (L, R):
                w = f(u)
                if w not in s: s.add(w); o.append(w); st.append(w)
        seen |= s; out.append(o)
    return out, L, R
t0 = time.time(); summary = {}
for N, p in ((27, 3), (81, 3), (125, 5), (343, 7)):
    out, L, R = orbs(N, p)
    print("== mod %d over the common point: %d orbits" % (N, len(out)), flush=True)
    seen_types = {}
    for o in sorted(out, key=len):
        n = len(o); idx = {v: i for i, v in enumerate(o)}
        PL = np.zeros((n, n)); PR = np.zeros((n, n))
        for v in o: PL[idx[L(v)], idx[v]] = 1; PR[idx[R(v)], idx[v]] = 1
        ev = np.linalg.eigvals(PL + PR); evs = np.linalg.eigvalsh(PL + PL.T + PR + PR.T)
        und = sorted({round(cmath.phase(z) / (2 * np.pi), 6) % 1 for z in ev if abs(abs(z) - 2) < 1e-7})
        slow = max([abs(z) for z in ev if abs(z) < 2 - 1e-7], default=0.0)
        gap = evs[-1] - max([e for e in evs if e < evs[-1] - 1e-7], default=evs[-1])
        key = (n, tuple(und), round(slow, 4), round(gap, 4))
        seen_types[key] = seen_types.get(key, 0) + 1
    for (n, und, slow, gap), c in sorted(seen_types.items()):
        print("  orbits of %4d (x%d): undamped modes at arguments (turns) %s; slowest decay |eigenvalue| %.4f (ratio %.4f); W+- gap below the top %.4f" % (n, c, list(und), slow, slow / 2, gap), flush=True)
        summary.setdefault(N, []).append((n, und, slow))
    print("  [%.0f s]" % (time.time() - t0), flush=True)
allund = sorted({u for N in summary for (_, und, _) in summary[N] for u in und})
print("SUMMARY T1: the undamped modes' arguments over every orbit and level run (turns; 0 = the constant, 0.5 = the sign): %s" % allund)
grow = [(N, n, s) for N in summary for (n, und, s) in summary[N] if n in (72, 648, 120, 1176)]
print("SUMMARY T2: on the grown orbits the slowest decay ratios: %s" % sorted({(N, n, round(s / 2, 4)) for (N, n, s) in grow}))
