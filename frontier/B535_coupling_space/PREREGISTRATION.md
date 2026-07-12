# B535 — The Coupling Space (pre-registration)

*Committed before compute, 2026-07-12. The reframed program's stage 1: the
owner's directive — the structure/value split is not the end of the ToE
question; it reframes it. Explore the coupling space ENTIRELY, quantify the
one-measurement claim, catalog the forced relations. The SM comparison
(relations, not values) is a LATER campaign with its own prereg and controls.*

## Cell C1 — Coupling census completion (does the type space saturate?)

B533 classified couplings for factor windows |u| ≤ 4: exactly 5 Perron types.
Durand's theorem (1998) guarantees a primitive substitutive sequence has
FINITELY many derived systems over all factors — so the census MUST saturate.
Compute |u| = 1..8 (host depth 11):
  (a) number of distinct Perron types per length, cumulative;
  (b) number of distinct canonical induced systems (the finer invariant);
  (c) the saturation length.

**Predictions** (stated before compute): Perron types saturate at 5;
canonical systems saturate at ~7 (B530's induction census found 7 canonical
types). **Falsifier**: new types appearing at length 7-8 with no sign of
saturation → the B533 "5 types" claim was a length artifact; retract.

## Cell C2 — The one-measurement test (word level)

Matrix level is already a THEOREM (B533 audit): measuring β fixes the
abelianization uniquely up to GL(4,ℤ) (maximal order, h = 1,
Latimer–MacDuffee). The open question is WORD level: the same matrix M
lifts to 60·6·24·2 = 17,280 substitutions (words with σ's image Parikh
vectors). Compute, for ALL 17,280 lifts:
  (a) the bigram grammar (adjacency set) of the generated language;
  (b) how many have exactly σ's banked 7/16 grammar;
  (c) among those, how many have σ's full language (factor sets to length 6);
  (d) the count of distinct languages across all lifts.

**Prediction**: the grammar+language cut is a small set (≤ ~dozens)
containing σ; NOT unique (free-group/conjugation moves preserve language).
The deliverable number: |{lifts with σ's language}| and |{distinct languages}|.
**Falsifier of the one-measurement hope**: if the distinct-language count is
in the thousands with no structure, one measurement + grammar constrains
almost nothing at word level; report as the honest bound.

## Cell C3 — The relations catalog (measure one, compute all)

All read-outs live in ℚ(τ), τ = √φ. For every distinct Perron component x
across the 5 types (16 values, B533):
  (a) the degree of x over ℚ (4 = complete measurement; < 4 = degenerate);
  (b) for complete x: the explicit polynomial g ∈ ℚ[x] with τ = g(x)
      (then EVERY other read-out is a known expression in the one measured x);
  (c) the list of degenerate read-outs and what they fail to determine.

**Prediction**: most components are degree 4 (complete); the degenerate ones
are the symmetric combinations (e.g. f_a + f_A = φ − ... lives lower).
**Deliverable**: the read-out dictionary — the literal "one measurement
determines the rest" table, exact.

## Method

Engine: B530 return-word induction (`listen_39_induction_engine`); exact
algebra via sympy in ℚ(τ) = ℚ[t]/(t⁴−t²−1). No SM numbers anywhere in this
campaign. Locks in `tests/test_b535.py`.
