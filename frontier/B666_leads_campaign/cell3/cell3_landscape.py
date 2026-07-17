"""B666 cell 3 — L107-E6: the landscape at the E6 level-2 stage + the
generating function (the B664 registered question).

PART A (the E6 landscape):
  1. Build the banked E6 level-2 stage (B570 c3 module: |W(E6)| = 51840,
     Kac-Peterson S, T; gates as in B570/B594).
  2. EXACT phase arithmetic (sympy Rational): the theta-odd T-phases are
     zeta_84^{13, 73, 61}; ALL pairwise ratios are 7th roots of unity
     => the modulus |tr_odd(R^{n-2}L)| has EXACT period 7 in n
     (the E6 stage's conductor kappa = 14 enters through its odd prime;
     the 2-part is modulus-invisible).  R^7 acts as the scalar zeta_12
     on the theta-odd 3-space (13*7 = 73*7 = 61*7 = 7 mod 84).
  3. EXACT cyclotomic evaluation in Q(zeta_84) (integer multiplicity
     vectors for the Kac-Peterson sum, custom arithmetic mod Phi_84):
     the seven values |tr_odd|^2 per residue class are computed EXACTLY.
  4. The shadow-class law at the E6 stage: |tr_odd(W)| tested for
     constancy on PSL(2,7) conjugacy classes of W mod 7 over a corpus
     of ~570 words, and matched against the 3-dim character of
     PSL(2,7): |chi_3| = {1A:3, 2A:1, 3A:0, 4A:1, 7A:sqrt2, 7B:sqrt2}.
  5. The split witnesses: the E6 hearing does NOT factor mod 5, the
     golden hearing does NOT factor mod 7 (each stage hears only its
     own shadow).

PART B (the generating function, the mod-5 registered question, exact):
  a_n = |tr_odd(R^{n-2}L; SU(3)_2)| satisfies the Dirichlet-character
  identity  a_n = (phi*chi_0(n) + phi^{-2}*chi_2(n))/2  (chi_0 the
  principal, chi_2 the Legendre symbol mod 5) — proved per residue from
  B664's closed form; the generating function is the rational function
  f(q) = (q^3/phi + q^4 + q^6 + q^7/phi)/(1 - q^5) and equals the
  character combination; the PRODUCT (Euler) form is REFUTED
  (a_3 a_21-witness); the Dirichlet series is the linear combination
  (phi/2)(1-5^{-s}) zeta(s) + (1/(2 phi^2)) L(s, chi_5).

Run: python3 cell3_landscape.py   (pyenv; ~2-4 min).
Exact arithmetic in every decisive step: sympy Rational for phases,
integer cyclotomic vectors mod Phi_84 for the E6 values, sympy exact
for the GF identities.  Floats only for the corpus sweep gates (1e-9).
"""
import importlib.util
import itertools
import os
import sys
from fractions import Fraction

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "..")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


print("=" * 72)
print("PART A — THE E6 LEVEL-2 LANDSCAPE")
print("=" * 72)

c3 = load("c3", os.path.join(ROOT, "frontier", "B570_allowed_plays",
                             "c3_e6_level2_monodromy.py"))
b238 = load("b238", os.path.join(ROOT, "frontier", "B238_su32_levelrank",
                                 "su32_wrt.py"))

# ---- A1: the stage build (B570/B594 pattern) + gates ----
W, eps_signs = c3.weyl_group()
assert len(W) == 51840
print(f"|W(E6)| = {len(W)} (exact)")
rho_w = c3.root_coords([1] * 6)
shifted = [c3.root_coords(p) + rho_w for p in c3.PRIM]
Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
S = np.zeros((9, 9), dtype=complex)
IPS = {}                                    # keep the exact exponent data
for a in range(9):
    for b in range(a, 9):
        ips = Wl[:, a, :] @ (c3.C @ shifted[b])
        IPS[(a, b)] = ips
        S[a, b] = S[b, a] = np.sum(eps_signs * np.exp(-2j * np.pi * ips / c3.KH))
