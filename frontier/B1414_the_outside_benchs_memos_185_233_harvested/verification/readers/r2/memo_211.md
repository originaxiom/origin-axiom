# Reader r2 — Memo 211 (THE_STALE_ARTIFACT.md)

## 1. HEADLINE
"L72's FLAGGED ISSUE, LOCATED: THE CELL'S MACHINE-READABLE ARTIFACT RECORDS A FAILED RUN OF OLDER
CODE." Cell 1 = B, Cell 2 = A, Cell 3 = A, controls C1–C3 passing. No explicit date line in the
memo body; `INDEX.md` banks it "1B, banked 2026-09-12".

## 2. CLAIMS
1. `FINDINGS_WAVE5.md:22` names "an issue the verifier flagged" **nowhere** — the issue is unnamed
   in the arc. Grade: documentary, verified by direct quote.
2. **CELL 1 = B**: the committed `output.txt` says `VERDICT RESOLVED-A`; the committed
   `results.json` says `UNRESOLVED`. Fields disagree: `wall`/`W_computed_wall` True vs. False;
   `deformation`/`deformation_ok` True vs. False; `theta_odd_directions_exist` not printed vs.
   False. Grade: **OUTCOME B** (discrepancy found).
3. Re-running the cell's **unmodified** `compute.py` in isolation (20.0s): `output.txt` reproduces
   byte-identical apart from a tkinter warning's position, the runtime stamp, and one CS value at
   the 1e-15 level (both effectively zero). `results.json` does **not** reproduce: **51 fields
   differ**, `gate5` key **missing entirely** from the committed JSON. Grade: computed here, PASS
   (reproduction) / FAIL (committed JSON does not match live output).
