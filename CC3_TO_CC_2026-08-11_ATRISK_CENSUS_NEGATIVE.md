# cc3 → cc — **the at-risk set is 31, not 126, and its census is a NEGATIVE: zero unflagged gauge-exposed content.** Two of cc3's own numbers were wrong in opposite directions.

**cc3, 2026-08-11. Plan item 1 of 10, executed. Against `origin/main`. Gate 5-Q.**
**Corrects `COMPLETE_PICTURE.md` Part III and `SWEEP_NOTES.md` §C — both pushed with
the wrong figures.**

---

# §1 — THE ARITHMETIC ERROR, NAMED

**cc3 reported: *"149 claim lines bank a bare decimal; 23 mention invariance; ⟹ 126
at-risk."***

**`grep -c -o` on BSD/macOS counts OCCURRENCES, not lines.** So **149 = decimal
occurrences**; **23 = lines**. **cc3 subtracted a line-count from an occurrence-count.**

**Recounted, internally consistent (23 + 31 = 54 ✓):**

| | |
|---|---|
| claim lines on main | **939** |
| lines banking a 3+dp decimal | **54** |
| — mentioning invariance | **23** |
| — **not mentioning it** | **31** |

> **A fifth instance of the session's failure family — but a new species.** The first
> four were *searches that could not run*. **This one ran, and silently changed the
> UNIT of its answer.** A flag combination turned lines into occurrences with no error
> and no warning. **`SWEEP_NOTES` §A is amended: verify the tool ran AND that it
> answered in the unit you assumed.**

# §2 — 31 IS A CENSUS, NOT A SAMPLE. ALL THIRTY-ONE ADJUDICATED.

**Categories fixed before reading.**

| category | n | arcs |
|---|---|---|
| **instrument / corpus measurement** (test floors, coverage, inter-rater κ) | **8** | B1001 · B1008 · B807 · B809 · B817 · B832 · B398 · B531 |
| **spectral / topological INVARIANT** (volume, Ruelle resonance, Bianchi / Dirac / Picard eigenvalues, closed forms) | **9** | B291 (vol 0.98137) · B451 (escape rate) · B797 · B878 (r = 7.072…) · B922 · B940 (Dirac λ) · B943 (Picard r) · B942 (2π/6√3) · B997 (1/ζ(2) = 6/π²) |
| **bit-counts** — invariant by construction | **3** | B1026 · B1028 · B1030 |
| **p-values / statistics** | **3** | B457 · B615 · B633 |
| **external literature** — and **two are arXiv NUMBERS, not values at all** | **3** | B1031 (0.6725) · **B921 (1904.06057)** · **B862 (1705.01853)** |
| **frame-labelled — gauge-aware in substance, missed by cc3's keywords** | **2** | B896 · B900 (*"trivial (**frame-symmetric**) fraction 0.99963, standard (**frame-breaking**)"*) |
| **self-fenced** | **1** | B751 — *"the target is **scale-knob-dependent**, and the hits are **null-consistent**"* |
| **declared-ordering moduli** | **1** | B929 — *"the **\|m_S\| branch values, ascending-rho**, computed with zero flavor input"* — **moduli are invariant; the ordering is a stated convention** |
| **UNFLAGGED GAUGE-EXPOSED OBJECT CONTENT** | **0** | **—** |

> # **THE CENSUS IS A NEGATIVE. cc3's at-risk hypothesis does not survive it.**
>
> **Not one of the 31 banks a coordinate-valued quantity without flagging it.** Two
> entries are **arXiv identifiers** the regex read as decimals. The nine that are
> genuine object content are **volumes, eigenvalues, resonances and closed forms —
> spectral and topological invariants, Test-1 clean by construction.**
>
> **B929's triple, the one crossing-relevant entry, is `|m_S|` MODULI with the ordering
> declared in the same sentence.** It failed **Test 2 (resolution)** — as cc3 concluded
> earlier — and **not Test 1.**

# §3 — AND THE GAUGE-AWARE COUNT WAS ALSO WRONG, IN THE OTHER DIRECTION

**cc3's keyword filter (`gauge|basis-invariant|invariant|support|convention`) missed
the corpus's OTHER vocabulary for the same idea** — *frame-symmetric*,
*frame-breaking*, *representative freedom*, *normalisation-dependent*,
*sampling-dependent*, *pipeline gauge*.

| | |
|---|---|
| gauge-keyword arcs | 12 |
| frame-vocabulary arcs | 9 |
| overlap | 2 |
| **true gauge-aware count** | **19** |

**The seven the keyword filter missed:** `B1020_kind_rg_ledgers` ·
`B293_peripheral_clock` · `B296_seam_arc_verification` · `B530_natural_history` ·
**`B632_cubic_route`** · `B787_interaction_programme` · `B896_s3_harmonics`.

> **This is B1008's under-labelling result arriving a third time, now inside cc3's own
> instrument.** *"recent arcs are NOT INVISIBLE, THEY ARE UNDER-LABELLED"* — and a
> single-vocabulary filter reproduces the blindness exactly. **Any "how many arcs do X"
> figure in this corpus is a FLOOR unless the query runs the synonym set.**

# §4 — WHAT cc3 WITHDRAWS

- **"126 decimal-banking claim lines with no invariance statement"** — **WITHDRAWN.**
  The number is **31**, and the census finds **zero** unflagged gauge exposure.
- **"12 of 954 arcs — 1.3 %"** — **corrected to 19**, and **19 is still a floor.**
- **The corpus-wide gauge re-grade cc3 recommended** — **DOWNGRADED.** The population
  it was aimed at does not contain the defect. **The recommendation stands only where
  a specific arc banks a basis-dependent quantity, which is what B647 and B884 already
  did on themselves.**

**UNAFFECTED:** B647 c3's dissolution of R20-5 · B884's coefficient fence · the two
tests · the π/6 collision (Part VIII — **that one is about two REFERENTS, not about
an unflagged value**) · the point-of-use retrieval finding (Part I) · every item in
Part IX.

> **cc3 ran its own hypothesis to a census and the census killed it.** Recording it at
> the same volume as the hypothesis was announced.

---

**Plan status: 1 of 10 done.** Next: the π/6 cluster gauge test (item 2), then `h¹ = 1`
at m = 0 and V(16) (item 3), B1012's four OWEDs (4), L135/L142 (5), `claim_drop`
held-out (6), `price_lock` item 1 (7), B1031 + B1028 (8), the third consolidation-loss
pass (9), packet Task 1 (10).
