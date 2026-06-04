# Metallic-anyon / TQC probe — the golden→Fibonacci bridge does NOT generalize (controlled negative)

**Date:** 2026-06-04. **Status:** exploratory probe, committed for honest history (labels below).
Proven core P1–P16 untouched. Script: `frontier/physics_probes/metallic_anyon_probe.py` (exact sympy).
Standalone TQFT/anyon mathematics; **no Origin-core / no thesis claim**.

**Question.** The Fibonacci anyon (quantum dimension = golden mean `φ`, the `m=1` metallic mean) is
**universal** for topological quantum computation. Does this generalize: is there an anyon *family*
— a unitary modular tensor category with the "metallic" fusion rule `τ⊗τ = 1 + m·τ` for `m=2,3,…`
(silver, bronze, …) — and is it universal? This is the sharpest real-physics (TQC) target the
trace-map metallic structure suggested.

**Verdict: NEGATIVE (controlled).** The metallic-anyon *family* does **not** exist. The
golden→Fibonacci→universal-TQC bridge is **special to `m=1`**; it does not extend to a coherent
silver/bronze anyon family. The metallic means appear only *sporadically* as quantum dimensions in
higher `SU(2)_k`, with different fusion rules — no tower↔anyon correspondence.

## What was computed

**(1) The metallic fusion ring is consistent for every `m` (necessary, not sufficient).**
`N_m = [[0,1],[1,m]]` (fusion `τ²=1+mτ`) has Perron–Frobenius eigenvalue exactly the metallic mean
`d_m=(m+√(m²+4))/2` (verified symbolically, `m=1..5`; min. poly `x²−mx−1`). So a *fusion ring* with
PF-dimension `d_m` exists for all `m`.

**(2) Categorification fails for `m≥2` — only the golden anyon is real.** A 2-object fusion category
`{1,τ}` has, by **Ostrik** (*Fusion categories of rank 2*, Math. Res. Lett. 10, 2003), fusion rule
**either** `Z/2` (`τ²=1`, pointed) **or** Fibonacci (`τ²=1+τ`). The metallic rule `τ²=1+mτ` is
Fibonacci **only for `m=1`**. Hence for `m≥2` there is **no unitary fusion category** (no anyon
model) with the metallic fusion rule — the pentagon equations have a unitary solution (the golden
F-matrix) only at `m=1`. *(This is the cited classification, not re-derived here.)* The
"metallic anyon" exists **only** for golden = Fibonacci.

**(3) The metallic means appear only sporadically as quantum dimensions (with other fusion rules).**
Searching every `SU(2)_k` quantum dimension `[n]_q`, `k≤40`:

| metallic mean | appears as a quantum dim of | exact? |
|---|---|---|
| golden `φ=1.618` (`m=1`) | `SU(2)_3`, spin ½ and spin 1 | ✓ |
| silver `1+√2=2.414` (`m=2`) | `SU(2)_6`, spin 1 and spin 2 | ✓ |
| bronze `(3+√13)/2=3.303` (`m=3`) | **none** (`k≤40`) | — |
| copper `2+√5=4.236` (`m=4`) | **none** (`k≤40`) | — |

So golden and silver *do* occur as `SU(2)_k` quantum dimensions (both at **universal** levels —
`SU(2)_k` braiding is universal for `k≥3, k≠4`, Freedman–Larsen–Wang), but with the *native*
`SU(2)_k` fusion rules, **not** the metallic `τ²=1+mτ` rule — and bronze/copper do not appear at all.
There is no metallic *family* and no map from the trace-map tower to an anyon family.

**Selectivity control (the search is meaningful, not matching everything):** the plastic number
(`1.325`) and bronze/copper return **no** `SU(2)_k` match; the integer `2` matches only the
non-universal `SU(2)_4`; `1+√3` matches `SU(2)_10`; golden matches `SU(2)_3`. So "is a quantum
dimension" is a genuine, selective constraint — the golden/silver hits are not artifacts.

## Honest reading

- **The known anchor stands:** `m=1` (golden) genuinely connects to the Fibonacci anyon and
  universal TQC. That is real, but already known, and special.
- **The generalization fails:** there is no silver/bronze "metallic anyon," so the trace-map metallic
  *family* (which is the project's actual novel object) has **no anyon/TQC realization**. The
  golden↔TQC link is a coincidence of `m=1`, not a feature of the tower.
- This is a clean **controlled negative** — it *closes* the "metallic-anyon family" path and corrects
  the tempting extrapolation from the golden case. (Silver-in-`SU(2)_6` is a real but isolated fact,
  not a family.)

**Disposition:** path CLOSED (no anyon-family crossing). The one residual real-physics target in
condensed-matter remains the `SU(2)/SU(n)` multichannel spectrum probe (separate). Proven core
untouched.
