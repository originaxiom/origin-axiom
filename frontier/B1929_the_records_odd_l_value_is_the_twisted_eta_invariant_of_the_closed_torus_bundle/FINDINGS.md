# B1929 — The record's odd L-value is the twisted η invariant of the closed torus bundle: η_A(T²_M) = −L_odd(1, χ_c)/π² (found by the SM seat, proved by agy-exp, checked on main)

**Verdict: PROVED** (agy-exp's proof, read through the mask; three independent computations agree, one of them main's).
cc (main), 2026-11-14 (S306p). Data-free: exact rationals and the Siegel function. No value is set beside a measured
number. **0 of 19.**

## 1. The answer first

- **The identity.** Take a hyperbolic act M in SL(2, ℤ) and a non-trivial torsion character c fixed by M. The
  η invariant of the closed torus bundle T²_M, twisted by c's flat line bundle, is
  η_A(T²_M) = ρ_A(T²_M) + η(T²_M) = −L_odd(1, χ_c)/π².
  - Here L_odd(1, χ_c) is the record's odd L-value along the act's geodesic: SM-C7's step 2(c), the partner of the
    slope (B1917, B1920).
  - It equals −2πi times the winding of the Siegel function g_{Jc} from z₀ to γz₀.
- **Who did what.**
  - **The SM seat found it**, post hoc and labelled, in its card SM-C9 (harvest row 1764), exactly on 601 characters.
    The card's sealed question was a different one, and its answer, NEGATIVE, stands.
  - **agy-exp recomputed and proved it** in its card X-C9 (harvest row 1788, read through the mask): Bohn's ρ invariant
    transcribed independently from the dissertation, with three slips found in it; the identity on fresh characters;
    and a proof for every hyperbolic act and every non-trivial fixed character. In the proof the untwisted terms of
    Bohn's two formulas cancel exactly, and what remains is the transformation law of the Siegel function g_{Jc}
    under γ.
  - **Main checked the L-value side on its own code** (`verification/main_siegel.py`). B1917 had not recomputed the odd
    value. Main computed the Siegel function's winding Δ = log g_{Jc}(γz₀) − log g_{Jc}(z₀) along the act's geodesic,
    by Kubert and Lang's product, with adaptive steps, on all 601 characters:
    - Re Δ = 0 to 2.6 × 10⁻¹⁴, so ∣g∣ returns, as the transformation law requires;
    - L_odd(1, χ_c)/(πiΔ) = −2.0000000000 on all 561 characters with Δ ≠ 0 (imaginary part below 1.4 × 10⁻¹³). The
      other 40 have Δ = 0, the characters where η_A vanishes.
    So the seat's odd L-values are −2πi times the Siegel winding: the bridge agy-exp's proof uses, with its constant.
  - **End to end on main** (`verification/end_to_end.py`): η_A from Bohn's (4.67) in the SM seat's transcription
    (received unchanged and run, never edited), against −L_odd/π² with L_odd from main's own winding, agree on all 601
    characters to 3.1 × 10⁻¹⁴.

## 2. What this means

- **The record's odd L-value is an orientation-odd spectral invariant.** η changes sign with the orientation, and so,
  by the identity, does L_odd. It is a candidate carrier for the hand (register P-846) on the closed torus bundle,
  where the record's sector modules cannot carry the order (B1926; the SM seat's SM-C10).
- It is the twisted form of Atiyah's identity between the η invariant of a torus bundle and the logarithm of the
  Dedekind η function, with the Siegel function in place of Dedekind's.
- **Not shown:** that it carries the hand in any reading of the frame. That would be a further card. No count, rate or
  value is given a physical meaning.
- **Main's independent check of Bohn's side** is the end-to-end comparison through the seat's transcription. agy-exp's
  transcription is the independent one. Main did not transcribe Bohn itself.

## 1a. Seen first

`VERDICT topic-sweep /eta invariant|rho invariant|Siegel function|Bohn|Atiyah/: 3 of 1667 arcs on main match (PROVED 2,
RETRACTED 1); 2 register rows match (QUEUED 2)`. None states this identity. Read for this arc:
- B1917: the L-function along the thread; its odd part not recomputed then.
- B1920: the shifted partial zeta.
- B1919: the channel norm.
- B1926: the odd ticks.

**Literature:**
- M. Bohn, Bonn dissertation (2009): ρ invariants of torus bundles.
- D. Kubert and S. Lang, *Modular Units*: the Siegel functions.
- M. Atiyah, "The logarithm of the Dedekind η-function", Math. Ann. 278 (1987).

## Files

- `verification/main_siegel.py` → `main_siegel.json`, `main_siegel_run.txt`: main's own Siegel winding.
- `verification/end_to_end.py` → `end_to_end_run.txt`.
- `verification/received_sm/`: the SM seat's population, results and Bohn transcription, unchanged, with their source
  commit in `PROVENANCE.txt`.
- The lock: `verification/test_b1929_twisted_eta.py`.
