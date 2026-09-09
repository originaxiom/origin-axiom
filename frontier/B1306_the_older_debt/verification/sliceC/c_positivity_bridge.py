"""C3 -- cc3 B8083: two positive words in R, L are conjugate in SL(2,Z) iff they are cyclic rotations of one another. Own complete invariant:
the Gauss reduction cycle of the fixed-point form f_M = (r, s-p, -q) of M = [[p,q],[r,s]] (proper equivalence of indefinite forms <-> cycles of
reduced forms), together with the trace. Checked on every positive word of length 2..LMAX (pure R^n, L^n excluded: parabolic)."""
import sys, json
from math import isqrt
LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10
R = ((1, 1), (0, 1)); L = ((1, 0), (1, 1))
def mul(X, Y): return ((X[0][0]*Y[0][0] + X[0][1]*Y[1][0], X[0][0]*Y[0][1] + X[0][1]*Y[1][1]), (X[1][0]*Y[0][0] + X[1][1]*Y[1][0], X[1][0]*Y[0][1] + X[1][1]*Y[1][1]))
def matrix(w):
    M = ((1, 0), (0, 1))
    for ch in w: M = mul(M, R if ch == "R" else L)
    return M
def is_square(n): return n >= 0 and isqrt(n) ** 2 == n
def reduced(a, b, c, D):
    return b > 0 and b * b < D and (2 * abs(a) + b) ** 2 > D and (2 * abs(a) < b or (2 * abs(a) - b) ** 2 < D)
def step(a, b, c, D):
    """(a,b,c) -> (c, b', c') with b' = -b mod 2|c| chosen in (sqrt D - 2|c|, sqrt D)"""
    m = 2 * abs(c); s = isqrt(D)
    bp = s - ((s + b) % m)                       # largest b' <= s with b' = -b (mod m)
    if bp * bp == D: bp -= m                     # never equal to sqrt D (D non-square anyway)
    cp = (bp * bp - D) // (4 * c); assert (bp * bp - D) % (4 * c) == 0
    return (c, bp, cp)
def cycle_invariant(M):
    (p, q), (r, s) = M; t = p + s; a, b, c = r, s - p, -q; D = b * b - 4 * a * c
    assert D == t * t - 4 and D > 0 and not is_square(D)
    f = (a, b, c); seen = []
    for _ in range(10000):
        if reduced(*f, D): break
        f = step(*f, D)
    start = f; cyc = [f]
    while True:
        f = step(*f, D)
        if f == start: break
        cyc.append(f)
        assert len(cyc) < 10000
    k = min(range(len(cyc)), key=lambda i: cyc[i:] + cyc[:i]); canon = tuple(cyc[k:] + cyc[:k])
    return (t, canon)
def rot_class(w):
    return min(w[i:] + w[:i] for i in range(len(w)))
words = [w for n in range(2, LMAX + 1) for w in ("".join(bits) for bits in __import__("itertools").product("RL", repeat=n)) if "R" in w and "L" in w]
inv = {w: cycle_invariant(matrix(w)) for w in words}; rc = {w: rot_class(w) for w in words}
by_rot = {}; by_inv = {}
for w in words: by_rot.setdefault(rc[w], set()).add(inv[w]); by_inv.setdefault(inv[w], set()).add(rc[w])
rot_consistent = all(len(v) == 1 for v in by_rot.values())          # rotations share the invariant (conjugate => same cycle)
inv_separates = all(len(v) == 1 for v in by_inv.values())           # same invariant => same rotation class (the bridge)
t18 = [w for w in words if sum(matrix(w)[i][i] for i in range(2)) == 18]
print(f"words (length 2..{LMAX}, mixed): {len(words)}; rotation classes: {len(by_rot)}; distinct invariants: {len(by_inv)}")
print(f"rotations share their invariant: {rot_consistent}; the invariant separates rotation classes: {inv_separates}")
print(f"trace-18 words: {len(t18)} in {len({rc[w] for w in t18})} rotation classes with {len({inv[w] for w in t18})} invariants (B8083: phi1^3 and phi4 both trace 18, not conjugate)")
ok = rot_consistent and inv_separates and len(by_rot) == len(by_inv)
json.dump(dict(LMAX=LMAX, words=len(words), rotation_classes=len(by_rot), invariants=len(by_inv), rot_consistent=rot_consistent, inv_separates=inv_separates, ok=ok), open("c_positivity_bridge.json", "w"), indent=1)
print("C3:", "PASS" if ok else "FAIL")
