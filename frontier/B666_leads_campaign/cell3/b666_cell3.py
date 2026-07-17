"""B666 cell 3 — L107-E6: the landscape at the E6 level-2 stage + the
generating function.

QUESTION (sealed): is the B664/B665 landscape law stage-universal?
 (1) |tr_odd(R^{n-2}L)| at E6 level 2, n = 3..40: three-value/five-tone
     structure? period 5 or the stage's own conductor?
 (2) general words (RLRL, RRLL, RRRLLL): a shadow-class law with the E6
     stage's own shadow?
 (3) the generating function of the golden family sequence, exactly, and
     the Dirichlet-character-mod-5 factorization form (B664's registered
     question).

EXACT ARITHMETIC in every decisive step:
 - h-values / T-phases: Fractions (pure Kac-Peterson h-arithmetic);
 - the S-matrix: EXACT in Q(zeta_42) by integer-counting the 51840
   Kac-Peterson terms (each term is +-zeta_42^m); lifted to Q(zeta_84);
   all identities checked by reduction mod the cyclotomic polynomial
   Phi_84 (sympy, domain QQ) — zero tolerance;
 - the odd-block coefficients X_jj, the closed form, and the 7 residue
   values of |tr_odd|^2: exact in Q(zeta_84);
 - the generating function: sympy exact over Q(sqrt5)/Q(sqrt2).
Floats appear only for discovery/sanity cross-checks (1e-9) and the
finite-group BFS/bucket scans (unitary matrices, entries O(1)).

Run: python3 b666_cell3.py  (pyenv; ~2-4 min).
"""
import importlib.util
import itertools
import os
from fractions import Fraction

import numpy as np
import sympy as sp
_REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

ROOT = _REPO + ""


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


c3 = load("c3", "frontier/B570_allowed_plays/c3_e6_level2_monodromy.py")
b238 = load("b238", "frontier/B238_su32_levelrank/su32_wrt.py")

print("=" * 72)
print("PART 0 — the E6 level-2 stage (banked build: B570-C3 / B594) + gates")
print("=" * 72)
W, eps = c3.weyl_group()
assert len(W) == 51840
rho_w = c3.root_coords([1] * 6)
shifted = [c3.root_coords(p) + rho_w for p in c3.PRIM]
S = np.zeros((9, 9), dtype=complex)
Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
for a in range(9):
    for b in range(a, 9):
        ips = Wl[:, a, :] @ (c3.C @ shifted[b])
        S[a, b] = S[b, a] = np.sum(eps * np.exp(-2j * np.pi * ips / c3.KH))
S /= np.sqrt((S @ S.conj().T)[0, 0].real)
if S[0, 0].real < 0:
    S = -S

# exact h-values (Fractions via sympy Rational matrix inverse)
Cm_s = sp.Matrix(c3.C6)
Cinv_s = Cm_s.inv()
rho_vec = Cinv_s * sp.Matrix([1] * 6)
KH = 14
hs = []
for p in c3.PRIM:
    lam = Cinv_s * sp.Matrix(list(p))
    hs.append(sp.Rational(((lam.T * Cm_s * (lam + 2 * rho_vec))[0, 0])) / (2 * KH))
cc = sp.Rational(2 * 78, KH)                      # c = 78/7
print(f"c = {cc}; c/24 = {sp.nsimplify(cc/24)}")
print("h:", {c3.NAMES[i]: str(hs[i]) for i in range(9)})
T = np.diag([complex(sp.exp(2 * sp.pi * sp.I * (h - cc / 24)).evalf(30))
             for h in hs])
uni = np.linalg.norm(S @ S.conj().T - np.eye(9))
sym = np.linalg.norm(S - S.T)
C2n = S @ S
rel = np.linalg.norm(np.linalg.matrix_power(S @ T, 3) - C2n)
expect = np.zeros((9, 9))
for i, p in enumerate(c3.PRIM):
    expect[c3.PRIM.index(c3.theta(p)), i] = 1
gC = np.linalg.norm(C2n - expect)
print(f"gates: unitary {uni:.1e}  symmetric {sym:.1e}  (ST)^3=S^2 {rel:.1e}"
      f"  S^2=theta-flip {gC:.1e}")
