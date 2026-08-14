# B932 — R-EMB decided at the structural level: the conformal chain VERIFIED in-house (W18 upgraded) — and it is GRAMMATICALLY UNREACHABLE by measurement; the cascade IS the GUT chain

**Date:** 2026-08-06 · **Seat:** computation agent (Lane 3 of the crossing-study round) ·
**Status:** DRAFT (banking seat to add locks). Mathematics scope; STRUCTURE ONLY — this cell
cannot produce a measured number, ever (its registration says so; this document keeps it so).
Nothing to `CLAIMS.md`; Gate 5 untouched. **Not preregistered** — this is an adjudication cell
of the B854/B874 class (it verifies an incoming computation and sweeps banked typings by exact
computation); its footing is the 57-check verification battery in `chain_select.py` →
`results.json`, plus the two-outcome criteria and the computed vacuity certificate below.

**Registration:** masterplan R-EMB (dated amendment 2026-08-05); shape M3 of
`frontier/B926_crossing_anatomy/ANATOMY.md` §4; this cell also discharges ANATOMY §5 honest
gap 1 (W18's in-house verification).

---

## LEG 1 — the conformal chain, computed in-house (W18's verification)

**The question:** Chat-1's externally-computed claim (wall W18): the (E6)₁ conformal-embedding
chain decomposes the 27 as (3,2,2)+(3,3,1)+(6,1,1) — no color singlets, no leptons.

**The embedding, documented and built exactly over ℚ** (split forms; branching is a
complex-representation fact, independent of real form — conventions block at the head of
`chain_select.py`):

- **O** = split octonions as Zorn vector matrices over ℚ (composition, alternativity,
  conjugation verified exactly at runtime);
- **g₂ = Der(O)** — computed as an exact nullspace: dim 14, bracket-closed, kills the unit,
  commutes with conjugation;
- **the 27 = J₃(O)** (octonionic Hermitian 3×3) with the Freudenthal cubic N via Jordan traces,
  N = (t₁³ − 3t₁t₂ + 2t₃)/6, and its full polarization θ (θ(x,x,x) = 6N(x));
- **sl(3)** acting by ρ(A): X ↦ AX + XAᵀ (verified a Lie homomorphism), **g₂** entrywise;
  the two actions commute exactly (8×14 pairs);
- **the ambient e₆**: all 22 generators annihilate θ exactly, so they lie in Lie(Inv(N));
  that algebra's dimension is pinned **exactly**: dim = 78 by a two-sided sandwich —
  lower bound 78 from 373 exhibited exactly-θ-invariant elements (the 22, the 26 traceless
  Jordan multiplications L_a — each verified invariant — and their inner-derivation brackets)
  with mod-p rank 78 at two primes (rank_p ≤ rank_ℚ, the valid direction); upper bound 78
  from the exact integer constraint system's rank 651 at two primes (dim_ℚ ≤ dim_p, the valid
  direction). Identification of Lie(Inv(N)) with (split) e₆ is Chevalley–Schafer (cited;
  corroborated by B854's independent exact Chevalley e₆: dim 78, exponents {1,4,5,7,8,11});
- **su(2)×su(2) ⊂ g₂** as the stabilizer of the split quaternions H ⊂ O: dim 6, splitting
  over ℚ into two commuting sl₂ ideals (a = faithful on Im H, b = kernel on Im H), exact
  sl2-triples found in both.

**The branching, decided by exact weight multisets** (characters determine the class —
complete reducibility):

> **27 = (3̄, 2, 2) ⊕ (3̄, 3, 1) ⊕ (6, 1, 1)** under su(3) × su(2)_a × su(2)_b,
> with the (3,1)-piece the triplet of the INDEX-3 su(2). Exact multiset equality; and
> **the number of su(3)-singlet states in the 27 is ZERO** (stronger than "no singlet
> constituents": not one state of the 27 is color-neutral under this chain's su(3)).

**The chain is the conformal one, certified exactly:**

- embedding indices by the Killing form of the constructed 78-dim algebra:
  κ(h₁,h₁) = 96, κ(h_a,h_a) = 144, κ(h_b,h_b) = 48; with 4h∨(E6) = 48
  (h∨ = 12 = 1 + max B854 exponent, simply-laced) ⟹ **j = (2, 3, 1)** ⟹ levels
  **(A2)₂ × (A1)₃ × (A1)₁** inside (E6)₁ — cross-checked by 27-traces
  (Tr h² = 24, 36, 12 = 4jT_{E6}(27)/… consistent with T_{E6}(27) = 3);
- central charges, exact rationals: c(A2,2)+c(G2,1) = 16/5 + 14/5 = 6 = c(E6,1) and
  c(A1,3)+c(A1,1) = 9/5 + 1 = 14/5 = c(G2,1) — both steps conformal.

**Verdict on W18:** Chat-1's computation **CONFIRMS in-house**. The conformal chain's 27 has
no color singlets — **no leptons**. W18 upgrades from "externally computed, registered
negative" to **in-house verified** (ANATOMY §5 gap 1 discharged).

**One wrinkle, recorded honestly:** the triplets and the sextet come **oppositely**
conjugated — the invariant fact (stable under relabeling by the su(3) outer automorphism) is
{3̄, 3̄, 6} in one fundamental and {3, 3, 6̄} in the other. The registered same-handed label
"(3,2,2)+(3,3,1)+(6,1,1)" carries a bar slip on one piece. Immaterial to every verdict here
(singlet count, su(2) content, indices, conformality are conjugation-blind); noted so the
registration can be tightened.

---

## LEG 2 — the selection question, formalized and decided

**The two-outcome statement (vacuity-checked before the sweep):** does any banked structure
realize the conformal chain's subalgebra su(3)⊕su(2)⊕su(2) — invariants
(dim, derived, center) = (14, 14, 0), rank 4, factor indices (2,3,1) — as a
centralizer/wall of the build?

- **Outcome B was statable** (the cell is not vacuous): the Levi type A2+A1+A1 EXISTS in e₆ —
  the subdiagram enumeration finds 5 realizations (e.g. nodes {1,2,3,5}, A2 on edge (1,3)),
  so a wall of semisimple type A2+A1+A1 (⊕ u(1)²) is abstractly available in e₆'s Levi
  lattice, reachable in principle by a single charge. Whether the object's charges ever land
  there is a fact about the OBJECT, not about e₆.

**The sweep — the banked wall lattice, typed** (each row re-confirmed from the arcs' own
results files at run time where banked JSON exists):

| wall | arc | dim | derived | center | semisimple type |
|---|---|---|---|---|---|
| C = Cent(2T) (charge torus) | B854 | 4 | 0 | 4 | — (u(1)⁴) |
| FMT K-walls (three lines) | B866/B877/B874 | 46 | 45 | 1 | D5 = so(10) |
| core / soft plane / compact wall (CMT) | B874/B875/B877/B892/B909 | 30 | 28 | 2 | D4 = so(8) |
| cross-shadow | B909 (solo §XXI) | 18 | 15 | 3 | A3 = su(4) — **forced**: dim-15 semisimple of rank ≤ 3 is A3 uniquely (enumeration in-script) |
| SMT wall z(x₁,y*) | B892 | 14 | 11 | 3 | A2+A1 (su(3)⊕su(2)) |
| Cent(C) (the floor) | B874 | 12 | 8 | 4 | A2 (su(2,1) real form) |
| G20 (generated, NOT a centralizer) | B892/B897 | 20 | 19 | 1 | A2+A2+A1 |

**No row matches (derived, center) = (14, 0).** The unique dim-14 wall — the SMT wall — is
su(3)⊕su(2)⊕u(1)³: derived 11 ≠ 14, center 3 ≠ 0. The near-miss is exact and instructive:
the banked cascade carries the A2+A1 core and **trades the conformal chain's second su(2)
for the u(1)³ that measurement mandates**.

**Two theorem-shaped obstructions make the outcome permanent, not accidental:**

- **T1 (center).** For any nonempty set S of commuting semisimple charges, S ⊆ center(z(S)),
  so every charge wall has center ≥ 1. The conformal subalgebra has center 0. It can never
  be a charge centralizer AS IS. (Every banked charge wall indeed shows center ≥ 1 — in fact
  center grows monotonically 1→2→3→4 down the cascade.)
- **T2 (regularity — the sharp one).** The centralizer of a set of commuting semisimple
  elements is a full-rank REGULAR (Levi-type) subalgebra ({α : α|_S = 0} is a rationally
  closed subsystem, W-conjugate to a standard parabolic subsystem — Bourbaki), and in
  simply-laced e₆ every simple factor of a Levi is generated by e₆-roots, hence has Dynkin
  index 1. The conformal chain's factors are computed at indices **(2, 3, 1)**: its su(3)
  (index 2) and its index-3 su(2) are **S-subalgebra factors, not E6-conjugate to any Levi
  factor** — so no centralizer of ANY charge system in e₆, banked or future, can carry the
  conformal chain's own su(3) or heavy su(2) as a wall factor. (The index-1 su(2) — the
  self-dual boson B854 §6 flagged — is the one regular piece.) The conformal chain and the
  GUT chain do not even share a color su(3) up to E6-conjugacy: index 2 vs index 1.

**And the positive half:** the banked measurement cascade **IS the GUT-side chain** —
FMT: 46 = so(10)⊕u(1) (B866/B877) → SMT: 14 = su(3)⊕su(2)⊕u(1)³ (B892), with SU(5)
provably skipped (no 26-stratum, B874). Matter agrees: the object's all-perspectives tiling
of the 27 carries **9 color-singlet states** (the (1_c,3_f) lepton-pattern block, B897 —
count-consistent with 16+10+1's 9 color singlets) versus the conformal chain's **0**.
The discriminating integers are 9 vs 0, both exact, both in-house.

> **VERDICT (outcome A): no banked structure realizes the conformal chain's subalgebra as a
> centralizer/wall — and none ever can (T1+T2). The object's measurement grammar produces
> regular (Levi) walls only; the conformal chain runs through an S-subalgebra. The object
> selects the GUT chain at the structural level — not by preference among two options, but
> because the conformal chain is grammatically unreachable by measurement.**

Theorem-shape, with hypotheses stated: *for the object's charge system (elements of the
banked torus C and its algebraic wall points — toral, per B854's typing with nondegenerate
restricted Killing form), every measurement wall is a full-rank Levi subalgebra of e₆ with
center ≥ 1 and index-1 simple factors; the conformal chain's subalgebra has center 0 and
factor indices (2,3,1); therefore no measurement realizes it, while the banked cascade
realizes the GUT chain exactly (46 → 14, SU(5) skipped).*

**What this does NOT do:** it does not adjudicate the conformal embedding as 2d-CFT
mathematics (that chain is correct AS a conformal embedding — leg 1 verifies it); it does not
produce or license any value, scale, or coupling (the M3 registration's fence: this shape
"fixes which matter-typing any future shape is allowed to consume", nothing more); it does
not claim the GUT chain reaches M_Z (W19/W20 stand untouched).

---

## Honest gaps

1. **Type identification cited:** Lie(Inv(N)) ≅ e₆ is Chevalley–Schafer (classical); what is
   proven in-house is dim = 78 exactly (two-sided sandwich, both mod-p directions valid) with
   the 22-dim sl3⊕g₂ inside, corroborated by B854's independent exact e₆. Similarly cited:
   h∨(E6) = 12 via B854's banked exponents + the simply-laced h = 1 + max-exponent relation;
   h∨(A2) = 3, h∨(G2) = 4, h∨(A1) = 2; "conformal embedding ⟺ equal central charge"
   (standard); the Bourbaki parabolic-subsystem fact behind T2 (the rational-closure step is
   the one-liner {α : α(x) = 0} = R ∩ x^⊥).
2. **Uniqueness of the A2×G2 class:** the conformal chain is pinned by its computed indices
   (2,1) and exact c-sums; uniqueness of the maximal S-subalgebra A2×G2 up to conjugacy
   (Dynkin) is cited, not recomputed.
3. **Sweep completeness = the banked record as of 2026-08-06.** The within-C stratification
   {78, 46, 30, 18, 14, 12} is banked as "includes" (B892); T1/T2 are what make the negative
   future-proof independent of lattice completeness. ANATOMY §5.3's off-register caveat
   (B801) is inherited.
4. **The toral hypothesis** on the charges (semisimplicity of C's elements and of y*) is the
   banked typing (B854 u(1)⁴, nondegenerate restricted Killing; B892's y* algebraic on the
   torus), stated as hypothesis of the theorem-shape, not re-derived here.
5. **Not preregistered** (adjudication-cell class, B854/B874 precedent); the two-outcome
   criteria and the vacuity certificate are in-script and computed, and the cell could have
   returned outcome B (the Levi homonym exists — 5 subdiagrams).
6. **Locks pending banking** (tests/test_b932_* to be added by the banking seat); LAW_MAP
   row for the T2 regularity lemma to be considered at banking (WORKING_RULES rule 10's
   sub-lemma clause).

## Files

`chain_select.py` (all conventions declared at head) → `results.json` (57/57 checks PASS).

## Depends on / feeds

Depends: B854 (exact e₆, exponents, C = u(1)⁴), B866/B877 (FMT, 46 = so(10)⊕u(1)),
B874 (census, Cent(C), no-26), B892 (SMT 14, within-C strata), B897 (G20 tiling, the 9),
B909 (CMT 30, cross-shadow 18), B925 (D-chain su(4)/so(8) context), B926 (ANATOMY M3/W18).
Feeds: the masterplan's R-EMB row (chain selected: GUT-side, structurally); W18's status
(in-house verified); the crossing study's surviving-shapes menu (M3 closed as outcome A).
