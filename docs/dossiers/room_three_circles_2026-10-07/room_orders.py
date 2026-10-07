"""Structure only: the line's interior supply n(chi) at N45's cusp-trivial characters of order m (free part; odd m has no
torsion part), route R.  python3 room_orders.py ROOT m [m ...]"""
import importlib.util, sys, time, itertools
from collections import Counter
from pathlib import Path
import numpy as np
V = Path(sys.argv[1]) / "frontier/B1547_the_room_three_members/verification"
spec = importlib.util.spec_from_file_location("ro_member_lib", V / "member_lib.py")
ML = importlib.util.module_from_spec(spec); sys.modules["ro_member_lib"] = ML; spec.loader.exec_module(ML)
FL = ML.FL
rc = FL.RCover("N45"); RC = ML.RChars(rc)
p = rc.p
loops = ML.common_loops({g: list(rc.cov.P[g]) for g in ("a", "t")})
for m in map(int, sys.argv[2:]):
    t0 = time.time()
    zm = rc.root(m)
    seen, rows = set(), []
    tors = [()] if m % 2 else list(itertools.product(range(2), repeat=RC.T.shape[0]))
    for a in itertools.product(range(m), repeat=RC.F.shape[0]):
        for b in tors:
            e = sum(ai * RC.F[i] for i, ai in enumerate(a))
            if b:
                e = e + (m // 2) * sum(bi * RC.T[i] for i, bi in enumerate(b))
            e = np.asarray(e, dtype=np.int64) % m
            key = RC.values(e, loops, m)
            from math import gcd
            o = m
            for x in key:
                o = gcd(o, x)
            if m // o != m:          # not of exact order m
                continue
            gal = min(tuple((k * x) % m for x in key) for k in range(1, m) if gcd(k, m) == 1)
            if gal in seen:
                continue
            seen.add(gal)
            mod = rc.R.CMod([np.array([[pow(zm, int(x) % m, p)]], dtype=np.int64) for x in e], p)
            C = rc.R.Coh(rc.cov, mod)
            rows.append((int(C.h1), int(C.n)))
    print("order", m, "Galois classes", len(rows), "(h1, n):", dict(sorted(Counter(rows).items())), round(time.time() - t0, 1), "s", flush=True)
