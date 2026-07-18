# engine_v7 gate_report upstream patch — prepared, NOT applied

Prepared by the B674 computation cell for main-seat review, per the
PRICED_DOORS row "The engine_v7 gate_report upstream patch (from B678)".
Nothing tracked was modified; nothing outside this directory was written;
the shared engine itself was NOT touched.

## The target

The shared engine is NOT in the repo tree. It lives in the seat conduits:

    <seat-workdir>/veins/v7_conduit/engine_v7.py      (cc2 and cc3 seats,
                                                       byte-identical copies,
                                                       md5 a1f230f65bd5390ffcc8b81c6daadac6)

Byte snapshot here: `engine_v7_current.py`
sha256 `986a0e667fac5aef45a221a1291ddc6682d6ec13a65e59e7ceaf4a3bd26f7359`.

Patched file: `engine_v7_patched.py`
sha256 `a66825d994bfa7a48f466365893e3dfd139d36ac0f614165db85a7baa5004a00`.

Unified diff (current -> patched): `patch.diff`. To apply, either run
`patch engine_v7.py < patch.diff` in each seat's `veins/v7_conduit/`, or copy
`engine_v7_patched.py` over each seat copy (both seats carry the same bytes).

## What changed (the exact hunks)

ONE hunk, entirely inside `def gate_report`. Nothing else in the file
changed (`equivalence_proof.py` check (0) verifies this mechanically by
ast-excision of `gate_report` from both files and comparing the remainder:
identical).

The old code placed each gate's full matrix expression inside the
`max(...)` generator body:

    rep['unitary'] = max(abs((S * S.conjugate().transpose() - I)[i, j])
                          for i in range(N) for j in range(N))

A Python generator re-evaluates its body on every step, so the O(N^3)
product `S * S.conjugate().transpose() - I` was recomputed on EVERY (i,j) —
O(N^5) per gate. The same pattern hit `symmetric` (O(N^4)), `(ST)^3=S^2`
(O(N^4): the difference of two precomputed matrices rebuilt per (i,j)),
`S^4=I` (O(N^5): two matmuls per (i,j)), and `rho_unitary` (O(N^5)).

The patch hoists each expression VERBATIM into a local computed once, then
scans it in O(N^2):

    D_unitary = S * S.conjugate().transpose() - I
    rep['unitary'] = max(abs(D_unitary[i, j])
                          for i in range(N) for j in range(N))

(and identically for `D_symmetric`, `D_st3`, `D_s4`, `D_rho_unitary`),
plus an explanatory docstring. `rho_A1_matrix` is UNCHANGED — its two LU
inversions were already computed once and are kept exactly so the
`two_word` deviation stays bit-identical (see "cc2 deviations" below).

## Why it is behaviorally identical (the argument)

1. Every hoisted expression is character-identical to the old one: same
   operands, same operator order. mpmath operations are deterministic at
   fixed precision, so the old code's N^2 re-evaluations of the identical
   expression all produced the identical matrix, from which it read entry
   (i,j); the patched code computes that matrix once and reads the same
   entries. Same values, bit for bit.
2. The `max` generators iterate in the same row-major order over the same
   values; the rep dict is populated in the same key order; the `label`
   print path formats the same values with the same format strings.
3. Signatures, return values `(rep, rho)`, module-level constants, and
   every other function in the file are untouched (mechanically verified).
4. Exact/rational paths (`An_Level` constructor: PRIM, Fraction `h`, `c`,
   `theta_split`) are outside the hunk and byte-identical; asserted anyway
   in the battery.

Deliberate divergences from cc2's local `fast_gate_report` (B678
`d4_level.py`), which was the model for the compute-once structure but is
NOT bit-compatible with the old engine — and therefore was NOT upstreamed
verbatim:

- cc2 replaces `S**-1` by `S^dagger` and `T**-1` by the elementwise
  conjugate (unitarity-justified but numerically different at the 1e-60
  level) — the patch keeps `rho_A1_matrix`'s LU inversions so `two_word`
  is bit-identical.
