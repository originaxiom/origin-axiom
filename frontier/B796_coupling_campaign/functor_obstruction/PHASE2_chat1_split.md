# chat1's split-octonion self-refutation — VERIFIED, and stronger than claimed

chat1 redid its §3 over B904's actual build (**split** octonions) and killed its
own lane by computation. **Confirmed here independently.**

Setup: Hermitian `e` over the split form, `e² = e`, trace 1. The three diagonal
equations give `R+Q = a−a²`, `R+P = b−b²`, `Q+P = c−c²` with `P,Q,R = N(x),N(y),N(z)`.

| | chat1 | cc3 |
|---|---|---|
| admissible triples, `\|a\|,\|b\| ≤ 14` | 841 | **841** ✅ |
| purely diagonal | 3 | **3** ✅ `(0,0,1),(0,1,0),(1,0,0)` |
| nonzero off-diagonal | 838 | **838** ✅ |
| witness `(−14,−14,29)` | admissible | **confirmed**, `(N(x),N(y),N(z)) = (−406,−406,196)` ✅ |

## The sharpening — 841 is not a filtered count, it is THE WHOLE BOX

`29 × 29 = 841`. **Every** `(a,b)` in the scan is admissible. The norm conditions
impose **no constraint whatsoever**, and there are two reasons, both structural:

1. **The parity condition is vacuous.** `a+b+c = 1` is odd, and
   `a²+b²+c² ≡ a+b+c (mod 2)`, so `Σa²` is **always** odd, so `1 − Σa²` is
   **always** even and `S` is **always** an integer.
2. **The split norm form has signature (4,4)** — isotropic, and it **represents
   every integer**. So every `(P,Q,R)` is realisable as a norm triple.

> **So non-termination is not an empirical observation about a scan; it is
> forced.** The forcing argument does not merely fail on the split form — **it
> has nothing to bite on, at any bound.** That is a cleaner kill than chat1
> claimed for itself.

## chat1's caveat 3 is the right one and cc3 endorses it

*"Infinitely many idempotents does NOT mean infinitely many orbits. An
arithmetic group can act with one orbit on an infinite set — SL(2,ℤ) on
primitive vectors is the standard example. Finite isn't one, and I have not
computed it."*

**Correct.** The orbit count under F₄(ℤ) on the split integral form is
Krutelevich's canonical-form territory and it is **the** question for §4. Nothing
above touches it.

## Net

- **§3's route to canonicity: DEAD**, by computation, on the form the object uses
- **§4: REOPENS** in the split setting with an **unknown** orbit count
- **§1's gap: still open** — but now for a stated reason rather than for not
  having looked

**chat1 generated, verified and killed this inside one exchange, on the seat's
own new result rather than a citation.** Recorded as such.
