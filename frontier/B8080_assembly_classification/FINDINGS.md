# B8080 — the assembly classification is FALSE as stated: all six candidates admit one

**Date:** 2026-08-18 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS. **Gate 5:** untouched.
**Verdict: REFUTES** a paper theorem. Reproducer `assembly.py`; the decisive witnesses are also
checked on explicit matrices over ℚ. **Not preregistered** — the controls are classical facts and
the paper's own claims, neither chosen here.

## What the paper asked for, and why

`Scope (assembly)` flags Theorem `thm:classify` as owed, in its own words:

> *"That search is described here but its code is not deposited, so by this paper's own standard
> the theorem is an assertion **about** a computation. … The full six-group classification should
> be read as unverified."*

This is that code. The six groups are constructed as the theorem describes — the binary ones as
unit quaternions (2T the 24 Hurwitz units, 2O the 48, 2I the 120 icosians), the others as
permutation groups — and **conjugacy classes, power maps and characters are computed**, by Dixon's
algorithm at the least prime `p > C(29,3) = 3654` with `p ≡ 1 mod 120` (the lcm of the six
exponents, so every character value lies in `𝔽ₚ` and every multiplicity below is recovered
unambiguously). **No character value is transcribed.**

## The result

**Theorem `thm:classify` is false as stated.** A 27-dimensional assembly — *in exactly the sense
the paper defines: a direct sum of non-trivial complex irreducibles of total dimension 27 carrying
a non-degenerate invariant cubic form* — exists for **all six candidates**, not only `A₄` and `2T`.

**The block-sum lemma**, which decides it:

> Let `W` be an **irreducible** `G`-module carrying a non-zero invariant cubic `f`. Then the
> trilinear form `T` has **zero radical** — `rad(T)` is `G`-stable, so it is `0` or `W`, and
> `rad(T) = W` says `f = 0`.
>
> Hence if `27 = Σ mᵢdᵢ` over non-trivial irreducibles of degree `dᵢ` each carrying a non-zero
> invariant cubic, the block-diagonal cubic on `⊕Vᵢ^{mᵢ}` is invariant with zero radical.

| group | non-trivial irreducibles with an invariant cubic (degree, dim) | witness for 27 |
|---|---|---|
| `A₄` | (1,1) (1,1) (3,1) | `9×3` |
| `S₄` | (2,1) **(3,1)** | **`9×3`** |
| `2T` | (1,1) (1,1) (3,1) | `9×3` |
| `2O` | (2,1) **(3,1)** | **`9×3`** |
| `A₅` | **(4,1) (5,2)** | **`3×4 + 3×5`** |
| `2I` | **(4,1) (5,2)** | **`3×4 + 3×5`** |

Checked independently on **explicit matrices over ℚ**, invariance verified on every group element
and every triple, radical computed:

- `Σxᵢ³` on `{Σxᵢ = 0} ⊂ ℚ⁴` is `S₄`-invariant (24 elements, 27 triples), **radical 0** — so the
  standard 3-dimensional irreducible carries a non-degenerate invariant cubic, and `2O` inherits it
  through `2O/{±1} ≅ S₄`;
- `A₅` on 5 points → the **4**, and on the six Sylow-5 subgroups → the **5**, each with `Σxᵢ³`
  invariant under all 60 elements and **radical 0**; `2I` inherits both.

## Why the earlier repair was not enough

`Scope (assembly)` records that an earlier version was false because every group has a
27-dimensional **trivial** representation, and repaired it by excluding trivial summands and
demanding non-degeneracy. **The same failure mode survives the repair one level up.** Instead of 27
copies of the trivial module, take 9 copies of a 3-dimensional irreducible with an invariant cubic,
or 3 copies each of a 4- and a 5-dimensional one. **What the definition fails to control is
multiplicity, not triviality.**

Sharper still: **`A₄` and `2T`'s own witness is 27 copies of a non-trivial *linear* character**
(both have a linear character of order 3, so its cube is trivial and every cubic on the sum is
invariant). That is the refuted construction — 27 copies of the trivial module — barely disguised.
Excluding trivial summands did not touch the actual defect, and the two groups the theorem
*keeps* are kept by the very mechanism it was repaired to exclude.

## Why it is load-bearing, and why the chain does not break

The paper's next step reads *"Of the two survivors only `2T` is binary… which is what the McKay
correspondence requires."* That needs the survivor set to be `{A₄, 2T}`. **`2O` and `2I` survive,
and both are binary** — by Corollary `onlybinary`, which this arc also verifies. So binariness
does **not** absorb the failure, and §`sec:classification`'s reading — *"the
27-with-invariant-cubic condition leaves only `A₄` and `2T`, and only `2T` is binary"* — is refuted.

**What does not break.** The paper's primary route to `2T` is not this theorem. The abstract reaches
it arithmetically: *reducing the trace-field representation at the ramified prime gives a surjection
`π₁(4₁) ↠ SL(2,𝔽₃) ≅ 2T`* — and **B8076 item 6 verified that exhaustively** (48 surjections; and
`2I`, `A₅` are **not** quotients, over all 14,400 and 3,600 pairs). So what is lost is a
**corroborating** argument that the entrance is not an assignment, not the entrance itself.

## What the repair has to be

The definition must **pin the cubic**, not merely require one to exist. The natural condition — and
the one the construction actually uses — is that the pair `(V, f)` be **the 27 of E₆ with its
Jordan determinant**, equivalently that the assembly realise the group inside `E₆`. That is a
different computation from the one the paper describes, and it is **registered as owed, not
asserted** here.

## Controls

- every group closed under its own multiplication, at its stated order
- `Σ (deg)² = |G|` and column orthogonality, for all six tables
- Lemma `quat` verified: every faithful **special-linear** 2-dimensional irreducible has
  Frobenius–Schur indicator `−1` (the determinant filter matters — 2T's other two 2-dimensional
  irreducibles are that one twisted by an order-3 character and are not special-linear)
- Corollary `onlybinary` verified: only `2T`, `2O`, `2I` admit one
- the 3-dimensional icosahedral irreducibles carry **no** invariant cubic, matching the classical
  invariant degrees 2, 6, 10 — a fact this arc did not choose

## SCOPE

The refutation is of the theorem **as stated**, under the paper's own definition. It does **not**
show that no correct classification exists; it shows the stated one is not it, and names the
condition a correct one would need. Nothing here touches the member, the class, the sisters, the
rows, Gate 5, or any physical identification.
