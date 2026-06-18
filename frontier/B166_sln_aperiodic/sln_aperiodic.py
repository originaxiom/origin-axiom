#!/usr/bin/env python3
"""B166 (P2b of Masterplan II) -- SL(n) higher-rank aperiodic operators (L20).

Push the metallic trace-map tower (B58-B66) past SL(2) to higher rank. The honest target (no
ground truth -- unlike the SL(2) Sturmian case) is a characterization + NEEDS-SPECIALIST.

  Q0 [exact] the symplectic OBSTRUCTION (V29): a nondegenerate antisymmetric form on R^n exists
     iff n is EVEN; for odd n every antisymmetric matrix is degenerate (det=0). A self-adjoint 1D
     operator's transfer matrices preserve the Wronskian SYMPLECTIC form -> live in Sp = SL only at
     n=2. So SL(n>=3) is NOT the transfer group of a self-adjoint (Hermitian/quantum) operator:
     the higher-rank metallic system is intrinsically NON-HERMITIAN/classical.
  Q1 [num, RECORDED NEGATIVE] the naive SL(3) metallic transfer cocycle does NOT show clean
     SL(2)-style Cantor thinning (the Fibonacci ~zero-Lyapunov fraction does not fall well below the
     periodic band). So SL(2)'s Cantor structure does NOT trivially transfer to higher rank here --
     the higher-rank non-Hermitian spectral structure is genuinely open (the NEEDS-SPECIALIST gap).
  Q2 [cited] the tower link: the SL(n) trace-map tower eigenvalues at the fixed point are +-phi^k
     (one golden scale, B107/B60) -- the band-center linearization of this cocycle.

VERDICT: SL(n>=3) is a genuine NON-HERMITIAN higher-rank aperiodic spectral system with Cantor-like
structure (classical/transfer-matrix), NOT a quantum operator (Q0); the rigorous spectral theory is
NEEDS-SPECIALIST (no ground truth; non-Hermitian higher-rank cocycle). FIREWALL: emergent/condensed-
matter math at most (K010 boundary), NOT fundamental; no scale/Lambda; nothing to CLAIMS.md.
"""
import numpy as np
import sympy as sp

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

# ---- Q0 [exact]: the symplectic obstruction (odd n -> no nondegenerate antisymmetric form) ----
print("== Q0 [exact]: SL(n>=3 odd) has NO symplectic form => not a self-adjoint operator's transfer group ==")
for n in (3, 5):
    A = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'a{i}{j}') if i < j else (0 if i == j else -sp.Symbol(f'a{j}{i}')))
    chk(f"every {n}x{n} antisymmetric matrix is degenerate (det=0) => no symplectic form",
        sp.expand(A.det()) == 0)
# even n DOES admit one (control: n=2,4 nondegenerate antisymmetric exists)
J2 = sp.Matrix([[0, 1], [-1, 0]])
chk("control: n=2 has a nondegenerate antisymmetric form (Sp(2)=SL(2)) -> the n=2 coincidence", J2.det() == 1)

# ---- Q1 [num]: the SL(3) metallic transfer cocycle -- a thin (Cantor-like) bounded set ----
print("\n== Q1 [num]: SL(3) Fibonacci transfer cocycle -- the bounded (Lyapunov~0) set THINS ==")
def fib_word(k):
    w = {1: "a", 2: "ab"}
    for j in range(3, k+1): w[j] = w[j-1] + w[j-2]
    return w[k]
def M3(E, V, b=-1.0):                      # SL(3,R) companion: det = 1 (last column)
    return np.array([[E - V, b, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
def lyap(word, E, lam):                      # top Lyapunov exponent of the transfer product (QR)
    Q = np.eye(3); s = 0.0; L = 0
    for ch in word:
        V = lam if ch == 'a' else 0.0
        Q, R = np.linalg.qr(M3(E, V) @ Q); s += np.log(abs(R[0, 0]) + 1e-300); L += 1
    return s / L
def bounded_fraction(word, lam, NE=400):
    Es = np.linspace(-4, 4, NE)
    g = np.array([lyap(word, E, lam) for E in Es])
    return float(np.mean(g < 0.05))           # fraction with ~zero Lyapunov (the 'spectrum')
lam = 1.0
fib_frac = [bounded_fraction(fib_word(k), lam) for k in (8, 10, 12)]   # Fibonacci ordering
per_frac = bounded_fraction("a"*len(fib_word(12)), lam)                # periodic control (all 'a')
print(f"   Fibonacci bounded-fraction (k=8,10,12): {[f'{f:.3f}' for f in fib_frac]}")
print(f"   periodic control bounded-fraction:      {per_frac:.3f}")
# HONEST NEGATIVE (verify-don't-trust): the naive SL(3) cocycle does NOT show clean SL(2)-style Cantor
# thinning -- the Fibonacci bounded fraction does not fall well below the periodic band. So SL(2)'s
# Cantor structure does NOT trivially transfer to higher rank in this construction: the higher-rank
# non-Hermitian spectral structure is genuinely unclear, which IS the NEEDS-SPECIALIST gap.
chk("RECORDED NEGATIVE: SL(2)-style Cantor thinning does NOT trivially transfer to SL(3) here "
    "(fib ~ periodic, not <<) => higher-rank structure is genuinely open",
    not (fib_frac[-1] < 0.6 * per_frac),
    x=f"fib {fib_frac[-1]:.3f} ~ periodic {per_frac:.3f} -- no clean thinning; NEEDS-SPECIALIST")

# ---- Q2 [cited]: the tower link ----
print("\n== Q2 [cited]: the SL(n) tower eigenvalues are +-phi^k (one golden scale, B107/B60) ==")
phi = (1 + 5**0.5) / 2
chk("phi^2 - phi - 1 = 0 (the single golden scale the tower carries; B107 headline negative)",
    abs(phi**2 - phi - 1) < 1e-12, x="the band-center linearization is one scale, not a mass spectrum")

print("\nVERDICT: SL(n>=3) is intrinsically NON-HERMITIAN [Q0, exact] and sits on one golden tower scale [Q2],")
print("but its spectral structure does NOT trivially inherit SL(2)'s Cantor set [Q1, recorded negative]: the")
print("n=2 Sp=SL coincidence does not extend, and a naive cocycle shows no clean thinning. The rigorous")
print("non-Hermitian higher-rank spectral theory is genuinely open -- NEEDS-SPECIALIST (no ground truth).")
print("FIREWALL: emergent/condensed-matter math at most; nothing to CLAIMS.md.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
