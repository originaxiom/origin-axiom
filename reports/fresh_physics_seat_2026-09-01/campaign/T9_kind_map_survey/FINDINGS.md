# T9 — THE L154 KIND-MAP SURVEY: the instrument GC-6 named, run at corpus scale

**Cell:** T9, fresh physics seat, 2026-09-01. **Gate 5 absolute** (every number
below is a lattice norm, a series coefficient, or the central charge of a named
module — no measured SM value anywhere). Code: `kind_map_survey.py` (exact
int/Fraction arithmetic in every decisive step; floats only in the banded
growth-fit diagnostics). Full log: `survey_output.txt`; machine-readable
verdicts: `survey_results.json`; the census with locations: `CENSUS.md`.

## VERDICT: EMPTY-CONFIRMED — with the census claim itself corrected

**No candidate boundary character exists anywhere in the committed corpus.**
The census is exhausted (16 computable series entries + 10 not-comparable
classes), the kind-map was actually run on every entry, **0/16 pass**, and
every failure lands on a **named** condition with its exact first violation
recorded. The controls bite in both directions (below), so the emptiness is a
property of the corpus, not of a toothless gate. This upgrades GC-12's
one-file claim to corpus scale and **hardens sigma's anchor status** (GC row
C4 / v0 §5 row sigma / §6 row 1): the bridge object L154 needs is a genuine
boundary character **no banked artifact supplies or approximates**.

## 1. The census claim (GC-12), adjudicated first

GC-12 claimed: *exactly one banked q-series exists — B672's doublet — and it
fails the kind-map's non-negativity at its first nontrivial coefficient.*

**Split verdict, both halves bankable:**

