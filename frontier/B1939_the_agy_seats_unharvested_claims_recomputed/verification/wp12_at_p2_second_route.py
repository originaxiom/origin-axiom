#!/usr/bin/env python3
"""Independent adversarial re-check of the WP-1.2 (p = 2) report. Written from scratch; imports no repository or prior code.
Words are strings over 'aAbB' (A = a^-1, B = b^-1). Exact arithmetic only (ints, Gaussian-int pairs, sympy rationals/I).
Definitions: EXPECTATIONS.md in this folder."""
import sys, json
from collections import Counter, deque
import sympy as sp

OUT = {"checks": [], "plants": []}
def chk(name, ok, det=""):
    OUT["checks"].append([name, bool(ok), str(det)[:400]]); print(("PASS " if ok else "FAIL ") + name + ("  | " + str(det)[:300] if det != "" else ""))
    return bool(ok)
def plant(name, check_value, det=""):
    caught = not check_value
    OUT["plants"].append([name, caught, str(det)[:400]]); print(("CAUGHT " if caught else "MISSED ") + "PLANT " + name + ("  | " + str(det)[:300] if det != "" else ""))

INV = {"a": "A", "A": "a", "b": "B", "B": "b"}
def red(w):
    st = []
    for c in w:
        if st and st[-1] == INV[c]: st.pop()
        else: st.append(c)
    return "".join(st)
def winv(w): return "".join(INV[c] for c in reversed(w))
def cred(w):
    w = red(w)
    i, j = 0, len(w)
    while j - i >= 2 and w[i] == INV[w[j - 1]]: i += 1; j -= 1
    return w[i:j]
def conj(u, v):
    u, v = cred(u), cred(v)
    return len(u) == len(v) and (u == v == "" or v in u + u)
def canon(w):
    c = cred(w)
    return min((c[k:] + c[:k] for k in range(len(c))), default="")

def words_by_bfs(n, start_len=0):
    """Reduced words of length start_len..n, generated level by level (BFS)."""
    out, level = [], [""]
    for L in range(0, n + 1):
        if L >= start_len: out.extend(level)
        level = [w + c for w in level for c in "aAbB" if not (w and w[-1] == INV[c])]
    return out

def move(ia, ib):
    T = {"a": ia, "A": winv(ia), "b": ib, "B": winv(ib)}
    return lambda w: red("".join(T[c] for c in w))
MOVES = {"R1 a->ab": move("ab", "b"), "R2 a->ba": move("ba", "b"), "R3 b->ba": move("a", "ba"), "R4 b->ab": move("a", "ab"),
         "S swap": move("b", "a"), "T tick": move("ab", "a")}
IMAGES = {"R1 a->ab": ("ab", "b"), "R2 a->ba": ("ba", "b"), "R3 b->ba": ("a", "ba"), "R4 b->ab": ("a", "ab"),
          "S swap": ("b", "a"), "T tick": ("ab", "a")}
REC = ["R1 a->ab", "R2 a->ba", "R3 b->ba", "R4 b->ab"]
C = "abAB"

# ------------------------------------------------------------------ (1) statement B
def kept_classes(start_len=0, conjtest=conj, moves=REC):
    reps = {}
    for w in words_by_bfs(8, start_len):
        reps.setdefault(canon(w), w)
    kept = sorted([c for c in reps if all(conjtest(MOVES[m](c), c) for m in moves)], key=lambda c: (len(c), c))
    return kept, reps
W8 = words_by_bfs(8)
chk("B: 13,121 reduced words of length <= 8", len(W8) == 13121, len(W8))
kept, reps = kept_classes()
OUT["n_classes_le8"] = len(reps)
chk("B: the 13,121 words fall into 1,387 conjugacy classes", len(reps) == 1387, len(reps))
# cross-check class count by Burnside on cyclically reduced words of each length
def n_cyc_red(n): return sum(1 for w in words_by_bfs(n, n) if cred(w) == w)
from math import gcd
def n_necklaces(n):
    # count classes of cyclically reduced words of length n by direct canon
    return len({canon(w) for w in words_by_bfs(n, n) if cred(w) == w})
