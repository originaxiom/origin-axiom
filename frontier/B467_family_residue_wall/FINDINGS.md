# B467 — the owner's three thoughts, computed: family / residue / wall

**Status: banked (frontier). Firewalled. Prereg: `PREREGISTRATION.md` (committed before
computation). All three cells run. Verdicts: F1 = earned, quantified negative; F2 = the
one uncancelable bit exists and is the ORIENTATION character (derivable, and it is the
Gieseking/B466 bit again); F3 = Chat-1's two-parents-one-child premise VERIFIED with a
twist — the merge is orientation-REVERSING, so the wall merges everything EXCEPT the
orientation bit. The three thoughts converge on the same ℤ/2. No H1.**

## Corrections to the incoming factual layer (registered in prereg, confirmed)

- The metallic family are punctured-torus BUNDLES: m=2 = m136 (silver), NOT 5₂ — 5₂ is
  not fibered (banked B449) and cannot be in the family. 5₂ enters the story only as a
  parent through the wall (F3), which is where it genuinely belongs.
- "disc 5, 8, 13 ≈ Fibonacci" dies at m=4 (20 ≠ 21) — small-number coincidence.
- Chat-1's decimals corrected: α₁/α₂ = 0.670212 (not 0.6686), α₂/α₃ = 0.730965 (not 0.7346).

## F1 — the family-ratio scan vs CKM: an EARNED negative (`f1_ckm.py`)

886 prereg'd expressions (fixed function class, one composition level) against the four
CKM targets at rel-tol 1e-3: **ZERO hits on every target**, with the null model expecting
~0.35 (Cabibbo) — no anomaly in either direction. The metallic eigenvalue ratios do not
encode CKM parameters at this complexity budget; the negative is earned, not assumed
(dual-protocol rule 7 satisfied). B428's killed trap ("3 = generations") stays killed.

**H112 fold-in (the family table)**: tr(A_m A_n) = (mn+1)² + m² + n² + 1 — HOLDS for all
1 ≤ m ≤ n ≤ 6 (elementary Fricke algebra, derivable). The naive reading of H112
("trace = the pair-seam conductor") is **REFUTED at (1,3)**: tr = 27 while
cond(ℚ(√5)·ℚ(√13)) = 65. The (1,2) coincidence tr(A₁A₂) = 15 = the seam level does not
generalize as stated; H112 is updated in the ledger with the table (the surviving
question: why 15 twice at (1,2) — now bounded to a single-pair phenomenon).

## F2 — the smallest uncancelable residue (`f2_parity.py`, exact)

Exact permutation signs on the phase-space torus (ℤ/15)²:

| action | sign |
|---|---|
| A₁, A₂, A₁A₂, −I (Par), −A₁A₂ | **+1 all** |
| every Galois scaling x ↦ cx | **+1 all** |
| **σ = [[1,1],[1,0]] (the Gieseking half-monodromy, det −1)** | **−1** |

The entire orientation-preserving dynamics is even; **the single odd permutation is the
orientation-reversing half-monodromy**. The table is derivable — sign = the Jacobi
character (det|15) throughout — so it LAUNDERS as classical arithmetic; but the owner's
question receives a real answer: the smallest residue that survives every cancellation is
**one bit, and that bit is the orientation character** — the same ℤ/2 as B466's Gieseking
deck action and the banked B289 sign law / B356 chirality window (= ω). "Chirality /
matter-antimatter" as names: HELD per the standing rules. Chat-1's per-point sum over the
240 dual-torus points still awaits their loop construction (recorded).

## F3 — the wall transfer function (`f3_wall.py`; banked anchor CS = ±0.07703818 PASS)

**The gate VERIFIED Chat-1's factual premise** (which I had expected to refute):
4₁(5,1) ≅ 5₂(5,1) — SnapPy isometry certificate, vol = 0.9813688289, H₁ = ℤ/5, identified
as **m003(−2,3)** (a filling of the fig-8's SISTER — three surgery descriptions, one
manifold). And the exact table adds the decisive refinement:

- **The merge is orientation-REVERSING**: CS(4₁(5,1)) = +0.0770382, CS(5₂(5,1)) =
  −0.0770382; the oriented statement is **5₂(5,1) = 4₁(−5,1)** (verified: oriented
  isometry + CS equality to 14 digits). The wall merges two different parents into one
  child **up to orientation — the one bit it refuses to merge is F2's bit.**
- Merge slopes: p = 5 is the certified hyperbolic coincidence; p ∈ {1,2,3} also report
  isometric but both fillings there are exceptional (non-hyperbolic) — flagged UNCERTIFIED
  (SnapPy's isometry test is rigorous only for hyperbolic manifolds); p = 4 exceptional on
  both sides, undecided.
- What the wall transmits vs forgets: H₁ = ℤ/p exactly (the slope, nothing of the parent);
  vol(p) increases monotonically to the parent's (Neumann–Zagier, cited); CS separates the
  parents everywhere EXCEPT the merge point; exceptional-slope CS values are rational
  (Seifert; classical).
- **Lit-gate (blocking, recorded)**: pairs of distinct knots sharing a surgery are a known
  phenomenon class (Brakes/Livingston-type "knots with the same child"); whether
  4₁(5,1) ≅ −5₂(5,1) specifically is in the literature is NEEDS-LIT before any novelty
  word is used. The computation stands regardless.

## The synthesis verdict (the three thoughts, honestly)

The owner's three thoughts converge, verifiably, on a single object: **the ℤ/2
orientation bit** — the residue no cancellation removes (F2), exactly the datum the wall
refuses to merge (F3), carried by the half-monodromy that generates the family's
self-reference (B466). Every mechanism involved is classical/derivable and the physics
names stay HELD — but the convergence itself is real structure: three independent
questions, one bit. What did NOT survive: family ratios as CKM (F1's earned zero), the
naive H112 law (refuted at (1,3)), and 5₂'s family membership (corrected). Nothing to
CLAIMS.md.

## Reproduce
```
python3 f1_ckm.py      # the scan + null + H112 table
python3 f2_parity.py   # exact signs
python3 f3_wall.py     # the transfer table + gate + banked anchor
pytest ../../tests/test_b467.py
```