assert uni < 1e-9 and sym < 1e-9 and rel < 1e-8 and gC < 1e-9

# theta-odd 3-space; B664/B238 conventions: R = T, L = S^-1 T^-1 S
pairs = [(1, 2), (3, 4), (7, 8)]                  # (27,27b) (351p,351pb) (351,351b)
PNAMES = ["27", "351p", "351"]
for (a, b) in pairs:
    assert hs[a] == hs[b], "conjugate pair h-equality (exact)"
print("EXACT: h(la) = h(conj la) on all three pairs -> T preserves the")
print("theta-split; [T,C] = 0 and C = S^2 => EVERY word in R,L is")
print("block-diagonal in the theta-split (structural, exact).")

print()
print("=" * 72)
print("PART 1 — exact T-phase arithmetic on the odd 3-space (Fractions)")
print("=" * 72)
alphas = [sp.nsimplify(hs[a] - cc / 24) % 1 for (a, b) in pairs]
betas = [int(84 * al) for al in alphas]
for nm, al, be in zip(PNAMES, alphas, betas):
    assert sp.Rational(be, 84) == al
    print(f"  pair {nm:>5}: T-phase alpha = {al} = zeta_84^{be}")
print("pairwise differences:",
      [str(sp.nsimplify(alphas[i] - alphas[j]) % 1)
       for i in range(3) for j in range(i + 1, 3)],
      " -> ALL in (1/7)Z  => modulus period divides 7 (EXACT)")
assert {(sp.nsimplify(alphas[i] - alphas[j]) % 1) * 7 % 1
        for i in range(3) for j in range(i + 1, 3)} == {0}
r7 = sorted({(7 * b) % 84 for b in betas})
print(f"R^7 on the odd space: phases 7*beta mod 84 = {r7} -> ALL equal 7")
assert r7 == [7]
print("  => rho_odd(R^7) = zeta_12 * I EXACTLY (the scalar mechanism —")
print("     the E6 analog of the golden stage's rho_odd(R^5) = zeta_3^2 I).")
g5 = sorted({(5 * int(15 * al)) % 15 for al in
             [sp.Rational(2, 15), sp.Rational(8, 15)]})
print(f"  (golden check, B664 phases 2/15, 8/15: 5*beta mod 15 = {g5})")

print()
print("=" * 72)
print("PART 2 — the EXACT S-matrix in Q(zeta_84) and the exact X_jj")
print("=" * 72)
# 3*(lambda+rho) are integer vectors (E6 weight lattice pairing in (1/3)Z)
A = []
for p in c3.PRIM:
    v = (Cinv_s * (sp.Matrix(list(p)) + sp.Matrix([1] * 6))) * 3
    vi = [int(x) for x in v]
    assert all(sp.Rational(x) == y for x, y in zip(vi, v))
    A.append(np.array(vi, dtype=np.int64))
Cint = np.array(c3.C6, dtype=np.int64)
Wint = W.astype(np.int64)

