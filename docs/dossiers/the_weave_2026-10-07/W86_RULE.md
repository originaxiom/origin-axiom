# W86 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before any check is run. What the seat read before writing it is listed
under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **The owner (2026-10-14, night):** "verify all from chat1 so its not based on wrong computations or bugs for
  conclusions, or misinforment".
- **chat1's branch** (`chat1/web-seat` at 9fbab9f5e) holds 13 folders of computations and readings: 39 scripts, their
  outputs, 35 documents (findings, preregistrations, reports and a meditation), and 14 relays to main. All of it is
  under `relays/` on that branch.
  chat1 offers its thread frame to the tribunal as F5. Main (B1650, S124, S125) and this seat (W84, §105–§110) cite its
  results.
- **Parts were checked before:**
  - W75 put chat1's scale check on this seat's instruments;
  - W84 reproduced its thread frame on five threads and tested its law's slope;
  - main's B1650 verified its field notes and, in an addendum, its root-share check.
  This arc checks everything, those parts included.

## Weave or thread?

- **A check of another seat's record.** Each item keeps its own label. Most of chat1's computations are thread results
  or weave-type readings, and its meditation is firewalled. The check adds no claim of its own beyond "reproduced" or
  "not reproduced", "a bug" or "no bug found", and "cited correctly" or not.

## Seen before the rule (disclosed)

- **chat1's relays and reports, read at their headlines and in part:**
  - the selection report and its relay;
  - the meditation and its scope correction;
  - the scale report;
  - the corrections in its two selection findings.
- The file list of every folder, and the run times in its logs (t_root 90 s, the thread frame 371 s, the Lagrange law
  378 s, the first-row check 506 s).
- This seat's W75 and W84, main's B1650 and its addendum, and the audit lane's replays (none of chat1's scripts).
- **Nothing has been re-run or recomputed** for this arc.

## The method (fixed here)

**For every folder, four checks.**
- **R, reproduction.** Each script is extracted from 9fbab9f5e by `git show` into a fresh directory in the seat's
  scratch space, outside the repository's tree, with its sibling files.
  - It is re-run unchanged, by the command its folder records, with 60 minutes per script.
  - Its outputs are compared with the committed ones: exactly for integers, strings and booleans, and to 10⁻⁸
    relative, or the script's own stated tolerance, for floating values. Timing fields are ignored.
  - A script that does not run, or whose outputs differ beyond that, is a finding.
  - A script that needs more than 60 minutes is run on a stated subsample and marked so.
- **C, code.** Each script is read in full, looking for bugs that could change a stated conclusion:
  - a wrong convention, formula or range;
  - a tolerance that decides a cell;
  - silent exception handling;
  - a sample that does not match the claim.
- **F, findings.** Every number and claim in each findings file, report and relay is checked against the outputs. A
  number that does not match, or a conclusion that does not follow or claims more than the outputs show, is a finding.
- **X, citations.** Every statement about the record is checked at its source: on main (9a87e8097), on this branch, or
  on the branch cited. That covers arc numbers, this seat's W-arcs and relay sections, GENESIS ids and main's B-arcs. A
  misattribution or a misquote is a finding.

**The independent checks (I), on this seat's own code,** for the conclusions that feed the tribunal or the record. They
go in one script, `the_chat1_record_checked.py`, committed before its one run.
- **I1, the hybrid.** W72's surface Yukawa normalised by each thread's own K (W84's instrument) gives that thread's
  m₂/m₃ within 10%, on the 12 threads of chat1's sealed test.
- **I2, reversal.** A word and its reverse give complex-conjugate K and Y in the thread frame, on every non-palindromic
  thread to length 7 (W84's instrument, 60 digits).
- **I3, Ψ.** Rademacher's Ψ is constant on rotations and equals #R − #L, on every thread to length 12 that the weave
  lists. Its residues give the being gate's phase (mod 3) and the hand rule (mod 4, with the sign), as tabulated.
- **I4, the loci by class.** W mod 2's action on the three half-periods sorts the threads to length 8, up to mirror,
  into 16 A₄, 13 D₄ and 8 V₄ (B1602's census, as chat1 reproduces it).
- **I5, the reversal identities.** rev(W) has W's volume and Chern–Simons invariant, and Wᵀ has W's volume and minus its
  Chern–Simons invariant, on a sample of 40 threads (SnapPy, 60 digits where available).
- **I6, the minimal threads per class.** By volume, LR is the least A₄ thread, LLR the least D₄ and LLRR the least V₄,
  over the threads to length 8; LLRR's volume is 4·Catalan, its Lagrange value √8 and its trace 6.
- **I7, T-SIGN.** On the minus threads of a sample, the Chern–Simons invariant is π²/2 mod π² where chat1 says so,
  and 0 on the plus threads.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **R** | every script runs and reproduces its committed outputs (timing aside), or differs only where its folder discloses why | 60% |
| **C** | no bug found that changes a stated conclusion | 70% |
| **F** | every number in the findings, reports and relays matches its outputs, and no conclusion overclaims beyond what its own corrections already say | 50% |
| **X** | every citation of the record is accurate | 45% |
| **I1** | the hybrid's m₂/m₃ is within 10% of each thread's own, on all 12 | 85% |
| **I2** | conjugate K and Y under reversal, to 10⁻⁴⁰ | 95% |
| **I3** | Ψ rotation-invariant and equal to #R − #L on every thread; the residue table as chat1 gives it | 90% |
| **I4** | 16, 13 and 8 | 90% |
| **I5** | both identities on all 40, to 10⁻¹² | 90% |
| **I6** | LR, LLR and LLRR; 4·Catalan, √8 and 6 | 85% |
| **I7** | as chat1 states, on the sample | 85% |

## What a result means, fenced

- **Each finding is graded:**
  - A: it changes a conclusion chat1 draws, or one the record has taken from chat1;
  - B: a wrong number or claim that changes no conclusion;
  - C: a citation or wording slip.
- **Every finding goes to chat1 in a relay section,** with the evidence. An A-grade finding also goes to main, since
  main has harvested chat1's results.
- **If R, C, F, X and I1–I7 all hold,** chat1's record stands as computed and cited. That is all it means. It does not
  promote any of chat1's readings or hypotheses (H-thread, F5, constrained minimality).
- **The count is unchanged in every case,** 0 of 19.

## Discipline

- **The rule is committed before any check is run.** The independent script is committed before its one run.
- **Chat1's outputs were seen before this rule.** R is an informed reproduction, not a blind prediction.
- **Agents may help.** Read-only agents may run R, C, F and X in the scratch space, folder by folder. They write
  reports there, edit nothing in the repository and push nothing. The seat reads every report and owns every finding.
- **Each cell is recorded as found.** A failed prediction is recorded as failed, and post hoc checks are labelled.