norm2_num = (S @ S.conj().T)[0, 0].real
S = S / np.sqrt(norm2_num)
if S[0, 0].real < 0:
    S = -S
uni = np.linalg.norm(S @ S.conj().T - np.eye(9))
sym = np.linalg.norm(S - S.T)
assert uni < 1e-9 and sym < 1e-9
Cmat = sp.Matrix(c3.C6)
Cinv = Cmat.inv()
KH = 14
h_exact = []
for p in c3.PRIM:
    lam = sp.Matrix(p)
    h_exact.append(sp.Rational((lam.T * Cinv * (lam + 2 * sp.Matrix([1] * 6)))[0, 0], 2 * KH))
c_exact = sp.Rational(2 * 78, KH)
T = np.diag([complex(sp.exp(2 * sp.pi * sp.I * (h - c_exact / 24)).evalf(20))
             for h in h_exact])
ST3 = np.linalg.matrix_power(S @ T, 3)
S2 = S @ S
expect = np.zeros((9, 9))
for i, p in enumerate(c3.PRIM):
    expect[c3.PRIM.index(c3.theta(p)), i] = 1
g_mod = np.linalg.norm(ST3 - S2) < 1e-8
g_cc = np.allclose(S2, expect, atol=1e-9)
print(f"GATES: S unitary {uni:.1e}, symmetric {sym:.1e}; (ST)^3 = S^2: "
      f"{g_mod}; S^2 = theta-flip conjugation: {g_cc}")
assert g_mod and g_cc

# the theta-odd 3-space (pairs (27,27b), (351p,351pb), (351,351b))
pairs = [(1, 2), (3, 4), (7, 8)]
odd = np.zeros((9, 3))
for j, (a, b) in enumerate(pairs):
    odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
X = S.conj() @ T.conj() @ S                 # L = S^{-1} T^{-1} S (S unitary symmetric)
Rr, Lr = T, X
# the odd space is invariant (C = S^2 is central in the image): gate
inv_gap = max(np.linalg.norm((np.eye(9) - odd @ odd.T) @ M @ odd)
              for M in (Rr, Lr))
print(f"GATE: theta-odd 3-space invariant under R and L: off-block {inv_gap:.1e}")
assert inv_gap < 1e-9

# ---- A2: EXACT phase arithmetic (the decisive step) ----
print("\n== A2: the exact theta-odd T-phases (sympy Rational) ==")
c24 = c_exact / 24
podd = []
for j, (a, b) in enumerate(pairs):
    assert h_exact[a] == h_exact[b]         # conjugates share h => odd vec is a T-eigenvector
    p = sp.nsimplify((h_exact[a] - c24) % 1)
    podd.append(sp.Rational(p))
    print(f"  pair {c3.NAMES[a]:>5}: h = {h_exact[a]},  t = e^(2 pi i {p}) = zeta_84^{int(p*84)}")
assert [int(p * 84) for p in podd] == [13, 73, 61]
print("  c = 78/7, c/24 = 13/28 (exact)")
diffs = [(sp.Rational((podd[i] - podd[j]) % 1)) for i, j in [(1, 0), (2, 0), (2, 1)]]
orders = [sp.Rational(d).q for d in diffs]
print(f"  pairwise phase ratios: {[str(d) for d in diffs]} — orders {orders}")
assert orders == [7, 7, 7]
P = 7
print(f"  => |tr_odd(R^(n-2) L)|^2 = sum c_j cbar_i (t_j/t_i)^(n-2) has EXACT")
print(f"     period {P} in n (all ratios are PRIMITIVE 7th roots).  The E6")
print(f"     stage conductor kappa = 14 enters through its ODD PRIME 7;")
print(f"     the 2-part is modulus-invisible (a central phase).")
sev = [sp.nsimplify((7 * p) % 1) for p in podd]
print(f"  t_j^7 = e^(2 pi i {sev[0]}) for ALL three j: {sev[0] == sev[1] == sev[2]}"
      f"  => R^7 acts as the SCALAR zeta_12 on the theta-odd 3-space")
