# B1068 — the object's canonical cubic étale algebra IS the charge field

**Date:** 2026-08-17 · **Seat:** cc3 · **Gate 5:** no physical identification anywhere.
**Verdict: PROVED**, against the two-sided criterion of `PREREGISTRATION.md`, with the
seal's weakness stated there and not repeated here as though it were absent.

---

## THE HEADLINE

> **`J^{2T} ≅ K = ℚ[x]/(x³ − 12x − 5)`**, field discriminant **6237 = 3⁴·7·11**,
> totally real, Galois group `S₃`.

`J^{2T}` is the fixed Jordan subalgebra of the **principal** `2T ⊂ F₄ = Aut(J)` acting on
the exceptional Jordan algebra. `K` is the programme's **charge field**, computed on the
opposite side of the construction — from the cascade's pencil, not from the 27.

**They are the same field.** Not two cubics of similar shape; the same field, verified
three independent ways.

## THE THREE VERIFICATIONS

The characteristic polynomial of `v₈` (the degree-8 invariant) is
`f = L³ − 2515968 L + 1213857792`, irreducible.

1. **Root test.** `μ = x³ − 12x − 5` acquires a linear factor over `ℚ[L]/(f)`. Both
   cubic ⟹ isomorphic.
2. **Field discriminant, computed without any extension machinery.**
   `disc f = 23922095638236364800 = 6237 × 61931520²`, and `61931520²` is a perfect
   square by factorisation (`2³²·3⁶·5²·7²`). So the **field** discriminant is exactly
   `6237`.
3. **Reduced model.** `L³ − 273L + 1372`, `disc = 30561300 = 6237 × 70²`. Same field.
   Square-free part of the discriminant is **77** for `μ`, for `f`, and for the reduced
   model alike; `S₃` in all three.

## THE RESTRICTED CUBIC

For `u = a·e + b·v₈ + c·v₁₆`, interpolated exactly (**residual 0**):

```
det(u) = a³ − 2515968 a b² − (10300450406400/13) a c²
           − 1213857792 b³ + (20600900812800/13) b²c
           + (193813274846822400/169) b c² − (365476461139722240000/2197) c³
```

after normalising so `det(e) = 1`. **The absence of `a²b`, `a²c` and `abc` was predicted
before the computation** and is the arc's sharpest internal check: `v₈` and `v₁₆` are
traceless, so no `a²·` term survives, and distinct `sl₂`-isotypic components are
orthogonal for the invariant form, so `σ₂` is diagonal and no `abc` term survives.

Hence `σ₂(w) = −(193536/13)(169b² + 53222400c²)` and `σ₃(w) = det(w)`, and the
characteristic polynomial of a traceless `w` is `L³ + σ₂ L − σ₃`.

## WHAT IT DECIDES, against the sealed criterion

**`J^{2T}` is a cubic FIELD, not split.** Every generic element's characteristic
polynomial is irreducible. Therefore **there are no primitive idempotents over ℚ**, and
**the object supplies no rational rank-1 VEV**. L138 does not fire rationally.

**But `K` is totally real**, so `K ⊗ ℝ ≅ ℝ × ℝ × ℝ`: over ℝ there are **exactly three
primitive idempotents**, canonically and with no choice entering. Two of them are what
`E₆ → SU(5)` requires. This is reported with equal weight, as the preregistration demands.

**So the answer is split by the base field, and that is the finding**: nothing over ℚ,
three of them over ℝ.

## WHY IT MATTERS BEYOND THE VEV QUESTION

The charge field was previously an output of **one** computation. It is now the output of
**two computations that share no code path** — the cascade's pencil on the measurement
side (`check_charge_field.py`), and the invariant Jordan subalgebra of the 27 on the
representation side (here). The corpus's own standard for such a coincidence is that
agreement is a *check*, not a repetition.

It also closes, on the algebra side, the gap logged as "the coupling law couples character
*values*, not representations": `J^{2T}` is a statement about a subalgebra of the 27, not
about character values.

## GATES — all green before any number was read

| gate | result |
|---|---|
| 27 minuscule, Weyl orbit of `ω₁`, multiplicity one | 27 weights, all distinct |
| principal `h`-profile = `V(16)⊕V(8)⊕V(0)` | exact match |
| cubic form supported on 45 weight-triples, each weight in 5 | 45; `27×5 = 135 = 45×3` |
| `dim (27)^{2T} = 3` at degrees `{0,8,16}` | Molien, computed independently |
| `e₈`: 240 roots, dim 248 | pass |
| ℤ/3-grading `78 / 81 / 81`; deg-0 = `72 + 6` | pass |
| deg-1 splits into three 27-blocks by `c₈` | `{−1: 27, 0: 27, 1: 27}` |
| principal `sl₂`: `[e,f]=h`, `[h,e]=2e`, `[h,f]=−2f` | pass |
| block profile inside `e₈` matches `V(16)⊕V(8)⊕V(0)` | exact match |
| ternary cubic interpolation residual | **0** |
| no `a²b`, `a²c`, `abc` terms | pass (predicted in advance) |

