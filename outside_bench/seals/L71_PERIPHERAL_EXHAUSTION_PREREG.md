# SEAL — L71: the full peripheral class, and whether the route is exhausted

**Sealed before the certificate was written. No prototype was run for any cell below;
no prior is declared for any of them.**

Memo 213 closed one route into L71: the peripheral **coker slope** is forced by the cusp
and reads the cusp shape and nothing else. It named the successor: *"the full peripheral
class, not its coker shadow — `H¹(T²; Sym^{2m})` is 2-dimensional and the coker map crushes
it to one number."* This seal tests that successor and, with it, whether the peripheral
route has any content left at all.

## The setup, fixed here so the coordinates are reproducible

`ρ(a) = exp(N)`, `ρ(λ) = exp(τN)` on `V = Sym^{2m}`, `N` a single nilpotent block with
`N e_i = e_{i+1}`, `ker N = ⟨e_n⟩`, `n = 2m`. Cusp cocycles are pairs
`(x, y) = (ξ(a), ξ(λ))` with `(e^N − I)y = (e^{τN} − I)x`; coboundaries are
`((e^N − I)v, (e^{τN} − I)v)`.

**The declared basis of `H¹(T²; V)`:**

- **`u₂ := (0, e_n)`** — canonical: `e_n` spans `ker N`, and `(0, e_n)` is a cocycle and not
  a coboundary.
- **`u₁ := (e_0, y₀)`** where `y₀` is the unique solution of `(e^N − I)y = (e^{τN} − I)e_0`
  with `(y₀)_n = 0`.

Write `res(ξ) = α·u₁ + β·u₂` modulo coboundaries, for the generator `ξ` of `H¹(M; V)`.

## CELL 1 — is the restriction injective?

**Observed:** whether `res(ξ) ≠ 0` in `H¹(T²; V)`, for **m = 1 … 11** (all six E₆ exponents
and five non-exponents).

- **Outcome A:** `res(ξ) ≠ 0` for every m — no block's deformation is invisible at the
  boundary.
- **Outcome B:** `res(ξ) = 0` for at least one m — that block's deformation is **cuspidal**,
  and the θ-parity of the blocks where it happens is the finding.

## CELL 2 — does the class lie on the canonical line?

**Observed:** whether `res(ξ) ∈ ℂ·u₂`, i.e. whether `α = 0`.

- **Outcome A:** `α ≠ 0` for every m.
- **Outcome B:** `α = 0` for at least one m.

## CELL 3 — the second coordinate, and whether it can differ at all

**Observed, in this order:**

1. **First the MB12 partner.** The set of values `β/α` takes as `(x, y)` ranges over the
   cusp cocycle space `Z¹(T²; V)` — specifically whether it takes **more than one** value.
2. Only if it does: the twelve values `β_m/α_m` for the global generator.

- **Outcome A:** `β/α` takes more than one value on `Z¹(T²;V)` **and** `β_m/α_m` is the same
  for every m.
- **Outcome B:** `β/α` takes more than one value on `Z¹(T²;V)` **and** `β_m/α_m` varies
  with m.
- **Outcome C:** `β/α` takes only one value on `Z¹(T²;V)` — the coordinate is forced by the
  cusp exactly as the coker slope was, **and the per-block values may not be read**
  (memo 164, and memo 213's rule).

## CELL 4 — is L71's computable content exhausted?

L71 asks for the **geometric meaning** of the θ-odd deformations. Four computable questions
sit under it, and this cell checks whether the record already answers each — by exact string
presence at HEAD, not by memory.

**Observed:** whether each of these is present in the corpus:

1. **integrability at second order** — `B575`'s `Q ≡ 0`;
2. **the Zariski closure per direction** — `B576`'s closure lattice;
3. **the cup-product obstruction at the foundation** — `B270`'s vanishing;
4. **the peripheral behaviour** — memo 213 plus CELLs 1–3 here.

- **Outcome A:** all four present.
- **Outcome B:** at least one absent — and that absence is L71's live computational content.

## Controls

- **C1** — `ρ_{2m}(r) = I` and `ρ(λ)` commutes with `ρ(a)`, every m.
- **C2** — `h⁰ = 0`, `h¹ = 1`, `dim ker(ρ(a) − I) = 1` at the six E₆ exponents (the
  `P2W5-L72` exact table).
- **C3** — `dim Z¹(T²;V) − dim B¹(T²;V) = 2` for every m, and `{u₁, u₂}` independent modulo
  `B¹` — the declared basis must actually be a basis.
- **C4** — the coker slope recovered from this richer description must come out `−2√−3`,
  agreeing with memo 213.

## Interpretation is not preregistered

Per bench rule #21 the outcomes state only what is observed.
