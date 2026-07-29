All nine commits in `1ab53d3b..origin/main` read, plus cc3's branch-side originals for comparison. Findings below; paths are on `origin/main` unless marked "branch".

---

## Commit range (oldest → newest)

| commit | title |
|---|---|
| `4ba8d579` | B791 CORRECTIONS: sector-count factor error + 51.014 is unsourced |
| `5c716804` | **B791 RESOLUTION: 51.014 corroborated by cc3's solver; the multiplicity trap locked** ← *not on your list; extra, summarized in §7* |
| `1e907302` | B793 GATE 8R2-A sealed; the B788 V1 control is bracket-refinement, not detection |
| `024fcd3b` | B794 THEOREM (cc3 harvest): Gamma_41 is congruence of level (4) |
| `18b8c1e4` | B791 caveat: the Weyl budget is the LEADING TERM ONLY |
| `512a03a9` | B795: cc3's m004 Maass eigenvalues INDEPENDENTLY VERIFIED 7/7 |
| `9841c06b` | ERROR_LEDGER: E28–E32 |
| `d6aadf83` | B797: m004 Maass spectrum harvested |
| `cec8b099` | B797 addendum: sector call SETTLED — cc's advance prediction REFUTED |

Whole range: 35 files, +2473/−31. No CLAIMS.md change anywhere ("Nothing to CLAIMS" in all nine).

---

## 1. B793 — GATE 8R2-A sealed, and BLOCKED

`frontier/B793_gate8r2a_parent_localisation/{FINDINGS.md, GATE8R2A_PREREGISTRATION.md, bank_hash_baseline_{pre,post}.json, ARTIFACT_HASHES.txt}` (`1e907302`)

**What was sealed.** A *new* Stage-A gate, prereg sha256[0:16] = `d6b6f434206f5c18`, logged in `docs/SEAL_LEDGER.md`. Design origin: "Chat-1 relay 2026-07-28; arithmetic verified independently by cc." Verbatim gate text:

> **GATE 8R2-A.** Run the B788 V₁ solver on r ∈ [0.5, 7.6] at **two heights**. **PASS** if exactly one confirmed root is found, with both heights agreeing. **Record its value.** **No literature comparison. No window. No pass/fail on the value itself.**

Criterion basis: per-sector W = 0.002856530136 → 0.784 parent eigenvalues below r = 6.5, 1.254 below 7.6, so exactly one expected in [0.5, 7.6]. Three outcomes: PASS / FAIL-ZERO / FAIL-MANY (each with a disambiguation rule). "**Recording the root's value is mandatory; comparing it to anything is forbidden in Stage A.**"

**Why split.** GATE8R2's window ±0.005 = 0.0707 % vs a total Weyl spread of 0.14 % across four transcription slips (51.014→r 7.072058 IN; 51.00→7.071068 IN; 51.104→7.078418 OUT; 51.14→7.080960 OUT). "**The gate is over 40× tighter than its own corroboration**… a second-decimal slip **passes the Weyl check and fails the gate**, producing a **spurious FAIL that sends a seat hunting a solver defect that does not exist**." GATE8R2 (`012a29f8578c6036`) is **not amended** — it stays byte-frozen and becomes **Stage B**, which "waits on a primary-source read of Grunewald–Huntebrinker Table 3 and **blocks nothing**."

**"Bracket-refinement, not detection."** Found by reading `build_gate8_v1_control.py::search_configuration`: `minimize_scalar(..., bounds=interval, method="bounded")` with `"search_interval": ["24.50320","24.50340"]` — "a bounded scalar minimisation inside a 2×10⁻⁴-wide window centred on the literature value." Three consequences, in cc's order: (1) refinement not detection — "the window is supplied by the answer"; (2) `minimize_scalar(bounded)` **always returns a point**, "no 'no eigenvalue here' outcome"; (3) **it cannot count roots**, and root-counting is Stage A's whole PASS criterion — "**The criterion is not measurable by this instrument.**"

**Fair-to-the-bank paragraph.** Three genuine negative controls all pass (`displaced_parameter` 0.02, `outer_band_removal`, `perturbed_coefficient`), so "there is a sharp σ-minimum near r = 24.5033 and not at 24.5233." What it does *not* establish: Gate 8R's "10-digit agreement" is between two heights running bounded minimisation "over **the same supplied 2×10⁻⁴ window** … a **convergence** statement about an optimiser, not an independent localisation." "The solver has never demonstrated it can find an eigenvalue whose location it was not given." Hence "**parent-validated** … needs qualifying: validated by bracket-refinement, at **one** r, in a window taken from a **figure caption**." Bears on Gate 9, which must *find* V₅/V₆ eigenvalues at unknown locations.

**Custody protocol (evidenced).** Hashes **84 verified / 0 mismatches** before (`bank_hash_baseline_pre.json`), solver copied OUT, inspection only, **84/0 after — BANK UNMODIFIED** (`..._post.json`). "Step 4 converts 'I did not fork it' from an assertion into evidence." Copied solver not committed. Separate observation: the **10 unresolved hash entries are the bank's own lock tests** (`tests/test_b788_maass_*.py`), absent from the delivered zip — "the bank's *data* is verifiable; its *locks* are not."

**What the gate now requires — the three options, verbatim headings:**
- **(a) Convert the copy into a scanner.** Mesh σ_min over [0.5, 7.6], then confirm each dip. "Honest, and weaker as a bank validation."
- **(b) Accept cc3's B792 run as Stage A in a different frame.** cc3 mesh-scans (dr = 0.002), found one high-parent-weight root at r = 7.072004 in [6.4, 7.35]. "Methodologically this is **stronger** than the bank's control on precisely the axis at issue — it is a detection, not a refinement. It does not validate the bank's solver."
- **(c) Leave Stage A blocked** and bank the architectural finding — "which is what this arc does pending a decision."

