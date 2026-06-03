"""Overnight Job 5 -- SL(3) figure-eight A-poly, full (GATED on Job 2 == GO).

The runner only invokes this if Job 2 returned GO; otherwise it writes the skip stub
itself. If invoked: build explicit SL(3,C) reps at the fixed points (principal Sym^2
lift), solve the SL(3) monodromy t in SL(3,C) (conjugation by phi_1^2), and record the
peripheral eigenvalues -- the SL(3) cusp has TWO meridian + TWO longitude parameters,
so the deliverable is a VARIETY (sample of (M1,M2,L1,L2) points), not a single 2-var
polynomial. NO automated GTZ match (conventions/component are a morning human step).
Writes sl3_apoly_full.json only. No commit.
"""

import importlib.util
import json
import sys
import time
import warnings
from pathlib import Path

import numpy as np

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / "sl3_apoly_full.json"


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def sym2(g):
    a, b, c, d = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    return np.array([[a * a, a * b, b * b],
                     [2 * a * c, a * d + b * c, 2 * b * d],
                     [c * c, c * d, d * d]], dtype=complex)


def solve_monodromy(A3, B3):
    """t in SL(3,C) with t A3 t^-1 = phi_1^2(a)=A3 B3 A3, t B3 t^-1 = phi_1^2(b)=A3 B3."""
    n = 3
    pa = A3 @ B3 @ A3
    pb = A3 @ B3
    I = np.eye(n, dtype=complex)
    E = np.vstack([np.kron(A3.T, I) - np.kron(I, pa),
                   np.kron(B3.T, I) - np.kron(I, pb)])
    t = np.linalg.svd(E)[2][-1].conj().reshape(n, n, order="F")
    det = np.linalg.det(t)
    t = t / (det ** (1.0 / 3.0))
    res = float(np.max(np.abs(t @ A3 @ np.linalg.inv(t) - pa))
                + np.max(np.abs(t @ B3 @ np.linalg.inv(t) - pb)))
    return t, res


def main():
    b67 = load("b67_probe", "frontier/B67_figure_eight_apolynomial/probe.py")
    out = {"job": "sl3_apoly_full", "started": time.strftime("%F %T"), "status": "running",
           "note": ("SL(3) cusp -> TWO meridian + TWO longitude eigenvalue parameters; "
                    "deliverable is a VARIETY sample. No automated GTZ match (morning human step).")}
    OUT.write_text(json.dumps(out, indent=2, default=str))

    samples = []
    for xv in (3.0, 4.0, 5.0, 2.5, 6.0, complex(3, 1), complex(4, -1)):
        try:
            A2, B2, _t, _r = b67.build_rep(xv)
            A3, B3 = sym2(A2), sym2(B2)
            t, res = solve_monodromy(A3, B3)
            if res > 1e-6:
                continue
            comm = A3 @ B3 @ np.linalg.inv(A3) @ np.linalg.inv(B3)
            mer = sorted(np.linalg.eigvals(t), key=lambda z: abs(z))
            lon = sorted(np.linalg.eigvals(comm), key=lambda z: abs(z))
            samples.append({"x": str(xv), "monodromy_residual": res,
                            "meridian_eigs": [str(z) for z in mer],
                            "longitude_eigs": [str(z) for z in lon]})
            out["variety_sample"] = samples
            OUT.write_text(json.dumps(out, indent=2, default=str))
        except Exception as e:
            samples.append({"x": str(xv), "error": f"{type(e).__name__}: {e}"})
    out["count"] = len([s for s in samples if "error" not in s])
    out["status"] = "ok"
    out["finished"] = time.strftime("%F %T")
    OUT.write_text(json.dumps(out, indent=2, default=str))
    print("JOB5 done: variety samples", out["count"])


if __name__ == "__main__":
    main()
