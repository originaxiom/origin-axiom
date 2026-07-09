# B496 — The Thue–Morse endomorphism probe: PREREGISTRATION
### Committed before the banking-seat computation (owner directive: "TM = Thue–Morse, the other object which by interacting with ours might be the path to physics")

## The frame
Every substitution on {a,b} is an endomorphism of F₂ and induces a polynomial map on the Fricke
character variety X(F₂), coordinates (x,y,z) = (tr A, tr B, tr AB). The program's metallic maps are the
**invertible** part (GL(2,ℤ) abelianization, det ±1 — the existing object). The Thue–Morse substitution
a→ab, b→ba has abelianization [[1,1],[1,1]], **det 0** — the canonical **singular** (non-invertible)
element of End(F₂). This probe computes what the singular part of End(F₂) does to the program's own
stage — the "interaction of the two objects" made concrete on the shared character variety.

## Prereg'd statements (verified by the exploration seat; re-derived independently before banking)
- **T1** — TM trace map: T(x,y,z) = (z, z, xyz − x² − y² + 2). [exact, bankable]
- **T2** — κ law and factorization: κ′ = κ² − (κ−2)z² − 2, and κ′ − 2 = (κ − 2)(x² + y² − xyz).
  Consequences: κ=2 (reducible locus) invariant; the Markov surface κ=−2 → κ′ = 2 + 4z² (foliation
  destroyed except the κ=2 leaf). [exact, bankable]
- **T3** — collapse to the plane x=y after one step; plane map (u,v)→(v, u²(v−2)+2); in w=v−2:
  w′ = u²·w (multiplicative cocycle). [exact, bankable]
- **T4** — exact angle-doubling: F(γ(θ)) = γ(2θ) for γ(θ) = (2cos θ, 2cos 2θ), γ ⊂ κ=2. [exact, bankable]
- **T5** — degree growth [3,5,11,21,43,85] (n≤6), recursion a′=b, b′=2a+b, Perron root 2. [exact data +
  elementary argument; state as "degree growth", NOT "entropy"]
- **T6** — Perron dichotomy: TM eigenvalue 2, Fibonacci φ; the two primordial comparisons carry log 2
  and log φ. [exact]
- **T7** — invariant sweep (negative): no polynomial invariant of the plane map up to total degree 8
  except constants. [exact]
- **E1** — h_top = log 2 on the plane: **CITED-CONDITIONAL** — the lower bound is exact (T4 doubling
  curve); the upper bound needs Gromov / Dinh–Sibony (entropy ≤ log dyn-degree) with a noncompactness
  caveat. **Do NOT bank as proven.**

## Governance
- **Independent re-derivation** of T1–T7 (done: `verify_tm.py`, not a port); F_p guards at two primes.
- **Novelty gate (BLOCKING before any "novel" word):** Axel–Peyrière (1989) TM trace map; Allouche–
  Shallit; Bellissard TM-trace-map literature — check T1's exact form and whether T2 (κ-factorization)
  and T4 (γ-curve) are new. Label KNOWN / PARTIALLY-KNOWN / APPEARS-NOVEL. (The map T1 is likely known;
  the κ-factorization and the exact doubling curve are the candidates for new content.)
- **HELD(value-matching) from birth** on any physics reading; killed-trap flags; firewall (nothing to
  CLAIMS.md; speculation → speculations/, philosophy → one-way cite).

## Committed next questions (preregister, then compute)
- **Q1 — the mixed semigroup.** Words in ⟨T₁ (golden), T_TM⟩ acting on exact ℚ-points of κ=−2: does any
  mixed word return points to a κ level set? Fate of the figure-eight fixed locus under a single TM event
  (attracted to κ=2, escaping, or landing on named loci)?
- **Q2 — the defect dictionary (physics-shaped; firewalled).** In the B221 golden-chain setup, the TCI
  Fibonacci defect line W (W²=1+W, quantum dimension φ) vs T_TM's action on trace coordinates. A clean
  failure is a valid verdict; any rhyme stays in speculations/ pending the emergence bar.

## Bins / expected honest outcome
T1–T7 are exact facts (banked). The interpretation — TM = the singular/cancellation verb, the Markov
foliation destroyed except the reducible leaf, degree growth 2 vs the units' λ_m — is a real structural
result about how the singular monoid acts on the program's stage. Whether the *interaction* (Q1/Q2)
supplies a delta ingredient (scale via log 2 vs log φ; mixed spectral type; multiplicity) is the live
path-to-physics question, gated. Firewalled.
