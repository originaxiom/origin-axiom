"""B584 — Round 3 of the chord program: THE LISTENER.

X3 (B583): the vacuum is C-fixed and [C,S]=[C,T]=0, so filling/vacuum probes never
hear the theta-odd sector. This cell computes the minimal nontrivial listener on
the golden stage SU(3)_2 (B238's gate-verified modular data, kappa=5):

  R3-1  the theta-odd 2x2 block of the figure-eight monodromy rho(RL) — BLIND
        (trace, eigenvalues, multiplicative order);
  R3-2  the operational identity tr_odd rho = (Z - Z_C)/2 with Z_C = tr(C rho):
        the theta-odd amplitude = half (plain play - mirror-twisted play);
  R3-3  bare knots are deaf sources: J_3(4_1) = J_3bar(4_1) at generic q
        (B245's validated IMMM colored-HOMFLY formulas; dual color [1] vs [1,1]);
  R3-4  E6 level 2 re-read (cited from banked C3): char poly (l-1)(l^2+1)
        => theta-odd listener amplitude 1, order 4.

Banked gates that must reproduce: Z(RL; SU(3)_2) = -1/phi (B238); modular gate
green; exact even/odd decoupling (C central). Run: python3 theta_listener.py (pyenv).
Firewall: nothing to CLAIMS.md; no SM quantities (the B580 binding rule).
"""
import cmath
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(relpath, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, relpath))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = load("../B238_su32_levelrank/su32_wrt.py", "b238")
b245 = load("../B245_higher_color_levelrank/higher_color_levelrank.py", "b245")

PHI = (1 + 5 ** 0.5) / 2

# ---------------- the stage: SU(3)_2 (kappa = 5, the golden stage) ----------------
w, S, T, c = b238.su3_data(2)
n = len(w)
assert b238.modular_gate(S, T), "modular gate failed"

# charge conjugation C: weight (a,b) -> (b,a)
C = np.zeros((n, n))
for i, wt in enumerate(w):
    C[w.index((wt[1], wt[0])), i] = 1.0

# gates: C^2 = 1, C central in the modular rep, C = S^2
assert np.allclose(C @ C, np.eye(n))
assert np.allclose(C @ S, S @ C, atol=1e-10), "[C,S] != 0"
assert np.allclose(C @ T, T @ C, atol=1e-10), "[C,T] != 0"
# B238's column-norm normalization leaves a global sign: S^2 = -C here; the
# PERMUTATION pattern |S^2| = C is the convention-free statement.
assert np.allclose(np.abs(S @ S), C, atol=1e-9), "|S^2| != C"
print(f"gates: C^2=1, [C,S]=[C,T]=0, |S^2|=C  -- ALL PASS  (primaries {w})")

# the figure-eight monodromy (B238 convention: R=T, L=S^-1 T^-1 S)
Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
M = T @ (Si @ Ti @ S)
Z = np.trace(M)
assert abs(Z - (-1 / PHI)) < 1e-9, f"banked gate Z=-1/phi failed: {Z}"
print(f"banked gate: Z = tr rho(RL) = {Z.real:+.9f} = -1/phi  PASS")

# ---------------- R3-2: the operational identity ----------------
ZC = np.trace(C @ M)
P_odd = (np.eye(n) - C) / 2
tr_odd = np.trace(M @ P_odd)
tr_even = np.trace(M @ (np.eye(n) + C) / 2)
assert abs(tr_odd - (Z - ZC) / 2) < 1e-12
assert abs(tr_even + tr_odd - Z) < 1e-12
print(f"\nR3-2 the identity: tr_odd = (Z - Z_C)/2 with Z_C = tr(C rho)  VERIFIED")
print(f"  Z (plain play)          = {Z:+.9f}")
print(f"  Z_C (mirror-twisted)    = {ZC:+.9f}")
print(f"  tr_even                 = {tr_even:+.9f}")
print(f"  tr_odd (the listener)   = {tr_odd:+.9f}")

