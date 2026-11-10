#!/usr/bin/env python3
"""Two acts or one tick: what the tick adds, exactly (data-free; integers, and SnapPy for the manifolds).

Two acts:  L = [[1,1],[0,1]], R = [[1,0],[1,1]]; a history is a cyclic word in L and R.
One tick:  T_m = L^m P = [[m,1],[1,0]] ("add m times, then the two sides change roles"), P the exchange. A history is a
           cyclic sequence of positive integers (m_1 .. m_k); since P L^m P = R^m, an even k gives the two-act word
           L^m1 R^m2 ..., and an odd k gives L^m1 R^m2 .. L^mk P, of determinant -1.
    python3 relays/advisor_2026-11-10_audit/principle_top_down/the_tick/tick_facts.py"""
import itertools, math, warnings
warnings.filterwarnings("ignore")
I2 = ((1, 0), (0, 1)); L = ((1, 1), (0, 1)); R = ((1, 0), (1, 1)); P = ((0, 1), (1, 0)); F = ((1, 1), (1, 0))
mul = lambda A, B, N=None: tuple(tuple((sum(A[i][k] * B[k][j] for k in range(2)) % N) if N else sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def gen(gens, N):
    G = {tuple(tuple(x % N for x in r) for r in I2)}; frontier = list(G)
    gens = [tuple(tuple(x % N for x in r) for r in g) for g in gens]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                x = mul(g, h, N)
                if x not in G: G.add(x); nxt.append(x)
        frontier = nxt
    return G
out = []
# ---- T3: the levels
out.append("T3  the exchange at the levels")
for N in (2, 3, 4, 5, 7, 8):
    two, tick = gen([L, R], N), gen([L, P], N)
    out.append("    N = %d: |<L,R>| = %-5d |<L,P>| = %-5d ratio %d   exchange already inside <L,R>: %s" % (
        N, len(two), len(tick), len(tick) // len(two), tuple(tuple(x % N for x in r) for r in P) in two))
F5 = tuple(tuple(x % 5 for x in r) for r in F)
v = (1, 2); Fv = ((F[0][0] * v[0] + F[0][1] * v[1]) % 5, (F[1][0] * v[0] + F[1][1] * v[1]) % 5)
out.append("    the tick mod 5: F (1,2) = %s = 3 * (1,2): %s;  F^2 = LR: %s;  (F - 3)^2 = 0 mod 5: %s" % (
    Fv, Fv == ((3 * v[0]) % 5, (3 * v[1]) % 5), mul(F, F) == mul(L, R),
    mul(tuple(tuple((F[i][j] - 3 * I2[i][j]) % 5 for j in range(2)) for i in range(2)), tuple(tuple((F[i][j] - 3 * I2[i][j]) % 5 for j in range(2)) for i in range(2)), 5) == ((0, 0), (0, 0))))
orbit = [v]
while True:
    w = ((F[0][0] * orbit[-1][0] + F[0][1] * orbit[-1][1]) % 5, (F[1][0] * orbit[-1][0] + F[1][1] * orbit[-1][1]) % 5)
    if w == v: break
    orbit.append(w)
pm = lambda u: min(u, ((-u[0]) % 5, (-u[1]) % 5))
out.append("    orbit of (1,2) under the tick: %s -- as points up to sign: %s" % (orbit, [pm(u) for u in orbit]))
det = lambda M: M[0][0] * M[1][1] - M[0][1] * M[1][0]
sub = lambda M, c: tuple(tuple(M[i][j] - c * I2[i][j] for j in range(2)) for i in range(2))
out.append("    fibre characters fixed by the tick: |det(F - I)| = %d; sent to their inverse: |det(F + I)| = %d;  by two ticks: %d and %d" % (
    abs(det(sub(F, 1))), abs(det(sub(F, -1))), abs(det(sub(mul(F, F), 1))), abs(det(sub(mul(F, F), -1)))))
# ---- T4: which single act survives alone (clause 3: the subtraction of the two sides never ends)
out.append("T4  a single act alone: fixed direction rational (the subtraction ends) or not")
for name, M in (("L", L), ("R", R), ("the exchange P", P), ("the tick F = LP", F)):
    t, d = M[0][0] + M[1][1], det(M); disc = t * t - 4 * d
    r = math.isqrt(disc) if disc >= 0 else -1
    out.append("    %-16s trace %d det %2d discriminant %d -> fixed direction %s" % (name, t, d, disc, "rational: it ends" if r * r == disc else "irrational: it never ends"))
# ---- T1: what exists under each grammar (cyclic sequences of run lengths, by number of letters)
def necklaces(n):
    seen = set(); res = []
    def comps(n):
        if n == 0: yield (); return
        for r in range(1, n + 1):
            for rest in comps(n - r): yield (r,) + rest
    for c in comps(n):
        rots = [c[i:] + c[:i] for i in range(len(c))]
        key = min(rots)
        if key in seen: continue
        seen.add(key)
        prim = all(c != c[:d] * (len(c) // d) for d in range(1, len(c)) if len(c) % d == 0)
        res.append((key, prim))
    return res
out.append("T1  cyclic sequences of run lengths with n letters in all (primitive ones): an even number of runs / an odd number")
for n in range(1, 13):
    nk = [k for k, prim in necklaces(n) if prim]
    out.append("    n = %2d: even %-4d odd %-4d" % (n, sum(1 for k in nk if len(k) % 2 == 0), sum(1 for k in nk if len(k) % 2 == 1)))
# ---- T2: handedness (SnapPy)
try:
    import snappy
    def word(seq): return "".join(("L" if i % 2 == 0 else "R") * m for i, m in enumerate(seq))
    def predicted_amph(seq):
        k = len(seq)
        if any(seq[s:] + seq[:s] == seq for s in range(1, k, 2)): return "odd rotation"
        rev = seq[::-1]
        if any(rev[s:] + rev[:s] == seq and (k - 1 - s) % 2 == 1 for s in range(k)): return "parity-changing reflection"
        return None
    out.append("T2  handedness of the two-act histories with at most 8 letters (SnapPy), against the combinatorial prediction")
    tot = agree = 0; classes = {"double of an odd sequence": [0, 0], "its own mirror another way": [0, 0], "has a mirror partner": [0, 0]}
    bad = []
    for n in range(2, 9):
        for seq, prim in necklaces(n):
            if not prim or len(seq) % 2: continue
            k = len(seq)
            # the two-act word class is the sequence up to EVEN rotation; an odd rotation is the mirror. Take each even-rotation class once.
            evenrots = {seq[s:] + seq[:s] for s in range(0, k, 2)}
            for rep in sorted({min(evenrots), min({seq[s:] + seq[:s] for s in range(1, k, 2)})}):
                M = snappy.Manifold("b++" + word(rep)); G = M.symmetry_group()
                amph = bool(G.is_amphicheiral()); pred = predicted_amph(rep)
                half = k // 2
                dbl = (half % 2 == 1) and rep[:half] == rep[half:]
                cls = "double of an odd sequence" if dbl else ("its own mirror another way" if pred else "has a mirror partner")
                classes[cls][0] += 1; classes[cls][1] += amph
                tot += 1; agree += (amph == bool(pred))
                if amph != bool(pred): bad.append((rep, amph, pred))
    out.append("    histories checked: %d; SnapPy agrees with the prediction on %d; disagreements: %s" % (tot, agree, bad[:5]))
    for c, (a, b) in classes.items(): out.append("    %-28s %3d histories, %3d amphicheiral" % (c, a, b))
    out.append("T2b the histories with an odd number of runs (the tick's own), at most 5 letters")
    for n in range(1, 6):
        for seq, prim in necklaces(n):
            if not prim or len(seq) % 2 == 0: continue
            try:
                M = snappy.Manifold("b-+" + word(seq)); C = M.orientation_cover(); D2 = snappy.Manifold("b++" + word(seq + seq))
                out.append("    %-12s b-+%-6s orientable %s  volume %.6f  H1 %-12s orientation cover = b++%s: %s" % (
                    seq, word(seq), M.is_orientable(), float(M.volume()), M.homology(), word(seq + seq), bool(C.is_isometric_to(D2))))
            except Exception as exc:
                out.append("    %-12s SnapPy: %r" % (seq, repr(exc)[:60]))
except ImportError:
    out.append("T2  skipped: SnapPy not available")
print("\n".join(out))