M = 84
Sv = [[None] * 9 for _ in range(9)]               # S_un as int vectors, zeta_84 powers
for a in range(9):
    WA = np.einsum('wij,j->wi', Wint, A[a])
    for b in range(a, 9):
        E = WA @ (Cint @ A[b])                    # 9*(w(la+r), lb+r), integer
        assert (E % 3 == 0).all()
        m42 = (-(E // 3)) % 42                    # term = eps * zeta_42^m42
        m84 = (2 * m42) % 84
        cnt = np.bincount(m84[eps > 0], minlength=M).astype(object) \
            - np.bincount(m84[eps < 0], minlength=M).astype(object)
        vec = [int(x) for x in cnt]
        Sv[a][b] = vec
        Sv[b][a] = vec

x = sp.symbols('x')
PHI84 = sp.Poly(sp.cyclotomic_poly(84, x), x, domain='QQ')


def red(vec):
    return sp.Poly.from_dict({i: sp.Rational(v) for i, v in enumerate(vec)
                              if v != 0}, x, domain='QQ').rem(PHI84)


def conj(u):
    out = [0] * M
    for i, v in enumerate(u):
        if v:
            out[(-i) % M] += v
    return out


def mul(u, v):
    out = [0] * M
    for i, a_ in enumerate(u):
        if a_:
            for j, b_ in enumerate(v):
                if b_:
                    out[(i + j) % M] += a_ * b_
    return out


def shift(u, k):
    out = [0] * M
    for i, v in enumerate(u):
        if v:
            out[(i + k) % M] += v
    return out


def add(u, v, sgn=1):
    return [a_ + sgn * b_ for a_, b_ in zip(u, v)]


def mono(k, coef=1):
    out = [0] * M
    out[k % M] = coef
    return out


# exact normalization: N^2 = 3 * 14^6 (Kac-Peterson: |P/Q| = 3, l = 6, kap = 14)
N2 = 3 * 14 ** 6
acc = [0] * M
for b in range(9):
    acc = add(acc, mul(Sv[0][b], conj(Sv[0][b])))
rN = red(acc)
print(f"EXACT (S_un S_un^dag)_00 = {rN.as_expr()}  (target 3*14^6 = {N2})")
assert rN == sp.Poly(N2, x, domain='QQ')

# exact S^2 = C (the theta-flip permutation), scaled by N^2
conj_idx = [c3.PRIM.index(c3.theta(p)) for p in c3.PRIM]
ok = True
for a in range(9):
    for b in range(9):
        acc = [0] * M
        for p in range(9):
            acc = add(acc, mul(Sv[a][p], Sv[p][b]))
        target = sp.Poly(N2, x, domain='QQ') if b == conj_idx[a] \
            else sp.Poly(0, x, domain='QQ')
        ok &= (red(acc) == target)
assert ok
print("EXACT: S^2 = N^2 * C (theta-flip) — all 81 entries, zero residue.")

# exact T-bar exponents (all nine h have 84*(h - 13/28) integer)
tbar = []
for h in hs:
    e = 84 * (h - sp.Rational(13, 28))
    assert e == int(e)
    tbar.append((-int(e)) % 84)

# exact odd block of X = S^-1 T^-1 S = (1/N^2) S_bar T_bar S
odd_idx = pairs
Bodd = [[None] * 3 for _ in range(3)]             # times 2*N^2 (integer vectors)
for j, (a1, b1) in enumerate(odd_idx):
    for k, (a2, b2) in enumerate(odd_idx):
        acc = [0] * M
        for (u, su) in ((a1, 1), (b1, -1)):
            for (v, sv) in ((a2, 1), (b2, -1)):
                for p in range(9):
                    acc = add(acc, shift(mul(conj(Sv[u][p]), Sv[p][v]),
                                         tbar[p]), sgn=su * sv)
        Bodd[j][k] = acc                          # = 2*N^2 * (X_odd)_{jk}

# numeric cross-check of the exact odd block
z84 = np.exp(2j * np.pi / 84)
num = lambda vec: sum(v * z84 ** i for i, v in enumerate(vec) if v)
odd = np.zeros((9, 3))
for j, (a, b) in enumerate(pairs):
    odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
Xn = np.linalg.inv(S) @ np.linalg.inv(T) @ S
Bx = odd.T @ Xn @ odd
dev = max(abs(num(Bodd[j][k]) / (2 * N2) - Bx[j, k])
          for j in range(3) for k in range(3))
print(f"exact odd block vs numeric stage build: max dev = {dev:.2e}")
assert dev < 1e-8

# the Gauss sum g7 = sum chi7(t) zeta_7^t;  g7^2 = -7 (exact)
QR7 = {1, 2, 4}
g7 = [0] * M
for t in range(1, 7):
    g7[(12 * t) % 84] += (1 if t in QR7 else -1)
assert red(add(mul(g7, g7), mono(0, 7))) == sp.Poly(0, x, domain='QQ')
print("EXACT: Gauss sum g7^2 = -7 (g7 = i sqrt7 branch checked numerically:"
      f" {num(g7):+.6f})")
assert abs(num(g7) - 1j * np.sqrt(7)) < 1e-9

print("\nTHE EXACT DIAGONAL COEFFICIENTS (the closed form's ingredients):")
CAND = [(1, 5), (3, -1), (2, 17)]                 # (j', m): X_jj = (2/sqrt7) sin(2pi j'/7) zeta_84^m
for j, (jp, mph) in enumerate(CAND):
    # claim: X_jj * g7 = (zeta_7^jp - zeta_7^-jp) * zeta_84^mph
    lhs = mul(Bodd[j][j], g7)                     # = 2 N^2 X_jj g7
    rhs = add(mono((12 * jp + mph) % M, 2 * N2),
              mono((-12 * jp + mph) % M, 2 * N2), sgn=-1)
    assert red(add(lhs, rhs, sgn=-1)) == sp.Poly(0, x, domain='QQ')
    print(f"  X_{j+1}{j+1} ({PNAMES[j]:>5}) = (2/sqrt7) sin(2pi*{jp}/7) *"
          f" zeta_84^{mph % 84}   [EXACT, zero residue mod Phi_84]")
print("  => the odd-diagonal of L IS the Z/7 SINE KERNEL (B589/B594's")
print("     hearing amplitudes) times exact 84th roots of unity.")

print("\nTHE CLOSED FORM (exact, from T-diagonality of the odd block):")
print("  tr_odd(R^{n-2}L) = sum_j zeta_84^{beta_j (n-2)} X_jj,")
print(f"  beta = {betas}, X_jj as above — a THREE-term exponential sum")
print("  (golden stage: TWO-term).  sum_j |X_jj|^2 = (4/7)(s1^2+s2^2+s3^2) = 1.")

print()
print("=" * 72)
print("PART 3 — the landscape n = 3..40 (and to 170): values and period")
print("=" * 72)
Toddn = np.diag([z84 ** b for b in betas])
Xodd = np.array([[num(Bodd[j][k]) / (2 * N2) for k in range(3)]
                 for j in range(3)])
SQ2 = np.sqrt(2)
vals, reals_nz = [], []
for n in range(3, 171):
    tr = np.trace(np.linalg.matrix_power(Toddn, n - 2) @ Xodd)
    a_ = abs(tr)
    cls = min((0.0, 1.0, SQ2), key=lambda v: abs(a_ - v))
    assert abs(a_ - cls) < 1e-9, (n, a_)
    vals.append((n, cls))
    if abs(tr.imag) < 1e-9 and a_ > 1e-9:
        reals_nz.append(n)
    if n <= 40:
        lab = {0.0: "deaf", 1.0: "one ", SQ2: "sqrt2"}[cls]
        print(f"  n={n:3d}  |tr_odd| = {a_:.9f}  [{lab}]  tr = {tr:+.6f}")
seq = [v for _, v in vals]
per = next(P for P in range(1, 100)
           if all(abs(seq[i] - seq[i + P]) < 1e-12
                  for i in range(len(seq) - P)))
print(f"\nvalue set = {{0, 1, sqrt2}}  (three values, ALL n=3..170)")
print(f"observed modulus period = {per}  (exact upper bound 7 from PART 1;")
print("  values within one period differ => period EXACTLY 7)")
assert per == 7
print("residue law (r = n mod 7):  r=0 -> 1 | r=+-1 -> 0 (deaf) |"
      " r=+-2 -> sqrt2 | r=+-3 -> 1")
by_r = {}
for n, v in vals:
    by_r.setdefault(n % 7, set()).add(v)
assert all(len(s) == 1 for s in by_r.values())
assert [by_r[r].pop() for r in range(7)] == [1.0, 0.0, SQ2, 1.0, 1.0, SQ2, 0.0]
print(f"nonzero-REAL tr_odd at n = {reals_nz[:8]}...  residues mod 84: "
      f"{sorted(set(n % 84 for n in reals_nz))}")
print("  (the reality lattice is mod-84 — the E6 analog of golden's mod-15;")
print("   the modulus never needs it: period 7.)")

print()
print("=" * 72)
print("PART 4 — THE EXACT SEVEN-VALUE THEOREM: |tr_odd|^2 in {0,1,2}")
print("=" * 72)
targets = {3: 1, 4: 1, 5: 2, 6: 0, 7: 1, 8: 0, 9: 2}
for n, v in targets.items():
    tv = [0] * M
    for j in range(3):
        tv = add(tv, shift(Bodd[j][j], (betas[j] * (n - 2)) % M))
    msq = mul(tv, conj(tv))                       # = (2N^2)^2 |tr_odd|^2
    assert red(msq) == sp.Poly(v * (2 * N2) ** 2, x, domain='QQ'), n
    print(f"  n = {n} (r = {n % 7}):  |tr_odd|^2 = {v}   [EXACT mod Phi_84]")
print("EXACT: |tr_odd(R^{n-2}L)| in {0, 1, sqrt2} with period exactly 7 —")
print("the THREE-VALUE THEOREM reproduces at the E6 stage with the stage's")
print("OWN values ({0, 1/phi, 1} -> {0, 1, sqrt2}) and OWN conductor (5 -> 7).")

print()
print("=" * 72)
print("PART 5 — the shadow-class law at the E6 stage (mod-7 shadow)")
print("=" * 72)
# the finite image of the odd rep (numeric BFS; entries O(1), tol 1e-6)
gens = [Toddn, Xodd]


def bfs(gens, cap=200000):
    key = lambda Mm: tuple(np.round(Mm, 6).flatten().view(float))
    n0 = gens[0].shape[0]
    I = np.eye(n0, dtype=complex)
    seen = {key(I): I}
    frontier = [I]
    while frontier:
        new = []
        for Mm in frontier:
            for g in gens:
                Ng = Mm @ g
                k = key(Ng)
                if k not in seen:
                    seen[k] = Ng
                    new.append(Ng)
        frontier = new
        assert len(seen) < cap
    return list(seen.values())


G = bfs(gens)
scal = [Mm for Mm in G
        if np.allclose(Mm, Mm[0, 0] * np.eye(3), atol=1e-6)]
print(f"|image of rho_odd| = {len(G)};  scalars in image = {len(scal)};"
      f"  projective order = {len(G) // len(scal)}")
assert len(G) % len(scal) == 0
proj = len(G) // len(scal)
print(f"  => the PROJECTIVE odd image has order {proj}"
      + ("  = |PSL(2,7)| = 168  (the Klein-quartic group — B646's"
         " 'PSL(2,7) core')" if proj == 168 else "  (NOT 168!)"))

# SL(2,7) + PSL(2,7) class machinery (exact integer arithmetic mod 7)
def sl27():
    els = []
    for a_, b_, c_, d_ in itertools.product(range(7), repeat=4):
        if (a_ * d_ - b_ * c_) % 7 == 1:
            els.append((a_, b_, c_, d_))
    return els


EL = sl27()
assert len(EL) == 336
mmul7 = lambda A_, B_: ((A_[0] * B_[0] + A_[1] * B_[2]) % 7,
                        (A_[0] * B_[1] + A_[1] * B_[3]) % 7,
                        (A_[2] * B_[0] + A_[3] * B_[2]) % 7,
                        (A_[2] * B_[1] + A_[3] * B_[3]) % 7)
neg7 = lambda A_: tuple((-t) % 7 for t in A_)
inv7 = lambda A_: (A_[3], (-A_[1]) % 7, (-A_[2]) % 7, A_[0])
class_id, classes = {}, []
for Mm in EL:
    if Mm in class_id:
        continue
    orb = set()
    for g in EL:
        cgi = mmul7(mmul7(g, Mm), inv7(g))
        orb.add(cgi)
        orb.add(neg7(cgi))
    cid = len(classes)
    classes.append(orb)
    for e in orb:
        class_id[e] = cid


def psl_order(Mm):
    P, o = Mm, 1
    while P != (1, 0, 0, 1) and P != (6, 0, 0, 6):
        P = mmul7(P, Mm)
        o += 1
    return o


cls_info = []
for cid, orb in enumerate(classes):
    rep = sorted(orb)[0]
    cls_info.append((cid, psl_order(rep), len(orb)))
print(f"PSL(2,7) classes found: {len(classes)} "
      f"(orders {sorted(o for _, o, _ in cls_info)})")

# all words of length 1..13 in {R, L}: modulus vs mod-7 matrix bucket
R7, L7 = (1, 1, 0, 1), (1, 0, 1, 1)
buckets = {}                                       # mod-7 matrix -> set(round modulus)
cls_val = {}                                       # PSL class -> set(round modulus)
stack = [("", np.eye(3, dtype=complex), (1, 0, 0, 1))]
count = 0
for ln in range(13):
    nxt = []
    for wname, Mo, M7 in stack:
        for ch, go, g7_ in (("R", Toddn, R7), ("L", Xodd, L7)):
            w2, Mo2, M72 = wname + ch, Mo @ go, mmul7(M7, g7_)
            a_ = round(abs(np.trace(Mo2)), 9)
            buckets.setdefault(M72, set()).add(a_)
            cls_val.setdefault(class_id[M72], set()).add(a_)
            nxt.append((w2, Mo2, M72))
            count += 1
    stack = nxt
print(f"words scanned: {count} (all lengths 1..13);"
      f" SL(2,7) elements hit: {len(buckets)}/336")
assert len(buckets) == 336
spread = max(max(s) - min(s) for s in buckets.values())
print(f"max modulus spread within a mod-7 bucket: {spread:.1e}")
assert spread < 1e-8
print("  => THE SHADOW-CLASS LAW HOLDS: |tr_odd(W)| is a function of")
print("     W mod 7 alone (the E6 stage's own shadow), over all 336 classes.")

chi3 = {1: 3.0, 2: 1.0, 3: 0.0, 4: 1.0, 7: SQ2}   # |chi_3| of PSL(2,7), 3-dim irrep
print("\nthe tone table (PSL(2,7) class -> |tr_odd|) vs |chi_3| of the")
print("3-dim irrep (the Klein-quartic representation):")
okall = True
for cid, o, sz in sorted(cls_info, key=lambda t: t[1]):
    vs = cls_val.get(cid, set())
    assert len(vs) == 1
    v = vs.pop()
    okc = abs(v - chi3[o]) < 1e-8
    okall &= okc
    print(f"  class (PSL-order {o}, size {sz:3d}): |tr_odd| = {v:.9f}"
          f"   |chi_3| = {chi3[o]:.9f}   match: {okc}")
assert okall
print("  => |tr_odd(W)| = |chi_3(class of W mod 7)| — the modulus IS the")
print("     absolute character of the 3-dim PSL(2,7) irrep.  EXACT anchor:")
print("     PART 4 gives the family residues exactly (classes 2A,3A,4A,7A/B),")
print("     |chi_3|^2 on the order-7 classes = |(-1+-i sqrt7)/2|^2 = 2  ✓.")

# the three preregistered general words, explicitly
print("\nthe preregistered general words:")
for wname in ("RLRL", "RRLL", "RRRLLL"):
    Mo = np.eye(3, dtype=complex)
    M7 = (1, 0, 0, 1)
    for ch in wname:
        Mo, M7 = Mo @ (Toddn if ch == "R" else Xodd), \
            mmul7(M7, R7 if ch == "R" else L7)
    o = psl_order(M7)
    tr = np.trace(Mo)
    print(f"  {wname:>7}: tr_odd = {tr:+.6f}  |tr_odd| = {abs(tr):.9f}"
          f"   mod-7 PSL-order {o}  |chi_3| = {chi3[o]}")

print()
print("=" * 72)
print("PART 6 — stage-universality: the same law at the golden stage")
print("=" * 72)
w3, S3, T3, c3v = b238.su3_data(2)
prs = [(i, w3.index((wt[1], wt[0]))) for i, wt in enumerate(w3)
       if (wt[1], wt[0]) > wt]
odd2 = np.zeros((len(w3), len(prs)))
for j, (a, b) in enumerate(prs):
    odd2[a, j], odd2[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
X3 = np.linalg.inv(S3) @ np.linalg.inv(T3) @ S3
T3o = odd2.T @ T3 @ odd2
X3o = odd2.T @ X3 @ odd2
G2 = bfs([T3o, X3o])
scal2 = [Mm for Mm in G2 if np.allclose(Mm, Mm[0, 0] * np.eye(2), atol=1e-6)]
print(f"golden stage: |image| = {len(G2)}, scalars = {len(scal2)},"
      f" projective order = {len(G2) // len(scal2)}"
      + ("  = |PSL(2,5)| = |A5| = 60" if len(G2) // len(scal2) == 60 else ""))
PHI = (1 + np.sqrt(5)) / 2
# bucket by mod-5 matrix; tone table vs |chi_2| of SL(2,5) (binary icosahedral)
mmul5 = lambda A_, B_: ((A_[0] * B_[0] + A_[1] * B_[2]) % 5,
                        (A_[0] * B_[1] + A_[1] * B_[3]) % 5,
                        (A_[2] * B_[0] + A_[3] * B_[2]) % 5,
                        (A_[2] * B_[1] + A_[3] * B_[3]) % 5)
buck5 = {}
stack = [(np.eye(2, dtype=complex), (1, 0, 0, 1))]
for ln in range(13):
    nxt = []
    for Mo, M5 in stack:
        for go, g5_ in ((T3o, (1, 1, 0, 1)), ((X3o), (1, 0, 1, 1))):
            Mo2, M52 = Mo @ go, mmul5(M5, g5_)
            buck5.setdefault(M52, set()).add(round(abs(np.trace(Mo2)), 9))
            nxt.append((Mo2, M52))
    stack = nxt
assert len(buck5) == 120
sp5 = max(max(s) - min(s) for s in buck5.values())
tones5 = sorted({min(s) for s in buck5.values()})
print(f"SL(2,5) elements hit: {len(buck5)}/120; max in-bucket spread:"
      f" {sp5:.1e}")
assert sp5 < 1e-8
print(f"golden tone set: {[f'{t:.6f}' for t in tones5]}")
exp5 = sorted([0.0, 1 / PHI, 1.0, PHI, 2.0])
assert all(abs(a_ - b_) < 1e-8 for a_, b_ in zip(tones5, exp5))
print("  = {0, 1/phi, 1, phi, 2} = |chi_2| of SL(2,5) (the binary-icosahedral")
print("    2-dim character: 2, 0, +-1, +-phi, +-1/phi) — B665's five tones,")
print("    now read as the CHARACTER of the shadow group's distinguished irrep.")
print("\nTHE STAGE-UNIVERSAL LAW (both stages, verified):")
print("  |tr_odd(W)| = |chi_D(shadow(W))|,   shadow = reduction mod the")
print("  stage's own odd conductor (golden: 5, E6_2: 7); chi_D = the")
print("  distinguished D-dim irrep character (D = dim theta-odd: 2 resp. 3;")
print("  SL(2,5) 2-dim binary-icosahedral resp. PSL(2,7) 3-dim Klein-quartic).")

print()
print("=" * 72)
print("PART 7 — THE GENERATING FUNCTION (B664's registered question; exact)")
print("=" * 72)
nn = sp.symbols('n', integer=True)
xs = sp.symbols('x')
PH = (1 + sp.sqrt(5)) / 2
Dg = sp.sqrt(3 * PH * sp.sqrt(5))
a_closed = lambda n_: 2 * sp.sqrt(3) / Dg * sp.Abs(sp.cos(sp.pi * (4 * n_ - 5) / 10))
chi0 = lambda n_: 0 if n_ % 5 == 0 else 1
chi5 = lambda n_: 0 if n_ % 5 == 0 else (1 if n_ % 5 in (1, 4) else -1)
print("G1 — the Dirichlet-character factorization (mod 5), EXACT per residue:")
allok = True
for n_ in range(5, 10):
    lhs = sp.simplify(a_closed(n_))
    rhs = sp.simplify(PH / 2 * chi0(n_) + 1 / (2 * PH ** 2) * chi5(n_))
    mult = sp.simplify(chi0(n_) * PH ** sp.Rational(chi5(n_) - 1, 2)) \
        if n_ % 5 else sp.Integer(0)
    ok1 = sp.simplify(lhs - rhs) == 0 and sp.simplify(lhs - mult) == 0
    allok &= ok1
    print(f"  n mod 5 = {n_ % 5}:  a_n = {lhs}   "
          f"= (phi/2) chi_0 + (1/(2 phi^2)) chi_5 = chi_0 phi^((chi_5-1)/2):"
          f" {ok1}")
assert allok
print("\n  THEOREM (from B664's closed form, exact):  for n >= 3,")
print("    a_n := |tr_odd(R^{n-2}L)|_golden = (phi/2) chi_0(n)"
      " + (1/(2 phi^2)) chi_5(n)")
print("    = chi_0(n) * phi^((chi_5(n)-1)/2),")
print("  chi_0 = principal, chi_5 = quadratic (Legendre) character mod 5 —")
print("  the two REAL Dirichlet characters mod 5.")

print("\nG2 — the generating function, exact:")
numer = x ** 3 * (1 / PH + x + x ** 3 + x ** 4 / PH)
F = numer / (1 - x ** 5)
ser = sp.series(F, x, 0, 24).removeO()
okg = all(sp.simplify(ser.coeff(x, n_) - a_closed(n_)) == 0
          for n_ in range(3, 24))
assert okg
print("  F(x) = sum_{n>=3} a_n x^n = x^3 (1/phi + x + x^3 + x^4/phi)"
      " / (1 - x^5)   [verified to x^23, exact]")
fact = sp.factor(1 / PH + x + x ** 3 + x ** 4 / PH, extension=sp.sqrt(5))
print(f"  numerator factorization over Q(sqrt5): {fact}")
Fsplit = (PH / 2) * (x + x ** 2 + x ** 3 + x ** 4) / (1 - x ** 5) \
    + (1 / (2 * PH ** 2)) * (x - x ** 2 - x ** 3 + x ** 4) / (1 - x ** 5) \
    - x - x ** 2 / PH
assert sp.simplify(sp.factor(F - Fsplit)) == 0
print("  character split (exact):  F(x) = (phi/2) x(1+x)(1+x^2)/(1-x^5)")
print("    + (1/(2 phi^2)) x(1-x)^2(1+x)/(1-x^5)  -  x  -  x^2/phi")
print("  Dirichlet-series face (coefficientwise from G1, n >= 1 periodized):")
print("    sum a_n n^-s = (phi/2)(1 - 5^-s) zeta(s) + (1/(2 phi^2)) L(s, chi_5)")

print("\nG3 — the E6-stage generating function and the honest split:")
c7 = {0: 1, 1: 0, 2: sp.sqrt(2), 3: 1, 4: 1, 5: sp.sqrt(2), 6: 0}
numer7 = x ** 3 * (1 + x + sp.sqrt(2) * x ** 2 + x ** 4 + sp.sqrt(2) * x ** 6)
F7 = numer7 / (1 - x ** 7)
ser7 = sp.series(F7, x, 0, 26).removeO()
ok7 = all(sp.simplify(ser7.coeff(x, n_) - c7[n_ % 7]) == 0
          for n_ in range(3, 26))
assert ok7
print("  F7(x) = x^3 (1 + x + sqrt2 x^2 + x^4 + sqrt2 x^6) / (1 - x^7)"
      "   [verified to x^25, exact]")
fac7 = sp.factor(1 + x + sp.sqrt(2) * x ** 2 + x ** 4 + sp.sqrt(2) * x ** 6,
                 extension=sp.sqrt(2))
print(f"  numerator factorization over Q(sqrt2): {fac7}")
print("  NO real-Dirichlet-character factorization mod 7 exists:")
print("    any a chi_0 + b chi_7 is CONSTANT on the residues {1, 2, 4}")
print("    (the quadratic residues), but the E6 values there are"
      " {0, sqrt2, 1} —")
print("    pairwise distinct.  Mechanism: (Z/5)* has 2 = |{+-1}-cosets| real")
print("    characters (even functions mod 5 = char span, FORCED by period +")
print("    palindrome + deaf-at-0), while (Z/7)* has 3 +-cosets but only 2")
print("    real characters.  The mod-5 Dirichlet form is a golden-stage")
print("    accident; the STAGE-UNIVERSAL form is the irrep-character law:")
print("      a_n^(stage) = |chi_D(class of [[n-1,n-2],[1,1]] mod kappa')|.")

print("\nB666 CELL 3: ALL GATES PASS")