# ---------------- R3-1: the theta-odd block (BLIND) ----------------
pairs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w) if (wt[1], wt[0]) > wt]
odd = np.zeros((n, len(pairs)))
even_fixed = [i for i, wt in enumerate(w) if wt == (wt[1], wt[0])]
for j, (i, ib) in enumerate(pairs):
    odd[i, j], odd[ib, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
evenv = np.zeros((n, len(pairs) + len(even_fixed)))
for j, (i, ib) in enumerate(pairs):
    evenv[i, j], evenv[ib, j] = 1 / np.sqrt(2), 1 / np.sqrt(2)
for j, i in enumerate(even_fixed):
    evenv[i, len(pairs) + j] = 1.0

off = np.linalg.norm(evenv.T @ M @ odd) + np.linalg.norm(odd.T @ M @ evenv)
assert off < 1e-10, f"even/odd blocks do NOT decouple: {off}"
B_odd = odd.T @ M @ odd
print(f"\nR3-1 the theta-odd block (dim {len(pairs)}; pairs "
      f"{[(w[i], w[j]) for i, j in pairs]}; decoupling exact, off = {off:.1e}):")
for row in B_odd:
    print("   [" + "  ".join(f"{x:+.6f}" for x in row) + "]")
ev = np.linalg.eigvals(B_odd)
print(f"  eigenvalues: {['%+.6f%+.6fj' % (e.real, e.imag) for e in ev]}")
print(f"  |eigenvalues|: {[round(abs(e), 9) for e in ev]}")
print(f"  trace = {np.trace(B_odd):+.9f}")
order = None
P = np.eye(len(pairs), dtype=complex)
for k in range(1, 241):
    P = P @ B_odd
    if np.allclose(P, np.eye(len(pairs)), atol=1e-9):
        order = k
        break
print(f"  multiplicative order of the block: {order}")
# identify eigenvalue arguments as fractions of 2pi
for e in ev:
    arg = cmath.phase(e) / (2 * np.pi)
    print(f"    eig arg/2pi = {arg:+.9f}   (|e|={abs(e):.9f})")

# addendum (descriptive, post-blind): the deaf channel and the exact identification
B_even = evenv.T @ M @ evenv
ee = np.linalg.eigvals(B_even)
print(f"  even block (dim {B_even.shape[0]}) eigenvalues: "
      f"{['%+.4f%+.4fj' % (e.real, e.imag) for e in ee]}  (trace {np.trace(B_even):+.2e})")
assert abs(tr_even) < 1e-10, "tr_even not zero"
assert abs(np.trace(B_odd) - 2 * np.cos(3 * np.pi / 5)) < 1e-9
print("  exact identification: eigenvalues e^(+-3 pi i/5) (primitive 10th roots),")
print("  trace = 2cos(3pi/5) = -1/phi; the odd block is the order-10 golden rotation.")
print("  => tr_even = 0: the ENTIRE banked Z = -1/phi (B238) is theta-odd.")
print("  (SU(2)_3 contrast: all reps self-dual, C = 1, no odd sector -- the SAME")
print("   value -1/phi is trivially all-even there: the level-rank pair realizes")
print("   one number in two opposite sectors.)")

# ---------------- R3-3: bare knots are deaf sources ----------------
# su(3): J_3 = H^sym_[1](A=q^3, q); J_3bar = H^antisym_[1,1](A=q^3, q).
print("\nR3-3 bare-knot deafness: J_3(4_1) vs J_3bar(4_1) at generic q on the circle:")
worst = 0.0
for t in [0.13, 0.29, 0.41, 0.57, 0.73, 0.89, 1.07, 1.31]:
    q = cmath.exp(1j * t)
    j3 = b245.H_sym(1, q ** 3, q)
    j3b = b245.H_antisym(2, q ** 3, q)
    worst = max(worst, abs(j3 - j3b))
    print(f"  q=e^(i{t:.2f}):  J_3={j3:+.6f}   J_3bar={j3b:+.6f}   diff={abs(j3-j3b):.2e}")
assert worst < 1e-9, "J_3 != J_3bar -- STOP and re-derive (prereg falsifier)"
print("  => J_3 = J_3bar identically: the bare knot state has ZERO theta-odd component.")

# ---------------- R3-4: E6 level 2 (cited from banked C3) ----------------
print("\nR3-4 (cited, B570-C3 banked): E6_2 theta-odd block char poly (l-1)(l^2+1)")
print("  => theta-odd listener amplitude tr = 1 + i + (-i) = 1, order 4.")

print("\nALL GATES PASS")
