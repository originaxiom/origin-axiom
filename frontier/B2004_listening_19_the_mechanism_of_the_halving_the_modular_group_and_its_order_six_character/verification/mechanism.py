"""B2004, listening card 19 (main, 2026-11-25; data-free): the mechanism of the halving.
K1: sigma = R C^-1 is an involution, R = sigma C, L = sigma C^2, X = C sigma C (sympy); W = T - D exactly as integer matrices,
    W|neutral = 6 Pi0 Psig Pi0, W|charged = -3 Piq Psig Piq (numerically, to 1e-12).
K2, K3: every reduced word in C^{+-1} and sigma of length <= 10: fixed points on the orbit, rho(word) (rho(C) = omega,
    rho(sigma) = -1), class of its cyclic reduction.
    python3 -B mechanism.py > mechanism_run.txt"""
import itertools
import numpy as np, sympy as sp
x, y, z = sp.symbols("x y z")
def comp(f, g): return tuple(sp.expand(e.subs({x: g[0], y: g[1], z: g[2]}, simultaneous=True)) for e in f)
L = (x, z, x*z - y); R = (z, y, y*z - x); C = (y, z, x); Ci = (z, x, y); X = comp(C, comp(L, Ci))
sig = comp(R, Ci)
print("K1 (sympy): sigma = R C^-1 = %s; sigma^2 = id: %s; R = sigma C: %s; L = sigma C^2: %s; X = C L C^-1 = C sigma C: %s" % (
    sig, comp(sig, sig) == (x, y, z), comp(sig, C) == R, comp(sig, comp(C, C)) == L, comp(C, comp(sig, C)) == X))
def orbit(N, start):
    Lf = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N); Rf = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Lif = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1]); Rif = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    if start is None:
        pts = [(a, b, c) for a in range(N) for b in range(N) for c in range(N) if (a*a + b*b + c*c - a*b*c) % N == 0 and (a, b, c) != (0, 0, 0)]
    else:
        seen, todo = {start}, [start]
        while todo:
            v = todo.pop()
            for g in (Lf, Rf, Lif, Rif):
                u = g(v)
                if u not in seen: seen.add(u); todo.append(u)
        pts = sorted(seen)
    idx = {v: i for i, v in enumerate(pts)}
    pC = np.array([idx[(v[1], v[2], v[0])] for v in pts]); pS = np.array([idx[(v[1], v[0], (v[0] * v[1] - v[2]) % N)] for v in pts])
    moves = [Lf, Rf, Lif, Rif, lambda v: (v[1], (v[1] * v[2] - v[0]) % N, v[2]), lambda v: ((v[0] * v[2] - v[1]) % N, v[0], v[2])]   # X^-1 = C^2 R C^-2 = (xz - y, x, z) (B2001's sympy); first written wrongly as (yz - x, x, z), caught by a KeyError before any output, fixed
    return pts, idx, pC, pS, moves
def Pm(p):
    n = len(p); M = np.zeros((n, n), dtype=np.int64); M[p, np.arange(n)] = 1; return M
def k1(N, start, lab):
    pts, idx, pC, pS, moves = orbit(N, start); n = len(pts)
    W = np.zeros((n, n), dtype=np.int64)
    for v in pts:
        for m in moves: W[idx[m(v)], idx[v]] += 1
    PC, PS = Pm(pC), Pm(pS); I = np.eye(n, dtype=np.int64); PCi = PC.T
    J = I + PC + PCi; T = J @ PS @ J; D = PS + PC @ PS @ PCi + PCi @ PS @ PC
    w = np.exp(2j * np.pi / 3)
    Pi = [(I + (w ** (-q)) * PC + (w ** (-2 * q)) * (PC @ PC)) / 3 for q in range(3)]
    e0 = np.abs(Pi[0] @ W @ Pi[0] - 6 * Pi[0] @ PS @ Pi[0]).max(); e1 = np.abs(Pi[1] @ W @ Pi[1] - (-3) * Pi[1] @ PS @ Pi[1]).max()
    print("K1 (%s, %d points): sigma an involution on the orbit: %s; W == T - D exactly: %s; |W|0 - 6 Pi0 Ps Pi0| = %.1e; |W|1 + 3 Pi1 Ps Pi1| = %.1e" % (
        lab, n, bool(np.all(pS[pS] == np.arange(n))), bool(np.array_equal(W, T - D)), e0, e1))
    return pts, pC, pS
