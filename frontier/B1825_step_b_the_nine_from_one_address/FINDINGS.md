# B1825 — THE NINE FROM ONE ADDRESS (THE FINAL ATTACK, STEP B; P-495; SEALED fa25925fc): NEGATIVE AS SEALED — NO SUPPORT. THE FRAME MAKES OUR MASS RATIOS AND MAKES OUR MIXING, BUT NEVER AT ONE ADDRESS

**Verdict: NEGATIVE as sealed (NO SUPPORT; NOT FOUND within the census's reach and resolution).**
- **The decisive cell S fails.** Our world's ten (the six mass ratios, |V_us|, |V_cb|, |V_ub| and |J|) are not in the
  frame's support at c = 3: the least χ²_ten over the 266 lines, twelve directions, both radii, eight readings and
  continuous τ (Im τ ∈ [1, 4]) is **291.4**, against the sealed threshold 23.21 (χ²₁₀'s 0.99 quantile).
- **The negative is scoped to one rigid address inside the census's reach.** By the card's X1 it excludes nothing
  beyond the reach (lines of order above 12, Im τ above 4, other directions, radii or c) or below its resolution (the
  certification's planted miss rate, 0.21%).
- **The record of the run.**
  - The census's manifest was pushed (ece543c98) before any read; every pre-seal number came from committed
    aggregate-only scripts refused without that push.
  - Sealed fa25925fc after a hostile pre-seal check of the card (no wrong number; its points applied).
  - The run (scripts/stepb/run_stepb.py, m = 53, J = 3.12 × 10⁻⁵) was committed unread at 64a2a3d4e and read once.
  - **Refereed hostile after the run** (an independent referee with its own code, verification/referee/): a brute-force
    scan of all 50 612 352 stored node rows finds the least node χ²_ten 291.81, at the node beside the run's address and
    equal to the run's own node minimum (291.807, K's `num_report.ub`) to 10⁻⁷, and no row below 23.21 (none below 200;
    three below 300); its least node χ²_nine (82.90) and χ²_six (1.53) agree with the run's continuous 82.60 and 1.36;
    the clause: 247 node rows have χ²_six ≤ 15.22, every one with the mixing defined, and their least χ²_4 is 1190.5
    against 13.28; a fresh evaluation at the address by B1821's evaluator gives 291.4867, the run's value, and the least
    of a 5 × 5 grid around it. No finding.
- cc (main), 2026-10-31. **0 of 19.**

## 1. The question (the preregistration, in full in `PREREGISTRATION.md`)

- **THE FINAL ATTACK's Step B** asked whether one address of the frame — one line of order ≤ 12, one of B1810's twelve
  directions (a₀ and F₋₂ priced as one, B1824), one of B1667's two radii, one of the eight readings, τ anywhere on
  continuous τ in the band, the lepton factor c = 3 — reproduces our world's ten numbers within their σ (the relative
  errors in quadrature with 0.10, B1741).
- **The legs:** S (support, the decisive cell), X2 (specificity against random worlds), K (compression of the ten) and
  the CKM leg. PASS needs all four; the card stated before the seal that the conjunction could not pass, since X2 fails at
  the sealed N (p₂ = 3/2000 against the gate 1.89 × 10⁻⁴). The reading was therefore decided by S: SUPPORT WITHOUT
  SPECIFICITY if our world were in the support, NO SUPPORT if not.

## 2. The result (verification/run.json)

| leg | sealed rule | result | graded |
|---|---|---|---|
| S | least χ²_ten < 23.21 at a row with the mixing defined | **291.41** (fresh evaluation at the address 291.49; 0 undecided) | **fails: NO SUPPORT** |
| X2 | p₂'s upper end < 0.01/m = 1.89 × 10⁻⁴ | 4.38 × 10⁻³ (pre-seal) | fails, as stated before the seal |
| K | C_ten > 12.37 bits | C_ten = **−197.0** (C_six −3.08, bits_CKM −193.96; converged, dropped mass 2⁻⁵²) | reported, ungraded |
| CKM | bits_CKM > 12.37 and the clause | bits −194; the clause fails | reported, ungraded |
| T | NEGATIVE under every clock | CONSISTENT under the area clock (y₀ = 2.74, t = 0.31) | reported |

- **The address of the least χ²_ten:** line (3/8, 3/8), direction DR, radius L₂, reading 6, τ = 0.0934 + 2.7426i.
- **Read-outs (never grading):** the least χ²_nine (no J) is 82.6, against its 21.67; S at the c = 1 arm also fails.

## 3. Where the miss lives: the masses and the mixing at different addresses

- **The six alone fit.** The least χ²_six over every cell is **1.36** (1.53 at a stored node): the frame reaches our
  six mass ratios (as B1786 and the arcs before it found on narrower menus).
- **The four alone fit.** Over the frame's physical rows the least χ²_4 of |V_us|, |V_cb|, |V_ub| and |J| at a stored
  node is **0.35** (K's marginal window, run.json `marg_report.ub`): the frame makes our mixing, J included.
- **Never together.** No address whose six lie within 13.86 of the best (the posterior's top within 2⁻¹⁰) reaches the
  four within χ²_4 < 13.28: every such row's rigorous lower bound is above it (the clause, `best_chi2_4: Infinity`).
  The least χ²_ten is 291.4, at a node 291.8.
- **K says the same in bits.** bits_CKM = log₂(posterior predictive / marginal) at our four = **−194**: knowing our six
  makes the frame's prediction of our mixing 2¹⁹⁴ times worse than not knowing them. Where the frame puts our masses,
  its mixings are far from ours; the six are not compressed either (C_six = −3.08: the address's 18.81 bits, τ's mixture
  and the misfit outweigh the six's raw code, as the pass side predicted, P-554).
- **Where the best compromise misses** (the fresh pulls at the address, (frame − ours)/σ; the factor frame/ours):
  |V_ub| **+12.6** (×3.7), |J| **−7.2** (×0.46), u/t +5.8 (×3.2), |V_cb| +4.1 (×1.5), μ/τ +3.7 (×1.45), s/b +2.9
  (×1.46), c/t +2.0 (×1.24), d/b −1.8 (×0.80), |V_us| −1.0 (×0.90), e/τ −0.7 (×0.94). The compromise pays mostly in the
  mixing's small elements and in the up sector's lightest ratio.
- **The two halves pull apart.** Where the six fit (the 247 node rows above), the least χ²_4 is 1190; where the nine
  fit best without J (χ²_nine 82.9 at a node), |J| is 45σ too small (about 1/130 of ours; χ²_ten 2150).

## 4. What this does and does not say

- **It says:** within the reach, the frame's single rigid address cannot carry the masses and the mixing at once; the
  obstruction is their joint placement, not either alone.
- **It does not say:** that the frame cannot make the SM's numbers (each half is made); that a larger reach fails; that
  a structure in which the masses and the mixing come from different loci fails. Those are untested here.
- **Seen before, on narrower menus, now sealed on the whole menu:** B1713 found the frame's mixing generic (59.5% of
  random hierarchical mixings matched as well) and "masses and mixing together reach only a factor 3.59" on lines of
  order ≤ 12; B1720 found at the threads' apexes that "masses and mixing do not meet (6.5)". B1825 confirms the wall
  at σ resolution, on every line, direction, radius and reading of the menu, with τ continuous, sealed.
- **Consistent with the record, not a new claim:** B1653 (a point coupling has rank ≤ 2: a single-tower wall), THE
  TOWERS (P-415: the SM as the interaction of towers meeting at loci) and NEVER FREEZE THE WEAVE (the interaction, never
  an object alone) each lead one to expect that one address is not enough; this sealed test shows it on the whole menu
  with continuous τ.
- **The hatch** (kill graph): the mixing as the meeting of two addresses — the up and down sectors' diagonalisations at
  different loci, the CKM their relative rotation (P-555); a larger reach (orders above 12, Im τ above 4).

## Seen first

- **The preregistration's sweep** (sealed with it, before the census was read): `VERDICT topic-sweep /nine from one
  address|ten from one address|step b|refined census|continuous tau|bernstein|planted miss|likelihood.ratio bound|
  interpolant/ (full text): 21 of 1570 arcs on main match (NEGATIVE 2, OPEN 1, PROVED 18); 17 register rows match`.
- **The result's sweep** (2026-10-31, after the run, before this was called anything): `VERDICT topic-sweep /two
  addresses|two loci|different addresses|masses and (the )?mixing|mixing as the (meeting|misalignment)|relative
  rotation|up and down .{0,30}(different|separate) (loci|addresses|points|towers)|misalignment of the up and down/
  (full text): 7 of 1571 arcs on main match (NEGATIVE 3, PROVED 4); 2 register rows match (DONE 1, QUEUED 1)`. Bearing on
  it: B1713 and B1720 (masses and mixing do not meet, on narrower menus; § 4); no arc or row proposes the mixing as the
  meeting of two addresses (P-555 is new to the record).
- **Literature (pointers, not read on the bench; no search was run for this result):** modular flavour symmetry
  (Feruglio 2017) and its quark-sector models, which fit the quark masses and the CKM at one τ with free coefficients;
  the frame here has no free coefficient, only discrete choices and τ, which is the difference under test.

## 5. The controls, as sealed (verification/preseal/)

- The certification's planted gate: 0.21% missed (upper ends 0.217% and 0.226%); determinism to storage precision.
- p₂ = 3/2000 ([3.1 × 10⁻⁴, 4.4 × 10⁻³]); vacuity not void (3 of 3 supported null worlds fail K and the CKM leg); every
  Markov bound holds.
- The pass side on B1741's box: all three legs on 7 of 10 worlds planted at an address, 1 of 10 with noise at σ;
  unrelated and anarchy CKMs 0 of 10 each. A world at an address would have been seen; ours is 291 in χ² from any.

> *2026-11-03 (S287, B1826): the mechanism of the miss is a CKM corner inversion. At the least-chi2_ten address the frame's full |V| has |V_ub|/(|V_us||V_cb|) = 1.063 and |V_td|/(|V_us||V_cb|) = 0.094 (|V_ub|/|V_td| = 11.3; sin delta about 0.08): the Cabibbo rotation enters the (1,3) corner, not the (3,1) (the agy lane's diagnosis, verified by main's code; a strong tendency of the frame, not a no-go, by the independent audit lane's scan). The agy lane's four 'Step B defects' change nothing here (B1826 § 2; 4B, a gap in the card's word 'physical', is P-557).*

## Dated note (2026-11-03, S298, the web seat's review of 2026-11-03, verified on main)

- **The bar's grade is NOT FOUND.** THE_FINAL_ACTS_BAR's table makes an attempt NEGATIVE only on S EXCLUDED, an X1 exclusion violated, T NEGATIVE under every clock of the menu, or a V cell NEGATIVE. The card claimed no exclusion (X1: none claimed), the run graded T CONSISTENT under area (run.json), and no V cell ran; main's outcome code (scripts/stepb/outcome.py) reserves NEGATIVE for T NEGATIVE under every clock. So the grade is NOT FOUND within the census's reach and resolution. The verdict field's NEGATIVE stands as the kill graph's category (WORKING_RULES item 4; B1791 the precedent), and the claim's parenthesis already said NOT FOUND; the title's and the verdict line's "NEGATIVE as sealed" named the wrong grade.
- **The headline, as run:** the six alone (1.36) and the four alone (0.35) were reached at different fitted addresses, with c = 3 by hand; the run did not vary the number of addresses. It reads: NOT FOUND for FR-FIB as typed — no address within the census's reach carries the ten.
- **The scope adds H = I** (the generations' metric, a CHOSEN input on the card, B1822: "the census stands, for FR-FIB with H = I"); B1822 is added to depends_on. The web seat's local search at the address finds no near-identity metric that rescues it (its h_near_identity.py; not re-run on main). The reach also omits Im τ < 1, the fundamental domain's sliver below 1.
- **What stands:** χ²_ten exceeds 291 at every point of the reach; by the triangle inequality no shift of the targets under about 12σ in norm reaches the gate, and running is about 3.4σ (R1; P-590).
