# B645 — C3: THE UNIT CROSS-RATIO LAW and the 13-dial

**The question (C3, the do-them-all queue):** what governs the
dial-sensitive slot of the chord's Y-tensor across the nine computed
doubles? A raw regression on Y[234] would be numerology — slot values
are basis-scale contaminated (magnitudes span 1e−7 to 1e25 across
doubles). The honest objects are the **normalization-free invariants**:
products ∏Y[s]^{n_s} whose exponents balance every mode index
(Y[ijk] ↦ cᵢcⱼcₖ·Y[ijk] under rep rescaling ⇒ invariance ⟺ the
incidence system Σ_{s∋i} n_s = 0).

Run: `b645_invariants.py` → `b645_output.txt` (parses the banked B637
stage-3 + part-2b tables — an independent transcription path; exact
sympy over ℚ(√−3)).

## Locks recovered from the independent parse

- The core law **Y[023] = 24ζ₆·Y[123]** re-verified on ALL NINE doubles
  from the re-parsed tables (9/9 exact).

## The invariant lattice

Per double the incidence system has rank 4, so: six doubles with 6
nonzero slots carry exactly ONE invariant; the three doubles with 7
nonzero slots carry TWO. The dial-sensitive slot Y[234] appears in **no
normalization-free invariant on any double** (its exponent is forced to
0) — the "one dial-sensitive slot" of the banked story is precisely the
slot the basis-free geometry cannot see alone.

## THE UNIT CROSS-RATIO LAW (exact, 6/6)

On every double where the 024-slot is SILENT (Y[024] = 0: the unbent
weld, bent m ∈ {5, 7, 11}, D_φ(a)=b, D_φ(a)=B):

> **(Y[023]·Y[134]) / (Y[034]·Y[123]) = 1 exactly** — equivalently,
> the 24ζ₆ core ratio extends to the (3,4) spectator pair:
> Y[034] = 24ζ₆·Y[134].

The mode-0 ↔ mode-1 proportionality is NOT slot-independent (on the
024-silent doubles Y[024] = 0 while Y[124] ≠ 0), so this is a genuine
second identity, not a corollary of a cochain-level proportionality.

## The 13-dial (exact, 3/3 + 4/4 deviations)

On the three 024-LIT doubles — bent m = 1, D_φ(a)=a, D_φ(a)=A — every
invariant deviates from 1, and **every deviation is divisible by 13**
(numerator divisible by 13 in lowest terms; all denominators coprime
to 13). Exact normal forms:

| double | invariant | value |
|---|---|---|
| D_φ(a)=a, D_φ(a)=A | inv1 | 1 + 13·ζ₃/3696 |
| D_φ(a)=a, D_φ(a)=A | inv2 | **(3⁸ + 13√−3)/(3⁸ + 13)** |
| bent m=1 | inv1 | 1 + 13/3696 (real) |
| bent m=1 | inv2 | 1 + 13·(6613 + 13√−3)/21866138 |

So the dial statement, 13-adically: **v₁₃(cross-ratio − 1) ≥ 1 on every
computed double, with equality-to-∞ (i.e. exactly 1) precisely on the
024-silent class.** 13 = 1 + 3·2² splits in ℚ(√−3) (N(1 + 2√−3) = 13).

## Status and routing

- Strength: **LAW** (exact on every computed instance; mechanism open).
  This replaces C3's sketched "regression against τ_m" with something
  strictly stronger: exact identities, zero fitted parameters.
- The lit class {m=1, φ(a)=a, φ(a)=A} is exactly the banked "m = 1
  dial" class (the zero law Y[01k] ≡ 0 off m = 1) — the two dials
  agree; one classification, two witnesses.
- HINT rows (recorded, not judged): the 3⁸ in inv2's normal form
  (8 = the Sym⁸ block's highest weight?); 13 = (27 − 1)/2; the
  deviation units {1, ζ₃, √−3} are associates-shaped.
- No SM numbers; internal exact arithmetic only; Gate 5 untouched.

## Reproduction

- `python3 frontier/B645_dial_law/b645_invariants.py` (~seconds).
- `tests/test_b645_dial_law.py` — the locks (parse + all identities).
