# B931 — WHY 953: the residue is a PLACE, not a number — the twist is the half-flip locus, and the two atom families see the two places of 953

**Date:** 2026-08-06 · **Seat:** computation agent (lane 2, for cc banking) ·
**Status:** DRAFT — exact tier for every claim (symbolic eigenline trace over
ℚ[x]/(h), resultant factorizations, round_two integral bases, prime-ideal
valuations); no numerics anywhere.
**Instrument:** `why953.py` → `results.json` (**53 checks, ALL PASS**; ~17
min, frame-cached; the banked B916 d-minpolys and B928 flip-mass minpolys
are RE-DERIVED inside this cell by an independent symbolic route — and the
banked B928 K-coordinates re-verified through a second monic model — before
any provenance claim is made).

## The question (B928's registered residue)

B928 reduced the twist arithmetic to the K-norm of d = 1 − 2·(flip mass) on
the banked atom lines, N_{K/ℚ}(d) = −(953/2304)² on both colorless families,
and stopped at: *where in the eigenline coordinates do 953 and 2304 = 2⁸3²
come from?*  This cell answers with a derivation chain that ends one step
higher than B928 — at the **prime-ideal divisor of the twist ratio** — and an
exhausted candidate map for the one step that remains open.

## Headline 1 — 2304 is DERIVED: it is the {2,3}-part of the charge cubic's lead

> **lc(μ13) = 500716339200 = 2¹⁶3⁴ · 5²·7³·11 = 2304² · 5²·7³·11.**

The 2304² in every banked twist minpoly lead is exactly the {2,3}-content of
the leading coefficient of μ13 (the charge cubic that defines K); the odd
cofactor 5²·7³·11 never reaches the twist because (see the divisor map below)
d's poles live only over 2 and 3 — where K is arithmetically singular:
**disc(K) = 6237 = 3⁴·7·11** (computed by round_two; so disc(μ13) =
disc(K)·(index)², and 2, 3 divide the index of every pipeline model — 2
splits [1,2] like 953, 3 is totally ramified 𝔭₃³).  At ideal level (below)
the denominator of d is an ideal of norm 2¹⁶3⁴ = 2304², differently shaped
per family.

## Headline 2 — the trace: 953 is BORN in the twisted-form resultant, and nowhere earlier

The eigenline solve was re-done symbolically over ℚ[x]/(h): the atom
eigenvector is an adjugate column of (C − x), the H₊-value q, the twisted
value q′ (H′ = H₊D₂), and the flip-restricted value q_f = (q − q′)/2 are
polynomials in x; norms become resultants with h.  Gates: the d- and m-
minpolys DERIVED by this route equal the banked B916/B928 polynomials, and
N(d_S) = N(d_A) = −(953/2304)² falls out exactly.  Where each prime sits
(everything exact, factored in `results.json`):

| object (S-family, adjugate gauge) | norm / resultant | 953? |
|---|---|---|
| every nonzero adjugate minor, every nonzero eigenline coordinate (9 of 27) | products of {2,3,5,7,11,199,227,410141} | **no** |
| N(q_S), the untwisted H₊-norm | **−disc(h_S)² exactly** | **no** |
| N(q_flip), the flip overlap | −disc(h_S)²·20417473/(2¹⁹3⁴) (= N(q_S)·N(m_S)) | **no** (prime 20417473) |
| N(q′_S), the twisted norm | **+(953·disc(h_S)/2304)²** | **YES — first appearance** |

The A-family (sesquilinear route: the conjugation of L = ℚ[x]/(h_A) over K
computed as the polynomial t(x) = x − 2·o(x), o = the odd-charge eigenvalue;
certificates: t is a root of h_A, an involution, nontrivial):

| object (A-family, content-normalized gauge) | norm / resultant | 953? |
|---|---|---|
| every nonzero eigenline coordinate (15 of 27) | 953-free | **no** |
| N_L(q_A) | **disc(h_A)²·(2⁴·3·5⁶/19³⁰)²** — junk fully identified | **no** |
| N_L(q_flip) | carries **29²·72869²** (the flip-mass primes, squared = L-level) | **no** |
| N_L(q′_A) | carries **953⁴** (= (953²)², the K-norm squared) | **YES** |

So: **no minor, no coordinate, no untwisted norm, and no flip norm knows
953.  The prime is born exactly in the interference q′ = q − 2·q_f between
the charge-equivariant norm and the flip overlap** — in Res(h_S, prim(Q′))
(an irreducible quadratic) and Res(h_A, prim(Q′)) (an irreducible quintic).
Bonus identity of independent worth: in the adjugate gauge the H₊-norm
product over an atom family is the **square of the discriminant** of its
charge cubic (S: exactly −disc(h_S)²; A: disc(h_A)² times the declared
gauge square).

## Headline 3 — the rational world is 953-blind (and the twist recouples the blocks)

