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
| **B139-G** | **Does the chirality block survive the genus ladder?** — Item 1's chirality block (B139/P009) rests on the mirror being a *simple R↔L relabeling that preserves the trace* (`M → Mᵀ`), special to **genus-1** (once-punctured torus ↔ SL(2,ℤ), two generators). At **genus ≥ 2** the MCG is richer than SL(2,ℤ), the mirror may **not** be a relabeling. | MATH | ★★ | **ANSWERED (B140) — genus-general, the block survives.** The genus-1 `M→Mᵀ` is a genus-1 *mechanism*, but the **conclusion** is the standard **orientation-reversal theorem** (genus-independent): the mirror has same volume, opposite CS, conjugate-isomorphic trace field. Confirmed genus-1 bundles + chiral knots (vol same / CS opposite); the genus-2 CS numeric is theorem-backed (twister/Sage absent in-sandbox). The firewall is *stronger* than the genus-1 argument implied. Residual caveat = the general "no *cleverer* invariant" hedge (not genus). |
| **s776/SU(3)** | "The Borromean rings (`s776`) show SU(3) gauge enhancement (SL(2,ℂ) char-variety dim 2 = rank SU(3))". | MATH (emergent shadow) | — | **DEAD (B142) — tombstone K-I.** Three kills: misidentified manifold (s776 = magic manifold ℚ(√−7), not the Borromean rings L6a4 ℚ(i)); structure ≠ gauge (Thurston dim = #cusps = 3, and SL(2,ℂ) ≠ SU(3), MB10); outside the forced chain (not ℚ(√−3)). The genuine non-abelian thread needs **SL(3,ℂ)** CS (S033-adjacent, tool-gated; Sage now available). |
| **L9** | Silver (m=2) ↔ the L5a1 selection criterion. | MATH | — | **BANKED** — handled in B132 S6 (the m=2 selection comparison). Do not re-run. |
| **L13** | Whitehead link / "Gate-1" (cusp-swap = Weyl reflection → a simple non-abelian factor), tool-gated on Sage/GKLP. | MATH (emergent shadow) | ★ | **BANKED as `../speculations/S033`** (firewalled, prior LOW, tool-gated). |
| **L4** | "Chiral fragility" — the k=4 partition-function vanishing read as a chirality signature ("symmetric vacuum = ground state"). | — | — | **WITHDRAWN (B133)** — refuted by control: achiral words `RRLRLL`,`RLRRLL` also vanish at k=4; the vanishing is **word-composition driven, not chirality**. Do not revive. See `../speculations/TOMBSTONES.md` K-H + guard MB6. |
| **L1–L3** | m=1 selection criteria (pure-phase, `Z=ω`, eigenvalue-order field). | — | — | **BANKED** — `../knowledge/K016`. Do not re-run. |
| **L12** | "Chirality shifts the eigenvalue arithmetic." | — | — | **WITHDRAWN** — tombstone K-H, guard MB6 (the field content is the SU(2)_k quantum-group twist, present in achiral words). |

## The campaign roadmap (B143 — see `STRATEGIC_SYNTHESIS.md`)

The three-voice strategic synthesis (CC + Chat-1 + Chat-2) is banked in **`STRATEGIC_SYNTHESIS.md`** (two-tier:
math program / labeled POSTULATED aspiration). It sets the governing roadmap:

- **Campaign 1 — chirality of interactions (the bottleneck).** Does a cusp-glued composite of two distinct seeds have
  an orientation-*independent* invariant distinguishing it from its mirror (chirality-(ii), the real wall)?
  **Venue verdict (B143):** the algebraic (trace) venue is **mirror-blind** (rigorous, B139/B140) — it carries the
  κ-landscape, not chirality. Chirality-(ii) needs the **topological venue** (closed JSJ composite → **install
  Regina**) or a **2-cusped hyperbolic-link realization** (construction open). ⟹ **B144.**
- **Campaign 2 — ground or demote the cusp↔gauge dictionary** (cheap part done: MB11 + the synthesis tiers; heavy part
  = compute `T[M]` for one metallic bundle, optional).
- **Campaign 3 — S031a full-locus** (symbolic elimination, Singular; when idle).

## Standing open threads (B142 inventory — lose nothing)

The bigger open *prizes/threads* (distinct from the per-lead catalog above), with status and cleanest next step:

| thread | status | cleanest next step |
|---|---|---|
| **S031a full-locus** (φ-fixed entirely reducible at SL(n)) | principal stratum **RIGOROUS** (B142 Klein-4); full locus **CONJECTURE** | **symbolic elimination** of the φ-fixed system `A g⁻¹ A g = g A g⁻¹` (B=g⁻¹Ag), 0-dim (det=−1 ⟹ isolated); the `A~B~AB` (char `x³−sx²+px−1`) reduction cuts it. **Same machinery as the SL(4) route — do together.** Sage/Singular now available. |
| **B85** — functorial `Sym(W) → trace-ring` wall | standing MATH prize, untouched | the honest proof-work target. |
| **S032-A** — no-forced-choice *theorem*-version | OPEN | prove **no** invariant whatsoever (not just trace-ring) is discretely-multivalued-and-unsymmetric. |
| **S033** — Gate-1 / Whitehead cusp-swap → SU(2)? | tool-gated, prior LOW | **now tied to MB10:** any SU(N) enhancement needs the **SL(N,ℂ)** CS data (`T_N[M]`), not SL(2,ℂ) dimension-matching. Sage/GKLP now available. |
| **K011 GHH-iff** | optional/pending | promote the Goodman–Heard–Hodgson "iff" from K011's parenthetical to a status line (the chirality recursion's load-bearing dependency). |
| **Genus-2 CS numeric** (B140 soft spot) | optional, low priority | retriangulate + re-run the genus-2 twister `complex_volume` (it returned None); the orientation-reversal theorem is the load-bearing content. |

## Note on the CHAT-1 doc's §E guard numbering

The CHAT-1 doc's §E used "MB7" for the *"a generic/necessary feature is not discriminating — check the null
case"* guard. That **collides** with the repo's existing MB7 (`../REPRODUCIBILITY.md` = "filter the reducible
locus before counting escapes", B137). The §E guard has therefore been banked as **MB8**, not MB7. (A *second*,
distinct guard — "a non-abelian *group* is not non-abelian *gauge* content" — is queued in a later handoff and
will be **MB9**.) See `../REPRODUCIBILITY.md`.