assert sev[0] == sev[1] == sev[2] == sp.Rational(1, 12)
t1o = sp.Rational(1, sp.gcd(13, 84))
print(f"  t(27) = zeta_84^13 has order 84 => full-value (reality) period 84 = 6*kappa")

# ---- A3: EXACT cyclotomic values in Q(zeta_84) ----
print("\n== A3: the EXACT landscape values (integer cyclotomics mod Phi_84) ==")
NC = 84
xsym = sp.symbols('x')
PHI84 = [int(cf) for cf in sp.Poly(sp.cyclotomic_poly(NC, xsym), xsym).all_coeffs()]
DEG = len(PHI84) - 1                        # 24


def cyc_reduce(v):
    """reduce a length-84 Fraction/int vector (coeffs of zeta^i) mod Phi_84."""
    r = [Fraction(x) for x in v]
    for i in range(len(r) - 1, DEG - 1, -1):
        c = r[i]
        if c:
            for k in range(1, len(PHI84)):
                r[i - k] -= c * PHI84[k]
            r[i] = Fraction(0)
    return r[:DEG]


def cyc_mul(u, v):
    out = [0] * NC
    for i, ui in enumerate(u):
        if ui:
            for j, vj in enumerate(v):
                if vj:
                    out[(i + j) % NC] += ui * vj
    return out


def cyc_conj(u):
    out = [0] * NC
    for i, ui in enumerate(u):
        out[(-i) % NC] += ui
    return out


def cyc_add(u, v):
    return [a + b for a, b in zip(u, v)]


def cyc_scal(c, u):
    return [c * x for x in u]


def cyc_rat(u):
    """assert the element is rational; return it as a Fraction."""
    r = cyc_reduce(u)
    assert all(x == 0 for x in r[1:]), "not rational!"
    return r[0]


def cyc_num(u):
    return sum(float(x) * np.exp(2j * np.pi * i / NC)
               for i, x in enumerate(u) if x)


# exact unnormalized S entries: U[a][b] = sum_w eps(w) zeta_84^{-6 ips}
U = {}
for a in range(9):
    for b in range(a, 9):
        ips6 = np.rint(6 * IPS[(a, b)]).astype(np.int64)
        assert np.max(np.abs(6 * IPS[(a, b)] - ips6)) < 1e-6
        idx = (-ips6) % NC
        vec = np.zeros(NC, dtype=np.int64)
        np.add.at(vec, idx, eps_signs)
        U[(a, b)] = U[(b, a)] = [int(x) for x in vec]
N2 = cyc_rat([sum(x) for x in
              zip(*[cyc_mul(U[(0, k)], cyc_conj(U[(0, k)])) for k in range(9)])])
print(f"  exact norm^2 = {N2} (numeric {norm2_num:.6f}: "
      f"match {abs(float(N2) - norm2_num) < 1e-6})")
assert abs(float(N2) - norm2_num) < 1e-6

# T-bar as zeta_84 monomials: exponent = -(h_k - 13/28)*84 (all integers)
tbar_idx = [int((-(h - c24) * 84) % 84) for h in h_exact]


def Xent(a, b):
    """exact (S-bar T-bar S)_{ab} * N2  (integer cyclotomic)."""
    acc = [0] * NC
    for k in range(9):
        m = cyc_mul(cyc_conj(U[(a, k)]), U[(k, b)])
        mono = [0] * NC
        mono[tbar_idx[k]] = 1
        acc = cyc_add(acc, cyc_mul(m, mono))
    return acc


Xjj_int = []                                # X_jj * (2 N2), integer cyclotomic
for (a, b) in pairs:
    v = cyc_add(cyc_add(Xent(a, a), Xent(b, b)),
                cyc_scal(-1, cyc_add(Xent(a, b), Xent(b, a))))
    Xjj_int.append(v)
    xnum = cyc_num(v) / (2 * float(N2))
    xref = (odd.T @ X @ odd)[len(Xjj_int) - 1, len(Xjj_int) - 1]
    assert abs(xnum - xref) < 1e-8, (xnum, xref)
print("  exact X_jj (theta-odd diag of S-bar T-bar S) cross-checked vs numerics: OK")

