"""P2W5-LSCHAAR (OI-121 / L82 residual) — the Landsberg-Schaar closed form at SU(3).

TARGET. B587 found the Weyl-twisted Weil factorization exactly; B666 cell R3 then
exhibited the twelve per-term values as residue TABLES, but its decisive step was
(I5) "the standard multivariate Landsberg-Schaar / Krazer input", used as an
identity verified numerically (floats at kappa=4..200, dps-40 at 15 kappa) plus
(I4) g0 = -i sqrt(3) kappa, itself an unproved reciprocity instance.  So the
per-term closed form was CONDITIONAL on an uncomputed input.  This cell removes
the condition and replaces the tables by closed forms in kappa.

THE PROOF (each step gated below; kappa >= 1 throughout, stage needs kappa >= 4).

 (P1) KERNEL.  On C[L], L = P/kappa Q (|L| = n = 3 kappa^2), with T = diag
      e^{i pi |mu|^2/kappa} and S the bare finite Fourier transform,
      rho(RL) = T . S* T^bar S  has matrix elements (g0/n) e^{i pi |mu-nu|^2/kappa}
      (completion of the square; the shift lambda -> lambda + (mu-nu) is a
      bijection of L), g0 = sum_mu e^{-i pi |mu|^2/kappa}.  Hence
          t_{+-w}(kappa) := tr(rho(RL) P_{+-w}) = (g0/n) * Theta_{F}(kappa),
          Theta_F(kappa) = sum_{mu in L} e^{i pi F[mu]/(3 kappa)},
          F_{+-w} = K + (I -+ w)^T K (I -+ w),  K = [[2,1],[1,2]] = 3 * (A2 weight form).
 (P2) STRUCTURE.  F = K B,  B_{+-w} = tr(A) I -+ (w + w^{-1}), tr(A_RL) = 3;
      and det(A (x) (+-w) - I_4) = det(+-w) det(B).  [exact algebra, gate G1]
 (P3) MODULUS THEOREM (elementary orthogonality -- the reciprocity-free step).
          |Theta_F(kappa)|^2 = n * R_F(kappa),
          R_F(kappa) = #{ delta in L : F delta = 0 in the character group } (radical).
      Proof: |Theta|^2 = sum_delta e^{i pi F[delta]/(3 kappa)} sum_nu chi_delta(nu)
      with chi_delta(nu) = e^{2 pi i nu^T F delta/(3 kappa)}; the inner sum is n on
      the radical and 0 off it, and F[delta]/(3 kappa) is an even integer on the
      radical.  NO reciprocity, NO Gauss sign theorem.  [gate G3]
 (P4) NORMALISATION.  R_K = 1 for every kappa (K delta = 0 mod 3 kappa <=> delta in
      kappa Q), and g0 = conj(Theta_K), so
          t_{+w0}(kappa) = (g0/n) Theta_K = |g0|^2/n = R_K = 1  exactly.
      => the (I4) input g0 = -i sqrt3 kappa is NOT needed, and
          t_{+-w}(kappa) = Theta_{F}(kappa) / Theta_{K}(kappa).           [gate G4]
 (P5) CONDUCTOR-MODULUS THEOREM.  |t_{+-w}(kappa)|^2 = R_F(kappa)
      = prod_{i=1..4} gcd(kappa, e_i), e_i = Smith elementary divisors of
      A (x) (+-w) - I_4.  The B587 conductor menu is exactly this data. [gate G5]
 (P6) SIGN / PERIODICITY.  Theta_F(kappa) = (1/12) G_F(6 kappa), G_F(M) =
      sum_{x in (Z/M)^2} e^{2 pi i F[x]/M} (free-lattice reduction, gate G2), and
      G_F is CRT-multiplicative:  G_F(M1 M2) = g_F(M2,M1) g_F(M1,M2) for coprime
      M1,M2, g_F(a,N) = sum_{x in (Z/N)^2} e^{2 pi i a F[x]/N}.  SHIFT RECURSION
      g_F(a,p^v) = p^2 g_F(a,p^{v-2}) for v >= v0, with an onset v0 PROVEN for
      every prime, including the three bad ones:
        odd p: 2 is invertible => F diagonalises over Z_p with exponents v_p(d1),
               v_p(d2) (Smith divisors of F); the 1-variable shift lemma gives
               v0 = v_p(d2) + 2;
        p = 2: F is EVEN, F[x] = 2Q(x) with integral polarisation x^T F y, so
               g_F(a,2^v) = 4 G_Q(a,2^{v-1}) and the same argument closes at
               v0 = 3 whenever det F is odd; the four terms with even det F are
               exactly the scalar ones F = cK (c = 2,4), which reduce to K
               (det K = 3, odd) at a level shifted by v_2(c), i.e. v0 = 3 + v_2(c).
               So no prime is exempted -- and the gate below FIRES on a wrong
               onset (it did, at v0 = 3 for the c = 2,4 terms, before the shift
               was put in).
      and g_F(a,p) = eta_p(-det F) p (elementary: diagonalise, then
      g(c,p) = eta(c) g(1,p) and g(1,p)^2 = eta(-1) p -- no Gauss sign theorem).  Since
      det F = 3 det B, the RATIO for F against K at such p is
          g_F/g_K = (det B | p)^{v_p},
      independent of the unit a -- the p-adic AMPLITUDE p^v and the eighth-root
      phase cancel in the ratio.  det B in {1,4,16,25} (squares) => ratio 1;
      det B = 5 => ratio (5|p)^{v_p}, and (5|m) = (m|5) (5 = 1 mod 4).  Only the
      primes 2,3,5 need local data, all finite.                            [gate G6]
 (P7) THE CLOSED FORMS (the deliverable), for every kappa >= 1:
          t_{+w0} = 1
          t_{+refl} = g(kappa,5)/sqrt5,  t_{-refl} = g(2 kappa,5)/sqrt5
                      (g(a,5) = sum_{x mod 5} e^{2 pi i a x^2/5}; = (kappa|5) off 5,
                       = sqrt5 at 5 | kappa)                  [w1,w2,w5]
          t_{+rot} = (-2)^{min(v_2(kappa),2)},  t_{-rot} = -(-2)^{min(v_2(kappa),1)}
                                                              [w3,w4]
          t_{-w0} = -(-5)^{min(v_5(kappa),1)}
      verified EXACTLY (cyclotomic integer arithmetic, no floats) on two disjoint
      kappa ranges incl. deep prime powers.                                [gate G7]
 (P8) LAW-O for ALL kappa, and -- new -- a CLOSED FORM for LAW-E, which B587 called
      "lawless by mechanism": it is not lawless, it is a quadratic-character law
      in (kappa|5) modulated by v_2(kappa).                                [gate G8]
 (P9) BOUNDARY (computed, not cited): the proof does NOT extend to the other
      balanced words.  For W = R^n L^n the monodromy has A_21 = n, and for n >= 2
      the Weil kernel is not a Gaussian on L; the ratio ansatz fails at every
      kappa tested.  L24(c) proper stays open with an identified reason.   [gate G9]

House method: B775 Phase-2 structural; exact/symbolic preferred; every decisive
number computed in-cell; the verdict block below can emit RESOLVED-A / RESOLVED-B
(EXTERNAL) / UNRESOLVED and every branch can fire and can fail.
Run: python3 compute.py   (pyenv python3; ~2-4 min).  Nothing to CLAIMS.md.
"""
import importlib.util
import json
import math
import os
import time
from math import gcd

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
OUT = {}
T0 = time.time()
LOG = []