tot = 1 + sum(n_necklaces(n) for n in range(1, 9))
chk("B: class count re-derived from cyclically reduced words by length", tot == len(reps), tot)
expected5 = sorted({canon(""), canon(C), canon(winv(C)), canon(C + C), canon(winv(C) * 2)}, key=lambda c: (len(c), c))
chk("B: classes kept by all four record moves, empty word included: exactly 1, [a,b]^{+-1}, [a,b]^{+-2}", kept == expected5, kept)
chk("B: non-empty: exactly four", [k for k in kept if k] == [k for k in expected5 if k] and len([k for k in kept if k]) == 4)
for m in REC: chk(f"B: {m} sends [a,b] to a conjugate of [a,b]", conj(MOVES[m](C), C), MOVES[m](C))
for m in ("S swap", "T tick"): chk(f"B: {m} sends [a,b] to a conjugate of [a,b]^-1 (not of [a,b])", conj(MOVES[m](C), winv(C)) and not conj(MOVES[m](C), C), MOVES[m](C))
k12, _ = kept_classes(moves=["R1 a->ab", "R2 a->ba"])
OUT["kept_under_R1_R2"] = len(k12); chk("B: 87 classes kept under {R1, R2} alone (relay's number)", len(k12) == 87, len(k12))
w, L = C, []
for _ in range(5): L.append(len(w)); w = MOVES["R2 a->ba"](w)
chk("B: iterating a->ba on the word [a,b]: lengths 4,6,8,10,12", L == [4, 6, 8, 10, 12], L)
kP, _ = kept_classes(start_len=1); plant("P-1a enumeration from length 1 (empty word dropped); check 'five kept'", kP == expected5, kP)
nr = lambda u, v: cred(u) == cred(v)
kQ, _ = kept_classes(conjtest=nr); plant("P-1b conjugacy without rotation; check 'five kept'", kQ == expected5, kQ)

# ------------------------------------------------------------------ evaluators
def ev_factory(gen, mul, one):
    def ev_all(maxlen):
        """DFS over reduced words with prefix products: yields (word, value)."""
        st = [("", one)]
        while st:
            w, M = st.pop()
            yield w, M
            if len(w) < maxlen:
                for c in "aAbB":
                    if not (w and w[-1] == INV[c]): st.append((w + c, mul(M, gen[c])))
    def ev(w):
        M = one
        for c in w: M = mul(M, gen[c])
        return M
    return ev, ev_all
# integer matrices as tuples
def imul(M, N):
    n = len(M); return tuple(tuple(sum(M[i][k] * N[k][j] for k in range(n)) for j in range(n)) for i in range(n))
I2 = ((1, 0), (0, 1)); I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
# Heisenberg as triples
def hmul(p, q): return (p[0] + q[0], p[1] + q[1], p[2] + q[2] + p[0] * q[1])
HE = {"a": (1, 0, 0), "A": (-1, 0, 0), "b": (0, 1, 0), "B": (0, -1, 0)}
for c in "ab": assert hmul(HE[c], HE[c.upper()]) == (0, 0, 0) == hmul(HE[c.upper()], HE[c])
hev, hall = ev_factory(HE, hmul, (0, 0, 0))
# Heisenberg, lower unitriangular matrices (second evaluation)
HL = {"a": ((1, 0, 0), (1, 1, 0), (0, 0, 1)), "A": ((1, 0, 0), (-1, 1, 0), (0, 0, 1)),
      "b": ((1, 0, 0), (0, 1, 0), (0, 1, 1)), "B": ((1, 0, 0), (0, 1, 0), (0, -1, 1))}
