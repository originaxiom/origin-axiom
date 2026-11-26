"""B2014, S6 (main, 2026-11-26; data-free; GAP through sage): the order of G7 = <C, sigma> on the orbit of (3,3,3) mod 2187
(472,392 points), against 24 * 3^21 (agy-002's step d7 = 7 after B2007's 2, 2, 3, 7).
    ~/.local/bin/sage -python -B order_gap.py > order_gap_run.txt"""
import time
from sage.all import libgap, factor
t0 = time.time()
N = 2187
L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N); R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
Li = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1]); Ri = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
s0 = (3, 3, 3); seen, todo = {s0}, [s0]
while todo:
    v = todo.pop()
    for g in (L, R, Li, Ri):
        u = g(v)
        if u not in seen:
            seen.add(u); todo.append(u)
pts = sorted(seen); idx = {v: i for i, v in enumerate(pts)}
c = libgap.PermList([idx[(v[1], v[2], v[0])] + 1 for v in pts]); s = libgap.PermList([idx[(v[1], v[0], (v[0] * v[1] - v[2]) % N)] + 1 for v in pts])
G = libgap.Group(c, s)
n = libgap.Size(G)
print("mod %d: %d points; |G7| = %s = %s; equals 24 * 3^21: %s  [%.0f s]" % (N, len(pts), n, factor(int(n)), int(n) == 24 * 3 ** 21, time.time() - t0))