Sequence item 3 (open): "Gate 9 re-run on the widened interval with W(T) as the completeness gate and a **budget-derived** screen cap replacing the hand-set `maximum_minima_per_sector = 24`."

---

## 2. B794 — Γ₄₁ is congruence of level (4) (cc3 harvest)

`frontier/B794_congruence_level4/{FINDINGS.md, verify_congruence.py, output.txt, results.json}`, `tests/test_b794_congruence.py`, `docs/LAW_MAP.md`, `docs/HINT_LEDGER.md` (`024fcd3b`)

**Provenance.** First line of FINDINGS: "**Provenance: both theorems are cc3's** (audit seat, its `1757d6d5`). cc3 never merges; per the standing rule they are re-derived here from scratch under a new number — `verify_congruence.py` takes nothing from cc3's script."

**The two theorems as banked (verbatim):**
> **THEOREM 1 (congruence).** Γ₄₁ is a **congruence subgroup of level exactly (4)**: Γ(4) ⊆ Γ₄₁, and Γ(2) ⊄ Γ₄₁.
> **THEOREM 2 (trace law).** For every γ ∈ Γ₄₁, **N(tr γ) ≡ 0 or 3 (mod 4)** — never 1. Hence every m004 geodesic trace norm avoids 1 mod 4, **at every cutoff**.

**Re-derivation, all steps reproduced** (`results.json`): |SL(2,ℤ[ω]/4)| = **3840**; |PSL| = **1920**; ⟨T,U,S⟩ mod 4 = 3840 (**surjective**); |H = ⟨A,B⟩ mod 4| = **320**, −I ∈ H, |H̄| = **160**; index **12** = [PSL(2,O₃):Γ₄₁] ⇒ Theorem 1; |H mod 2| = **10** (D₅ < A₅), index **6 ≠ 12** ⇒ level exactly (4); trace norms mod 4 = **{0, 3}** ⇒ Theorem 2. 2 is **inert**, residue field 𝔽₄, |ℤ[ω]/4| = 16.

**Strengthening/scope added by cc (not in cc3's statement):** the retroactive identification — "**B791's 1920 is not a coincidence — it *is* |PSL(2,ℤ[ω]/4)|.** The B788 bank's coset action is **reduction mod 4**: ambient 3840 = |SL₂(O/4)|, image 1920 = |PSL₂(O/4)|, kernel 2 = {±I}. cc verified that order from raw generators in B791 without knowing what it was; this identifies it." (cc3 states the same identification more briefly in its commit; cc's version also ties in the stabilizer.)

**Effect on cc's own claims:** B790's "not the principal congruence subgroup of level √−3" is **REFINED** ("still true — now visibly the weaker half"); B790's hint `H-B788-NORMSPLIT` ("m004-only norms are all ≡ 0 (mod 4)") is **REFUTED/RETRACTED** — "The odd norms cc3 found — 7, 103, 127, 175, 367 — are **all ≡ 3 (mod 4)**." cc's contrary re-verification is recorded as **an artifact**: "its ℤ[ω]-membership tolerance filter **silently discarding long geodesics** … **The filter selected for the author's expectation.**" 12 m004-only norms (cc) vs 41 (attributed to cc3).

**New error class registered** (→ E28): "**A filter that discards data must report its discards**, or it silently selects for the author's expectation. … Named by Chat-1 in relay; it earned its place by catching cc within the hour of being proposed."

**Ledger effects.** `LAW_MAP.md` row "**THE mod-4 TRACE LAW / Γ₄₁ CONGRUENCE THEOREM**", tier "**THEOREM (exact, computer-assisted)**", provenance "cc3 `1757d6d5`, re-derived independently in B794", lock `tests/test_b794_congruence.py`. `HINT_LEDGER` (7) **RETRACTED**; (8) opened as **H-B794-A5 (type HOOK)**: "the mod-2 image of Γ₄₁ is D₅ inside PSL(2,𝔽₄) ≅ A₅, and A₅ also carries B787's 5A/5B ambivalence argument. Two appearances of the smallest simple group is suggestive and NOT thereby a connection. Open cell: same A₅ or not?" 4 locks.

---

## 3. B795 — cc3's eigenvalues independently verified 7/7

`frontier/B795_eigenvalue_verification/{FINDINGS.md, collocation_verify.py, collocation_verify_hitrunc.py, output.txt}` (`512a03a9`)

**Method.** cc's own Hejhal/Then implementation, "written from the … method rather than from cc3's code. It shares **no source** with cc3's solver". cc's stated comparison table: cc3 height Y 0.75/0.62, modes 476–654, pullback words ≤5 |c|≤2.2, K_ir trapezoid, sample points 492–690 — vs cc Y 0.62, modes 112 then 322, words ≤4 dedup by matrix, points 336 then 805. Ingredients pre-checked: cusp shape τ = 2√−3 vs SnapPy to 1e-9; relator `w a = b w`, w = a b⁻¹ a⁻¹ b, exact — "the same word cc found by brute-force search in B789 — two seats, two routes, one word." **Discriminator: a displaced control at r ± 0.02**, not a bare dip.

**Banked result (7/7), σ_min / control / ratio:**

| r (cc3) | σ_min | control | ratio |
|---|---|---|---|
| 3.938916864 | 9.90e-05 | 2.96e-03 | **29.8×** |
| 4.900085373 | 2.53e-04 | 4.08e-03 | **16.2×** |
| 5.670720035 | 1.14e-03 | 4.78e-03 | **4.2×** |
| 5.912917882 | 5.68e-04 | 2.71e-03 | **4.8×** |
| 6.632802303 | 1.10e-03 | 4.07e-03 | **3.7×** |
| 7.072004187 | 7.82e-07 | 4.22e-05 | **54.0×** (high-trunc) |
| 8.863405356 | 3.91e-06 | 5.88e-05 | **15.1×** (high-trunc) |

