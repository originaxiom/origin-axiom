# Open leads — the live, unrun catalog (MATH tier)

A registry of **open leads**: directions named but not yet run, ranked by value and tractability. This is a
*pointer file*, not a results file — nothing here is a claim, nothing promotes to `../CLAIMS.md`. Each lead is a
candidate for a future frontier stage; banking one means *deciding to run it*, not asserting it.

Provenance: the bulk of this catalog was extracted from the **CHAT-1 LEADS REGISTER** (a cross-session triage of
~23 quantum-layer threads). Only the **non-duplicate, non-stale** leads are carried here; the cross-check against
the repo is recorded in the "disposition" column so duplicates are not re-run and withdrawn items are not revived.

## How to read this

- **Status:** `OPEN` (unrun, registrable) · `BANKED` (already done elsewhere — do not re-run, see ref) ·
  `WITHDRAWN` (refuted/stale — do not revive, see tombstone/correction).
- **Value:** subjective ranking of payoff if it closes (`★★★` = a real generalization / theorem; `★★` = a useful
  extension; `★` = a probe).
- A lead going `OPEN → frontier stage` should cite its CHAT-1 `L#` tag for traceability.

## The catalog

| tag | lead | tier | value | status / disposition |
|---|---|---|---|---|
| **L6** | **Non-metallic sealing** — does the S031 sealing (trace map fixes only the `Sym^{n−1}` image; fixed-point traces stay in the SL(2) trace field) hold for **general once-punctured-torus-bundle words**, not just the metallic `R^mL^m`? The genuine generalization of S031. | MATH | ★★★ | **OPEN** — highest-value continuation of `../speculations/S031`. Needs the same SL(3) trace-coordinate machinery (Lawton); SL(2) sub-case may be reachable now. |
| **L5** | **General-word sealing, SL(3) first pass** — the concrete SL(3) entry point to L6: run the B137-style off-sublocus search for a few non-metallic words and check `K`-sealing among irreducible fixed points (MB7 guard applies). | MATH | ★★ | **OPEN** — the tractable scout for L6; reuses the B129/B137 pipeline. |
| **L7** | **One-theorem capstone** — fold S031 (sealing) + S032-A (no-forced-choice) + the chirality recursion (B134/K011) into a single structural statement about the metallic mapping class on the character variety. | MATH | ★★★ | **OPEN** — a synthesis target, not a new computation; gated on at least one of S031/S032-A closing. |
| **L8** | **Chiral compositions** — for composite (concatenated-block) words, how do chirality (B128/B134) and the eigenvalue field content (B132/K016, corrected) interact across the composition? Distinct from S032-B's boundary gluing — this is word concatenation. | MATH | ★★ | **OPEN** — bounded by the B134 chirality recursion; field content is composition-driven (B133). |
| **L10** | **Classical field-fusion** — is there a *classical* (trace-ring) analogue of the SU(2)_k quantum-group field content (B132/K015)? I.e. does the classical trace field of a composite word fuse from its blocks' fields the way the quantum eigenvalue field does (mod-4 twist)? | MATH | ★★ | **OPEN** — classical trace fields stay disjoint (ℚ(√−3)∩ℚ(i)=ℚ, B125/B129), so a naïve fusion is likely **negative**; worth a clean control. |
| **L11** | **Rank-2 covers** — examine finite (rank-2) covers of the metallic bundles and whether the sealing / field content lifts predictably to the cover. | MATH | ★ | **OPEN** — exploratory; SnapPy `covers()` is the entry point. |
| **B139-G** | **Does the chirality block survive the genus ladder?** — Item 1's chirality block (B139/P009) rests on the mirror being a *simple R↔L relabeling that preserves the trace* (`M → Mᵀ`), special to **genus-1** (once-punctured torus ↔ SL(2,ℤ), two generators). At **genus ≥ 2** the MCG is richer than SL(2,ℤ), the mirror may **not** be a relabeling, and B131 already shows the free invariant **discretizes** on the genus ladder — so genus ≥ 2 is the one place the chirality firewall might have a genuine gap (a bundle and its mirror genuinely inequivalent, not just opposite-CS). | MATH | ★★ | **OPEN** — the **falsifier for B139 Item 1**; trace-level first pass (no Sage); either outcome informative. Scope: even a break gives **emergent** chirality, not the SM's fundamental chirality. |
| **L9** | Silver (m=2) ↔ the L5a1 selection criterion. | MATH | — | **BANKED** — handled in B132 S6 (the m=2 selection comparison). Do not re-run. |
| **L13** | Whitehead link / "Gate-1" (cusp-swap = Weyl reflection → a simple non-abelian factor), tool-gated on Sage/GKLP. | MATH (emergent shadow) | ★ | **BANKED as `../speculations/S033`** (firewalled, prior LOW, tool-gated). |
| **L4** | "Chiral fragility" — the k=4 partition-function vanishing read as a chirality signature ("symmetric vacuum = ground state"). | — | — | **WITHDRAWN (B133)** — refuted by control: achiral words `RRLRLL`,`RLRRLL` also vanish at k=4; the vanishing is **word-composition driven, not chirality**. Do not revive. See `../speculations/TOMBSTONES.md` K-H + guard MB6. |
| **L1–L3** | m=1 selection criteria (pure-phase, `Z=ω`, eigenvalue-order field). | — | — | **BANKED** — `../knowledge/K016`. Do not re-run. |
| **L12** | "Chirality shifts the eigenvalue arithmetic." | — | — | **WITHDRAWN** — tombstone K-H, guard MB6 (the field content is the SU(2)_k quantum-group twist, present in achiral words). |

## Note on the CHAT-1 doc's §E guard numbering

The CHAT-1 doc's §E used "MB7" for the *"a generic/necessary feature is not discriminating — check the null
case"* guard. That **collides** with the repo's existing MB7 (`../REPRODUCIBILITY.md` = "filter the reducible
locus before counting escapes", B137). The §E guard has therefore been banked as **MB8**, not MB7. (A *second*,
distinct guard — "a non-abelian *group* is not non-abelian *gauge* content" — is queued in a later handoff and
will be **MB9**.) See `../REPRODUCIBILITY.md`.
