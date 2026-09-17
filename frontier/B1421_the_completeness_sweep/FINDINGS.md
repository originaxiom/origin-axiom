# B1421 — THE COMPLETENESS SWEEP: the paper's headline input count was a lower bound, four ledger rows contradicted the paper, one refuted claim sat in the freedom ledger, and the record held six results the paper did not state

cc, 2026-09-17. **Owner-directed:** *"make sure sure sure, and verify verify verify, that the paper properly reflects the
most recent and complete state of the program and no important result, law, theorem or realization/understanding is
lost… the mass harvest worries me that the work got buried."* Eight readers over disjoint source sets, every finding
re-verified on this bench before adoption. **Verdict: PROVED (the audit), with the repairs landed.**

## 0. The scale, measured rather than asserted
`verification/orphan_map_summary.txt`: of 1 247 arcs carrying a verdict, 1 144 have a strong one (PROVED / THEOREM /
NEGATIVE / RESOLVED / VERIFIED). **524 are cited on none of the live surfaces** — the paper, its provenance list,
THEOREM_LEDGER, OPEN_LEADS, MAIN_GOAL, THE_END_TO_END_CHAIN, TOE_REQUIREMENTS_LEDGER. All 524 **are** in the generated
verdict views, so the failure is propagation, not loss. Only 15 are from B1300+, so the recent mass harvests are not
where the burial is concentrated; the harvest arcs' *second and third* results are — the item each arc is named for
reached the paper in every case.

## 1. THE INPUT COUNT — the paper's headline was a lower bound (`verification/identification_recount.py`)
The paper leads with **four undischarged inputs**. The record keeps a second, governed ledger — every claim of the form
"X here IS Y there" — whose own rule says *"the input ledger's parameter count is a **lower bound** until every row here
is EARNED or priced."* Recomputing B1266's union-find on today's rows (its two traps kept: an EARNED row is not a debt;
a 2-cycle is one source): **30 rows, 8 EARNED, 8 REFUTED, 14 UNEARNED → 8 irreducible sources → 4 + 8 = 12 irreducible
free inputs.** Control: restricted to B1266's ten rows the method reproduces its published partition exactly (7 sources).
B1266 measured 11 on 2026-09-06; four rows have landed since. **Cross-check:** the outside bench's own
`THE_PRICE_IS_TWELVE.md` recomputes the same 12 independently. The paper now states four for the mathematical chain and
twelve for a physical reading, and says where the other eight would enter.

## 2. A REFUTED CLAIM WAS LOAD-BEARING IN THE FREEDOM LEDGER
The paper booked the chirality bit as *"relational and selection-free"* on a heterogeneous-pair argument: the mirror is
realisable over GL(2,ℤ) only with determinant −1, and the resulting class is *"mirror-odd… invisible to the traces."*
**B1192's own addendum (B1248) refutes exactly this**: the class is 2 − κ modulo squares with κ the Fricke commutator
trace, a function of three mirror-invariant traces, so it is **mirror-EVEN** — *"the arc's description of ε as
mirror-odd — do not survive"* — and being constant across branches it **cannot be the orientation bit**. The paper also
called it "invisible to the traces" two sentences before naming the trace invariant that computes it. Repaired: the row
is re-grounded on B1324's theorem (*on every knot complement, mirror = swap × arrow*), which the paper already carries
and which supports the same conclusion — the hand is not a third input once the swap and the arrow are fixed — and the
refuted reading is stated as refuted, with what survives (a relational ℤ/2 datum; the object supplies its own partner;
the class trivialises over the partner's eigenvalue field for every pair, so only *which* field is the object's).

## 3. CHAIN ROWS THAT CONTRADICTED THE PAPER OR THEMSELVES
- **C53** asserted *"the price of a third record is the atom"* while the paper (corrected in S10b) says the fork is
  fragile past depth three: m412 keeps ℚ(√−3), is chiral, and lacks only the 2T door. The arc's own verdict line feeds
  the generated views, so the refuted sentence was regenerating on every run. Corrected in the row, in the arc verdict,
  and by addendum.
- **C9** printed *"geometric index 12 at level 8"* into the paper's table while the prose (S12) says the level is (4).
- **C35** printed *"flavour triplets"* into the table while the prose says that name was tested and refuted.
- **C42** printed the 3/8 identity with no genericity fence while the prose states it discriminates nothing.
- **C50** claimed the cyclic tower vector-like with no geometric-holonomy fence, and B1418 fires on t12839 — the C₄
  cover itself — on reducible non-split modules. **C43** still carried the withdrawn "16σ" framing. **C52's** label
  asserts universally what the paper states as a supported conjecture. All fenced in place.

