# Weave quantum realization — Run 2

Start with `TECHNICAL_REPORT.md`. This is a mathematical continuation, not a completed quantum or gravitational theory.

## Reproduce

Python 3.10+ with SymPy and mpmath:

```sh
python -m pip install -r requirements.txt
python verify_cover_states.py
python verify_cover_states.py --reverse-tree
python verify_quantum_reduction.py --dps 80
python verify_quantum_reduction.py --dps 100
```

The scripts write JSON outputs beside themselves. Each normally runs in seconds.
There are 52 named checks across the two scripts, including enumeration of all 64 compact spin structures.

## What is genuinely established

- Reconstructed faithful Q8 cover and exact L,R/deck homology actions.
- Compact holomorphic forms split 1+2 under Q8.
- Degree-two theta-section doublet; its quadratics recover the three theta-squared functions.
- No compact spin structure invariant under all deck Q8; one odd spin invariant under the specified based L,R lifts.
- Analytic kernel/cokernel counts for two explicitly stated parabolic Dolbeault extensions.
- Exact factorization of the target metaplectic multiplier into an eta-cubed scalar and a 24-element rotation action.

## Do not promote these to

- Three elementary fermion zero modes or three derived generations.
- A calculated Q8-twisted CFT determinant, connection or puncture correlator.
- A derivation of the eta-cubed scalar from dynamics.
- Gauge chirality, a Standard Model fit, or gravity.

## Next task for an agent or researcher

Specify a faithful field theory and puncture domain first. Then compute the family determinant/Pfaffian line and zero-mode-saturating insertions. Compare its actual S,T and central holonomies with the explicitly recorded scalar eta-cubed character. Do not tensor in that character merely to obtain agreement.
