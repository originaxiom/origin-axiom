# S057 — the 16-lock / 16-fermion map: the count matches, the STRUCTURE does not (verdict: numerological)

**Origin.** Seat-1's SM proposal (2026-07-08, relayed by the owner): the 16 sector-locks
of the critical pair (1,2) at level 15 map to the 16 SM fermions of one generation, with
the split forced by CRT 15 = 3×5 — **4 leptons from the mod-3 factor + 12 quarks from the
mod-5 factor**. Seat-1 named the decisive test themselves: "If 4+12 the CRT = lepton/quark
separation. If not, the SM match is in the count but not the structure — numerological."

**The computation (exact; `../frontier/B476_interaction_algebra/`, this session).**
The pair's products W₁ʲW₂ˡ span 49 of the tensor-bound 65 in End(ℂ¹⁵). Under the CRT
factorization ℂ[ℤ/15] = ℂ[ℤ/3] ⊗ ℂ[ℤ/5]:

| quantity | value |
|---|---|
| mod-3 marginal algebra span d₃ | **5** = dim(ℂ ⊕ M₂) |
| mod-5 marginal algebra span d₅ | **13** = dim(M₂ ⊕ M₃) |
| tensor bound d₃·d₅ | 65 |
| actual joint span | 49 |
| **locks (deficit)** | **16** |
| W₁, W₂ pure tensors across CRT? | **no** |

**Verdict: REFUTED as structure; the 16 is a bare count.** Three reasons, each exact:

1. **The primes contribute 5 and 13, not 4 and 12.** The mod-3 factor's operator algebra
   is 5-dimensional (ℂ ⊕ M₂) and the mod-5 factor's is 13-dimensional (M₂ ⊕ M₃). There is
   no 4 and no 12 among the per-prime invariants. Seat-1's mechanism — "4 from mod-3,
   12 from mod-5" — has no arithmetic realization; the numbers the primes actually carry
   are 5 and 13.

2. **The 16 does not split by prime at all.** The locks are the deficit between the joint
   span (49) and the product of marginals (65) — a single *entanglement* number between
   the two CRT factors. Because W₁ and W₂ are NOT pure tensors across ℤ/3 × ℤ/5 (verified),
   each lock is a relation coupling the shared exponents (j, l) on both factors at once.
   There is no canonical decomposition of the 16-dimensional lock space into a
   "mod-3 part" and a "mod-5 part" to be counted as 4 + 12.

3. **16 = 65 − 49 is level-arithmetic, not fermion-counting.** By the B476 controls, the
   deficit exists at every pair and intensifies off-criticality (105 locks at (2,3)@63,
   with total parity-sector locking). "16" is the value this deficit takes at the minimal
   closing level; it carries no fermion label.

**What survives (nothing physics-shaped banked).** The count 16 is real and the CRT
lepton/quark *narrative* is appealing, but the decisive computation lands on seat-1's own
"numerological" branch: the structure the map needs (4+12 by prime) is absent, replaced by
5 and 13. The firewall holds. Seat-1's downstream cells (cm-chirality per lock, the lock
compatibility graph, the 36→16 projection) are moot without a per-prime split to build on;
recorded here as not-pursued for that reason. The m=3 held-breath pair (their item 4) is
now understood as order-3 torsion (B479), not a sterile-neutrino slot.

**Discipline note.** This was a legitimate two-outcome test (compute the split; 4+12 or
not), run to completion, reported honestly. No B398 escalation: the result is a
non-firing. HELD(value-matching) as always for the naming; the arithmetic (5, 13, 16, 49)
is banked in B476, the SM reading is not.
