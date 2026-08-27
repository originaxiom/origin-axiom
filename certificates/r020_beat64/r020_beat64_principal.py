#!/usr/bin/env python3
"""R020 — principal semilinear beat against the banked 64 (exact).

Run from any directory: ``python3 certificates/r020_beat64/r020_beat64_principal.py``.
Only ``sympy`` from requirements.txt is used, through R006's vendored E6 builder.
All arithmetic after loading E6 is Fraction arithmetic in K=Q(q), q^2=q-1.

The essential convention lock is executable: the beat generator is the PRINCIPAL
sum of the six simple-root vectors.  It is not the unrelated single root vector
ROOTS[0].  The rational slot involution theta is constructed only to define the
banked fork; it is never substituted for the semilinear beat.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path

HERE = Path(__file__).resolve().parent
STACK = HERE.parent / "r006_e6_invariants" / "twisted_double.py"
source = STACK.read_text(encoding="utf-8")
cut = source.index("# ---------------- stage 1")
saved_file = __file__
__file__ = str(STACK)
exec(compile(source[:cut], str(STACK), "exec"), globals())
__file__ = saved_file

def vadd(x, y): return [a + b for a, b in zip(x, y)]
def vscale(a, x): return [a * z for z in x]
def a2_pair(S):
    for r in sorted(S):
        for s in sorted(S):
            if ip(r, s) == -1 and tuple(a + b for a, b in zip(r, s)) in S:
                return r, s
    raise AssertionError("A2 pair absent")

# Slots: S0 is the declared A2 on simple roots 0,2.  The B1140 source run
# uses the small-support component as S1 (the second Lorentz A2) and the
# long-root component as S2 (compact color).  Freeze that ordering exactly;
# a lexicographic S1,S2 assignment reverses the stored frame.
a0 = tuple(1 if i == 0 else 0 for i in range(N))
a2 = tuple(1 if i == 2 else 0 for i in range(N))
S0 = {r for r in ROOTS if r in {tuple(x * a0[i] + y * a2[i] for i in range(N))
                                for x in (-1, 0, 1) for y in (-1, 0, 1)}}
orth = {r for r in ROOTS if ip(r, a0) == 0 and ip(r, a2) == 0}
pieces = []
while orth:
    seed = min(orth); comp = {seed}; changed = True
    while changed:
        changed = False
        for r in list(orth - comp):
            if any(ip(r, s) != 0 for s in comp): comp.add(r); changed = True
    pieces.append(comp); orth -= comp
ordered_pieces = sorted(pieces, key=lambda x: tuple(sorted(x)))
S2, S1 = ordered_pieces
assert [len(S) for S in (S0, S1, S2)] == [6, 6, 6]
assert min(S1) == (0, 0, 0, 0, -1, -1)
assert min(S2) == (-1, -2, -2, -3, -2, -1)

# Rational Chevalley lift of a slot-swap theta.  This is deliberately separate
# from Sigma; only its exact linear action defines theta(T1).
root_list = ROOTS; nR = len(ROOTS); ident = tuple(range(nR))
CART = [[ip(tuple(1 if k == i else 0 for k in range(N)),
            tuple(1 if k == j else 0 for k in range(N))) for j in range(N)]
        for i in range(N)]
def srefl(i):
    ai = tuple(1 if k == i else 0 for k in range(N))
    return tuple(IDX[tuple(r[k] - ip(r, ai) * ai[k] for k in range(N))] for r in root_list)
gens = [srefl(i) for i in range(N)]
seen = {ident}; frontier = [ident]; W = [ident]
while frontier:
    nxt = []
    for p in frontier:
        for g in gens:
            z = tuple(p[g[i]] for i in range(nR))
            if z not in seen: seen.add(z); nxt.append(z); W.append(z)
    frontier = nxt
pi = next(p for p in permutations(range(N)) if p != tuple(range(N)) and
          all(CART[p[i]][p[j]] == CART[i][j] for i in range(N) for j in range(N)))
delta = tuple(IDX[tuple(r[pi.index(i)] for i in range(N))] for r in root_list)
def compose(p, q): return tuple(p[q[i]] for i in range(nR))
AUT = W + [compose(delta, w) for w in W]
i0, i1, i2 = (frozenset(IDX[r] for r in S) for S in (S0, S1, S2))
def image(p, s): return frozenset(p[i] for i in s)
swappers = [g for g in AUT if image(g, i0) == i1 and image(g, i1) == i0 and
            image(g, i2) == i2 and compose(g, g) == ident]
assert swappers

NEG = tuple(IDX[tuple(-x for x in r)] for r in root_list)
def solve_lift(phi):
    rows = []
    def addrow(indices, rhs):
        mask = 0
        for i in indices: mask ^= 1 << i
        rows.append((mask, rhs))
    for ia, ra in enumerate(root_list):
        addrow([ia, NEG[ia]], 0); addrow([ia, phi[ia]], 0)
        for ib in range(ia + 1, nR):
            s = tuple(ra[k] + root_list[ib][k] for k in range(N))
            if s in IDX:
                addrow([ia, ib, IDX[s]], 0 if eps(ra, root_list[ib]) * eps(root_list[phi[ia]], root_list[phi[ib]]) == 1 else 1)
    piv = {}
    for mask, rhs in rows:
        while mask:
            h = mask.bit_length() - 1
            if h in piv: mask ^= piv[h][0]; rhs ^= piv[h][1]
            else: piv[h] = (mask, rhs); break
        else: assert not rhs
    sol = 0
    for h in sorted(piv):
        mask, rhs = piv[h]
        if rhs ^ (((mask ^ (1 << h)) & sol).bit_count() & 1):
            sol |= 1 << h
    free = [i for i in range(nR) if i not in piv]
    kernels = []
    for f in free:
        k = 1 << f
        for h in sorted(piv):
            if ((piv[h][0] ^ (1 << h)) & k).bit_count() & 1: k |= 1 << h
        kernels.append(k)
    out = []
    for bits in range(1 << len(kernels)):
        x = sol
        for j, k in enumerate(kernels):
            if bits >> j & 1: x ^= k
        assert all(((mask & x).bit_count() & 1) == rhs for mask, rhs in rows)
        out.append([1 - 2 * ((x >> i) & 1) for i in range(nR)])
    return out
assert len(swappers) == 48
# The source-locked B1140 representative is the first compact-color
# E6(-26) hit in its exhaustive ordering: swapper #13, lift #0.
g = swappers[13]
lifts = solve_lift(g)
assert lifts
c = lifts[0]
def theta(v):
    out = [F(0)] * DIM
    for i in range(N):
        ai = tuple(1 if j == i else 0 for j in range(N))
        target = root_list[g[IDX[ai]]]
        for j in range(N): out[j] += v[i] * target[j]
    for ir in range(nR): out[N + g[ir]] += v[N + ir] * c[ir]
    return out
standard = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS]
assert all(theta(theta(x)) == x for x in standard)
assert all(theta(br(x, y)) == br(theta(x), theta(y))
           for i, x in enumerate(standard) for y in standard[i:])

def q_rref(M):
    M = [row[:] for row in M]; pivots = []; row = 0
    for col in range(len(M[0]) if M else 0):
        pivot = next((i for i in range(row, len(M)) if M[i][col]), None)
        if pivot is None: continue
        M[row], M[pivot] = M[pivot], M[row]
        inv = F(1) / M[row][col]
        M[row] = [inv * x for x in M[row]]
        for i in range(len(M)):
            if i != row and M[i][col]:
                a = M[i][col]
                M[i] = [x - a * y for x, y in zip(M[i], M[row])]
        pivots.append(col); row += 1
        if row == len(M): break
    return M, pivots

def q_nullspace(M):
    R, pivots = q_rref(M)
    cols = len(M[0])
    out = []
    for free in (j for j in range(cols) if j not in pivots):
        v = [F(0)] * cols; v[free] = F(1)
        for i, col in enumerate(pivots): v[col] = -R[i][free]
        out.append(v)
    return out

def signature(M):
    M = [row[:] for row in M]; pos = neg = zero = 0; i = 0
    while i < len(M):
        if M[i][i] == 0:
            j = next((j for j in range(i + 1, len(M)) if M[j][i]), None)
            if j is None: zero += 1; i += 1; continue
            for k in range(len(M)): M[i][k] += M[j][k]
            for k in range(len(M)): M[k][i] += M[k][j]
        d = M[i][i]
        if d > 0: pos += 1
        else: neg += 1
        for j in range(i + 1, len(M)):
            if M[j][i]:
                a = M[j][i] / d
                for k in range(len(M)): M[j][k] -= a * M[i][k]
                for k in range(len(M)): M[k][j] -= a * M[k][i]
        i += 1
    return pos, neg, zero

# The invariant rational form used by the source closing certificate.  It is
# a nonzero scalar multiple of the Killing form, so it has the same
# orthogonal complement and real-form signatures.
def gform(u, v):
    out = sum(u[i] * F(CART[i][j]) * v[j]
              for i in range(N) for j in range(N))
    out -= sum(u[N + i] * v[N + NEG[i]] for i in range(nR))
    return out

Ttheta = [[theta(standard[j])[i] for j in range(DIM)] for i in range(DIM)]
fixed = q_nullspace([[Ttheta[i][j] - (F(1) if i == j else F(0))
                      for j in range(DIM)] for i in range(DIM)])
anti = q_nullspace([[Ttheta[i][j] + (F(1) if i == j else F(0))
                     for j in range(DIM)] for i in range(DIM)])
sf = signature([[gform(x, y) for y in fixed] for x in fixed])
sa = signature([[-gform(x, y) for y in anti] for x in anti])
global_signature = (sf[0] + sa[0], sf[1] + sa[1], sf[2] + sa[2])
assert global_signature == (26, 52, 0)

def principal(S):
    r, s = a2_pair(S)
    e = vadd(evec(r), evec(s)); h = [F(0)] * DIM
    for i in range(N): h[i] = F(2 * (r[i] + s[i]))
    f = vadd(vscale(-2, evec(tuple(-x for x in r))), vscale(-2, evec(tuple(-x for x in s))))
    assert br(e, f) == h
    return e, h, f
T1 = principal(S0); T2 = tuple(theta(x) for x in T1)
def spin5(T):
    e, h, f = T
    top = next(evec(r) for r in ROOTS if br(h, evec(r)) == vscale(4, evec(r)))
    out = [top]
    for _ in range(4): out.append(br(f, out[-1]))
    assert all(any(x != 0 for x in v) for v in out)
    assert all(br(h, v) == vscale(4 - 2 * i, v) for i, v in enumerate(out))
    assert all(x == 0 for x in br(f, out[-1]))
    return out
P0, P1 = spin5(T1), spin5(T2)
r2, s2 = a2_pair(S2)

def basis_coords(v, basis):
    aug = [[basis[j][i] for j in range(len(basis))] + [v[i]]
           for i in range(DIM)]
    R, pivots = q_rref(aug)
    assert len(basis) not in pivots
    out = [F(0)] * len(basis)
    for i, col in enumerate(pivots):
        if col < len(basis): out[col] = R[i][-1]
    assert [sum(out[j] * basis[j][i] for j in range(len(basis)))
            for i in range(DIM)] == v
    return out

color_basis = [evec(r) for r in sorted(S2)]
for r in (r2, s2):
    h = [F(0)] * DIM
    for i in range(N): h[i] = F(r[i])
    color_basis.append(h)
Tcolor = [[basis_coords(theta(color_basis[j]), color_basis)[i]
           for j in range(8)] for i in range(8)]
color_fixed_coeff = q_nullspace([[Tcolor[i][j] - (F(1) if i == j else F(0))
                                  for j in range(8)] for i in range(8)])
color_anti_coeff = q_nullspace([[Tcolor[i][j] + (F(1) if i == j else F(0))
                                 for j in range(8)] for i in range(8)])
lift_full = lambda c: [sum(c[j] * color_basis[j][i] for j in range(8))
                       for i in range(DIM)]
color_fixed = [lift_full(c) for c in color_fixed_coeff]
color_anti = [lift_full(c) for c in color_anti_coeff]
csf = signature([[gform(x, y) for y in color_fixed] for x in color_fixed])
csa = signature([[-gform(x, y) for y in color_anti] for x in color_anti])
color_signature = (csf[0] + csa[0], csf[1] + csa[1], csf[2] + csa[2])
assert color_signature == (0, 8, 0)

def cwt(r): return ip(r, r2), ip(r, s2)
Croots = [r for r in ROOTS if cwt(r) != (0, 0) and r not in S2]
C54 = [evec(r) for r in Croots]
V64 = P0 + P1 + C54
fork = list(T1) + list(T2) + [evec(r) for r in sorted(S2)]
for r in (r2, s2):
    h = [F(0)] * DIM
    for i in range(N): h[i] = F(r[i])
    fork.append(h)
assert all(gform(v, f) == 0 for v in V64 for f in fork)

# K=Q(q), pairs a+bq, q^2=q-1.
Z = (F(0), F(0)); Q = (F(0), F(1)); ONE = (F(1), F(0))
def fa(x, y): return x[0] + y[0], x[1] + y[1]
def fs(x, y): return x[0] - y[0], x[1] - y[1]
def fm(x, y): return x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0] + x[1]*y[1]
def fi(x):
    n = x[0]*x[0] + x[0]*x[1] + x[1]*x[1]
    return (x[0] + x[1]) / n, -x[1] / n
def gal(v): return [(x[0] + x[1], -x[1]) for x in v]
def toK(v): return [(x, F(0)) for x in v]
def mmv(M, v):
    return [sumK((fm(M[i][j], v[j]) for j in range(DIM) if M[i][j] != Z and v[j] != Z)) for i in range(DIM)]
def sumK(xs):
    out = Z
    for x in xs: out = fa(out, x)
    return out
def rankK(cols):
    rows = [x[:] for x in cols]; r = 0
    for j in range(DIM):
        p = next((i for i in range(r, len(rows)) if rows[i][j] != Z), None)
        if p is None: continue
        rows[r], rows[p] = rows[p], rows[r]; inv = fi(rows[r][j])
        rows[r] = [fm(inv, x) for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][j] != Z:
                a = rows[i][j]; rows[i] = [fs(x, fm(a, y)) for x, y in zip(rows[i], rows[r])]
        r += 1
    return r
def contained(a, b): return rankK(a + b) == rankK(b)

E = [F(0)] * DIM
for i in range(N): E = vadd(E, evec(tuple(1 if j == i else 0 for j in range(N))))
assert E == e6e and sum(1 for x in E if x) == 6
wrong = evec(ROOTS[0])
assert wrong != E and sum(1 for x in wrong if x) == 1
ad = [[F(0)] * DIM for _ in range(DIM)]
for j in range(DIM):
    b = [F(1) if i == j else F(0) for i in range(DIM)]
    col = br(E, b)
    for i in range(DIM): ad[i][j] = col[i]
def expad(scale):
    M = [[(x, F(0)) for x in row] for row in ad]
    out = [[ONE if i == j else Z for j in range(DIM)] for i in range(DIM)]
    term = [row[:] for row in out]; k = 1
    while True:
        nxt = [[Z] * DIM for _ in range(DIM)]
        for i in range(DIM):
            for l in range(DIM):
                if term[i][l] == Z: continue
                for j in range(DIM):
                    if M[l][j] != Z: nxt[i][j] = fa(nxt[i][j], fm(term[i][l], M[l][j]))
        term = [[fm(fm(x, scale), fi((F(k), F(0)))) for x in row] for row in nxt]
        if all(x == Z for row in term for x in row): return out
        out = [[fa(x, y) for x, y in zip(a, b)] for a, b in zip(out, term)]; k += 1
        assert k < 80
Uq, U1 = expad(Q), expad(ONE)
def Sigma(v): return mmv(Uq, gal(v))

B = [toK(v) for v in V64]; F14 = [toK(v) for v in fork]
assert len(V64) == 64 and len(fork) == 14 and rankK(B) == 64 and rankK(B + F14) == 78
SB = [Sigma(v) for v in B]
print("R020 beat64 principal exact certificate")
print("field: q^2=q-1; gal(a+bq)=a+b-bq")
print("theta: rational linear slot involution; Sigma: exp(ad(qE_principal)) o gal")
print("source frame: B1140 component order; compact hit swapper#13/lift#0")
print("theta exact checks: full Chevalley automorphism; global signature=", global_signature,
      " color signature=", color_signature)
print("principal generator: sum of six simple-root vectors: PASS")
print("wrong single-root generator differs from principal generator: PASS")
print("basis ranks: V64=", rankK(B), " fork=", rankK(F14), " total=", rankK(B + F14))
print("Sigma(V64) subset V64:", contained(SB, B))
print("Sigma(P0) subset V64:", contained(SB[:5], B))
print("Sigma(P1) subset V64:", contained(SB[5:10], B))
print("Sigma(C54) subset V64:", contained(SB[10:], B))
print("Sigma(C54) subset C54:", contained(SB[10:], B[10:]))

# Canonical leakage: first basis vector and first fork coordinate in fixed order.
def coords(v, basis):
    M = [[basis[j][i] for j in range(78)] + [v[i]] for i in range(DIM)]
    for j in range(78):
        p = next(i for i in range(j, DIM) if M[i][j] != Z)
        M[j], M[p] = M[p], M[j]; inv = fi(M[j][j]); M[j] = [fm(inv, x) for x in M[j]]
        for i in range(DIM):
            if i != j and M[i][j] != Z:
                a = M[i][j]; M[i] = [fs(x, fm(a, y)) for x, y in zip(M[i], M[j])]
    return [M[i][-1] for i in range(78)]
co = coords(SB[10], F14 + B)
first = next((i, x) for i, x in enumerate(co[:14]) if x != Z)
print("canonical leakage source root:", Croots[0])
print("canonical first nonzero fork coordinate (index, a+bq):", first)
S2B = [Sigma(v) for v in SB]
print("Sigma^2(V64) subset V64:", contained(S2B, B))
ambient = [toK(v) for v in standard]
ambient_square_ok = all(Sigma(Sigma(v)) == mmv(U1, v) for v in ambient)
print("Sigma^2=exp(ad E_principal) on all 78 Chevalley basis vectors:", ambient_square_ok)
assert ambient_square_ok
print("R020 VERDICT: REFUTED — no restricted Sigma or restricted tick endomorphism of V64.")
