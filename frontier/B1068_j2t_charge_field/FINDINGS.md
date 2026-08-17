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

# CELL 2 — the object's own idempotent pair does NOT give SU(5)

**Verdict: NEGATIVE, and it is the sharpest negative in the arc.**

## THE QUESTION CELL 1 LEFT OPEN

The standard route is `E₆ → SU(5)` by **two Jordan-rank-1 VEVs**. That result is for two
rank-1 elements in **general position**. The two the object supplies are not in general
position: cell 1 showed `e₁ + e₂ + e₃ = 1` exactly, so they are two members of an
**orthogonal frame**. Whether a frame pair is a general-position pair is a question, and
the whole physics reading turns on it.

## THE COMPUTATION

The joint stabiliser's Lie algebra is the annihilator `{X ∈ e₆ : X·u = 0}` — a linear
condition, so a rank computation. `e₆` is the `c₇ = c₈ = 0` part of the `e₈` carrier,
acting on the 27-block. Done mod primes at which the idempotent coordinates split, so the
arithmetic is exact. **Confirmed at p = 1093, 1097, 1151 — identical.**

| stabilised | dimension | Killing rank | reductive part |
|---|---|---|---|
| one idempotent | **61** | — | `so(10) ⋉ 16` — **the gate**, forced by rank-1 (78 − 17) |
| **two** | **44** | **28** | `so(8)`, rank 4 |
| all three | **28** | **28** | `so(8)`, reductive |

**A CORRECTION TO THIS CELL'S FIRST WRITE-UP, recorded rather than silently patched.**
The first version read the reductive part off the dimension 44 together with the
observation that the 28 sits inside it. **That is not an argument**, and 44 is genuinely
ambiguous:

```
    so(8) (x) 16  = 28 + 16 = 44          su(5) (x) 20 = 24 + 20 = 44
```

Both fit. The question was settled only by computing the **rank of the Killing form** on
the stabiliser, whose radical contains the nilradical, so that its rank is the dimension
of the reductive part. That rank is **28, not 24**, which excludes `su(5)`.

The 28 is then pinned a second way: stabilising all three idempotents fixes their sum,
the identity, so the group lies in `F₄`, where the pointwise frame stabiliser is
`Spin(8)` of dimension 28. Both routes agree — but the first write-up had only the second
route and presented it as if it settled the first question. It did not.

## WHAT IT DECIDES

**Not 24, not 25.** `su(5)` and `su(5) ⊕ u(1)` are both excluded by dimension. **The
object's canonical VEV pair does not produce SU(5).**

And the group it does produce is achiral: `−1 ∈ W(D₄)`, so **every** representation of
`so(8)` is self-dual, so the 27 restricts real. Right rank, no chirality.

**This is the fourth independent arrival at the same trade-off**, and they are genuinely
independent — different mechanisms, different arcs:

1. **B953** — the θ-split: `78 = 52 (F₄) + 26`; `rank F₄ = 4`, all reps real
2. **B959** — the τ-fold: reaches rank 4, makes the 27 self-dual
3. **cell 1 / degree-0** — the canonical VEV direction is the Jordan identity, stabiliser `F₄`
4. **cell 2 / the pair** — `so(8) ⋉ 16`, rank 4, all reps self-dual

The object reaches rank 4 by every route it has, and **kills the 27's complexity every
time**. That is now a pattern with four instances rather than a coincidence with one.

## WHY, STRUCTURALLY

Orthogonality is a **special** position, not a generic one. A frame pair is exactly the
degenerate configuration. The object hands over its rank-1 elements already mutually
orthogonal — because they are the primitive idempotents of a *field*, hence a complete
frame — and that orthogonality is precisely what costs the SU(5).

**So L138 does not fire even over ℝ**, and the reason is not the reality of the points but
their relative position. Cell 1's "three idempotents over ℝ" is true and is not enough.

## LIMITS

- Dimensions are computed; the isomorphism types are **inferred from dimension plus the
  independent 28 = frame-stabiliser reading**. A direct structure-constant identification
  of the 44 was not done.
- Mod-p rank can only *over*-estimate a nullity; agreement across three primes makes an
  artefact unlikely but does not exclude it.


## A GATE THAT WAS NAMED AND NOT RUN

`cell2_stabilizer.py` carries a comment reading `# GATE: closed under bracket?` and that
check was **never executed**. Stabilisers are subalgebras, so it is automatic and nothing
downstream is wrong — but a gate that is named and not run reads as coverage it does not
provide, which is precisely the failure this repository's discipline exists to catch. It
is recorded here rather than quietly deleted.
