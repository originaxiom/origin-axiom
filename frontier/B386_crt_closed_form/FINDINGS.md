# B386 (W1) — L1 BANKED: the Par-trace tensor identity

**Status: L1 banked; L2 (the windowed split → closed form) next session (within the W1
time-box). Pre-registration: PREREGISTRATION.md (committed first). Firewalled.**

**L1 (the gate): C[j,l] = C₃[j,l] · C₅[j,l] exactly, all 240 cells** — the level-15
Par-graded trace is the product of the q=3 and q=5 local theta-model Par-traces at the
banked multiplier convention (u₃,u₅) = (2,2) (the naive (1,1) fails at 146/240 cells: the
multiplier is load-bearing, consistent with B377's tensor law). Consequence: every seam
constant — including the 1/12 — factorizes into 3-local × 5-local data; L2 evaluates the
windowed sums (note for L2: the 5-local factor has period 10 = 2·5, sharing its 2-part
with the 3-local period 4 — the closed form is a two-branch product over the shared parity,
not a naive ℤ₄×ℤ₅ split).

**Provenance.** tensor_gate.py (~2 min) → tensor_gate.json; lock in
tests/test_b386_tensor.py.