- **REFUTED as a count.** The corpus's genuine-series census is larger than
  one artifact: (a) the B666/B672 family is ~twelve streams, including a
  SECOND doublet (2hat') and six sextet rows GC-12 never enumerated (banked
  machine-readable in `B666_leads_campaign/cellW33/cellW33_doublet_streams.json`);
  (b) **B724's GGM rotated 3D-index of 4_1** (`Ind = 1 - 8q - 9q^2 + 18q^3 +
  46q^4 + 90q^5 + ...`) is a genuine object-side q-series GC-12's keyword
  sweep could not see (its token is "3D-index"); (c) the **B364/B365/B366
  fiber-torus theta families** (level-15/30, `E(n) = n(n-1)/30` and `n^2/15`)
  are genuine object-side theta q-series ("theta" was not in GC-12's token
  set); (d) the **(E6)_1 characters themselves** sit in the committed corpus
  as B1190's verification artifact. GC-12's own caveat 1 anticipated exactly
  this failure mode.
- **CONFIRMED in operative content.** Every artifact the wider sweep adds
  fails the kind-map too. The corrected census changes the count, not the
  emptiness.

## 2. The kind-map, implemented (conventions stated)

Five machine conditions (`kind_map()` in `kind_map_survey.py`), matching the
six-condition gate of B1034/B1216/P3-"The wall":

- **K-i** genuine formal q-series on a grid `alpha + Z_{>=0}`, rational alpha
  (the `q^{h-c/24}` slot). Objects with no formal expansion -> NOT-COMPARABLE.
- **K-ii** non-negative INTEGER coefficients after stripping `q^alpha` (a
  character is a graded-dimension count); first violation reported exactly.
- **K-iii** `c = 6` exactly. **Convention for reading c off a candidate
  (stated):** a candidate supplies c only if its banked record names a chiral
  algebra/module with stated central charge, or banks (h, c) with
  `alpha = h - c/24`; otherwise UNTYPED-FAIL — the artifact does not present
  itself as a character of anything, and inventing a c for it would be the
  kind error GC-6 was refuted for.
- **K-iv** Cardy growth at SIX cusp-boson units, as the sqrt-growth-constant
  test: least-squares `log a_n = A*sqrt(n) + B*log(n) + C` on the upper half
  of the support, `c_eff = 6A^2/4pi^2`; PASS band `c_eff in [4.5, 7.5]` with
  >= 200 usable terms; the ONE-UNIT band `[0.5, 1.6]` is separately named so
  6-vs-1 discriminates.
- **K-v** anti-numerology: the object's own datum (m004/family-constructed),
  not imported; classified per entry from the banked provenance, documented.

## 3. MB12 — the controls, actually run, biting both ways

| control | requirement | result |
|---|---|---|
| **planted VALID**: (E6)_1 vacuum character `q^{-1/4} Theta_E6/(q;q)^6`, built in-cell from the E6 root lattice via the A2^3+glue decomposition {(000),(111),(222)} | must PASS K-i..K-iv | **PASS** — `c_eff = 5.996`, sqrt-constant `A = 6.2813` vs `2pi = 6.2832` (601 exact terms) |
| **6-vs-1**: the single cusp boson `1/(q;q)` (what the banked T[4_1] supplies) | must FAIL K-iv in the ONE-UNIT band | **FAIL as required** — `c_eff = 0.999`, flagged "ONE cusp-boson unit" |
| **planted INVALID**: seeded random non-negative integer series (601 terms) | must PASS K-ii and FAIL K-iv | **exactly that** — `c_eff = 0.005` |

The planted character's own construction was gated before use: E6 root count
**72** from the Cartan matrix; direct 6-dim enumeration with a **saturation
check** (boxes +-6 and +-7 agree on norms 0..8 — the inverse-Cartan diagonal
reaches 6, so naive small boxes clip long vectors); glue construction ==
direct enumeration on `q^0..q^4` = `[1, 72, 270, 720, 936]`, then extended
exactly to `q^600`; and the `q^1` grade of the character = **78 = dim E6**
(the level-1 vacuum's grade-1 space is the adjoint). Additionally the B672
reconstruction (fresh, from the Rogers-Ramanujan product identities) matched
the banked B666 integer streams **60/60 per component** before use.

Every condition is failable both ways within this run: K-ii kills eight
census entries and passes eight; K-iii kills the untyped entries and passes
the plant; K-iv kills the random and one-boson controls and passes the plant;
K-v kills the imported (E6)_1 artifact and passes every object-side entry.

## 4. The run: 16 entries, 0 passes, every failure named

| entry (census class) | first failed | exact violation |
|---|---|---|
| 2hat.comp1 / comp2 (A1) | K-ii | n=1: **-9** / **-10** |
| 2hat'.comp1 / comp2 (A1) | K-ii | n=2: **-108** / **-378** |
| F1 / F2 streams (A1) | K-ii | n=1: **3/5**, **-2/5** (non-integer) |
| sextet rows 1,2,5,6 (A1) | K-ii | n=4: -5; n=9: -5; n=5: -1; n=1: -1 |
| sextet rows 3,4 (A1) | K-iii | untyped (no c datum); K-iv also fails (c_eff ~ 0, 20 terms) |
| B724 3D-index (A2) | K-ii | n=1: **-8** |
| B364 triangular / square thetas (A3) | K-iii | untyped; K-iv also fails: unit coefficients => **c_eff ~ 0 — zero boson units, not six** |
| B1190's (E6)_1 vacuum character (A4) | **K-v** | passes K-i..K-iv (c_eff ~ 5.996) but is built from the E6 root lattice, not m004 data — **imported** |

Diagnostic worth banking: even ignoring signs, the B672 streams' |a_n| carry
`c_eff ~ 0.02` — eta-quotient polynomial-type growth. The family is wrong by
**kind and by growth**, independent of any exponent-bookkeeping debate.

The A4 row is the sharpest structural fact the survey adds: the kind-map's
passing branch **is non-empty inside the committed corpus** — the unique
named target (B1228's (E6)_1 vacuum module, c = 6) exists there as a computed
artifact and clears K-i..K-iv — and the ONE clause it fails is exactly the
anti-numerology clause, whose discharge is B1228's one remaining
identification (*nominated type vs geometric connection*). The corpus-wide
survey therefore reproduces, from the object-inventory side, precisely the
bridge statement L154 still owes: not "find a series" (there are series; none
qualify) but "show the boundary algebra of the object's own quotient IS the
nominated (E6)_1" — the K-v discharge.

## 5. What this changes upstream

- **GC ledger row C4 / v0 §5 row sigma / §6 row 1**: the "survey ALL banked
  series" instruction of the typed instrument is now DISCHARGED at corpus
  scale with a runnable, two-sided-controlled gate. sigma's anchor status is
  hardened: no banked artifact is, or approximates, the bridge character.
- **GC-12's row**: carried forward with the count corrected (one family +
  two missed series classes + the imported stage artifact) and the operative
  emptiness upgraded from keyword-scale to extended-sweep scale.
- **The Cardy 6-vs-1 requirement (B1228 K5)** now has a computed referent:
  the one-boson `1/(q;q)` control measures 0.999 units, the (E6)_1 vacuum
  measures 5.996 — the instrument that would recognize a bridge character if
  one ever appears is armed, calibrated on both ends, and committed here.

## 6. Caveats (owed)

1. The sweep is keyword+filename based (extended well beyond GC-12's token
   set, and every hit inspected), but a series artifact named by none of the
   tokens and stored without a series-suggesting filename could in principle
   remain unfound — the same residual caveat GC-12 carried, now narrower.
2. K-iv verdicts are float-banded fits, not exact; nothing decisive rests on
   them alone (every kill also has an exact K-ii or typed K-iii leg; the
   growth clause's calibration is the controls' job).
3. The sextet rows carry only 20 banked terms and an untyped normalization;
   their K-iv failures are typed UNDERPOWERED, but their K-iii failures (and
   for four of six, exact K-ii failures) stand regardless.
4. Provenance classifications (K-v) are documented readings of the banked
   records, not computations; the one entry they kill (the imported (E6)_1
   character) is uncontroversial — it is the stage side of the very bridge
   under adjudication.
5. The B724 3D-index enters via its six banked coefficients (recomputed in
   B724 from the cited literature); the K-ii kill is exact on term 1 and
   needs no extension.

## Reproduce

`python3 kind_map_survey.py` from this directory (~2 s; requires numpy;
reads only `frontier/B666_leads_campaign/cellW33/cellW33_doublet_streams.json`
from the repo). Asserts every gate named above; writes `survey_output.txt`
and `survey_results.json`.