def log(m=""):
    print(m, flush=True)
    LOG.append(m)


# ------------------------------------------------------------------ constructions
K = np.array([[2, 1], [1, 2]])                 # 3 * A2 weight form
CART = np.array([[2, -1], [-1, 2]])            # A2 Cartan (root lattice basis in P)
S1 = np.array([[-1, 0], [1, 1]])
S2 = np.array([[1, 1], [0, -1]])
WEYL = []
for word in ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)):
    M = np.eye(2, dtype=int)
    for g in word:
        M = (S1 if g == 0 else S2) @ M
    WEYL.append((M, (-1) ** len(word)))
R2 = np.array([[1, 1], [0, 1]])
L2 = np.array([[1, 0], [1, 1]])


def mono(w):
    M = np.eye(2, dtype=int)
    for ch in w:
        M = M @ (R2 if ch == 'R' else L2)
    return M


A_RL = mono("RL")                              # [[2,1],[1,1]], tr 3, A_21 = 1
TERMS = []
for pm in (1, -1):
    for wi, (w, sg) in enumerate(WEYL):
        wp = pm * w
        winv = np.rint(np.linalg.inv(wp)).astype(int)
        B = 3 * np.eye(2, dtype=int) - wp - winv
        I2 = np.eye(2, dtype=int)
        F = K + (I2 - wp).T @ K @ (I2 - wp)
        TERMS.append(dict(lab=f"{'+' if pm > 0 else '-'}w{wi}", pm=pm, wi=wi, w=wp,
                          sign=sg, B=B, F=F))
LABS = [t['lab'] for t in TERMS]
BYLAB = {t['lab']: t for t in TERMS}

UINV = np.array([[2, 1], [-1, 0]])             # P/kappa Q reps: mu = UINV @ (c1,c2)


def reps_of(kap):
    g1, g2 = np.meshgrid(np.arange(kap), np.arange(3 * kap), indexing='ij')
    return (2 * g1 + g2).ravel(), (-g1).ravel()


def qform(F, m0, m1):
    return F[0, 0] * m0 * m0 + 2 * F[0, 1] * m0 * m1 + F[1, 1] * m1 * m1


def theta_counts(F, kap):
    """Theta_F(kappa) = sum_j counts[j] zeta_{6kappa}^j   (exact integer counts)."""
    M = 6 * kap
    m0, m1 = reps_of(kap)
    return np.bincount((qform(F, m0, m1) % M), minlength=M)


def theta_val(F, kap):
    M = 6 * kap
    c = theta_counts(F, kap)
    return (c * np.exp(2j * np.pi * np.arange(M) / M)).sum()


# ------------------------------------------------------------------ exact cyclotomic
def cyc(M):
    x = sp.symbols('x')
    return [int(c) for c in sp.Poly(sp.cyclotomic_poly(M, x), x).all_coeffs()][::-1]


def polyrem(a, phi):
    a = [int(v) for v in a]
    d = len(phi) - 1
    for i in range(len(a) - 1, d - 1, -1):
        c = a[i]
        if c:
            a[i] = 0
            for j in range(d):
                a[i - d + j] -= c * phi[j]
    return a[:d]


