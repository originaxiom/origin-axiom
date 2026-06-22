#!/usr/bin/env python3
"""B192 (Masterplan III, Track D -- SL(n>=3) higher-rank Lyapunov spectra; L20/B166).

*** CORRECTED 2026-06-23 (independent adversarial verification) -- the original "parity law" is REFUTED. ***

The ORIGINAL B192 claim (now RETRACTED) was: the metallic SL(n) Lyapunov spectrum is SYMMETRIC iff n EVEN /
ASYMMETRIC iff n ODD (realizing V29), and this is SPECIAL to the metallic cocycle. Independent verification BROKE it:
the apparent parity was an artifact of (a) CHERRY-PICKED energies and (b) a RIGGED control (dense-Gaussian SL(n),
which has none of the transfer-matrix structure). The honest computation:

  D1 [SL(n) structure -- STANDS] the full Lyapunov spectrum (QR-flag) sums to 0 (det=1) for n=3,4,5.
  D2 [REFUTED: there is NO even/odd parity law] the symmetry defect Sum|g_i+g_{n+1-i}| at the cherry-picked
     energies (n=4:0.003 "symmetric") INVERTS on a fair broad energy grid: n=2:0.00, n=3:0.03, n=4:0.34, n=5:0.41,
     n=6:0.50 -- it grows monotonically with n, with NO even/odd alternation (n=4 is MORE asymmetric than n=3; n=6,
     even, is NOT symmetric). The "law" was a property of three hand-picked energies, not of the cocycle.
  D3 [REFUTED: NOT special to the metallic cocycle] a RANDOM potential in the SAME companion matches metallic on
     the fair grid (n=4: randpot 0.337 vs metallic 0.344) -- so the (energy-dependent) approximate +-symmetry is a
     STRUCTURAL property of the nearest-neighbour transfer/companion matrix (its eigenvalues come in reciprocal
     pairs lambda, 1/lambda at the relevant energies), present for random/periodic potentials too. The original
     "163x special" compared metallic-at-cherry-energy against a dense-Gaussian SL(n) (no transfer structure) --
     apples-to-oranges; matched against a same-companion random potential the ratio is ~1x.
  D4 [what SURVIVES + firewall] V29 (the symplectic form exists iff n even) is NOT realized as a Lyapunov-spectrum
     parity. B166's ORIGINAL results STAND (they are B166, not B192): SL(n>=3) is intrinsically non-Hermitian via
     the symplectic obstruction [exact], and the naive SL(3) cocycle shows no clean SL(2)-style Cantor thinning
     [recorded negative]. The rigorous higher-rank spectral theory stays NEEDS-SPECIALIST. Emergent non-Hermitian
     math (K010 boundary); nothing to CLAIMS.md; P1-P16 frozen.

VERDICT (corrected): the B192 deepening (a metallic parity law realizing V29) is REFUTED -- it was an energy-cherry
-picking + rigged-control artifact, caught by independent verification (verify-don't-trust). Only D1 (sum=0) and
B166's standing results survive; the apparent symmetry is a generic transfer-matrix reciprocal-pairing effect, not a
parity law and not metallic-special. A recorded negative.
"""
import numpy as np

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

rng = np.random.default_rng(7)
phi = (1 + 5**0.5)/2
def fib_word(k):
    w = {1: "a", 2: "ab"}
    for j in range(3, k+1): w[j] = w[j-1] + w[j-2]
    return w[k]
def Mn(n, E, V):
    if n == 2: return np.array([[E - V, -1.0], [1.0, 0.0]])
    M = np.zeros((n, n)); M[0, 0] = E - V; M[0, 1] = -1.0; M[0, n-1] += (-1.0)**(n-1)
    for i in range(1, n): M[i, i-1] = 1.0
    return M
def lyap_spectrum(mats):
    n = mats[0].shape[0]; Q = np.eye(n); s = np.zeros(n)
    for M in mats:
        Q, R = np.linalg.qr(M @ Q); d = np.sign(np.diag(R)); Q = Q*d; R = (R.T*d).T
        s += np.log(np.abs(np.diag(R)) + 1e-300)
    return np.sort(s/len(mats))[::-1]
def asym(g): return float(np.sum(np.abs(g + g[::-1]))/2)
def metallic_defect(n, Es, k=13):
    w = fib_word(k)
    return asym(np.mean([lyap_spectrum([Mn(n, E, 1.0 if c == "a" else 0.0) for c in w]) for E in Es], axis=0))
