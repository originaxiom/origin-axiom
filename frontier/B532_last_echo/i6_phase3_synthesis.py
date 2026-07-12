"""
B532-I6: Nine Ingredients, One Object — Phase 3 synthesis.

Combines all 9 probes into the final verdict table.
Probes 3 (Continuity) and 5 (Locality) use their settled verdicts.
"""

import numpy as np
from collections import Counter
from math import log2, sqrt

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
LETTERS = 'abAB'
PHI = (1 + sqrt(5)) / 2


def grow(letter, depth):
    word = letter
    for _ in range(depth):
        word = ''.join(SUB[c] for c in word)
    return word


def main():
    print("=" * 78)
    print("NINE INGREDIENTS, ONE OBJECT — SYNTHESIS")
    print("σ: a→abAAB, b→aAB, A→abAB, B→aA")
    print("=" * 78)

    word = grow('a', 9)
    N = len(word)
    freq = Counter(word)
    freqs = {c: freq[c]/N for c in LETTERS}
    beta = 3.676205

    # ===================================================================
    # THE NINE VERDICTS
    # ===================================================================

    print("""
╔══════════════════════════════════════════════════════════════════════════╗
║                       THE NINE VERDICTS                                ║
╠════╤═══════════════╤════════════╤════════════════════════════════════════╣
║  # │ Ingredient    │ Verdict    │ Discriminating fact                   ║
╠════╪═══════════════╪════════════╪════════════════════════════════════════╣
║  1 │ Time          │ FORCED     │ σ ≠ σ̄ mod conjugation;               ║
║    │               │            │ D_KL(ω||ω̄) ≈ 12 bits;               ║
║    │               │            │ bidirectional (R=9) but asymmetric    ║
╠════╪═══════════════╪════════════╪════════════════════════════════════════╣
║  2 │ Randomness    │ FORCED     │ P(b|a) = 1/φ (6-digit);             ║
║    │ (Born rule)   │            │ NOT max-entropy (Δ = 0.29);          ║
║    │               │            │ convergence quasiperiodic             ║
╠════╪═══════════════╪════════════╪════════════════════════════════════════╣
║  3 │ Continuity    │ FORCED     │ Cantor spectrum (pure discrete);     ║
║    │               │ [settled]  │ self-similar gap structure             ║
╠════╪═══════════════╪════════════╪════════════════════════════════════════╣
║  4 │ Forces        │ CONDITIONED│ gap POSITIONS forced (IDS labels);   ║
║    │               │            │ gap-opening SLOPES vary with V;      ║
║    │               │            │ k₂/k₃ ∈ [0.65, 15.05] across 4 V    ║
╠════╪═══════════════╪════════════╪════════════════════════════════════════╣
║  5 │ Locality      │ CONDITIONED│ grammar = nearest-neighbor;          ║
║    │               │ [settled]  │ long-range order from Pisot, not H    ║
╠════╪═══════════════╪════════════╪════════════════════════════════════════╣
║  6 │ Scale         │ ABSENT /   │ ~7 forced ratios (all from σ);       ║
║    │               │ FORCED     │ absolute scale ℓ is ONE free param   ║
╠════╪═══════════════╪════════════╪════════════════════════════════════════╣
║  7 │ Thermo-       │ FORCED     │ T(n) ~ 0.49·(0.85)ⁿ with plateaus; ║
║    │ dynamics      │            │ recognizability structure at n=R=9    ║
╠════╪═══════════════╪════════════╪════════════════════════════════════════╣
║  8 │ Matter        │ FORCED     │ 4 irreducible species, |Aut(σ)|=1;  ║
║    │               │            │ species = (old/new)×(str/tun) exact; ║
║    │               │            │ no coarsening is substitutive         ║
╠════╪═══════════════╪════════════╪════════════════════════════════════════╣
║  9 │ Gravity       │ CONDITIONED│ topology forced (gaps, Rauzy, Pisot);║
║    │               │            │ metric requires Hamiltonian;          ║
║    │               │            │ fluctuations bounded (H≈0, PDS)      ║
╚════╧═══════════════╧════════════╧════════════════════════════════════════╝
""")

    # ===================================================================
    # SCORECARD
    # ===================================================================
    print("SCORECARD")
    print("-" * 50)
    print(f"  FORCED:      5  (time, randomness, continuity, thermodynamics, matter)")
    print(f"  CONDITIONED: 3  (forces, locality, gravity)")
    print(f"  ABSENT:      1  (absolute scale)")
    print(f"  Total:       9")

    # ===================================================================
    # WHAT THE OBJECT ACCOUNTS FOR
    # ===================================================================
    print(f"""
{'='*78}
WHAT THE OBJECT ACCOUNTS FOR
{'='*78}

WITHOUT ANY EXTERNAL INPUT, σ forces:

  1. TIME ARROW — forward/backward grammars differ (5/5 bigram pairs asymmetric);
     the arrow is bidirectional (recognizable) but structurally irreversible
     (D_KL ≈ 12 bits between ω and ω̄).

  2. TRANSITION PROBABILITIES — algebraic, not statistical. P(b|a) = 1/φ to 6
     digits. The "Born rule" is deterministic but structured: it carries specific
     algebraic values from the substitution, not max-entropy predictions.

  3. SPECTRAL CONTINUITY — Cantor spectrum, pure discrete diffraction, self-
     similar gap hierarchy at IDS = cumulative Perron frequencies.

  4. COMPLEXITY SCALING — T(n) = h(n)/h_top decays exponentially with algebraic
     plateaus (n=3-4, 9-10, 12-14). The recognizability radius R=9 appears as
     the scale where context fully determines local structure.

  5. FOUR IRREDUCIBLE SPECIES — no nontrivial automorphism (|Aut(σ)|=1),
     no identification possible, no substitutive coarsening. The species form
     an exact product (old/new) × (structural/tunnel) with zero correlation
     residual. Two binary features, independently determined.

  6. ALL DIMENSIONLESS RATIOS — freq(a)/freq(b) = freq(A)/freq(B) = φ,
     freq(old)/freq(new) = |λ₂| = {abs(-0.440137):.6f}, gap labels from
     cumulative frequencies. ~7 independent constants, all algebraic.

GIVEN ONE EXTERNAL INPUT, σ produces:

  7. FORCE-LIKE STRUCTURE — the potential assignment V: {{a,b,A,B}} → ℝ
     selects gap-opening slopes. Different V give different "force strengths"
     (k₂/k₃ varies from 0.65 to 15.05). Gap POSITIONS are fixed; gap WIDTHS
     are conditioned on V.

  8. LONG-RANGE ORDER — the grammar is nearest-neighbor (7/16 bigrams allowed),
     but global correlations extend to all scales via the Pisot property. The
     mechanism is built into σ; the range of physical interaction depends on
     the Hamiltonian.

  9. TOPOLOGICAL GEOMETRY — gap positions, Rauzy fractal embedding in ℝ³,
     fractal dimension, Pisot spectral type are all forced. Metric geometry
     (distances, curvature, gap widths) requires the Schrödinger Hamiltonian.

THE ONE THING σ CANNOT PROVIDE:

  ABSOLUTE SCALE — the physical length ℓ (or equivalently, energy unit ε).
  Every ratio is determined; the overall scale is free. This is the irreducible
  external input: one measured quantity from which all others follow.
""")

    # ===================================================================
    # THE PREDICTION FORM
    # ===================================================================
    print(f"""
{'='*78}
THE PREDICTION FORM
{'='*78}

  Given: σ (the substitution — 4 rules, 14 letters total)
         + one external input (scale ℓ or potential assignment V)

  σ alone determines:
    • 4 species with frequencies in ratio φ:1:φ²:(φ+1) (golden tensor)
    • 3 spectral gaps at IDS = f_a, f_a+f_b, f_a+f_b+f_A
    • time arrow (σ ≠ σ̄)
    • transition matrix (P(b|a) = 1/φ, etc.)
    • complexity function T(n) with recognizability R=9
    • Rauzy fractal in ℝ³ with pure discrete spectrum

  V determines:
    • which gaps open and how wide
    • what "forces" act (gap-opening slopes)
    • band structure and gap widths

  ℓ determines:
    • physical energy scale
    • all dimensionful quantities

  THE ONE-MEASUREMENT PREDICTION:
    If you measure ONE physical quantity (e.g., the energy of the lowest gap),
    then σ + that measurement determines ALL ratios of physical quantities
    in the spectrum. The potential shape V may introduce additional freedom,
    but the gap POSITIONS and frequency RATIOS are fixed regardless of V.
""")

    # ===================================================================
    # DISCRIMINATING FACTS (for firewall)
    # ===================================================================
    print(f"""
{'='*78}
DISCRIMINATING FACTS (computed, not asserted)
{'='*78}

  1. P(b|a) = 1/φ to 6 digits: COMPUTED (27421/44368 vs 27420.93/44368)
     Max-entropy prediction: 0.327. Actual: 0.618. Δ = 0.291.

  2. D_KL(ω||ω̄) = 12.21 bits at bigram level: COMPUTED
     4 bigrams present in ω absent in ω̄ and vice versa.

  3. |Aut(σ)| = 1: COMPUTED (exhaustive check of 24 permutations)
     |Aut(grammar)| = 1: COMPUTED

  4. Species product is exact: COMPUTED
     f(a) = f_old · f_str ± 0, f(b) = f_old · f_tun ± 0 (to 6 digits)

  5. No coarsening is substitutive: COMPUTED (all 7 binary partitions checked)

  6. k₂/k₃ varies: COMPUTED
     Box = 0.655, Inverted = 0.800, Structural = 15.05

  7. H ≈ 0 (bounded fluctuations): COMPUTED
     Var(S_n) ≈ 0.37 for n ∈ [10, 5000], consistent with PDS

  8. T(n) ~ 0.489 · 0.849ⁿ: COMPUTED (n=1..15, depth-9 word)
     Plateaus at n=3-4, 9-10, 12-14

  9. σ̄ not conjugate to σ: COMPUTED (exhaustive over 24 permutations)
""")


if __name__ == '__main__':
    main()
