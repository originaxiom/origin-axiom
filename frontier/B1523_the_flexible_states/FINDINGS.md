# B1523 — THE FLEXIBLE STATES: every word state to length 12 carries a projective family at its hyperbolic point; the fibre boundary is a rigid slope on all of them, so main's one-bit rule holds everywhere; and on exactly the 482 states with no longitude-inverting symmetry, no symmetry dualises the family

cc (the SM-derivation seat), 2026-10-03. Sealed at `c13cb636` before `census.py` read dim H¹(M; v) on any census manifold
(`PREREGISTRATION.md`, sha-256 `c61caeb0…`, SEAL_LEDGER).
- **The census.** 3 610 s on four cores: two routes that share no code, on all 536 manifolds of the 758 word states to length 12.
- **Verdict: PROVED, outcome B.** All nine predictions came true (P1–P9); the priors expected 7.1 of 9.
- **Post-run checks (§4).** Written after the seal and disclosed. X1 is a third route, route F, that rebuilds each bundle from its
  word and reads it with its own code. It reached all 536 manifolds, 66 of them also with no SnapPy holonomy, and agrees with
  the census on every one.
- **Prior work: EXTENDS.** The criterion and the family are Heusener–Porti's, Ballas–Danciger–Lee's and Ballas'. The m004 case of
  Lemma R is Heusener–Porti Lemma 8.2 and Ballas Lemma 6.2(2). Main's B1455 and sm:B1520 found the one-bit rule on m004. Here it
  is the census, and the rule on every word state (§6).
- **0 of 19 stays 0.**

## 0. What was found

- **Every word state to length 12 is infinitesimally projectively rigid rel cusp** (P2: 536 of 536, both routes).
  - So each carries a one-parameter family of convex projective structures with its cusp opened, at its hyperbolic point
    (Ballas–Danciger–Lee Thm. 3.2 for smoothness; Ballas, arXiv:1805.09274, Thm. 0.2 for the family).
  - The analogue of m004's Ballas family exists on all 758 states.
  - This answers sL-10 item 6, whose criterion was corrected before the seal. For this class it fills in what Ballas–Danciger–Lee
    left to future work (Remark 3.3): which manifolds of a census are rigid rel cusp.
  - Daly's two examples, L²R² and R²L (arXiv:2411.04431, §4), are reproduced.
- **The fibre boundary is a rigid slope on all 536** (P6). By Lemma R this is the same as **main's one-bit rule (B1455) on every
  word state**: an isometry dualises the family exactly when it inverts the fibre boundary (P3, on all 66 reflective manifolds).
- **Outcome B: the mirror-broken flexible states are exactly the states with no longitude-inverting symmetry** (P5).
  - They are 262 manifolds, 131 per sign, carrying 482 of the 758 states:
    - the **220 chiral** manifolds, whose only symmetries are the identity and ι;
    - the **42 swaprev-only** ones, whose orientation-reversing symmetry keeps the fibre boundary and so does not dualise.
  - On them, near the hyperbolic point, no count-odd map fixes any of the family's vacua other than that point (Lemma T; a local
    statement). B1455's symmetry proof that the index vanishes cannot be made there.
  - The first, at length 6, is **±LLRLRR** (swaprev-only). The first chiral ones are **±L³RLR²**, at length 7.
  - By length 6–12 there are 2, 2, 8, 14, 36, 62 and 138, exactly as sealed.
