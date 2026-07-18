# B698 Leg A — THE MEETING, PROBED (analytic side): a product with a ℤ/2 residue

*cc banking seat, 2026-07-18. Owner directive "go FULL ON for 2 and 3,
very informed." Leg A = the rigorous computation (S067 row 2's analytic
side); Leg B (the firewalled interface) is separate. Prereg sealed
BEFORE the verdict (PREREG_LEG_A.md, sha 1e51ae30). Two literature sweeps
(deep, primary-source) ground every claim. Gate 5 stands.*

## The question (sealed)

The figure-eight A-polynomial's elliptic model is the conductor-15 curve
15a8 (j = −1/15, N = 3·5). Does the level-15 meeting's ANALYTIC content
(special L-values) COUPLE the being-prime 3 and hearing-prime 5 — an
entanglement neither hand has — or is it FACTORED (both primes present
only as independent Euler factors)?

## VERDICT: FACTORED — but a *product with a residue*, not nothing.

### 1. No analytic coupling — by a theorem, not just base-rate.
The weight-2 level-15 newform (15.2.a.a, = E₁₅) is non-CM, rank 0, ε = +1,
with **W₃ = +1, W₅ = −1** (confirms B695). By **Flath's tensor-product
theorem** its automorphic representation is a restricted tensor product
π = ⊗′ᵥ πᵥ — the primes 3 and 5 are **independent local factors by
construction**; W₃, W₅ commute; L(E,s) is an Euler product with
independent factors at 3 and 5. "The two faces couple at level 15" is the
WRONG WORD for the automorphic/analytic structure. Confirmed empirically:
- L(15a,1) = Ω/16 with **Ш = 1** — generic BSD, no exotic.
- **Base-rate control** (rank-0 conductor-p·q curves): 15a8's L(2)/being =
  0.847 sits mid-spread (0.85→1.71; 26a1 = 1.009 is *closer* to a round
  value) — 15a8's special values are unremarkable.
- **PSLQ** (60 digits): no integer relation among {m(A_{4₁}), L(15a,2),
  L'(15a,0), L(χ₋₃,2), π}. The meeting carries no hidden being-value.

So the strong reading of S067 row 2 — "reality is the *entanglement* of
the two hands" — is **FALSIFIED structurally.** The meeting does not fuse.

### 2. The meeting's ONE genuine new invariant: a genus-theory ℤ/2.
Where 3·5 truly *manufactures* something neither hand has is NOT the
L-function (it factors) but the **field arithmetic**:
- h(ℚ(√−3)) = 1, h(ℚ(√5)) = 1, but **h(ℚ(√−15)) = ℤ/2** (verified two
  ways: reduced binary quadratic forms + sage class group).
- Genus theory: the 2-rank of Cl(ℚ(√d)) = ω(disc) − 1; for −15 = (−3)·5
  there are two prime discriminants, so the 2-rank is exactly 1. **The ℤ/2
  exists iff both primes are present.**
The meeting is a **product that leaves a ℤ/2 residue** — an orientation
bit, invisible to either hand alone, landing exactly on the program's
ℤ/2 orientation/residue/c-pair spine ([[two-chiralities-c-vs-theta]],
the breath campaign).

### 3. The being hand keeps its own analytic quantity (K₃, not K₂).
The sharpest structural fact, PSLQ-verified:
- The figure-eight's OWN Mahler measure **m(A_{4₁}) = Vol/π = (3√3/2π)·
  L(χ₋₃,2)** (exact to 40+ digits) is the **Borel regulator of
  K₃ⁱⁿᵈ(ℚ(√−3))** — the BEING hand's arithmetic (Zagier; Boyd; B683).
- The MEETING's K₂ Beilinson regulator is a **different** number,
  **L'(15a,0) = 0.25133… = m(1 + x + 1/x + y + 1/y)** — Deninger's curve,
  a model of X₀(15) = 15a1, a *different curve in the same isogeny class*.
- m(A_{4₁}) = 0.6461 vs L(15a,2) = 0.6615 is a **2.37% near-miss** (a real
  numerical trap — no PSLQ relation). Precedent: Boyd 1998 exhibits a
  *different* conductor-15 genus-1 curve whose measure is "type D
  (dilogarithm), not type E (elliptic L′)" — conductor-matching does NOT
  fix the K-group.
- So even at conductor 15, the being hand's analytic quantity (K₃) is
  arithmetically independent of the meeting's (K₂). **The two hands share
  a conductor, not a regulator.**

## Prior art / novelty (for the specialist gate, R23-1)
- The conductor-15 curve identification is **PRIOR ART**: Borot–Eynard
  (arXiv:1205.2261, *Quantum Topology* 2015, §6.1.5, verbatim "15A8
  … figure-eight knot", Δ = −15, non-CM); Şengün (arXiv:1401.7484).
  Independently re-derived here (A(M,L) → 15a8, isomorphic not just
  isogenous).
- **NOVEL (program framing, NEEDS-SPECIALIST):** the being×hearing = 3×5
  bifocal reading of conductor 15; the K₃(being)/K₂(meeting) split on one
  isogeny class; the ℤ/2 genus residue as the meeting invariant. The
  phrase "conductor 3·5 / level 3·5" appears NOWHERE in the literature.
- **Physics side: EMPTY** (searched). The figure-eight is the canonical
  3d-3d example (T[4₁]), but its arithmetic is the **"3" side only**
  (trace field ℚ(√−3), the unique arithmetic knot); conductor-15 /
  level-15 appears in NO physics paper; 15a is non-CM, so not an attractor
  point. No hidden physical bridge — confirmed by search, not assumed.

## The one line
The two hands meet at level 15 — but the meeting is a **product, not a
fusion**: the L-function factors (Flath), the being hand keeps its own
K₃ regulator, and all the meeting leaves behind is a single ℤ/2, the
genus-theory residue of "both primes present."

## Firewall
Gate 5 stands. Every quantity here is arithmetic. The dimensionful no-go
(LAW_MAP §E) guarantees even this ℤ/2 is dimensionless algebraic data,
never a physical value. Leg B (the interface speculation) is firewalled
separately and reads this result, does not claim beyond it.
