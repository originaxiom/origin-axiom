# Gate 1 (arithmetic→CM) + Gate 3 (genus) — the "spectral-curve family" framing is refuted

**Date:** 2026-06-04. **Status:** exploratory, committed. Proven core P1–P16 untouched. Script:
`frontier/physics_probes/spectral_curve_gate1.py` (exact sympy). Standalone topology / number theory;
**no physics claim**. Builds on Gate 0 (V32: the m=2 curve is verified = m136's A-polynomial).

**Questions.** (Gate 1) Is the j=1728 / CM structure a real arithmetic *family* feature of the
metallic mapping tori, with CM field tied to the manifold's arithmetic? (Gate 3) What is the actual
genus across m=1,2,3 — does the web's "3 → 1 → 0, gauge theories of decreasing rank" hold?

**Verdict: the family/physics framing is REFUTED.** The curves have *different* genus (3, 1, ≥2 — not
"3,1,0"); only m=2 is elliptic; its j=1728 is forced + isolated, and its CM field is unrelated to the
manifold's arithmetic.

## Exact results

The metallic A-polynomials are degree 2 in L, so the spectral curve is the hyperelliptic double cover
`w² = disc_L(M)`; genus = `⌊(deg squarefree disc − 1)/2⌋`.

| m | manifold | genus | spectral curve / j | branch locus |
|---|---|---|---|---|
| 1 | figure-eight `4₁` | **3** | not elliptic (no single j) | `(M²−M−1)(M²−M+1)(M²+M−1)(M²+M+1)` — golden ratio + 6th-roots factors |
| 2 | `m136` (silver) | **1** | **j = 1728, CM by `Z[i]`** | `(M²−2M−1)(M²+2M−1)` — silver eigenvalues |
| 3 | `aaaBBB`=`R³L³` | **≥ 2** | NOT elliptic | fixed locus carries `√(5x⁴−10x³−x²+6x+1)` → not rational |

## Findings

1. **Genus is 3, 1, ≥2 — not "3, 1, 0".** m=2 is a genus *minimum*, not part of a decreasing
   sequence; m=3 is **not** the claimed "genus 0, free theory" (its fixed locus is irrational, so the
   curve is genus ≥ 2). The web's **"gauge theories of decreasing rank" is refuted by exact genus.**
2. **No uniform family of comparable curves.** Different genus ⇒ there is no family of elliptic
   spectral curves with comparable j-invariants. **Only m=2 (m136) is elliptic** — so "j=1728 across
   the family" is a category error; it is a fact about a **single** manifold.
3. **m=2's j=1728 is exact but forced + isolated.** It is forced by the silver trace identity
   (`a=6` in `κ=P²−6`; verified `j=1728 ⟺ a∈{0,±6}` for `y²=M⁴−aM²+1`). And the **CM field `Q(i)` is
   unrelated to the silver branch field `Q(√2)`** — so the CM is a property of the *quartic
   coefficients*, **not** the manifold's arithmetic (trace/cusp field) showing through. The "arithmetic
   → CM" story does not hold.
4. **m=1 is a genuine arithmetic curve but genus 3** — branch points at the golden ratio and
   6th-roots-of-unity factors — with no single j-invariant / no CM-by-one-field. Pretty, but not
   elliptic, not part of a CM family.

(Note: the SnapPy holonomy *fit* method is too flaky to census genus across many bundles — it failed
even to fit the *known* figure-eight A-polynomial under a poorly-conditioned word — so the verdict
rests on the **exact** A-polynomials for m=1,2 and the structural irrationality for m=3, not on fits.)

## Disposition

Gate 1 + Gate 3: the "metallic family of spectral curves → decreasing-rank 4D gauge theories" framing
is **refuted** (different genus, only one elliptic member, CM forced + isolated + arithmetically
unrelated). What survives, exactly: **m136's A-polynomial spectral curve is the j=1728 CM elliptic
curve** — a real, isolated fact about one manifold, forced by the silver mean. Number theory, not a
4D-physics family. Proven core untouched. Next: Gate 2 (the SW differential for the single m=2 curve —
expected to confirm j=1728 is a forced coincidence, not a genuine Seiberg–Witten identification).
