# B864 — the anomaly ledger: the dial/gauge split is DERIVED, and hypercharge is the UNIQUE gaugeable abelian direction

> ## ⚠ SCOPE SHARPENED 2026-08-17 (B8070) — NOT a retraction; this arc is correct as scoped
>
> Result (3)'s uniqueness is uniqueness **inside the chosen 3-plane** `span(Y, χ, ψ)`, which is
> what §3 says and what the downstream rows carry ("in the chain's abelian sector"). Two
> sharpenings, both re-derived from scratch on the B8070 bench:
>
> 1. **The coefficient `a` drops out identically.** The anomaly functionals are linear in `Q`, so
>    `Q = aY + bχ + cψ` gives `a·A(Y) + b·A(χ) + c·A(ψ) = 0`, and `A(Y) = 0` is the textbook fact.
>    **So the computation says nothing about `Y` itself** — it says `χ` and `ψ` are anomalous over
>    the imported chiral 15. `Y` enters as a basis vector and is reported back.
> 2. **Drop the 3-plane and uniqueness fails.** Over the full 5-dimensional charge space on
>    `(Q, uᶜ, eᶜ, dᶜ, L)` the linear conditions cut to a 2-plane on which the cubic **factors into
>    three lines**: `−2·yL·(2yL + 3yd)·(4yL − 3yd)/3` — hypercharge, the u↔d-swapped
>    Minahan–Ramond–Warner solution, and the vector-like direction `yL = 0`.
>
> **Consequence for quoting:** *"hypercharge is the unique gaugeable U(1) **in the chain's abelian
> sector**"* is correct and stands. *"Anomaly cancellation selects hypercharge"* — with the scope
> dropped — is **not** supported: there are three anomaly-free lines and the 3-plane is what picks
> one. See also B971, which shows the selective power lives in the imported truncation, not in the
> anomaly conditions.

cc banking seat, 2026-08-03, the critic's G3 run in full. Mathematics scope; nothing to
`CLAIMS.md`; Gate 5 untouched. **Not preregistered** — the critic's G3 pre-stated both outcomes
("forces the re-anchoring or indicts the truncation") before this ran; exact arithmetic throughout.

## 1. Three exact results

**(1) The parent level is anomaly-safe everywhere.** Over the full 27: Tr ψ = 16−20+4 = 0,
Tr ψ³ = 16−80+64 = 0, [SO(10)]²ψ = 2−2 = 0. Over the full 16: Tr χ = Tr χ³ = [SU(5)]²χ = 0, and
SU(5)'s own cubic cancels (A(10)+A(5̄) = 1−1 = 0 — the classic). **Nothing at the parent level
forces a truncation.**

**(2) Over the CHIRAL matter, the dials become anomalous.** ψ over the re-anchored 16:
**Tr = 16, Tr³ = 16, [SO(10)]² = 2 — all nonzero.** χ over the generation 10+5̄: **Tr = 5,
Tr³ = 125.** An anomalous U(1) cannot be gauged. **So the framework's claim that ψ, χ are
observer DIALS is now a consequence, not an assertion**: they are precisely the abelian
directions that physics *cannot* gauge over the chiral matter.

**(3) UNIQUENESS.** Writing the general abelian direction Q = aY + bχ + cψ over the generation,
the linear anomaly conditions come out `grav = 5b + 15c`, `[SU(3)]² = 2c`, `[SU(2)]² = 2c` —
**forcing b = c = 0 exactly.**

> **Hypercharge is the unique gaugeable U(1) in the chain's abelian sector — and its cubic then
> vanishes for free.** The "textbook miracle" (Tr Y = Tr Y³ = [SU(3)]²Y = [SU(2)]²Y = 0, all
> verified) is here inherited *and forced*.

## 2. The derivation arrow

> **The cascade's dial-stripping rule = anomaly consistency of the chiral sector.**
> The U(1)s the cascade strips (ψ, χ) are exactly the ungaugeable ones; the one it keeps (Y) is
> exactly the unique gaugeable one.

This upgrades the fused principle's "strip the θ-odd abelian factors" from a definition to a
consequence — with one scope note kept honest: B860/B861's criterion strips *all* abelian factors
including Y, which is *more* than anomaly consistency requires; chirality survives even that
(the non-abelian carrier), so the stronger stripping is safe but not forced. **The finer
structure G3 reveals: the θ-odd abelian sector is not homogeneous — it contains ungaugeable dials
(ψ, χ) and one gaugeable direction (Y), and anomaly consistency is what separates them.**

## 3. Layer 5, upgraded

The ledger's line *"anomaly freedom: automatic for complete SU(5) multiplets"* was **wrong as
stated** (a lone 10 is complete and anomalous — the critic's catch). The correct statement, now
computed: the generation's anomaly freedom is the **cross-cancellation A(10)+A(5̄) = 0** plus the
four-condition hypercharge check, all exact. **L5: CITED-wrong → COMPUTED.**

## 4. What this does NOT establish

- **It does not derive the re-anchoring itself** (G2's question stands): over the full 27 nothing
  is anomalous, so anomaly alone does not force keeping only the chiral core. What it derives is
  the dial/gauge split *given* the chiral matter.
- Convention note: ψ, χ charges in the standard normalization (27 = 16₁ + 10₋₂ + 1₄;
  16 = 10₋₁ + 5̄₃ + 1₋₅); the uniqueness conclusion is normalization-independent.
- Nothing about values, generations, the real form, or spacetime.

## Carried forward

1. **G2 next** (the padding lemma + the re-anchoring rule) — now sharpened: does *chirality of the
   kept sector* + *anomaly consistency* jointly force the re-anchoring uniquely?
2. G6 (the three involutions), G4 (the false-positive control), G7 (the lift), G5 (the keystone).

`tests/test_b864_anomaly.py`