## 4. SIX RESULTS THE RECORD HELD AND THE PAPER DID NOT STATE (each verified here, each now in the paper)
1. **Menal-Ferrer–Porti's hypothesis is wider than we used.** Checked against the source, not the record's quote of it:
   Theorem 0.1 asks only that M be complete, non-elementary and **topologically finite** — no one-cusp condition (the
   single-cusp hypothesis belongs to its Theorem 0.2, a different statement). So the 54 multi-cusped chiral covers'
   zeros are **forced by the theorem**, where the paper had booked them three times as *"reported rather than
   reproducible"*. The residual debt is E80 reproducibility, not mathematics.
2. **The surviving gauge group (B1336).** Every centraliser available to a holonomy containing 2T in the principal sl₂
   is abelian of dimension ≤ 4; the Standard-Model algebra is non-abelian of dimension 12. **No flat connection of this
   kind leaves it unbroken, whatever the holonomy.** The arc's own script could not run as committed (`pathlib` used and
   never imported); fixed, run, and locked here.
3. **The rank obstruction (B1265).** The branch carrying Lorentz signature and compact colour has maximal compact f₄ of
   rank four, and no torus element of e₆ reaches it — crossing needs an outer automorphism. That is *why* the four
   interactions do not meet inside this algebra, and the one candidate crosser (θ) is fenced twice.
4. **The reproducing arithmetic (B1117/B1120/B1124).** Vol(m004) = 9√3·ζ_K(2)/π² to 32 decimals by two independent
   routes, and the reality-parity law of the quantum invariant's expansion confirmed at five consecutive orders —
   detection, not derivation, and it is what makes the disjointness result informative rather than trivial.
5. **The family index is impossible on the object (B307 + B1161).** Three interchangeable generations need a cyclic
   cubic trace field; **no hyperbolic knot has one** (cyclic cubic ⇒ totally real; a hyperbolic invariant trace field
   has a complex place — the two classes are disjoint). The object's quadratic field permits multiplicities 1 and 2,
   never 3.
6. **The unique trilinear (B1148) and the E₈ family mechanism (B1275).** The coupling on the constructed carrier is
   unique by direct nullspace (6615 → 4 → 1, no shape assumed), so the Yukawa *shape* is forced where its values are
   not; and the three-family mechanism is verified from E₈'s own definition, where **nothing mentions the manifold** —
   the object-specific step is unchecked, and the record holds three distinct order-three structures whose
   identification is open.

## 5. PLACES WHERE THE PAPER UNDERSTATED ITSELF OR WENT STALE
- **Seven crossings, not three.** The record documents seven sealed value crossings; the paper described three, dropping
  four of its own negatives.
- **The census drift.** The paper quoted 36.25 % → 33.92 % over the first 5 000; sampled in blocks of 800 at depths 0,
  20 000 and 80 000 the rate falls 34.25 % → 29.38 % → 21.12 %, entirely in the two-generator stratum
  (34.23 % → 15.36 %), with the flat three-generator stratum propping the aggregate up. The larger number cuts against
  us and is now stated.
- **The strongest coincidence was not the one volunteered.** The paper volunteered a five-significant-figure determinant
  near-miss; the record's strongest SM-adjacent coincidence is the Koide angle at **0.89σ from 2/9**. Now volunteered
  first, with its three structural dismissals.
- **A status clause outlived its lane.** The ℙ(B₀) row said its closing datum was *"a computation in progress
  elsewhere"*; the lane holding it was tag-archived and deleted on 2026-09-15 without delivering. Now stated as unowned.
- **An absence claim with a counterexample in the record.** The paper said no compact G₂ object realising the design
  exists in the record; the record holds a compact flat G₂ **orbifold** built from the object's own data whose b₂ = 0
  fails the paper's own b₂ ≥ 2 condition two sentences earlier. Now reported as the counterexample it is.

## 6. ONE GATE REPORTING GREEN OVER THE LARGER HALF OF ITS DEBT
`docs/HARVEST_LEDGER.md` carries 283 SCHEDULED rows; `scripts/checks/harvest_debt.py` reports 3, because it walks only
the live seats and SKIPs the retired or merged ones (codex, cc3, cloud, braver, qor5up). Roughly 196 SCHEDULED rows can
no longer trip it. Registered as a lead rather than repaired here: the fix is a ledger-side count that does not depend
on a live remote.

## Locks
`tests/test_b1421_completeness_sweep.py` (the recount, its B1266 control, the orphan-map summary, and that the paper
states the twelve) and `tests/test_b1336_surviving_gauge_group.py` (the centraliser computation, with a positive
control that the criterion can return something non-zero).
