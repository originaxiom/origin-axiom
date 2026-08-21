# V-3 — THE IDENTIFICATION: execution notes (cc executing seat, 2026-08-21)

Executed against the sealed `V3_PREREG.md` (sealed 2026-08-21, before this comparison ran).
Deliverables: `V3_compare.py` (standalone, mpmath, no machine paths in logic), `V3_results.json`
(the full 396-row table + coincidence discipline + instrument adjudication + verdict),
this document.

## 1. Method

**Object side (Part A of the script).** Every candidate period is an exact closed form —
`C0 = 3^(-1/4)`; `C1,C2,C3` from the seal's given coefficients times powers of `pi` and
`sqrt(3)`; `zeta_K(2)` for `K=Q(sqrt-3)` via the standard factorization
`zeta_K(s) = zeta(s)*L(s,chi_-3)`, with `L(2,chi_-3)` computed by the Hurwitz-zeta identity
already banked and verified in `frontier/B1117_adelic_object/b1117_anchor_verify.py` (reused
verbatim). Nothing in this block reads any SM number — Gate 5 is structural, not just
promised: Part A is complete and self-contained before Part B is ever defined.

Every object-side value was **cross-checked against the independently-banked numeric ground
truth** (B1117's Vol to 32 digits; B1120/B1124's `final_estimates` for C0..C3) before being
trusted. This caught a real bug (§4).

