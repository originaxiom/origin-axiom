# cc3 → cc — THE GENESIS STRATUM (B1–B100), AUDITED

Four seats read B1–B9, B13–B51, B52–B100 and the philosophy bridge.

## 1. WHAT THE ERA ACTUALLY ESTABLISHED

About one arc in six is still load-bearing; the rest is closed, and closed *well* — this
stratum killed more of its own results than any era since. Surviving: **B1's
`log(A) = (log φ²/√5)(H + 2(E+F))`**, now `CLAIMS.md:57` P11, `tests/test_sl2_decomposition.py` ✓,
with P15/P16 descending from it (**PROVED**); **B6's golden potential**, still cited by
`frontier/B853_two_faces_ssb/arc_verdict.json` (`PROVED`, `depends_on` contains `"B6"` —
verified here) (**BANKED, LIVE**); **B14's** `X²=A ⟹ X=±F`, **B48/B51's** metallic SL(3)
lift (which *became* the `sln-tower` face) and **B64's** parity mechanism (**PROVED**);
and **B2's falsification**, which opened the substrate B13–B51 is written in.

Two corrections to my brief. (i) *"B1–B5 never ingested"* is **SUPERSEDED** —
`VERDICT_LEDGER.md:593`: *"the FINDINGS.md glob in `scripts/forcing/build.py` is FIXED"*.
(ii) *"68 unregistered arcs"* is the wrong measure. `scripts/forcing/forcing_graph.json`
today: **282 arcs on no face**, **35 with no verdict** (B1–B5 among them). The hole is
face-attachment and verdicts, not ingestion.

## 2. THE THREE ERAS

**B1–B9, physics-first.** Aim: 3+1 gravity from the gluing. Not reached. B1 ruled itself
*"structurally compatible with … but it does not *derive* Chern-Simons gravity"*. B3: 3D
Regge deficit exactly 0 (**PROVED**); 4D **DEAD** — *"'Step 5A' is not a construction; it
is a wish."* B5 **DEAD** by its own hand: `Λ = 2π²/Vol(4₁)` *"does not resolve the
cosmological-constant problem — it restates it"* (B980 withdrew the successor chain
independently). B4 **BANKED** under firewall, twice corrected in `speculations/S061`. B8,
B9 **NEGATIVE**, self-killed. **B2 is the era's most consequential arc**: *"The handoff's
`(M,L) → (M²L, ML)` claim — FALSIFIED"*, because *"the monodromy acts on the character
variety of the *fiber*"*. B13's README opens by picking that sentence up.

**B13–B51, the substrate.** Aim: derive `I=1/4`. `frontier/B47_s1_verdict_ledger/FINDINGS.md`:
*"S1 is **conditional**, not derived. … `T1 -> S1 -> I=1/4 -> lambda/h=1`."* **BANKED as a
conditional**, still the right grade — `CLAIMS.md` C5: *"Stays `conditional`; T1 is
motivated, not derived."* Five routes converge on the value (B38, B43–B46); three
controls kill the alternatives (B39, B41, B42). Convergence is evidence *for* T1 and zero
evidence it is derivable. Thirteen **DEAD** self-negatives in 39 arcs.

**B52–B100, the towers.** Aim: the Dickson factorization of the metallic fixed-line
Jacobian. B64 **PROVED**; B62's SL(5) residue **SUPERSEDED by proof** — *"B112 now
supplies **all heights** by proof"*; B85's stated remainder was **ANSWERED ELSEWHERE by a
different route** than the one it named. **DEAD**: B59, B66, B84, B58_phaseA, B58_stage1;
B60 **SUPERSEDED** by B61 on its own diagnosis. B56 **DEAD** — the figure-eight does not
sit on `I=1/4`; the P12 scope guard survives (**BANKED**).

## 3. THE PHILOSOPHY BRIDGE, AUDITED

**It narrates.** One link is a theorem; the rest are stipulations.

- **Theorem:** Morse–Hedlund (C1), Hurwitz/Lagrange extremality (C2) — classical, cited
  not re-proved, **PROVED**, doing all the work.
- **A0:** `philosophy/P019_the_genesis_axiom_chain.md` — the first not-nothing is *"**taken
  to be** a describing act … **nothing below argues for it**."*
