"""CELL W3-1 (R21-1) — THE KAPPA-UNCONDITIONAL RECIPROCITY FORM (B625's target).

BANKED CONDITIONAL (B625): the Deloup-Turaev Theorem-1 evaluation on the
auxiliary lattice W = Q(+)Q (Q = A2 root lattice) at level r = kappa matches
the twelve Weyl-Weil terms EXACTLY iff 3 | kappa; root cause = DT hypothesis
(1) [(r/2)<y,h(y)> in Z for all y in W* = P(+)P] fails whenever 3 nmid r,
because the dual pairing values land in (2/3)Z — the denominator is the A2
lattice discriminant [P:Q] = 3.

THE UNCONDITIONAL FORM (this cell): the conditional boundary is a
PRESENTATION artifact, not content.  Absorb the discriminant into the level:

  (U1)  At level r = 3*kappa the DT hypothesis reads (3k/2)(2m/3) = k*m in Z
        — satisfied for EVERY kappa.  The same theorem, same lattice, same
        h_w, applied at level 3*kappa, holds UNCONDITIONALLY.  (Phase 3:
        exact cyclotomic certification, all 12 terms, 10 kappa covering
        every resonant type and both 3-classes.)
  (U2)  Equivalently, in the presentation (Z^2, F_w = K*B_w) the form F_w is
        EVEN (verified exactly), so the classical even-form reciprocity
        S(F,N) = (N/sqrt(det F)) * i * Gamma_F(N)  holds at every level N;
        with N = 3*kappa this is precisely the banked closed form
        t_w(kappa) = Gamma_w(3 kappa)/(3 sqrt(det B_w))  — valid at EVERY
        kappa.  (Phase 2: exact cyclotomic certification on 26 rungs x 12
        terms + exact match to the banked cellR3 tables.)
  (U3)  The certificate structure IS the unconditional reciprocity data: the
        dual frequencies stored by the banked certificates are 3*q mod 2
        (cellR3 DUAL) resp. q = mu^T C6 B_w^{-1} mu on an EVEN lattice
        (cellG); in both cases the character sum is well-defined at every
        rung with no divisibility condition.  At level r with 3 nmid r the
        Q(+)Q-dual sum is NOT EVEN WELL-DEFINED on cosets (rep-dependent) —
        exhibited exactly (Phase 3b).  The E6 side is BORN unconditional
        because the E6 root lattice is even: nu^T C6 B_w nu in 2Z for all
        51840 Weyl elements (Phase 1e, exact).

House rules: exact arithmetic in every decisive step (integer counts +
integer cyclotomic vectors reduced mod Phi_M; Fractions everywhere else);
floats only as pre-gates / display.  New files only.

Machinery provenance: WEYL/K/h_w verbatim from B587 weil_mechanism.py /
B623 step3_reciprocity.py / B625 step4_diagnosis.py; the Cyc exact
cyclotomic class adapted from B666/cellR3 r3_e6_perterm.py (banked); banked
cross-anchors: cellR3 r3_su3_results.json per-term tables, cellG
l100_results.json support table (130 frequencies), B238 su32_wrt.py stage
data.

Run: python3 w31_unconditional.py   (~3-8 min)
"""
import importlib.util
import itertools
import json
import math
import os
import time
from collections import Counter
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

HERE = os.path.dirname(os.path.abspath(__file__))
CELLR3 = os.path.normpath(os.path.join(HERE, '..', 'cellR3', 'r3_su3_results.json'))
CELLG = os.path.normpath(os.path.join(
    HERE, '..', '..', 'B662_successor_campaign', 'cellG', 'l100_results.json'))
B238 = os.path.normpath(os.path.join(
    HERE, '..', '..', 'B238_su32_levelrank', 'su32_wrt.py'))

OUT = {}
GATES = {}
T0 = time.time()


def log(msg=""):
    print(msg, flush=True)


# ---------------------------------------------------------------- A2 data (banked)
K = sp.Matrix([[2, 1], [1, 2]])                    # 3 * weight-space form
OMEGA = sp.Matrix(sp.BlockDiagMatrix(K, K)) / 3    # Gram on weight coords (P(+)P = Z^4)
S1 = sp.Matrix([[-1, 0], [1, 1]])
S2 = sp.Matrix([[1, 1], [0, -1]])
WEYL = []
for word in ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)):
    M = sp.eye(2)
    for g in word:
        M = (S1 if g == 0 else S2) * M
    WEYL.append((M, (-1) ** len(word)))

