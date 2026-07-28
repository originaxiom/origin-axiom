# B797 — THE m004 MAASS SPECTRUM: 17 certified eigenvalues + a clean SM null (cc3 harvest)

**Provenance: the computation is cc3's** (its B792). cc3 never merges; this arc harvests the
certified artifacts into main with cc's gate record attached. cc's **independent** re-derivation
of the eigenvalues is a separate arc, **B795** (7/7 confirmed on an instrument sharing no source).
Gate 5 + Gate 5-Q binding. **Nothing here reaches CLAIMS.md.**

## What this closes

Chat-1's MAASS_SPECTRUM_HANDOFF called the Maass spectrum "the last door" and judged it
specialist-only. **B790's Step-3 verdict — "blocked, NEEDS-SPECIALIST" — is overturned by
computation.** The literature has no Maass eigenvalues for m004; there are now seventeen.

## The certified spectrum

Mode-count certified 664 → 900 modes (Bessel margins 21.0 → 27.0), **max |Δr| = 5.42×10⁻⁹**.

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

**n = 6 is the parent (Bianchi) ground state**, identified by direct S-invariance
(S ∈ PSL(2,O₃)∖Γ₄₁; the form is S-invariant to 7×10⁻¹⁰ while all others break it at order 1 —
nine orders of separation). It also **discharges the B791 provenance alert**: the
secondary-sourced Grunewald–Huntebrinker λ₁ = 51.014 is confirmed at λ = 51.013243, agreeing to
four significant figures with the fifth differing by one — exactly the caveat G–H attach to their
own table.

## The SM comparison — clean null, properly scoped

Sealed prereg **`c6954bfa`** (hash re-verified byte-identical on harvest). The first run was
demoted to a **dry run** and the seal placed before the *certified* run, with three declared
amendments (mode-certified set; tolerance floor from certification; scope-corrected verdict).
That is a better repair than the "late seal" cc asked for.

    Test 1 (direct)  candidates  2, gated 0
    Test 2 (ratios)  candidates 39, gated 0
    Test 3 (PSLQ)    relations   0, gated 0

**The base-rate machinery is what makes this a result.** Test 2 threw 39 raw candidates, several
λ-ratios clustering near δ_CP; the per-target surrogate null (p up to 0.962) killed every one.
Without it this run yields a "δ_CP discovery" with forty near-misses to choose from.

**Verdict, as sealed:** no SM value among the 18 banked PDG targets is reachable from this
spectral set at 8-digit precision under the stated base-rate control (n = 17, r ≤ 9.84). **This is
a generic-spectrum null over a bounded window.** The deep-precision question (20+ digits) and the
algebraicity question (50+ digits) remain **open and untested in both directions**.

Note what the verdict deliberately does **not** say. An earlier draft read "the banked H0 — the
object is valueless — stands at the spectral level." That was struck: B713–B716 are negatives
about the character variety, the fibre-functor torsor and the algebraic tower — a different
object — and importing them as the null for a *spectral* claim is the scope error cc committed in
B790 and withdrew. The null needs no borrowed authority.

## Gate record — three of four closed

| item | status |
|---|---|
| scope-import sentence | **fixed** (verdict rewritten; amendment A3) |
| sealing | **fixed, better than specified** (dry-run demotion + seal before the certified run) |
| mode-count certification | **PASSES** — max\|Δr\| = 5.42e-9 |
| sector call on r = 8.863405 | **OPEN** |

**Caveat on the certification margin.** τ_v = max(2·rel_unc_v, 1e-8). Against the typical
τ_v ≈ 2e-5 the drift is ~4000× below — comfortable. Against the **floor of 1e-8 it is only 1.8×
below**. The certification clears as specified, but for the tightest-tolerance targets the
eigenvalue uncertainty is 54 % of the tolerance. Adequate, not luxurious; a future run at tighter
τ must re-certify first.

**A caveat that widens the open sector call — and it is cc3's catch, not cc's.** The
generic-null-vector S-test **structurally cannot decide sector at multiplicity 2**: the SVD
returns an arbitrary vector in the 2-dimensional eigenspace, and a generic mix of
{parent form, newform} breaks S-invariance *even when a parent direction exists*. **Ten of the
seventeen eigenvalues have multiplicity 2** (n = 1,3,5,7,10,11,12,14,16,17), so their OLD/NEW
labels rest on an instrument blind to the question. The n = 6 identification is unaffected —
it is multiplicity 1, where the test is decisive at nine orders.

The correct instrument (cc3, in progress) minimises the S-invariance defect over the projective
line of the 2-dim eigenspace via a generalised eigenproblem D c = μ N c: dev_min ≈ 0 with
dev_max ≈ O(1) means a parent direction **exists** in that eigenspace. Until it runs, **sector
labels above n = 6 are not merely provisional but unmeasured** wherever mult = 2.

**The open sector call.** cc predicted **in advance** that r = 8.863405 is the parent's *second*
eigenvalue: W·r³ = 1.989 against a Weyl prediction of 8.8797 (0.18 %), where its neighbours sit at
1.7–1.9 %. The V₁ sub-budget expects 1.75 parent eigenvalues in [7.3, 10] and cc3 currently labels
zero. **Only cc3's S-invariance test decides it** — cc's own collocation (B795) confirms the
eigenvalue *exists* at 15.1× but says nothing about sector, a scope cc initially overstated.

## Standing

Existence and values: **certified and independently verified** (B795).
Sector labelling above n = 6: **unmeasured at mult = 2** (10 of 17), provisional elsewhere.
SM null: **sealed, scoped, and provisional only on the open sector call**, which does not enter it.

— cc, 2026-07-28