# tr_odd(n) = sum_j t_j^(n-2) X_jj ; exact |tr_odd|^2 for one full period
print("\n  the seven EXACT values |tr_odd(R^(n-2)L)|^2, n mod 7:")
texp = [13, 73, 61]
vals_exact = {}
for n in range(3, 10):
    z = [0] * NC
    for j in range(3):
        mono = [0] * NC
        mono[(texp[j] * (n - 2)) % NC] = 1
        z = cyc_add(z, cyc_mul(mono, Xjj_int[j]))
    m2 = cyc_rat(cyc_mul(z, cyc_conj(z))) / (4 * N2 * N2)
    vals_exact[n % 7] = m2
    print(f"    n = {n} (n mod 7 = {n % 7}):  |tr_odd|^2 = {m2}   "
          f"|tr_odd| = {'sqrt(2)' if m2 == 2 else str(m2 if m2 in (0, 1) else float(m2) ** .5)}")
assert vals_exact == {3: Fraction(1), 4: Fraction(1), 5: Fraction(2),
                      6: Fraction(0), 0: Fraction(1), 1: Fraction(0),
                      2: Fraction(2)}
print("  => THE E6 THREE-VALUE THEOREM (exact): |tr_odd| takes EXACTLY the")
print("     values {0, 1, sqrt2} on the metallic family, period 7:")
print("     n mod 7: 0 -> 1, +-1 -> 0 (DEAF), +-2 -> sqrt2, +-3 -> 1")
print("     (palindromic about n = 0 mod 7; the deaf residues are +-1).")

# ---- A4: the numeric landscape table n = 3..40 + three-term-sum gate ----
print("\n== A4: the landscape n = 3..44 (direct matrix product; 1e-9 gates) ==")
tnum = [np.exp(2j * np.pi * float(p)) for p in podd]
xnum = [cyc_num(v) / (2 * float(N2)) for v in Xjj_int]
ok3, table = True, []
for n in range(3, 45):
    Wm = np.linalg.matrix_power(Rr, n - 2) @ Lr
    tr = np.trace(odd.T @ Wm @ odd)
    tsum = sum(tnum[j] ** (n - 2) * xnum[j] for j in range(3))
    ok3 &= abs(tr - tsum) < 1e-8
    table.append((n, abs(tr), tr.imag))
assert ok3
print("  three-term sum == direct matrix product, 42/42: True")
mods = {0: '1', 1: '0', 2: 'sqrt2', 3: '1', 4: '1', 5: 'sqrt2', 6: '0'}
period_ok = all(abs(m - {0: 1, 1: 0, 2: 2 ** .5, 3: 1, 4: 1, 5: 2 ** .5,
                         6: 0}[n % 7]) < 1e-9 for n, m, _ in table)
print(f"  |tr_odd| == exact-theorem pattern (period 7), 42/42: {period_ok}")
assert period_ok
reals = [n for n, m, im in table if abs(im) < 1e-9]
print(f"  n = 3..44: |tr_odd| by n: " +
      " ".join(mods[n % 7] for n, _, _ in table[:14]) + " ...")
print(f"  REAL tr_odd at n = {reals} (residues mod 84 — the full-value lattice)")

# ---- A5: the shadow-class law over a word corpus ----
print("\n== A5: the shadow-class law |tr_odd(W)| = |chi_3dim(W mod 7)| ==")
# SL(2,7) and the PSL(2,7) conjugacy classifier (exact integer arithmetic)
Rm, Lm = ((1, 1), (0, 1)), ((1, 0), (1, 1))


def mmul(A, B, p=7):
    return (((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % p,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % p),
            ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % p,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % p))


def word_mat7(w):
    M = ((1, 0), (0, 1))
    for ch in w:
        M = mmul(M, Rm if ch == 'R' else Lm)
    return M


SL27 = []
for a, b, cq, d in itertools.product(range(7), repeat=4):
    if (a * d - b * cq) % 7 == 1:
        SL27.append(((a, b), (cq, d)))
