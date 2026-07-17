"""CELL R3 (part 1) — the SU(3) per-term Landsberg-Schaar closed form (L24(c) + L82 residual).

TARGET (triage R3 / B587 residual): prove the per-term closed form for the twelve
Gauss terms t_{pm w}(kappa) = tr(rho_Weil(RL) . P_{pm w}) of B587's Weyl-twisted
Weil factorization at SU(3) — LAW-O's per-term mechanism.

THE DERIVATION (each step gated below):
  (I1)  rho(L)_{mu,nu} = (g0/n) e^{i pi |mu-nu|^2 / kappa}   [exact Gaussian
        completion of the square in the S-conjugation sum; lemma],
        hence  t_{pm w}(kappa) = (g0/n) * Theta_{pm w}(kappa),
        Theta_{pm w}(kappa) = sum_{mu in P/kQ} e^{i pi F_{pm w}[mu] / (3 kappa)},
        F_{pm w} = K + (I -/+ w)^T K (I -/+ w),  K = 3*(weight-space form) = [[2,1],[1,2]].
  (I2)  THE STRUCTURE IDENTITY:  F_{pm w} = K * B_{pm w},
        B_{pm w} = 3I -/+ (w + w^{-1})    [proof: w^T K w = K => w^T K = K w^{-1};
        F = 2K - Kw - w^T K + w^T K w = 3K - K(w + w^{-1}) = K B].
        This is the SAME B_w-shape as the banked E6 ladder terms (P_WORD = 3
        = tr(A_RL)): the cross-stage reciprocity family.
  (I3)  THE TONE-CONDUCTOR IDENTITY:  det(A x (pm w) - I_4) = det(pm w) * det(B_{pm w})
        [proof: eigenvalues; (a l - 1)(a^{-1} l - 1) = l^2 - 3l + 1 = -l(3 - l - l^{-1})
        for tr A = 3, det A = 1, so the product over eig(w) gives det(w) det(3I - w - w^{-1})].
        B587's registered conductor menu is reproduced exactly.
  (I4)  g0(kappa) = sum_{mu} e^{-i pi |mu|^2/kappa} = -i sqrt(3) kappa   [its own
        reciprocity instance: the dual sum for F = -K is 1 + 2 e^{2 pi i kappa} = 3].
  (I5)  RECIPROCITY (the standard multivariate Landsberg-Schaar / Krazer input, the
        B204 pattern; F even, positive definite => signature 2):
        Theta_{pm w}(kappa) = (1/3) S(F, 3kappa),
        S(F, N) = sum_{x in Z^2/NZ^2} e^{i pi F[x]/N}
                = (N / sqrt(det F)) * e^{i pi/2} * Gamma_F(N),
        Gamma_F(N) = sum_{y in Z^2/F Z^2} e^{-i pi N F^{-1}[y]}.
        Combining (I1)-(I5), kappa cancels COMPLETELY:

        >>>  t_{pm w}(kappa) = Gamma_{pm w}(3 kappa) / (3 sqrt(det B_{pm w}))  <<<

        a finite quadratic-Gauss sum on Z^2/(K B)Z^2 — periodic in kappa with period
        L_w = lcm of ord(3 F^{-1}[y]) — evaluated EXACTLY (cyclotomic integers) on
        every residue: the per-term closed form, valid for ALL kappa.
  (I6)  LAW-O ASSEMBLY: tr_odd(kappa) = (1/12) sum_w sign(w)(t_{+w} + t_{-w})
        == [4|kappa] - [5|kappa]/phi  verified EXACTLY over the full period 20
        => LAW-O proven for all kappa >= 4 (modulo the standard reciprocity input,
        itself verified to 0 mismatches over kappa = 4..200 below).
        LAW-E's channel gets its explicit 20-periodic exact closed form the same way.

House rules: exact arithmetic in every decisive step (Fractions + integer cyclotomic
vectors mod Phi_M); floats only for the identity gates (B204 standard: the standard
reciprocity inputs verified as exact identities, 0 mismatches). New files only.
Run: python3 r3_su3_perterm.py  (~2-4 min).
Provenance: WEYL/monodromy/group construction verbatim from
frontier/B587_weil_mechanism/weil_mechanism.py (banked); B238 stage data imported
for the (D)-gate as in B587.
"""
import importlib.util
import json
import math
import os
import time
from collections import Counter
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = {}
T0 = time.time()