## LIMITS, stated rather than managed

- **The seal is weaker than the house bar.** Declared before compute, not committed
  before compute. See `PREREGISTRATION.md`.
- **The cubic form is computed; the multiplication table is not.** The algebra is read
  from the characteristic polynomial of a generic element. For a cubic étale algebra the
  norm form plus the identity determines it — an inference, recorded as one.
- **Novelty is NOT claimed.** No literature search has been run on "the fixed Jordan
  subalgebra of a principal `2T` in `F₄`". Fixed subalgebras of finite subgroups of `F₄`
  and cubic étale subalgebras of `J` are classical territory (Springer, Jacobson,
  McCrimmon), and this may well be recorded there. Per `WORKING_RULES §0`: **I have not
  searched for it**, which is not the same as its being absent. A sweep row is owed before
  any novelty claim is made anywhere.
- Kato–Yukie is **cited from the L138 lead, not read here.** The statement that they
  classify rational orbits of pairs of 27s by cubic étale algebras is inherited, not
  verified in this arc.

## RUN

```
python3 build_j2t.py    # gates 1–3, the 27's skeleton
python3 j2t_cubic.py    # the e8 carrier, the invariants, the restricted cubic
```

`e8_build.py` is the carrier: `e₈`'s Chevalley basis with sparse on-demand brackets, the
same construction as the paper's `check_charge_bracket.py` with the `E₈` Cartan matrix
substituted.

**Depends on:** B874 (the measurement ladder), B1011 (the McKay tensor and the two faces),
B962/L138 (the VEV picture), B959 (the centraliser no-go this sits outside of).

---

# CELL 2 — WITHDRAWN

**Status: WITHDRAWN 2026-08-17, the same day it was written. Its conclusion is not
established and its framing was false. Nothing in cell 1 depends on it.**

Cell 2 claimed that the object's idempotent pair fails to give `su(5)` because the two
idempotents are orthogonal, hence in a degenerate relative position. **Three errors, each
found only when the work was challenged rather than by the checks the cell itself ran.**

**Error 1 — the reductive part was inferred from a dimension.** `dim 44` is ambiguous
between `so(8) ⋉ 16` and `su(5) ⋉ 20`. Corrected by computing the Killing form's rank
(28, so `su(5)` is out *for that pairing*). The conclusion survived; the argument had not.

**Error 2 — "orthogonality is degenerate" is FALSE.** The control was never run. Over all
351 pairs of weight vectors of the 27 the joint-stabiliser spectrum is `{44: 135,
49: 216}`, so **44 is the generic value** and the object's pair sits in the *generic*
orbit. Orthogonality costs nothing. The entire explanatory story was wrong.

**Error 3 — the wrong pairing was computed.** Two vectors of the *same* 27 never give
`su(5)`. The standard route is `27 ⊕ 27-bar`, and that reproduces correctly: over all
729 weight-vector pairs the minimum is `dim 45` with **Killing rank 24 = su(5)**. Cell 2
answered a question nobody asked.

An attempt to repair it immediately produced a fourth error: reusing the 27's idempotent
coordinates on the 27-bar side gives vectors of stabiliser dimension **52, not 61** —
i.e. **rank 3, not rank 1** — because the 27-bar has its own cubic form which was never
computed. That pairing was rank-1 against rank-3 and is meaningless.

## WHAT SURVIVES, verified

| statement | status |
|---|---|
| every weight vector of the minuscule 27 is rank 1 (stabiliser 61) | verified |
| the three 2T-invariant idempotents of the 27 are rank 1 | verified |
| two rank-1 elements of the same 27: generic stabiliser 44, reductive part 28 | verified |
| the object's idempotent pair is in that **generic** orbit | verified |
| `27 ⊕ 27-bar`, rank-1 both: minimum 45, reductive part **24 = su(5)** | verified |
| **cell 1 (`J^{2T} ≅ K`)** | **untouched — no dependency on cell 2** |

## THE QUESTION THAT REMAINS OPEN

Compute the **27-bar's own cubic form** and its own 2T-invariant idempotents, then the
joint stabiliser of a 27-idempotent with a 27-bar-idempotent. Only that decides whether
the object reaches `su(5)`. **It has not been computed.**

## THE PATTERN, named because it recurred

Three times in one cell I computed something *adjacent* to the question and read it as the
answer — a dimension for a type, a special case for a generic one, a same-space pair for a
conjugate pair. Each was caught by a challenge, not by a gate. The cell had gates and they
all passed; they simply did not test the thing that was wrong.