hlev, hlall = ev_factory(HL, imul, I3)
# Hamilton quaternions on integer 4-tuples (w, x, y, z)
def qm(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1*a2 - b1*b2 - c1*c2 - d1*d2, a1*b2 + b1*a2 + c1*d2 - d1*c2, a1*c2 - b1*d2 + c1*a2 + d1*b2, a1*d2 + b1*c2 - c1*b2 + d1*a2)
QH = {"a": (0, 1, 0, 0), "A": (0, -1, 0, 0), "b": (0, 0, 1, 0), "B": (0, 0, -1, 0)}
qhev, qhall = ev_factory(QH, qm, (1, 0, 0, 0))
# statement C's matrices over Z[i] (pairs re, im)
def gmul(x, y): return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def gmm(M, N): return tuple(tuple(tuple(map(sum, zip(gmul(M[i][0], N[0][j]), gmul(M[i][1], N[1][j])))) for j in range(2)) for i in range(2))
z, o, mo, ii, mi = (0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)
GI = ((o, z), (z, o))
QM = {"a": ((ii, z), (z, mi)), "A": ((mi, z), (z, ii)), "b": ((z, o), (mo, z)), "B": ((z, mo), (o, z))}
for c in "ab": assert gmm(QM[c], QM[c.upper()]) == GI
qmev, qmall = ev_factory(QM, gmm, GI)
SAN = {"a": ((1, 2), (0, 1)), "A": ((1, -2), (0, 1)), "b": ((1, 0), (2, 1)), "B": ((1, 0), (-2, 1))}
sev, sall = ev_factory(SAN, imul, I2)

# ------------------------------------------------------------------ (2) statement C
chk("C: [a,b] = -I at the quaternion point (Z[i])", qmev(C) == ((mo, z), (z, mo)))
chk("C: traces of a, b, ab are 0", all((lambda M: (M[0][0][0] + M[1][1][0], M[0][0][1] + M[1][1][1]))(qmev(w)) == (0, 0) for w in ("a", "b", "ab")))
for g in "abAB":
    t = C + g + winv(C) + INV[g]
    chk(f"C: [[a,b],{g}] = 1 at Q8 and in H3(Z); [a,b] != 1 in H3", qmev(t) == GI and hev(t) == (0, 0, 0) and hev(C) != (0, 0, 0))
tc = sev(C + "a" + winv(C) + "A"); OUT["sanov_[[a,b],a]"] = tc
chk("C: [[a,b],a] at the Sanov pair is [[-335,1552],[-128,593]] (relay's matrix), not I", tc == ((-335, 1552), (-128, 593)), tc)
cS = Counter(len(w) for w, M in sall(8) if M == I2)
chk("C last clause LITERAL (empty word counted): no reduced word <= 8 trivial at Sanov  [expected to FAIL: objection (2)]", sum(cS.values()) == 0, dict(cS))
chk("C last clause with 'non-empty': none trivial at Sanov", sum(v for k, v in cS.items() if k) == 0, dict(cS))
PL = {"a": ((1, 1), (0, 1)), "A": ((1, -1), (0, 1)), "b": ((1, 0), (-1, 1)), "B": ((1, 0), (1, 1))}
_, pall = ev_factory(PL, imul, I2)
cP = Counter(len(w) for w, M in pall(8) if M == I2)
plant("P-2 non-free pair L, R^-1 in place of Sanov; check 'no non-empty word <= 8 trivial'", sum(v for k, v in cP.items() if k) == 0, dict(sorted(cP.items())))

