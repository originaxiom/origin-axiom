"""Overnight Job 3 -- cross-m A-polynomial at m=2 (silver mean), bundle [[5,2],[2,1]].

phi_2: a->a^2 b, b->a; monodromy phi_2^2 abelianizes to [[5,2],[2,1]] = R^2 L^2,
the once-punctured-torus bundle = census m136 (vol 3.664). Trace map T_2^2.
Gather (a) trace-map (M,L) at T_2^2 fixed points (meridian = eig t solving the phi_2^2
monodromy, longitude = eig[B,A]); (b) m136's (M,L) deformation-variety sample via SnapPy
(verified working); attempt a candidate A-polynomial fit + framing search M->M*L^k and
verify it vanishes on the SnapPy sample. EXPLORATORY -- honest MATCH / INCONCLUSIVE flag.
Writes cross_m_silver.json only. No commit. (NO "new/unpublished" claim: m136 is well
studied.)
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
OUT = HERE / "cross_m_silver.json"


def T2(v):
    x, y, z = v
    return np.array([x * z - y, x, x * x * z - x * y - z])


def T2sq(v):
    return T2(T2(v))


def fixed_point(seed):
    rng = np.random.default_rng(seed)
    v = rng.standard_normal(3) + 1j * rng.standard_normal(3)
    for _ in range(100):
        F = T2sq(v) - v
        J = np.zeros((3, 3), dtype=complex)
        h = 1e-7
        for j in range(3):
            vp = v.copy(); vp[j] += h
            J[:, j] = ((T2sq(vp) - vp) - F) / h
        try:
            v = v - np.linalg.solve(J + 1e-12 * np.eye(3, dtype=complex), F)
        except np.linalg.LinAlgError:
            break
        if np.max(np.abs(T2sq(v) - v)) < 1e-13:
            break
    return v, float(np.max(np.abs(T2sq(v) - v)))


def ML_tracemap(v):
    """(M=eig t, L=eig[B,A], monodromy residual) at a T_2^2 fixed point v=(x,y,z)."""
    x, y, z = v
    b = (z + np.sqrt(z * z - 4 + 0j)) / 2
    A = np.array([[x, -1], [1, 0]], dtype=complex)
    B = np.array([[0, b], [-1 / b, y]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    pa = A @ A @ B @ A @ A @ B @ A          # phi_2^2(a) = a^2 b a^2 b a
    pb = A @ A @ B                          # phi_2^2(b) = a^2 b
    E = np.vstack([np.kron(A.T, I2) - np.kron(I2, pa),
                   np.kron(B.T, I2) - np.kron(I2, pb)])
    t = np.linalg.svd(E)[2][-1].conj().reshape(2, 2, order="F")
    t = t / np.sqrt(np.linalg.det(t))
    res = float(np.max(np.abs(t @ A @ np.linalg.inv(t) - pa))
                + np.max(np.abs(t @ B @ np.linalg.inv(t) - pb)))
    comm = B @ A @ np.linalg.inv(B) @ np.linalg.inv(A)
    return np.linalg.eigvals(t)[0], np.linalg.eigvals(comm)[0], res


def snappy_sample():
    import snappy.twister as tw
    to_np = lambda Mat: np.array([[complex(Mat[i, j]) for j in range(2)] for i in range(2)], dtype=complex)
    eigs = lambda Mat: sorted(np.linalg.eigvals(to_np(Mat)), key=lambda zz: abs(zz))
    base = tw.Surface("S_1_1").bundle("aaBB")     # R^2 L^2 = [[5,2],[2,1]]
    vol = float(base.volume()); ident = [str(x) for x in base.identify()]
    pts = []
    fills = [(p, 1) for p in range(5, 25)] + [(p, 2) for p in range(5, 15)]
    for fill in fills:
        try:
            Md = tw.Surface("S_1_1").bundle("aaBB"); Md.dehn_fill(fill)
            if "degenerate" in str(Md.solution_type()):
                continue
            G = Md.fundamental_group(); mw, lw = G.peripheral_curves()[0]
            Mv = complex(eigs(G.SL2C(mw))[1]); Lv = complex(eigs(G.SL2C(lw))[1])
            if np.isfinite(Mv) and np.isfinite(Lv):
                pts.append((Mv, Lv))
        except Exception:
            continue
        if len(pts) >= 16:
            break
    return vol, ident, pts


def fit_candidate(points, max_dM=8, max_dL=4):
    """Least-squares implicit fit: smallest-singular-vector over monomials M^i L^j on
    bounded points. Returns (coeffs dict, (dM,dL), fit_residual) or None."""
    pts = [(M, L) for (M, L) in points if abs(M) < 12 and abs(L) < 12]
    if len(pts) < 12:
        return None
    best = None
    for dL in range(1, max_dL + 1):
        for dM in range(2, max_dM + 1, 2):
            monos = [(i, j) for j in range(dL + 1) for i in range(dM + 1)]
            if len(pts) < len(monos) + 2:
                continue
            Amat = np.array([[ (M ** i) * (L ** j) for (i, j) in monos] for (M, L) in pts], dtype=complex)
            # scale columns for conditioning
            scale = np.maximum(np.abs(Amat).max(axis=0), 1e-30)
            U, S, Vh = np.linalg.svd(Amat / scale)
            coeffs = (Vh[-1].conj() / scale)
            resid = float(S[-1] / max(S[0], 1e-30))
            if resid < 1e-6 and (best is None or len(monos) < best[3]):
                best = (dict(zip(monos, coeffs)), (dM, dL), resid, len(monos))
        if best is not None:
            break
    if best is None:
        return None
    return {"coeffs": best[0], "bidegree": best[1], "rel_fit_residual": best[2]}


def evaluate(coeffs, M, L):
    return sum(c * (M ** i) * (L ** j) for (i, j), c in coeffs.items())


def main():
    out = {"job": "cross_m_silver", "started": time.strftime("%F %T"), "status": "running",
           "monodromy": "[[5,2],[2,1]] = R^2 L^2 = phi_2^2", "expected_manifold": "m136"}
    OUT.write_text(json.dumps(out, indent=2, default=str))

    # --- trace-map (M,L) cloud ---
    tm = []
    for s in range(60):
        v, fres = fixed_point(s)
        if fres < 1e-9:
            try:
                M, L, mres = ML_tracemap(v)
                if mres < 1e-6:
                    tm.append((complex(M), complex(L)))
            except Exception:
                pass
    out["tracemap_ML_sample"] = [[str(M), str(L)] for M, L in tm[:40]]
    out["tracemap_count"] = len(tm)
    OUT.write_text(json.dumps(out, indent=2, default=str))

    # --- SnapPy m136 (M,L) sample ---
    try:
        vol, ident, snp = snappy_sample()
        out["snappy"] = {"volume": vol, "identify": ident,
                         "ML_sample": [[str(M), str(L)] for M, L in snp], "count": len(snp)}
    except Exception as e:
        out["snappy"] = {"error": f"{type(e).__name__}: {e}"}
        snp = []
    OUT.write_text(json.dumps(out, indent=2, default=str))

    # --- candidate fit + framing search vs SnapPy ---
    cand = None
    try:
        cand = fit_candidate(tm)
    except Exception as e:
        out["candidate_fit_error"] = f"{type(e).__name__}: {e}"
    verdict = "INCONCLUSIVE"
    if cand and snp:
        out["candidate"] = {"bidegree": cand["bidegree"], "rel_fit_residual": cand["rel_fit_residual"],
                            "num_terms": len(cand["coeffs"])}
        best = None
        for k in range(-4, 5):
            try:
                res = max(abs(evaluate(cand["coeffs"], M * (L ** k), L)) /
                          (sum(abs(c) for c in cand["coeffs"].values()) * max(abs(M), abs(L), 1) ** sum(cand["bidegree"]))
                          for M, L in snp)
                if best is None or res < best[1]:
                    best = (k, float(res))
            except Exception:
                continue
        if best:
            out["framing_search"] = {"best_k": best[0], "max_rel_residual_on_snappy": best[1]}
            verdict = "MATCH" if best[1] < 1e-3 else "INCONCLUSIVE"
    elif cand:
        out["candidate"] = {"bidegree": cand["bidegree"], "rel_fit_residual": cand["rel_fit_residual"]}
    out["verdict"] = verdict
    out["note"] = ("m136 is a well-studied census manifold; this is a cross-check of the "
                   "trace-map construction at m=2, NOT a new/unpublished result. Point-by-point "
                   "matching is not expected (different parametrizations); the test is curve "
                   "coincidence via the fitted candidate + framing search. INCONCLUSIVE => "
                   "morning review (framing/orientation/fit-degree).")
    out["status"] = "ok"; out["finished"] = time.strftime("%F %T")
    OUT.write_text(json.dumps(out, indent=2, default=str))
    print("JOB3 verdict:", verdict, "| tracemap pts:", len(tm), "| snappy pts:", len(snp))


if __name__ == "__main__":
    main()