def log(msg=""):
    print(msg, flush=True)


# ---------------------------------------------------------------- banked constructions
K = np.array([[2, 1], [1, 2]])                     # 3 * weight-space form of A2
QB = np.array([[2, -1], [-1, 2]])                  # A2 Cartan;  K @ QB = 3I
S1 = np.array([[-1, 0], [1, 1]])
S2 = np.array([[1, 1], [0, -1]])
WEYL = []
for word in ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)):
    M = np.eye(2, dtype=int)
    for g in word:
        M = (S1 if g == 0 else S2) @ M
    WEYL.append((M, (-1) ** len(word)))
A_RL = np.array([[1, 1], [0, 1]]) @ np.array([[1, 0], [1, 1]])   # golden monodromy, tr 3

TERMS = []                                          # (label, pm, wi, w, sign, B, F)
for pm in (1, -1):
    for wi, (w, sg) in enumerate(WEYL):
        wpm = pm * w
        winv = np.rint(np.linalg.inv(wpm)).astype(int)
        B = 3 * np.eye(2, dtype=int) - wpm - winv
        F = K + (np.eye(2, dtype=int) - wpm).T @ K @ (np.eye(2, dtype=int) - wpm)
        TERMS.append(dict(label=f"{'+' if pm > 0 else '-'}w{wi}", pm=pm, wi=wi,
                          w=wpm, sign=sg, B=B, F=F))


def build_G(kap):
    """P/kappa Q as weight-coordinate representatives (verbatim B587 pattern)."""
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


# ================================================================ PHASE A — identities
log("=== CELL R3 / SU(3) — the per-term Landsberg-Schaar closed form ===")
log(f"golden monodromy A = {A_RL.tolist()},  tr = {np.trace(A_RL)}")

log("\n-- A1/A2: F = K*B and the tone-conductor identity (exact integers, 12 terms) --")
a12_ok = True
menu = {}
for t in TERMS:
    okF = (t['F'] == K @ t['B']).all()
    d = round(np.linalg.det(np.kron(A_RL, t['w']) - np.eye(4)))
    pred = round(np.linalg.det(t['w'])) * round(np.linalg.det(t['B']))
    okD = (d == pred)
    a12_ok &= okF and okD
    detB = round(np.linalg.det(t['B']))
    menu[t['label']] = d
    log(f"  {t['label']}: F==K*B {okF}  det B = {detB:>2}  "
        f"det(A(x)w - I4) = {d:>3} == det(w)*detB = {pred:>3}  {okD}")
assert a12_ok, "HARD STOP: structure/conductor identity failed"
# B587's registered menu (FINDINGS (M), golden): {+w0:1, -w0:25, +rot:16, -rot:4, refl:-5}
b587_menu_ok = (menu['+w0'] == 1 and menu['-w0'] == 25 and menu['+w3'] == 16
                and menu['+w4'] == 16 and menu['-w3'] == 4 and menu['-w4'] == 4
                and all(menu[f'{s}w{i}'] == -5 for s in '+-' for i in (1, 2, 5)))
log(f"  B587 registered golden menu reproduced: {b587_menu_ok}")
assert b587_menu_ok
OUT['A12_identities'] = True
OUT['conductor_menu'] = menu

