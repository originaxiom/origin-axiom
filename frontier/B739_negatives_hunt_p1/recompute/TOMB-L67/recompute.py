#!/usr/bin/env python3
"""
B739 Stage-B recompute — TOMB-L67 (TOMBSTONES.md:L67, Standard-theory-kills bullet 1).
Run-2 script (extends the run-1 script left by a prior agent, same conventions; deltas:
inverses are now TRUE numerical inverses, never conjugate-transposes — removing a
circularity in which building rho(L)=S T^-1 S^-1 presumed the unitarity under test;
added large-k persistence and an independent high-precision mpmath cross-check).

CLAIM KILLED (banked): "|lambda|=1 in the quantum tower is a framework-specific signal."
BANKED KILL (fact_basis=asserted, Chat-2 triage; one-hop check: FAILURE_ATLAS.md G5 cites
only "Chat-2 triage" — no in-repo computation existed):
  quantum tower |lambda|=1  =  UNITARITY of the Chern-Simons representation (true of every
  quantum theory); classical |lambda|=phi^k is the trace-map linearization being a
  SYMPLECTOMORPHISM, not unitary.  Kill form: category-error.

DISCRIMINATING FACT (the one that, if true, kills the claim):
  |lambda|=1 for the quantum tower operator is a corollary of matrix unitarity of the level-k
  mapping-class representation, and therefore holds identically for EVERY mapping-class word
  (framework or not), at EVERY level k, and in EVERY modular theory (including the non-unitary
  Yang-Lee categorification) — so the property carries ZERO framework-specific information;
  whereas the classical tower eigenvalues +/-phi^k lie OFF the unit circle because the
  classical linearization is symplectic-not-unitary, a constraint that permits any |lambda|.

E19 compute-not-cite, BOTH directions:
  - If the quantum eigenvalue moduli were word- or theory-dependent (in particular, if the
    golden/framework word RL were distinguished by its moduli), the banked fact would NOT be
    discriminating and the verdict would be REVIVED.  This script computes that test.
  - If the moduli are identically 1 across words/levels/theories while classical moduli vary
    (phi^2 for RL, (1+sqrt2)^2 for R^2L^2, ...), the kill is RECONFIRMED by computation.

DECLARED CONVENTIONS (E1) — the original arc's, re-declared where implicit:
  C1. Classical tower (B103/K001, in-repo): the linearization of the SL(n) trace map at the
      void fixed point factors through the abelianization N in GL(2,Z) of the monodromy word.
      Figure-eight (m=1) word = RL with R=[[1,1],[0,1]], L=[[1,0],[1,1]]; N = R.L = [[2,1],[1,1]],
      eigenvalues phi^{+-2}.  The tombstone's "+-phi^k" form is the GL(2,Z) golden seed
      F=[[1,1],[1,0]] (F^2=N, det F=-1, eigenvalues phi, -1/phi); tower level d contributes the
      Sym^d eigenvalues (-1)^j phi^(d-2j).  Both computed below.
  C2. Quantum tower (implicit in the Chat-2 kill; re-declared): the SU(2)_k Reshetikhin-Turaev
      (Chern-Simons level-k) representation of the torus mapping-class group SL(2,Z) on the
      (k+1)-dimensional space of conformal blocks, q = exp(2 pi i/(k+2)) (the shift the sibling
      tombstone bullet itself declares):
        S_ab = sqrt(2/(k+2)) sin(pi a b/(k+2)),  a,b = 1..k+1
        T_ab = delta_ab exp(2 pi i (a^2/(4(k+2)) - 1/8))
      (the phase a^2/(4(k+2)) - 1/8 equals h_j - c/24 exactly for a=2j+1, c=3k/(k+2); the
      representation is projective — every phase convention changes lambda only by a global
      unit-modulus scalar, so |lambda| is convention-independent; declared, immaterial).
      Generator dictionary: rho(R)=T for R=[[1,1],[0,1]]; rho(S)=S for [[0,-1],[1,0]];
      L = S T^{-1} S^{-1} in SL(2,Z) (verified exactly below), so rho(L) = S rho(T)^{-1} S^{-1}.
      All inverses are TRUE inverses (np.linalg.inv / mpmath **-1), so nothing presumes the
      unitarity that the computation is testing.
  C3. "all k (quantum side)" is recomputed as the finite sweep k=1..12, the large-k persistence
      points k=20,32,40, plus the per-level unitarity identity ||U v|| = ||v|| => |lambda|=1
      (verified numerically per eigenpair), which is level-uniform.
  C4. MTC overlay (the consulted face): three theories beyond SU(2)_k — Fibonacci (unitary,
      d_tau=+phi, theta=e^{4 pi i/5}), Yang-Lee (NON-unitary category, d_tau=-1/phi,
      theta=e^{-2 pi i/5}; the framework's native categorification per tombstone K-C), and
      Ising (theta_sigma=e^{2 pi i/16}, theta_psi=-1).  Global e^{-2 pi i c/24} phases omitted
      (projective; immaterial to |lambda| — declared).
  Deterministic: no wall-clock, no randomness, no network.  Gate 5: no SM quantities.
"""

