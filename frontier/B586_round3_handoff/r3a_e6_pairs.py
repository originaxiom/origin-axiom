"""B586 R3-A — the E6 level-2 per-pair chirality amplitudes (the honest core of
chat-1's R3-A after the frame correction; see PREREGISTRATION.md).

Rebuilds the C3-gated E6_2 stage (S, T, rho(A1)) by importing the banked C3
module's building blocks, re-verifies the gates, then reports BLIND:
  * the three per-pair diagonal amplitudes <u_p|rho(A1)|u_p>, pairs
    (27,27b), (351',351'b), (351,351b);
  * Z, Z_C, tr_even, tr_odd and the identity tr_odd = (Z - Z_C)/2;
  * the lift identity on THIS stage: S^2 = +C (S00>0 convention), so
    tr(C rho) = +tr rho(S^2 W) — sign convention recorded vs B238's S^2 = -C;
  * the blind -1/phi question (per-pair, ratios, or absent).

Run: python3 r3a_e6_pairs.py (pyenv, ~2-4 min: |W(E6)| = 51840 BFS).
Firewall: nothing to CLAIMS.md; no SM quantities.
"""
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "c3", os.path.join(HERE, "..", "B570_allowed_plays", "c3_e6_level2_monodromy.py"))
c3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c3)

PHI = (1 + 5 ** 0.5) / 2
PRIM, NAMES, KH, Gm = c3.PRIM, c3.NAMES, c3.KH, c3.C

W, eps = c3.weyl_group()
assert len(W) == 51840
rho_w = c3.root_coords([1] * 6)
shifted = [c3.root_coords(p) + rho_w for p in PRIM]

S = np.zeros((9, 9), dtype=complex)
Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
for a in range(9):
    for b in range(a, 9):
        ips = Wl[:, a, :] @ (Gm @ shifted[b])
        S[a, b] = S[b, a] = np.sum(eps * np.exp(-2j * np.pi * ips / KH))
S = S / np.sqrt((S @ S.conj().T)[0, 0].real)
if S[0, 0].real < 0:
    S = -S

ip = lambda x, y: float(x @ (Gm @ y))
cc = 2 * 78 / KH
hs = [ip(c3.root_coords(p), c3.root_coords(p) + 2 * rho_w) / (2 * KH) for p in PRIM]
T = np.diag([np.exp(2j * np.pi * (h - cc / 24)) for h in hs])

# ---- gates (must reproduce C3) ----
assert np.linalg.norm(S @ S.conj().T - np.eye(9)) < 1e-9
assert np.linalg.norm(S - S.T) < 1e-9
C2 = S @ S
expect = np.zeros((9, 9))
for i, p in enumerate(PRIM):
    expect[PRIM.index(c3.theta(p)), i] = 1
assert np.allclose(C2, expect, atol=1e-9), "S^2 != +C on E6_2"
assert np.linalg.norm(np.linalg.matrix_power(S @ T, 3) - C2) < 1e-9
w1 = T @ T @ S @ T
w2 = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
assert np.linalg.norm(w1 - w2) < 1e-9
rho = w1
print("gates: |W|=51840, S unitary+symmetric, S^2 = +C (theta flip), (ST)^3 = S^2,")
print("       rho(A1) two words agree -- ALL PASS (C3 reproduced)")
print("NOTE the sign convention: E6_2 has S^2 = +C (S00>0); B238's SU(3)_2 had S^2 = -C.")

Cmat = C2.real
Z = np.trace(rho)
ZC = np.trace(Cmat @ rho)
tr_odd = np.trace(rho @ (np.eye(9) - Cmat) / 2)
tr_even = Z - tr_odd
assert abs(tr_odd - (Z - ZC) / 2) < 1e-12
# the lift identity on THIS stage: tr(C rho) = +tr(rho(S^2 . word))
assert abs(ZC - np.trace(S @ S @ rho)) < 1e-9
print(f"\nZ = {Z:+.8f}   Z_C = {ZC:+.8f}")
print(f"tr_even = {tr_even:+.8f}   tr_odd = {tr_odd:+.8f}   (identity verified)")

pairs = [(1, 2, "27/27b"), (3, 4, "351'/351'b"), (7, 8, "351/351b")]
odd = np.zeros((9, 3))
for j, (a, b, _) in enumerate(pairs):
    odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
B_odd = odd.T @ rho @ odd
assert abs(np.trace(B_odd) - 1) < 1e-8, "C3 gate: tr(B_odd) = 1"
P = B_odd.copy()
order = None
for k in range(2, 201):
    P = P @ B_odd
    if np.linalg.norm(P - np.eye(3)) < 1e-8:
        order = k + 0
        break
# C3 banked order 4
P4 = np.linalg.matrix_power(B_odd, 4)
assert np.linalg.norm(P4 - np.eye(3)) < 1e-8, "C3 gate: order 4"

print("\nTHE PER-PAIR CHIRALITY AMPLITUDES (BLIND -- the new numbers):")
for j, (a, b, nm) in enumerate(pairs):
    d = B_odd[j, j]
    print(f"  <u|rho|u> [{nm:>11}] = {d:+.8f}")
print("full odd 3x3 block (pair basis):")
for row in B_odd:
    print("   [" + "  ".join(f"{x:+.6f}" for x in row) + "]")
print(f"odd-block trace = {np.trace(B_odd):+.8f} (C3 gate: 1), order 4 (C3 gate)  PASS")

print("\nblind -1/phi check (target 0.61803399):")
vals = [B_odd[j, j] for j in range(3)] + [Z, ZC, tr_even, tr_odd]
hits = [v for v in vals if abs(abs(v) - 1 / PHI) < 1e-6]
print(f"  matches among the amplitudes/traces: {hits if hits else 'NONE'}")
rat = []
for i in range(3):
    for j in range(3):
        if i != j and abs(B_odd[j, j]) > 1e-9:
            r = B_odd[i, i] / B_odd[j, j]
            if abs(abs(r) - 1 / PHI) < 1e-6 or abs(abs(r) - PHI) < 1e-6:
                rat.append((i, j, r))
print(f"  golden ratios between pair amplitudes: {rat if rat else 'NONE'}")