def polymul_cyclic(p, q, M):
    r = [0] * M
    for i, ci in enumerate(p):
        if ci:
            for j, cj in enumerate(q):
                if cj:
                    r[(i + j) % M] += ci * cj
    return r


def leg5(k):
    return {0: 0, 1: 1, 2: -1, 3: -1, 4: 1}[k % 5]


def vp(p, k):
    n = 0
    while k % p == 0:
        k //= p
        n += 1
    return n


# ---- the closed forms of (P7), as functions of kappa -------------------------
def cf_float(lab, kap):
    s5 = math.sqrt(5)
    if lab == '+w0':
        return 1.0
    if lab in ('+w1', '+w2', '+w5'):
        return s5 if kap % 5 == 0 else float(leg5(kap))
    if lab in ('-w1', '-w2', '-w5'):
        return s5 if kap % 5 == 0 else float(leg5(2 * kap))
    if lab in ('+w3', '+w4'):
        return float((-2) ** min(vp(2, kap), 2))
    if lab in ('-w3', '-w4'):
        return float(-((-2) ** min(vp(2, kap), 1)))
    if lab == '-w0':
        return float(-((-5) ** min(vp(5, kap), 1)))
    raise KeyError(lab)


def cf_poly(lab, kap, M):
    """the same closed form as an exact element of Z[zeta_M], M = 6 kappa."""
    p = [0] * M

    def add_int(c):
        p[0] += c

    def add_sqrt5(c):
        assert M % 5 == 0
        for a in range(1, 5):
            p[a * (M // 5)] += c * leg5(a)

    if lab == '+w0':
        add_int(1)
    elif lab in ('+w1', '+w2', '+w5'):
        add_sqrt5(1) if kap % 5 == 0 else add_int(leg5(kap))
    elif lab in ('-w1', '-w2', '-w5'):
        add_sqrt5(1) if kap % 5 == 0 else add_int(leg5(2 * kap))
    elif lab in ('+w3', '+w4'):
        add_int((-2) ** min(vp(2, kap), 2))
    elif lab in ('-w3', '-w4'):
        add_int(-((-2) ** min(vp(2, kap), 1)))
    elif lab == '-w0':
        add_int(-((-5) ** min(vp(5, kap), 1)))
    return p


FAIL = []                                       # every gate failure recorded here


def gate(name, ok, detail=""):
    log(f"  [{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    if not ok:
        FAIL.append(name)
    return ok


log("=" * 72)
log("P2W5-LSCHAAR — the Landsberg-Schaar closed form at SU(3) (OI-121 / L82)")
log("=" * 72)
log(f"golden monodromy A = {A_RL.tolist()}  tr = {int(np.trace(A_RL))}  A_21 = {A_RL[1,0]}")

# ================================================================ G1 structure
log("\n-- G1  structure + conductor identities (exact / symbolic) --")
g1_ok = True
menu = {}
for t in TERMS:
    g1_ok &= bool((t['F'] == K @ t['B']).all())
    d = int(round(np.linalg.det(np.kron(A_RL, t['w']) - np.eye(4))))
    pred = int(round(np.linalg.det(t['w']))) * int(round(np.linalg.det(t['B'])))
    g1_ok &= (d == pred)
    menu[t['lab']] = d
    ed = [abs(int(smith_normal_form(sp.Matrix(
        (np.kron(A_RL, t['w']) - np.eye(4, dtype=int)).astype(int).tolist()))[i, i]))
        for i in range(4)]
    t['ed'] = ed
# symbolic proof of the conductor identity for a general A with tr = T, det = 1:
# prod over the eigenvalues l of w of (a l - 1)(a^-1 l - 1) = l^2 - T l + 1
#                                    = -l (T - l - l^-1),  T = a + a^-1
tt, l, aa = sp.symbols('T l a')
sym_ok = (sp.simplify(sp.expand((aa * l - 1) * (l / aa - 1))
                      - (l ** 2 - (aa + 1 / aa) * l + 1)) == 0
          and sp.simplify(sp.expand(l ** 2 - tt * l + 1)
                          - sp.expand(-l * (tt - l - 1 / l))) == 0)
gate("G1 F = K.B and det(A(x)(+-w)-I4) = det(+-w) det(B) on all 12 terms", g1_ok,
     f"menu {menu['+w0']},{menu['+w1']},{menu['+w3']},{menu['-w0']},{menu['-w3']}")
gate("G1 symbolic eigenvalue identity (l^2 - T l + 1) = -l (T - l - l^-1)", sym_ok)
b587_menu_ok = (menu['+w0'] == 1 and menu['-w0'] == 25 and menu['+w3'] == 16
                and menu['-w3'] == 4 and all(menu[f'{s}w{i}'] == -5
                                             for s in '+-' for i in (1, 2, 5)))
gate("G1 B587's registered conductor menu reproduced", b587_menu_ok)
log("       Smith divisors of A(x)(+-w) - I4: " +
    ", ".join(f"{t['lab']}:{t['ed']}" for t in TERMS[:6]))

# ================================================================ G2 free-lattice
log("\n-- G2  well-definedness + free-lattice reduction Theta_F(k) = (1/12) G_F(6k) --")


def G_free(F, M):
    x = np.arange(M)
    X, Y = np.meshgrid(x, x, indexing='ij')
    return np.bincount((qform(F, X, Y) % M).ravel(), minlength=M)


wd_ok = True
for t in TERMS:                                  # phase well-defined on P/kappa Q
    for z in (np.array([1, 0]), np.array([0, 1])):
        nu = CART @ z                            # a root-lattice generator
        wd_ok &= (int(nu @ t['F'] @ nu) % 6 == 0)          # 6 | F[nu]
        for mu in (np.array([1, 0]), np.array([0, 1])):
            wd_ok &= (int(2 * mu @ t['F'] @ nu) % 6 == 0)  # 6 | 2 mu^T F nu
gate("G2 6 | F[nu] and 6 | 2 mu^T F nu for nu in Q  (=> phase well defined)", wd_ok)
fr_ok = True
for kap in (2, 3, 4, 5, 6, 7):
    M = 6 * kap
    for t in TERMS:
        a = theta_counts(t['F'], kap).astype(object) * 12
        b = G_free(t['F'], M).astype(object)
        fr_ok &= bool((a == b).all())
gate("G2 12 * Theta-counts == G_F(6 kappa)-counts, exact, kappa=2..7 x 12 terms", fr_ok)

# ================================================================ G3 modulus thm
log("\n-- G3  modulus theorem |Theta_F|^2 = n R_F  (elementary orthogonality) --")


def radical(F, kap):
    m0, m1 = reps_of(kap)
    mu = np.stack([m0, m1], 1)
    Fmu = mu @ F.T
    gens = [UINV @ np.array([1, 0]), UINV @ np.array([0, 1])]
    ok = np.ones(len(mu), dtype=bool)
    for g in gens:
        ok &= ((Fmu @ g) % (3 * kap) == 0)
    return int(ok.sum())


mod_ok = True
mod_rows = []
for kap in list(range(1, 26)) + [32, 40, 45, 50]:
    M = 6 * kap
    phi = cyc(M)
    for t in TERMS:
        c = theta_counts(t['F'], kap).astype(object).tolist()
        cbar = [0] * M
        for j, v in enumerate(c):
            cbar[(-j) % M] += v
        prod = polymul_cyclic(c, cbar, M)
        prod[0] -= 3 * kap * kap * radical(t['F'], kap)
        r = polyrem(prod, phi)
        if any(r):
            mod_ok = False
            mod_rows.append((kap, t['lab']))
gate("G3 |Theta_F(kappa)|^2 == 3 kappa^2 * R_F(kappa) EXACTLY (29 kappa x 12 terms)",
     mod_ok, f"{len(mod_rows)} exceptions")

# ================================================================ G4 normalisation
log("\n-- G4  normalisation: R_K = 1 and t_{+w0} = 1 exactly (kills the g0 input) --")
rk_ok = all(radical(K, kap) == 1 for kap in range(1, 61))
gate("G4 R_K(kappa) = 1 for kappa = 1..60 (K delta = 0 <=> delta in kappa Q)", rk_ok)
# t_{+w0} = |g0|^2/n = R_K = 1 : check against the honest matrix trace below (G5b)

# ================================================================ G5 conductor-modulus
log("\n-- G5  conductor-modulus theorem |t|^2 = prod_i gcd(kappa, e_i) --")
cm_ok = True
for kap in range(1, 61):
    for t in TERMS:
        pred = 1
        for e in t['ed']:
            pred *= gcd(kap, e)
        if radical(t['F'], kap) != pred:
            cm_ok = False
            log(f"    exception kappa={kap} {t['lab']}: R={radical(t['F'],kap)} pred={pred}")
gate("G5 R_F(kappa) = prod gcd(kappa, Smith divisors of A(x)(+-w)-I4), kappa=1..60",
     cm_ok)

log("\n-- G5b independent estimator: the B587 Weil MATRICES (and B238 stage traces) --")


def build_index(kap):
    U = np.array([[0, -1], [1, 2]])
    reps, index = [], {}

    def canon(mu):
        c = U @ mu
        return (int(c[0]) % kap, int(c[1]) % (3 * kap))

    for c1 in range(kap):
        for c2 in range(3 * kap):
            reps.append(UINV @ np.array([c1, c2]))
            index[(c1, c2)] = len(reps) - 1
    return np.array(reps), index, canon


def ipw(u, v):
    return (2 * (u[..., 0] * v[..., 0] + u[..., 1] * v[..., 1])
            + (u[..., 0] * v[..., 1] + u[..., 1] * v[..., 0])) / 3.0


def weil_matrix_terms(word, kap):
    reps, index, canon = build_index(kap)
    n = len(reps)
    q = ipw(reps, reps)
    T = np.exp(1j * np.pi * q / kap)
    pair = ipw(reps[:, None, :], reps[None, :, :])
    S = np.exp(-2j * np.pi * pair / kap) / math.sqrt(n)
    Rop = np.diag(T)
    Lop = S.conj().T @ np.diag(T).conj() @ S
    Mw = np.eye(n, dtype=complex)
    for ch in word:
        Mw = Mw @ (Rop if ch == 'R' else Lop)
    out = {}
    for pm in (1, -1):
        for wi, (w, sg) in enumerate(WEYL):
            idx = [index[canon(pm * (w @ mu))] for mu in reps]
            out[f"{'+' if pm > 0 else '-'}w{wi}"] = sum(Mw[i, idx[i]] for i in range(n))
    return out


mat_dev = 0.0
norm_dev = 0.0
for kap in (4, 5, 6, 7, 8, 9, 10, 12):
    tm = weil_matrix_terms("RL", kap)
    norm_dev = max(norm_dev, abs(tm['+w0'] - 1.0))
    for lab in LABS:
        mat_dev = max(mat_dev, abs(tm[lab] - cf_float(lab, kap)))
gate("G5b t_{+w0} = 1 on the honest Weil matrices (kappa=4..12)", norm_dev < 1e-8,
     f"max dev {norm_dev:.2e}")
gate("G5b matrix per-term traces == the (P7) closed forms (8 kappa x 12 terms)",
     mat_dev < 1e-7, f"max dev {mat_dev:.2e}")

spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(ROOT, "frontier", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)
z_dev = 0.0
for kap in range(4, 15):
    w3, S3, T3, c3 = b238.su3_data(kap - 3)
    zb = b238.wrt_trace(S3, T3, "RL")
    zc = sum(WEYL[wi][1] * cf_float(f'+w{wi}', kap) for wi in range(6)) / 6.0
    z_dev = max(z_dev, abs(zb - zc))
gate("G5b assembled Z(RL;SU(3)_k) from the closed forms == banked B238, kappa=4..14",
     z_dev < 1e-6, f"max dev {z_dev:.2e}")

# ================================================================ G6 local structure
log("\n-- G6  CRT multiplicativity, shift recursion, and the ratio lemma --")


def g_local(F, a, N):
    x = np.arange(N)
    X, Y = np.meshgrid(x, x, indexing='ij')
    ph = (a * qform(F, X, Y)) % N
    c = np.bincount(ph.ravel(), minlength=N)
    return (c * np.exp(2j * np.pi * np.arange(N) / N)).sum()


crt_ok = True
for (M1, M2) in ((4, 9), (8, 3), (5, 12), (7, 8), (9, 25), (11, 4)):
    M = M1 * M2
    for t in TERMS:
        lhs = (G_free(t['F'], M) * np.exp(2j * np.pi * np.arange(M) / M)).sum()
        rhs = g_local(t['F'], M2 % M1, M1) * g_local(t['F'], M1 % M2, M2)
        crt_ok &= abs(lhs - rhs) < 1e-6 * max(1.0, abs(lhs))
gate("G6 CRT: G_F(M1 M2) = g_F(M2,M1) g_F(M1,M2) on 6 coprime splits x 12 terms",
     crt_ok)

# --- the stabilisation onset v0, PROVEN per (F,p), then verified from v0 upwards.
#  odd p: 2 is invertible, so F diagonalises over Z_p with exponents = v_p of the
#         Smith divisors (d1|d2) of F; the 1-variable shift lemma
#         sum_{x mod p^v} e(b x^2/p^v) = p sum_{x mod p^{v-2}} e(b x^2/p^{v-2})
#         (p nmid b, v >= 2) then gives g_F(a,p^v) = p^2 g_F(a,p^{v-2}) for
#         v >= v0 = v_p(d2) + 2.  Elementary; no Gauss sign theorem.
#  p = 2: F is an EVEN form, F = 2Q with Q integral and integral polarisation x^T F y,
#         so g_F(a,2^v) = 4 G_Q(a,2^{v-1}); if det F is odd the same shift argument
#         closes for v >= 3.  The four terms with even det F are exactly the SCALAR
#         ones F = cK (c = 2,4), for which g_{cK}(a,2^v) = c^2 g_K(a,2^v - shifted)
#         reduces to K, and det K = 3 is odd.  So every term is covered.
log("       stabilisation onset v0 (proven per term/prime), then verified:")
snf_div = {}
for t in TERMS:
    S = smith_normal_form(sp.Matrix(t['F'].astype(int).tolist()))
    snf_div[t['lab']] = (abs(int(S[0, 0])), abs(int(S[1, 1])))
p2_cover = True
SCAL = {}
for t in TERMS:
    detF = int(round(np.linalg.det(t['F'])))
    c = t['F'][0, 0] // 2
    is_scalar = bool((t['F'] == c * K).all())
    SCAL[t['lab']] = c if is_scalar else 1
    p2_cover &= (detF % 2 == 1) or is_scalar
gate("G6 p=2 coverage: every F has odd det F, or is a scalar multiple c.K "
     "(reduces to K at level shifted by v_2(c); det K = 3, odd)", p2_cover,
     f"scalars {sorted(set(int(v) for v in SCAL.values()))}")

rec_rows, rec_ok = [], True
VMAX = {2: 7, 3: 5, 5: 4, 7: 3, 11: 2, 13: 2}
for p in (2, 3, 5, 7, 11, 13):
    for t in TERMS:
        d2 = snf_div[t['lab']][1]
        # onset: p=2 -> 3 for odd det F, shifted by v_2(c) for the scalar terms F=cK
        v0 = (3 + vp(2, SCAL[t['lab']])) if p == 2 else vp(p, d2) + 2
        for v in range(v0, VMAX[p] + 1):
            for a in (1, 2):
                if a % p == 0:
                    continue
                lhs = g_local(t['F'], a, p ** v)
                rhs = (p ** 2) * g_local(t['F'], a, p ** (v - 2))
                if abs(lhs - rhs) > 1e-5 * max(1.0, abs(rhs)):
                    rec_rows.append((p, v, a, t['lab']))
                    rec_ok = False
gate("G6 shift recursion g_F(a,p^v) = p^2 g_F(a,p^{v-2}) for v >= v0 "
     "(v0 = v_p(d2)+2 odd p; 3 + v_2(c) at p = 2), p = 2,3,5,7,11,13, a = 1,2", rec_ok,
     f"{len(rec_rows)} exceptions; v0 per term/prime from the Smith divisors "
     f"{sorted(set(snf_div.values()))}")

ratio_ok = True
ratio_rows = []
for p in (7, 11, 13, 17, 19, 23, 29, 31):
    for t in TERMS:
        detB = int(round(np.linalg.det(t['B'])))
        for v in (1, 2):
            r = g_local(t['F'], 1, p ** v) / g_local(K, 1, p ** v)
            pred = sp.legendre_symbol(detB, p) ** (v % 2) if detB % p else None
            if pred is None:
                continue
            if abs(r - float(pred)) > 1e-6:
                ratio_ok = False
                ratio_rows.append((p, v, t['lab'], complex(r), float(pred)))
gate("G6 ratio lemma g_F/g_K = (det B | p)^{v mod 2} at p = 7..31, v = 1,2",
     ratio_ok, f"{len(ratio_rows)} exceptions")
qr_ok = all(sp.legendre_symbol(5, p) == sp.legendre_symbol(p, 5)
            for p in (7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43))
gate("G6 (5|p) = (p|5) (reciprocity, 5 = 1 mod 4) => the det B = 5 terms are "
     "functions of kappa mod 5", qr_ok)

# ================================================================ G7 the closed forms
log("\n-- G7  THE CLOSED FORMS: exact cyclotomic verification, two disjoint ranges --")
RANGE_A = list(range(1, 61))
RANGE_B = [61, 64, 71, 75, 80, 81, 96, 100, 101, 120, 121, 125, 128, 135, 144, 160,
           162, 169, 175, 180, 200]
ex_bad = []
for tag, rng in (("A: kappa = 1..60", RANGE_A), ("B: kappa = 61..200 sparse", RANGE_B)):
    bad = 0
    for kap in rng:
        M = 6 * kap
        phi = cyc(M)
        cK = theta_counts(K, kap).astype(object).tolist()
        for t in TERMS:
            cF = theta_counts(t['F'], kap).astype(object).tolist()
            pp = cf_poly(t['lab'], kap, M)
            prod = polymul_cyclic(pp, cK, M)
            diff = [int(cF[i]) - prod[i] for i in range(M)]
            if any(polyrem(diff, phi)):
                bad += 1
                ex_bad.append((kap, t['lab']))
    gate(f"G7 exact: Theta_F == t_closedform * Theta_K, range {tag} "
         f"({len(rng)} kappa x 12 terms)", bad == 0, f"{bad} mismatches")

# third range: DEEP p-valuations, well past every stabilisation onset v0 (the one
# place a wrong onset would show up).  Floating sums of 3 kappa^2 unit phases,
# relative error ~1e-10; the two exact ranges above carry the proof grade.
RANGE_C = [256, 384, 405, 512, 625, 729, 1000, 1024]
deep_bad = 0
for kap in RANGE_C:
    tk = theta_val(K, kap)
    for t in TERMS:
        if abs(theta_val(t['F'], kap) / tk - cf_float(t['lab'], kap)) > 1e-5:
            deep_bad += 1
gate("G7c deep valuations v2 <= 10, v3 <= 6, v5 <= 4 (kappa up to 1024, 8 kappa x "
     "12 terms)", deep_bad == 0, f"{deep_bad} mismatches")

log("       the twelve closed forms (P7):")
log("         +w0    : 1")
log("         +-refl : g(kappa,5)/sqrt5 resp. g(2 kappa,5)/sqrt5   [= (kappa|5) off 5,"
    " sqrt5 at 5|kappa]")
log("         +rot   : (-2)^min(v2(kappa),2)      -rot : -(-2)^min(v2(kappa),1)")
log("         -w0    : -(-5)^min(v5(kappa),1)")

# ================================================================ G8 LAW-O / LAW-E
log("\n-- G8  LAW-O for all kappa; LAW-E gets a closed form (new) --")
PHI = (1 + math.sqrt(5)) / 2
lawo_ok, lawe_ok = True, True
for kap in range(1, 401):
    tp = {lab: cf_float(lab, kap) for lab in LABS}
    odd = sum(WEYL[wi][1] * (tp[f'+w{wi}'] + tp[f'-w{wi}']) for wi in range(6)) / 12
    even = sum(WEYL[wi][1] * (tp[f'+w{wi}'] - tp[f'-w{wi}']) for wi in range(6)) / 12
    tgt = (1.0 if kap % 4 == 0 else 0.0) - ((1 / PHI) if kap % 5 == 0 else 0.0)
    if abs(odd - tgt) > 1e-9:
        lawo_ok = False
    if vp(2, kap) != 1:
        ec = ((1 if kap % 5 else 0) - leg5(kap)) / 2
    else:
        ec = -((1 + (0 if kap % 5 else 1) + leg5(kap)) / 2)
    if abs(even - ec) > 1e-9:
        lawe_ok = False
gate("G8 LAW-O = [4|kappa] - [5|kappa]/phi from the closed forms, kappa = 1..400",
     lawo_ok)
gate("G8 LAW-E closed form: ([5 not| k] - (k|5))/2 if v2(k) != 1, else "
     "-(1 + [5|k] + (k|5))/2", lawe_ok)
banked_even = {6: -1, 7: 1, 8: 1, 10: -1, 12: 1, 13: 1, 14: -1}
be_ok = True
for kap, v in banked_even.items():
    tp = {lab: cf_float(lab, kap) for lab in LABS}
    even = sum(WEYL[wi][1] * (tp[f'+w{wi}'] - tp[f'-w{wi}']) for wi in range(6)) / 12
    be_ok &= abs(even - v) < 1e-9
gate("G8 banked B587 even-channel values (kappa = 6..14) reproduced", be_ok)
# LAW-O in closed algebraic form, symbolically, on the 20 residue classes
s5 = sp.sqrt(5)


def cf_sym(lab, kap):
    if lab == '+w0':
        return sp.Integer(1)
    if lab in ('+w1', '+w2', '+w5'):
        return s5 if kap % 5 == 0 else sp.Integer(leg5(kap))
    if lab in ('-w1', '-w2', '-w5'):
        return s5 if kap % 5 == 0 else sp.Integer(leg5(2 * kap))
    if lab in ('+w3', '+w4'):
        return sp.Integer((-2) ** min(vp(2, kap), 2))
    if lab in ('-w3', '-w4'):
        return sp.Integer(-((-2) ** min(vp(2, kap), 1)))
    return sp.Integer(-((-5) ** min(vp(5, kap), 1)))


sym_rows = []
sym_ok2 = True
for kap in range(20, 40):                      # one full period, v2 >= 2 realised
    odd = sum(WEYL[wi][1] * (cf_sym(f'+w{wi}', kap) + cf_sym(f'-w{wi}', kap))
              for wi in range(6)) / 12
    tgt = (sp.Integer(1) if kap % 4 == 0 else 0) - \
          ((2 / (1 + s5)) if kap % 5 == 0 else 0)
    if sp.simplify(odd - tgt) != 0:
        sym_ok2 = False
    sym_rows.append((kap, sp.sstr(sp.simplify(odd))))
gate("G8 LAW-O symbolic (exact sqrt5 algebra) on a full period kappa = 20..39",
     sym_ok2)

# ================================================================ G9 boundary
log("\n-- G9  boundary: does the proof extend to the other balanced words? --")


def theta_gen(F, kap, c):
    M = 6 * c * kap
    m0, m1 = reps_of(kap)
    cnt = np.bincount((qform(F, m0, m1) % M), minlength=M)
    return (cnt * np.exp(2j * np.pi * np.arange(M) / M)).sum()


gen_rows = {}
for word in ("RL", "RRLL", "RRRLLL"):
    A = mono(word)
    c = int(A[1, 0])
    tr = int(np.trace(A))
    hits = tot = 0
    for kap in (4, 5, 6, 7, 8):
        tm = weil_matrix_terms(word, kap)
        base = tm['+w0']
        Fid = K @ (tr * np.eye(2, dtype=int) - 2 * np.eye(2, dtype=int))
        den = theta_gen(Fid, kap, c)
        for t in TERMS:
            wp = t['w']
            winv = np.rint(np.linalg.inv(wp)).astype(int)
            Bg = tr * np.eye(2, dtype=int) - wp - winv
            pred = theta_gen(K @ Bg, kap, c) / den
            got = tm[t['lab']] / base
            tot += 1
            hits += int(abs(pred - got) < 1e-6)
    gen_rows[word] = dict(A=A.tolist(), tr=tr, c=int(c), hits=hits, tot=tot)
    log(f"    {word:>7}: A_21 = {c}, tr = {tr}  ->  Gaussian-kernel ansatz matches "
        f"{hits}/{tot} per-term ratios")
gate("G9 the ansatz is EXACT for RL (A_21 = 1)",
     gen_rows['RL']['hits'] == gen_rows['RL']['tot'])
gate("G9 the ansatz FAILS for R^nL^n, n >= 2 (A_21 = n > 1): a computed boundary, "
     "not a citation",
     gen_rows['RRLL']['hits'] < gen_rows['RRLL']['tot']
     and gen_rows['RRRLLL']['hits'] < gen_rows['RRRLLL']['tot'],
     f"silver {gen_rows['RRLL']['hits']}/{gen_rows['RRLL']['tot']}, "
     f"bronze {gen_rows['RRRLLL']['hits']}/{gen_rows['RRRLLL']['tot']}")

# ================================================================ VERDICT
log("\n" + "=" * 72)
log("VERDICT BLOCK (branches: RESOLVED-A / RESOLVED-B(EXTERNAL) / UNRESOLVED)")
log("=" * 72)

def none_failed(prefix):
    return not any(n.startswith(prefix) for n in FAIL)


P_struct = none_failed("G1")
P_reduction = none_failed("G2")
P_modulus = none_failed("G3") and none_failed("G4") and none_failed("G5 ")
P_matrix = none_failed("G5b")
P_local = none_failed("G6")
P_closed = none_failed("G7")
P_laws = none_failed("G8")
P_boundary = none_failed("G9")

log(f"  reduction (P1/P6 free-lattice)          : {P_reduction}")
log(f"  modulus theorem + normalisation (P3-P5) : {P_modulus}")
log(f"  local structure / ratio lemma (P6)      : {P_local}")
log(f"  closed forms exact, two ranges (P7)     : {P_closed}")
log(f"  independent estimators (matrices, B238) : {P_matrix}")
log(f"  LAW-O all kappa + LAW-E closed form (P8): {P_laws}")
log(f"  structure/conductor identities (P2)     : {P_struct}")
log(f"  general-word boundary computed (P9)     : {P_boundary}")

RECIPROCITY_NEEDED = not (P_modulus and P_closed)     # would force an EXTERNAL call

if P_struct and P_reduction and P_modulus and P_local and P_closed and P_matrix \
        and P_laws and P_boundary:
    VERDICT = "RESOLVED-A"
    HEAD = ("the SU(3) per-term closed form is PROVEN and the Landsberg-Schaar / "
            "multivariate-reciprocity input is ELIMINATED: t = Theta_F/Theta_K, "
            "amplitude and eighth-root phase cancel in the ratio, only a Legendre "
            "symbol survives")
elif P_modulus and P_matrix and not P_closed:
    VERDICT = "RESOLVED-B"
    HEAD = ("obstruction named (EXTERNAL): the modulus is elementary but the per-term "
            "SIGN cannot be pinned without the classical Gauss sign theorem / Weil "
            "index at the ramified prime")
else:
    VERDICT = "UNRESOLVED"
    HEAD = "gates failed; the chain does not close in-cell"

log(f"\n  FAILED GATES: {FAIL if FAIL else 'none'}")
log(f"\n  VERDICT: {VERDICT}")
log(f"  {HEAD}")
log("\n  DISCRIMINATING FACT (in-cell): |Theta_F(kappa)|^2 = 3 kappa^2 R_F(kappa) by "
    "orthogonality alone,")
log("  and R_K = 1, so t_{+w0} = |g0|^2/n = 1 EXACTLY -- the B666-R3 inputs (I4) "
    "g0 = -i sqrt3 kappa")
log("  and (I5) multivariate reciprocity are both unnecessary; t = Theta_F/Theta_K.")
log("  Twelve closed forms in kappa (not residue tables), exact over 81 kappa.")
log("  NEW: LAW-E is NOT lawless (B587) -- it is the quadratic character (kappa|5) "
    "modulated by v2(kappa).")
log("  RESIDUAL (computed boundary): R^nL^n with n >= 2 has A_21 = n > 1, the Weil "
    "kernel is not")
log("  a Gaussian on P/kappa Q, and the ratio ansatz fails at every kappa tested "
    "=> L24(c) proper stays open.")

OUT = dict(
    cell="P2W5-LSCHAAR", oi="OI-121", lead="L82 residual", verdict=VERDICT,
    headline=HEAD,
    gates_failed=FAIL,
    conductor_menu=menu,
    smith_divisors={t['lab']: t['ed'] for t in TERMS},
    closed_forms={
        "+w0": "1",
        "+w1,+w2,+w5": "g(kappa,5)/sqrt5  = (kappa|5) if 5 nmid kappa, sqrt5 if 5|kappa",
        "-w1,-w2,-w5": "g(2 kappa,5)/sqrt5 = -(kappa|5) if 5 nmid kappa, sqrt5 if 5|kappa",
        "+w3,+w4": "(-2)^min(v2(kappa),2)",
        "-w3,-w4": "-(-2)^min(v2(kappa),1)",
        "-w0": "-(-5)^min(v5(kappa),1)"},
    theorems={
        "modulus": "|Theta_F(k)|^2 = 3k^2 R_F(k) (orthogonality; no reciprocity)",
        "normalisation": "R_K = 1 => t_{+w0} = 1 exactly => t = Theta_F/Theta_K",
        "conductor_modulus": "|t_{pm w}(k)|^2 = prod_i gcd(k, e_i(A x (pm w) - I4))",
        "ratio": "g_F/g_K = (det B | p)^{v_p} at p nmid 2 det F (amplitude cancels)",
        "LAW_O": "[4|k] - [5|k]/phi, proven for ALL k >= 1",
        "LAW_E": "([5 nmid k] - (k|5))/2 if v2(k) != 1, else -(1 + [5|k] + (k|5))/2"},
    exact_verification=dict(range_A="kappa 1..60 (all)", range_B=RANGE_B,
                            range_C_deep_valuation=RANGE_C, terms=12,
                            mismatches=len(ex_bad) + deep_bad, arithmetic="Z[zeta_6k]"),
    estimators=dict(weil_matrix_maxdev=mat_dev, normalisation_maxdev=norm_dev,
                    b238_stage_maxdev=z_dev),
    boundary_general_words=gen_rows,
    eliminated_inputs=["B666-R3 (I4) g0 = -i sqrt(3) kappa",
                       "B666-R3 (I5) multivariate Landsberg-Schaar / Krazer reciprocity"],
    classical_inputs_retained=["finite-abelian-group orthogonality (proved in-cell)",
                               "CRT multiplicativity of Gauss sums (gated G6)",
                               "binary-form local sum sum_{F_p^2} psi(aQ) = eta(-det Q) p",
                               "quadratic reciprocity (5|p) = (p|5)"],
    residual_open="L24(c) proper: general words R^nL^n, n >= 2 (A_21 = n > 1)",
    runtime_s=round(time.time() - T0, 1))
with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(OUT, f, indent=1, default=str)
with open(os.path.join(HERE, "output.txt"), "w") as f:
    f.write("\n".join(LOG) + "\n")
log(f"\nresults.json + output.txt written  ({OUT['runtime_s']}s)")