assert len(SL27) == 336
orbit7A = set()
for h in SL27:
    hinv = ((h[1][1], (-h[0][1]) % 7), ((-h[1][0]) % 7, h[0][0]))
    g = mmul(mmul(h, Rm), hinv)
    orbit7A.add(g)
    orbit7A.add(tuple(tuple((-x) % 7 for x in row) for row in g))


def psl_class(M):
    Id, nId = ((1, 0), (0, 1)), ((6, 0), (0, 6))
    if M in (Id, nId):
        return '1A'
    Mk, k = M, 1
    while True:
        Mk, k = mmul(Mk, M), k + 1
        if Mk in (Id, nId):
            break
    if k == 2:
        return '2A'
    if k == 3:
        return '3A'
    if k == 4:
        return '4A'
    assert k == 7
    return '7A' if M in orbit7A else '7B'


CHI3 = {'1A': 3.0, '2A': 1.0, '3A': 0.0, '4A': 1.0,
        '7A': 2 ** .5, '7B': 2 ** .5}      # |chi| of the 3-dim of PSL(2,7)
MATS = {'R': Rr, 'L': Lr}


def tr_odd_E6(w):
    M = np.eye(9, dtype=complex)
    for ch in w:
        M = M @ MATS[ch]
    return np.trace(odd.T @ M @ odd)


corpus = ['R' * (n - 2) + 'L' for n in range(3, 45)]
for length in range(2, 9):
    corpus += [''.join(t) for t in itertools.product('RL', repeat=length)]
corpus += ['R' * 14, 'L' * 14, 'RL' * 7, 'R' * 7 + 'L' * 7]
corpus = sorted(set(corpus))
by_class = {}
for w in corpus:
    cl = psl_class(word_mat7(w))
    by_class.setdefault(cl, []).append((w, abs(tr_odd_E6(w))))
print(f"  corpus: {len(corpus)} words (family n=3..44, all length<=8 words, specials)")
law_ok = True
for cl in ['1A', '2A', '3A', '4A', '7A', '7B']:
    ms = [m for _, m in by_class[cl]]
    spread = max(ms) - min(ms)
    match = abs(ms[0] - CHI3[cl]) < 1e-9
    law_ok &= (spread < 1e-9) and match
    print(f"    class {cl}: {len(ms):4d} words, |tr_odd| = {ms[0]:.9f} "
          f"(spread {spread:.1e}), |chi_3dim| = {CHI3[cl]:.9f}, match: {match}")
assert law_ok
print("  => THE SHADOW-CLASS LAW HOLDS AT THE E6 STAGE:")
print("     |tr_odd(W)| = |chi_3dim(class of W mod 7)| for every word tested;")
print("     the E6 tone set = {0, 1, sqrt2, 3} (4 values over 6 classes).")

zr7 = tr_odd_E6('R' * 7)
print(f"  R^7 check: tr_odd = {zr7:.9f} = 3 zeta_12 "
      f"(exact phase 1/12): {abs(zr7 - 3 * np.exp(1j * np.pi / 6)) < 1e-9}")
assert abs(zr7 - 3 * np.exp(1j * np.pi / 6)) < 1e-9

print("\n  the three named general words at E6 (prereg):")
for w in ['RLRL', 'RRLL', 'RRRLLL']:
    z = tr_odd_E6(w)
    cl = psl_class(word_mat7(w))
    print(f"    {w:>7}: tr_odd = {z:+.6f}, |tr_odd| = {abs(z):.6f}, "
          f"class mod 7 = {cl}  (golden-stage values were phi-family; here {cl}-tone)")

# ---- A6: the split witnesses (each stage hears only its own shadow) ----
print("\n== A6: the split — the shadows do NOT transfer across stages ==")
w3, S3, T3, cc3 = b238.su3_data(2)
prs = [(i, w3.index((wt[1], wt[0]))) for i, wt in enumerate(w3)
       if (wt[1], wt[0]) > wt]
