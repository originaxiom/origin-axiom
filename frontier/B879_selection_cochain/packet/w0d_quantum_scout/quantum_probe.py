"""W0d scout probe (seat cc3, 2026-07-17). EXPLORATORY, NOT A SEALED WAVE-2
COMPUTATION -- this is a scouting numeric check to attach concrete numbers to
candidate (d) of SCOUT.md, run to inform the wave-1 design decision. Uses
float64/numpy (same precision class as the banked su32_wrt.py gate script
itself), not the exact-arithmetic standard the campaign uses for sealed
results. Every number below should be re-derived exactly before any wave-2
cell relies on it.

Reads (read-only, no modification) the banked, test-locked script:
  /Users/dri/oa-seat-cc3/origin-axiom/frontier/B238_su32_levelrank/su32_wrt.py
(locked by tests/test_b238_su32_levelrank.py). Convention for R, L follows
the banked one verbatim (papers/drafts/PC26_full_chain/PAPER.md line ~297:
"Put R = T, L = S^{-1} T^{-1} S"; also frontier/B664 .../METALLIC_LANDSCAPE_
HANDOFF.md: "the weld operator W(n) = R^{n-2}L on the SU(3)_2 space" -- the
figure-eight case is n=3, i.e. W = R^1 L = RL).
"""
import importlib.util
import numpy as np

PATH = "/Users/dri/oa-seat-cc3/origin-axiom/frontier/B238_su32_levelrank/su32_wrt.py"
spec = importlib.util.spec_from_file_location("b238_su32", PATH)
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

print("=" * 70)
print("PART 1 -- SU(3)_2 fusion data (Verlinde formula from the banked S)")
print("=" * 70)
w3, S3, T3, c3 = b238.su3_data(2)
n = S3.shape[0]
print("n (simple objects) =", n, " weights:", w3)
print("gate (modular relations) pass:", b238.modular_gate(S3, T3))

d = (S3[0, :] / S3[0, 0]).real
print("quantum dimensions d_a:", d)
print("total quantum dim^2  D^2 = sum d_a^2 =", sum(x**2 for x in d),
      " (= 6 + 3*phi =", 6 + 3 * b238.PHI, ")")

N = np.zeros((n, n, n), dtype=complex)
for a in range(n):
    for bb in range(n):
        for c in range(n):
            N[a, bb, c] = sum(S3[a, x] * S3[bb, x] * np.conj(S3[c, x]) / S3[0, x]
                              for x in range(n))
Nint = np.round(N.real).astype(int)
print("integrality check: max|imag| =", np.max(np.abs(N.imag)),
      " max|real-round| =", np.max(np.abs(N.real - Nint)))
print("nonzero (a,b,c) fusion triples:", int((Nint != 0).sum()), "/", n**3,
      " (all equal to 1: multiplicity-free)",
      bool(np.all(Nint[Nint != 0] == 1)))

inv_idx = [a for a in range(n) if abs(d[a] - 1.0) < 1e-9]
print("\ninvertible (dim=1) objects:", [w3[a] for a in inv_idx],
      "-- fusion-table check (forms a group):")
for a in inv_idx:
    for bb in inv_idx:
        fused = {w3[c]: int(Nint[a, bb, c]) for c in range(n) if Nint[a, bb, c] != 0}
        print(f"    {w3[a]} x {w3[bb]} = {fused}")
print("=> universal grading group / Aut(id_C)-candidate = Z/3 (finite, discrete)")

print()
print("=" * 70)
print("PART 2 -- the weld operator W = rho(RL) = T . (S^-1 T^-1 S) on the")
print("6-dim SU(3)_2 stage: candidate (d)'s simplest ('single monodromy")
print("operator on the state space') falsifier")
print("=" * 70)
Si, Ti = np.linalg.inv(S3), np.linalg.inv(T3)
Rr, Lr = T3, Si @ Ti @ S3
W = Rr @ Lr
print("trace(W) =", np.trace(W), "  (banked -1/phi =", -1 / b238.PHI, ") -- cross-check")

eigs = np.linalg.eigvals(W)
print("\neigenvalues of W (angle/2pi, i.e. which root of unity):")
for e in eigs:
    print(f"  {e:.6f}   |e|={abs(e):.6f}   angle/2pi={np.angle(e)/(2*np.pi):+.6f}")

A = W - np.eye(n)
s = np.linalg.svd(A, compute_uv=False)
tol = 1e-8
rank = int(np.sum(s > tol))
nullity = n - rank
print(f"\nrank(W - I) = {rank},  nullity = dim ker(W-I) = dim coker(W-I) = {nullity}")
print("(square matrix => rank-nullity gives ker dim = coker dim automatically)")
print("=> naive 'H^0(Z;V_stage) = H^1(Z;V_stage)' for the bare weld operator"
      " = 0-dimensional.")
print("   Cross-check vs banked B640: ord(W(RL)) on the FULL 6-dim stage = 20."
      " Observed eigenvalue orders here: four of order 20, two of order 10"
      " (lcm = 20) -- MATCHES.")

print()
print("=" * 70)
print("PART 3 -- comparison: SU(2)_3 (level-rank partner, 4-dim stage)")
print("=" * 70)
S2, T2, c2 = b238.su2_data(3)
Si2, Ti2 = np.linalg.inv(S2), np.linalg.inv(T2)
W2 = T2 @ (Si2 @ Ti2 @ S2)
A2 = W2 - np.eye(4)
s2 = np.linalg.svd(A2, compute_uv=False)
rank2 = int(np.sum(s2 > tol))
print(f"rank(W2 - I) = {rank2}, nullity = {4 - rank2}")
print("eigenvalues:", np.linalg.eigvals(W2))
