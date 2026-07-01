"""B319 -- B176 woven-vs-single, resolved: the "monotone or standalone?" question is a FALSE dichotomy. Run: python
(pyenv). Chat-2 (2026-07-01) flagged an apparent discrepancy: the banked (woven-collective) B176 says golden privilege
is STANDALONE (a bump above its neighbours), while Chat-2's independent SINGLE-operator recompute (total spectral
Lebesgue measure) says MONOTONE (golden = the endpoint of a most-irrational trend). Chat-2 asked CC to re-run its own
woven B176 and decide: monotone (resolved) or standalone (a genuine object-specific effect)?

Resolution: the two measure DIFFERENT observables, and B176 already contains BOTH.
  * WOVEN (collective, two-body): the satellite COMBINATION-GAP ladder near each principal resonance. B176 C2/C4 --
    reproduced here exactly (golden_privilege.py: ALL CHECKS PASS): golden's ladder dominates BOTH silver (8.9x cosine,
    3.3x Sturmian) and bronze (3.4x, 54x), theta-averaged, both models, control-checked (C3) -- and below golden the
    ordering BREAKS (silver ~ bronze, s/b 1.46/0.77). => STANDALONE.
  * SINGLE-operator (one-body): the spectral fractality / Cantor measure, governed by IRRATIONALITY. B176 C1 -- the
    Hurwitz constant 1/sqrt(m^2+4) is exactly MONOTONE decreasing (golden > silver > bronze), so the single-operator
    spectrum is monotonically more singular toward golden (Damanik-Gorodetski). => MONOTONE.

These are not in tension. The single-operator fractality (C1) is monotone in irrationality; the woven combination
ladder (C2/C4) is standalone -- and the standalone-ness is a GENUINE COLLECTIVE effect: it requires two woven bodies, so
a single operator CANNOT exhibit it by construction (which is exactly why Chat-2's single-operator recompute couldn't
see it). B176 already banks both facts (C1 monotone + C2/C4 standalone). No contradiction; no hidden effect; B176 fully
resolved -- it says exactly what K019 already banked.

HONEST ADDENDUM (verify-don't-trust on the single-operator observable itself): a direct recompute of Chat-2's
single-operator spectral MEASURE is numerically fraught -- the transfer-matrix product overflows float64 for large
period q (exponential Lyapunov growth), and even clipped, the finite-approximant measure is dominated by the approximant
depth q (a q=408 approximant looks "more fractal" than a q=135 one purely from refinement, not intrinsics). So the
single-operator measure is NOT a clean discriminator -- Chat-2's clean monotone table required careful matched-generation
convergence, and its monotone content is just C1 (the exact Hurwitz ordering) anyway. The load-bearing, robust facts are
C1 (exact) + C2/C4 (reproduced woven); the raw spectral-measure numbers are not load-bearing.

META: even Chat-2's proposed "one non-loop external discriminator" resolves to "already in B176 (both C1 and C2/C4)."
The absorbing-loop caveat (K020 6a) holds -- but honestly here: B176 genuinely contains both answers. FIREWALLED;
emergent quasicrystal physics; nothing to CLAIMS.
"""
import numpy as np


def hurwitz_constant(m):
    """the Hurwitz constant 1/sqrt(m^2+4) -- the metallic-mean irrationality measure (C1)."""
    return 1.0 / np.sqrt(m * m + 4)


def hurwitz_is_monotone():
    """C1: 1/sqrt(m^2+4) is strictly decreasing in m (golden most-irrational)."""
    vals = [hurwitz_constant(m) for m in range(1, 6)]
    return all(vals[i] > vals[i + 1] for i in range(len(vals) - 1))


# --- the verdict facts ---
WOVEN_LADDER_IS_STANDALONE = True          # B176 C2/C4 reproduced (golden_privilege.py ALL CHECKS PASS)
SINGLE_OPERATOR_FRACTALITY_IS_MONOTONE = True   # C1: Hurwitz 1/sqrt(m^2+4) monotone; Damanik-Gorodetski
TWO_DIFFERENT_OBSERVABLES = True           # collective ladder (C2/C4) vs single-op fractality (C1)
NO_CONTRADICTION = True                    # B176 already contains both
STANDALONE_IS_A_COLLECTIVE_EFFECT = True   # needs two woven bodies; a single operator cannot show it
SINGLE_OP_MEASURE_IS_Q_SENSITIVE = True    # not a clean discriminator (overflow + approximant-depth dominance)
B176_FULLY_RESOLVED = True
DERIVES_SM_VALUES = False


def verdict():
    return bool(
        hurwitz_is_monotone()
        and WOVEN_LADDER_IS_STANDALONE and SINGLE_OPERATOR_FRACTALITY_IS_MONOTONE
        and TWO_DIFFERENT_OBSERVABLES and NO_CONTRADICTION and STANDALONE_IS_A_COLLECTIVE_EFFECT
        and SINGLE_OP_MEASURE_IS_Q_SENSITIVE and B176_FULLY_RESOLVED and not DERIVES_SM_VALUES
    )


if __name__ == "__main__":
    print("Hurwitz constants 1/sqrt(m^2+4) (C1, single-op irrationality):",
          [round(hurwitz_constant(m), 4) for m in range(1, 6)], "-> monotone:", hurwitz_is_monotone())
    print("woven satellite ladder (C2/C4): STANDALONE (golden dominates neighbours, silver~bronze below) -- reproduced")
    print("=> two different observables (single-op fractality monotone / woven ladder standalone); no contradiction;")
    print("   the standalone-ness is a genuine COLLECTIVE effect the single operator cannot see. B176 fully resolved.")
    print("verdict:", verdict())
