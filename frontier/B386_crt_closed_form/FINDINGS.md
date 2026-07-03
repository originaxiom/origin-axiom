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

---

# L2 BANKED: THE CLOSED FORM — the 1/12 derived end-to-end (→ P66)

**The identity (verified exact, both classes):**

    partial(K) = (1/240) · Σ_{4 window terms, signs} Σ_{j₄,l₄ ∈ ℤ₄×ℤ₄}
                    f_K^{term}(j₄,l₄) · GH_K^{term}(j₄ mod 2, l₄ mod 2)

with f = (ζ₄-window parts)·C₃·ind₃ (the 3-side 16-cell table) and GH = the 5-side lattice
sums (ζ₅/ζ₃-window parts · C₅ · ind₅ over the period-(10,6) lattice at fixed parities).
Assembly reproduces **(0,0,−1/16,−1/16)** (class 1) and **(0,0,−1/48,−1/48)** (class 5)
EXACTLY — with L1 this derives 1/12 = 1/16 + 1/48 from local data end-to-end.

**Structure in the factors (term (6,2) shown; closed_form.json has all):**
- class-1: GH depends only on the parity SUM — GH[00] = GH[11] = 25/4 − √5/4 − √−15/2 and
  GH[01] = GH[10] = −5/8 − √5/8 + (5/8)√−3 + (5/8)√−15 — a ℤ₂ grading of the 5-side sums.
- class-5 (the golden boundary): **the unequal-parity branches VANISH** — GH[01] = GH[10] = 0;
  GH[00] = GH[11] = 5/8 + √5/8 − (5/8)√−3 − √−15/8. The boundary couples equal parities only.

**Provenance.** windowed_split.py (the periods + end-to-end gate), closed_form.py (~3 min)
→ closed_form.json, windowed_split.json; locks tests/test_b386_tensor.py. W1 exits BANKED
on session 2 of 2 (time-box respected).