# ------------------------------------------------------------------ (5) Heisenberg-trivial words
triv_h = [w for w, M in hall(10) if M == (0, 0, 0)]
triv_hl = [w for w, M in hlall(10) if M == I3]
ch = Counter(len(w) for w in triv_h)
OUT["H3_trivial_by_len_le10"] = dict(sorted(ch.items()))
chk("5: H3(Z)-trivial reduced words <= 10 by length: {0:1, 8:64, 10:288}", dict(ch) == {0: 1, 8: 64, 10: 288}, dict(sorted(ch.items())))
chk("5: the lower-unitriangular evaluation gives the same set of words", sorted(triv_h) == sorted(triv_hl), len(triv_hl))
t8 = [w for w in triv_h if 0 < len(w) <= 8]
OUT["H3_len8_classes"] = len({canon(w) for w in t8})
chk("5: the 64 length-8 words fall in 8 conjugacy classes (relay/prior)", len({canon(w) for w in t8}) == 8, sorted({canon(w) for w in t8}))
chk("5: all 64 non-empty length-8 H3-trivial words are I at the quaternion point (Z[i] matrices)", all(qmev(w) == GI for w in t8))
chk("5: ... and = 1 as Hamilton quaternions i, j", all(qhev(w) == (1, 0, 0, 0) for w in t8))
chk("5: all 353 H3-trivial words <= 10 are 1 at Q8", all(qmev(w) == GI and qhev(w) == (1, 0, 0, 0) for w in triv_h), len(triv_h))
cq = Counter(len(w) for w, M in qmall(8) if M == GI); cqh = Counter(len(w) for w, M in qhall(8) if M == (1, 0, 0, 0))
OUT["Q8_trivial_by_len_le8"] = dict(sorted(cq.items()))
chk("5: Q8-trivial words <= 8 by length {0:1,4:36,6:216,8:2268}, both evaluations", dict(cq) == dict(cqh) == {0: 1, 4: 36, 6: 216, 8: 2268}, dict(sorted(cq.items())))
print("   example length-8 H3-trivial words:", sorted(t8)[:4])
# plants for (5)
def hmod2(p, q): return ((p[0] + q[0]) % 2, (p[1] + q[1]) % 2, (p[2] + q[2] + p[0] * q[1]) % 2)
_, h2all = ev_factory({"a": (1, 0, 0), "A": (1, 0, 0), "b": (0, 1, 0), "B": (0, 1, 0)}, hmod2, (0, 0, 0))
assert hmod2((1, 0, 0), (1, 0, 0)) == (0, 0, 0)
t_h2 = [w for w, M in h2all(8) if M == (0, 0, 0)]
plant("P-5a H3(F2) (dihedral of order 8) in place of H3(Z); check 'trivial there => trivial at Q8'", all(qmev(w) == GI for w in t_h2),
      {"n_trivial": len(t_h2), "first_bad": min((w for w in t_h2 if qmev(w) != GI), key=len, default=None)})
HB = {"a": ((1, 1, 0), (0, 1, 0), (0, 0, 1)), "A": ((1, -1, 0), (0, 1, 0), (0, 0, 1)), "b": ((1, 0, 1), (0, 1, 0), (0, 0, 1)), "B": ((1, 0, -1), (0, 1, 0), (0, 0, 1))}
_, hball = ev_factory(HB, imul, I3)
t_hb = [w for w, M in hball(8) if M == I3]
plant("P-5b 'Heisenberg' with b = I + E13 (commutes with a); check 'trivial there => trivial at Q8'", all(qmev(w) == GI for w in t_hb),
      {"n_trivial": len(t_hb), "first_bad": min((w for w in t_hb if qmev(w) != GI), key=len, default=None)})

# ------------------------------------------------------------------ (3) statement D (homology parts)
def absum(w): return (w.count("a") - w.count("A"), w.count("b") - w.count("B"))
bd = {"torus1": ["abAB"], "pants": ["a", "b", winv("ab")], "RP2_2holes": ["b", winv("aab")], "Klein1 (x^2y^2)": [winv("aabb")], "Klein1 (xyxY)": [winv("abaB")]}
cls = {k: [absum(w) for w in v] for k, v in bd.items()}; OUT["boundary_classes"] = cls
chk("D: boundary classes null in H1(Z) only on the one-holed torus (both Klein presentations non-null)",
    [k for k, v in cls.items() if all(x == (0, 0) for x in v)] == ["torus1"], cls)
def hact(m, v):
    ia, ib = IMAGES[m]; A_, B_ = absum(ia), absum(ib)
    return (v[0] * A_[0] + v[1] * B_[0], v[0] * A_[1] + v[1] * B_[1])
mod2 = {(1, 0), (0, 1), (1, 1)}
chk("D: mod 2 the three non-zero classes are permuted by every one of the six moves", all({tuple(x % 2 for x in hact(m, v)) for v in mod2} == mod2 for m in MOVES))
grow = all(len({tuple(v)} | {hact("R1 a->ab", v)} | {hact("R3 b->ba", v)}) > 1 for v in [(1, 0), (0, 1), (3, -2)])
chk("D: no non-zero integral class is fixed by both R1 and R3 (so no finite non-empty invariant set except {0})", grow)

