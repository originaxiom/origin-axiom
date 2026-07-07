# B463 — Relation R4: the principal centralizer is ZERO — the 4d-commutant cell closes, scoped

**Status: banked (frontier). Firewalled. Prereg: PREREGISTRATION.md (PR #607, before
computation). Verdict: the prediction confirmed exactly; the kill scoped to the principal lift.**

## The computation (exact, Fractions, B351's algebra)

- **Control gate PASSED**: C_𝔢₆(long-root A₁) = **35 = 𝔰𝔩₆** — reproduces banked B247 exactly.
- **The cell**: C_𝔢₆(principal sl2) = **0** (joint kernel of ad(e), ad(h), ad(f), exact Gauss).
  Mechanism visible: ker(ad e) has ad-h weights {2, 8, 10, 14, 16, 22} — all strictly positive,
  so the weight-0 intersection is empty (= twice the exponents, the Kostant structure).

## The scoped consequence

The algebra centralizer of the **principal** lift (the program's banked E₆ route —
B347/B351/B445) is zero ⇒ the group centralizer is **finite** (Kostant's theorem identifies it
as Z(E₆) — ℤ/3 simply-connected, trivial adjoint — **cited as lit-gate, not booked as
computed**). With the one-line Zariski-density step (irreducible holonomy ⇒ the centralizer of
ρ₀(π₁) equals the SL(2)'s): **Chat-1's "the 4d theory's gauge group is determined by the
commutant of ρ₀ in E₆" yields a FINITE group — no continuous 4d gauge symmetry — on the banked
route.** The kill is embedding-specific (the long-root lift's SU(6), banked, is the
counterexample that scopes it); the 4d lift itself remains the four-times-named specialist
boundary (B278 W4, B259 W4, Gate B/Dimofte, L50) — re-cited, not re-opened.

## Reproduce
```
python3 centralizer.py    # control gate -> the cell -> ALL CHECKS PASS (~1 min, exact)
```
