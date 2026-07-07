# B452 — PREREGISTRATION: the Ethogram campaign (E0 — the dictionary + the typed comparison gates)

**Committed BEFORE any observation. Firewalled; nothing to `CLAIMS.md`. Campaign registration:
`docs/OPEN_LEADS.md` §"The Ethogram campaign"; frame + card deck:
`speculations/S055_ethogram/DICTIONARY.md`. Plan v2 (adversarially red-teamed: 1 FATAL + 7 MAJOR
fixed before launch; the EZ type-error fix is THIS document's reason to exist).**

## The campaign in one paragraph

Treat the object as an organism: catalog its behaviors across four generative channels
(surgery lineage, covering tower, word evolution, trace-map dynamics) with **no physics target
during observation**; freeze the catalog; only then compare against a **frozen registry** under
two **typed** gates. Bins per probe: LAUNDERS (burden-inversion F exhibited) · NEW-MATH · H1
(only via EZ, B398 discipline, owner present) · UNDECIDED-AT-DEPTH-L (E2 only, never counted as
H0a). The S054 whitelist binds verbatim; extensions = owner sign-off, retraction-grade.

## The probes (numbering pinned)

E0 = B452 (this) · E1 = B453 (reproduction: covers of the child; the sterility assembly; the
parent cover-field table) · E2 = B454 (the closure lemma + bounded scan, L=8) · E3 = B455
(integrate the five non-geometric E₆ directions; landing-verdict taxonomy) · E4 = B456 (the
catalog, frozen + hashed before EZ) · EZ = B457 (the two typed gates). Thermo D3/D4 keep
B450/B451; thermo-Z pinned ≥ B458.

## THE TWO TYPED GATES (the FATAL fix — frozen here, dry-run-validated in this probe)

**EZ-1 — specificity (behavior vs behavior).** Every catalog entry reduces to a SIGNATURE
(a typed tuple: kind, integer data, field discriminants, periods). For each object signature,
`p₁ = frequency of that signature among the null-ensemble catalogs` (the identical extraction
pipeline run on the environment samples). A signature is *specific* iff p₁ < 0.01 with the null
size supporting it (word channel: n ≥ 1000 random words ⇒ p-values licensed; knot channels:
n < 10 ⇒ **forced/laundered adjudication only, never p-values**).

**EZ-2 — correspondence (number vs number).** Only the NUMERIC parts of signatures (integers,
periods, exponents, discriminants, ratios) enter the SM comparison, under the B322/B398
machinery against the registry below: 1σ windows, match-count statistic, 2000-draw null,
trials-corrected, **binding p < 0.01**. Structural targets use the frozen predicates below with
a combinatorial joint statistic; **structural predicates alone cannot fire H1** (three binary
predicates cannot reach p<0.01) — they contribute only jointly with EZ-2 numerics or an
EZ-1-licensed rarity.

**H1 requires: EZ-1 specificity AND EZ-2 correspondence AND both controls AND the B398
escalation protocol (independent adversarial recompute, owner present) — before a word is voiced.**

## THE FROZEN REGISTRY (comparison targets; frozen at this commit)

- **Numeric (from B398 `s5_statistics.py`, 20 observables with 1σ):** pmns_s12 0.307(13),
  pmns_s23 0.545(23), pmns_s13 0.0220(7), weinberg_MZ 0.23122(4), alpha 0.0072974(1),
  alpha_s_MZ 0.1179(9), ckm_lambda 0.2250(7), ckm_A 0.826(12), ckm_rhobar 0.159(10),
  ckm_etabar 0.348(10), mmu_mtau 0.05946(5), me_mmu 0.004836(1), mc_mt 0.0074(4), ms_mb 0.022(2),
  mu_md 0.47(6), mb_mt 0.0243(5), mtau_mt 0.01027(5), md_ms 0.050(4), theta_c_sin2 0.0506(3),
  jcp_ckm_e5 0.3(1). (B322's 12 are a subset up to naming; deduplicated in `registry.py`.)
- **Structural predicates (frozen as code in `registry.py`):**
  - `P_GEN3`: some behavior's multiplicity invariant equals exactly 3, present in the object's
    catalog and ABSENT from every null catalog (both controls).
  - `P_GAUGE`: some behavior's integer signature contains the multiset {8,3,1} (adjoint dims of
    SU(3)×SU(2)×U(1)) or the rank pattern {3,2,1}, object-specific under both controls.
  - `P_CP`: some behavior is a sign-definite parity-odd invariant (a fixed handedness), nonzero
    and object-specific. [Expected FAIL: the banked heartbeat results show the object's
    chirality oscillates — B448.]
  - Joint statistic: #predicates satisfied; null = the frequency of ≥ that count across the
    null-ensemble catalogs.
- Registry changes after this commit: PROHIBITED (a change = a new campaign).

## THE NULL-ENSEMBLE SPEC (the environment, frozen)

1. **Random-word ensemble** (the p-value channel): n = 1000 uniform binary words per length
  class, seeded (`rng(20260708)`), run through the identical signature-extraction pipeline.
2. **Thue–Morse** (a→ab, b→ba): the structured aperiodic control (constant-length, different
  spectral type).
3. **Foreign knots**: 5₂, 6₁, m003 (+ their slope-5 children where the channel applies).
4. **Same-class**: silver, bronze (m = 2, 3).
Knot-channel and m-channel behaviors: forced/laundered adjudication only (n too small for p).

## The dry run (this probe's computation — the launch gate)

`ez_dryrun.py` builds a synthetic object catalog + 200 synthetic null catalogs and demonstrates:
EZ-1 **fires** on a planted rare signature and **fails** on a common one; EZ-2 **fires** on a
planted 1σ-matching numeric set that beats its 2000-draw null and **fails** on random numerics;
the structural joint statistic behaves (cannot fire alone). The campaign does not proceed to
E1–E4 unless the dry run prints `ALL GATES VALIDATED`.

## MB-guards

MB12: every card carries a falsifier or a forward prediction (the two unfalsifiable v1 cards
were re-cut or retired at red-team); EZ validated to fire AND fail before use. MB7/MB8: no
value-matching anywhere before EZ; the registry is frozen now precisely so the observation phase
cannot drift toward it. The B322 lesson (dense ratio sets match anything) is the reason EZ-2
inherits the trials-corrected null, not naked window-matching.
