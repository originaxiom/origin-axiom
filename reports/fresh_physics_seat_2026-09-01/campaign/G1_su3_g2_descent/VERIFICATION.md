# VERIFICATION — G1 (G1_su3_g2_descent)

**Verifier seat:** adversarial verification, 2026-09-01.
**Claimed:** NON-SM-ENDPOINT (and step 1 IS registerable — NOT-REGISTERABLE-AT-STEP-1 false).

## Verdict: **CONFIRMED**

Every load-bearing claim was re-derived with an independently written implementation (own rep
data from closed-form Casimir/index/anomaly formulas, own enumeration, own descent engine —
not a re-run of the cell's code), and every one reproduced. The cell's code was also re-run:
all live assertions pass and the regenerated `results.json`/`branching_data.json` are
byte-identical to the committed files (deterministic).

## What was attacked and the outcomes

**(1) Re-run.** `python3 su3_g2_descent.py` completes with all assertions live: 44/44
branching-rule checks, 7/7 criterion controls + engine control, branching filter chain 4→4→2,
6 chains, verdict NON-SM-ENDPOINT. Outputs byte-identical to the committed artifacts
(`git status` clean after the run). PASS.

**(2) The 27's branching, independently re-derived.** A from-scratch enumeration (A2 data from
the Weyl dimension formula, C2 = (p²+q²+pq+3p+3q)/3, T = dim·C2/8, A = dim(p−q)(p+2q+3)(2p+q+3)/60;
G2 list 1/7/14/27 — complete for dim ≤ 27; both lists exhaustive at the cap) reproduces the
filter chain exactly: **4 solutions** under {Σdim = 27, ΣT_su(3) = 6 = 2·T_E6(27),
ΣT_g2 = 3 = 1·T_E6(27)} — precisely the four conjugation variants {3/3̄ ⊗ 7} + {6/6̄ ⊗ 1};
all 4 survive h ≡ 2/3 (mod 1); the su(3)-anomaly filter leaves exactly the **conjugate pair**,
so 27 = (3,7) ⊕ (6̄,1) unique up to overall conjugation. Hand-checks of the anchors:
h(3 of su(3)₂) = 4/15, h(7 of g₂₁) = 2/5, sum 2/3 ✓; h(6̄ of su(3)₂) = 2/3 ✓ (these are the
standard su(3)₂/g₂₁ primary weights); c = 16/5 + 14/5 = 6 = 78/13 = c(E6₁) ✓;
T-sums (1/2)·7 + 5/2 = 6 and 1·3 + 0 = 3 ✓. The anomaly argument is sound: E6's invariant
degrees are 2,5,6,8,9,12 — no cubic Casimir — so the cubic anomaly of any embedded su(3)
vanishes on any restricted E6-rep; the crossed pairings carry A = ±(7·1 + 7) = ±14 and die.
A(6) = 7 confirmed from the closed form. PASS — the row is genuinely derived, not cited;
the h- and anomaly-filters are correct additions (note the h-filter is non-discriminating
here, 4→4, honestly reported as such in the filter table).