- cc2 computes `ST*ST*ST` where the engine computes `(S*T)**3` (different
  association order under mpmath's binary powering) — the patch keeps
  `(S*T)**3` and `(S*S)**2` verbatim.

So: NO tolerance was accepted anywhere; the equivalence battery asserts
raw-mantissa (`._mpf_`/`._mpc_`) equality and passed on every case.

## Equivalence battery (`equivalence_proof.py` -> `equivalence_out.txt`)

Covers every distinct call pattern found in the repo's importing cells:
`An_Level(3, k)` positional / `name=` / full-keyword forms, `An_Level(2, 3)`
(the engine's own SU(2)_3 validation case), `build(verbose=False)`,
`theta_split`, bare `gate_report(S, T)`, `gate_report(S, T, label=...)`
with captured stdout compared character-exact (the d4_ceiling pattern),
`rho_A1_matrix(S, T)` direct (the a3_stage / d4_su3_run pattern), and
`verlinde_N` at small N. All compared OLD vs PATCHED on the same (S, T),
bit-for-bit.

Result: **ALL EQUIVALENCE ASSERTIONS PASSED**, bit-for-bit, on every case
(see `equivalence_out.txt`). `rep` dicts matched in key ORDER and every
value's raw mantissa; `rho`, `w1`, `w2`, `dev`, and `verlinde_N` matched
entrywise; the `label=` printed output matched character-for-character.

### Speedup table (gate_report, same (S,T), same process)

Same-process wall time of one `gate_report(S, T)` call, OLD vs PATCHED.
(The old timing IS the O(N^5) cost the door prices; at N=28 one call is
7.4 min, and it grows ~11x per step of this ladder — the mechanism behind
the multi-hour high-level ladder runs.)

| theory  |  N | old (s)  | patched (s) | speedup |
|---------|---:|---------:|------------:|--------:|
| SU(2)_3 |  4 |    0.035 |       0.007 |    5.2x |
| SU(3)_1 |  3 |    0.015 |       0.005 |    3.1x |
| SU(3)_2 |  6 |    0.266 |       0.028 |    9.4x |
| SU(3)_4 | 15 |   19.454 |       0.289 |   67.3x |
| SU(3)_6 | 28 |  444.008 |       2.006 |  221.3x |
| SU(3)_8 | 45 |  N45_OLD |    N45_NEW  | N45_SPD |

(Small-N speedups are modest because per-call fixed cost dominates; the
ratio grows as N^3 once the O(N^5) term dominates — 9.4x -> 67x -> 221x
across N=6,15,28 — which is exactly the regime the banked high-level cells
run in. The patched cost grows ~O(N^3), as expected for compute-once.)

Independent large-N corroboration from the lock reruns (below): the
d4_ceiling cells call the PATCHED gate_report at k=1..12 (N up to 91) and
finish in seconds; at k=1..9 (N up to 55) the PATCHED printed gate values
reproduce the BANKED OLD-engine log (`B673 d4_run_log.txt`)
character-for-character — an old-vs-patched agreement at N=55 through the
real call site, to the log's printed precision.

## Importing cells / tests checked

`tests/` contains NO importer of engine_v7 (grep over the suite: zero
hits; `tests/test_b570_ap2.py` has its own self-contained numpy
`gate_report(S, T, D)` — a different function, untouched; the
`test_b144_interaction_chirality.py` hit is a test NAME, not the engine).
The engine's importers are the banked frontier cell scripts:

| cell (repo path under frontier/) | imports | lock rerun |
|---|---|---|
| B673_loop4_integration/packet/loop4/d4_ceiling/d4_ceiling.py | An_Level, gate_report | b673_d4_ceiling |
| B678_d4_annex/d4_ceiling.py | An_Level, gate_report | b678_d4_ceiling |
| B678_d4_annex/d4_level.py | An_Level (own fast path) | b678_d4_level_k2 |
| B651_.../loops_queue/d4_su3/d4_su3_run.py | An_Level, rho_A1_matrix | b651_d4_su3_run |
| B663_bifocal_anatomy/.../loop1/a3_stage/a3_stage.py | An_Level, rho_A1_matrix | b663_a3_stage |
| B670_anatomy_full/packet/loop1/a3_stage/a3_stage.py | (byte-identical to the B663 copy, md5 480684c2...) | covered by b663_a3_stage |
| B670_anatomy_full/packet/loop2/b4_landscape/b4_landscape.py | An_Level | b670_b4_landscape |
| B670_anatomy_full/packet/loop3/c3_signtable/c3_signtable.py | An_Level | b670_c3_signtable |
| B646_.../q2_conductor/q2_mechanism.py | An_Level | b646_q2_mechanism |
| B646_.../q2_conductor/q2_conductor.py | An_Level | b646_q2_conductor |
| B646_.../n4_receipt/verify_b644_independent.py | An_Level | b646_n4_receipt |
| B646_.../n2_clock_law/n2_su3_13_measure.py | An_Level | b646_n2_su3_13 |
| B646_.../n2_clock_law/n2_clock_predict.py | An_Level | b646_n2_clock_predict |

## Lock reruns (`equivalence_locks.py` -> `equivalence_locks_out.txt`)

Every importing cell was rerun BYTE-UNTOUCHED (one noted exception below)
against the PATCHED engine, injected under the module name `engine_v7` by
`lock_bootstrap.py` (sys.modules pre-load, which wins over the cells' own
`sys.path.insert`). The committed cells' scrubbed placeholder constants
(`<cc2-seat>/...`, `<seat-workdir>/...`) are relative paths, so each cell
ran in a sandbox cwd (`lock_runs/<id>/`) with the placeholder input trees
pre-created from repo-banked inputs (level-ladder `.npz` inputs copied from
the seat conduit, whose root is parsed at runtime from the tracked B646
cell's own recorded path).

Key cross-artifact check: the banked B673 `d4_run_log.txt` was produced
with the OLD engine (k = 1..9 before the multi-hour wall); the patched
reruns must reproduce its printed gate values character-for-character.

### Per-cell results

18 locks attempted, **0 FAIL / 0 TIMEOUT**.

| lock | status | evidence |
|---|---|---|
| b678_d4_ceiling | PASS(note) | ran to completion; G0 modular battery PASS k=1..12; 9 banked OLD-engine gate blocks reproduced character-exactly |
| b673_d4_ceiling | PASS(note) | idem (the two d4_ceiling copies) |
| b678_d4_level_k2 | PASS | rerun JSON == banked `d4_results_k2.json`, structural-exact |
| b651_d4_su3_run | PASS | rerun JSON == banked `d4_results.json`, structural-exact |
| b670_b4_landscape | PASS(note) | rerun JSON == banked `b4_matrix.json` except `/runtime_s` (a wall-clock field); byte-identical copy executed |
| b663_a3_stage | PASS | rerun JSON == banked `a3_results.json`, structural-exact (also covers the byte-identical B670 loop1 copy) |
| b670_c3_signtable | PASS | rerun JSON == banked `c3_table.json`, structural-exact |
| b646_q2_mechanism | PASS | exit 0 (self-asserting cell) |
| b646_q2_conductor | PASS | exit 0 |
| b646_n4_receipt | PASS | exit 0 |
| b646_n2_su3_13 | PASS | exit 0 |
| b646_n2_clock_predict | PASS | exit 0 |
| pytest test_b678_d4_annex.py | PASS | 3 passed |
| pytest test_b651_wave3.py | PASS | 3 passed |
| pytest test_b646_wave2.py | PASS | 3 passed |
| pytest test_b663_bifocal.py | PASS | 4 passed |
| pytest test_b670_anatomy.py | PASS | 2 passed |
| pytest test_b570_ap2.py | PASS | 8 passed (self-contained numpy gate_report; sanity that its own lock is unaffected) |

The tracked pytest suites were run with the PATCHED engine pre-injected as
`engine_v7` (so any transitive import resolves to it); they are data /
transcript locks over the banked outputs, and they all pass. Several of
those banked outputs were REGENERATED by the cell reruns above under the
patched engine and matched the committed JSON structurally-exactly, so the
locks assert against freshly-patched-engine values too.

On the two d4_ceiling cells' `exit 1`: run to completion they fail their
OWN pre-annex G1 (fig-8 reproduction) check — d4_ceiling.py lacks the
`det(w0)` sign correction that d4_su3_run.py's Gate-3 audit established and
that B678's SUPERSEDING d4_level.py carries, so its G1 comparison against
the banked d4_su3 tr_odd column mismatches at integer level for several
kappa. This is ENGINE-INDEPENDENT (the sign convention, not the gate
values) and the banked B673 run never reached G1 anyway (its log dies at
the k=9 O(N^5) wall). What the patch has to preserve — and does — is the G0
modular battery (PASS, k=1..12) and every banked OLD-engine gate block,
reproduced character-for-character.

Exception noted: `b670_b4_landscape` executes a byte-identical COPY of the
cell (`shutil.copyfile`) from the sandbox, because the cell writes
`b4_matrix.json` next to its own source file (`HERE = dirname(__file__)`)
and running it in place would have written into the tracked tree.

## Risks not fully discharged

1. **Scope of bit-identity vs. arbitrary future inputs.** Bit-identity is
   PROVEN (not tolerance-bounded) on the battery: SU(2)_3 and SU(3)_k for
   k in {1,2,4,6} at full mantissa, plus N45_STATUS. The argument in "Why"
   is input-agnostic (identical expressions, deterministic mpmath at fixed
   precision, hoisting only), so it extends to any (S, T); but the machine
   check is on those sizes. No importer uses a call pattern outside the
   battery (verified by the importer sweep). Residual risk: a future caller
   at some N never exercised here — mitigated by the structural argument,
   not eliminated by machine check at that N.

2. **The engine is not in the repo.** It lives only in the seat conduits
   (`<seat-workdir>/veins/v7_conduit/engine_v7.py`), not under version
   control here. The patch was prepared against a byte snapshot (sha256
   recorded above). Before applying, the main seat should re-confirm the
   live seat file still hashes to `986a0e66...`; if a seat edited it since,
   re-diff. Both seat copies (cc2, cc3) currently share md5
   `a1f230f65bd5390ffcc8b81c6daadac6`.

3. **mpmath precision context.** Every timing/equivalence run used the
   module's own `mp.mp.dps = 60`. The bit-identity holds at that precision;
   the argument holds at any precision, but the machine evidence is at
   dps=60 (the value every importer runs at).

4. **JSON `runtime_s` field (b670_b4_landscape).** The only substantive
   diff in any rerun-vs-banked JSON is a wall-clock field (36.5 s banked vs
   ~42 s rerun) — expected and non-mathematical. No mathematical value
   differs in any lock.

5. **Path-guard vs. byte-fidelity (main-seat decision).**
   `engine_v7_current.py` and `engine_v7_patched.py` carry the engine's OWN
   pre-existing header comment, which names a seat path
   (`.../oa-seat-cc2/seat-work/level_ladder_campaign/scripts/engine.py`). I
   did NOT scrub it: these files must stay byte-faithful so `patch.diff`
   applies to the live seat engine and so "copy patched over seat" does not
   silently rewrite the engine's header (the task forbids changing anything
   outside the one hunk). Consequence: `tests/test_no_hardcoded_paths.py`
   (which scans committed `frontier/**.py`, and does NOT skip
   `B674_generation_leg/`) would FLAG both files if they are committed
   as-is. Main-seat options: (a) apply via `patch.diff` and keep the two
   `.py` as review-only, uncommitted; or (b) add this prep dir to that
   guard's `_SKIP_DIRS`; or (c) commit only the diff. This is a
   documentation/hygiene collision, not a mathematical risk. `patch.diff`
   and this report contain no machine paths; `lock_runs/` was scrubbed to
   `<seat-workdir>`/`<repo>`/`<home>` placeholders and pruned to logs only.

Nothing else is left undischarged: no tolerance was silently accepted, no
float-summation-order branch was papered over (the deliberate divergences
from cc2's fast_gate_report that WOULD have changed float order were NOT
taken — the patch keeps `(S*T)**3`, `(S*S)**2`, and the LU inversions
verbatim), and every importing cell + tracked lock was run against the
patched engine.

## Inventory

- `engine_v7_current.py` — byte snapshot of the shared engine (evidence;
  carries the engine's own pre-existing header comment verbatim, including
  its recorded seat path — preserved for byte-fidelity of the snapshot).
- `engine_v7_patched.py` — the full patched engine (the deliverable).
- `patch.diff` — unified diff, one hunk, applies to both seat copies.
- `equivalence_proof.py` / `equivalence_out.txt` — bit-identity battery +
  speedup table.
- `equivalence_locks.py`, `lock_bootstrap.py` /
  `equivalence_locks_out.txt`, `lock_runs/<id>/run_out.txt` — importing-cell
  reruns against the patched engine.