def words(maxlen):
    out = []
    def ext(w):
        if w: out.append(tuple(w))
        if len(w) == maxlen: return
        last = w[-1] if w else None
        for a in ("s", "c", "C"):
            if last is None or (a == "s") != (last == "s"):
                ext(w + [a])
    ext([]); return out
def rho_exp(w): return (sum(2 for a in w if a == "c") + sum(4 for a in w if a == "C") + sum(3 for a in w if a == "s")) % 6
def cyc_class(w):
    w = list(w)
    def merge(a, b):   # combine two C-letters
        e = (1 if a == "c" else 2) + (1 if b == "c" else 2)
        return None if e % 3 == 0 else ("c" if e % 3 == 1 else "C")
    changed = True
    while changed and len(w) > 1:
        changed = False
        a, b = w[0], w[-1]
        if a == "s" and b == "s": w = w[1:-1]; changed = True
        elif a != "s" and b != "s":
            m = merge(a, b); w = w[1:-1] if m is None else [m] + w[1:-1]; changed = True
    if not w: return "identity"
    if len(w) == 1: return "conjugate of C^+-1" if w[0] != "s" else "conjugate of sigma"
    return "other"
WORDS = words(10)
print("census: %d reduced words of length 1 to 10" % len(WORDS))
def census(N, start, lab):
    pts, pC, pS = k1(N, start, lab); n = len(pts)
    pCC = pC[pC]; perm = {"s": pS, "c": pC, "C": pCC}
    stats = {}; examples = {}
    for w in WORDS:
        p = np.arange(n)
        for a in reversed(w): p = perm[a][p]     # the map w = a1 a2 ... applied right to left
        f = int(np.sum(p == np.arange(n))); e = rho_exp(w); cl = cyc_class(w)
        if e != 0 and f > 0:
            key = cl; stats.setdefault(key, set()).add(f)
            if cl != "conjugate of C^+-1": examples.setdefault(key, []).append(("".join(w), f))
    print("  %s: words outside the commutator subgroup with fixed points, by class of the cyclic reduction (fixed-point counts seen): %s" % (lab, {k: sorted(v) for k, v in stats.items()}))
    for k, ex in examples.items(): print("    examples (%s): %s" % (k, ex[:4]))
    return stats
res = {}
for N, start, lab in ((27, (3, 3, 3), "mod 27, orbit of (3,3,3)"), (81, (3, 3, 3), "mod 81, orbit of (3,3,3)"), (9, (3, 3, 3), "mod 9, orbit of (3,3,3)"),
                      (25, (3, 3, 3), "mod 25, orbit of (3,3,3)"), (5, None, "mod 5, leaf"), (7, None, "mod 7, leaf")):
    res[lab] = census(N, start, lab)
ok2 = all(set(res[l].keys()) == {"conjugate of C^+-1"} and res[l]["conjugate of C^+-1"] == {3} for l in ("mod 27, orbit of (3,3,3)", "mod 81, orbit of (3,3,3)"))
ok3 = all(any(k != "conjugate of C^+-1" for k in res[l]) for l in ("mod 9, orbit of (3,3,3)", "mod 25, orbit of (3,3,3)", "mod 5, leaf", "mod 7, leaf"))
print("SUMMARY K2: on the 3-tower only conjugates of C^+-1 fix points outside the commutator subgroup, three each: %s" % ok2)
print("SUMMARY K3: at mod 9, 25, 5, 7 some other word outside it fixes a point: %s" % ok3)
