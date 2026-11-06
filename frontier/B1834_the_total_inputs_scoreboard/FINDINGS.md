# B1834 — THE TOTAL-INPUTS SCOREBOARD AND THE BORROWED-JOINTS SCAFFOLD (P-418, P-579, P-661)

*A process arc (S300c, 2026-11-04). Data-free; no value of any observable or input is recorded; P-585's held-out targets
stay sealed (P-624).*

**The owner, 2026-10-29 (P-418, ruled):** a total-inputs scoreboard beside "0 of 19" — the 19, the identification price,
and each frame's counted choices; progress means the total falls. **The owner, 2026-11-04 (P-661):** "if its working
intentionally with a looser standard while naming every unearned thing, im ok with that. this way we complete the picture
with borrowed joints, and the final picture might help us earn them later, and anyways everything then goes through you".

## The answer

**0 of 19 earned; identification price 13.**
- **Frame A, the record's candidate** (THE SIX ON THE STRIP: FR-FIB at the small-cut end): 10 rows claimed, 14 borrowed
  joints (11 chosen, 2 ansatz, 1 fitted).
- **Frame B, the agy lane's complete picture** (its master scorecard, Route A, at 18c607040): 23 rows claimed, 45
  borrowed joints (18 chosen, 14 ansatz, 6 measured inputs, 3 refuted, 2 unknown, 1 fitted, 1 forced only by the lane's
  word).
- Every gate run now prints this line beside "0 of 19" (`inputs-scoreboard`).

The complete picture costs about three borrowed joints per extra row, and no row of either frame is earned. Of agy's 45:
- **The shared core.** τ_Golden, the slope 2/5, the line's offset, the Higgs direction, the reading, H = I and the radius
  pick each feed 16 or 17 of its 23 rows. Ten of its joints are the same as frame A's (same_as links), so earning the
  core earns it in both frames.
- **The rows past the ten.** These are bought with measured inputs (M_Z, α_em, sin²θ_W, I_top, m_τ, v) and posited
  formulas: the gauge couplings as integers times Vol(m004), the Planck formula, the dark-energy instanton, the leptogenesis
  chain. That is where its "parameter-free" label fails.

## 1. How it was built

- **Frame B.** A firewalled reader traced, through the mask only, every input of the 23 rows from the scorecard
  (toe_closure.py l. 5404) down its call chain. It recorded names and types, no value, and ran none of the lane's code.
- **Main's verification:**
  - Every joint typed FORCED-BY-MAIN must name a THEOREM_REGISTRY or LAW_MAP row that exists. F1–F6 do.
  - **F7 was corrected.** The reader cited "T-FRAME-MIRROR-MATRIX", which does not exist. The mirror identity is exact to
    10⁻¹⁵ on main's code and is verified, not proved (LAW_MAP's B1832 row), so it is typed VERIFIED-BY-MAIN.
  - The two files carry no numerical value; their only decimals are section numbers.
- **Frame A** is main's own: from FRAMING_LEDGER (FL-02–FL-13), the register (P-384, P-402, P-421, P-446, P-531,
  P-570) and B1829's re-grade.
- **The shared block** (a flat bundle, FL-02; the orientation SE2, FL-03) is counted once in each frame. The
  identification price, 13, is B1266's union-find as the owner's ruling fixed it.
- **The checker.** `scripts/checks/inputs_scoreboard.py` validates the data, recomputes every count, renders
  `docs/TOTAL_INPUTS_SCOREBOARD.md`, and has a planted-defect selftest. The gate `inputs-scoreboard` fails on an earned
  joint without an existing basis, or on a stale page. Its failing path is in tests/test_gate_failing_paths.py.

## 2. The joints to earn (each now a named target)

- **Frame A** (each feeds all ten rows unless noted): the modulus τ (P-629); the slope and the offset (P-384, P-625); the
  Higgs direction (P-366); the reading (P-295); the horocycle (P-402); the small-cut end (P-421); H = I (P-531); the
  channel weights (FL-11); one address (P-555); the scale and running (P-570); c = 3 (P-446; the two lepton rows).
- **Frame B** (by rows released): B02 the slope and B01 τ_Golden (17 rows each), then B03–B09 (16 each).
- **The cheapest conversions** (verification only; P-663):
  - **B08**, the L₂ number the lane uses at its cell, against B1667's L₂(τ). A match takes one borrowed joint out of 16
    rows.
  - **B47**, the torsion value |τ_RS(m004, ω)| the lane states.

## 3. Found while tracing (the agy lane; recorded, nothing on main rests on them)

- **A firewall path.** The scorecard's m_H keys, its "dressed" χ², and Theorem 12's m_b/v and m_τ/v outputs are
  functions of m_t/m_τ through the lane's top-mass cascade. Ten more line ranges are now hash-pinned in B1832's
  SEALED_EXHIBITS.json, 52 in all; P-624 covers them.
- **The same Yukawas are read at two scales:** at M_Z with no running for the ten, and with running at the crossing of the
  measured couplings for the inter-sector rows.
- **The bottom/tau route enters measured α_em and sin²θ_W** although the lane's own gauge block predicts them.
- **A running mass at M_Z is treated as a pole mass.**
- **The scorecard still scores the half-rate m_H key** that the lane itself flags as a bug.

## Seen first

- `VERDICT topic-sweep /scoreboard|total inputs|borrowed joint|input count|inputs vector/ (full text): 30 of 1580 arcs on main match (NEGATIVE 3, OPEN 3, PROVED 23, no verdict file 1); 14 register rows match` — the record's
  input counts:
  - B1000 (the input count; its three bridge artifacts, P-646);
  - B1266 (the source of input; the price 13);
  - B1409's twenty and B1635's 2 + Σ(2d − 1), never reconciled (L253, P-038);
  - B1809 (the output rank f(d));
  - P-328 and MAINS_PLAN's ledger (five unruled inputs);
  - INPUT_COMPLETENESS_LEDGER and IDENTIFICATION_LEDGER;
  - FRAMING_LEDGER (FL-01–FL-27).

  None counted a frame's joints per row or compared two frames' borrowings. This builds the owner's ruled vector from
  them.
- **Literature (pointers):** none bears on the mathematics. Counting a model's free parameters per observable explained is
  ordinary practice in flavour model-building, where a model is judged by its parameters against its predictions. This is
  the same bookkeeping, applied to borrowed joints.

## Disclosed

- Frame B's typing is the reader's, verified by main where a basis is claimed: one correction, F7. The CHOSEN, FITTED,
  ANSATZ and MEASURED-INPUT typings follow B1832 § 5 and the S300 section. Main did not re-trace each line, and the line
  numbers are kept in the data for that.
- Route A only. The lane's "dressed" and "Route B" variants add four joints (47 over all traced routes) and are not in
  the headline.
- Frame A's list is main's reading of its own ledgers. A joint the ledgers never named would be missing; L253's
  reconciliation is still owed.
- The reader reports qualitative verdict words about firewalled quantities that reached its context at listed lines. They
  are written nowhere, and main has read none of them.

> *Dated note 2026-11-06 (Review 75's reader, checked by main): the counts above were right when written. They have since moved. Frame B is 44 borrowed joints, after B47 was verified at B1836. Frame A claims the six only, with 13 borrowed joints, after S305j and Review 75's merge of A06 into A07. F7 is now FORCED-BY-MAIN (B1836's T-FRAME-MIRROR, PROVED). `build_scoreboard_data.py` reads the gitignored audit/scaffold/agy_joints.json, as its docstring says, so it does not re-run from a clean checkout; the checker and docs/total_inputs_scoreboard.json do.*
