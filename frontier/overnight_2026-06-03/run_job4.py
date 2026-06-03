"""Overnight Job 4 -- SL(7) partial fixed-line spectrum (dim 48).

B66 inverse-word pipeline at n=7, m=1, dps=50 (expect severe gauge degeneracy).
For |k|=1,2,3 count eigenvalues near BOTH the big and small roots of char(+-M^k);
a count is trustworthy only if big- and small-root counts agree (else INCONCLUSIVE).
Tests open patterns (a_1=n-3=4? mult(3)=2? a_2=?). DO NOT extrapolate a formula.
Writes sl7_partial.json only. No commit.
"""

import importlib.util
import json
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / "sl7_partial.json"
N = 7
DIM = 48


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def jacobian(b66, words, seed, dps=50, deg=7):
    """dt0 = lim DX.pinv(Dx) at the SL(7) fixed line (returns the 48x48 numpy matrix)."""
    mp.mp.dps = dps
    epss = [mp.mpf(e) for e in ("0.006", "0.009", "0.012", "0.015", "0.018", "0.021", "0.024", "0.027")]
    h = mp.mpf(10) ** (-(dps // 3))
    basis = b66._basis_mp(N)
    pp = [b66.PR.expm_mp(h * g) for g in basis]
    pm = [b66.PR.expm_mp(-h * g) for g in basis]
    Pm, Qm = b66._random_PQ(N, seed)
    dts = []
    for eps in epss:
        A, B = b66.PR.expm_mp(eps * Pm), b66.PR.expm_mp(eps * Qm)
        dx = b66._diff_matrix(words, A, B, False, pp, pm, h, DIM)
        dX = b66._diff_matrix(words, A, B, True, pp, pm, h, DIM)
        dts.append(dX * b66.PR.svd_pinv(dx))
    dt0 = mp.zeros(DIM, DIM)
    for i in range(DIM):
        for j in range(DIM):
            dt0[i, j] = mp.re(b66.PR._extrap0(epss, [d[i, j] for d in dts], deg))
    return np.array([[complex(dt0[i, j]) for j in range(DIM)] for i in range(DIM)])


def roots_pm(k):
    """big/small roots of char(M^k) and char(-M^k) at m=1."""
    L = {1: 1.0, 2: 3.0, 3: 4.0}[k]
    c = (-1) ** (k % 2)
    d = (L * L - 4 * c) ** 0.5
    r1, r2 = (L + d) / 2, (L - d) / 2
    big_p, small_p = (r1, r2) if abs(r1) >= abs(r2) else (r2, r1)   # char(M^k)
    return {"char(M^%d)" % k: {"big": big_p, "small": small_p},
            "char(-M^%d)" % k: {"big": -big_p, "small": -small_p}}


def near_count(vals, root, tol=0.05):
    return int(np.sum([abs(v.real - root) < tol and abs(v.imag) < tol for v in vals]))


def main():
    b66 = load("b66_validate", "frontier/B66_sl6_tower/validate.py")
    out = {"job": "sl7_partial", "started": time.strftime("%F %T"), "status": "running",
           "n": N, "dim": DIM, "dps": 50}
    OUT.write_text(json.dumps(out, indent=2, default=str))

    words = b66.select_words(N, 5, seed=20)
    out["num_words"] = len(words)
    OUT.write_text(json.dumps(out, indent=2, default=str))

    dt0 = jacobian(b66, words, seed=20)
    vals, V = np.linalg.eig(dt0)
    Vi = np.linalg.inv(V)
    kappa = np.array([float(np.linalg.norm(V[:, i]) * np.linalg.norm(Vi[i, :])) for i in range(DIM)])

    # resolved fraction: eigenvalues within 0.03 of ANY catalog root (k=-7..7) and real
    cat = []
    for k in range(-7, 8):
        if k == 0:
            continue
        Lk = float(np.real(np.trace(np.linalg.matrix_power(np.array([[1, 1], [1, 0]], float), k) if k > 0
                                    else np.linalg.matrix_power(np.linalg.inv(np.array([[1, 1], [1, 0]], float)), -k))))
        c = (-1) ** (k % 2)
        dd = (Lk * Lk - 4 * c + 0j) ** 0.5
        for r in [(Lk + dd) / 2, (Lk - dd) / 2, (-Lk + dd) / 2, (-Lk - dd) / 2]:
            cat.append(complex(r))
    cat += [1.0, -1.0]
    cat = np.array(cat)
    resolved = int(np.sum([min(abs(v - cat)) < 0.03 and abs(v.imag) < 0.03 for v in vals]))

    out["resolved_fraction"] = f"{resolved}/{DIM}"
    out["likely_gauge_count"] = int(np.sum([abs(v.imag) > 0.03 for v in vals]))

    # per-|k| big/small counts (checkpoint each)
    profile = {}
    for k in (1, 2, 3):
        entry = {}
        for lab, rr in roots_pm(k).items():
            nb = near_count(vals, rr["big"])
            ns = near_count(vals, rr["small"])
            entry[lab] = {"big_root": round(rr["big"], 6), "small_root": round(rr["small"], 6),
                          "big_count": nb, "small_count": ns,
                          "trustworthy": bool(nb == ns), "mult": nb if nb == ns else None}
        kabs_mult = None
        if all(e["trustworthy"] for e in entry.values()):
            kabs_mult = sum(e["mult"] for e in entry.values())
        entry["|k|=%d_multiplicity" % k] = kabs_mult
        entry["INCONCLUSIVE"] = bool(kabs_mult is None)
        profile["|k|=%d" % k] = entry
        out["low_k_profile"] = profile
        OUT.write_text(json.dumps(out, indent=2, default=str))

    out["eig1_to_5_condition_numbers"] = {
        "min": round(float(kappa.min()), 3), "max": round(float(kappa.max()), 3),
        "median": round(float(np.median(kappa)), 3)}
    out["note"] = ("Severe gauge degeneracy expected at n=7; |k| multiplicities are trustworthy "
                   "only where big_count==small_count. Data to constrain, NOT a formula.")
    out["status"] = "ok"
    out["finished"] = time.strftime("%F %T")
    OUT.write_text(json.dumps(out, indent=2, default=str))
    print("JOB4 done:", out["resolved_fraction"], "profile:",
          {k: v.get("|k|=%s_multiplicity" % k[-1]) for k, v in profile.items()})


if __name__ == "__main__":
    main()
