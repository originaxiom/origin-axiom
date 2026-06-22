"""B188 -- the driven-dissipative metallic chain (V182). Fast locks.

The dephasing Liouvillian gap (single-particle) inverts the naive 'criticality => gapless' guess: the LOCALIZED
(Aubry-Andre) chain is near-gapless (~100x smaller gap), while the permanently-critical metallic chain relaxes
like an EXTENDED chain (gap ~ periodic). The gap is homogeneous under scaling the external rates
(Delta(sH,sgamma)=s*Delta) -> no intrinsic scale. Full version in lindblad_gap.py.
"""
import numpy as np
np.seterr(over="ignore", invalid="ignore")

phi = (1 + 5**0.5)/2; alpha = 1/phi
def _H(L, kind, lam):
    n = np.arange(1, L+1)
    if kind == "metallic": V = lam*(((n*alpha) % 1.0) >= 1.0 - alpha).astype(float)
    elif kind == "aa":     V = 2*lam*np.cos(2*np.pi*alpha*n)
    else:                  V = np.zeros(L)
    H = np.diag(V).astype(complex); i = np.arange(L-1); H[i, i+1] = 1; H[i+1, i] = 1
    return H


def _gap(L, kind, lam, gamma=1.0, s=1.0):
    H = s*_H(L, kind, lam); I = np.eye(L)
    Lcoh = -1j*(np.kron(I, H) - np.kron(H.T, I))
    offdiag = np.array([[0.0 if a == b else 1.0 for b in range(L)] for a in range(L)])
    Ldis = -(s*gamma)*np.diag(offdiag.flatten("F"))
    ev = np.linalg.eigvals(Lcoh + Ldis).real
    return float(-np.max(ev[np.abs(ev) > 1e-7]))


def test_localized_is_near_gapless_critical_is_not():
    for L in (8, 10):
        gm = _gap(L, "metallic", 1.0); ga = _gap(L, "aa", 4.0); gp = _gap(L, "periodic", 0.0)
        assert gp/ga > 20 and gm/ga > 20          # localized ~100x more gapless than both extended-type
        assert 0.3 < gm/gp < 3                     # critical relaxes like extended (not anomalously slow)


def test_gap_is_homogeneous_no_intrinsic_scale():
    d1 = _gap(10, "metallic", 1.0)
    for s in (2.0, 3.0):
        assert abs(_gap(10, "metallic", 1.0, s=s)/(s*d1) - 1) < 1e-6