**(3) The chirality claim, scrutinized hard as instructed.** g₂'s irreps are indeed all
self-dual (−1 ∈ W(G2)), as are su(2)'s; the code encodes this correctly (`rconj` identity on
A1/G2/C4). Chirality therefore rests entirely on the su(3) factor, and it is real:
{(3,7), (6̄,1)} vs conjugate {(3̄,7), (6,1)} are distinct multisets — the 3 (×7 states) and 6̄
have no partners. Consistent with the 27 itself being complex. Step 1 registerable = True is
correct; the "g₂ forces self-conjugate" shortcut is genuinely false. Verified independently
at every tree node as well (my engine recomputes every option's verdict; all match, including
the deaths: both su(3)-breakings at step 2, both diagonals at su(3)+su(3)′ — the exact pairing
{6,3̄,8,1,3,6̄} under both twisted and untwisted diagonals checked by hand — and the terminal
node's three deaths). PASS.

**(4) The descent tree, independently rebuilt.** My own engine (own branching tables:
g₂ ⊃ su(3): 7 = 3+3̄+1; g₂ ⊃ su(2)×su(2): 7 = (2,2)+(1,3); g₂ ⊃ su(2)₂₈: 7 = 7;
su(3) ⊃ su(2)+u(1), so(3); diagonals with Z2 twist for A2 pairs; each hand-verified against
dim + per-factor index sums) yields **exactly 6 chains, all terminating at su(3) with
{3:7, 6̄:1}**, with identical chain structure to `results.json`. The SM-algebra intermediate
node {(3,2):2, (3,1):3, (6̄,1):1} has exactly one registerable option — su(2)→u(1) — so it is
NOT terminal there, confirming the (algebra, content)-pair sharpening. Menu completeness:
per-factor maximal lists for su(3)/g₂/su(2) are the classical exhaustive rank ≤ 2 lists
(g₂: A2, A1+A1, A1 index 28 — complete per Dynkin), product-node menus per Dynkin's
factor-wise + diagonal classification; honestly flagged as classical imports in §5. PASS.

**(5) The two controls + the banked rows (MB12).** Independently recomputed: SO(10)×U(1)
{16,10,1} chiral ✓; Sp(8) 27 self-dual not-chiral ✓; SU(5)→SU(4)×U(1) content {6, 4:2, 4̄:2}
self-conjugate, not chiral ✓; SU(5)→SM chiral ✓; B863 (a) {3:2, 3̄:2, 1:3} vector-like ✓;
B863 (b′) principal branching all-real ✓; banked SM generation chiral and TERMINAL under the
same engine (B863 reproduced) ✓. The criterion fails and passes both ways on banked rows —
bite demonstrated. The stated conventions (C1 full-27, C2 dial-stripped complex non-abelian
multiset) match the pin: B863 row (a) is NO only under charge-stripping, exactly as argued. PASS.

**(6) No silent import of B873's conclusions.** Checked line-by-line: the branching enters the
descent as `cont0` only downstream of the in-cell enumeration, whose uniqueness assert would
hard-fail if the derivation disagreed (fail-safe, not import); step-1 registerability and the
whole tree are computed, never quoted. B873 (`frontier/B873_p5_gate/FINDINGS.md`) contains no
descent below su(3)+g₂ — "registerable but dim 22 < 46: cannot win" is its full statement —
so this cell's tree is indeed new to the corpus. The **one genuine import** is disclosed: the
step-1 registerable menu {SO(10)×U(1) 46, SU(6)×SU(2) 38, SU(3)³ 24, su(3)+g₂ 22} used for
the min-dim consequence comes from B873's completed menus (labeled as such in the code and
FINDINGS §4). That import is banked and was itself verified by the T8b verification; dims
re-checked here (45+1, 35+3, 3·8, 8+14 ✓, 22 minimal). Acceptable and disclosed. PASS.

**(7) Consequences for T8b.** Cross-checked against `campaign/T8_terminality_draft/VERIFICATION.md`
Finding 1: this cell is exactly its repair option (ii) ("compute su(3)⊕g₂'s descent"), and the
computed outcome refutes the wide part-(ii) quantifier precisely as claimed — min-dim on the
specials-inclusive menu takes E6 → su(3)+g₂ → su(3)+su(2)₂₈ [dim 11 minimal of {16,14,11}] →
su(3), never the SM. The claims about B994 (six chains over B861's special-free menus) and
B863 (rows (a),(b′), terminality) match the banked FINDINGS verbatim. The robustness claim in
§5 checks: the two genuinely conformal step-2 options (c = 1 + 9/5 = 14/5 and c = 84/30 = 14/5,
both re-verified) are both in the tree and both funnel to su(3). PASS.

**(8) Gate 5.** Every numeral in FINDINGS.md and the code is a dimension, rank, index, central
charge, conformal weight, anomaly coefficient, or multiset count. No measured value. PASS.

## Minor notes (no verdict weight)

- **N1.** The code comment C3 lists "su(3)_k > so(3) principal" among "genuine conformal cases
  at these levels"; that embedding is conformal only at k = 1 (B863's b′, c = 2), not at the
  k = 2 realized on this branch (c(su(2)₈) = 12/5 ≠ 16/5). Cosmetic — the option is in the
  structural menu regardless and dies on registerability; FINDINGS §5 states the conformal
  step-2 pair correctly.
- **N2.** The h-filter uses h mod 1 (correct for character decomposition) and happens to cut
  nothing (4→4); the anomaly filter does the real work. The FINDINGS table reports this
  honestly; just noting the filter is decorative here.
- **N3.** `branching_data.json` says "all_verified_by: dimension sum + per-factor Dynkin-index
  sum"; index arithmetic alone does not in general pin a branching uniquely — but every rule
  used is the classical known branching (each re-verified here by hand), and §5 flags the
  classical-import status, so nothing is overclaimed.

## Bottom line

The computation is correct, deterministic, self-contained where it claims to be, and honestly
fenced where it imports. Step 1 is registerable (B873 confirmed); all six chains terminate at
su(3) with {3:7, 6̄:1}; the endpoint is not the SM; the SM algebra occurs mid-chain with
non-banked content and is not terminal there; the T8b wide-quantifier refutation and the
necessity of the scope correction follow. **CONFIRMED.**