- **The golden reading** (P7, the owner's "choice might be golden" in its second sealed form).
  - Of the 14 manifolds with monodromy field ℚ(√5), exactly **±L⁴RL³R²** (trace 47) and **±L⁴RLR³LR²** (trace 123) are
    mirror-broken.
  - Their words select them, not their field: both words are chiral, with no rev, no swap and no swaprev.
  - The golden field does not shield a state, and does not single one out.
- **Lemma S holds on the whole census** (P9): every rigid manifold's non-rigid slopes lie in one coset of 60°.
  - *After the run, not sealed:* the box of 16 slopes contains a non-rigid one on exactly the 66 reflective manifolds, always in the
    30° coset (the fibre boundary rigid), and on none of the 470 others.
  - The section is non-rigid on 23 manifolds: m004 = +LR (Ballas' unipotent meridian), its sister −LR, L²R², and others whose
    section lies at 30°, 90° or 150° from the fibre boundary.
- **For the goal.**
  - The projective family exists on every state.
  - An isometry that dualises the family's line (ε = −1) exists on 274 of the 536 manifolds and on none of the other 262.
    - On the 274, Lemma T gives a locus of count-odd-fixed vacua whose tangent space contains the v-line. On m004 that locus
      contains Ballas' family itself (B1455, sm:B1520). Whether it contains the family on the other 273 is not computed here.
    - On the 262, near the hyperbolic point, no count-odd map fixes a vacuum of the family other than the hyperbolic point. So
      B1455's symmetry argument cannot force the family's count to zero there.
  - **Whether the index is nonzero there is not decided here.** That needs the family off its hyperbolic point and the class index
    on it (registered as sL-10 item 8, sealed first).
  - Main's L241 still holds: both orders over a split vacuum count opposite, whatever the stabiliser.

## Seen first (the repo sweep and the literature)

**The repo sweep, before the seal** (PREREGISTRATION §0, the PRIOR ART section). `scripts/checks/prior_work.py` ran on fifteen
terms over nine heads: main `8d1c1329`, the audit lane `7b088f50`, this branch `07faac0a`, the four seat lanes and sep16.
- No head computed infinitesimal projective rigidity, or an isometry's sign on H¹(M; v), on any word state but m004.
- Main's B1455 (the one-bit rule on m004; the only "longitude-inverting" on any head) and sm:B1520 (m004's sign table) were read.
  C5 reproduces both.

**Refreshed at banking** (2026-10-03, after a fresh `git fetch`).
- Main moved to `70ca9c92` and the audit lane to `24c039c8`. A new branch, `art/camper-van-bar` (`b3745696`), is one illustration
  on top of main's `70ca9c92`. The seat lanes are unchanged.
- During the bank, a last fetch found main at `77714caf`: B1459 run. The other heads had not moved.
- The same terms, with "elliptic involution" added, were run again on every head. What is new and bears:
  - **Main's B1457** (S40) rows the audit lane's R32–R80. Its convex-projective reports (from R42 on: the canonical background,
    the cusp's proper convexity, the exceptional loci) are about m004's Ballas family only. None computes rigidity or signs on
    another state.
  - **Main's B1459** (sealed at `70ca9c92`, run at `77714caf`, both read at banking) is adjacent. The fibre's elliptic
    involution ι acts trivially on SL(2) characters of the fibre and inverts abelian characters. So on B1451's rank-four modules
    ρ_ℓ ⊗ ρ_η ⊗ χ it acts as a duality up to a meridian sign: ι̃*V ≅ V* ⊗ ε_mer. Main proves from this that the class index
    vanishes at the 188 complete points (PROVED; ε_mer = −1 on 77 of them). On this arc's SL(4) family ι does not dualise:
    it keeps the family's line (Lemma ι; the sign on the line is +1 on all 536 manifolds in both routes), so it is not
    count-odd there. A sign twist is central, so it acts trivially on sl(4) and does not reach the family's line.
  - **Main's GENESIS v1.4** (B1458) and main's two relays to this seat (this seat's v1.2 adopted on main as v1.3; the bar adopted)
    do not touch this arc's question. They and the audit lane's two relays are logged in RELAY_LEDGER.
  - **The audit lane's** branch sync (`24c039c8`) fetched this arc's seal (`c13cb636`) and records it as sealed, not run.

**The literature, read before the seal** (PREREGISTRATION §0).
- Heusener–Porti: Cor. 5.4, Lemma 5.5, Remark 5.6, Def. 7.1, Remark 8.1 and Prop. 1.9.
- Ballas–Danciger–Lee: Thm. 3.2 and Remark 3.3.
- Ballas: arXiv:1805.09274 Thm. 0.2, arXiv:1403.3314 and arXiv:1210.8419.
- Daly: arXiv:2411.04431 and arXiv:2408.08405.

**After the seal**, while the census ran (at 203 of 536), the claim to novelty of Lemma R was checked. Heusener–Porti Lemma 8.2 and
Ballas arXiv:1210.8419 Lemma 6.2(2) were read; they are Lemma R's special case (§2).
- The sealed reading had stopped at Remark 8.1 and at Ballas' Thm. 1.2, beside them.
- So the seal's "new, as far as swept" for Lemma R is corrected to EXTENDS (ERROR_LEDGER, E54 instance).
- The literature was not searched again at banking.

## 1. The run

**As sealed** (`census.py`, `census_run.txt`, 3 610 s).
- Route R: the real form, SnapPy's simplified presentation, about 2.3 s a manifold.
- Route C: the complex form, the unsimplified presentation, about 24.5 s a manifold.
- They ran on all 536 manifolds. The three literature controls were re-read first and matched `controls.json` (the banked identity).
- `read_out.py` read P1–P9 with no disagreement between the routes and no lemma failure (`read_out.json`, `read_out_run.txt`).

| class (by the words' self-maps) | manifolds | rigid | dualising | mirror-broken |
|---|---|---|---|---|
| chiral (identity, ι) | 220 | 220 | 0 | **220** |
| rev only | 250 | 250 | 250 (−I, Lemma rev) | 0 |
| swaprev only | 42 | 42 | 0 (fibre boundary rigid) | **42** |
| swap only (±L³RL²R³LR²) | 2 | 2 | 2 (fibre boundary rigid) | 0 |
| all three | 22 | 22 | 22 | 0 |
| **total** | **536** | **536** | **274** | **262** |

**The margins** (the decisions' own, in both routes):

| decision | margin |
|---|---|
| rank of H¹(v) | kept singular values ≥ 2.9 × 10⁻⁷, dropped ≤ 2.4 × 10⁻⁴⁶ (route R); ≥ 7.3 × 10⁻⁶ and ≤ 3.8 × 10⁻⁵⁷ (route C) |
| slopes | a non-rigid slope's residual ≤ 4.7 × 10⁻⁵³, a rigid one's ≥ 1.3 × 10⁻⁸ (route R); 2.8 × 10⁻⁵⁴ and 1.5 × 10⁻⁷ (route C) |
| signs | every ε is ±1 exactly in double precision; eigen-residuals ≤ 9.6 × 10⁻⁴⁵ |

## 2. The lemmas, as sealed, on the census

Sealed in PREREGISTRATION §3; each is checked on every rigid manifold in both routes (P8, P9):
- **S.** A class c_a on the cusp vanishes on the slope t iff Re(a t³) = 0. So its zero slopes form three directions 60° apart.
- **ι.** Cusp map I gives ε = +1 (translations act trivially on H¹(P; v)).
- **rev.** Cusp map −I acts on H¹(P; v) as −1, so ε = −1.
- **R.** An orientation-reversing isometry acts on H¹(P; v) as a reflection, and ε = −1 iff it inverts the fibre boundary XOR the
  fibre boundary is not a rigid slope.
  - Its special case at the complete structure is **Heusener–Porti Lemma 8.2** (the figure-eight: i*_l∘ϕ₀* = i*_l,
    i*_m∘ϕ₀* = −i*_m), extended by **Ballas, arXiv:1210.8419, Lemma 6.2(2)** to amphicheiral knot complements. Both were read
    after the seal, when the claim to novelty was checked.
  - What R adds is every orientation-reversing isometry of a rigid one-cusped manifold, rhombic cusps included, with the XOR on the
    slope's rigidity.
- **T.** With no ε = −1 isometry, no count-odd map fixes the family's vacua near the hyperbolic point, other than that point. This
  uses the linearisation of finite group actions at a fixed point, so it is local: it says nothing about the family far from the
  hyperbolic point.

## 3. The predictions

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | the controls pass and the census re-reads them | 99% | **YES** |
| P2 | all 536 rigid rel cusp | 80% | **YES** |
| P3 | on every reflective rigid manifold, ε = −1 exactly on the fibre-boundary-inverting isometries | 65% | **YES** (66 manifolds) |
| P4 | the routes agree everywhere, every margin kept | 99% | **YES** |
| P5 | mirror-broken = no longitude-inverting isometry (262, 131 per sign, 482 states) | 55% | **YES** |
| P6 | the fibre boundary rigid on every rigid manifold | 60% | **YES** (536) |
| P7 | golden: exactly ±L⁴RL³R² and ±L⁴RLR³LR² | 55% | **YES** |
| P8 | the lemmas on every rigid manifold, both routes | 99% | **YES** |
| P9 | Lemma S's 60° coset on every rigid manifold | 99% | **YES** |

Expected 7.1 of 9 under the priors; nine held. P3, P5, P6 and P7 were the open ones. The structure behind them, a fibre boundary
that is rigid on every state, was the least certain sealed prior (60–65%), and it held on all 536.

## 4. Post-run checks (written after the seal; disclosed)

**X1 — route F, the fibration** (`route_f.py`; the passes `route_f_batch.py`, `route_f_reach.py` and `route_f_seeded.py`,
with their `.json` records). See §4.1 for the result.
- *How it works.*
  - It rebuilds each bundle as F₂ ⋊ ℤ from its word: L: a ↦ ab; R: b ↦ ba; ι for the sign −.
  - It finds the fibre representation as a fixed point of the trace map, by its own Newton iteration at 60 digits.
  - It obtains the monodromy's action on cocycles letter by letter.
  - It reads dim H¹(Γ; V) = dim H¹(F₂; V)^t + dim H¹(ℤ; H⁰(F₂; V)) (Lyndon–Hochschild–Serre), and the fibre boundary's
    rigidity on [a, b].
  - It shares no code or presentation with routes R and C. In its first two passes it shares no holonomy either: SnapPy's cusp
    shape only picks which fixed point is the hyperbolic one. Its third pass locates the fixed point from SnapPy's holonomy
    (§4.1).
- *How it was written.*
  - It was written while the census ran, after a preview of the partial records (route agreement; the fibre boundary on the first
    39 reflective manifolds).
  - Two bugs were caught before it read anything: an economy SVD that drops the kernel, and the trivial module's count, which
    omitted H⁰. ERROR_LEDGER.
  - Its first form expanded the automorphism into words of hundreds of letters and was too slow. It was replaced by the
    letter-by-letter recursion, whose controls agree with the first form to every digit.
- *Its reach.* On longer words the trace map has many fixed points, and Newton from random starts can miss the hyperbolic one.
  The first two passes, with no SnapPy holonomy, ran on a stratified set; a third, seeded from SnapPy's holonomy, ran on all 536
  manifolds (§4.1).

### 4.1 X1's result

- **Three passes.** They differ only in how the hyperbolic fixed point of the trace map is found. The reading (the modules, the
  cocycles on F₂ ⋊ ℤ, the ranks, the fibre boundary) is `route_f.py`'s in all three.
  1. **First pass, no SnapPy holonomy** (`route_f_batch.py`, `route_f_batch.json`). It ran on a stratified set of 118
     manifolds: every manifold to length 8, the 42 swaprev-only, the 2 swap-only, the 14 golden and the 23 with a non-rigid
     section (overlapping). Newton at 60 digits from 600 random starts reached 60 and missed 58; the shortest missed:
     ±L²RL²R², at length 7.
  2. **Second pass, no SnapPy holonomy** (`route_f_reach.py`, `route_f_reach.json`), on the 58 misses. A double-precision
     Newton over 20 000 starts a round, polished at 60 digits, with the word's cyclic rotations tried in turn (the same oriented
     manifold), reached 6 more.
  3. **Third pass, seeded** (`route_f_seeded.py`, `route_f_seeded.json`), on all 536 manifolds. The fixed point is located
     from SnapPy's holonomy: a triple of traces of short fibre words in SnapPy's group that route F's own trace map fixes, up to
     an even sign change. It is then polished at 60 digits and checked as in the other passes. It reached 536 of 536.
     - On ±L³RLRLR²LR² the word's own basis gave no seed. Both were reached through a rotation of the word (the same oriented
       manifold), by a fallback added after the first attempt.
     - That attempt's log (`route_f_seeded_run.txt`) is kept, and only these two were run again
       (`route_f_seeded_retry_run.txt`).
- **Without SnapPy's holonomy: 66 of 118.** By class: length ≤ 8, 58 of 68; swaprev-only, 6 of 42; swap-only, 0 of 2;
  golden, 12 of 14; a non-rigid section, 7 of 23.
- **Every manifold reached, by any pass, agrees with the census.** The dimensions are (1, 2, 1) and the fibre boundary is rigid.
  - Where an unseeded pass and the seeded pass both reached a manifold (66 of them), the readings are identical.
  - Several roots can match the cusp shape. The representation twisted by a sign character of the fibre that the monodromy
    fixes is again a fixed point of the trace map, with the same image in PSL(2, ℂ). In the seeded pass, which tries every sign
    change of its seed, the number of matching roots equals the number of such characters on every manifold
    (one on 218 manifolds, two on 190, four on 128). Where a pass found several matching roots, their readings agree.
  - Residuals: the monodromy conjugation ≤ 7.9 × 10⁻⁴⁹, the cusp commutation ≤ 3.8 × 10⁻⁴⁹. The smallest fibre-boundary
    residual is 1.4 × 10⁻⁵; only zero against nonzero is meaningful, since the size depends on the representative.
- **What the seeded pass shares with routes R and C:** SnapPy's holonomy, used only to locate the representation, which is unique
  (Mostow). The point it locates is a fixed point of route F's own trace map to 10⁻⁴⁰, with SnapPy's cusp shape. Everything
  it reads is route F's own.
- **Not reached by any pass:** none.

## 5. What it means

- **The structure is uniform.** On the word states a projective family always exists. Whether a symmetry can dualise it is read
  off the word: rev, or swap, with the fibre boundary always rigid.
- **m004 was not special in having its family's line dualised.** 274 of the 536 manifolds share that. m004 is special only in
  having all three kinds of symmetry, with 21 other manifolds.
- **Where the symmetry argument is unavailable** (the 262), the next question is the one B1455 answered on m004 by symmetry:
  whether the class index on the family's vacua is zero. There it has to be computed.

## 6. Errors, disclosures and standing

- **Before the seal** (in the sealed text):
  - route C's frame read from a vanishing row (ERROR_LEDGER, E31 instance);
  - sL-10 item 6's inverted criterion (E2 instance);
  - C3's relator bar moved from an arbitrary 1e-45 to 1e-35;
  - C9 and P9 added after Lemma S was checked live on m004.
- **After the seal:**
  - Lemma R's prior art (Heusener–Porti 8.2, Ballas 6.2(2)) was found while the census ran, and the sealed "new" was corrected to
    EXTENDS (ERROR_LEDGER, E54 instance).
  - Route F (§4): its two pre-reading bugs (E31 instance), and its second and third passes, which change only the root search.
    A draft named its first miss as ±L³RL²R² at length 8; the record says ±L²RL²R² at length 7 (E11 instance, before the
    commit).
- **The lane.** The fast lane on 07faac0a, B1522's tree, was lost twice:
  - at 55%, to the 30-minute default timeout;
  - at 100%, ten F's in the progress lines matching the baseline's ten, but the container restarted before pytest wrote its summary.

  It is certified on this arc's tree instead (CHANGELOG).
- **Standing: EXTENDS.**
  - The census of rigidity is new as swept: no head computes it, and the literature leaves it open (BDL Remark 3.3; Ballas'
    "majority" without a list).
  - Lemma R extends Heusener–Porti 8.2 and Ballas 6.2(2).
  - The one-bit rule on every word state extends B1455 and sm:B1520.
  - The published version of Daly's paper was not read (behind a login).
