# PREDICTION.md — Phase C, the calibrated-pair probe under the C-prime variant
# (predictor seat cc2; campaign a463c6aa; design seal 864909ce; prereg 87418916)

## The prediction

**sin^2(theta_12) = 1/(2 phi) = (sqrt(5) - 1)/4  — EXACT, ZERO adjustable parameters.**
Decimal (50 digits): 0.30901699437494742410229341718281905886015458990288
Grammar-side interval: ZERO-WIDTH (the C2 uncertainty-propagation clause is vacuous
under C-prime — no calibration measurement was consumed; recorded per the design).

## The derivation chain (every step a THEOREM row or the sealed design)

1. **B640 (THEOREM, LAW_MAP: the hearing-group theorem):** the hearing factors
   through 2I x Z/3 at level 15; the theta-odd plane carries the golden 2-dim
   character.
2. **B641 (THEOREM, LAW_MAP: the twist-frame tone law):** the ear-independent
   absolute tones are exactly {0, 1/(2 phi), 1/2, phi/2, 1}. The second nonzero
   tone is 1/(2 phi). INDEPENDENT COMPUTATIONAL ANCHOR (this packet,
   derivation/derive.py): this seat's own hearing-group build (360-element image,
   dps 50) reproduces exactly five absolute tones equal to that set (1e-25).
3. **B652 (GATE B, sealed) + B642:** the grammar's single freedom is the Galois
   branch {chi, chi-bar}; its action on the tone is sqrt(5) -> -sqrt(5), giving the
   orbit {1/(2 phi), -phi/2} (exact: (-sqrt(5)-1)/4 = -phi/2).
4. **C-prime (the sealed design, section "THE C-PRIME EVENT"):** the target's type
   is sin^2 in [0, 1]; branch chi-bar's value -phi/2 < 0 is excluded by range
   physicality. THE BIT IS FIXED WITH ZERO MEASUREMENTS. N_eff(channel) = 0.
5. **B633 (banked 2026-07-15, PRE-campaign):** the forward pairing
   sin^2(theta_12) <-> tone_2 — registered before any campaign artifact existed.
6. **R5 typing (frozen checker, frontier/B650_typed_functor/types_checker.py):**
   descriptor dict(contraction_against='listener', x_independence_theorem=True,
   word=None, core_coupled=True, dimensionless=True) -> ('T_coup^inv',
   ('F', 'core', 'dimless')) — same-type, dimensionless, core-coupled as R5 demands.

STOP-condition was armed and never fired: every step above is a FORCED/THEOREM row
or the sealed design's own clause; no unforced quantity entered.

## Exposure line (predictor seat)

Prior SM-value exposure: B615-R (2026-07-15/16) — reanalysis of the banked
comparison statistics (mass-ratio inputs, NuFIT-6.1-era mixing values at the level
of what the record compared, incl. the then-current solar value now quoted in the
design as pre-banked power context); D1 (2026-07-16) — one qualitative Yukawa fact,
no values. This seat has not read any experiment-side value during this lane; the
held-out target (JUNO's first published sin^2(theta_12)) is unpublished and absent
by causality. Blinding rests on the seal order plus this disclosure.

## Conventions block

Exact arithmetic: sympy exact radicals + integer-quantized mpmath at dps 50 (keys at
1e-30); the locked word conventions per the banked record; Galois branch notation
chi/chi-bar of SL(2, F_5) per B642/B644; hash = sha256. Artifacts in derivation/:
derive.py, derive_run.log, derive_out.json. Seals: PREREG_PRED.md 87418916 (sealed
before compute); LANE_READY df7f0300; the design 864909ce verified three ways
(quoted = uploaded = canonical on main).

## One-shot acknowledgment

This is the only comparison under this license. Whatever the outcome, this seat
runs no second channel, statistic, or re-derivation without a fresh owner directive
under the stopping rule.
