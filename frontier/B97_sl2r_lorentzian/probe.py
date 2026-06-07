"""B97 -- where Lorentzian structure lives: the SL(2,R)/Teichmuller component vs the SL(2,C) geometric one.

Neutral low-dim-topology / Lie-theory mathematics; the 2+1-gravity reading is quarantined in
speculations/archive/PHYSICS_RESONANCES.md and is NOT used here.

B96 computed the volume Hessian on the SL(2,C) GEOMETRIC (hyperbolic-3-manifold) component and found it
NEGATIVE DEFINITE -- signature (0,2), Euclidean (Mostow: the complete structure maximizes volume). The
once-punctured-torus FIBER, however, also has an SL(2,R) (Fuchsian / Teichmuller) component, which is the
phase space of (2+1)-dimensional gravity (Witten 1988: 2+1 gravity = Chern-Simons of SL(2,R)). This probe
locates the Lorentzian structure precisely.

(1) THE GAUGE-ALGEBRA SIGNATURE. The trace/Killing form tr(XY) on the gauge algebra:
        sl(2,R) = so(2,1):  signature (2,1)  -- the (2+1) MINKOWSKI metric (LORENTZIAN)
        su(2)   = so(3):    signature (0,3)  -- EUCLIDEAN
    So the Lorentzian (2,1) form is the Killing form of sl(2,R); it is absent on the compact/su(2) side.

(2) THE REAL COMPONENT EXISTS. The fiber group F_2 = <X,Y> admits an explicit SL(2,R) FUCHSIAN
    representation (a Teichmuller point of the once-punctured torus): X,Y real, det 1, |tr|>2 (hyperbolic),
    and tr[X,Y] = -2 (the boundary/puncture is parabolic). This is a genuine SL(2,R) point, distinct from
    the SL(2,C) geometric 3-manifold rep that B96 used.

(3) LOCAL LORENTZ INVARIANCE. The SL(2,R) holonomy acts on the gauge algebra by the adjoint, and Ad(g)
    PRESERVES the (2,1) Minkowski form (Ad^T G Ad = G to ~1e-15): the holonomy acts by SO(2,1) Lorentz
    transformations. This is the local Lorentz structure of 2+1 gravity.

VERDICT (mathematics): Lorentzian structure IS present -- but it is the so(2,1) = sl(2,R) GAUGE-ALGEBRA
(Killing-form) signature on the SL(2,R)/Teichmuller component, i.e. the 2+1 Minkowski metric. It is
STRUCTURAL (the gauge group of 2+1 gravity is the Lorentz group), present by construction, NOT an emergent
or derived feature of the geometry. So B96 (Euclidean on the geometric component) + B97 (Lorentzian
gauge-algebra on the real component) precisely locate where the Lorentzian form is and is not. (The 2+1
mathematical-physics reading -- and the caveat that 2+1 gravity is a solvable toy model with no local
gravitons, not 3+1 fundamental physics -- is in the quarantine.)

Standalone Lie theory / low-dim topology; no physics claim; no Origin-core claim; P1-P16 untouched.
"""
from __future__ import annotations

import numpy as np

_H = np.array([[1, 0], [0, -1]], float)
_E = np.array([[0, 1], [0, 0]], float)
_F = np.array([[0, 0], [1, 0]], float)
_SL2R = [_H, _E + _F, _E - _F]                       # a basis of sl(2,R)
_PAULI = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex),
          np.array([[1, 0], [0, -1]], complex)]
_SU2 = [1j * s for s in _PAULI]                      # a basis of su(2)


def _trace_form_signature(basis):
    n = len(basis)
    G = np.array([[np.trace(basis[i] @ basis[j]).real for j in range(n)] for i in range(n)])
    ev = np.linalg.eigvalsh(G)
    return (int(np.sum(ev > 1e-9)), int(np.sum(ev < -1e-9))), G


def gauge_signatures():
    """(sl(2,R) signature, su(2) signature) of the trace form -- (2,1) Lorentzian vs (0,3) Euclidean."""
    return _trace_form_signature(_SL2R)[0], _trace_form_signature(_SU2)[0]


def fuchsian_fiber_rep():
    """An explicit SL(2,R) Fuchsian rep of the once-punctured-torus fiber F_2=<X,Y>: real, det 1, |tr|>2,
    tr[X,Y] = -2 (parabolic boundary). Returns (X, Y, tr_commutator)."""
    X = np.array([[1, 1], [1, 2]], float)
    Y = np.array([[1, -1], [-1, 2]], float)
    comm = X @ Y @ np.linalg.inv(X) @ np.linalg.inv(Y)
    return X, Y, float(np.trace(comm))


def holonomy_preserves_minkowski():
    """Ad(g) for an SL(2,R) holonomy element preserves the (2,1) form (local Lorentz / SO(2,1)). Returns
    the max deviation |Ad^T G Ad - G|."""
    _, G = _trace_form_signature(_SL2R)
    X = fuchsian_fiber_rep()[0]
    ad = [X @ b @ np.linalg.inv(X) for b in _SL2R]
    B = np.array([b.flatten() for b in _SL2R]).T
    Adm = np.linalg.lstsq(B, np.array([a.flatten() for a in ad]).T, rcond=None)[0]
    return float(np.max(np.abs(Adm.T @ G @ Adm - G)))


def main():
    print("B97 -- where Lorentzian structure lives: SL(2,R)/Teichmuller vs SL(2,C) geometric\n")
    sR, su = gauge_signatures()
    print(f"(1) gauge-algebra trace-form signature:  sl(2,R)=so(2,1) -> {sR} (LORENTZIAN, 2+1 Minkowski); "
          f"su(2)=so(3) -> {su} (Euclidean)")
    X, Y, trc = fuchsian_fiber_rep()
    print(f"(2) explicit SL(2,R) Fuchsian fiber rep:  det X={np.linalg.det(X):.0f}, tr X={np.trace(X):.0f}, "
          f"tr[X,Y]={trc:.1f} (parabolic boundary => Teichmuller point; distinct from the SL(2,C) geometric rep)")
    dev = holonomy_preserves_minkowski()
    print(f"(3) Ad(holonomy) preserves the (2,1) Minkowski form:  max|Ad^T G Ad - G| = {dev:.1e}  (SO(2,1) local Lorentz)")
    print("\n=> B96 (geometric side, Euclidean (0,2)) + B97 (real side, Lorentzian gauge algebra (2,1))")
    print("   locate the Lorentzian form precisely: it is the so(2,1) gauge structure on the SL(2,R)")
    print("   component (the 2+1-gravity phase space) -- STRUCTURAL, not emergent. (Reading: quarantine.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
