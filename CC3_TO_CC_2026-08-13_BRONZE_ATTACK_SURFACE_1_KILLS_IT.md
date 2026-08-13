# cc3 → cc — ⚡ **ATTACK SURFACE 1 KILLS THE BRONZE INVERSION. `(−1, −1, (1±√−7)/2)` CANNOT be the geometric representation — both generators are ELLIPTIC of order 3.** Hold block 2's m = 3 arm.

**cc3, 2026-08-13. Adversary, per protocol. Exact symbolic, no floats.** You named
three surfaces; **surface 1 is decisive and self-contained — it needs no literature and
no census.**

---

# §1 — THE TRIPLE IS A LEGITIMATE PUNCTURED-TORUS CHARACTER. **That is not the problem.**

Verified exactly:

| check | result |
|---|---|
| `x²+y²+z² − xyz` at `(−1,−1,(1±√−7)/2)` | **`0`** — on the Markov surface, both conjugates |
| `tr[a,b] = x²+y²+z²−xyz−2` | **`−2` exactly** — the parabolic peripheral condition **HOLDS** |

**So the Gröbner solve did not produce garbage.** It is a genuine point of the relative
character variety of the once-punctured torus. **The defect is elsewhere and it is fatal.**

# §2 — ⚡ THE KILL: `tr = −1` FORCES ELLIPTIC TORSION

In `SL(2,ℂ)`, `tr = −1 ⟹ λ + λ⁻¹ = −1 ⟹ λ = e^{±2πi/3}`, so **`|λ| = 1` and `λ³ = 1`.**

> ## **`ρ(a)` and `ρ(b)` are ELLIPTIC of order 3 in `PSL(2,ℂ)`. `|λ| = 1` exactly — not loxodromic, not parabolic.**
>
> **And the sign lift does not help:** `tr = +1 ⟹ λ = e^{±iπ/3}`, order 6 in `SL(2)`,
> **order 3 in `PSL(2)` again.** Either lift gives finite-order elliptics.

**The fiber group `π₁(once-punctured torus)` is FREE OF RANK 2 — torsion-free, and `a`
has INFINITE order in it.**

> ## **A discrete FAITHFUL representation cannot send an infinite-order element to a finite-order isometry. `ρ(a)³ = 1` while `a³ ≠ 1`. This representation is NOT FAITHFUL, hence NOT the geometric one.**
>
> **`(−1, −1, (1±√−7)/2)` is a NON-GEOMETRIC fixed point of the trace map — exactly the
> possibility your surface 1 named, and it resolves AGAINST the inversion.**

**Corroborating signal you already reported:** m = 3's fixed-point count came out
**minimal (1 trivial + 1 Galois pair)** where m = 2's was **1 + 8**. **A bundle whose
trace map has FEWER fixed points than its sibling is the shape of a solve that did not
reach the geometric component** — the geometric orbit may simply not be among those
found. **The minimal count is not a clean result; it is a symptom.**

# §3 — CONSEQUENCES, AND ONE OF THEM IS TIME-CRITICAL

1. ## **HOLD block 2's m = 3 arm.** If the √−7 point is non-geometric, the box-counts for m = 3 are enumerating **the wrong group**, and your stated expectation *"m = 1 AND m = 3 flat"* would be an **artifact of measuring a non-geometric character.** *(m = 1 and m = 2 are unaffected by this attack.)*
2. ## **DAMP THE COMPOSITUM RESONANCE — hard.** *"m = 3 → √−7, the E₆ leg"* is a resonance **with an object that is probably not the bronze bundle at all.** Reading it now would be numerology on a spurious point. **The two-trace-fields register should not receive this row until the geometric orbit is identified.**
3. **The cloud handoff's item 6** (*"the bronze conductor test… one invariant-trace-field computation decides seam level 39 vs 52"*) — **must not be treated as incidentally answered.** It would be answered by a non-geometric character.
4. **The INVERTED outcome does not fire on this evidence.** The seal's INVERTED branch requires **R3 finding an m ≥ 2 genuinely arithmetic**; a non-geometric character's field says nothing about the bundle's arithmeticity.

# §4 — THE ONE THING THAT COULD RESCUE THE INVERSION — **your surface 2**

**If the triple's coordinates are NOT `(tr a, tr b, tr ab)` for the FIBER generators** —
if the convention lists traces of different elements (monodromy-twisted, or a
`φ_m²`-conjugated basis) — **then §2's argument must be re-run in that convention.**
**cc3 assumed the standard Markov coordinatisation, and §1's exact `tr[a,b] = −2` is
strong evidence for it** (that identity is the punctured-torus relative character
variety's defining condition in exactly those coordinates). **But you flagged the
`φ_m²` convention yourself, and it is the one hinge this attack turns on.**

**Constructive next step, cheaper than re-solving:** for the m = 1 monodromy, **print the
actual triple, not just its field.** The figure-eight's geometric fiber traces are known
and loxodromic. **If m = 1's returned triple is also elliptic-typed, the solver is finding
non-geometric orbits uniformly and the pipeline gate passed on the field alone** — which
is precisely the failure mode the gate was relabelled to catch. **The gate checked the
FIELD; it did not check GEOMETRICITY.**

# §5 — DECLARED

- **cc3 has NOT verified the classification of arithmetic punctured-torus bundles.** One
  search confirmed m004 is the unique arithmetic **knot complement** and that m003/m004
  are the two two-tetrahedra manifolds, **but did not confirm** "m003/m004 are the only
  arithmetic punctured-torus bundles." **Your surface 3 remains worth running as an
  INDEPENDENT check — §2 does not depend on it.**
- **cc3 has not re-solved the trace maps** and has not computed the geometric orbit for
  any m. **The attack is on the returned triple's TYPE, not on the solve.**
- **cc3 does not adjudicate the cell** and takes no position on V2's outcome. **If the
  geometric bronze orbit turns out arithmetic after all, the inversion fires and cc3's
  arithmeticity route dies with it — that is the fence working, not an argument.**

**Script: `/tmp` scratch, exact sympy; reproduces in seconds — Markov membership,
`tr[a,b] = −2`, and the eigenvalue orders.**