Raw run log (`output.txt`) also records the *first*, low-truncation ratios at 7.072 and 8.863: **1.8×** and **1.0×**.

**The two cc errors, as recorded:**
1. **"The first run was VACUOUS."** 90 sample points against 112 modes: "a 90×112 matrix has nullity ≥ 22 *by construction*, so σ_min ≈ 1e-48 for **every** r including the controls. The test would have 'confirmed' any number fed to it. **Caught by the displacement controls** — every ratio came back ≈ 1, which is impossible for a working discriminator. Fixed by requiring npts ≫ modes."
2. **"Insufficient truncation was nearly misread as a negative."** At |μ| ≤ 3.2, Y = 0.62: Bessel argument 2π·3.2·0.62 ≈ 12.5 — margin 3.2× at r = 3.9 but only **1.4×** at r = 8.86. Ratios decayed 29.8 → 16.2 → 4.2 → 4.8 → 3.7 → 1.8 → 1.0 and the top two read as no dip. "**That was cc's instrument running out, not cc3's eigenvalues.**" Raising to |μ| ≤ 5.4 (margin 2.37×) restored 54× and 15.1×. "Had cc stopped at the first adequate-rank run, it would have reported cc3's upper eigenvalues as unverified — a **false negative manufactured by cc's own truncation**, and pointed at another seat's correct result."

**Scope section, verbatim key sentences:** "σ_min confirms an eigenvalue **exists** at a location. It says **nothing about sector**. cc had implied its collocation could adjudicate whether r = 8.863405 is the parent's second eigenvalue (V₁) or Γ₄₁-relative; **it cannot.** Only cc3's S-invariance test … can decide that. The prediction stands as a prediction; existence is now confirmed, sector is not." Open item registered against cc3: "the **mode-count certification** cc3 still owes (max |Δr| between mode counts), which sets the floor on every tolerance its SM comparison can honestly use." Standing lesson: "a confident, precise number produced by an instrument whose preconditions were unchecked" — commit message calls it the "seventh instance this session."

---

## 4. B797 — the official spectrum + SM null + sector call

`frontier/B797_maass_spectrum_harvest/{FINDINGS.md, SM_COMPARISON_PREREGISTRATION.md, eigenvalues_final.json, mode_count_certification.json, sm_comparison_results.json, sector_projection_results.json}`, `tests/test_b797_maass_harvest.py`, `docs/SEAL_LEDGER.md` (`d6aadf83` + `cec8b099`)

**Provenance/credit lines (verbatim):** "**Provenance: the computation is cc3's** (its B792). cc3 never merges; this arc harvests the certified artifacts into main with cc's gate record attached. cc's **independent** re-derivation of the eigenvalues is a separate arc, **B795** (7/7 confirmed on an instrument sharing no source)." Also: "**B790's Step-3 verdict — 'blocked, NEEDS-SPECIALIST' — is overturned by computation.** The literature has no Maass eigenvalues for m004; there are now seventeen." SEAL_LEDGER row credits "cc3's seal, hash re-verified BYTE-IDENTICAL on harvest". The mult-2 caveat is explicitly "**cc3's catch, not cc's**"; the sealing repair is "**fixed, better than specified**" / "a better repair than the 'late seal' cc asked for."

**The certified spectrum** — mode-count certified 664 → 900 modes (Bessel margins 21.0 → 27.0), **max |Δr| = 5.42×10⁻⁹**, Y = 0.75:

| n | r | λ = 1+r² | mult | n | r | λ = 1+r² | mult |
|---|---|---|---|---|---|---|---|
| 1 | 3.938916864 | 16.515066 | 2 | 10 | 7.857783263 | 62.744758 | 2 |
| 2 | 4.900085373 | 25.010837 | 1 | 11 | 8.308224803 | 70.026599 | 2 |
| 3 | 5.670720035 | 33.157066 | 2 | 12 | 8.863405356 | 79.559955 | 2 |
| 4 | 5.912917882 | 35.962598 | 1 | 13 | 9.027421524 | 82.494339 | 1 |
| 5 | 6.632802303 | 44.994066 | 2 | 14 | 9.047788231 | 82.862472 | 2 |
| 6 | **7.072004187** | **51.013243** | 1 | 15 | 9.080648624 | 83.458179 | 1 |
| 7 | 7.349526641 | 55.015542 | 2 | 16 | 9.640121030 | 93.931933 | 2 |
| 8 | 7.406615600 | 55.857955 | 1 | 17 | 9.837116218 | 97.768855 | 2 |
| 9 | 7.687671168 | 60.100288 | 1 | | | | |

n = 6 is the parent Bianchi ground state by direct S-invariance (S ∈ PSL(2,O₃)∖Γ₄₁, invariant to **7×10⁻¹⁰** vs order 1 for all others — "nine orders of separation"), and "**discharges the B791 provenance alert**": G–H λ₁ = 51.014 vs computed 51.013243, "agreeing to four significant figures with the fifth differing by one — exactly the caveat G–H attach to their own table."

**SM null.** Sealed prereg **`c6954bfa`**, byte-verified on harvest. Results: **Test 1 (direct) candidates 2, gated 0; Test 2 (ratios) candidates 39, gated 0; Test 3 (PSLQ) relations 0, gated 0.** "**The base-rate machinery is what makes this a result.** Test 2 threw 39 raw candidates, several λ-ratios clustering near δ_CP; the per-target surrogate null (p up to 0.962) killed every one. Without it this run yields a 'δ_CP discovery' with forty near-misses to choose from."

**Scoping language for the null — quoted in full:**
> **Verdict, as sealed:** no SM value among the 18 banked PDG targets is reachable from this spectral set at 8-digit precision under the stated base-rate control (n = 17, r ≤ 9.84). **This is a generic-spectrum null over a bounded window.** The deep-precision question (20+ digits) and the algebraicity question (50+ digits) remain **open and untested in both directions**.