import numpy as np
import sympy as sp
import mpmath as mp

np.set_printoptions(precision=6, suppress=True)
TOL = 1e-10


def out(s=""):
    print(s)


# ----------------------------------------------------------------------------------
out("=" * 88)
out("SECTION 0 — SL(2,Z) generator dictionary check (exact integer arithmetic)")
out("=" * 88)
R2 = sp.Matrix([[1, 1], [0, 1]])
L2 = sp.Matrix([[1, 0], [1, 1]])
S2 = sp.Matrix([[0, -1], [1, 0]])
lhs = S2 * R2**-1 * S2**-1          # S T^{-1} S^{-1}  with T = R
out(f"S T^-1 S^-1 = {lhs.tolist()}  ; equals L: {lhs == L2}")
assert lhs == L2

# ----------------------------------------------------------------------------------
out()
out("=" * 88)
out("SECTION 1 — CLASSICAL side (exact, sympy): tower eigenvalues +-phi^k, symplectic not unitary")
out("=" * 88)
phi = (1 + sp.sqrt(5)) / 2
N = R2 * L2                          # abelianization of the figure-eight word RL (B103 convention)
out(f"N = R.L = {N.tolist()}   det N = {N.det()}   tr N = {N.trace()}")
evN = list(N.eigenvals().keys())
evN_simpl = [sp.radsimp(sp.simplify(e)) for e in evN]
out(f"eigenvalues of N: {evN_simpl}")
chk2 = sorted([sp.simplify(e - phi**2) for e in evN], key=lambda x: abs(float(x)))
out(f"eigenvalue - phi^2 (one of them must vanish): {[sp.simplify(c) for c in chk2]}")
assert any(sp.simplify(e - phi**2) == 0 for e in evN)
assert any(sp.simplify(e - phi**-2) == 0 for e in evN)
out(f"=> eigenvalues are exactly phi^2 = {float(phi**2):.12f} and phi^-2 = {float(phi**-2):.12f}")

F = sp.Matrix([[1, 1], [1, 0]])      # the GL(2,Z) golden seed, F^2 = N, det = -1
out(f"F = {F.tolist()}, F^2 == N: {sp.simplify(F**2 - N) == sp.zeros(2)}   det F = {F.det()}")
evF = list(F.eigenvals().keys())
out(f"eigenvalues of F: {[sp.radsimp(sp.simplify(e)) for e in evF]}  (= phi and -1/phi: "
    f"{any(sp.simplify(e - phi) == 0 for e in evF) and any(sp.simplify(e + phi**-1) == 0 for e in evF)})")

out()
out("Sym^d tower eigenvalues of the seed F (level d): lambda = (-1)^j phi^(d-2j), j=0..d")
for d in range(1, 5):
    evs = [sp.simplify((phi) ** (d - j) * (-phi ** -1) ** j) for j in range(d + 1)]
    expo = [(d - 2 * j) for j in range(d + 1)]
    signs = ["+" if j % 2 == 0 else "-" for j in range(d + 1)]
    out(f"  d={d}: {{ {', '.join(s + 'phi^' + str(e) for s, e in zip(signs, expo))} }}  "
        f"moduli = {[f'{abs(float(v)):.6f}' for v in evs]}")
out("=> every classical tower eigenvalue is +-phi^k, |lambda| = phi^k != 1 except k=0.")

out()
J = sp.Matrix([[0, 1], [-1, 0]])
out(f"symplectic check:  N^T J N - J = {(N.T * J * N - J).tolist()}   (zero => symplectomorphism)")
assert N.T * J * N - J == sp.zeros(2)
NNt = N * N.T
out(f"unitarity check:   N N^T = {NNt.tolist()}  != I  (N is NOT unitary/orthogonal)")
assert NNt != sp.eye(2)
A = sp.diag(2, sp.Rational(1, 2))
out(f"category witness:  A = diag(2, 1/2): A^T J A - J = {(A.T * J * A - J).tolist()} (symplectic), "
    f"|eigenvalue| = 2")