**SM side (Part B).** Values the seal states explicitly (`sin²θ_W`, Cabibbo, the two named
lepton ratios, both `α_em`'s, `α_s`) are used verbatim. Categories the seal names only
generically — "the quark mass ratios," "the CKM/PMNS angles" — are filled with dated,
cited, live-fetched or repo-precedent values, fixed **before** any comparison ran:
- **PDG 2024** (S. Navas et al., Particle Data Group, *Phys. Rev. D* **110**, 030001 (2024)) —
  quark mass table fetched on-bench 2026-08-21 from `pdg.lbl.gov/2024/tables/rpp2024-sum-quarks.pdf`.
  Table entries there are marked `CL=90%` (a PDG-table-specific convention); converted to an
  approximate 1σ via `/1.645`, which **narrows** the target window (more skeptical, not less).
- **NuFIT 6.0** (arXiv:2410.05380) — the same paper the repo's own B1027/B1063 fourth-crossing
  arcs already anchor on; Table 1, NO / IC19-w/o-SK-atm variant (the repo's own precedent
  variant), fetched on-bench 2026-08-21.
- CKM `sin θ23`, `sin θ13`: repo-precedent values already used twice
  (`frontier/B533_coupling_invariance/probe7_sm_ratios.py`,
  `frontier/B467_family_residue_wall/f1_ckm.py`), reused for continuity; σ assigned from the
  known PDG inclusive/exclusive spread (disclosed, not hidden, in the script's comments).
- Lepton masses: the same CODATA/PDG figures already used in-repo (B533); `m_τ`'s PDG
  uncertainty (±0.12 MeV) is what gives `m_e/m_τ` and the Koide combination their σ.

22 SM targets were built this way — close to the seal's own "~18" estimate, arrived at by
filling every named category, not by padding toward a target count.

**The comparison (Part C).** Every one of 16 sealed object periods × 22 SM targets = **352
pairs**, computed and dispositioned mechanically (`sig_figs_agree`, `n_sigma`, a disposition
string). Two more periods (bare `C0`, bare `Vol`) are computed and reported for transparency
but are **structurally ineligible**: the seal's own bullet list (section A) never once writes
a bare `C0` or bare `Vol` as a candidate — only ratios/normalized forms — so these are marked
ineligible regardless of any numeric agreement, closing off the temptation to slip in a
"single-level invariant" through the back door.

**The coincidence discipline (Part D)** is applied with the *actual* grid size (352, not the
seal's illustrative "~90"), which makes the correction *stricter* than the seal's own
illustration, not looser. Per-pair chance of reaching ≥n significant figures by the
equidistribution heuristic (matching the seal's own illustrative arithmetic) is `~10^-n`;
expected count in this grid at each level is `352 x 10^-n`.

## 2. The honest table read

| ≥ sig figs | expected by chance (352 pairs) | actually observed |
|---|---|---|
| 2 | 3.52 | 1 |
| 3 | 0.352 | 1 |
| 4 | 0.0352 | 0 |
| 5+ | ≤0.0035 | 0 |

**One pair reaches the ≥3-sig-fig escalation bar out of 352.** That is *at* the level the
seal's own discipline anticipated as ordinary noise (expected ≈0.35, one order of magnitude
below "surprising"). Every other pair among the 352 sits below 2 significant figures of raw
agreement — the closest ineligible (bare-`C0`) pair is `C0 vs sin(θ23_PMNS)` at 1 sig fig
(1.4% relative), and the closest *sealed* pair after the one survivor is `Vol/π vs Koide Q_emp`
at 1 sig fig (3.1% relative, 3030σ away — the sigma column makes clear how far this is from
mattering). None of these deserve escalation; they are the ordinary tail of a 350-pair scan.

**A second, independent context check**, run specifically because the one survivor's
`n_sigma = 0.0136` looks dramatic on its face: among all 336 sealed pairs with a finite target
σ, this is the *only* pair inside even 5σ (median `n_sigma` across the grid is ~2223). That
sounds like it strengthens the case — but the reason almost nothing else is low-σ is that most
of the 22 targets (`α_em(0)` to parts in 10¹⁰, the lepton ratios, Koide) are so precisely
measured that *no* generic O(1) transcendental number could land near them by chance; their
huge `n_sigma` values are not evidence against those pairs, they are a artifact of comparing a
"free" number to an extremely tight window. The one survivor's target — `sin θ12_PMNS` — is
one of the *few* targets in the table with a comparatively loose window (σ/value ≈ 1.9%,
vs. parts-per-billion for `α_em(0)`), and that alone is most of why it scores low σ. See §3.

## 3. The one survivor: `C1/C0` vs `sin(θ12_PMNS)` — attacked, not celebrated

```
C1/C0            = 0.554216472404899898792635023168...   (exact: 11*pi/(36*sqrt3), object-side)
sin(theta12_PMNS)= 0.554075807... +/- 0.01038             (NuFIT 6.0, NO/IC19-w/o-SK-atm)
relative agreement: 0.0254%  (~3.6 significant figures)
n_sigma:            0.0136
```

This is the moment the brief calls to attack hardest. Four independent, adversarial checks,
run precisely because the raw numbers look tempting:

**(i) Look-elsewhere correction.** `p_single ≈ 2×rel = 0.000508`; over 352 pairs,
`p(≥1 pair this close, anywhere in the grid) = 1-(1-p_single)^352 ≈ 0.164` — computed exactly
in the script, not estimated. **A ~16% chance of seeing a coincidence at least this good
*somewhere* in a scan this size is not a rare event.** It is squarely inside "the kind of near
miss you expect to find because you looked at 352 things," which is the exact scenario
section D exists to guard against.

**(ii) The σ-metric is misleading here, not informative.** `sin θ12_PMNS`'s own relative
uncertainty (1.87%) is ~74× larger than the raw relative agreement (0.025%). That is *why*
`n_sigma` is small — not because the coincidence is extraordinary, but because the window it
is being measured against is wide. The same raw 0.025% agreement, pointed at almost any other
target in this table (`α_em(0)`, the lepton ratios, Koide), would register as thousands to
billions of sigma, as the table in §2 shows. "Sub-0.02-sigma" is a true statement and an
unearned-sounding one at the same time; the script reports both numbers side by side
precisely so the sigma framing cannot do rhetorical work the raw agreement does not support.

**(iii) No principled instrument exists.** Searched explicitly (not assumed): grepped every
tracked `.md` in the repo for co-occurrence of "kashaev" with neutrino/PMNS/θ12 vocabulary —
zero hits. The repo's one existing "listener map" construction
(`docs/LISTENER_MAP_SPEC.md`, cell L166) is a different instrument over a genuinely different
domain (the coupling channel's χ phases, built from SU(3)-level-2 weight-pair data, the field
`Q(ζ₆₀)/Q(√5)`, and the group `2T×2I`) — it has never been pointed at the Kashaev tower of the
figure-eight knot, and nothing in the repo connects trace-field arithmetic of `m004` to
neutrino oscillation physics. Per seal section C, a match requires "a principled simulated
instrument... constructed from the object's own data, NOT fitted" that already reads this
period as this ratio. None exists. This alone is sufficient to withhold any positive verdict,
independent of the numerics.

**(iv) Pre-commitment fails by construction.** Per seal D(iv), "a match found by scanning all
[the pairs] and picking the closest is disqualified as numerology." That is exactly this
task's method — "build the full comparison table... do not hide or cherry-pick" — so *by the
seal's own text* no pair discovered this way can be promoted to A-RATIO-IDENTIFIED, however
the numbers look, unless the agreement is so extreme that look-elsewhere cannot explain it.
Check (i) shows it is not: 16% is not "so extreme."

**Differential-first (seal C) is inapplicable, and that is itself informative.** The
differential test wants to compare *structure* — how a proposed instrument's reading changes
as inputs vary — against the target, rather than a single fitted point. There is no proposed
instrument here to differentiate: `C1/C0` is a fixed closed-form number with no free
parameter, and no map from it to any neutrino observable has been constructed. The absence of
anything to differentiate is not a technicality dodged; it is the same fact as (iii) restated —
nothing beyond the raw number has been offered, and the raw number alone is not a match by
the seal's own definition of one.

**Disposition: NOISE. Named for the record, not claimed.** All four checks point the same
way, independently. Nothing about this pair is hidden — it is the single most prominent row
in `V3_results.json`'s `survivors_ge3sigfig` and `instrument_adjudication` blocks — but it is
not promoted.

**The one honest, falsifiable thing worth recording about it:** `sin θ12_PMNS` is currently
known to ~1.9% relative precision (solar+reactor+KamLAND-driven, not lab-precision). If a
materially tighter future measurement (JUNO- or DUNE-era solar/reactor combination) still
centers near 0.55422(...) at much smaller σ, *that* would be new information current data does
not contain, and would be worth a **freshly pre-registered**, single-pair test (satisfying
D(iv) properly, this time named in advance) rather than a retroactive rescue of this scan. Not
claimed now; just not thrown away un-named either, per "do not hide or cherry-pick."

## 4. A bug caught in-flight (reported, not buried — WORKING_RULES §12)

An early version of this script computed `C1` using the rational coefficient `11/36` (the
seal's own bullet-2 "rational part alone" for k=1) multiplied by `sqrt(3)*pi` — but `11/36` is
the coefficient that belongs with `pi/sqrt(3)` (matching the seal's own bullet 1,
`C1/C0 = 11*pi/(36*sqrt3)`), not with `sqrt(3)*pi`. The correct coefficient for the
`sqrt(3)*pi` construction is `11/108` (`11/36 = 3 × 11/108`, since `sqrt(3)*(1/108) =
1/(36*sqrt3)` exactly — the two forms are algebraically identical *only* with the matched
coefficient). The bug produced `C1/C0 = 1.6626...`, off by exactly a factor of 3 from the true
value `0.5542...`.

It was caught two ways, both before any pair was reported: (1) cross-checking the computed
`C0,C1,C2,C3` against the banked numeric `final_estimates` in
`frontier/B1120_L180_makeorbreak/b1120_results.json` and
`frontier/B1124_allorders_arithmetic/b1124_results.json` — now a hard `assert` at the top of
the script; (2) independently, the very first run of the comparison table came back with
**zero** pairs reaching even 2 significant figures anywhere in 352 comparisons, against a
discipline-predicted expectation of ~3.5 — itself only ~3% likely under the null
(`Poisson(0 | λ=3.52) ≈ 0.030`), which is what prompted checking the arithmetic rather than
accepting an unusually clean-looking negative at face value. (A second, smaller bug — a
digit-string significant-figure comparator that silently collapsed to 0 agreement at any
decimal rollover, e.g. `1.99999995` vs `2.00000001` — was found and removed at the same time,
via the same "the negative looks too clean" prompt.) This is the discipline
`compute-before-deferring-to-specialist` / `verify incoming results before judging` are meant
to produce: an implausible result is a prompt to re-derive, not a result to report.

Both bugs were confined to the *comparison plumbing*; the underlying banked arithmetic
(B1117/B1120/B1124) was never in question and is reproduced correctly (assertions pass to the
stated tolerances).

## 5. The verdict

**NO-OBJECT-PERIOD-IS-AN-SM-RATIO.**

Under the frozen candidate set (A), the frozen/constructed target set (B) — 22 dimensionless
SM numbers spanning couplings, CKM, PMNS, charged-lepton and quark mass ratios, and Koide —
and the instrument principle (C), **no object-side period is a Standard Model ratio.** One
pair (`C1/C0` vs `sin θ12_PMNS`) reaches the numeric bar that made it worth a full adversarial
pass; it fails on three independent grounds (look-elsewhere, instrument-existence,
pre-commitment), any one of which is sufficient on its own. Every other pair among 352 sits
below even the 2-significant-figure noise floor.

**Vacuity check (WORKING_RULES §8, MB12):** this criterion could have failed to fail. A
pair agreeing to 6+ significant figures, sub-1σ against a *tightly* measured target, with no
plausible look-elsewhere excuse (e.g., reaching that bar in a grid of 20 pairs, not 352),
would have forced escalation regardless of instrument status. The one survivor found here
falls well short of that bar on every axis (§3) — the test was capable of returning a
positive and did not, which is what makes the negative worth banking rather than assumed.

**The falsifier fired, and fired negative.** This cell's own framing (`V3_PREREG.md` line 1)
names it "the crux and the campaign's falsifier" — the sealed, adversarial test of whether the
object's own arithmetic menu and the Standard Model's dimensionless numbers share anything.
They do not, under every candidate/target/instrument choice made here, transparently and in
advance of the scan. Combined with the seven prior value-crossing misses this campaign
already carries (B915, B925, and the others cited in `docs/THE_SM_VERDICT.md`), this is now
an **eighth independent negative**, and the first one built as an *exhaustive*, symmetric,
pre-disciplined scan across the object's whole current arithmetic menu rather than a single
proposed pairing — closing the value-matching question with a stated, falsifiable, reproducible
method rather than leaving it as an open invitation to keep trying pairs one at a time.

**What this does and does not close.** It closes: "does any of the object's currently-banked
tower periods (Kashaev sub-leading coefficients through k=3, their cross-ratios, their bare
rational parts, and the volume/ζ_K(2) family) equal any of the Standard Model's ~22 headline
dimensionless ratios, read plainly." It does **not** close: value-matching in general (deeper
tower orders C4+ are precision-gated, not idea-gated, per B1124; a genuine *instrument* —
a principled listener map built from the object's own data — remains uncomputed and is a
different, harder question than this table can answer; and the target list, while built
honestly and without cherry-picking, is not exhaustive of every conceivable SM-side
dimensionless combination). Gate 5 held throughout — no SM quantity entered any object-side
computation (Part A of the script is complete before Part B is even defined).