# ------------------------------------------------------------------ (4) the prime 2
X = sp.Matrix([[0, 1], [1, 0]]); Zc = sp.diag(1, -1)
QA = sp.Matrix([[sp.I, 0], [0, -sp.I]]); QB = sp.Matrix([[0, 1], [-1, 0]])
def sev_pair(pair, w):
    a_, b_ = pair; G = {"a": a_, "A": a_.inv(), "b": b_, "B": b_.inv()}
    M = sp.eye(a_.shape[0])
    for c in w: M = M * G[c]
    return sp.expand(M)
def image(pair, m): ia, ib = IMAGES[m]; return (sev_pair(pair, ia), sev_pair(pair, ib))
def hom_dim(src, dst):
    """dim of {g : g src(x) = dst(x) g}, via vec(g A - B g) = (A^T kron I - I kron B) vec g."""
    n = src[0].shape[0]; I = sp.eye(n)
    K = sp.Matrix.vstack(*[sp.kronecker_product(s_.T, I) - sp.kronecker_product(I, d_) for s_, d_ in zip(src, dst)])
    ns = K.nullspace()
    return ns, n
def iso(src, dst):
    ns, n = hom_dim(src, dst)
    if not ns: return False, None
    ts = sp.symbols("t0:%d" % len(ns))
    g = sp.zeros(n, n)
    for t, v in zip(ts, ns): g += t * sp.Matrix(n, n, list(v)).T   # vec is column-stacked
    d = sp.expand(g.det())
    if d == 0: return False, None
    # verify with a concrete invertible choice
    for trial in ([1] * len(ts), list(range(1, len(ts) + 1)), [2, 3, 5, 7, 11][:len(ts)]):
        gg = g.subs(dict(zip(ts, trial)))
        if gg.det() != 0:
            assert all(sp.expand(gg * s_ - d_ * gg) == sp.zeros(n, n) for s_, d_ in zip(src, dst))
            return True, gg
    return True, g
CS = (X, Zc); Q = (QA, QB); one = sp.eye(2)
chk("4: clock-and-shift: a^2 = b^2 = I, (ab)^2 = -I, [a,b] = -I",
    sev_pair(CS, "aa") == one and sev_pair(CS, "bb") == one and sev_pair(CS, "abab") == -one and sev_pair(CS, C) == -one)
lin = {m: iso(CS, image(CS, m))[0] for m in MOVES}
OUT["clock_shift_linear_fixed"] = lin
# second method: a^2, b^2 as invariants (scalars on this family)
inv2 = {m: ((image(CS, m)[0] ** 2)[0, 0], (image(CS, m)[1] ** 2)[0, 0]) for m in MOVES}
OUT["clock_shift_image_squares"] = {m: str(v) for m, v in inv2.items()}
chk("4: linearly, only the swap fixes clock-and-shift (nullspace method)", [m for m in MOVES if lin[m]] == ["S swap"], lin)
chk("4: the same from the squares invariant (a'^2, b'^2) = (1, 1) only for the swap", [m for m in MOVES if inv2[m] == (1, 1)] == ["S swap"], inv2)
def tick_not_fix(pair): return not iso(pair, image(pair, "T tick"))[0]
chk("4: the tick does NOT fix clock-and-shift linearly", tick_not_fix(CS))
plant("P-4a quaternion point fed to 'the tick does NOT fix it linearly'", tick_not_fix(Q))
H = sp.Matrix([[1, 1], [1, -1]]); chk("4: Hadamard carries (X, Z) to (Z, X)", H * X * H.inv() == Zc and H * Zc * H.inv() == X)
CS2 = (sp.diag(X, X), sp.diag(Zc, Zc))
chk("4: rho + conj(rho) = rho + rho (real entries) is not fixed linearly by the tick", not iso(CS2, image(CS2, "T tick"))[0])
chk("4: ... but it is fixed by the swap", iso(CS2, image(CS2, "S swap"))[0])
qfix = {m: iso(Q, image(Q, m)) for m in MOVES}
OUT["quaternion_intertwiners"] = {m: str(v[1].tolist()) if v[1] is not None else None for m, v in qfix.items()}
def fixed_by_all_six(pair): return all(iso(pair, image(pair, m))[0] for m in MOVES)
chk("4: the quaternion point is fixed linearly by all six moves (verified intertwiners)", fixed_by_all_six(Q), OUT["quaternion_intertwiners"])
plant("P-4b clock-and-shift fed to 'fixed linearly by all six'", fixed_by_all_six(CS))
plant("P-4c mis-written quaternion point a = diag(1,-1), b = [[0,1],[-1,0]] fed to 'fixed by all six'", fixed_by_all_six((Zc, QB)))
# prior agent's intertwiners for the quaternion point, checked as stated in its report
prior = {"R1 a->ab": [[1, -1], [1, 1]], "R2 a->ba": [[1, 1], [-1, 1]], "R3 b->ba": [[-sp.I, 0], [0, 1]], "R4 b->ab": [[sp.I, 0], [0, 1]],
         "S swap": [[-1, sp.I], [-sp.I, 1]], "T tick": [[-sp.I, -1], [-sp.I, 1]]}
