"""B109 -- the trace-map DYNAMICS at the void (D2 / CC-web Task 2+6).

The figure-eight trace map iterated near the trivial fixed point (the "void"). The CC-web probing session
reported three empirical facts (a bounded z-direction; a slow asymmetry mode; the void a critical point of kappa).
VERIFY-DON'T-TRUST found the *coordinate-axis* versions do NOT reproduce -- but the rigorous LINEARIZATION does,
and it UNIFIES and sharpens them:

  * SL(2): the trace map is T1(x,y,z)=(z,x,xz-y) (B67); the figure-eight monodromy is T1^2. At the void (2,2,2)
    the Jacobian DT1^2 has eigenvalues {1, phi^4, phi^-4} -- ONE center direction (lambda=1), one unstable
    (phi^4), one stable (phi^-4). The center eigenvector is (1,-1,-1), the A<->B ASYMMETRY direction -- so the
    "bounded direction" and the "slow asymmetry mode" are the SAME object (the handoff's Fact 1 = Fact 2). Along
    it the nonlinear orbit stays bounded (max|v|~3.46 at eps=1e-3, matching the reported 3.47) but only locally
    (larger eps escapes). The Lyapunov exponents are {0, +-4 log phi}.

  * The void is a CRITICAL POINT of kappa = tr[A,B] = x^2+y^2+z^2-xyz-2 (grad = 0 at (2,2,2)); its Hessian has
    eigenvalues {-2, 4, 4}, signature (2,1) -- a SADDLE (Fact 3 + the classification). (Note kappa=+2 at the
    void; the parabolic/geometric cusp is kappa=-2, B98/B101 -- the correction the COSMOGONY draft got wrong.)

  * SL(3): the trivial-point Jacobian IS the Dickson tower (B89-T); its 8 eigenvalue magnitudes are the tower
    {1,1,phi^2,phi^-2,...}, of which exactly TWO have |lambda|=1 (the {1,-1} parity sector). So the void's
    CENTER MANIFOLD = the root-of-unity (parity) sector of the tower: dim 1 at SL(2), dim 2 at SL(3). The
    "number of bounded directions" is a TOWER invariant, not a coordinate count.

Standalone trace-map dynamics; NO physics (the eigenvalues are mathematical structure); no CLAIMS.md promotion;
proven core P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import numpy as np
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_B103 = _load("b109_b103", "frontier/B103_tower_equivariance/probe.py")

_PHI = (1 + np.sqrt(5)) / 2


# --------------------------------------------------------------------------- #
# the SL(2) trace map and the void
# --------------------------------------------------------------------------- #
def _T1(v):
    x, y, z = v
    return np.array([z, x, x * z - y])


def _T1sq(v):
    return _T1(_T1(v))


def sl2_void_linearization():
    """DT1^2 at the void (2,2,2): eigenvalues {1, phi^4, phi^-4} (1 center, 1 unstable, 1 stable); the center
    eigenvector is the A<->B asymmetry (1,-1,-1); Lyapunov exponents log|lambda| = {0, +-4 log phi}."""
    x, y, z = sp.symbols("x y z")
    T1 = [z, x, x * z - y]
    T1sq = [e.subs({x: T1[0], y: T1[1], z: T1[2]}, simultaneous=True) for e in T1]
    J = sp.Matrix(3, 3, lambda i, j: sp.diff(T1sq[i], (x, y, z)[j])).subs({x: 2, y: 2, z: 2})
    eig = {sp.nsimplify(k, [sp.sqrt(5)]): m for k, m in J.eigenvals().items()}
    vals = np.array([complex(complex(k)) for k in J.eigenvals()])
    center = [v for v in vals if abs(abs(v) - 1) < 1e-9]
    unstable = [v for v in vals if abs(v) > 1 + 1e-9]
    stable = [v for v in vals if abs(v) < 1 - 1e-9]
    # center eigenvector
    cvec = None
    for val, _, vecs in J.eigenvects():
        if sp.simplify(val - 1) == 0:
            cvec = [int(c) for c in vecs[0]]
    return {"eigenvalues_symbolic": {str(k): int(m) for k, m in eig.items()},
            "n_center": len(center), "n_unstable": len(unstable), "n_stable": len(stable),
            "center_eigvec": cvec, "center_is_asymmetry": cvec in ([-1, 1, 1], [1, -1, -1]),
            "lyapunov": sorted([round(float(np.log(abs(v))), 4) for v in vals]),
            "four_log_phi": round(float(4 * np.log(_PHI)), 4)}


def sl2_center_orbit(epsilons=(1e-4, 1e-3, 1e-2), steps=2000):
    """Nonlinear orbit along the center eigenvector (-1,1,1) (Lyapunov 0, marginal): LOCALLY bounded -- max|v|~3.46
    at eps=1e-3, slowly escaping for larger eps; the quadratic nonlinearity is sign-sensitive (the +(-1,1,1) ray
    is the bounded one). Honest scope: a genuine center direction (lambda=1 exactly), locally bounded only."""
    d = np.array([-1.0, 1.0, 1.0]) / np.sqrt(3)        # the lambda=1 eigenvector (= A<->B asymmetry)
    out = {}
    for eps in epsilons:
        v = np.array([2.0, 2.0, 2.0]) + eps * d
        mx = 0.0
        for _ in range(steps):
            v = _T1sq(v)
            nv = float(np.linalg.norm(v))
            if not np.isfinite(nv) or nv > 1e6:
                mx = float("inf")
                break
            mx = max(mx, nv)
        out[eps] = round(mx, 4) if np.isfinite(mx) else mx
    return out


def kappa_void_critical_point():
    """The void is a critical point of kappa=tr[A,B]; its Hessian has eigenvalues {-2,4,4}, signature (2,1) =
    a SADDLE. (kappa=+2 at the void; the parabolic cusp is kappa=-2, B98/B101.)"""
    x, y, z = sp.symbols("x y z")
    K = x * x + y * y + z * z - x * y * z - 2
    at = {x: 2, y: 2, z: 2}
    grad = [int(sp.diff(K, v).subs(at)) for v in (x, y, z)]
    H = sp.hessian(K, (x, y, z)).subs(at)
    eig = {int(k): int(m) for k, m in H.eigenvals().items()}
    pos = sum(m for k, m in eig.items() if k > 0)
    neg = sum(m for k, m in eig.items() if k < 0)
    return {"kappa_at_void": int(K.subs(at)), "grad": grad, "is_critical": grad == [0, 0, 0],
            "hessian_eigenvalues": eig, "signature": (pos, neg), "type": "saddle (indefinite)"}


# --------------------------------------------------------------------------- #
# SL(3): the center manifold = the tower's root-of-unity (parity) sector
# --------------------------------------------------------------------------- #
def sl3_void_center_count(word=("U", "L")):
    """SL(3) trivial-point Jacobian (the Dickson tower) eigenvalue magnitudes; # of |lambda|=1 center directions.
    word ('U','L') abelianizes to M^2 (the figure-eight); ('U','S') to M (the single-twist tower)."""
    J = np.array(_B103.lawton_jacobian(list(word))).astype(float)
    ev = np.linalg.eigvals(J)
    mags = sorted(round(float(abs(e)), 4) for e in ev)
    center = [e for e in ev if abs(abs(e) - 1) < 1e-9]
    N = np.array(_B103.word_abelianization(list(word))).astype(int).tolist()
    return {"word": list(word), "abelianization": N, "n_coords": len(ev),
            "eig_magnitudes": mags, "n_center": len(center),
            "center_eigenvalues": sorted(round(float(e.real), 3) for e in center)}


def center_manifold_summary():
    """The void's center-manifold dimension = the tower's root-of-unity (parity) sector: 1 (SL2), 2 (SL3)."""
    return {"SL2": sl2_void_linearization()["n_center"],
            "SL3_figure_eight": sl3_void_center_count(("U", "L"))["n_center"],
            "SL3_single_twist": sl3_void_center_count(("U", "S"))["n_center"]}


def main():
    print("=" * 78)
    print("B109 -- the trace-map DYNAMICS at the void (D2). NO physics.")
    print("=" * 78)
    lin = sl2_void_linearization()
    print("\n[SL(2)] DT1^2 at the void (2,2,2):")
    print(f"    eigenvalues       : {lin['eigenvalues_symbolic']}")
    print(f"    center/unst/stable: {lin['n_center']}/{lin['n_unstable']}/{lin['n_stable']}")
    print(f"    center eigenvector: {lin['center_eigvec']}  (= A<->B asymmetry: {lin['center_is_asymmetry']})")
    print(f"    Lyapunov log|lam| : {lin['lyapunov']}   (4 log phi = {lin['four_log_phi']})")
    print("\n[SL(2)] center-eigenvector orbit (local boundedness):")
    for eps, mx in sl2_center_orbit().items():
        print(f"    eps={eps:<6}: max|v| over 2000 = {mx:.4f}")
    print("\n[kappa] the void as a critical point of tr[A,B]:")
    kc = kappa_void_critical_point()
    print(f"    kappa(void)={kc['kappa_at_void']}  grad={kc['grad']} (critical={kc['is_critical']})")
    print(f"    Hessian eigenvalues={kc['hessian_eigenvalues']}  signature={kc['signature']} -> {kc['type']}")
    print("\n[SL(3)] center directions = the tower's root-of-unity (parity) sector:")
    for w in (("U", "L"), ("U", "S")):
        r = sl3_void_center_count(w)
        print(f"    word {r['word']} (abel {r['abelianization']}): {r['n_center']}/8 center; "
              f"mags {r['eig_magnitudes']}")
    print(f"\n  center-manifold dim: SL(2)={center_manifold_summary()['SL2']}, "
          f"SL(3)={center_manifold_summary()['SL3_figure_eight']}  (= the tower parity sector)")


if __name__ == "__main__":
    main()