out("=> the symplectic category permits ANY |lambda| = a > 0; |lambda|=phi^k off the unit circle")
out("   is exactly what a symplectomorphism may do and a unitary map may not.")

# ----------------------------------------------------------------------------------
out()
out("=" * 88)
out("SECTION 2 — QUANTUM side, SU(2)_k Chern-Simons rep of SL(2,Z), k = 1..12")
out("=" * 88)


def su2k_ST(k):
    n = k + 1
    a = np.arange(1, n + 1)
    Smat = np.sqrt(2.0 / (k + 2)) * np.sin(np.pi * np.outer(a, a) / (k + 2))
    Tdiag = np.exp(2j * np.pi * (a ** 2 / (4.0 * (k + 2)) - 1.0 / 8.0))
    return Smat.astype(complex), np.diag(Tdiag)


def unit_dev(U):
    return np.max(np.abs(U @ U.conj().T - np.eye(U.shape[0])))


def rho_word(Smat, Tmat, word):
    """word: list of (letter, power) with letters 'R','L','S'.
    TRUE inverses throughout — no unitarity presumed."""
    Sinv = np.linalg.inv(Smat)
    Tinv = np.linalg.inv(Tmat)
    Lq = Smat @ Tinv @ Sinv                 # rho(L) = S T^-1 S^-1
    Lqinv = Smat @ Tmat @ Sinv
    M = np.eye(Smat.shape[0], dtype=complex)
    for letter, p in word:
        if letter == "R":
            G = Tmat if p > 0 else Tinv
        elif letter == "L":
            G = Lq if p > 0 else Lqinv
        elif letter == "S":
            G = Smat if p > 0 else Sinv
        for _ in range(abs(p)):
            M = M @ G
    return M


out(f"{'k':>3} {'dim':>4} {'||SS+-I||':>11} {'||S^2-I||':>11} {'||(ST)^3~S^2||':>15} "
    f"{'||rho(RL)U-dev||':>17} {'max||lam|-1|':>13}")
overall_q_dev = 0.0
for k in range(1, 13):
    Smat, Tmat = su2k_ST(k)
    sdev = unit_dev(Smat)
    s2dev = np.max(np.abs(Smat @ Smat - np.eye(k + 1)))
    ST3 = np.linalg.matrix_power(Smat @ Tmat, 3)
    # projective relation (ST)^3 = mu * S^2 for a unit scalar mu
    mu = ST3[0, 0] / (Smat @ Smat)[0, 0]
    reldev = np.max(np.abs(ST3 - mu * (Smat @ Smat)))
    U = rho_word(Smat, Tmat, [("R", 1), ("L", 1)])       # the quantum tower operator rho(RL)
    udev = unit_dev(U)
    lam, vec = np.linalg.eig(U)
    mdev = np.max(np.abs(np.abs(lam) - 1.0))
    # the unitarity => |lambda|=1 identity, per eigenpair: ||U v|| / ||v|| = 1
    norm_dev = max(abs(np.linalg.norm(U @ vec[:, j]) / np.linalg.norm(vec[:, j]) - 1.0)
                   for j in range(len(lam)))
    overall_q_dev = max(overall_q_dev, mdev)
    out(f"{k:>3} {k+1:>4} {sdev:>11.2e} {s2dev:>11.2e} {reldev:>15.2e} {udev:>17.2e} {mdev:>13.2e}"
        f"   (||Uv||/||v||-1 max: {norm_dev:.2e}, |mu|={abs(mu):.12f})")
out(f"=> rho(RL) is UNITARY at every level; max ||lambda|-1| over k=1..12: {overall_q_dev:.3e}")
out("   The identity is level-uniform: U unitary => ||Uv||=||v|| => |lambda|=1 (verified per eigenpair).")

out()
out("SECTION 2b — the quantum TOWER powers rho(RL)^n, and large-k (semiclassical) persistence")
tower_dev = 0.0
for k in (3, 4, 8):
    Smat, Tmat = su2k_ST(k)
    U = rho_word(Smat, Tmat, [("R", 1), ("L", 1)])
    devs = []
    for n in range(1, 7):
        Un = np.linalg.matrix_power(U, n)
        devs.append(np.max(np.abs(np.abs(np.linalg.eigvals(Un)) - 1.0)))
    tower_dev = max(tower_dev, max(devs))
    out(f"  k={k}: max||lam|-1| for rho(RL)^n, n=1..6: {['%.1e' % d for d in devs]}"
        f"   (classical rungs phi^2n: {['%.3f' % float(phi**(2*n)) for n in range(1,7)]})")