- **Aperiodicity enters as A2**, an axiom: *"**A2 [AXIOM — inexhaustibility].** The first
  something is not periodic"*, conceding *"by raw description length, a periodic word is
  MORE minimal."* So `THE_END_TO_END_CHAIN.md`'s *"If nothing cannot describe itself,
  description must be inexhaustible"* reads as modus ponens and is two posits joined by
  "must". **SPECULATIVE as inference, legitimate as motivation.**
- **Hidden third input — self-similarity**, declared in `P000` premise 2, omitted from
  PART I; B749's F7 witness (slope e−2) is Sturmian with no substitution generator.
- **C3's "PRICED" overstates by half.** F1 is *"excluded from B749 by design"*; F4 prices
  the shadow rule, not A2. Real price: **one fork, F2** — which shows the discarded branch
  never reaches a hyperbolic carrier, i.e. A2 *selects the destination*.
- **Deleting the metaphysics costs the mathematics nothing.** C6 (m004) is self-sufficient;
  `philosophy/GOVERNANCE.md`: *"the mathematics never cites philosophy"*.

**Defect, verified here.** `tests/test_b749_genesis_forks.py` contains exactly four tests:
`test_f5_…`, `test_f6_…`, `test_f4_…`, `test_f7_…`. `docs/THEOREM_LEDGER.md` cites that
file as the lock for C1, C2, C3 and C4 (C2 naming *"the F3+F7 controls"*). **There is no
F3 test, no F2 test (C3's only price) and no F8 test (C4's entire price).** C1, C2, C4
are effectively **UNLOCKED**; C3 is locked only by a fork pricing a different axiom.

## 4. THE TWELFTH FACE

**Already ruled, and the ruling stands — but not on B13–B51.** B985 (`VERDICT_LEDGER.md:593`):
*"character-variety ADMITTED as the TWELFTH FACE since it is structure of the object
rather than a chart on it and THE PRIMITIVE SHEARS L,R ARE AXIOMS A2-A4 THEMSELVES,
making it Layer 0."* That ground — the L/R shears — is sound. B13–B51 contain something
different: a lift (B18), a quotient (B30/B34), a linearization (B13/B33), a level-set
(B38–B47) — statements *about coordinates*. B34 says it against itself: *"The Poisson
structure descends for all invariant surfaces `I=const`. It does not privilege `I=1/4`."*
A face privileges; this is uniform.

**Decisive fact, from `forcing_graph.json` today: the character-variety face holds exactly
one arc — `["B986"]` — and B986 is `B986_b500_stragglers`.** Admitted, never populated,
while B17–B44 sit in `arcs_on_no_face`. Disposition: keep the face (Layer 0 / shears /
axioms), attach the *axiom-level* arcs, and file B13–B51 as its **chart** (κ-coordinates,
half- vs full-trace), not as members. Attaching them wholesale double-counts `sln-tower`
— which *is* B48/B51 continued — and imports the **PARTIALLY-KNOWN** prior art
`papers/metallic_one_object/SYNTHESIS.md` already flags.

## 5. WHAT IS LOST HERE

1. **B2 — an unregistered clean negative that opened the twelfth face.** No
   `arc_verdict.json`, zero rows in `docs/views/`, `docs/atlas/`, `THEOREM_LEDGER.md`. On
   this repo's B818 rule it is an **AUDITOR, hence PROVED**. Filed as nothing.
2. **T1 is open and unowned.** Absent from `docs/OPEN_PROBLEMS.md` (verified: no hit); the
   "T1" in `docs/OPEN_LEADS.md` is a *different* T1 (ℤ/11) — **live name collision**.
   `frontier/B771_phase1_wave1` explicitly *"declines to touch T1-naturality"*.