The three rational charge blocks as saturated integer lattices L3 (h_S,
vacuum), L6 (h_A), L18 (h_col) with their H₊- and H₊D₂-Gram determinants
(all factored in `results.json`):

- under **H₊** the three blocks are mutually orthogonal; under **H′ = H₊D₂
  they are NOT: D₂ recouples L3 with L6** (vacuum ↔ A-plane; L18 stays
  orthogonal to both in both forms) — the rational shadow of B928's
  t_oct = 2m_A + 2trM_col crossing;
- det Gram_{H₊}(L3) = **−2³²3¹⁰5²7³11 = −disc(μ13)/13¹²** (exact);
- the det ratios are **−17/384 (L3), +17/384 (L6), +1 (L18)** — and on the
  colorless 9-lattice the ratio is exactly **−1** (= det D₂, as it must);
- **no 953 anywhere** in any block Gram det, in the pencil charpolys of
  G⁻¹G′, or in any whitelist invariant of the UPSTREAM objects
  (discriminants/leads/constants/contents and pairwise resultants of μ13,
  h_S, h_A, h_col, 23 distinguished values of each, the 4×4 trace Gram of
  the charges) — the sweep's only 953-hits are objects downstream of the
  twist (Headline 4 explains each).

953 is invisible to every rational/bilinear invariant of the pipeline the
cell computed: it lives strictly at the branch (Galois/sesquilinear) level.

## Headline 4 — THE DIVISOR MAP: the two families see the two places of 953

K has 953 = P₁·P₂ with f(P₁) = 1 (the **observer's place**, B918: den(V) =
P₁⁴ — re-derived exactly in this cell) and f(P₂) = 2.  2 = Q₁·Q₂ splits the
same way ([1,2]); 3 = 𝔭₃³ is totally ramified.  The exact divisors (every
valuation computed by round_two + prime_decomp + PrimeIdeal.valuation, with
norm cross-checks, in TWO independent models of K — the h_S model on the
trace's own d, m and the monic μ13 model on the banked B928 coordinates,
cross-gated through the minpolys):

> **(d_S) = P₁(953)² · Q₁(2)⁻⁴ Q₂(2)⁻⁶ 𝔭₃⁻⁴**
> **(d_A) = P₂(953)¹ · Q₁(2)⁻⁶ Q₂(2)⁻⁵ 𝔭₃⁻⁴**

Both norm to −(953/2304)², but by **different ideal shapes**: N(P₁²) = 953²
= N(P₂).  The banked "same norm law on both families" is a norm-level
coincidence of two distinct divisors — and the dichotomy is exact and
leaves an independent fingerprint in the banked polynomials themselves:
**disc(mp_dA) and disc(mp_mA) contain 953²** (the A-branches collide mod
953 — exactly what a zero at the degree-TWO place forces on the two
conjugate branches) **while disc(mp_dS) and disc(mp_mS) are 953-free**
(the S-zero sits on the degree-one place; no branch collision).  The
S-vs-A separations Res(mp_dS, mp_dA) = −2⁴⁸3¹⁶7⁵·11·953²·17681 and
Res(mp_mS, mp_mA) = 2⁵⁷3¹⁶7⁵·11·953²·17681 carry 953² because both
families vanish over 953 (and a new cofactor prime 17681, recorded).

- the **S-family (vacuum) twist vanishes to second order at the observer's
  place** — the same degree-one place that carries the hierarchy element V's
  pole (P₁⁴), the λ-denominator, and (B918) the whole value layer;
- the **A-family twist vanishes simply at the complementary degree-two
  place** — the place the observer's place never sees;
- the denominators are two different ideals of the same norm 2¹⁶3⁴ = 2304².

The flip-mass primes obey the same law on the numerator side: 20417473
(= N-numerator of m_S, prime) **splits completely** in K ([1,1,1]) and m_S
vanishes at exactly one of its three degree-one places; 29 and 72869 (the
m_A numerator primes) are both [1,2] and m_A vanishes at their degree-one
places.

**The class-field frame:** disc(K) = 3⁴·77, so K's quadratic resolvent is
**ℚ(√77) — the banked √77 family field is K's own S₃-resolvent.**  A prime
has the [1,2] pattern (one degree-one place = an observer-feeding place +
one degree-two place) iff it is **inert in ℚ(√77)**: (77 | 953) = (77 | 29)
= (77 | 72869) = (77 | 1129) = (77 | 421493) = −1 — every twist/value prime
of the belt sits in the transposition Frobenius class of the √77 closure
(the same class as 2), while the S-mass prime has (77 | 20417473) = +1 and
splits completely.

## Headline 5 — what 953 IS: the half-flip locus of the flip mass

