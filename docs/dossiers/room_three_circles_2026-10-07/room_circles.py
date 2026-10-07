"""Structure only: the free-lattice coordinates (mod m) of N45's cusp-trivial characters with n = 3, orders 2..6 and 8, route R;
test whether they are the order-m points of five circles t -> t v (v primitive in Z^4).  python3 room_circles.py ROOT"""
import importlib.util, sys, time, itertools
from math import gcd
from pathlib import Path
import numpy as np
V = Path(sys.argv[1]) / "frontier/B1547_the_room_three_members/verification"
spec = importlib.util.spec_from_file_location("rc_member_lib", V / "member_lib.py")
ML = importlib.util.module_from_spec(spec); sys.modules["rc_member_lib"] = ML; spec.loader.exec_module(ML)
FL = ML.FL
rc = FL.RCover("N45"); RC = ML.RChars(rc)
p = rc.p
found = {}
for m in (2, 3, 4, 5, 6):
    zm = rc.root(m)
    out = []
    for a in itertools.product(range(m), repeat=4):
        g = m
        for x in a:
            g = gcd(g, x)
        if g != 1:          # exact order m on the free part
            continue
        e = np.asarray(sum(ai * RC.F[i] for i, ai in enumerate(a)), dtype=np.int64) % m
        mod = rc.R.CMod([np.array([[pow(zm, int(x) % m, p)]], dtype=np.int64) for x in e], p)
        n = int(rc.R.Coh(rc.cov, mod).n)
        if n >= 3:
            out.append(a)
    found[m] = out
    print("order", m, "n>=3 at", len(out), "characters:", out[:12], flush=True)
# the order-2 directions (mod 2) and whether each order-m point reduces to one of them
v2 = set(found[2])
for m in (4, 6):
    print("order", m, "points mod 2:", sorted({tuple(x % 2 for x in a) for a in found[m]}), "within the order-2 set:",
          all(tuple((x * (m // 2)) % m // (m // 2) for x in a) in v2 for a in found[m]), flush=True)
# lines through the origin: for order 3 and 5, a point a generates the line {t a}; group them
for m in (3, 5):
    lines = []
    for a in found[m]:
        L = frozenset(tuple((t * x) % m for x in a) for t in range(1, m))
        if L not in lines:
            lines.append(L)
    print("order", m, "lines:", len(lines), [sorted(L)[0] for L in lines], flush=True)
