"""Overnight Job 2 -- SL(3) figure-eight A-poly GO/NO-GO probe.

Principal Sym^2 lift of an SL(2) fixed-point rep to SL(3); linearize the induced
SL(3) trace map T_1^2 at that point; nullity = dim ker(DT - I) = local dim of the
fixed-point set. Computed at 2 base points x AND 2 auto word sets (4 runs). GO only
if nullity ~ 2 (= n-1) AND stable across runs AND well-conditioned; UNSTABLE if
high-but-unstable; NO-GO if 0/1. Exploratory; writes sl3_apoly_go_nogo.json. No commit.
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
OUT = HERE / "sl3_apoly_go_nogo.json"
N = 3
DIM = 8


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def sym2(g):
    """Principal Sym^2: SL(2) -> SL(3) (irreducible 3-dim rep), on basis (u^2,uv,v^2)."""
    a, b, c, d = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    return np.array([[a * a, a * b, b * b],
                     [2 * a * c, a * d + b * c, 2 * b * d],
                     [c * c, c * d, d * d]], dtype=complex)


def DT_at(b66, A3, B3, words, dps=40):
    """Trace-map T_1^2 Jacobian DT = dX . pinv(dx) on the 8-dim SL(3) character variety
    at (A3,B3). T_1^2 = phi_1^2: a->aba, b->ab, i.e. substituted (A,B) -> (ABA, AB)."""
    mp.mp.dps = dps
    to_mp = lambda Z: mp.matrix([[mp.mpc(complex(Z[i, j]).real, complex(Z[i, j]).imag)
                                  for j in range(N)] for i in range(N)])
    A, B = to_mp(A3), to_mp(B3)
    h = mp.mpf(10) ** (-(dps // 3))
    basis = b66._basis_mp(N)
    pp = [b66.PR.expm_mp(h * g) for g in basis]
    pm = [b66.PR.expm_mp(-h * g) for g in basis]
    tr = b66.PR._trace

    def diffmat(sub):
        M = mp.zeros(DIM, 2 * DIM)
        col = 0
        for Pp, Pm in zip(pp, pm):
            Ap, Am = Pp * A, Pm * A
            wp = b66._words_mp(words, Ap * B * Ap, Ap * B) if sub else b66._words_mp(words, Ap, B)
            wm = b66._words_mp(words, Am * B * Am, Am * B) if sub else b66._words_mp(words, Am, B)
            for r in range(DIM):
                M[r, col] = (tr(wp[r]) - tr(wm[r])) / (2 * h)
            col += 1
        for Pp, Pm in zip(pp, pm):
            Bp, Bm = Pp * B, Pm * B
            wp = b66._words_mp(words, A * Bp * A, A * Bp) if sub else b66._words_mp(words, A, Bp)
            wm = b66._words_mp(words, A * Bm * A, A * Bm) if sub else b66._words_mp(words, A, Bm)
            for r in range(DIM):
                M[r, col] = (tr(wp[r]) - tr(wm[r])) / (2 * h)
            col += 1
        return M

    DT = diffmat(True) * b66.PR.svd_pinv(diffmat(False))
    return np.array([[complex(DT[i, j]) for j in range(DIM)] for i in range(DIM)])


def main():
    b66 = load("b66_validate", "frontier/B66_sl6_tower/validate.py")
    b67 = load("b67_probe", "frontier/B67_figure_eight_apolynomial/probe.py")
    partial = {"job": "sl3_apoly_go_nogo", "started": time.strftime("%F %T"), "status": "running",
               "embedding": "principal Sym^2: SL(2)->SL(3)", "target": "nullity ~ n-1 = 2 => GO",
               "runs": []}
    OUT.write_text(json.dumps(partial, indent=2))

    runs = []
    for xval in (3.0, 4.0):
        A2, B2, _t, _res = b67.build_rep(xval)
        A3, B3 = sym2(A2), sym2(B2)
        for wseed in (20, 24):
            words = b66.select_words(N, 4, seed=wseed)
            DT = DT_at(b66, A3, B3, words)
            S = np.linalg.svd(DT - np.eye(DIM), compute_uv=False)
            svmax = float(S.max())
            nullity = int(np.sum(S < 1e-6 * max(1.0, svmax)))
            # eigenvalue-1 cluster condition numbers
            vals, V = np.linalg.eig(DT)
            Vi = np.linalg.inv(V)
            kappa = [float(np.linalg.norm(V[:, i]) * np.linalg.norm(Vi[i, :]))
                     for i in range(DIM) if abs(vals[i] - 1) < 1e-3]
            runs.append({"x": xval, "word_seed": wseed, "nullity": nullity,
                         "singular_values_of_DT_minus_I": [round(float(s), 8) for s in sorted(S)],
                         "eig1_count": int(np.sum(np.abs(vals - 1) < 1e-3)),
                         "eig1_condition_numbers": [round(k, 3) for k in kappa]})
            partial["runs"] = runs
            OUT.write_text(json.dumps(partial, indent=2))

    nulls = [r["nullity"] for r in runs]
    stable = len(set(nulls)) == 1
    well_cond = all(all(k < 1e3 for k in r["eig1_condition_numbers"]) for r in runs) and \
        all(len(r["eig1_condition_numbers"]) > 0 for r in runs)
    common = nulls[0] if stable else None
    if stable and common == N - 1 and well_cond:
        verdict = "GO"
    elif stable and common in (0, 1):
        verdict = "NO-GO"
    elif not stable:
        verdict = "UNSTABLE"
    else:
        verdict = "NO-GO"  # stable but != 2 (and not 0/1): not the expected geometric dim
    partial.update({"nullities": nulls, "stable": bool(stable), "well_conditioned": bool(well_cond),
                    "nullity_summary": common, "verdict": verdict,
                    "status": "ok", "finished": time.strftime("%F %T")})
    OUT.write_text(json.dumps(partial, indent=2))
    print("JOB2 verdict:", verdict, "nullities:", nulls)


if __name__ == "__main__":
    main()