log("\n-- A3: matrix trace == Gauss formula t = (g0/n) Theta  (kappa = 4..14, 12 terms) --")
a3_max = 0.0
g0_max = 0.0
for kap in range(4, 15):
    reps, index, canon = build_G(kap)
    n = len(reps)
    q = np.einsum('ai,ij,aj->a', reps, K, reps) / 3.0
    g0 = np.exp(-1j * np.pi * q / kap).sum()
    g0_max = max(g0_max, abs(g0 - (-1j * math.sqrt(3) * kap)))
    T = np.exp(1j * np.pi * q / kap)
    pair = np.einsum('ai,ij,bj->ab', reps, K, reps) / 3.0
    S = np.exp(-2j * np.pi * pair / kap) / math.sqrt(n)
    Mrl = np.diag(T) @ (S.conj().T @ np.diag(T).conj() @ S)
    for t in TERMS:
        tmat = sum(Mrl[i, index[canon(t['pm'] * (WEYL[t['wi']][0] @ mu))]]
                   for i, mu in enumerate(reps))
        qf = np.einsum('ai,ij,aj->a', reps, t['F'], reps) / 3.0
        tg = (g0 / n) * np.exp(1j * np.pi * qf / kap).sum()
        a3_max = max(a3_max, abs(tmat - tg))
log(f"  max |matrix - Gauss| over 11 kappa x 12 terms = {a3_max:.3e}")
log(f"  max |g0 - (-i sqrt3 kappa)| (I4)              = {g0_max:.3e}")
assert a3_max < 1e-7 and g0_max < 1e-7, "HARD STOP: A3/I4"
OUT['A3_matrix_vs_gauss_maxdev'] = a3_max
OUT['I4_g0_maxdev'] = g0_max

log("\n-- A5/A6: the reciprocity identity t == Gamma(3 kappa)/(3 sqrt(detB)) --")
log("   (the standard multivariate Landsberg-Schaar input, B204 pattern:")
log("    verified as an exact identity, target 0 mismatches)")


def dual_data(F):
    """Z^2/FZ^2 box (column-HNF) + exact Fractions F^{-1}[y]."""
    Fs = sp.Matrix(F.tolist())
    from sympy.matrices.normalforms import hermite_normal_form
    H = np.array(hermite_normal_form(Fs).tolist(), dtype=np.int64)
    detF = abs(int(Fs.det()))
    assert H[1, 0] == 0  # upper triangular column HNF
    Finv = Fs.inv()
    box = []
    for y0 in range(int(H[0, 0])):
        for y1 in range(int(H[1, 1])):
            y = sp.Matrix([y0, y1])
            qv = (y.T * Finv * y)[0, 0]
            box.append(Fraction(int(sp.fraction(qv)[0]), int(sp.fraction(qv)[1]))
                       if not isinstance(qv, sp.Rational) else Fraction(qv.p, qv.q))
    assert len(box) == int(H[0, 0]) * int(H[1, 1]) == detF
    return box, detF


DUAL = {}
for t in TERMS:
    box, detF = dual_data(t['F'])
    detB = round(np.linalg.det(t['B']))
    assert detF == 3 * detB
    # period in kappa of Gamma(3 kappa): phases e^{-i pi 3 kappa q}, q = F^{-1}[y]
    L = 1
    mult = Counter()
    for qv in box:
        e = (3 * qv) % 2
        mult[e] += 1
        a, b = e.numerator, e.denominator
        o = 1 if a == 0 else (2 * b if a % 2 else b)
        L = L * o // math.gcd(L, o)
    DUAL[t['label']] = dict(mult=mult, detF=detF, detB=detB, period=L)

# float gate over the full range kappa = 4..200
rec_max = 0.0
for kap in range(4, 201):
    reps = None
    # Theta via the direct P/kQ sum (float; O(3 kap^2))
    U = np.array([[2, 1], [-1, 0]])  # Uinv
    c1 = np.arange(kap)
    c2 = np.arange(3 * kap)
    g1, g2 = np.meshgrid(c1, c2, indexing='ij')
    mu0 = 2 * g1 + g2
    mu1 = -g1
    for t in TERMS:
        F = t['F']
        qf = (F[0, 0] * mu0 * mu0 + 2 * F[0, 1] * mu0 * mu1 + F[1, 1] * mu1 * mu1) / 3.0
        theta = np.exp(1j * np.pi * qf / kap).sum()
        tval = (-1j * math.sqrt(3) * kap / (3 * kap ** 2)) * theta
        # closed-form side
        # mult stores e = (3*q) mod 2, so the phase at level kappa is (kappa*e) mod 2
        gam = sum(c * np.exp(-1j * np.pi * float((kap * qv) % 2))
                  for qv, c in DUAL[t['label']]['mult'].items())
        rhs = gam / (3 * math.sqrt(DUAL[t['label']]['detB']))
        rec_max = max(rec_max, abs(tval - rhs))