large_k_dev = 0.0
for k in (20, 32, 40):
    Smat, Tmat = su2k_ST(k)
    U = rho_word(Smat, Tmat, [("R", 1), ("L", 1)])
    d = np.max(np.abs(np.abs(np.linalg.eigvals(U)) - 1.0))
    large_k_dev = max(large_k_dev, d)
    out(f"  k={k} (dim {k+1}): max||lam|-1| = {d:.2e}")
out("=> the tower stays on the unit circle at every rung; NO drift toward phi^2n at any n,")
out("   and no crossover at large k: the quantum->classical transition is invisible in the")
out("   |lambda| register (standard semiclassics lives elsewhere), as the kill states.")

# ----------------------------------------------------------------------------------
out()
out("=" * 88)
out("SECTION 3 — genericity across mapping-class WORDS (is |lambda|=1 framework-specific?)")
out("=" * 88)
WORDS = [
    ("RL      (framework, golden m=1)", [("R", 1), ("L", 1)]),
    ("R^2L^2  (metallic m=2, silver)",  [("R", 2), ("L", 2)]),
    ("R^3L^3  (metallic m=3, bronze)",  [("R", 3), ("L", 3)]),
    ("R^2L^3  (generic hyperbolic)",    [("R", 2), ("L", 3)]),
    ("R^5L    (generic hyperbolic)",    [("R", 5), ("L", 1)]),
    ("RL^-1   (elliptic, order 6)",     [("R", 1), ("L", -1)]),
    ("S       (elliptic, order 4)",     [("S", 1)]),
    ("R       (parabolic)",             [("R", 1)]),
]
R2n = np.array([[1, 1], [0, 1]]); L2n = np.array([[1, 0], [1, 1]]); S2n = np.array([[0, -1], [1, 0]])


def classical_word(word):
    M = np.eye(2, dtype=np.int64)
    for letter, p in word:
        G = {"R": R2n, "L": L2n, "S": S2n}[letter]
        G = G if p > 0 else np.round(np.linalg.inv(G)).astype(np.int64)
        for _ in range(abs(p)):
            M = M @ G
    return M


out(f"{'word':<34} {'classical |lambda|max':>21} {'q-dev k=4':>12} {'q-dev k=7':>12}")
S4, T4 = su2k_ST(4)
S7, T7 = su2k_ST(7)
word_qdevs = []
for name, w in WORDS:
    Mc = classical_word(w)
    lc = np.max(np.abs(np.linalg.eigvals(Mc.astype(float))))
    d4 = np.max(np.abs(np.abs(np.linalg.eigvals(rho_word(S4, T4, w))) - 1.0))
    d7 = np.max(np.abs(np.abs(np.linalg.eigvals(rho_word(S7, T7, w))) - 1.0))
    word_qdevs.append(max(d4, d7))
    out(f"{name:<34} {lc:>21.9f} {d4:>12.2e} {d7:>12.2e}")
out(f"phi^2 = {float(phi**2):.9f}; (1+sqrt2)^2 = {float((1+sp.sqrt(2))**2):.9f}; "
    f"phi_3^2 = {float(((3+sp.sqrt(13))/2)**2):.9f}")
out("=> classical moduli VARY with the word (phi^2, silver^2, bronze^2, ..., =1 only for")
out("   elliptic/parabolic classes); quantum moduli are IDENTICALLY 1 for every word —")
out("   the property '|lambda|=1' cannot distinguish the framework word from any other.")

