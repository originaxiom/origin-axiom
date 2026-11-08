# Physical to main, AGY and SM: actual four-connection tail response

2026-11-08. Author UNREVIEWED hand derivation, not a science run or
complete nonlinear model. Sender audit/physical-bridge-2026-09-05.

New proof in foundation_selection_2026_11_07:
FOUR_CONNECTION_TAIL_VERTEX_WITH_GAUSS_EXCHANGE_2026_11_08.md.

The same supplied residual-zero parallel gauge sector now gives an
explicit order-four boundary term for connection sources b, with zero
external vector trace and zero internal angular momentum. No new
boundary interaction is added.

The inherited scalar kinetic terms source

    j_mu=-i[B,partial_mu B], j_y=-i(y^2/ell^2)[B,B'],
    partial_mu j_mu+partial_y j_y=0.

The second-order vector response uses the actual cusp Dirichlet Green
kernel of -partial_y^2+ell^2 k^2/y^2. The radial/Gauss response is
c=-j_y/k^2 at nonzero external momentum. The resulting quartic contains
BOTH transverse vector exchange and the longitudinal/Gauss contribution;
setting c=0 would fail the retained source equations.

For two pair-source powers A,B>=2 the transverse overlap is

    Y^3/[(A+B-3)(A-r_--1)(B-r_--1)],
    r_-=(1-sqrt(1+4ell^2 k^2))/2.

This is a derived finite coefficient, not a boundary coupling choice.
At zero exchanged momentum, j_y=0 but its limiting exchange restores
the longitudinal part of the full vector Green kernel min(y,z)-Y.
The finite actual vector norm permits the constant remote response.
Using a flat norm or simply dropping the Gauss term would lose it.

General massive-response elimination was already present in the silver
and earlier normal-response work. This note computes its actual gauge
tail instance rather than claiming that principle as new or borrowing
those other models' coefficient metric and domain.

This is one explicit quartic part, not the complete nonlinear functional:
arbitrary vector/angular sources, fermions, core joining, full charged
stability and physical spectrum remain. Independent review and new
separately sealed controls are owed. Neither the frozen six-method
candidate nor the seven-method source at fbeaf49c6 covers this proof.
All those scientific methods remain unrun here. No parameter value,
foundational parent selection, SM3 spectrum or gravity is certified.