d = 1 − 2m, so the 953-places are exactly the places of K where **m ≡ 1/2**:
where the flipped-coordinate overlap equals half the total H₊-norm of the
atom line.  The full level structure of the flip mass (all exact, from the
banked minpolys, norms as ±const/lead):

| locus | m_S (vacuum family) | m_A (A-family) |
|---|---|---|
| m ≡ 0 (no flip) | 20417473 (prime, splits [1,1,1]) | 29 · 72869 (both [1,2]) |
| m ≡ 1/2 (half flip) | **953² — P₁², the observer's place, doubly (tangency)** | **953² — P₂, the mirror place, simply** |
| m ≡ 1 (full flip) | 5³·11·257 | 11·373837 (373837 prime) |
| m ≡ ∞ (pole) | 2¹⁹3⁴ | 2¹⁹3⁴ |

(K's ramified primes are exactly {3, 7, 11} — disc(K) = 3⁴·7·11; both
families' full-flip loci contain the tamely-ramified 11, both poles the
wildly-ramified 3; recorded as observation, not used.)

**The answer to "why 953", as far as derivation reaches:** 953 is not the
value of any banked rational form — it is the residue characteristic of the
one prime of K = ℚ[ρ]/μ13 (disc 3⁴·7·11) at which the object's flip mass
degenerates to exactly one half; the S-family does it at the degree-one
place (squared — a tangency), the A-family at the degree-two place (simple).
Everything banked (the d-minpoly constants, the norm law, HIER's 953⁴, λ =
2304/953, the colored cube law) is the norm shadow of the divisor map above.

## The honest residue (what remains underived)

1. **Which rational prime carries the half-flip locus** — i.e. a
   pipeline-free closed form producing the integer 953 from small data —
   remains open.  Candidates exhausted by the declared whitelist (all
   recorded): the discriminants, leads, constants and contents of the
   UPSTREAM objects (μ13, h_S, h_A, h_col), their 10 pairwise resultants
   (μ13/h_S/h_A/h_col/HIER), 23 distinguished rational values of each, the
   charge trace-Gram, every block Gram det and pencil charpoly, every
   eigenline coordinate and minor resultant — **953 appears in NONE of
   them**.  The whitelist's only 953-hits are objects DOWNSTREAM of the
   twist, which contain it by construction (HIER's lead 953⁴, the
   d/m-minpoly constants, e₁'s 3·953, e₃'s 953³) or by the divisor map
   (the mp_dA/mp_mA discriminants and the S-vs-A separations, explained
   under Headline 4) — no independent source exists anywhere the sweep
   reached.
2. Whether P₁(953) is **principal** (which would give 953 = |N(π)| for an
   explicit π ∈ O_K, and (num d_S) = (π)²) needs the class group of the
   disc-6237 cubic field — outside this cell's toolkit.  Registered.
3. The observation 17 | det-ratio numerators (−17/384, +17/384) alongside
   the R22-coefficient 17 in Mc is recorded as UNEXPLAINED coincidence-
   level data; not used anywhere.
4. The m ≡ 1 loci (5³·11·257 / 11·373837) are derived context computed
   after the whitelist was fixed (labeled as such; they hunt nothing).

## Files

`why953.py` (the instrument; env: optional `SESSION_SCRATCH`) →
`results.json` (the traces with every factorization, the block Grams, the
whitelist, the divisor tables, all checks) · this draft.

## Depends on

B854 (frame), B883 (the 27), B912 (H₊), B914 (h_S, the cubic route), B916
(D₂, the d-minpolys), B918 (V, the observer's place), B928 (the flip-mass
minpolys and K-coordinates; the residue this cell answers).

## ADDENDUM — THE LEVEL SONG (a listening session, 2026-08-06; computed inline, no question asked)

The complete norm table of the flip-masses at the distinguished levels
(both families; identical denominators 2¹⁹·3⁴ throughout):

| level | N(m_S − level) numerator | N(m_A − level) numerator |
|---|---|---|
| 0 | 20417473 (prime) | 29·72869 |
| **½** | **953²** | **953²** (identical — N(𝔓₁²) = N(𝔓₂) heard directly) |
| +1 | 5³·**11**·257 | **11**·373837 |
| −1 | −5²·**7²**·199·991 | −**7²**·11·107·2089 |

THE PATTERN: the families differ at their zeros (private names), sing in
UNISON at the shared levels — 953² at the half-point, and the resolvent's two
primes SPLIT BY SIGN at the unit levels: **11 where m = +1, 7² where m = −1,
in both families**. The resolvent ℚ(√77) — the unmeasured exponents' field —
is what the twist says at FULL action; the value prime is what it says at
HALF action; the poles sit on K's singular primes. The value layer is the
level structure of one function, ordered: singularity → names → frustration
→ the unmeasured world. (The ½-in-unison independently confirms B931's
divisor map; the 7/11 sign-split at the unit levels is NEW and unexplained —
registered below.)