# ----------------------------------------------------------------------------------
out()
out("=" * 88)
out("SECTION 4 — genericity across QUANTUM THEORIES (mtc-overlay face): Fib, Yang-Lee, Ising")
out("=" * 88)
phi_f = (1 + np.sqrt(5)) / 2
MTCS = [
    ("Fibonacci (unitary, d_tau=+phi)",
     np.array([[1, phi_f], [phi_f, -1]]) / np.sqrt(1 + phi_f ** 2),
     np.diag([1.0, np.exp(4j * np.pi / 5)])),
    ("Yang-Lee (NON-unitary cat, d=-1/phi)",
     np.array([[1, -1 / phi_f], [-1 / phi_f, -1]]) / np.sqrt(1 + phi_f ** -2),
     np.diag([1.0, np.exp(-2j * np.pi / 5)])),
    ("Ising",
     0.5 * np.array([[1, np.sqrt(2), 1], [np.sqrt(2), 0, -np.sqrt(2)], [1, -np.sqrt(2), 1]]),
     np.diag([1.0, np.exp(2j * np.pi / 16), -1.0])),
]
out(f"{'theory':<38} {'||SS+-I||':>11} {'rho(RL) U-dev':>15} {'max||lam|-1|':>13}")
mtc_devs = []
for name, Sm, Tm in MTCS:
    Sm = Sm.astype(complex)
    U = rho_word(Sm, Tm, [("R", 1), ("L", 1)])
    sdev = unit_dev(Sm)
    udev = unit_dev(U)
    mdev = np.max(np.abs(np.abs(np.linalg.eigvals(U)) - 1.0))
    mtc_devs.append(mdev)
    out(f"{name:<38} {sdev:>11.2e} {udev:>15.2e} {mdev:>13.2e}")
out("=> |lambda|=1 holds in every theory tested, INCLUDING the non-unitary Yang-Lee")
out("   categorification (tombstone K-C: the framework's native one): the modular matrices")
out("   S,T are unitary AS MATRICES even when the category is non-unitary. 'True of every")
out("   quantum theory' is upheld at the level this kill uses it.")

# ----------------------------------------------------------------------------------
out()
out("=" * 88)
out("SECTION 5 — independent high-precision cross-check (mpmath, dps=40, true inverses)")
out("=" * 88)
mp.mp.dps = 40


def su2k_ST_mp(k):
    n = k + 2
    S = mp.matrix(k + 1, k + 1)
    for a in range(1, k + 2):
        for b in range(1, k + 2):
            S[a - 1, b - 1] = mp.sqrt(mp.mpf(2) / n) * mp.sin(mp.pi * a * b / n)
    T = mp.matrix(k + 1, k + 1)
    for a in range(1, k + 2):
        T[a - 1, a - 1] = mp.e ** (2j * mp.pi * (mp.mpf(a) ** 2 / (4 * n) - mp.mpf(1) / 8))
    return S, T


hp_dev = mp.mpf(0)
for k in (3, 5):
    S, T = su2k_ST_mp(k)
    Sinv = S ** -1                     # true inverse (LU), unitarity not presumed
    Tinv = T ** -1
    U = T * (S * Tinv * Sinv)          # rho(RL)
    Udag = mp.matrix(k + 1, k + 1)
    for i in range(k + 1):
        for j in range(k + 1):
            Udag[j, i] = mp.conj(U[i, j])
    ud = max(abs((U * Udag - mp.eye(k + 1))[i, j]) for i in range(k + 1) for j in range(k + 1))
    E, _ = mp.eig(U)
    md = max(abs(abs(l) - 1) for l in E)
    hp_dev = max(hp_dev, md)
    out(f"  k={k}: unitarity dev = {mp.nstr(ud, 3)},  max||lam|-1| = {mp.nstr(md, 3)}   [40 digits]")
out("=> at 40-digit precision the deviations sit at the noise floor (~1e-40): the float64")
out("   zeros of Sections 2-3 are exact identities, not rounding accidents.")

# ----------------------------------------------------------------------------------
out()
out("=" * 88)
out("VERDICT COMPUTATION")
out("=" * 88)
qmax = max([overall_q_dev, tower_dev, large_k_dev] + word_qdevs + mtc_devs)
out(f"quantum side:  max ||lambda|-1| over levels k=1..12,20,32,40, tower powers n=1..6,")
out(f"               8 words, 4 theories: {qmax:.3e}  (high-precision check: {mp.nstr(hp_dev, 3)})")
out(f"classical side: framework tower |lambda| = phi^k, e.g. phi^2 = {float(phi**2):.9f} "
    f"(deviation from unit circle {float(phi**2) - 1:.9f}); symplectic-permitted, unitary-forbidden.")
ok = qmax < TOL and hp_dev < mp.mpf(10) ** -35
out(f"discriminating-fact status: |lambda|=1 is word-independent, level-independent, and")
out(f"theory-independent on the quantum side ({'PASS' if ok else 'FAIL'} at tol {TOL:.0e} / 1e-35 hp) — it is the")
out("unitarity of the representation matrices, not a framework signal; the classical phi^k is the")
out("symplectic linearization doing what symplectomorphisms may do. Category-error kill UPHELD.")
out()
out("VERDICT: RECONFIRMED" if ok else "VERDICT: REVIVED (quantum moduli deviate — see numbers)")
