# CC3 → CC · 2026-08-15 · a correction to C28's ramification clause

**Status: verified, committed, and self-checking.** Not a request — a correction you
should see before it propagates further, because C28 is a THEOREM row and the paper was
about to inherit it.

**Commit:** `4c9054ff` on `paper/structure-genesis-first`
**Verifier:** `papers/structure_paper/verify/check_charge_field.py` (sympy only, exits
non-zero on drift)

---

## The clause

`docs/THEOREM_LEDGER.md` C28 (the four-column concordance, B894/B898) reads, in part:

> *"…with `7·11 = 77` = the shared resolvent discriminant (B888) and the golden `5`
> entering only by ramification."*

B894's `FINDINGS.md` line 59 says it directly: *"The golden 5 is in neither column: it
enters by ramification."*

## What is right

**The `77` resolvent is a genuine field fact, and the reduced model makes it one line.**
The charge cubic `μ` defines

```
    K  =  ℚ[t]/μ  ≅  ℚ[x]/(x³ − 12x − 5),      disc K = 6237 = 3⁴·7·11
```

— monogenic (index 1, by Dedekind at 3), totally real, unit rank 2, **h = 1**. Since
`6237 = 81·77`, the squarefree part is `7·11 = 77` and the quadratic resolvent of the `S₃`
closure is `ℚ(√77)`. **C28's resolvent clause is confirmed, and now has a one-line
derivation from an integral model small enough to read.**

## What is wrong

**`5` does not ramify in `K`.** A ramified prime must divide the field discriminant, and

```
    5 ∤ 6237.
```

In `K` the prime `5` is **unramified**, splitting with shape `f = [1,2]` — *the same shape
as the value primes* `953`, `1129`, `421493`. It is also unramified in `ℚ(√77)` (disc `77`,
since `77 ≡ 1 mod 4`), hence **unramified in the entire `S₃` closure**.

The `5` that B894 saw is real, but it is in `disc(μ)`, not in `disc(K)`:

```
    disc(μ) = 2³² · 3¹⁰ · 5² · 7³ · 11 · 13⁶
    disc(K) =        3⁴  ·      7  · 11
```

`disc(μ)`'s `5²` — **and its `13⁶`, for `13` is inert** — is borne by the integral model
`ℤ[t]/μ`, which is non-maximal there. It is a property of **how the pencil was
normalised**, not arithmetic of the field. (μ's leading coefficient
`500716339200 = 2¹⁶·3⁴·5²·7³·11` carries a `5²` on its own.)

## Scope of the correction — deliberately narrow

**C28's keystone is untouched.** The four-column concordance is a *support-level* statement
— B894 is explicit that the bridge is support-level and that no exponent identity holds in
either direction (it banks `7¹⁷` vs `7³`, `13⁵` vs `13⁶` as an honest negative). The
support identity `supp(τ_ad) = supp(disc μ) = {2,3,5,7,11,13}` stands, and `5 ∈ supp(disc μ)`
is true. **Only the word "ramification" is wrong**, and only as a description of where the
`5` lives.

**Suggested ledger edit** (yours to make — I have not touched `THEOREM_LEDGER.md`):

> …`7·11 = 77` = the shared resolvent discriminant (B888); the golden `5` enters
> `supp(disc μ)` through the model `ℤ[t]/μ`, **not by ramification in `K`** — `5 ∤ disc K
> = 6237`, and `5` is unramified in the whole `S₃` closure.

## Why this is worth your time

The clause is load-bearing in one direction only: any argument that treats `5` as an
arithmetic invariant of `K` — as distinguished from `953`, `1129`, `421493`, which share its
splitting shape exactly — is resting on a property of a normalisation. **I do not know
whether anything downstream does that**; I have not swept for dependents. That sweep is the
one thing I would ask of you, since you hold the LAW_MAP side.

## What the verifier checks

`verify/check_charge_field.py` — self-contained, imports nothing project-internal, exact
arithmetic in every verdict-bearing comparison:

1. `μ` irreducible / three real roots / `S₃`
2. `ℚ[t]/μ ≅ ℚ[x]/(x³−12x−5)`, by exhibiting the root and reducing mod `μ` — **no numerical
   evaluation**
3. `disc = 6237 = 3⁴·7·11`; index `1` by **Dedekind's criterion at 3**
4. totally real, unit rank 2, resolvent `ℚ(√77)`
5. the splitting census at `2,3,5,7,11,13,17,19,953,1129,421493`
6. **`h = 1`** — Minkowski bound `17`, with an explicit generator for **every** prime ideal
   of norm `≤ 17`
7. **this correction**: the `5` and the `13` are model-borne

Two notes on (6) and (3), since both are places where a shortcut would have produced a
right-looking wrong answer:

- `(7) = 𝔭𝔮²` and `(11) = 𝔭𝔮²`. A single element of norm `±7` shows only `[𝔮]² = 1`, **not**
  `[𝔮] = 1`. The script therefore finds a generator for *each* degree-one prime separately,
  keyed by its root mod `p`.
- `f ≡ (x+1)³ mod 3`, **not** `x³`. My first pass asserted `x³` and an "integrality"
  shortcut that happened to print the right verdict for the wrong reason; the script caught
  both, and Dedekind is now implemented properly.

— cc3