odd3 = np.zeros((len(w3), len(prs)))
for j, (a, b) in enumerate(prs):
    odd3[a, j], odd3[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
X3 = np.linalg.inv(S3) @ np.linalg.inv(T3) @ S3


def tr_odd_su32(w):
    M = np.eye(len(w3), dtype=complex)
    for ch in w:
        M = M @ (T3 if ch == 'R' else X3)
    return np.trace(odd3.T @ M @ odd3)


def word_mat(w, p):
    M = ((1, 0), (0, 1))
    Rp, Lp = ((1, 1), (0, 1)), ((1, 0), (1, 1))
    for ch in w:
        A, B = M, (Rp if ch == 'R' else Lp)
        M = (((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % p,
              (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % p),
             ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % p,
              (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % p))
    return M


wA, wB = 'R' + 'L', 'R' * 6 + 'L'           # n = 3 vs n = 8: same matrix mod 5
assert word_mat(wA, 5) == word_mat(wB, 5)
mA, mB = abs(tr_odd_E6(wA)), abs(tr_odd_E6(wB))
print(f"  E6 vs mod-5: n=3 and n=8 are THE SAME matrix mod 5, but "
      f"|tr_odd(E6)| = {mA:.6f} vs {mB:.6f}")
assert abs(mA - mB) > 0.5
wC, wD = 'R' + 'L', 'R' * 8 + 'L'           # n = 3 vs n = 10: same matrix mod 7
assert word_mat(wC, 7) == word_mat(wD, 7)
mC, mD = abs(tr_odd_su32(wC)), abs(tr_odd_su32(wD))
print(f"  SU(3)_2 vs mod-7: n=3 and n=10 are THE SAME matrix mod 7, but "
      f"|tr_odd(golden)| = {mC:.6f} vs {mD:.6f}")
assert abs(mC - mD) > 0.5
print("  => the golden stage does not factor mod 7; the E6 stage does not")
print("     factor mod 5.  STAGE-UNIVERSAL LAW FORM, STAGE-SPECIFIC SHADOW.")

# ============================================================
print("\n" + "=" * 72)
print("PART B — THE GENERATING FUNCTION (the mod-5 registered question)")
print("=" * 72)
q, s, nsym = sp.symbols('q s n')
PHI = (1 + sp.sqrt(5)) / 2
D2 = 3 * PHI * sp.sqrt(5)
closed = lambda n: 2 * sp.sqrt(3) / sp.sqrt(D2) * sp.Abs(sp.cos(sp.pi * sp.Rational(4 * n - 5, 10)))
chi0 = lambda n: 0 if n % 5 == 0 else 1
chi2 = lambda n: {0: 0, 1: 1, 2: -1, 3: -1, 4: 1}[n % 5]

print("\n== B1: the per-residue Dirichlet-character identity (exact sympy) ==")
print("  claim: a_n = ( phi*chi_0(n) + phi^(-2)*chi_2(n) ) / 2")


def achar(n):
    return sp.simplify((PHI * chi0(n) + PHI ** -2 * chi2(n)) / 2)


allok = True
for n in range(5, 10):                      # one full period, every residue
    lhs2 = sp.simplify(sp.expand(closed(n) ** 2))     # |.|^2: Abs-free
    rhs = achar(n)
    okr = (sp.simplify(sp.expand(lhs2 - rhs ** 2)) == 0) and rhs.evalf() >= 0
    allok &= okr
    print(f"    n mod 5 = {n % 5}: a = {sp.nsimplify(rhs)} "
          f"= (phi chi_0 + phi^-2 chi_2)/2: {okr}")
assert allok
print("  PROVED (5/5 residues, exact).  chi_0 = principal, chi_2 = Legendre (./5):")
print("  the two EVEN characters mod 5 — a_n is even in n, so only they enter;")
print("  the coefficients are phi/2 and 1/(2 phi^2)  (phi/2 IS the 4th tone).")

print("\n== B2: the sequence check against the banked stage (numeric, n=3..40) ==")
seq_ok = all(abs(abs(tr_odd_su32('R' * (n - 2) + 'L')) - float(closed(n).evalf()))
             < 1e-9 for n in range(3, 41))
print(f"  a_n from the SU(3)_2 stage build == closed form, 38/38: {seq_ok}")
assert seq_ok

print("\n== B3: the generating function (exact rational function) ==")
f_block = (q ** 3 / PHI + q ** 4 + q ** 6 + q ** 7 / PHI) / (1 - q ** 5)
F0 = (q + q ** 2 + q ** 3 + q ** 4) / (1 - q ** 5)          # sum chi_0(n) q^n
F2 = (q - q ** 2 - q ** 3 + q ** 4) / (1 - q ** 5)          # sum chi_2(n) q^n
f_char = (PHI * F0 + PHI ** -2 * F2) / 2 - (1 * q + (PHI - 1) * q ** 2)
ident = sp.simplify(sp.factor(f_block - f_char)) == 0
print("  f(q) := sum_(n>=3) a_n q^n = (q^3/phi + q^4 + q^6 + q^7/phi)/(1-q^5)")
print("        = (phi F_chi0(q) + phi^(-2) F_chi2(q))/2 - q - q^2/phi")
print(f"  rational-function identity (sympy exact): {ident}")
assert ident
ser = sp.series(f_block, q, 0, 12).removeO()
print(f"  series check: f = {sp.nsimplify(ser)}")
sok = all(sp.simplify(ser.coeff(q, n) - achar(n)) == 0 for n in range(3, 12))
print(f"  coefficients == the (proved) character values for n = 3..11 (exact): {sok}")
assert sok

print("\n== B4: the PRODUCT (Euler/L-function-product) form is REFUTED ==")
a3, a7, a21 = [sp.nsimplify(achar(n)) for n in (3, 7, 21)]
print(f"  a_3 a_7 = {sp.simplify(a3 * a7)} = phi^(-2), but a_21 = {a21}")
print(f"  (3,7 coprime, both in the family range) => a_n is NOT multiplicative:")
assert sp.simplify(a3 * a7 - a21) != 0
print("  no Euler product; 'factors as a product of L-functions' is REFUTED.")
print("  What IS true (corollary of B1, exact):")
print("    sum a_n n^(-s) = (phi/2)(1 - 5^(-s)) zeta(s) + (1/(2 phi^2)) L(s, chi_5)")
print("  — a LINEAR COMBINATION of the two even mod-5 L-functions (chi_5 = (./5)),")
print("  i.e. the Dirichlet-character-mod-5 shape holds ADDITIVELY, not as a product.")

print("\n== B5: the E6 analogue of the character form (bonus, exact) ==")
# b_n^2 in {1,0,2,1,1,2,0} for n mod 7 = 0..6; even chars mod 7: chi_0 + cubic pair
w3rt = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2          # omega, explicit radical
psi = {1: sp.Integer(1), 2: w3rt ** 2, 3: w3rt, 4: w3rt,
       5: w3rt ** 2, 6: sp.Integer(1)}      # the cubic even character (psi(3) = omega)
b2 = {0: 1, 1: 0, 2: 2, 3: 1, 4: 1, 5: 2, 6: 0}
e1 = sp.expand((2 * w3rt + w3rt ** 2) / 3)  # Fourier coeff of psi on classes (0,2,1)
ok6 = True
for n in range(7, 14):
    r = n % 7
    if r == 0:
        rhs = sp.Integer(1)                  # the forced delta term at 7|n
    else:
        rhs = sp.expand(1 + 2 * sp.re(sp.expand(e1 * psi[r])))
    ok6 &= sp.simplify(sp.expand(rhs - b2[r])) == 0
print(f"  b_n^2 = chi_0(n) + 2 Re[e1 psi(n)] + 1_(7|n),  e1 = {e1}: "
      f"verified 7/7 residues: {ok6}")
assert ok6
print("  NOTE the structural contrast: at the golden stage the deaf residue IS")
print("  the ramified one (5|n) so the principal character alone carries the")
print("  zero; at E6 the deaf residues are n = +-1 mod 7 (the 3A classes) and")
print("  7|n is LOUD — the delta term is forced.  The clean characters-only")
print("  form is a golden-stage specialty.")

print("\nALL GATES PASS — cell 3 complete")
