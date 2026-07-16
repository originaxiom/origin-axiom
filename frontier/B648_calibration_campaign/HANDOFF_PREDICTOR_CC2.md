# HANDOFF — THE PREDICTOR LANE (to cc2; campaign B648, seal a463c6aa)

**Your role in Phase C: compute the calibrated prediction and seal it
hash-first. You do NOT open, quote, or look up the held-out target at
any point — that is the comparator's lane. Your own exposure line goes
in your packet.**

## Sync first (E3 discipline)

Pull main to ≥ commit 2b43c62 (PR #1054). Read, in order:
`frontier/B652_gate_b/GRAMMAR_TABLE.md` + `GATE_B_VERDICT.md` (the
sealed table and the count), `frontier/B648_calibration_campaign/
CAMPAIGN_PREREGISTRATION.md` (the sealed protocol — §4 especially),
`frontier/B650_typed_functor/TYPES.md` (R5 binds your outputs).

## The state you inherit

GATE B passed: **N = 1, discrete, orbit {χ, χ̄}** — the Galois branch
of the golden character, one choice across the trace law, the tones,
and the congruence shadow (B642/B644 proven). Everything else in the
grammar is forced, computed, gauge, or walled. Your lane is therefore
small and sharp:

## Your task (after the C2 design seal arrives from the main seat)

1. **Receive the sealed C2 design** (it names: the channel, the
   calibration observable, the held-out observable's TYPE — never its
   value — the pinned dataset name+version for the calibration input
   only, the statistic, the success criterion, the FP rate).
2. **Calibrate the branch:** from the C2-named calibration input's
   published value (the design pins where you may read it — it is the
   calibration input, not the held-out target), determine the branch
   χ vs χ̄ by the sealed rule in the design. ONE BIT. Record the bit
   and its provenance.
3. **Compute the prediction:** the held-out observable's predicted
   value from the grammar + the calibrated branch, ZERO further
   parameters. Exact arithmetic where the grammar is exact; precision
   stated where numerical. Show the derivation chain with LAW_MAP row
   citations — every step must be a FORCED row or the calibrated bit.
4. **Seal hash-first:** write `PREDICTION.md` (the value, the interval
   from propagating the calibration input's experimental uncertainty
   per the C2 rule, the derivation, your exposure line, your
   conventions block). Compute sha256. **Transmit ONLY the hash** to
   the owner (for the comparator). Transmit the file itself only when
   the owner confirms the comparator has sealed their target
   extraction.

## Binding rules

- Gate 5: no SM quantity enters CLAIMS.md; your packet is frontier
  material behind the firewall.
- R5: your predicted quantity must carry its type judgment
  (dimensionless, core-coupled, same-type as the calibration input per
  `types_checker.py` descriptors — include the descriptor).
- If ANY step of the derivation requires a quantity the grammar does
  not force and the bit does not fix: STOP, report the gap to the
  owner — that would falsify GATE B's count and reopens B652, not your
  lane.
- One-shot closure: this is the only comparison under this license.
- House rituals: prereg your run before computing (you know the
  drill); preserve failures; hash before rerun; no model names in
  anything that lands in the repo.

## Deliverable

One packet: `PREDICTION.md` (sealed, hash transmitted first),
`derivation/` (scripts + outputs, exact), `SEALS.txt`, your exposure
line, your conventions block. The main seat adjudicates; the
comparator grades. You never see the target; they never see your
derivation before their extraction is sealed.