log(f"  float gate, kappa = 4..200 x 12 terms: max |t - Gamma/(3 sqrt detB)| = {rec_max:.3e}")
assert rec_max < 1e-6, "HARD STOP: reciprocity float gate"

# high-precision subsample (dps 40)
mp.mp.dps = 40
hp_max = mp.mpf(0)
for kap in (4, 5, 7, 8, 10, 12, 13, 16, 20, 24, 40, 60, 100, 144, 200):
    for t in TERMS:
        F = t['F']
        f00, f01, f11 = int(F[0, 0]), int(F[0, 1]), int(F[1, 1])
        tot = mp.mpc(0)
        for a in range(kap):
            for b in range(3 * kap):
                m0, m1 = 2 * a + b, -a
                qf = Fraction(f00 * m0 * m0 + 2 * f01 * m0 * m1 + f11 * m1 * m1, 3)
                e = Fraction(qf, kap) % 2
                tot += mp.e ** (1j * mp.pi * mp.mpf(e.numerator) / e.denominator)
        tval = (-1j * mp.sqrt(3) * kap / (3 * kap ** 2)) * tot
        gam = mp.mpc(0)
        for qv, c in DUAL[t['label']]['mult'].items():
            e = (kap * qv) % 2          # mult stores e = (3*q) mod 2 already
            gam += c * mp.e ** (-1j * mp.pi * mp.mpf(e.numerator) / e.denominator)
        rhs = gam / (3 * mp.sqrt(DUAL[t['label']]['detB']))
        hp_max = max(hp_max, abs(tval - rhs))
log(f"  dps-40 gate, 15 kappa x 12 terms: max dev = {mp.nstr(hp_max, 3)}")
assert hp_max < mp.mpf('1e-30'), "HARD STOP: reciprocity dps-40 gate"
OUT['A6_reciprocity_float_maxdev_k4_200'] = rec_max
OUT['A6_reciprocity_dps40_maxdev'] = float(hp_max)

# ================================================================ PHASE B — exact tables
log("\n=== PHASE B — the twelve exact per-term closed forms ===")
log("t_{pm w}(kappa) = Gamma_{pm w}(3 kappa)/(3 sqrt(det B)),  period L_w; exact values:")
M_CYC = 40                                          # zeta_40 covers zeta_8, zeta_5, i, sqrt5
zeta = [sp.exp(2 * sp.pi * sp.I * sp.Rational(k, M_CYC)) for k in range(M_CYC)]


def gamma_exact(mult, kap_res):
    """Gamma(3 kappa) for kappa ≡ kap_res, as an exact sympy number."""
    tot = sp.Integer(0)
    for qv, c in mult.items():
        e = (kap_res * qv) % 2              # mult stores e = (3*q) mod 2 already
        # e^{-i pi e} = zeta_{M}^{-e*M/2}
        expo = Fraction(-e * M_CYC, 2)
        assert expo.denominator == 1, (e, expo)
        tot += c * zeta[int(expo) % M_CYC]
    return sp.simplify(sp.expand(tot))


