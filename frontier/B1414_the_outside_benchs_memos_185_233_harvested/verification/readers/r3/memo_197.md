# Reader r3 — memo 197 (THE_CLOSURE_IS_GENERIC)

## 1. HEADLINE
"THE SEALED EDGE LAW IS THE MODAL BEHAVIOUR OF A RANDOM PHASE." **2026-09-11.**

## 2. CLAIMS
1. B1106's C-GEN (slope-genericity: golden closes, strict silver never does)
   **re-run here** at six Pell windows: silver closes at **none** — C-GEN preserved. — **B / PRESERVED, not overturned**
2. CELL 1 — closure-set measure in ρ at four Fibonacci windows: N=21 → 53.18%,
   N=144 → 54.97%, N=233 (odd index) → 55.10%, N=987 → 55.21% — closure is the
   **majority** case at every window, including the odd-index one. — **B (measured fact)**
3. CELL 2 — 3000 random phases over nine consecutive Fibonacci windows: **35
   distinct patterns**; the sealed law `C.C.C.C.C` is the **mode** at 19.77%; its
   mirror `.C.C.C.C.` second at 15.00%. — **B (measured fact)**
4. Consequence for the falsifier: an experimentalist scanning the phason passes
   through the sealed alternation at roughly **1 phase in 5**, so observing it at
   α does not identify α. — **derived from claims 2-3, stated as a reading, not re-sealed**
5. Combined reading: the lab lane's content is slope-specific (real), not
   phase-specific (this memo), not contingent on a measurement (memo 196 add'm 1),
   and unable to reach the SM (memo 196 add'm 2, tiling hull sees only the hearing). — **synthesis, not independently re-verified here**
6. THE COUNTER-ARGUMENT is stated and explicitly **NOT adjudicated**: the object has
   no free ρ (the cut phase IS the slope by construction), so a look-elsewhere count
   over a knob the theory never turns may not be a charge it must answer. Against
   that: B1085's banked object is the function ρ↦edge content and the apparatus
   scans ρ (144 banked points), so the sweep is the experiment's own. — **BOTH READINGS RECORDED, neither adjudicated — explicitly left to the seal-holder**
7. Nothing retracted: C-GEN stands and was re-run; B1095's mechanism stands;
   B1106's seal discipline "did what it was built to do." — **explicit non-retraction**

## 3. CERTIFICATE
`outside_bench/certificates/closure_is_generic_in_phase.py` exists.
`outside_bench/outputs/closure_is_generic_in_phase_out.txt` exists. Its final
verdict block:
```
CELL 2 ... reproducing the SEALED LAW exactly: 593 (19.77%) ... -> B
CELL 3 C-GEN's slope control, re-run here: silver closes at Pell windows?
  [False, False, False, False, False, False] -> B
ALL CONTROLS PASSED
VERDICT: CELL 1 = B, CELL 2 = B, CELL 3 = B
```
This **agrees** with the headline and with claims 1-3 exactly (numbers match:
19.77%, all-False silver). No seal is named for memo 197 (Gate 5 untouched, no
value promoted); sha256 check N/A.

## 4. ON MAIN ALREADY?
- **(b) applied via the merge as an ADDENDUM inside a main arc**, with an explicit,
  attributed citation: `docs/OPEN_LEADS.md:1917` (row **L173**) reads: *"the price of
  passing is priced: outside-bench memo 197 shows the sealed alternation is the
  **modal** behaviour of a random phase (19.77% of 3000; one phase in five
  reproduces it over nine windows), so observing it at ρ = α does **not** identify
  α — the lane is slope-specific, not phase-specific."* This is a verbatim,
  numbered citation of memo 197's own headline and figures on main.
- Claim 1 (C-GEN slope law) — **(a) already on main independently of this memo**:
  B1106 in `docs/EDGE_PREREG_SPEC.md`/`SEAL_LEDGER` predates and is cited by
  `OPEN_LEADS.md:1917` as the original C-GEN result this memo re-ran.
- Claim 5's "unable to reach the SM" component (memo 196 addendum 2) is not one of
  my assigned memos and not independently checked here.

## 5. NEEDS COMPUTATION HERE
- Claim 2/3: re-run the phase sweep (3000 uniform random ρ over the unit interval,
  the nine consecutive Fibonacci windows N ∈ {21,34,...,987} per B1085's edge-count
  routine) and confirm the modal pattern frequency lands near 19.77% (±1-2% given
  3000 samples) and the mirror pattern near 15.00%. Population: 3000 iid uniform
  phases; expected number: mode ≈ 592-600 of 3000.
- Claim 1: re-run C-GEN at the six Pell windows for the strict-silver slope and
  confirm all six return `False` (no closure).

## 6. SUPERSESSION
Not superseded by a later outside-bench memo (no later INDEX row references or
retracts 197). The counter-argument in §4 is explicitly left open by the memo
itself and by `OPEN_LEADS.md:1917`, which records the finding without resolving
which reading (object-has-no-free-ρ vs. the-scan-is-the-experiment's-own) wins —
this is a live, stated ambiguity, not a superseded claim.

## 7. GRADE PROPOSAL
**ALREADY-ON-MAIN** — the memo's headline, its two key numbers (19.77% mode,
silver-never-closes at six Pell windows) and its falsifier-pricing consequence are
quoted by number and by figure verbatim in `docs/OPEN_LEADS.md:1917` (row L173),
which is the arc this memo's finding was meant to feed. The unresolved
counter-argument (§4/2.4 above) is worth flagging for a future seal-holder
decision but is not itself a discrepancy with main.