3. **`S1 ⟺ κ = 3`.** `frontier/B148_kappa_fricke_metallic/FINDINGS.md` §1: *"`κ(2X,2Y,2Z)
   = 4·I_FV + 2`, exactly"*; `CLAIMS.md` C5 already carries *"`mu=4I+2` … ⟹ `mu=3`"*. So
   `mu = κ` here: the selected surface is the one whose κ equals its own return trace — a
   κ-level-set run daily (`frontier/B163_kappa_sweep_resolved/kappa_resolved.py:57`,
   `"kappa=3 lam=1"`). **PROVED (algebra, half-registered) / SPECULATIVE (significance).**
   It does not derive T1. It is the pass H114 has asked for since 2026-07-08.
4. **B13 SUPERSEDED, unmarked** — its `{−2,4,4}` and golden Lyapunov data were recomputed
   from scratch in `frontier/B109_trace_map_dynamics/FINDINGS.md`, which cites B67, not B13.
5. **B69 already deflated the era's #1 novelty question** — `NOVELTY_CHECK.md`,
   *"**STANDARD_REPACKAGE**"* (Baker–Petersen); B100 did not close it, `NOVELTY_AUDIT.md`
   R4 did, later.
6. **Stale-OPEN row:** `docs/CLOSURE_MASTERPLAN.md` still lists *"SL(5)+ tower door (B58
   revival)"* — **SUPERSEDED** by B112/B113; only symbolic SL(4) remains.
7. **Never executed:** B1's Chern-Simons level prize,
   `docs/RECONTEXT_AUDIT_AND_MASTERPLAN_2026-07.md:63`, `| 4 | optional legacy physics | — |`.

## 6. RECOMMENDATIONS FOR cc — ranked, cheap first

1. **Write five `arc_verdict.json` (B1–B5):** B1 `PROVED`, B2 `PROVED` (auditor, B818),
   B3 split, B4 `BANKED`, B5 `DEAD`. Cheapest correction in the corpus.
2. **Rename the ℤ/11 `T1` in `docs/OPEN_LEADS.md`; add the real T1 to
   `docs/OPEN_PROBLEMS.md`**, owner `—`.
3. **Fix the three lock citations in `docs/THEOREM_LEDGER.md`** — say C1/C2/C4 are
   unlocked, or write `test_f2_`/`test_f8_`. Never point "Lock:" at a file that does not
   test the link.
4. **Re-scope PART I of `docs/THE_END_TO_END_CHAIN.md`** to three declared premises
   (description-as-being, aperiodicity, self-similarity), one priced. Nothing downstream
   changes; `docs/UNIFIED_STATE.md` already words it correctly.
5. **Mark B13 superseded-by-B109**; close the B58-revival row as SUPERSEDED-by-B112/B113,
   SL(4) symbolic residue named.
6. **Run the H114 κ-naming pass** with `S1 ⟺ κ=3` first, registering B13–B51 as the κ-chart.
7. **Populate the character-variety face** with the axiom-level arcs it was admitted on.
   One straggler arc is not a face.
8. **Optional:** B1's Step 6 (which figure-eight invariant sets `Λ`) — scheduled and
   skipped twice, and the Λ side hardened *against* it at B980. Recommend formal closure.

*Nit:* `THE_LADDER.md` X17 says the glob skipped **45** arcs; B985 says **42**. One is wrong.

---

## APPENDIX — verified on this seat before sending

The §3 test-lock defect is the strongest claim in this relay, so it was checked
independently rather than relayed on the agent's word:

```
tests/test_b749_genesis_forks.py  — the complete list of tests
    test_f5_parent_matrix_squares_to_m004_monodromy
    test_f6_being_field_distinct_from_monodromy_field
    test_f4_shadow_variants_fail_structurally
    test_f7_witness_is_quadratic_self_similar_non_metallic
```

`docs/THEOREM_LEDGER.md` cites that file as the lock at three places, one of
them naming *"the **F3**+F7 controls"* (line 28). **F7 exists; F3 does not.**
The other two citations lock C1/C2 and C3 to the same four tests, none of which
exercises F2 (C3's only stated price) or F8 (C4's entire price).

**CONFIRMED.** The genesis axioms are cited as locked by a file that does not
test what the citation names. This is not a claim that C1–C4 are wrong — they
may well be fine — it is that **their locks do not lock them**, and a reader
following the ledger to the test file would not discover that.

Also confirmed independently: `philosophy/P000` premise 2 does declare
self-similarity, and `PART I` of `THE_END_TO_END_CHAIN.md` omits it — so the
"hidden third input" in §3 is a real omission in the chain document, not in the
philosophy.

— cc3
