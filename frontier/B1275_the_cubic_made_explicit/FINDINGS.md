# B1275 — THE CUBIC MADE EXPLICIT: B308's unique E₆ cubic solved from the repository's own 27, and the Jordan ranks of the object's lattice vectors — the mirror's triple is a rank-3 element with |I₃| = 6

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (exact; an instrument plus three structural facts) · **Price: unchanged**

## Why

B308 proved the E₆ Yukawa 27³ → 1 is a **unique** cubic (multiplicity 1) and never wrote it down; B1271 located its
support (the 45 zero-sum weight triples, 40 + 5 by SO(10) block); B1272 found that the object's mirror selects one
zero-sum triple of the 27; L202 (`docs/THE_VIEW_FROM_ABOVE_2026-09-06.md`) asks for the E₆ orbit invariants of the
object's own 27-lattice vectors. All of these need the tensor itself. This arc solves it.

## 1. d_abc, solved ((a), exact over ℚ)

Unknowns: the 45 values of a symmetric cubic on the zero-sum triples of B883's weights. Equations: invariance under
all 78 generators of e₆ in the repository's own 27 (`frontier/B883_the_27/rep27.json`), Σ_{a′} X_{a′a} d_{a′bc} +
Σ_{b′} X_{b′b} d_{ab′c} + Σ_{c′} X_{c′c} d_{abc′} = 0 for every generator X and every triple (a, b, c). **The
nullspace is one-dimensional** (the cubic is unique — B308 reproduced), and after normalisation **every value is
±1** (28 of one sign, 17 of the other in this basis; the signs are basis-dependent, the support and |d| are not).

## 2. The Jordan ranks of the object's lattice vectors ((b), exact)

With I₃(q) = d_abc q^a q^b q^c and the Freudenthal adjoint q # q (rank 1 ⟺ q # q = 0; rank 2 ⟺ q # q ≠ 0, I₃ = 0;
rank 3 ⟺ I₃ ≠ 0):

| vector | Jordan rank | count |
|---|---|---|
| a single weight of the 27 | **1** | all 27 — the Spin(10) orbit (B962/B969's rank-1 VEV) |
| a sum of two weights | 1 or 2 | 216 / 135 |
| a **zero-sum triple** w₁ + w₂ + w₃ | **3**, I₃ = ±6 | all 45 |
| a non-zero-sum triple | 1 or 2 | 720 / 2160 |

**Rank 3 ⟺ a zero-sum triple.** The triple the object's mirror selects (B1272 §4: three mutually orthogonal weights
with E₆ parts summing to zero) is therefore a **non-degenerate element of the cubic, |I₃| = 6** — in the E₆(6)
reading of L202, a charge that carries an entropy (π√|I₃|), with its three charges equal in size, so that its
attractor point is the S₃-symmetric point of the moduli space. Recorded as structure; no identification made.

## Controls (MB12)

- The solve can fail (a nullspace of dimension 0 or > 1 would break B308); it is 1.
- The ranks are computed from the tensor, not asserted: the 720 / 2160 non-zero-sum triples never reach rank 3.

## Verification

`verification/cubic_explicit.py` (exact; ~2 min; `SELFTEST: PASS`), run record `verification/cubic_explicit_run.txt`.
Lock: `tests/test_b1275_the_cubic_made_explicit.py`. Feeds on B883 (the 27), B308 (uniqueness), B1271 (the support),
B1272 (the mirror's triple). Registers no identification change.
