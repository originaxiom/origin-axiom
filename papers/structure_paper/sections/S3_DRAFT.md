# §3 — DRAFT v1: From minimal description to a knot

*Registry rows G1, G2, G6. Locks: `tests/test_b749_genesis_forks.py`,
`tests/test_c2_self_selection.py`, `tests/test_b285_commutator_phase.py`.*

---

## §3. From minimal description to a knot

This section carries the construction from the principle of §2 to a specific
3-manifold. Four steps: two theorems, then the two choices C4 and C5 already
declared, then a classical realization theorem. **No step introduces a
quantity.**

### 3.1 Minimality forces a Sturmian word

Let `w` be an infinite word over a finite alphabet and let `p(n)` be its factor
complexity — the number of distinct length-`n` subwords.

> **Theorem 3.1 (Morse–Hedlund).** If `w` is aperiodic then `p(n) ≥ n + 1` for
> every `n ≥ 1`. Words attaining `p(n) = n + 1` for all `n` are exactly the
> Sturmian words.

Periodic words have bounded complexity, so under §2's principle they are
excluded: they close. Among the words that do not close, Theorem 3.1 identifies a
**unique minimal complexity class**, and it is non-empty. *Minimal
non-terminating description is therefore Sturmian* — not by preference, but
because the inequality is sharp and its equality case is classified.

*(Registry G1. Lock: `tests/test_b749_genesis_forks.py`, control fork F7.)*

### 3.2 The principle applied to its own parameter selects the golden slope

Sturmian words are classified by a single irrational **slope** `α ∈ (0,1)`: the
word records the itinerary of a rotation by `α`. Theorem 3.1 fixes the *class*;
it does not fix `α`. But the slope is itself a parameter of the description, and
applying §2's principle to it is what removes the last freedom.

The relevant notion of "least reducible to a terminating description" for an
irrational is **worst rational approximability**, measured by the Lagrange
number `L(α) = limsup_{q→∞} (q·|qα − p|)⁻¹`.

> **Theorem 3.2 (self-selection).** Among the slopes with eventually constant
> continued fraction `[a; a, a, …]`, `a ≥ 1`, one has `L = √(a² + 4)`. This is
> strictly increasing in `a`; **the unique minimiser is `a = 1`**, the golden
> slope `φ = (1+√5)/2`, with `L(φ) = √5` — the bottom of the Lagrange spectrum
> (Hurwitz).

Two features of this step deserve emphasis, because they are what makes it a
theorem rather than a preference.

**(i) It is a fixed point, not a selection.** A continued fraction all of whose
partial quotients equal `1` is *precisely* a fixed point of `t ↦ 1 + 1/t`. So
`φ` is not chosen from a list of candidates: it is the value at which the
minimality condition, applied to its own parameter, reproduces itself. The
statements "the continued fraction is all-`1`s" and "`x = 1 + 1/x`" are the same
statement.

**(ii) The minimiser is unique.** Strict monotonicity of `√(a²+4)` gives
uniqueness directly, and we assert it separately so that the uniqueness clause
has an independent failure mode.

*(Registry G2. Lock: `tests/test_c2_self_selection.py` — all four clauses, exact
arithmetic, with a can-fail control asserting that the silver slope `a = 2`
**fails** the extremality test. Partial prior coverage, uncited by the chain,
exists in `tests/test_b176_golden_privilege.py` (in floating point) and
`tests/test_b179_metallic_numbers_unified.py`.)*

**The setting is classical and we name its modern reference explicitly.** The
correspondence this section runs on — Sturmian and Christoffel words, continued
fractions, and the Markoff/Lagrange theory — is the subject of Reutenauer's
monograph *From Christoffel Words to Markoff Numbers* (Oxford, 2019), whose Part I
is the classical Markoff theory and whose Part II covers finite Sturmian words, the
free group on two generators, Christoffel bases, Nielsen's criterion, **Sturmian
morphisms and positive automorphisms**. The link between Christoffel words and
Markoff theory goes back to Frobenius (1913). **Nothing in §3.1 or §3.2 is offered
as new**; what is ours is the use made of them — applying the minimality principle
to its own parameter, which is a modelling step, not a theorem.

### 3.3 Geometrization and orientation (C4, C5)

The two declarations of §2.2 now apply and produce a surface bundle.

By **C4** the word is realized on the **once-punctured torus**; its slope
determines an element of the mapping class group `SL(2,ℤ)`. By **C5** the
monodromy is taken orientation-preserving — the golden slope squared — giving

```
                       φ  ↦  M = [[2,1],[1,1]],      tr M = 3.
```

We restate the price of C5 here, at the point of use: the discarded `det = −1`
alternative yields the **Gieseking manifold**, the orientation double cover's
parent of the bundle below. That object is not degenerate; it is simply not the
one this construction follows.

### 3.4 The mapping torus is the figure-eight knot complement

> **Theorem 3.4 (Thurston; Riley).** The mapping torus of the once-punctured
> torus under `M = [[2,1],[1,1]]` is the complement of the figure-eight knot. It
> carries a unique complete hyperbolic structure, and its Kleinian trace field is
> `ℚ(√−3)`.

This is the end of the genesis. The construction has produced a specific,
canonical object, and the arithmetic invariant that governs everything in §§4–5
— the field `ℚ(√−3)` — is exactly the datum that C4 purchased and that no
non-geometric carrier supplies.

*(Registry G6. Lock: `tests/test_b285_commutator_phase.py`, with the exact Riley
representation `u² + u + 1 = 0`.)*

### 3.5 Where the count stands

**Three declarations have been spent** — C3 before §3.1, C4 and C5 in §3.3.
**Two theorems and one classical realization** carried the rest. **No numerical
value has entered.** From here to the end of §8, the chain contains no further
declared choice (§5.5).
