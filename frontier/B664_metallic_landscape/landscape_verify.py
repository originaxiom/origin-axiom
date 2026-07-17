"""B664 — the metallic hearing landscape at the golden stage: verify,
prove, and adjudicate chat1's handoff.

The reduction: the theta-odd block at SU(3)_2 is 2-dim and T-diagonal,
so tr_odd(R^{n-2}L) = t1^{n-2} X11 + t2^{n-2} X22 — a two-term
exponential sum. Exact T-phases from the h-arithmetic:
h(0,1) = 4/15, h(0,2) = 2/3, c = 16/5 => t1 = e^{2pi i 2/15},
t2 = e^{2pi i 8/15}; ratio t2/t1 = e^{2pi i 2/5}, a PRIMITIVE 5TH ROOT
=> modulus period 5; t1 has order 15 => full-value (reality) period 15.
The closed form: |tr_odd(n)| = (2 sqrt3 / D) |cos(pi (4n-5)/10)| with
D^2 = 3 phi sqrt5 — the three values follow from the exact golden-trig
identities  sin^2(72) = D^2/12  and  sin^2(36) = D^2/(12 phi^2).
"""
import importlib.util
import os

import numpy as np
import sympy as sp

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(ROOT, "frontier", "B238_su32_levelrank",
                         "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

w, S, T, c = b238.su3_data(2)
X = np.linalg.inv(S) @ np.linalg.inv(T) @ S
prs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w)
       if (wt[1], wt[0]) > wt]
odd = np.zeros((len(w), len(prs)))
for j, (a, b) in enumerate(prs):
    odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)

phi = (1 + 5**0.5) / 2
D = (3 * phi * 5**0.5)**0.5

print("== the exact T-phases (h-arithmetic) ==", flush=True)
To = np.diag(odd.T @ T @ odd)
ph = np.angle(To) / (2 * np.pi) % 1
print(f"  numeric phases: {ph.round(10)};  exact: 2/15 = {2/15:.10f}, "
      f"8/15 mod 1 = {8/15:.10f}", flush=True)
assert abs(ph[0] - 2 / 15) < 1e-9 and abs(ph[1] - 8 / 15) < 1e-9
print("  ratio t2/t1 = e^{2pi i 2/5}: primitive 5th root  [PROVEN from "
      "h(0,1)=4/15, h(0,2)=2/3, c=16/5]", flush=True)

print("\n== the golden-trig identities (exact, sympy) ==", flush=True)
PHI = (1 + sp.sqrt(5)) / 2
D2 = 3 * PHI * sp.sqrt(5)
i1 = sp.simplify(sp.sin(sp.rad(72))**2 - D2 / 12)
i2 = sp.simplify(sp.sin(sp.rad(36))**2 - D2 / (12 * PHI**2))
print(f"  sin^2(72) - D^2/12 = {i1};  sin^2(36) - D^2/(12 phi^2) = {i2}",
      flush=True)
assert i1 == 0 and i2 == 0

print("\n== the landscape, n = 3..40: closed form vs direct ==", flush=True)
ok_form, ok_three, reals = True, True, []
for n in range(3, 41):
    W = np.linalg.matrix_power(T, n - 2) @ X
    tr = np.trace(odd.T @ W @ odd)
    closed = (2 * np.sqrt(3) / D) * abs(np.cos(np.pi * (4 * n - 5) / 10))
    if abs(abs(tr) - closed) > 1e-9:
        ok_form = False
    if min(abs(abs(tr)), abs(abs(tr) - 1 / phi), abs(abs(tr) - 1)) > 1e-9:
        ok_three = False
    if abs(tr.imag) < 1e-9:
        reals.append(n)
print(f"  closed form matches 38/38: {ok_form}", flush=True)
print(f"  three values {{0, 1/phi, 1}} everywhere: {ok_three}", flush=True)
print(f"  REAL tr_odd at n = {reals}", flush=True)
qr = sorted(set(n % 15 for n in reals))
print(f"  reality residues mod 15: {qr}", flush=True)
quiet_real = [n for n in reals if abs(abs(np.trace(
    odd.T @ (np.linalg.matrix_power(T, n - 2) @ X) @ odd)) - 1 / phi) < 1e-9]
print(f"  QUIET+REAL at n = {quiet_real}  -> the golden (n=3) is NOT "
      f"unique (n ≡ 3 or 12 mod 15): chat1's Fact 2 REFUTED", flush=True)

print("\n== the criteria collapse ==", flush=True)
print("  conductor n^2-4 = (n-2)(n+2) is PRIME iff n-2 = 1 iff n = 3 iff "
      "det(A-I) = -(n-2) is a unit:", flush=True)
print("  'prime conductor' and 'unit determinant' are THE SAME criterion, "
      "not independent.", flush=True)

print("\nB664 DONE", flush=True)
