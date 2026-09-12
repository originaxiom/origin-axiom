# B1332 — the cup product vanishes, form-free, and the mechanism is cusp-triviality

> ## SCOPE CORRECTION (B1333 addendum, next day)
> **Everything below is a ONE-CUSP statement.** With several cusps `L_V` is usually **not** isotropic
> and `L_V != L_{V*}` — 36 of 40 sectors across 14 multi-cusped covers — **and the index vanishes
> anyway, in all 40.** So §1's implication (isotropy ⇒ `I = 0`) stands, but the reduction is **not**
> an equivalence: isotropy is sufficient, not necessary, and proving it would settle the one-cusped
> case only. §2–§3's "`L_V` is Lagrangian" and the form-free cup vanishing hold at one cusp and fail
> at two. See `frontier/B1333_the_index_on_several_cusps/ADDENDUM_isotropy_is_one_cusp.md`.

**Verdict: OPEN.** Still not a proof. But the thing to be proved is now a *different and smaller*
statement than B1331 left it, it is form-independent, and the reason the question is well-posed at
all has been identified — and it is not the reason B1331 guessed.

---

## 1. Why "isotropic" was ever a legal word

B1329 recorded that the classical isotropy argument **fails** for nontrivial `chi`, and it was right
to. `V = Sym^m (x) psi` with `psi` of order 3 admits an invariant bilinear form only if `psi^2 = 1`.
It isn't. **`V` is not self-dual, there is no pairing `H^1(M;V) x H^1(M;V) -> C`, and "isotropic"
has no referent upstairs.**

The escape is not a trick, and it is not optional: **`psi` is cusp-trivial, and the domain `D`
forces that.** `D` requires the cusp holonomy to lie in a one-parameter unipotent group times
finite-order scalars; the order-3 characters that survive are exactly those with
`psi(mu) = psi(lam) = 1`. So on the cusp torus

```
V|_T  =  Sym^m (x) 1  =  Sym^m  =  V*|_T        ( = W )
```

— not merely isomorphic, **the same module** (asserted and checked in every sector, not assumed).
Two consequences, and together they are the entire shape of the theorem:

**(1) An upgrade of a condition the domain already carries.** B1297's `D` *states* `t_0 = t_0*` — it is
part of the domain's definition, not a discovery here, and with `t_1 = t_0 + t_0*` it already gives
`t_0 = t_1/2`, so the target `r_1 = t_0` was always the target `r_1 = t_1/2`. (Every sector below shows
`t_1 = 2 t_0`, as it must.) What is new is **why**, and it is strictly stronger than the equality of two
numbers: the two restrictions are not merely equidimensional, they are **the same module**. That is what
puts `L_V` and `L_{V*}` in one space — equal dimensions would not — and so it is the upgrade from
`t_0 = t_0*` to a well-posed isotropy question.

**(2) The pairing exists downstairs.** `W = Sym^m` is self-dual as an `SL2` module, so the canonical
perfect pairing `H^1(T;V) x H^1(T;V*) -> H^2(T;C) = C` becomes a pairing of `H^1(T;W)` **with itself**,
and `L_V`, `L_{V*}` land in one space where "isotropic" means something.

> The global obstruction B1329 found is real. It is dissolved at the cusp, by a property the domain
> imposes anyway. So B1331's "the mechanism is local at the cusp" is not a hunch about where to
> search — **cusp-locality is what makes the question exist.**

---

## 2. Isotropy holds — and six of eighteen sectors prove nothing

Exactly over `Q(zeta_12)`, on the **geometric** holonomy, for each of the three chiral targets:

| | sectors | `t_0=1, r_1=1` | `t_0=2, r_1=2` | `t_0=3, r_1=3` | non-isotropic |
|---|---|---|---|---|---|
| `s958` | 18 | 6 | 9 | 3 | **0** |
| `t12833` | 18 | 6 | 9 | 3 | **0** |
| `t12835` | 18 | 6 | 9 | 3 | **0** |