pr_ok = {}
for m, g in prior.items():
    g = sp.Matrix(g); im_ = image(Q, m)
    pr_ok[m] = g.det() != 0 and sp.expand(g * QA * g.inv() - im_[0]) == sp.zeros(2) and sp.expand(g * QB * g.inv() - im_[1]) == sp.zeros(2)
chk("4: the six intertwiners stated in the report satisfy g rho(x) g^-1 = rho(phi(x))", all(pr_ok.values()), pr_ok)
# projective: twists by chi with chi(a), chi(b) in mu_4
mu4 = [1, sp.I, -1, -sp.I]
proj = {}
for m in MOVES:
    ia, ib = image(CS, m); found = None
    for ca in mu4:
        for cb in mu4:
            if iso(CS, (ca * ia, cb * ib))[0]: found = (ca, cb); break
        if found: break
    proj[m] = found
OUT["clock_shift_projective_twists"] = {m: str(v) for m, v in proj.items()}
chk("4: projectively all six fix clock-and-shift (a character twist exists)", all(v is not None for v in proj.values()), proj)
# the family [a,b] = -I: a = [[0,1],[alpha,0]], b = diag(s,-s)
al, s_ = sp.symbols("alpha s", nonzero=True)
F = (sp.Matrix([[0, 1], [al, 0]]), sp.diag(s_, -s_))
chk("4: family: [a,b] = -I, a^2 = alpha, b^2 = s^2", sp.simplify(sev_pair(F, C) + one) == sp.zeros(2) and sp.simplify(sev_pair(F, "aa") - al * one) == sp.zeros(2) and sp.simplify(sev_pair(F, "bb") - s_**2 * one) == sp.zeros(2))
act = {}
for m in MOVES:
    ia, ib = image(F, m)
    A2, B2 = sp.simplify(ia ** 2), sp.simplify(ib ** 2)
    assert A2[0, 1] == 0 and A2[1, 0] == 0 and sp.simplify(A2[0, 0] - A2[1, 1]) == 0
    act[m] = (sp.factor(A2[0, 0]), sp.factor(B2[0, 0]))
OUT["family_action"] = {m: str(v) for m, v in act.items()}
be = sp.symbols("beta")
expect_act = {"R1 a->ab": (-al * be, be), "R2 a->ba": (-al * be, be), "R3 b->ba": (al, -al * be), "R4 b->ab": (al, -al * be), "S swap": (be, al), "T tick": (-al * be, al)}
chk("4: action on (alpha, beta) matches R1,R2 (-ab, b); R3,R4 (a, -ab); S (b, a); T (-ab, a)",
    all(sp.simplify(act[m][0].subs(s_**2, be) - expect_act[m][0]) == 0 and sp.simplify(act[m][1].subs(s_**2, be) - expect_act[m][1]) == 0 for m in MOVES), OUT["family_action"])
eqs = []
for m in MOVES: eqs += [expect_act[m][0] - al, expect_act[m][1] - be]
G = sp.groebner(eqs + [al * be * sp.Symbol("u") - 1], sp.Symbol("u"), al, be, order="lex")
OUT["groebner_fixed_points"] = str(G.exprs)
sol = sp.solve(eqs, [al, be], dict=True)
sol_nz = [d for d in sol if d.get(al, 1) != 0 and d.get(be, 1) != 0]
chk("4: the only common fixed point in (C^*)^2 is (-1,-1)", sol_nz == [{al: -1, be: -1}] and set(G.exprs) >= {al + 1, be + 1}, (sol, G.exprs))
# sign table
def sgn_img(sa, sb, m):
    return tuple(int(x) for x in (expect_act[m][0].subs({al: sa, be: sb}), expect_act[m][1].subs({al: sa, be: sb})))