# W = Q(+)Q basis in weight coordinates (columns = simple roots), verbatim B625
BW = sp.Matrix([[2, -1, 0, 0], [-1, 2, 0, 0], [0, 0, 2, -1], [0, 0, -1, 2]])

TERMS = []
for pm in (1, -1):
    for wi, (w0, sg) in enumerate(WEYL):
        w = pm * w0
        winv = w.inv()
        h = sp.Matrix(sp.BlockMatrix([[sp.eye(2), sp.eye(2) - winv],
                                      [sp.eye(2) - w, -sp.eye(2)]]))
        B = 3 * sp.eye(2) - w - winv
        F = K * B
        TERMS.append(dict(label=f"{'+' if pm > 0 else '-'}w{wi}", pm=pm, wi=wi,
                          w=w, sign=sg, h=h, B=B, F=F,
                          detB=int(B.det()), detF=int(F.det())))


def frac(x):
    r = sp.Rational(x)
    return Fraction(int(r.p), int(r.q))


def sig_descartes(Msym):
    """Exact signature of a symmetric rational matrix via Descartes on the
    characteristic polynomial (all roots real; det != 0 asserted)."""
    lam = sp.symbols('lam')
    p = Msym.charpoly(lam)
    cs = [c for c in p.all_coeffs()]
    assert cs[-1] != 0, "singular"
    def var(seq):
        seq = [s for s in seq if s != 0]
        return sum(1 for a, b in zip(seq, seq[1:]) if (a > 0) != (b > 0))
    pos = var(cs)
    neg = var([c * (-1) ** i for i, c in enumerate(cs)])
    assert pos + neg == Msym.shape[0]
    return pos - neg


# ---------------------------------------------------------------- exact cyclotomics
class Cyc:
    """Exact integer arithmetic in Z[zeta_M]: elements = integer coefficient
    tuples of length deg(Phi_M); reduction rows (zeta_M^k mod Phi_M) built by
    synthetic division (adapted from the banked cellR3 Cyc).  reduce() uses a
    guarded int64 matrix product (exact: bound asserted), falling back to
    python ints if the bound could be exceeded."""

    def __init__(self, M):
        self.M = M
        x = sp.symbols('x')
        phi = sp.Poly(sp.cyclotomic_poly(M, x), x)
        self.deg = int(phi.degree())
        pc = [int(c) for c in phi.all_coeffs()]        # monic: x^deg + tail
        tail = list(reversed(pc[1:]))                  # tail[i] = coeff of x^i
        rows = []
        cur = [0] * self.deg
        cur[0] = 1
        for _ in range(M):
            rows.append(list(cur))
            lead = cur[-1]
            cur = [0] + cur[:-1]                       # multiply by x, drop lead
            if lead:                                   # x^deg = -tail
                cur = [a - lead * t for a, t in zip(cur, tail)]
        # sanity: zeta^M = 1
        lead = None
        assert rows[0][0] == 1 and all(c == 0 for c in rows[0][1:])
        self.red = rows
        self.red_np = np.array(rows, dtype=np.int64)
        self.max_row = int(np.abs(self.red_np).max())

    def reduce(self, counts):
        total = sum(abs(c) for c in counts.values())
        if total * max(1, self.max_row) < 2 ** 62 and \
                all(abs(c) < 2 ** 62 for c in counts.values()):
            vec = np.zeros(self.M, dtype=np.int64)
            for k, c in counts.items():
                vec[k % self.M] += c
            out = vec @ self.red_np
            return tuple(int(v) for v in out)
        out = [0] * self.deg
        for k, c in counts.items():
            if c:
                rk = self.red[k % self.M]
                for i in range(self.deg):
                    out[i] += c * rk[i]
        return tuple(out)

    def is_zero(self, a):
        return all(x == 0 for x in a)


CYCS = {}


def cyc(M):
    if M not in CYCS:
        CYCS[M] = Cyc(M)
    return CYCS[M]


def conv(c1, c2, M):
    """product of two power-count dicts in Z[zeta_M] (exponents mod M)."""
    out = {}
    for a, ca in c1.items():
        if ca:
            for b, cb in c2.items():
                if cb:
                    k = (a + b) % M
                    out[k] = out.get(k, 0) + ca * cb
    return out


def scale_counts(c1, s):
    return {k: v * s for k, v in c1.items()}


