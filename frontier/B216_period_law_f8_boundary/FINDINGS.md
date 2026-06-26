# B216 — the f≥8 boundary of the class-field period law: genus-theoretic (NEEDS-SPECIALIST)

> ⚠️ **OVERTURNED by B219 (V222, 2026-06-26).** The "genus-theoretic / NEEDS-SPECIALIST" verdict below is
> **wrong** — it was an artifact of testing `γ≡±I` (only the scalars ±1). The correct, **elementary** invariant
> is the binary-quadratic-form **content** `content(γ)=gcd(b,c,a−d)` = the largest modulus where `γ` reduces to
> *any* scalar. At `f=8`, mod 8 has extra square-roots of 1 ({1,3,5,7}), so `GAMMA_A=[[13,−8],[−8,5]]≡5·I (mod 8)`
> has true content **8**, not the `±I`-depth 4 — which is the *entire* "obstruction" below. B219 verifies
> `P(γ)=lcm(t−2,t+2)/content(γ)` exhaustively at `f=8` (all genera → period is genus-**independent**) and at
> `f=16`. The validated general-WRT tool built here is correct and reused by B219; only the *conclusion* is
> overturned. See `frontier/B219_period_content_law/`.

**Date:** 2026-06-26. **Status:** the focused attack on L39 (the `f≥8` residual of B215's class-field period
law). Built a **validated general-word WRT tool**, pushed the elementary criteria to **exhaustion**, and
**proved** the `f≥8` split is a finer **form-class / genus** invariant — a sharply-characterized
NEEDS-SPECIALIST boundary, not "it fails". Firewall: standalone quantum-topology / arithmetic; **nothing to
`CLAIMS.md`; P1–P16 untouched.** Ledger **V219**.

## The tool (validated)

To measure the split `d(γ)` for *any* conjugacy class (not just `R^aL^b` block words), `Z_k(γ)=tr(ρ_k(γ))`
needs a general `SL(2,ℤ)→S,T` factorization. Implemented and **validated to machine precision against the
block-word `Z` of B204/B214** (a real bug in a first quick version was caught and fixed — the `e=−1` final block
is `S²T^{−m}`, not `−T^m`; verify-don't-trust on my own code). This is reusable infrastructure for the WRT period
of any word.

## The obstruction (the result)

At `f=8` (`t=18`, `D=320=2⁶·5`, the golden field with conductor 8), the scalar-depth law of B215
(`d=max{d′∣f : γ≡±I mod d′}`) is incomplete. The decisive evidence — two **non-conjugate** trace-18 classes:

| class | period | `d` | scalar-depth | order-profile (mod 2,4,8,16) |
|---|---|---|---|---|
| `[[13,−8],[−8,5]]` | 10 | **8** | 4 | (1,1,2,4) |
| `[[17,−4],[−4,1]]` | 20 | **4** | 4 | (1,1,2,4) |

**Identical elementary invariants (scalar-depth 4, order-profile (1,1,2,4)), yet different `d` (8 vs 4).** Since
`d` is a conjugacy invariant and the two periods differ, the classes are definitively non-conjugate (confirmed by
orbit reduction). So:

> `d(γ)` is **not** a function of the scalar-reduction depth or the order of `γ` mod any `2^k`. It is a finer
> invariant of the **ideal class** (Latimer–Macduffee = the repo's **B92**) — a 2-adic **genus / spinor-genus**
> quantity.

I also checked the natural elementary refinements and they all fail uniformly: "scalar mod `d′` for *any* `λ`",
"order-2 ⟹ split-2" (refuted earlier in B215), etc. The elementary criteria are exhausted.

## Verdict

The full `f≥8` closed form is genuinely **genus-theoretic** (the 2-adic genus / spinor-genus / metaplectic-level
structure of the form class) — **NEEDS-SPECIALIST**. This is a *named, characterized* boundary (the precise
counterexample + the validated tool to attack it), reached by **computing to exhaustion** of the elementary
methods, not a premature deferral. The B215 law stands exact for `f∈{2,3,4}`; the `f≥8` refinement is the open
piece, now sharply located.

## Honest status / tiers
- the general WRT factorization: **`[exact]`** (validated vs block-word ground truth).
- the obstruction (same elementary invariants, different `d`, non-conjugate): **`[exact]`** (reliable periods +
  orbit conjugacy).
- the full `f≥8` law: **`[NEEDS-SPECIALIST]`** (2-adic genus theory) — a named boundary.
- Novelty UNCHECKED.

## Reproduction
- `python general_wrt.py` — the validation (vs block words) + the obstruction. (pyenv)
- `tests/test_b216_period_law_f8_boundary.py` — 2 locks (the tool validation + the obstruction are load-bearing).

## Caveat (for the next specialist pass)
Class **enumeration** at non-fundamental `D` is itself delicate — the form-enumeration here misses "thin" classes
(e.g. the single-block `R¹⁶L`, a `d=1` class), so a complete `h(D)`-class census needs a proper indefinite-form
reduction (cycle/continued-fraction), not box-bounded matrix search. The obstruction above does **not** depend on
completeness (it is two explicit classes); the genus-classification of `d` does.
