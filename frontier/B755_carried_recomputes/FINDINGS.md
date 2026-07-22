# FINDINGS — B755: the five carried recomputes — 5/5 LOCATED-BY-RECOMPUTE

cc banking seat, 2026-07-22. The R27-carried block: the five banked negatives whose
discriminating facts the fact_computed sweep graded NOT-LOCATED (sealed input:
frontier/B738_pathfinder_compiler/FACT_COMPUTED_SWEEP.md). Prereg 5627dd19 sealed before
any cell ran. E19 both directions throughout. Gate 5: B332's cell touches SM ratios only
as a null-test adjudication (B655/B751 precedent). Nothing to CLAIMS.

## Cell 1 — B140: the genus-2 mirror CS-flip witness — WITNESSED

The missing module at bank time (twister) is present in the current env. The bundle
S_2,1 / monodromy word `abcDef` (twister curve alphabet a..f) is hyperbolic
(vol 5.4611931991…, positively oriented) and CHIRAL, certified two independent ways per
the E25-era rule: (1) the CS obstruction — 2·CS = +0.01192 is not in (1/2)ℤ, so no
orientation-preserving isometry to the mirror exists; (2) the isometry-orientation route —
every isometry M → M̄ found has an orientation-reversing cusp map. And the discriminating
pattern holds exactly: vol(M̄) = vol(M) (|Δ| < 1e−60 at high precision), CS(M̄) = −CS(M)
(sum exactly 0). The banked citation (the orientation-reversal theorem) now has its first
in-repo genus-2 instance; B140's soft spot is closed. Artifacts: cell1_b140_genus2.py,
cell1_out.txt.

## Cell 2 — B332: the 1/4-numerology null — 1/4 NOT DISTINGUISHED

The ratio set the original kill relied on was chat-cited and not in-repo; per the sweep's
condition it was DECLARED in the sealed prereg (the B752 25-value PDG table restricted to
(0.1, 0.6) — 9 targets). Result: 1/4 hits ZERO targets at both the 2% and 5% windows;
the controls (1/5, 1/e, 1/φ, 1/π) and 40 seeded log-uniform randoms match comparably or
better (P(random ≥ 1/4's count) = 1.00 at both windows). The kill's null basis — "a
single small number's match is not discriminating" — is now computed in-repo, and in this
declared set 1/4 is not even a near-hit. Artifacts: cells245.py, cells245_out.txt.

## Cell 3 — B685: the GSWZ symmetrized-series pure-3 fact — COMPUTED (see verdict below)

The source (arXiv:2412.04241, Garoufalidis–Scholze–Wheeler–Zagier) was re-read directly;
the re-read RESOLVED the banked extraction's internal inconsistency: the paper's eq (2)
coefficients are −1/3³, +1/3³, −4/3⁵, −1/3⁵ — the extraction's inline "⅓ … ⅘ … ⅕" were
superscript-rendering artifacts of 1/3³ and 4/3⁵; the banked pure-3 CONCLUSION was right,
its inline rendering mangled. Then the fact was computed, not cited:

- **Part 1 (conventions + gates).** The asymptotic coefficients of the Kashaev invariant
  ⟨4₁⟩_N = Σ|(q)_k|² were extracted by exact-ladder Richardson (N = 800…16000, 20 points,
  420 dps) and PSLQ-recognized under the E25 coefficient-aware acceptance rule:
  r₁ = 11/24 and r₂ = 697/1152 — the paper's printed eq (1) values, REPRODUCED from the
  sum itself — plus r₃ = 724351/414720, r₄ = 278392949/39813120, r₅ = 244284791741/
  6688604160 (beyond what the paper prints; their denominators carry 5·7·… — the Φ-level
  coefficients are NOT pure-3, sharpening why only the SYMMETRIZED object is).
- **Part 2.** The tempting even-fit shortcut (t(N)² as the symmetrized product) was REFUTED in-session (with h imaginary every aⱼhʲ is real, so t(N)² = Φ(h)² — the
  parity trap, logged); the symmetrized product was instead built EXACTLY from r₁…r₅ and
  its (q−1) expansion reproduces **ALL FOUR of eq (2)'s printed coefficients exactly**
  (−1/27, +1/27, −4/243, −1/243) with **pure-3 denominators through u⁵**. The
  3¹⁴⁶-at-order-100 valuation remains cited beyond u⁵ — stated, not blurred.
- **Consequence.** B685's Habiro leg now rests on an in-repo computation; the VACUOUS lock
  (test_gswz_powers_of_three — factorint(3^e)=={3:e}, could never fail, MB12 signature) is
  REPLACED by real locks in tests/test_b755_carried.py. Artifacts: cell3_b685_gswz.py,
  cell3_out.txt.

## Cell 4 — B720: the computable halves of the threefold NO-MATCH — COMPUTED

(i) ℚ(ζ₃) and ℚ(i) are linearly disjoint (compositum degree 4, exact resultant;
discs −3 vs −4 — different ramification): the "wrong cyclotomic branch" half is exact.
(ii) The Markov quiver's mutation class has size 1 up to relabeling (computed closure)
and its entries are ±2, not ±1 — finite-MUTATION but not an ADE orientation, i.e. not
finite-TYPE: the object-side half of the ABHY mismatch is exact. (iii) The 3d
flat-connection no-local-DOF statement is recorded as a bounded derivation. The two
literature classifications (CM cosmic Galois mixed-Tate over ℤ[i]; ABHY requires
finite-type) remain CITED and are flagged as the irreducible cited residue.

## Cell 5 — S019: formulated, closed by dimension, tombstone repaired

The tombstone's kill citation was BROKEN (archive/PHYSICS_RESONANCES.md has no Fisher
content) — repointed to FAILURE_ATLAS C4 + the E21/V6 proxy with proxy status explicit.
The minimal formulation, posed and closed: any scalar-parameter family has a 1×1 Fisher
form ≥ 0, and a Lorentzian reading needs ≥ 2 dimensions with indefinite signature — the
kill holds BY DIMENSION for any Fisher-on-k formulation; the computed instance
(Fisher = 16/(m²(m²+4)) > 0, E21/V6 machinery) is re-verified exactly. The kill upgrades
from heuristic to trivial theorem.

## Verdict

**5/5 LOCATED-BY-RECOMPUTE** (target met; no cell blocked). Instrument notes, logged:
the twister curve-alphabet probe (the S_2 file needs its rectangle name; S_2,1's alphabet
is a..f+x); the pslq working-precision trap (an exact relation is invisible at full dps
when only k digits are meaningful — tolerance must be trust-scaled); the first draft of
cell 1 used a wrong solution-type filter (fixed in-session). Locks
tests/test_b755_carried.py (5). Consequences: the B685 vacuous-lock replacement; the
S019 tombstone repair (speculations/TOMBSTONES.md); no FINDINGS annotations needed on the
originals — every recompute CONFIRMED its kill's basis (E19: nothing flipped).