def sqrt_counts(n, M):
    """counts dict for sqrt(n), n in {1,2,3,4,5,16,25,...}: integer part times
    sqrt3 (zeta12 + zeta12^11) and/or sqrt5 (1 + 2 zeta5 + 2 zeta5^4)."""
    rem = n
    intpart = 1
    for s in range(int(math.isqrt(n)), 0, -1):
        if rem % (s * s) == 0:
            intpart = s
            rem //= s * s
            break
    out = {0: intpart}
    if rem == 1:
        return out
    assert rem in (3, 5, 15), rem
    if rem % 3 == 0:
        assert M % 12 == 0
        out = conv(out, {M // 12: 1, (11 * M // 12) % M: 1}, M)
    if rem % 5 == 0:
        assert M % 5 == 0
        out = conv(out, {0: 1, M // 5: 2, (4 * M // 5) % M: 2}, M)
    return out


def lcm(a, b):
    return a * b // math.gcd(a, b)


# =================================================================== PHASE 1
log("=== CELL W3-1 / PHASE 1 — exact hypothesis certificates (12 terms) ===")
log("q(y) = <y, h_w(y)> on the DUAL lattice W* = P(+)P (weight coords = Z^4):")
p1_ok = True
for t in TERMS:
    h = t['h']
    S4 = OMEGA * h                                  # Gram of q on W* basis
    sym = sp.simplify(S4 - S4.T) == sp.zeros(4)
    # q(Z^4) subset (2/3)Z  <=>  diag in (2/3)Z and off-diag in (1/3)Z
    diag_ok = all(frac(S4[i, i]) * 3 % 2 == 0 and (frac(S4[i, i]) * 3).denominator == 1
                  for i in range(4))
    off_ok = all((frac(S4[i, j]) * 3).denominator == 1
                 for i in range(4) for j in range(4) if i != j)
    # obstruction witness: some y with q(y) = 2m/3, 3 nmid m
    wit = None
    for y in itertools.product(range(-1, 2), repeat=4):
        if y == (0, 0, 0, 0):
            continue
        q = frac((sp.Matrix(y).T * S4 * sp.Matrix(y))[0, 0])
        if q.denominator == 3:
            wit = (y, q)
            break
    # LHS well-definedness on W = Q(+)Q at EVERY level: G4 integer, even diag
    G4 = BW.T * S4 * BW
    g4_int = all(frac(G4[i, j]).denominator == 1 for i in range(4) for j in range(4))
    g4_even = all(frac(G4[i, i]) % 2 == 0 for i in range(4))
    # h(W*) subset W*  (h integer in weight coords)
    h_int = all(frac(h[i, j]).denominator == 1 for i in range(4) for j in range(4))
    deth = int(h.det())
    sigma = sig_descartes(S4)
    t['G4'] = np.array([[int(frac(G4[i, j])) for j in range(4)] for i in range(4)],
                       dtype=np.int64)
    t['deth'] = deth
    t['sigma'] = sigma
    ok = sym and diag_ok and off_ok and (wit is not None) and g4_int and g4_even and h_int
    ok &= (abs(deth) == t['detB'])
    p1_ok &= ok
    log(f"  {t['label']}: Omega*h sym {sym}; q(W*) in (2/3)Z {diag_ok and off_ok}; "
        f"den-3 witness q({wit[0]})={wit[1]}; G4 int+even {g4_int and g4_even}; "
        f"|det h| = {abs(deth)} == detB = {t['detB']}; sigma = {sigma:+d}  [{ok}]")
assert p1_ok, "HARD STOP: Phase 1 hypothesis certificates"
volW2 = (BW.T * OMEGA * BW).det()
log(f"  vol(W)^2 = det(BW^T Omega BW) = {volW2}  =>  vol(W*) = 1/3 exactly: {volW2 == 9}")
assert volW2 == 9
log("\n  => DT hypothesis (1) at level r:   (r/2) q(y) in Z for all y in W*.")
log("     q(W*) subset (2/3)Z with denominator 3 realized (witnesses above), so")
log("     it holds at level r  IFF  3 | r   — B625's conditional boundary.")
log("     At level r = 3 kappa:  (3k/2)(2m/3) = k m in Z  FOR EVERY kappa —")
log("     the boundary DISSOLVES into the level normalization  [P:Q] = 3.")
GATES['P1_hypothesis_certificates_12'] = True

# E6 side: the even-lattice statement for ALL 51840 Weyl elements
log("\n-- Phase 1e: E6 — nu^T C6 B_w nu in 2Z for ALL w (the ladder terms are")
log("   BORN unconditional: even root lattice, no [P:Q] denominator) --")
C6 = np.array([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
               [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]],
              dtype=np.int64)


def weyl_group_e6():
    gens = []
    for j in range(6):
        M = np.eye(6, dtype=np.int64)
        M[j, :] -= C6[:, j]
        gens.append(M)
    I = np.eye(6, dtype=np.int64)
    seen = {I.tobytes()}
    mats = [I]
    frontier = [I]
    while frontier:
        new = []
        for M in frontier:
            for g in gens:
                Mg = g @ M
                key = Mg.tobytes()
                if key not in seen:
                    seen.add(key)
                    new.append(Mg)
                    mats.append(Mg)
        frontier = new
    return np.array(mats)


W6 = weyl_group_e6()
assert len(W6) == 51840
C6adj = np.array(sp.Matrix(C6.tolist()).adjugate().tolist(), dtype=np.int64)
Ainv3 = np.einsum('ij,njk,kl->nil', C6adj, W6.transpose(0, 2, 1), C6)
assert (Ainv3 % 3 == 0).all(), "w^{-1} = C6^{-1} w^T C6 not integral"
W6inv = Ainv3 // 3
chk = np.einsum('nij,njk->nik', W6, W6inv)
assert (chk == np.eye(6, dtype=np.int64)).all()
B6 = 3 * np.eye(6, dtype=np.int64)[None, :, :] - W6 - W6inv
D6 = np.einsum('ij,njk->nik', C6, B6)
sym_all = (D6 == D6.transpose(0, 2, 1)).all()
even_all = (np.diagonal(D6, axis1=1, axis2=2) % 2 == 0).all()
log(f"   C6 B_w symmetric for all 51840: {sym_all};  diag(C6 B_w) even for all: {even_all}")
assert sym_all and even_all
GATES['P1e_e6_even_all_51840'] = True
log(f"   => the E6 character sums G_w(r) are coset-well-defined at EVERY r:")
log(f"      no divisibility condition exists at the E6 stage.  ({time.time()-T0:.1f}s)")

# =================================================================== PHASE 2
log("\n=== PHASE 2 — the even-form reciprocity at level 3 kappa, certified EXACTLY ===")
log("S(F_w, 3k) = (3k/sqrt(det F_w)) * i * Gamma_w(3k)   [F_w = K B_w EVEN, pos def]")
log("=> t_w(kappa) = Gamma_w(3 kappa)/(3 sqrt(det B_w))  at EVERY kappa.")

# F even + positive definite (exact)
for t in TERMS:
    F = t['F']
    assert F == F.T and all(F[i, i] % 2 == 0 for i in range(2))
    assert F[0, 0] > 0 and F.det() > 0
    assert t['detF'] == 3 * t['detB']
log("  F_w symmetric, EVEN diagonal, positive definite, det F = 3 det B: 12/12 exact")
GATES['P2_F_even_posdef_12'] = True


def dual_data_rank2(F):
    Fs = sp.Matrix(F.tolist()) if not isinstance(F, sp.Matrix) else F
    H = hermite_normal_form(Fs)
    Hn = np.array(H.tolist(), dtype=np.int64)
    assert Hn[1, 0] == 0
    detF = abs(int(Fs.det()))
    assert int(Hn[0, 0] * Hn[1, 1]) == detF
    Finv = Fs.inv()
    box = []
    for y0 in range(int(Hn[0, 0])):
        for y1 in range(int(Hn[1, 1])):
            y = sp.Matrix([y0, y1])
            box.append(frac((y.T * Finv * y)[0, 0]) % 2)
    return box


for t in TERMS:
    t['dual2'] = dual_data_rank2(t['F'])
    dl = 1
    for q in t['dual2']:
        dl = lcm(dl, q.denominator)
    t['denlcm2'] = dl

RUNGS2 = list(range(4, 25)) + [35, 40, 45, 60, 100]
banked_tables = json.load(open(CELLR3))['per_term_tables']
n2_pass = n2_tab = 0
t_p2 = time.time()
for kap in RUNGS2:
    N = 3 * kap
    for t in TERMS:
        M = lcm(lcm(2 * N, 12), 2 * t['denlcm2'])
        if t['detB'] % 5 == 0:
            M = lcm(M, 5)
        cy = cyc(M)
        # LHS: S(F,N) exact integer counts (numpy int64, values < 2N)
        F = t['F']
        f00, f01, f11 = int(F[0, 0]), int(F[0, 1]), int(F[1, 1])
        x = np.arange(N, dtype=np.int64)
        X1, X2 = np.meshgrid(x, x, indexing='ij')
        c = (f00 * X1 * X1 + 2 * f01 * X1 * X2 + f11 * X2 * X2) % (2 * N)
        bc = np.bincount(c.ravel(), minlength=2 * N)
        s_counts = {int(k * (M // (2 * N))): int(v) for k, v in enumerate(bc) if v}
        # RHS: Gamma(N) counts
        g_counts = {}
        for q in t['dual2']:
            e = Fraction((-N * q.numerator) % (2 * q.denominator), q.denominator)
            k = int(e * M / 2) % M
            g_counts[k] = g_counts.get(k, 0) + 1
        # identity * sqrt(detF):  sqrtF * S  ==  i * N * Gamma
        lhs = cy.reduce(conv(sqrt_counts(t['detF'], M), s_counts, M))
        rhs = cy.reduce(scale_counts({(k + M // 4) % M: v for k, v in g_counts.items()}, N))
        ok = lhs == rhs
        n2_pass += ok
        if not ok:
            log(f"  FAIL P2 identity {t['label']} kappa={kap} (M={M})")
        # banked-table gate:  Gamma == 3 sqrt(detB) * v_banked
        tab = banked_tables[t['label']]
        v = sp.sympify(tab['values'][kap % tab['period']])
        c0 = int(v.subs(sp.sqrt(5), 0))
        c1 = int(sp.expand(v - c0).coeff(sp.sqrt(5)))
        vcounts = {0: c0}
        if c1:
            assert M % 5 == 0
            vc5 = scale_counts(sqrt_counts(5, M), c1)
            for k2, vv in vc5.items():
                vcounts[k2] = vcounts.get(k2, 0) + vv
        rhs2 = cy.reduce(scale_counts(conv(sqrt_counts(t['detB'], M), vcounts, M), 3))
        lhs2 = cy.reduce(g_counts)
        ok2 = lhs2 == rhs2
        n2_tab += ok2
        if not ok2:
            log(f"  FAIL P2 table gate {t['label']} kappa={kap}")
tot2 = len(RUNGS2) * 12
log(f"  exact cyclotomic identity (Phi_M-reduced): {n2_pass}/{tot2} PASS "
    f"({len(RUNGS2)} rungs x 12 terms; rungs cover ALL residues mod 20 — every")
log(f"  resonant type 2|k, 4|k, 5|k, 20|k, generic — and both 3-classes)")
log(f"  banked cellR3 tables re-derived from Gamma: {n2_tab}/{tot2} exact "
    f"({time.time()-t_p2:.1f}s)")
GATES['P2_identity_exact_all'] = (n2_pass == tot2)
GATES['P2_banked_tables_exact_all'] = (n2_tab == tot2)
assert n2_pass == tot2 and n2_tab == tot2, "HARD STOP: Phase 2"

# float cross-anchor vs the actual Weil-trace matrix (B587 verbatim route)
log("\n-- P2 cross-anchor: matrix traces vs the closed form (float gate, k=4..14) --")
spec = importlib.util.spec_from_file_location("b238", B238)
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)
Knp = np.array([[2., 1.], [1., 2.]])
WEYLnp = [np.array([[int(w[i, j]) for j in range(2)] for i in range(2)])
          for w, _ in WEYL]


def build_G(kap):
    U = np.array([[0, -1], [1, 2]])
    Uinv = np.array([[2, 1], [-1, 0]])
    reps, index = [], {}

    def canon(mu):
        c = U @ mu
        return (int(c[0]) % kap, int(c[1]) % (3 * kap))

    for c1 in range(kap):
        for c2 in range(3 * kap):
            mu = Uinv @ np.array([c1, c2])
            index[(c1, c2)] = len(reps)
            reps.append(mu)
    return np.array(reps), index, canon


xa_max = 0.0
for kap in range(4, 15):
    reps, index, canon = build_G(kap)
    n = len(reps)
    q = np.einsum('ai,ij,aj->a', reps, Knp, reps) / 3.0
    T = np.exp(1j * np.pi * q / kap)
    pair = np.einsum('ai,ij,bj->ab', reps, Knp, reps) / 3.0
    Smat = np.exp(-2j * np.pi * pair / kap) / math.sqrt(n)
    Mrl = np.diag(T) @ (Smat.conj().T @ np.diag(T).conj() @ Smat)
    for t in TERMS:
        tmat = sum(Mrl[i, index[canon(t['pm'] * (WEYLnp[t['wi']] @ mu))]]
                   for i, mu in enumerate(reps))
        tab = banked_tables[t['label']]
        pred = complex(sp.sympify(tab['values'][kap % tab['period']]))
        xa_max = max(xa_max, abs(tmat - pred))
log(f"   max |matrix trace - closed form| over 11 kappa x 12 terms = {xa_max:.3e}")
assert xa_max < 1e-7
GATES['P2_matrix_cross_anchor'] = True

# =================================================================== PHASE 3
log("\n=== PHASE 3 — the DT form itself at level 3 kappa: the boundary dissolved ===")
log("sqrt|det h| * Sum_{x in W/rW} zeta_2r^{<x,hx>}  ==  3 * zeta_8^sigma * r^2 * Gamma4(r)")
log("(the B625 identity, exact cyclotomic; r = 3 kappa => valid at EVERY kappa)")


def dual_data_rank4(t):
    h = t['h']
    H = hermite_normal_form(h)
    Hn = np.array(H.tolist(), dtype=np.int64)
    assert all(Hn[i, j] == 0 for i in range(4) for j in range(4) if i > j)
    D = abs(t['deth'])
    assert int(np.prod(np.diagonal(Hn))) == D
    Shinv = OMEGA * h.inv()
    box = []
    for yv in itertools.product(*[range(int(Hn[i, i])) for i in range(4)]):
        y = sp.Matrix(yv)
        box.append((yv, frac((y.T * Shinv * y)[0, 0]) % 2))
    assert len(box) == D
    return box, Shinv


for t in TERMS:
    t['dual4'], t['Shinv'] = dual_data_rank4(t)
    dl = 1
    for _, q in t['dual4']:
        dl = lcm(dl, q.denominator)
    t['denlcm4'] = dl


def theta4_counts(G4, r):
    twoR = 2 * r
    n = np.arange(r, dtype=np.int64)
    N2, N3, N4 = np.meshgrid(n, n, n, indexing='ij')
    Q234 = (G4[1, 1] * N2 * N2 + G4[2, 2] * N3 * N3 + G4[3, 3] * N4 * N4
            + 2 * (G4[1, 2] * N2 * N3 + G4[1, 3] * N2 * N4 + G4[2, 3] * N3 * N4))
    L1 = 2 * (G4[0, 1] * N2 + G4[0, 2] * N3 + G4[0, 3] * N4)
    counts = np.zeros(twoR, dtype=np.int64)
    for n1 in range(r):
        c = (G4[0, 0] * n1 * n1 + n1 * L1 + Q234) % twoR
        counts += np.bincount(c.ravel(), minlength=twoR)
    return counts


def dt_check_exact(t, r):
    """exact check of the DT identity at level r for term t; returns bool."""
    M = lcm(lcm(2 * r, 4), 2 * t['denlcm4'])
    if abs(t['deth']) % 5 == 0:
        M = lcm(M, 20)
    cy = cyc(M)
    bc = theta4_counts(t['G4'], r)
    th_counts = {int(k * (M // (2 * r))): int(v) for k, v in enumerate(bc) if v}
    g_counts = {}
    for _, q in t['dual4']:
        e = Fraction((-r * q.numerator) % (2 * q.denominator), q.denominator)
        k = int(e * M / 2) % M
        g_counts[k] = g_counts.get(k, 0) + 1
    lhs = cy.reduce(conv(sqrt_counts(abs(t['deth']), M), th_counts, M))
    sig_shift = (t['sigma'] // 2) * (M // 4) % M      # zeta_8^sigma, sigma even
    rhs = cy.reduce(scale_counts({(k + sig_shift) % M: v for k, v in g_counts.items()},
                                 3 * r * r))
    return lhs == rhs


KAP3 = [4, 5, 6, 7, 8, 9, 10, 12, 15, 20]
n3_pass = 0
t_p3 = time.time()
for kap in KAP3:
    r = 3 * kap
    row = []
    for t in TERMS:
        ok = dt_check_exact(t, r)
        n3_pass += ok
        row.append(ok)
    log(f"  kappa = {kap:>2} (r = {r:>2}, 3|kappa: {kap % 3 == 0}): "
        f"{sum(row)}/12 exact  {'PASS' if all(row) else 'FAIL'}")
tot3 = len(KAP3) * 12
log(f"  DT at level 3 kappa: {n3_pass}/{tot3} EXACT over 10 kappa x 12 terms")
log(f"  (kappa covers 3|k and 3 nmid k, 2|k, 4|k, 5|k, 20|k, generic; "
    f"{time.time()-t_p3:.1f}s)")
GATES['P3_dt_level3k_exact_all'] = (n3_pass == tot3)
assert n3_pass == tot3, "HARD STOP: Phase 3"

# ------------------------------------------------- Phase 3b: the boundary exhibit
log("\n-- Phase 3b: the boundary at level r = kappa (B625's conditional, reproduced")
log("   exactly): PASS iff 3|kappa; and at 3 nmid r the dual sum is not even")
log("   well-defined on cosets (rep-dependence, exact) --")
bx_rows = []
for kap in (5, 6, 7, 9):
    row = [dt_check_exact(t, kap) for t in TERMS]
    expect = (kap % 3 == 0)
    ok = all(v == expect for v in row)
    bx_rows.append(ok)
    log(f"   r = kappa = {kap} (3|kappa: {expect}): identity exact-PASS on "
        f"{sum(row)}/12 terms — {'as the conditional predicts' if ok else 'UNEXPECTED'}")
GATES['P3b_boundary_slice'] = all(bx_rows)
assert all(bx_rows)

# rep-dependence: find an exact witness (z, y) with the coset-shift phase
# delta = 2<z,y> + <z,h(z)> of denominator 3, then compare Gamma4 exactly
t1 = next(t for t in TERMS if t['label'] == '+w1')


def gamma4_counts_shifted(t, r, idx, shift_z, M):
    hz = t['h'] * sp.Matrix(shift_z)
    g_counts = {}
    for i, (yv, q) in enumerate(t['dual4']):
        if i == idx and any(shift_z):
            y = sp.Matrix(yv) + hz
            q = frac((y.T * t['Shinv'] * y)[0, 0]) % 2
        e = Fraction((-r * q.numerator) % (2 * q.denominator), q.denominator)
        k = int(e * M / 2) % M
        g_counts[k] = g_counts.get(k, 0) + 1
    return g_counts


witness = None
for zv in itertools.product(range(-1, 2), repeat=4):
    if zv == (0, 0, 0, 0):
        continue
    z = sp.Matrix(zv)
    hz = t1['h'] * z
    zhz = frac((z.T * OMEGA * hz)[0, 0])
    for i, (yv, q0) in enumerate(t1['dual4']):
        zy = frac((z.T * OMEGA.T * sp.Matrix(yv))[0, 0])
        delta = (2 * zy + zhz) % 2
        if delta.denominator == 3:
            witness = (zv, i, yv, delta)
            break
    if witness:
        break
assert witness is not None, "no denominator-3 coset-shift witness found"
zv, idx, yv, delta = witness
log(f"   witness (term +w1): z = {zv}, box element y = {yv}: coset-shift phase")
log(f"   delta = 2<z,y> + <z,h(z)> = {delta} mod 2  (denominator 3) —")
log(f"   e^(-i pi r delta) != 1 whenever 3 nmid r: the level-r dual sum changes")
log(f"   with the choice of representatives.")
for r in (5, 15):
    M = lcm(lcm(2 * r, 4), lcm(2 * t1['denlcm4'], 20))
    M = lcm(M, 2 * 3 * t1['denlcm4'])        # shifted q may pick up /3 phases
    cy = cyc(M)
    g0 = cy.reduce(gamma4_counts_shifted(t1, r, idx, (0, 0, 0, 0), M))
    g1 = cy.reduce(gamma4_counts_shifted(t1, r, idx, zv, M))
    same = (g0 == g1)
    log(f"   term +w1, r = {r} (3|r: {r % 3 == 0}): Gamma4 with shifted rep "
        f"{'== unshifted (well-defined)' if same else '!= unshifted (NOT well-defined)'}")
    if r % 3 == 0:
        assert same
    else:
        assert not same
GATES['P3b_rep_dependence_exhibited'] = True
log("   => at 3 nmid r the level-r dual sum depends on the choice of coset reps:")
log("      the 'conditional failure' was never a failing identity — it is a")
log("      presentation without meaning outside 3|r.  The level-3k form is the")
log("      canonical well-defined statement, valid at every kappa.")

# =================================================================== PHASE 4
log("\n=== PHASE 4 — the aggregate unconditional form at E6 (cellG certificate) ===")
log("Z(r) = sum_q N_q e^{-i pi r q} over the 130-frequency support — valid at")
log("EVERY r (Phase 1e well-definedness); gated on 20 rungs covering every")
log("resonant type p in {2,3,5,7,11,19}:")
cellg = json.load(open(CELLG))
support = {}
for qs, row in cellg['support'].items():
    q = Fraction(qs)
    a = Fraction(row.get('coeff_sqrt1', '0'))
    b = Fraction(row.get('coeff_sqrt5', '0'))
    support[q] = (a, b)
assert len(support) == 130
mp.mp.dps = 50
s5 = mp.sqrt(5)
NAMED = {13: (1, 0), 16: (0, 0), 19: (2, 0), 20: (1, 0), 25: (0, 0), 29: (0, 0),
         35: (0, -1), 36: (-2, 0), 40: (2, -1), 45: (1, 0), 48: (3, 0),
         55: (1, -1), 57: (2, 0), 60: (1, -1), 63: (-1, 0), 70: (0, -1),
         72: (3, 0), 76: (2, 0), 95: (2, 0), 100: (1, 0)}
p4_max = mp.mpf(0)
p4_ok = True
for r, (a0, b0) in NAMED.items():
    z = mp.mpc(0)
    for q, (a, b) in support.items():
        e = (r * q) % 2
        coef = mp.mpf(a.numerator) / a.denominator + \
            (mp.mpf(b.numerator) / b.denominator) * s5
        z += coef * mp.e ** (-1j * mp.pi * mp.mpf(e.numerator) / e.denominator)
    target = a0 + b0 * s5
    dev = abs(z - target)
    p4_max = max(p4_max, dev)
    ok = dev < mp.mpf('1e-30')
    p4_ok &= ok
    val = f"{a0}" + (f"{b0:+d}*sqrt5" if b0 else "")
    log(f"   Z({r:>3}) = {val:>12}   dev = {mp.nstr(dev, 3)}  [{'OK' if ok else 'FAIL'}]")
log(f"   max dev over 20 rungs at dps 50: {mp.nstr(p4_max, 3)}  (quantize 1e-30)")
GATES['P4_aggregate_20_rungs'] = bool(p4_ok)
assert p4_ok

# =================================================================== SUMMARY
log("\n=== GATE SUMMARY ===")
for k, v in GATES.items():
    log(f"  {k}: {'PASS' if v else 'FAIL'}")
verdict = all(GATES.values())
OUT['gates'] = {k: bool(v) for k, v in GATES.items()}
OUT['rungs_phase2'] = RUNGS2
OUT['kappas_phase3'] = KAP3
OUT['terms'] = [dict(label=t['label'], detB=t['detB'], detF=t['detF'],
                     deth=t['deth'], sigma=t['sigma'],
                     denlcm2=t['denlcm2'], denlcm4=t['denlcm4']) for t in TERMS]
OUT['phase2_counts'] = dict(identity=n2_pass, tables=n2_tab, total=tot2)
OUT['phase3_counts'] = dict(identity=n3_pass, total=tot3)
OUT['matrix_cross_anchor_maxdev'] = xa_max
OUT['phase4_maxdev'] = float(p4_max)
OUT['runtime_s'] = round(time.time() - T0, 2)
with open(os.path.join(HERE, 'w31_results.json'), 'w') as f:
    json.dump(OUT, f, indent=1, default=str)
log(f"\nresults -> w31_results.json   ({OUT['runtime_s']}s)")

if verdict:
    log("""
VERDICT: THE UNCONDITIONAL FORM IS ESTABLISHED.

  For EVERY kappa (no divisibility condition):
      t_w(kappa) = Gamma_w(3 kappa) / (3 sqrt(det B_w))      [12 SU(3) terms]
      Z(r)       = sum_q N_q e^{-i pi r q}                   [E6 aggregate]
  with the reciprocity input the even-form theorem at level N = 3 kappa
  (DT Theorem 1 in the presentation (Z^2, F_w = K B_w), F_w even — hypothesis
  holds at every level).  B625's 3|kappa boundary was a PRESENTATION artifact:
  the same theorem on W = Q(+)Q at level kappa has dual values in (2/3)Z
  ([P:Q] = 3), and at 3 nmid r its dual sum is not even coset-well-defined;
  at level 3 kappa the hypothesis reads kappa*m in Z — always true.  The
  conditional boundary dissolves into the certificate structure: the banked
  dual tables store exactly the level-3k frequencies (3q mod 2), and the E6
  ladder is born unconditional (even root lattice, all 51840 elements).""")
else:
    log("\nVERDICT: incomplete — see gate summary")