> Note what the verdict deliberately does **not** say. An earlier draft read "the banked H0 — the object is valueless — stands at the spectral level." That was struck: B713–B716 are negatives about the character variety, the fibre-functor torsor and the algebraic tower — a different object — and importing them as the null for a *spectral* claim is the scope error cc committed in B790 and withdrew. **The null needs no borrowed authority.**

**Gate record — three of four closed (verbatim table):**

| item | status |
|---|---|
| scope-import sentence | **fixed** (verdict rewritten; amendment A3) |
| sealing | **fixed, better than specified** (dry-run demotion + seal before the certified run) |
| mode-count certification | **PASSES** — max|Δr| = 5.42e-9 |
| sector call on r = 8.863405 | **OPEN** *(settled in the addendum)* |

**Follow-ups / open items registered (verbatim):**
- "**Caveat on the certification margin.** τ_v = max(2·rel_unc_v, 1e-8). Against the typical τ_v ≈ 2e-5 the drift is ~4000× below — comfortable. Against the **floor of 1e-8 it is only 1.8× below**. … for the tightest-tolerance targets the eigenvalue uncertainty is 54 % of the tolerance. Adequate, not luxurious; **a future run at tighter τ must re-certify first**."
- Mult-2 blindness: "the generic-null-vector S-test **structurally cannot decide sector at multiplicity 2** … **Ten of the seventeen eigenvalues have multiplicity 2** (n = 1,3,5,7,10,11,12,14,16,17), so their OLD/NEW labels rest on an instrument blind to the question. The n = 6 identification is unaffected." Correct instrument (cc3's, then in progress): "minimises the S-invariance defect over the projective line of the 2-dim eigenspace via a generalised eigenproblem D c = μ N c … Until it runs, **sector labels above n = 6 are not merely provisional but unmeasured** wherever mult = 2."
- The open sector call itself (cc's advance prediction: W·r³ = 1.989 vs Weyl 8.8797, 0.18 %, neighbours 1.7–1.9 %; V₁ sub-budget 1.75 in [7.3, 10] vs cc3's zero).
- Deep-precision (20+ digits) and algebraicity (50+ digits) left "open and untested in both directions."

**The addendum (`cec8b099`) — sector call SETTLED.** cc3's projective-line minimisation, `controls_ok = True`, 36 pairs:

```
r = 7.072004187   dev_min = 3.53e-10   ->  PARENT (V1)
r = 8.863405356   dev_min = 1.080      ->  no parent component
(all other 15: dev_min 0.83 - 1.20     ->  no parent component)
```

"**Exactly one parent eigenvalue in the certified window** … **cc's advance prediction that r = 8.863405 is the parent's k = 2 eigenvalue is REFUTED.**" cc's error is named against itself: "When cc3's λ = 51.013243 corroborated the secondary-sourced G–H value, cc argued that a **0.344 %** Weyl agreement was *too weak to verify anything* ('suspiciously good… consistent with fabrication'). cc then used a **0.18 %** Weyl agreement as the basis for a positive prediction about sector. **Both cannot be right.**" Classified **E4a**, an *instance* not a new class; standing rule: "**Weyl/asymptotic proximity is necessary-ish, never sufficient — the discriminating test must be computed**" (`docs/ERROR_LEDGER.md` E4a row). "**Not a counting failure.** The V₁ budget over [3.9, 9.84] expects **2.55** parent eigenvalues and one was found: z = −0.97, inside the PASS band … The prediction failed on **sector**, not on census."

**Final Standing block (verbatim):** "Existence and values: **certified and independently verified** (B795). Sector labelling: **SETTLED for all 17** … exactly one parent (n = 6), sixteen Γ₄₁-relative. cc's r = 8.863405 prediction REFUTED. SM null: **sealed, scoped, and provisional only on the open sector call**, which does not enter it."

**Does B797 register anything cc3 must still do?** Only implicitly: the certification-margin re-certification requirement if τ tightens, and (in the pre-addendum text) the projective-line run, since discharged. No open item is assigned to cc3 by name in the harvest text; B795 was where cc booked cc3's outstanding debt ("cc3 still owes the mode-count certification"), and B797 records it as PASSED. Atlas status for B797 is `"dormant"`.

---

## 5. B791 — the corrected Weyl-budget instrument and its limits

`frontier/B791_weyl_completeness/FINDINGS.md` (+`sector_count_correction.py`, `PROVENANCE_ALERT.md`), `tests/test_b791_weyl.py` (`4ba8d579`, `5c716804`, `18b8c1e4`)

**What the corrected instrument now claims.** The banked criterion, restated with units made "explicit and unavoidable" (§5b):

> **μ_s = dim(V_s) · W · (b³ − a³)** counts eigenvalues **WITH MULTIPLICITY**.
> The observed quantity **n_s must therefore be Σ multiplicities**, never the number of distinct confirmed parameters. If a run cannot resolve multiplicity, the criterion **does not apply** — it does not become a distinct-count test with a different constant.
> z = (n_s − μ_s)/√μ_s, PASS |z| ≤ 2, on confirmed counts only, declared before confirmation.

Plus: "A completeness gate whose two sides are counted in different units is worse than no gate: it produces confident, precise, wrong verdicts in whichever direction the mismatch happens to point." W = Vol(PSL(2,O₃)\H³)/(6π²) = **0.002856530136**; consistency check Σ_i dim(V_i)·W = 12·W = Vol(m004)/(6π²), "Verified exactly."

**Corrections commit (`4ba8d579`) content.** (1) Factor error: ranks 1, 5, 6, "Weyl on a rank-m flat bundle gives m*W(T) eigenvalues, generically SIMPLE: E_i has irreducible holonomy, and the degree-12 cover is NON-REGULAR (image 1920, point stabiliser 160), so no deck group forces a dim(V_i)-fold degeneracy." "Chat-1's derivation divided the with-multiplicity count by a multiplicity that is not there; cc verified the resulting arithmetic table without checking the derivation behind it. The error **HID AT V1**, where dim=1 and both readings agree." Discriminator = the bank's own data: Gate 9's screen retained V5=25, V6=24 against cap 24; corrected predictions 24.7 and 29.6 vs Chat-1's 4.9. **Consequence: "Chat-1's headline 'live defect' EVAPORATES"** — Gate 5's 10-per-sector needs r = 8.88 (V5) / 8.36 (V6), both inside Gate 9's sealed [0.5, 12]; "no widening to 15.5, no 2.03x cost, no re-preregistration. The real bug is the hand-set `maximum_minima_per_sector = 24`." Applied to cc3's B792 scan: 4 stable dips below r = 5.913 vs corrected expectation 7.09, z = −1.16 PASS ("uncorrected it would be z = +1.67, the opposite side — the factor decides the verdict"). Locks in `tests/test_b791_weyl.py` were replaced: `test_gate9_cannot_discharge_gate5` → `test_gate9_CAN_discharge_gate5_under_the_corrected_counting` + `test_sector_counts_carry_the_dim_factor`.

(2) **51.014 unsourced.** "GATE8R2 MUST NOT EXECUTE." Primary paywalled; value entered via a subagent "ASSERTING it had 'obtained and read the full PDF'"; the 0.344 % Weyl agreement "WITHDRAWN AS EVIDENCE … suspiciously good and is exactly what a model would generate from the obvious Weyl estimate. It is consistent with fabrication, not evidence against it." cc3 alerted mid-scan; r = 7.0721 demoted control → hypothesis. Lesson: "an agent's claim to have read a source is not evidence the source was read."

**Caveat commit (`18b8c1e4`) — the stated limits.** FINDINGS §7: "The budget μ_s = dim(V_s)·W·(b³−a³) is the **leading Weyl term only**." Elstrodt–Grunewald–Mennicke form quoted, φ(s) = Λ(s−1)/Λ(s), Λ(s) = (√3/2π)^s Γ(s) ζ_K(s), K = ℚ(√−3) (attributed: "cc3's B792 cell"). Scattering term computed independently by cc:

| T | main = 12·W·T³ | scattering term | ratio |
|---|---|---|---|
| 3.00 | 0.926 | −0.318 | −34 % |
| **7.35** | **13.611** | **−0.091** | **−0.7 %** |
| 12.0 | 59.233 | +1.600 | +2.7 % |

"At T = 7.35 … the correction moves the expectation by 0.09 and the z-score from −1.25 to ≈ −1.23. **The verdict (PASS) is unchanged**."

Limits, verbatim: "**What this check does NOT cover** … only the scattering-determinant term was computed. The **cusp terms are O(T log T)**, and at T = 7.35, T·log T ≈ 14.7 — potentially *larger* than the scattering piece just bounded. They are not estimated here, and cc3's cell absorbs them into a residual, which it correctly describes as a consistency check rather than a derivation." And: "μ carries an unquantified O(T log T) uncertainty at small T. That is tolerable for a **±2σ screen against silently skipped eigenvalues**, which is what the gate is for, and it is *not* tolerable for anything finer — **the budget must not be used to adjudicate a count difference of order one, nor quoted as an exact expectation.** The gate was banked in §2 without this caveat; the caveat is added rather than the gate withdrawn, since every verdict issued so far survives it."

**Also banked in B791** (unchanged by the corrections): the independent structure verification of the bank (image order 1920, transitive on 12 cosets, commutant dim 3, orbitals [12,12,120], ⟨χ,χ⟩=3, τ central/fpf/τ²=1, ρ = V₁⊕V₅⊕V₆ parities +,+,−; "**The decomposition is forced, not fitted**"), the §5 replication/scheduling-defect note about cc3's `89fc6794`, and "**Status of the door: unlocked, unopened.**"

---

## 6. ERROR_LEDGER `9841c06b` — E28–E32 (five new classes, all cc's own)

`docs/ERROR_LEDGER.md` lines 52–58. Quoted, class name + mechanism + rule + instance:

- **E28 — Silent-discard filter.** "a tolerance/membership filter that drops data **without reporting what it dropped**. Because the dropped items are systematically the hard cases (long geodesics, large norms, poorly-conditioned rows), the filter selects for the author's expectation and manufactures self-vindication." Rule: "**a filter that discards data must report its discards** — count them, report the worst discarded case, and treat a large discard fraction as a failed run, not a clean one." Instance: "**cc's own instance (B794, 2026-07-28)**: cc's ℤ[ω]-membership filter (tol 1e-7) silently dropped long geodesics while re-checking cc's OWN hint H-B788-NORMSPLIT; it returned 12 m004-only norms against cc3's 41, 'upholding' the claim. The dropped geodesics carried exactly the disconfirming odd norms (7,103,127,175,367). cc3's proved mod-4 theorem settled it against cc. Class named by Chat-1 in relay; **it caught cc within the hour of being proposed**."
- **E29 — Post-hoc analysis-model selection.** "multiple defensible analysis models (nulls, surrogates, tolerances, windows) exist; the one reported is chosen **after seeing outcomes**, and typically the most permissive. The individual computation is correct; the verdict is chosen." Rule: "the pre-registered model is the primary and is named in the prereg; any additional model is reported **alongside** it, never in place of it, with both numbers shown." Instance: "**cc's own instance (B790, 2026-07-28)**: prereg §2 named the density-matched null as primary; cc reported 'ordinary noise' off a **uniform** null that was never pre-registered. Compounding: cc's 'Weyl-matched' null was itself miscoded (e^ℓ instead of e^{2ℓ}), so **neither** reported model was the committed one. Caught by Chat-1. Corrected verdict (pool-matched, two models agreeing) still MISS, but earned."
- **E30 — Output-verified, derivation-unverified.** "a result's *numbers* are independently reproduced and the result is then called verified — while the *argument* that produced them is never checked. Every table row can be right and the premise still wrong." Rule: "verification names which layer it reached: numbers, derivation, or both. Reproducing a table is not checking its derivation, and a receipt must say which it did." Instance: "**cc's own instance (B791, 2026-07-28)**: cc re-derived all eight rows of Chat-1's Weyl budget from the L-value and confirmed them exactly — while the derivation behind them divided out a multiplicity that is not there. The arithmetic was right; N_i(T) = dim(V_i)·W(T), not W(T). Consequence: Chat-1's headline 'Gate 9 cannot discharge Gate 5' evaporated once the factor was restored."
- **E31 — Instrument-precondition unchecked.** "a measuring instrument returns a confident, precise number while a *validity condition* of the instrument is unmet — matrix rank, truncation margin, grid resolution, convergence radius. The number is not wrong so much as meaningless." Rule: "before trusting an instrument, assert its preconditions **in code**: overdetermination (rows ≫ cols), truncation margin vs the scale being probed, and a **displaced negative control** that must FAIL." Instance: "**cc's own instances ×2 (B795, 2026-07-28)**: (a) collocation run at 90 points × 112 modes — nullity ≥ 22 by construction, σ_min ≈ 1e-48 for every r *including controls*; would have 'confirmed' any input. (b) Bessel truncation margin 1.4× at r = 8.86 (needs ≳ 2×); the top two eigenvalues read as ABSENT. **Stopping one run earlier would have published a false negative aimed at another seat's correct result.** Both caught by the displacement controls, not by care."
- **E32 — Unfalsifiable premise (local rigour, global immunity).** "every *cell* carries a pre-registered falsifier and the *campaign premise* carries none. Each cell can fail correctly while the premise survives untouched ('we haven't found the right mechanism yet'). A programme can run to completion, produce nothing, and leave its premise as 'banked' as on day one." Rule: "a campaign states a **campaign-level** falsifier distinguishing its premise from the null-of-no-connection; if none can be written, the campaign is labelled **exploratory-interpretive** and nothing from it banks as *evidence for* the premise — only as mechanism-exclusions." Instance: "**B796 coupling campaign (2026-07-28, gated pre-launch)**: premise written as 'H0 (banked, now the campaign's **positive target**): values live in the observer–object coupling', justified by the refutation of values-in-the-object. **Refuting the rival does not establish the premise** — every banked null (character variety, rung-1 PSLQ, forced limits, B792 spectral) is predicted *identically* by H2 = 'the object has nothing to do with the SM', which the plan never states. Per-cell falsifiers were added and do **not** fix this."

**Session note appended:** "E28–E32 all arose in one session, all from cc, and all share one shape: **a confident, precise output whose preconditions were unchecked** … Of seven instances, **cc self-caught two**; the rest were caught by cc3, by Chat-1, or by a control built for another purpose. The operative lesson is not 'be careful' — it is that **controls built for one purpose catch errors of another**."

Note E32 is the only one aimed at cc3's live work (B796) — it is the sole *forward* obligation cc's ledger places on the audit seat: a campaign-level falsifier, or the campaign is relabelled exploratory-interpretive.

---

## 7. Extra not on your list — `5c716804` B791 RESOLUTION

`frontier/B791_weyl_completeness/PROVENANCE_ALERT.md` (RESOLUTION section) + FINDINGS §5b + `tests/test_b791_weyl.py`.

- **51.014 CORROBORATED by cc3's solver.** r = 7.072004187, λ = 51.013243 vs 51.014: "|Δλ| = 7.57e-04 → agreement to FOUR significant figures, the FIFTH differing by exactly 1." With mean spacing ≈ 0.482 in r, "P(a fabricated value landing this close…) ≈ 2.2e-04 — roughly **4500 : 1** in favour of the value being genuine." "**'Possibly model-fabricated' — WITHDRAWN.**" "**GATE8R2 — UNBLOCKED**", but explicitly "*not* thereby discharged: cc3 validated the **value**, in a different frame; GATE8R2's purpose is to validate the **B788 bank's V₁ solver**… that still requires running the bank's own code." "the **primary is still unread**, and the search window was supplied by cc, so this is **targeted corroboration rather than blind confirmation**."
- **Self-assessment:** right to refuse the subagent's PDF claim, right to refuse the 0.344 % agreement as verification, right to alert cc3 mid-scan; **over-escalated**: "the word **'fabricated'**, asserted before the one experiment that could settle it had reported… **An unverified input is not thereby a false one**, and stating otherwise is the mirror image of the credulity the alert was written against."
- **Consequence banked:** "The parent ground state is now a **validated, in-sandbox-reproducible control**: any m004 solver must find λ = 51.0132 at r = 7.0720, and nothing below it can be inherited."
- **The multiplicity trap locked** (as in §5 above), and **cc3's B792 result GATED, not banked** at that point: "cc3's OLD/NEW labels are WRONG — it marks r=3.939 (lam 16.5) and r=4.900 (lam 25.0) as parent, but lambda=51.01 IS the parent ground state… the V1 budget expects 1.13 in range against cc3's 4 (z=+2.69 FAIL-HIGH). Its O3star_weight is not a valid discriminator. Held pending a second MODE COUNT."

---

# DELTAS vs cc3's branch records

Branch = `audit/b775-braver-questions` (cc3). Its corresponding arc is the single `frontier/B792_maass_m004_eigenvalues` (commits `41c37d7f`, `10c2ed74`, `1757d6d5`, `f85c7577`, `87d7f270`) plus the relay `CC3_TO_CC_2026-07-28_gate_items_closed_and_prediction_decided.md`.

**Artifacts that are byte-identical** (verified by diff): `eigenvalues_final.json`, `mode_count_certification.json`, `sm_comparison_results.json`, `sector_projection_results.json`, `SM_COMPARISON_PREREGISTRATION.md`. So all 17 eigenvalues, multiplicities, dev_min values and SM candidate lists agree exactly. The deltas are in numbering, framing, scope, derived numbers and open-item lists.

1. **Numbering.** cc split cc3's one B792 arc into four main-side arcs: **B793** (gate), **B794** (theorems), **B795** (verification), **B797** (harvest). cc3 correspondingly renumbered its own coupling campaign **B793 → B796** ("B793-B795 yours", relay §6; branch `87d7f270`). cc's E32 already indexes it as "B796 coupling campaign", i.e. cc's ledger presupposes cc3's renumber. No B793/B794/B795/B797 directory exists on cc3's branch; no B792 directory exists on main.

2. **B794 norm counts — cc's figures are not reproducible from cc3's banked artifact.** cc banks "cc's filter returned **12** m004-only norms against **cc3's 41**" with "the odd norms cc3 found — **7, 103, 127, 175, 367**" (FINDINGS L41, `output.txt` L41/L45, `verify_congruence.py` L98, and **locked** in `tests/test_b794_congruence.py::test_cc_mod4_hint_is_refuted_by_the_theorem`, L88). cc3's banked `trace_norm_split.json`/`.txt` at cutoff 6.0 says: m004-only = **139 traces / 37 distinct norms**, mod-4 classes [0,3], with **exactly one odd norm, 7** ("norm 7: traces 3+w, 2−w"). **103, 127, 175, 367 are in cc3's *shared* set** (231 traces / 68 distinct norms), not the m004-only set. So (a) "41" appears nowhere on cc3's branch, and (b) cc's sentence conflates *m004-only* norms with *all m004* norms — a distinction cc3 keeps sharp (its third law is "ALL m004 trace norms avoid 1 mod 4"). The refutation of `H-B788-NORMSPLIT` is unaffected (norm 7 alone refutes it), but the ledgered instance figures for E28 are off.

3. **B794 scope: the m003 half is absent from cc's version.** cc3 banks three laws — m004-only ∈ {0,3}, **m003-only ≡ 1 (mod 4) exactly** (which it flags as "sharper than B790's 'odd'"), and all-m004 ∈ {0,3} — and explicitly scopes the m003 statement as **observational, not a theorem** ("m003's holonomy is not ⟨A,B⟩", FINDINGS Theorems block). cc's B794 mentions **m003 zero times** (grep-verified across B794/B795/B797). cc3's open remainder "m003-side congruence half" (`f85c7577`) is registered in no cc open-item list.

4. **B794 A₅: cc downgrades cc3's claim to a hook.** cc3 states it assertively — "A₅ = PSL(2,F₄) with dihedral D₅ image — **B787's 5A/5B ambivalence structure lives at the mod-2 level of Γ₄₁**" (branch FINDINGS; `1757d6d5`: "the A5/D5 = 5A/5B structure of B787 sits at mod 2"). cc banks it as **HINT (8) H-B794-A5, type HOOK**: "Two appearances of the smallest simple group is suggestive and **NOT thereby a connection**. Open cell: same A₅ or not?" That is a deliberate scope reduction of cc3's wording.

5. **B795's description of cc3's instrument does not match cc3's record.** cc's comparison table gives cc3 "mode count **476 – 654**" and "sample points **492 – 690**". cc3's FINDINGS says two-system refinement at **Y = 0.75 (516 modes / 705 pts)** and **Y = 0.62 (774 modes / 1044 pts, different seed)**, and certification at **664 → 900 modes**. None of cc's three ranges matches. (Everything else in the table — heights, word length ≤5, |c| ≤ 2.2 — does match.)

6. **The certification-margin caveat: cc's "1.8×" vs cc3's "14.5×-equivalent".** cc's B797 writes "τ_v = max(2·rel_unc_v, 1e-8)" and concludes "against the **floor of 1e-8 it is only 1.8× below** … the eigenvalue uncertainty is **54 % of the tolerance**" — locked as `assert 1.5 < 1e-8 / c["max_dr"] < 2.5` in `tests/test_b797_maass_harvest.py`. Two mismatches with cc3's record: (a) cc's quotation **drops the third term of amendment A2**, which in the byte-identical sealed prereg reads `tau_v = max(2 * rel_unc_v, 1e-8, 10 * max_rel_dr)`; (b) cc compares the **absolute** max|Δr| = 5.42e-9 (in r) against a **relative** tolerance floor of 1e-8. cc3's certified run header and relay report the relative figure: "A2: **max_rel_dr = 6.90e-10** → tolerance floor 6.90e-09" and "the honest tau floor is 6.9e-9 — **subsumed by the protocol's 1e-8**" (relay §1(ii)). On cc3's units the margin is ~14.5×, not 1.8×; cc's caveat is the conservative direction but is stated as fact and is locked in a test.

7. **cc harvested cc3's *dry-run* SM artifact as the official record.** cc3 states: "The first run is retained as a labeled **dry-run** (`sm_comparison_results.*`)" (branch FINDINGS, process note); its certified-run output is `sm_comparison_certified.txt`, which carries the A1/A2 header lines ("A1: certified set — 17 kept, excluded []", "A2: max_rel_dr = 6.90e-10 → tolerance floor 6.90e-09"). cc's B797 harvested `sm_comparison_results.json` (byte-identical to cc3's dry-run json) and did **not** harvest `sm_comparison_certified.txt`; `tests/test_b797_maass_harvest.py::test_sm_comparison_is_a_clean_null_...` reads that file as the certified record. Candidate lists and verdicts are identical between the two runs, so nothing material changes — but main's only SM evidence file is the one cc3 labels dry-run, and the certification header (the thing that makes A1/A2 auditable) is not in main.

8. **Census window and the k=2 statement.** cc's addendum: "the V₁ budget over **[3.9, 9.84]** expects **2.55** parent eigenvalues and one was found — **z = −0.97**, inside the PASS band, consistent with the **~79 % recovery**". cc3 uses the upper window: "the V₁ budget deficit in **[7.3, 10]** (expected **1.75**, observed 0, **z = −1.32**) stands as a fluctuation" — and adds the positive claim cc does not carry: "**the parent's k=2 eigenvalue lies above r = 10**". cc's B797 pre-addendum text does quote cc3's 1.75/[7.3,10] figure; the addendum silently switches window and z.

9. **SM verdict wording — converged, but the branch commit log still carries the struck sentence.** cc3's *current* FINDINGS uses cc's replacement wording verbatim ("no SM value is reachable … GENERIC-SPECTRUM null … B713–B716 as **context**, NOT as the hypothesis"), and cc3's relay §1(i) records "Scope-import sentence: **STRUCK**". But cc3's commit `f85c7577` message still reads "**H0 stands at the spectral level**" — the exact sentence cc's B797 says "was struck". Main's record of the null is scope-clean; the branch's git log is not.

10. **B791's "generic multiplicity" — cc3's requested scoping is not in cc's banked version.** cc3's B792 registers an "**Empirical input to B791's sector criterion**": observed m004 multiplicities are **{1, 2}**, not {1,5,6}; by Frobenius, dim V_i^H = 1 per sector (12 = 1·1 + 5·1 + 6·1), predicting multiplicity 1 per sector, "so the observed doubles must then come from a symmetry **OUTSIDE** the coset action (orientation / complex conjugation), not from the sector structure. **B791's 'generic multiplicity' phrasing should be scoped accordingly.**" cc's B791 (grep: no "Frobenius", no "V_i^H", no "orientation"/"complex conjugation") instead justifies generic simplicity from irreducible holonomy plus non-regularity of the degree-12 cover, and never records the observed-multiplicity-2 tension. cc's own §5b does require carrying multiplicity as first-class data — but the *origin* of the doubles is unaddressed on main.

11. **Weyl caveat: cc bounds a different quantity than cc3 and declines cc3's residual as a derivation.** cc's table reports the **scattering-determinant term** at T = 3 / 7.35 / 12 (−0.318 / −0.091 / +1.600). cc3's `weyl_scattering_check` reports the **post-correction residual** at T = 3 / 7 / 9.9 (−0.6 / −3.6 / −7.0), "tracking −(T/π)ln T … shape-predicted −4.3 and −7.2 at those T … **no missing-eigenvalue signature**." cc's official line: "cc3's cell absorbs them into a residual, which it **correctly describes as a consistency check rather than a derivation**", and therefore keeps the cusp terms as an *unquantified* O(T log T) ~14.7 at T = 7.35. So cc's banked instrument is strictly weaker than cc3's write-up implies ("B791's completeness criterion passes empirically on the m004 window" on the branch vs "the budget must not adjudicate a count difference of order one" on main).

12. **B793 has no branch counterpart, and it re-rates cc3's scan.** cc's Stage-A option (b) rates cc3's B792 mesh-scan as "**methodologically stronger** than the bank's control on precisely the axis at issue — it is a **detection**, not a refinement", while withholding it as a bank validation ("It does not validate the bank's solver"). cc3's branch has no B793 gate record at all (its old B793 was the coupling campaign). Related: GATE8R2's status moved three times across the range — "MUST NOT EXECUTE" (`4ba8d579`) → "UNBLOCKED, not discharged" (`5c716804`) → frozen as **Stage B**, "blocks nothing" (`1e907302`).

13. **Provenance phrasing of the 7.072 find.** Both seats converged on "**targeted** confirmation, not blind discovery" (cc: PROVENANCE_ALERT RESOLUTION, "targeted corroboration rather than blind confirmation"; cc3: FINDINGS §"BLIND OBSERVATION (provenance-corrected)" and relay §3). But cc's B797 harvest text states only that n = 6 "**discharges the B791 provenance alert**" without carrying the targeted-not-blind qualifier into the harvest arc; the qualifier lives only in B791. Also cc3 flags that "`eigenvalues_final.txt` still carries dry-run-era phrasing as a program artifact; FINDINGS.md governs" — that stale file was **not** harvested to main (only the `.json`), so main is clean on this point.

14. **Attribution asymmetries worth noting (no conflict, but uneven).** cc credits Chat-1 for naming E28 and for the split-gate design and the Weyl criterion; cc3's relay §5 records that **cc3 adopted the discard-reporting rule in `trace_norm_split.py`** and disclosed all three of its own filter stages (SnapPy multiplicity folding, PSL sign canonicalisation, ℤ[ω] rounding at tol 1e-6 with "zero rejections") — none of which is recorded in cc's E28 row. Conversely cc's B797 gives cc3 credit cc3 does not claim as loudly: "cc3's catch, not cc's" for the mult-2 structural blindness, and "fixed **better than specified**" for the sealing.

15. **Open items each side registers that the other does not.**
 - cc3 (`f85c7577`, relay §4): deep Test 3 at 50+ digits (needs mp-arithmetic eigenvalues) — *also on cc's list*; **parent r₂ above r = 10** — not on cc's list; **mult-2 old-form projection** — now closed; **m003-side congruence half** — not on cc's list; **τ-parity prototype for V₅ vs V₆** ("the central involution τ … is the scalar (1+2w)I mod 4 … Not built yet; say the word") — **not registered anywhere on main**; the ready-to-run **[0.5, 7.6] two-instrument cross-run** — which is precisely cc's B793 Stage-A option (a)/(b), but cc's B793 does not record that cc3 has offered it.
 - cc only: **re-certification before any tighter τ** (B797); **budget-derived screen cap replacing `maximum_minima_per_sector = 24`** for the Gate 9 re-run (B791/B793); **primary read of G–H Table 3** for the other ~35 values and the 5th digit (B791/B793 Stage B); **E32's campaign-level falsifier for B796** — the one live obligation cc's ledger places on cc3.