tables = {}
period_all = 1
for t in TERMS:
    d = DUAL[t['label']]
    L = d['period']
    period_all = period_all * L // math.gcd(period_all, L)
    vals = []
    for r in range(L):
        g = gamma_exact(d['mult'], r)
        tv = sp.radsimp(sp.simplify(g / (3 * sp.sqrt(d['detB']))))
        vals.append(sp.nsimplify(tv, [sp.sqrt(5)]))
    tables[t['label']] = dict(period=L, detB=d['detB'], sign=t['sign'], values=vals)
    log(f"  {t['label']} (detB {d['detB']:>2}, sign {t['sign']:+d}, period {L}): "
        f"t(kappa) for kappa mod {L} = {[sp.sstr(v) for v in vals]}")
OUT['per_term_tables'] = {lab: dict(period=v['period'], detB=v['detB'], sign=v['sign'],
                                    values=[sp.sstr(x) for x in v['values']])
                          for lab, v in tables.items()}
log(f"  assembly period lcm = {period_all}")

log("\n-- B-gate: exact tables vs the matrix traces (kappa = 4..14, dev vs A3 values) --")
bt_max = 0.0
for kap in range(4, 15):
    reps, index, canon = build_G(kap)
    n = len(reps)
    q = np.einsum('ai,ij,aj->a', reps, K, reps) / 3.0
    T = np.exp(1j * np.pi * q / kap)
    pair = np.einsum('ai,ij,bj->ab', reps, K, reps) / 3.0
    S = np.exp(-2j * np.pi * pair / kap) / math.sqrt(n)
    Mrl = np.diag(T) @ (S.conj().T @ np.diag(T).conj() @ S)
    for t in TERMS:
        tmat = sum(Mrl[i, index[canon(t['pm'] * (WEYL[t['wi']][0] @ mu))]]
                   for i, mu in enumerate(reps))
        tab = tables[t['label']]
        pred = complex(tab['values'][kap % tab['period']])
        bt_max = max(bt_max, abs(tmat - pred))
log(f"  max |matrix - closed form| = {bt_max:.3e}")
assert bt_max < 1e-7, "HARD STOP: closed-form vs matrix gate"
OUT['B_closedform_vs_matrix_maxdev'] = bt_max

log("\n-- B-gate 2: B587's per-term firing rules (FINDINGS (M), golden) --")
fire_ok = True
tab = tables['-w0']            # d = 25 term: +5 at 5|kappa
fire_ok &= all(tab['values'][r % tab['period']] == 5 for r in range(0, 20, 5))
tab = tables['+w3']            # d = 16 rotations: +4 at 4|kappa
fire_ok &= all(tab['values'][r % tab['period']] == 4 for r in range(0, 20, 4))
tab = tables['-w3']            # d = 4 rotations: +2 at 2|kappa
fire_ok &= all(tab['values'][r % tab['period']] == 2 for r in range(0, 20, 2))
fire_ok &= all(v == 1 for v in tables['+w0']['values'])   # identity: constant 1
# reflections (d = -5): sqrt5-firing at 5|kappa, Legendre oscillation otherwise
s5 = sp.sqrt(5)
tab = tables['+w1']
leg = {1: 1, 4: 1, 2: -1, 3: -1}
refl_expect = [ -s5 if r % 5 == 0 else None for r in range(tab['period'])]
refl_fire = sp.simplify(tab['values'][0] + s5) == 0 or sp.simplify(tab['values'][0] - s5) == 0
log(f"  -w0(+5 at 5|k) +w3(+4 at 4|k) -w3(+2 at 2|k) +w0(==1): {fire_ok}")
log(f"  reflection term at 5|kappa is +-sqrt5: {refl_fire}; full reflection table: "
    f"{[sp.sstr(v) for v in tables['+w1']['values']]}")
assert fire_ok and refl_fire
OUT['B587_firing_rules'] = True