def randpot_defect(n, Es, L=600):
    V = rng.uniform(0, 1.0, L)
    return asym(np.mean([lyap_spectrum([Mn(n, E, v) for v in V]) for E in Es], axis=0))

# ---- D1: sum=0 (SL(n)) ----
sums = {n: float(np.mean([lyap_spectrum([Mn(n, E, 1.0 if c == "a" else 0.0) for c in fib_word(12)])
                          for E in (1.3, 2.1, -1.7)], axis=0).sum()) for n in (3, 4, 5)}
chk("D1 [SL(n) structure STANDS]: the metallic Lyapunov spectrum sums to 0 (det=1) for n=3,4,5",
    all(abs(sums[n]) < 1e-9 for n in (3, 4, 5)))

# ---- D2: refute the parity law (cherry inverts on a fair grid) ----
cherry = [1.3, 2.1, -1.7]; fair = list(np.linspace(-3.5, 3.5, 15))
dc = {n: metallic_defect(n, cherry) for n in (2, 3, 4, 5, 6)}
df = {n: metallic_defect(n, fair) for n in (2, 3, 4, 5, 6)}
print("   symmetry defect:  n |  cherry-energies | fair broad grid")
for n in (2, 3, 4, 5, 6):
    print(f"                    {n} |  {dc[n]:14.3f}  | {df[n]:.3f}")
chk("D2 [REFUTED -- no parity law]: the 'even-symmetric' pattern at the cherry-picked energies (n=4~0.003) INVERTS "
    "on a fair broad grid (n=4>0.2 asymmetric, n=3<0.1; n=6 even NOT symmetric) -- energy-dependent, not a law",
    dc[4] < 0.02 and df[4] > 0.2 and df[6] > 0.2 and df[3] < df[4],
    x=f"cherry n4={dc[4]:.3f} vs fair n4={df[4]:.3f}; fair n6={df[6]:.3f} (no even/odd alternation)")

# ---- D3: refute metallic-specialness (random potential matches) ----
rp4 = randpot_defect(4, fair); rp6 = randpot_defect(6, fair)
chk("D3 [REFUTED -- not metallic-special]: a RANDOM potential in the same companion matches metallic on the fair "
    "grid (n=4: randpot ~ metallic) -- the approximate symmetry is a reciprocal-pair transfer-matrix structural "
    "property, not special to the metallic ordering; the original '163x' used a rigged dense-Gaussian control",
    abs(rp4 - df[4]) < 0.06 and abs(rp6 - df[6]) < 0.06,
    x=f"fair n=4: randpot {rp4:.3f} ~ metallic {df[4]:.3f}; n=6: randpot {rp6:.3f} ~ metallic {df[6]:.3f}")

# ---- D4: what survives (V29/B166) ----
import sympy as sp
A5 = sp.Matrix(5, 5, lambda i, j: sp.Symbol(f'a{i}{j}') if i < j else (0 if i == j else -sp.Symbol(f'a{j}{i}')))
chk("D4 [survives -- B166 stands]: V29 is NOT realized as a Lyapunov parity, but B166's ORIGINAL exact result "
    "holds -- every odd-n antisymmetric form is degenerate (det=0) => SL(n>=3 odd) is intrinsically non-Hermitian; "
    "rigorous higher-rank theory stays NEEDS-SPECIALIST",
    sp.expand(A5.det()) == 0 and abs(phi**2 - phi - 1) < 1e-12,
    x="V29 (symplectic-form-iff-even) intact at the algebra level; not a spectrum parity")

print("\nVERDICT (CORRECTED): the B192 'parity law' (metallic Lyapunov spectrum symmetric iff n even, realizing V29,")
print("special to the metallic cocycle) is REFUTED by independent verification -- an artifact of cherry-picked")
print("energies (the pattern inverts on a fair grid: n=4->0.34, n=6->0.50) and a rigged dense-Gaussian control (a")
print("same-companion RANDOM potential matches metallic). The approximate +-symmetry is a generic reciprocal-pair")
print("transfer-matrix property, energy-dependent, not metallic-special. SURVIVES: D1 (sum=0) + B166's exact V29")
print("obstruction + no-Cantor-thinning negative. A recorded NEGATIVE (verify-don't-trust). The rigorous higher-rank")
print("theory stays NEEDS-SPECIALIST. FIREWALL: emergent non-Hermitian math (K010); nothing to CLAIMS.md; P1-P16 frozen.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
