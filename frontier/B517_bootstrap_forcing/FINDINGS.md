# B517 — THE BOOTSTRAP FORCING CAMPAIGN. Phase 0: the intertwining theorem + golden-specificity (verified)
**Computed + verified 2026-07-11 (owner's conditional theorem + A3). Locks `tests/test_b517.py`.
Strong ground for the D1 (golden-3d) reopening: the coupling is CANONICAL and GOLDEN-SPECIFIC.**

## THE INTERTWINING THEOREM (verified, every step)
Two-way coupling M = [[F, C],[D, F]] of two Fibonacci copies (F = [[1,1],[1,0]]), with the coupling
blocks C, D **intertwining the Fibonacci dynamics** (CF=FC, DF=FD):
1. **Commutant:** CF=FC ⟺ C ∈ ℤ[F] = span{I, F} (F has distinct eigenvalues). [verified]
2. **The target forces CD=F³:** for commuting blocks, char(M) = det((F−xI)² − CD); and
   **det((F−xI)² − F³) = x⁴−2x³−5x²−4x−1** exactly — the golden quartic (β=φ(1+√φ)). So the golden-3d
   target ⟺ **CD = F³**. [verified]
3. **Both-nontrivial ⟹ (C,D)=(F,F²) up to exchange:** among nonneg-integer C,D ∈ ℤ[F] with CD=F³ and
   C,D ≠ I, the ONLY solutions are (F,F²) and (F²,F). [verified by exhaustive factorization of
   F³=2F+I in ℤ[F]]
4. **The canonical coupling M = [[F,F],[F²,F]] realizes β=φ(1+√φ)** (char poly = the golden quartic).
   [verified]

**Reading:** the golden-3d bootstrap coupling is NOT arbitrary — within the natural (Fibonacci-
equivariant) class it is UNIQUE and canonical: couple copy-1→copy-2 by F and copy-2→copy-1 by F²
(the object and its square, ratio 1:2).

## A3 — GOLDEN-SPECIFICITY IS STRUCTURAL (verified)
The SAME canonical coupling M = [[S,S],[S²,S]] for each metallic S=[[m,1],[1,0]] is **Pisot ONLY for
golden (m=1)**; silver/bronze/m=4/m=5 all fail (a conjugate exceeds 1: silver 1.337, bronze 2.70, …).
So golden 3d is golden-specific at the STRUCTURAL (canonical-coupling) level, not just via the
recursion (B516). Mechanism: φ is the unique metallic number small enough (the conjugate x(√x−1)<1).

## THE CAMPAIGN (prereg — what each cell takes)
- **Phase 0 (this, DONE):** the intertwining theorem + A3. Banked.
- **Phase A — THE GRAMMAR DERIVATION (the forcing core; owner's active thread):** is the intertwining
  condition itself forced by the repo's monoid/self-reference grammar, or an added categorical choice?
  A1a: formalize "intertwining = F-equivariant coupling" = the natural morphism when F is the structure
  (couple two Fibonacci systems compatibly with evolution). A1b: is F³/(F,F²) grammar-meaningful (the
  cube; the 1:2 asymmetry = object vs its square)? A1c: does End(F₂×F₂) with the diagonal F stabilize
  at exactly 4 strata (the self-reference fixed point)? Takes: exact monoid computation + a categorical
  argument; multi-session.
- **Phase B — β understood:** B1 is √φ already in the program (Fibonacci-anyon quantum dimension / WRT)?
  B2 β's unit structure in ℚ(√5,√φ). B3 plot the 3d Rauzy fractal. Takes: grep + exact + numeric plot.
- **Phase C — the physics edge (firewalled, B398):** does the genuine 3d β-substitution + its
  mapping-torus time carry (3,1)? Takes: the 4d pairing signature, only after A resolves.
- **Phase Z — verdict:** if intertwining is FORCED (A1) ⟹ "3d as two iterations of self-reference,
  golden, canonical" is a real theorem-shaped result → B398 for any physics word. If a choice ⟹ real
  math (canonical within the class) but not forced. Airlocks armed; HELD(value); nothing to CLAIMS.md.

---

## Phase A (2026-07-11): the bootstrap FOLLOWS FROM THE GRAMMAR (owner's question — resolved toward YES)
1. **Intertwining is forced, not chosen (A1a, verified):** the F-equivariant endomorphisms of F₂×F₂
   (commuting with the diagonal evolution F⊕F) = **M₂(ℤ[F]) exactly**. Requiring the coupling to be a
   MORPHISM of Fibonacci-dynamical systems (respect each copy's evolution) FORCES the blocks into ℤ[F]
   = intertwining. Not an added categorical choice — the natural-morphism condition.
2. **THE FORCING (verified, scan-bounded):** among ALL F-equivariant two-way bootstraps [[F,C],[D,F]]
   with C,D ∈ ℤ[F] both nontrivial, the **UNIQUE Pisot (clean-quasicrystal) irreducible quartic is the
   golden one** — (C,D)=(F,F²), β=φ(1+√φ) — confirmed across entries {0,1,2,3}⁴. **No golden target
   assumed: grammar (F-equivariance) + two-way + Pisot ⟹ golden 3d, uniquely.** So the golden-3d
   bootstrap DOES follow from the monoid/self-reference grammar; it is not an added choice.
3. **Path to the closed theorem:** char(M) for CD=eI+fF is the exact 2-parameter family
   P(x;e,f) = (x²+1−e)² + (x²+1−e)(1−2x−f) − (1−2x−f)²; the Pisot region in (e,f) + the nontrivial-
   factorization constraint would upgrade the scan to a theorem (Phase A residual).
4. **A1b (chirality reading):** the (F,F²) coupling is ASYMMETRIC (1:2, one copy sees the other at one
   step, the reverse at two) — the object's chirality (det F=−1) appearing at the bootstrap. [reading]

## B1 — √φ is already in the program (the anyon connection, verified shared field)
β = φ(1+√φ) lives in **ℚ(√5, √φ)**. The **Fibonacci anyon F-matrix** (B484) is
[[1/φ, 1/√φ],[1/√φ, −1/φ]] — entries in the SAME field ℚ(√5, √φ). **√φ is the shared ingredient of the
3d inflation (β) AND the anyonic braiding (the F-matrix).** [MATH: same field; HOOK, firewalled: the
3d spatial structure and the object's Fibonacci-anyon braiding meet at √φ.]

## Status
The D1 reopening is now strongly grounded: golden 3d is REAL (B515), golden-SPECIFIC (A3), and the
bootstrap FOLLOWS FROM THE GRAMMAR (Phase A — unique Pisot F-equivariant coupling, no target assumed).
Remaining: close the forcing theorem (the (e,f) Pisot region); Phase B (β unit structure, Rauzy plot);
Phase C (the 3d object's signature, B398). The "3 spatial dimensions = the unique golden quasicrystal
from self-reference" reading is now theorem-shaped, firewalled; no physical value claimed.