# ================================================================ PHASE C — LAW-O/LAW-E
log("\n=== PHASE C — LAW-O and LAW-E for ALL kappa (exact assembly over the full period) ===")
phi = (1 + sp.sqrt(5)) / 2
law_o_ok, law_e_vals = True, []
for r in range(period_all):
    odd = sp.Integer(0)
    even = sp.Integer(0)
    for wi in range(6):
        sg = WEYL[wi][1]
        tp = tables[f'+w{wi}']
        tm = tables[f'-w{wi}']
        vp = tp['values'][r % tp['period']]
        vm = tm['values'][r % tm['period']]
        odd += sg * (vp + vm)
        even += sg * (vp - vm)
    odd = sp.simplify(odd / 12)
    even = sp.simplify(even / 12)
    target = (1 if r % 4 == 0 else 0) - (1 / phi if r % 5 == 0 else 0)
    ok = sp.simplify(odd - target) == 0
    law_o_ok &= ok
    law_e_vals.append(even)
    log(f"  kappa ≡ {r:>2} (mod 20): tr_odd = {sp.sstr(odd):>20}  == LAW-O {ok}   "
        f"tr_even = {sp.sstr(even)}")
assert law_o_ok, "HARD STOP: LAW-O assembly"
log("\n  LAW-O = [4|kappa] - [5|kappa]/phi  PROVEN for ALL kappa >= 4")
log("  (exact on the full period 20; reciprocity input verified 0 mismatches above)")
OUT['LAW_O_proven_all_kappa'] = True
OUT['LAW_E_closed_form_period20'] = [sp.sstr(v) for v in law_e_vals]

# banked even values (B587 FINDINGS): kappa=6:-1, 7:+1, 8:+1, 10:-1, 12:+1, 13:+1, 14:-1
banked_even = {6: -1, 7: 1, 8: 1, 10: -1, 12: 1, 13: 1, 14: -1}
be_ok = all(sp.simplify(law_e_vals[k % 20] - v) == 0 for k, v in banked_even.items())
log(f"  banked B587 even values (kappa = 6..14) reproduced from the closed form: {be_ok}")
assert be_ok
OUT['LAW_E_banked_values'] = be_ok

# ================================================================ PHASE D — (D)-gate vs B238
log("\n=== PHASE D — the (D)-identity from the closed forms vs banked B238 Z values ===")
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)
d_max = 0.0
for kap in range(4, 17):
    k = kap - 3
    w3, S3, T3, c3 = b238.su3_data(k)
    zB = b238.wrt_trace(S3, T3, "RL")
    z_closed = sum(WEYL[wi][1] * complex(tables[f'+w{wi}']['values']
                   [kap % tables[f'+w{wi}']['period']]) for wi in range(6)) / 6.0
    d_max = max(d_max, abs(z_closed - zB))
log(f"  max |Z_closedform - Z_banked(B238)| over kappa = 4..16: {d_max:.3e}")
assert d_max < 1e-6, "HARD STOP: (D)-gate"
OUT['D_gate_vs_B238_maxdev'] = d_max

log("\n=== THE CROSS-STAGE STATEMENT ===")
log("  SU(3) per-term dual:  t_{pm w}(kappa) = Gamma(3 kappa)/(3 sqrt det B),")
log("      Gamma over Z^2/(K B_{pm w})Z^2,  B_{pm w} = 3I -/+ (w + w^{-1}),  tr(A_RL) = 3;")
log("  E6 ladder class term (banked B646/B651/B662-G):  G_w(r) over Z^6/B_w Z^6,")
log("      B_w = 3I - w - w^{-1},  q = mu^T C6 B_w^{-1} mu,  SAME P_WORD = 3.")
log("  => one reciprocity family across the two stages (L100's cross-stage point,")
log("     now a family); the E6-side per-class closed form is certified in part 2.")

OUT['runtime_s'] = round(time.time() - T0, 2)
with open(os.path.join(HERE, 'r3_su3_results.json'), 'w') as f:
    json.dump(OUT, f, indent=1, default=str)
log(f"\nresults -> r3_su3_results.json   ({OUT['runtime_s']}s)")
log("\nVERDICT (SU(3) side): the twelve per-term closed forms are PROVEN")
log("(exact dual tables, all residues; reciprocity input at B204's verified-exact")
log(" standard); LAW-O holds for ALL kappa; the tone conductors are the")
log(" det(pm w)*det(B) identity — B587's menu is a theorem.")