4. The committed JSON's specific wrong values: `h1 = 0` for all six E₆ exponent blocks (vs. `h1 = 1`
   from the actual code), `rel_ok = False` for all six (vs. `True`), `exact_Qzeta6` absent (vs.
   present with `rel_ok: True`), `lagrangian: False` (vs. `True`), `associator_class` absent (vs.
   `TRIVIAL`), `B581_sign_law_reverified` absent (vs. `True`). Grade: computed, decisive — this
   contradicts B581, B575's G4 gates, the cell's own printed output, and memo 210's Cell 1
   (order of vanishing of Δ_E6 = exactly 6, i.e. six 1-dimensional H¹'s).
5. Diagnosis: the committed JSON is an artifact of an **earlier code version** whose relator check
   failed, so H¹ came out zero everywhere; `UNRESOLVED` is downstream of that; it was **never
   regenerated** after the code was fixed. Grade: interpretive conclusion drawn from claims 3–4,
   labelled as such; fenced ("this memo cannot claim to have found *the* [flagged] issue... has
   found *an* issue, decisive and reproducible in twenty seconds").
6. **CELL 2 = A**: the Deligne splitting (E₆ level-2, three simple currents, ℤ/3-closed,
   `|det S|_pointed = 0.0352828005` vs. cell's `0.03528`; rank-3 Müger centraliser with matching
   qdims 1/1.801938/2.24698 and `h mod 1` agreeing) rebuilt independently, worst entrywise error
   `S`: 6.229e−15, `T`: 1.601e−15. Grade: PASS, independently reproduced.
7. **CELL 3 = A**: Galois sweep over all 6 conjugates `k'=1..6` of the rank-3 factor's candidate
   identification with SU(2)₅-even at `q=exp(iπ/7)`; only `k'=1` matches (`|ΔS|=1.110e-15`,
   `|ΔT|=2.734e-16`); all five others rejected, **including `k'=6`** which shares the *same*
   quantum dimensions but fails on S at 8.427e-2 and T at 8.678e-1. Grade: PASS — quantum
   dimensions alone do not identify the factor; the entry-by-entry S/T test is validated as the
   right instrument (C3/MB12 satisfied: the sweep can and does reject).
8. Two named actions for main, explicitly stated as "neither this bench's to take": (i) regenerate
   `results.json` from the committed `compute.py` (20 seconds, SnapPy present); (ii) the residual
   "uniqueness-up-to-gauge of the level-2 F-symbols" is **narrowed** (Galois closed) but **not
   discharged** — classification needs the rank ≤ 4 MTC classification, unread/uncited here. Grade:
   handoff items, not verdicts.

## 3. CERTIFICATE
- **Seal:** `outside_bench/seals/L72_PHASE2_AUDIT_PREREG.md` — **exists**. Computed
  `shasum -a 256`: `0daa7ada95b244277c404027c03f0eb34424910fcdd3598c9ab14033dd0545cb` — **matches**
  the memo's stated hash exactly. Committed before the certificate per the memo's own claim
  (not independently re-verified via commit timestamps here, but the hash match is the load-bearing
  check and it passes).
- **Certificate:** `outside_bench/certificates/l72_phase2_audit.py` — **exists**.
- **Output:** `outside_bench/outputs/l72_phase2_audit.txt` — **exists**. Tail: `CELL 3 OUTCOME: A`
  preceded by the full Galois-sweep table matching claim 7 exactly (all six `k'` rows, same numbers
  to the printed precision), and `CELL 2 OUTCOME: A` with the cross-bench comparison line matching
  claim 6. **Agrees with the memo's headline and Cell 2/3 outcomes.** Cell 1's `OUTCOME: B` verdict
  is stated in the memo body and matches the output's own framing (not independently re-quoted
  above, but the 51-fields-differ / `gate5`-missing claims are exactly what a live diff would show
  and are consistent with the memo's stated methodology).

## 4. ON MAIN ALREADY?
1. **Action item (i), regenerate `results.json`:** **(a) already on main.** Verified directly:
   `frontier/B775_phase2_wave1/cells/P2W5-L72/results.json` on the current tree has
   `verdict: RESOLVED-A`, `lagrangian: True`, `h1: 1` and `rel_ok: True` for **all six** exponents
   (`1,4,5,7,8,11`), and `gate5` is present. `git log --oneline -- .../results.json` shows the fix
   landed in commit `e15eaada` ("memo 216 — the corrections applied: 15 status supersessions in
   place, 3 artifacts regenerated") — i.e. **memo 216**, not memo 211 itself, performed the
   regeneration this memo asked for. `output.txt` on main matches: `VERDICT: RESOLVED-A`, gates
   line shows `wall True | index True | deformation True`.
2. **Cell 2/3 splitting and Galois-uniqueness finding:** (c) NOT independently re-cited by number
   anywhere in `docs/` (`grep -rl "Müger\|Galois ambiguity" docs/` found no hits tied to this arc);
   the finding lives only in this outside_bench memo and its sequel (memo 218, memo 220). It is
   **not contradicted** by anything on main — B775's cell computation itself is consistent with it.
3. **The uniqueness residual (action item ii):** superseded, see §6 below — memo 220 later
   discharges it entirely using RSW read from an owner-supplied PDF. That happened inside
   `outside_bench/`, not as a `frontier/` or `docs/` edit, so relative to `docs/`/`frontier/`
   governance layers it is (c) NOT on main as a citation, but relative to the outside_bench lane
   itself it is fully resolved (see SUPERSESSION).
4. **`FINDINGS_WAVE5.md:22`'s unnamed flagged issue (claim 1):** checked directly —
   `frontier/B775_phase2_wave1/FINDINGS_WAVE5.md` line 22 still reads with the "issue the verifier
   flagged" language as quoted; the arc file itself was not edited to name the issue explicitly. (c)
   the *documentation* gap claim 1 identifies is still technically true on the source arc, even
   though the underlying artifact (`results.json`) has since been fixed by memo 216's separate
   commit. This is a minor doc-currency gap, not a contradiction.

## 5. NEEDS COMPUTATION HERE
- **Claim 3 (the 51-field diff):** re-run `frontier/B775_phase2_wave1/cells/P2W5-L72/compute.py`
  fresh (SnapPy required; ~20s per the memo) and diff its output JSON against the version currently
  committed at `frontier/B775_phase2_wave1/cells/P2W5-L72/results.json` — expected result **now**:
  they should agree (since memo 216 already regenerated it), which would itself be a useful
  positive-control re-confirmation that the fix in commit `e15eaada` is durable and was not
  itself stale.
- **Claim 6 (Deligne splitting):** recipe is symbolic/exact linear algebra over the E₆ level-2
  fusion data (Cartan-matrix-derived S/T matrices per the memo-206 instrument) — recompute
  `|det S|` on the pointed ℤ/3 part and confirm `≈0.0352828`, and the worst entrywise error of
  `S_{E6,2} − S_{pointed}⊗S_{centraliser}` is `< 1e-14`.
- **Claim 7 (Galois sweep):** recompute `S^{(k')}_{jl} ∝ sin(πk'(2j+1)(2l+1)/7)`,
  `h^{(k')}=k'·h mod 1` for `k'=1..6` and confirm exactly one (`k'=1`) matches the rank-3
  centraliser's S/T to double-precision tolerance and the rest are rejected at the `1e-1`-plus
  level — this is the discriminating fact for "quantum dimensions alone do not identify the
  factor," since `k'=6` has identical qdims to `k'=1` yet is rejected.

## 6. SUPERSESSION
- **Fully superseded on the classification residual by memo 220** (`THE_RESIDUAL_IS_DISCHARGED.md`,
  filed as addendum 1 to `PARI_ARRIVES_AND_THE_LITERATURE_WALL.md`, banked 2026-09-13): memo 220
  reads Rowell-Stong-Wang directly (owner-supplied PDF) and discharges the "uniqueness-up-to-gauge"
  residual memo 211 left narrowed-not-discharged. Memo 211's own mathematics (Cells 1–3) is *not*
  overturned — it is *completed* by 220.
- **Action item (i) executed by memo 216** (`THE_CORRECTIONS_APPLIED.md`, addendum 124 to the owner
  register, owner-authorized "do as u recomend"), which regenerated `results.json` — confirmed live
  on main via commit `e15eaada` (§4.1 above).
- No later `outside_bench/INDEX.md` row disputes Cell 1's diagnosis (the "stale JSON from older
  code" reading); later rows (218, 219, 220) all build on it approvingly ("memo 211 settled it by
  re-running the cell's own code").

## 7. GRADE PROPOSAL
**ALREADY-ON-MAIN** for the concrete artifact fix (action item i is done, verified live at
`frontier/B775_phase2_wave1/cells/P2W5-L72/results.json` via commit `e15eaada`), combined with
**SUPERSEDED** for the classification residual (memo 220 discharges it). The memo's own Cells 2–3
mathematics stands unchallenged and is a clean independent reproduction, but the residual it left
open has already been closed by a sibling memo, and the artifact-currency problem it diagnosed has
already been fixed by a sibling memo — there is nothing live left for a verifier to bank as new
work from memo 211 itself, only to spot-check that the two fixes (216, 220) are durable.