table = {(sa, sb): {m: sgn_img(sa, sb, m) for m in MOVES} for sa in (1, -1) for sb in (1, -1)}
OUT["sign_table"] = {str(k): {m: str(v) for m, v in r.items()} for k, r in table.items()}
main_table = {  # transcribed from main's run file wp12_added/..._run.txt
    "R1 a->ab": {(1, 1): (-1, 1), (1, -1): (1, -1), (-1, 1): (1, 1), (-1, -1): (-1, -1)},
    "R2 a->ba": {(1, 1): (-1, 1), (1, -1): (1, -1), (-1, 1): (1, 1), (-1, -1): (-1, -1)},
    "R3 b->ba": {(1, 1): (1, -1), (1, -1): (1, 1), (-1, 1): (-1, 1), (-1, -1): (-1, -1)},
    "R4 b->ab": {(1, 1): (1, -1), (1, -1): (1, 1), (-1, 1): (-1, 1), (-1, -1): (-1, -1)},
    "S swap": {(1, 1): (1, 1), (1, -1): (-1, 1), (-1, 1): (1, -1), (-1, -1): (-1, -1)},
    "T tick": {(1, 1): (-1, 1), (1, -1): (1, 1), (-1, 1): (1, -1), (-1, -1): (-1, -1)}}
chk("4: my sign table equals main's (wp12_added run file), cell by cell", all(table[k][m] == main_table[m][k] for m in MOVES for k in table))
orb, fr = {(1, 1)}, [(1, 1)]
while fr:
    k = fr.pop()
    for m in MOVES:
        j = table[k][m]
        if j not in orb: orb.add(j); fr.append(j)
chk("4: (1,1), (-1,1), (1,-1) are one orbit; (-1,-1) is fixed", orb == {(1, 1), (-1, 1), (1, -1)} and all(table[(-1, -1)][m] == (-1, -1) for m in MOVES), sorted(orb))
# odd p: commutator scalar of the image pair, in exact cyclotomic arithmetic (sympy roots of unity)
for p in (2, 3, 5, 7):
    zeta = sp.exp(2 * sp.pi * sp.I / p)
    sh = sp.zeros(p, p)
    for j in range(p): sh[(j + 1) % p, j] = 1
    cl = sp.diag(*[zeta ** j for j in range(p)])
    xx = sp.Symbol("xx")
    def is0(e): return sp.minimal_polynomial(e, xx) == xx          # exact: algebraic number e is 0 iff its minimal polynomial is x
    def scal(Mx):
        Mx = sp.simplify(Mx)
        d = Mx[0, 0]
        ok = all(is0(Mx[i, j] - (d if i == j else 0)) for i in range(p) for j in range(p))
        return d if ok else None
    c0 = scal(sev_pair((sh, cl), C))
    res = {}
    for m in MOVES:
        ia, ib = image((sh, cl), m)
        res[m] = scal(sp.simplify(ia * ib * ia.inv() * ib.inv()))
    single = all(is0(res[m] - c0) for m in MOVES)
    pair = all(is0(res[m] - c0) or is0(res[m] - 1 / c0) for m in MOVES)
    flips = [m for m in MOVES if not is0(res[m] - c0)]
    chk(f"4 p={p}: [a,b] = zeta^-1 scalar; single sector kept by all six: {single}; pair kept: {pair}; flipped by {flips}",
        is0(c0 - 1 / zeta) and single == (p == 2) and pair and (p == 2 or flips == ["S swap", "T tick"]))

n_fail = sum(1 for c in OUT["checks"] if not c[1]); n_plants = len(OUT["plants"]); n_caught = sum(1 for p_ in OUT["plants"] if p_[1])
print(f"\nCHECKS {len(OUT['checks'])}, failing {n_fail}; PLANTS {n_plants}, caught {n_caught}")
json.dump(OUT, open(sys.argv[1], "w"), indent=1, default=str)
