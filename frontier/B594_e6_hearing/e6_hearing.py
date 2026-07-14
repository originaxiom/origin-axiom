"""B594 — the E6 level-2 hearing law (see PREREGISTRATION.md).

The chiral amplitude is state-independent, so the E6 colored-invariant method
gap does not block it: verify the law with random C-symmetric states, and
identify the eps^2 coefficients with B589's banked sine-kernel amplitudes.

Run: python3 e6_hearing.py (pyenv, ~30 s). Nothing to CLAIMS.md.
"""
import cmath
import importlib.util
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "c3", os.path.join(HERE, "..", "B570_allowed_plays", "c3_e6_level2_monodromy.py"))
c3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c3)

# ---- the E6_2 stage (the fast vectorized build; gates as in B586) ----
W, eps_signs = c3.weyl_group()
assert len(W) == 51840
rho_w = c3.root_coords([1] * 6)
shifted = [c3.root_coords(p) + rho_w for p in c3.PRIM]
S = np.zeros((9, 9), dtype=complex)
Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
for a in range(9):
    for b in range(a, 9):
        ips = Wl[:, a, :] @ (c3.C @ shifted[b])
        S[a, b] = S[b, a] = np.sum(eps_signs * np.exp(-2j * np.pi * ips / c3.KH))
S /= np.sqrt((S @ S.conj().T)[0, 0].real)
if S[0, 0].real < 0:
    S = -S
ipf = lambda x, y: float(x @ (c3.C @ y))
cc = 2 * 78 / c3.KH
hs = [ipf(c3.root_coords(p), c3.root_coords(p) + 2 * rho_w) / (2 * c3.KH)
      for p in c3.PRIM]
T = np.diag([np.exp(2j * np.pi * (h - cc / 24)) for h in hs])
rho = T @ T @ S @ T                                # rho(A1), C3's word
Cm = (S @ S).real                                  # S^2 = +C on E6_2 (B586)
n = 9
conj_idx = [c3.PRIM.index(c3.theta(p)) for p in c3.PRIM]
assert np.allclose(Cm @ rho, rho @ Cm, atol=1e-9)

pairs = [(1, 2, "27"), (3, 4, "351'"), (7, 8, "351")]
U = np.zeros((n, 3))
for j, (a, b, _) in enumerate(pairs):
    U[a, j], U[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)


def weld(word_mat, twisted):
    return (Cm @ word_mat) if twisted else word_mat


def amp(psi, Wm):
    vec = Wm @ psi
    return sum(np.conj(psi[conj_idx[i]]) * vec[i] for i in range(n))


print("H1 — the law with RANDOM C-symmetric states (psi-independence):")
rng = np.random.default_rng(20260714)
lawok = True
for word_mat, wname in ((np.eye(9, dtype=complex), "I"), (rho, "A1")):
    for twisted in (True, False):
        Wm = weld(word_mat, twisted)
        for seed in range(3):
            # random C-symmetric psi: components equal on conjugate labels
            z = rng.normal(size=n) + 1j * rng.normal(size=n)
            psi = np.array([(z[i] + z[conj_idx[i]]) / 2 for i in range(n)])
            A0 = amp(psi, Wm)
            for j in range(3):
                u = U[:, j].astype(complex)
                quad = np.conj(u) @ Wm @ u
                for e in (0.07, 0.31):
                    Ae = amp(psi + e * u, Wm)
                    lawok &= abs(Ae - (A0 - e * e * quad)) < 1e-10
assert lawok
print("  A_eps = A_0 - eps^2 (u'Wu), no O(eps): EXACT for all random C-symmetric")
print("  states x directions x welds x eps  PASS (the law is state-independent)")

print("\nH2 — the eps^2 coefficients ARE B589's sine-kernel amplitudes:")
BANKED = {
    "27": (2 / math.sqrt(7)) * math.sin(2 * math.pi / 7)
          * cmath.exp(2j * math.pi * 3 / 14),
    "351'": (2 / math.sqrt(7)) * math.sin(6 * math.pi / 7)
            * cmath.exp(-2j * math.pi * 2 / 14),
    "351": (2 / math.sqrt(7)) * math.sin(4 * math.pi / 7)
           * cmath.exp(-2j * math.pi * 1 / 14),
}
Wt = weld(rho, True)
ok2 = True
for j, (a, b, nm) in enumerate(pairs):
    u = U[:, j].astype(complex)
    coeff = np.conj(u) @ Wt @ u
    # C = -1 on the odd space => u'(C rho)u = -u' rho u = -p_j
    match = abs(coeff + BANKED[nm]) < 1e-7
    ok2 &= match and abs(coeff.imag) > 1e-3
    print(f"  pair {nm:>4}: u'(C rho)u = {coeff:+.9f} = -p_{nm}: {match}  (Im != 0)")
assert ok2
print("  => THE E6 HEARING COEFFICIENTS = MINUS THE BANKED SINE-KERNEL AMPLITUDES:")
print("     -(2/sqrt7) sin(2pi j'/7) zeta_14^k — the handoff's prediction CONFIRMED.")

print("\nH3 — the full 3x3 odd quadratic form of C rho(A1) (new numbers):")
B = U.T @ Wt @ U
for row in B:
    print("   [" + "  ".join(f"{x:+.6f}" for x in row) + "]")
print(f"  trace = {np.trace(B):+.9f}  (= -1 = -C3's odd trace: "
      f"{abs(np.trace(B) + 1) < 1e-8})")
P4 = np.linalg.matrix_power(U.T @ rho @ U, 4)
print(f"  order-4 consistency (C3): {np.allclose(P4, np.eye(3), atol=1e-7)}")

print("\nTHE E6 HEARING LAW: a dial-displaced listener on the E6 level-2 stage")
print("hears the twist at order eps^2 with amplitudes -(sine kernel x zeta_14):")
print("the two-stage picture is complete — golden stage: 1/(2phi) + i sin(2pi/5)/sqrt5;")
print("E6 stage: the Z/7 sine kernel. Same law, stage-specific numbers.")
print("ALL GATES PASS")
