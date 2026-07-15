"""B598 P3 — V3, THE E6_2 RANK PRODUCTION (sealed prereg cell 3 of 3;
runs ONLY after V2's output is committed).

Per STEP8_P3_PREREG.md: rebuild the banked B594-H3 3x3 odd quadratic form
B = U^T (C rho(A1)) U on the E6_2 stage (same construction as
e6_hearing.py, machinery gates included), then compute its
complex-conjugation pairing structure — NEVER computed before.

REQUIRED (V3 PASS): the spectrum of B splits as ONE non-real conjugate
pair {lambda, conj(lambda)} + ONE real eigenvalue mu != 0 with
|mu| != |lambda| — the conjugation-equivariant rank-2 + rank-1 splitting
(2 <-> 2 restored by structure; the third channel separated). The
computable equivalent: the characteristic polynomial has real
coefficients (trace is banked = -1), exactly one real root, and the
separation holds. Complex sigma_2 or det, three real roots, mu = 0, or
|mu| = |lambda| FAILS the cell.

Run: python3 p3_v3_e62_rank.py   (~2 min)
"""
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "c3", os.path.join(HERE, "..", "B570_allowed_plays",
                       "c3_e6_level2_monodromy.py"))
c3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c3)

# ---- the E6_2 stage (B594's construction verbatim; gates) -------------------
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
rho = T @ T @ S @ T
Cm = (S @ S).real
assert np.allclose(Cm @ rho, rho @ Cm, atol=1e-9)
n = 9
pairs = [(1, 2, "27"), (3, 4, "351'"), (7, 8, "351")]
U = np.zeros((n, 3))
for j, (a, b, _) in enumerate(pairs):
    U[a, j], U[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)

B = U.T @ (Cm @ rho) @ U
print("the 3x3 odd form B (B594-H3, rebuilt):", flush=True)
for row in B:
    print("   [" + "  ".join(f"{x:+.9f}" for x in row) + "]", flush=True)
tr = np.trace(B)
gate_tr = abs(tr + 1) < 1e-8
print(f"machinery gate: trace = {tr:+.9f} (banked -1): {gate_tr}", flush=True)
assert gate_tr, "trace gate failed"

# ---- THE BLIND ANALYSIS: the conjugation pairing structure ------------------
e2 = ((np.trace(B) ** 2 - np.trace(B @ B)) / 2)
e3 = np.linalg.det(B)
real_coeffs = abs(e2.imag) < 1e-8 and abs(e3.imag) < 1e-8
print(f"sigma_2 = {e2:+.9f}   det = {e3:+.9f}", flush=True)
print(f"(i) char poly real (spectrum conjugation-closed): {real_coeffs}",
      flush=True)

lams = np.linalg.eigvals(B)
lams = sorted(lams, key=lambda z: z.imag)
print(f"eigenvalues: " + "  ".join(f"{z:+.9f}" for z in lams), flush=True)
real_ones = [z for z in lams if abs(z.imag) < 1e-7]
nonreal = [z for z in lams if abs(z.imag) >= 1e-7]
one_pair = (len(real_ones) == 1 and len(nonreal) == 2
            and abs(nonreal[0] - np.conj(nonreal[1])) < 1e-7)
print(f"(ii) exactly one non-real conjugate pair + one real: {one_pair}",
      flush=True)
mu_ok = len(real_ones) == 1 and abs(real_ones[0]) > 1e-8
sep_ok = (one_pair and mu_ok
          and abs(abs(real_ones[0]) - abs(nonreal[0])) > 1e-6)
print(f"(iii) mu != 0: {mu_ok};  |mu| != |lambda| (width separation): "
      f"{sep_ok}", flush=True)

verdict = real_coeffs and one_pair and mu_ok and sep_ok
print(f"\nV3 VERDICT (the E6_2 rank-2+1 conjugation splitting): "
      f"{'PASS' if verdict else 'FAIL'}", flush=True)
print("banked blind; the outcome statement follows the locked A/B/D table.",
      flush=True)