`I = 0`, `L_V = L_{V*}`, `r_1 = t_0 = t_1/2` in all 54. **But the six `dim L_V = 1` rows in each are
vacuous.** For even `m` the induced pairing on `H^1(T;W)` is **alternating**, so `<z,z> = 0` for
*every* line — a 1x1 Gram of zero is forced by antisymmetry and says nothing at all. Only the
`r_1 = 2` and `r_1 = 3` rows carry content: `9*1 + 3*3 = 18` genuine scalar equations per manifold,
all satisfied exactly.

This is the same shape of trap as B1329's (a single `Sym^m` gives `t_0 = 1` and is structurally
biased toward `I = 0`), one level up. **Recording it because a reader who counts 18/18 and stops
has over-read the evidence by a third.**

---

## 3. The sharpening: the class vanishes, not merely its pairing

`L_V` is isotropic not only for the canonical `SL2`-invariant form but for **every**
`pi_1(T)`-invariant form on `W`:

| germ | `pi_1(T)`-invariant forms | isotropy holds on a subspace of dim |
|---|---|---|
| `Sym^2 (+) Sym^2` | 12 | **12** (all) |
| `Sym^4 (+) Sym^4` | 20 | **20** (all) |
| `Sym^2 (+) Sym^2 (+) Sym^2` | 27 | **27** (all) |
| `Sym^2 (+) Sym^4` | 14 | 12 (the `SL2`-invariant ones included) |

Isotropy is *linear* in the form, so these are honest subspace dimensions, not basis accidents.
And vanishing against every invariant form means more than isotropy: invariant forms are precisely
the functionals on `H^2(T;W (x) W) = (W (x) W)_{pi_1 T}`, so the statement can be made **form-free**
— checked directly, as a class, with no form involved:

| germ | `dim L_V` | `dim H^2(T;W (x) W)` | span of the cup classes |
|---|---|---|---|
| `Sym^2` | 1 | 3 | **0** |
| `Sym^4` | 1 | 5 | **0** |
| `Sym^2 (+) Sym^2` | 2 | 12 | **0** |
| `Sym^2 (+) Sym^4` | 2 | 14 | **2 — nonzero** |

**The last row is the one that fixes the statement.** For a germ whose summands are *non-isomorphic*
the class does **not** vanish outright, so "`L_V u L_V = 0`" would be false as written. Decomposing
`W (x) W` into blocks `Sym^a (x) Sym^b` shows exactly where the survivor lives:

| `Sym^2 (+) Sym^4` | diagonal blocks (`a = b`) | off-diagonal (`a != b`) |
|---|---|---|
| span of cup classes | **0 — vanishes** | 2 — the whole survivor |

`Hom_{SL2}(Sym^a, (Sym^b)^*) = 0` for `a != b`, so the off-diagonal blocks carry **no invariant
functional at all**: nothing that survives is visible to any form, hence to any duality statement.
That is also precisely why the `(2,4)` row above reads 12 of 14 rather than 14 of 14 — the two
missing directions are the non-`SL2`-invariant ones pairing the two unequal blocks. And for
`Sym^2 (+) Sym^2`, whose summands *are* isomorphic, the cross terms are duality-visible and they
vanish too (12 of 12).

So the correct form-free statement is:

> ## `L_V u L_V` vanishes in every component of `H^2(T; W (x) W)` that carries an `SL2`-invariant
> ## functional. For irreducible `W = Sym^m` that is the whole class.

This is what implies `I = 0`, for every choice of duality at once. And **it is not vacuous in the
`dim L_V = 1` sectors** §2 had to discount: there was a 3- and a 5-dimensional space for the class to
be nonzero in, and it is zero — those six sectors per manifold are recovered, with room to spare.

## 4. What this corrects in B1331

B1331 named cusp-locality as "the surviving candidate" for the mechanism, reasoning from unipotency.
That was the right direction for the wrong reason, and it understated the result:

- The role of cusp-triviality is **not** to make the mechanism plausible. It is to make the
  question **well-posed** (§1) — without it the global obstruction of B1329 stands and no pairing exists.
- The statement is **not** about a choice of identification `W ~ W*`. It is form-free (§3).
- `L_V = L_{V*}` was read off as subspace equality. The cup-class vanishing *implies* it and does
  not depend on how one identifies the two ambient spaces.

Galois remains ruled out (B1331 §3): all three targets are **chiral**, and the vanishing is
indifferent to it.

---

## 5. The implementation was validated before it was believed

The cup product was not trusted on the strength of a formula. On four commuting families in `SL2`
over `Q(zeta_12)`, `m = 1..6`:

- **well-defined**: coboundaries annihilate every cocycle — the check that catches sign and
  slot-order errors, since `<delta w, z> = 0` holds *only* via the cocycle condition;
- **parity as predicted**: exactly one invariant form per `Sym^m` (**solved for**, `g^T F g = F`, not
  quoted), alternating for `m` odd and symmetric for `m` even, full rank; composed with the
  antisymmetric cup this makes `H^1(T;W)` **symplectic for `m` even** — so "Lagrangian" is the
  literally correct word for the germs in play, and "maximal isotropic" for odd ones (B1329 §5);
- **perfect**: the Gram on `H^1(T;W)` has full rank in every case with `H^1 != 0` — Poincare
  duality on the torus, confirmed rather than assumed.

Four traps were hit and are worth the reader's time:

1. **Vacuity under an alternating form** (§2) — a 1-dimensional `L_V` is isotropic for free. Taken at
   face value this is a false proof.
2. **The `-I` projective lift.** `t12833` and `t12835` have relators evaluating to `-I`. The guard
   fired, exactly as B1330 addendum 2 warned; only even germs are valid there, and `Sym^even(-I) = +I`
   makes them safe. **Odd germs on those two manifolds would be silently meaningless.**
3. **Module-level scan code re-running on import** — twice, costing two long runs, until the library
   was split out and the driver put behind `__main__`.
4. **Test inputs not actually in `SL2`.** The first validation pass "failed" on a diagonal family;
   the inputs were `1 + 2*sqrt3`, not `1/2`. An assertion that the `SL2` form really is invariant
   under the test matrices was added *after* it bit, and now catches it at the door.
5. **Over-reading the form-free statement.** Three germ shapes vanish against *every* invariant form,
   which makes "`L_V u L_V = 0`" very tempting. It is false — `Sym^2 (+) Sym^4` is a counterexample
   found by running the block decomposition instead of stopping at the agreeable cases (§3).

---

## What to do with this

Prove that `L_V u L_V` vanishes in the `SL2`-visible part of `H^2(T;W (x) W)` — for irreducible
`W = Sym^m` that is simply `L_V u L_V = 0`, and §3 shows the general case reduces to it blockwise.
By §1 that is the whole index theorem; by §3 it is form-free; by §4 it is a statement about the
restriction map and the cusp, with no global symmetry of `M` available or needed. The natural route: the cup product on `H^*(T)` of two classes that both
extend over `M` factors through `H^2(M;W (x) W) -> H^2(T;W (x) W)`, and for a one-cusped `M` that
map is the boundary map whose vanishing is the classical half-lives-in-half argument — the content
is whether the *twisted* version survives, which is exactly where B1329 found the classical proof
breaking.

Reproduce: `verification/cupval.py` (the implementation validation — run this first),
`verification/iso.py <manifold>` (the 18-sector tally), `verification/iso3.py <mfld> <germ>` (how
special the form is), `verification/iso4.py <mfld> <germ>` (the form-free class), `verification/iso5.py <mfld> <germ>`
(the block decomposition that locates the nonvanishing), with `q12.py`,
`recog12.py`, `fi_lib.py` supplying exact `Q(zeta_12)` arithmetic and the recognised geometric
holonomy. Logs of the runs quoted above are in `verification/logs/`.
