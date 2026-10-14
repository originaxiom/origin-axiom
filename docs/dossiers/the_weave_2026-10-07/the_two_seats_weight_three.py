"""W79: are the two seats' weight-3 models the same representation, its conjugate, or neither? The rule (W79_RULE.md)
was committed before this script.

  C1  the triplets: this seat's rho_T (W52's PG.rho_T) against main's rho_theta (B1634, read from main's B1635 code):
      T-exponents and characters at S, T, ST, (ST)^2, T^2, S T^-1 and T S T, against main's and main's conjugate
  C2  the coupling action as each seat's weight-3 forms actually transform (checked at tau = 0.1 + 3i), and the two
      9-dimensional T-exponent multisets
  C3  this seat's model at main's three single-sector tau (B1637's F3), each sector alone at weight 3, 300 starts

Main's code is used read-only: every frontier/*/verification and frontier/*/received directory at 60c5470ae is
extracted by git archive into a temporary directory and imported from there.

Run: python3 the_two_seats_weight_three.py  ->  the_two_seats_weight_three.json beside it.
"""
import importlib.util
import io
import json
import os
import subprocess
import sys
import tarfile
import tempfile
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_fit_at_the_geometrys_weight as FW  # noqa: E402
import the_free_numbers_counted as FC  # noqa: E402
import the_rank_thirteen_structures as RT  # noqa: E402

OUT = HERE / "the_two_seats_weight_three.json"
REF = "60c5470ae"
MAIN_F3 = {"u": complex(-0.07371773130317516, 6.663964995864581),
           "d": complex(-0.19306001019703067, 5.086553557944307),
           "e": complex(0.1418602249723303, 5.854725153089794)}
TAU_CHECK = complex(0.1, 3.0)


def exps(M):
    return sorted(round(float(np.angle(z) / (2 * np.pi)) % 1.0, 6) % 1.0 for z in np.linalg.eigvals(M))


def our_rho():
    PG, GM, H = FC.PG, FC.GM, FC.H
    names, U = GM.units()
    named, _ = H.triplets()
    C = named["T"]
    _, _, xs, ell, lhat, _, _ = GM.M1(C, U)
    Ct = GM.t_basis(C, xs, ell, lhat)
    A, Tm = PG.rho_T(Ct)
    return np.array(A, dtype=complex), np.array(Tm, dtype=complex)


def load_main(tmp):
    specs = [":(glob)frontier/*/verification/**", ":(glob)frontier/*/received/**"]
    top = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=HERE, capture_output=True, check=True,
                         text=True).stdout.strip()
    raw = subprocess.run(["git", "archive", REF, "--"] + specs, cwd=top, capture_output=True, check=True).stdout
    with tarfile.open(fileobj=io.BytesIO(raw)) as tf:
        tf.extractall(tmp)
    front = Path(tmp) / "frontier"
    os.environ["OA_FRONTIER"] = str(front)
    path = front / "B1637_fits_on_the_ruled_branch" / "verification" / "fits_on_the_ruled_branch.py"
    spec = importlib.util.spec_from_file_location("b1637_main", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod, sum(1 for f in front.rglob("*") if f.is_file())


def words(S, T):
    Ti = np.linalg.inv(T)
    return {"S": S, "T": T, "ST": S @ T, "(ST)^2": S @ T @ S @ T, "T^2": T @ T, "S T^-1": S @ Ti, "T S T": T @ S @ T}


def c1(oS, oT, mS, mT):
    wo, wm = words(oS, oT), words(mS, mT)
    tr_o = {k: complex(np.trace(v)) for k, v in wo.items()}
    tr_m = {k: complex(np.trace(v)) for k, v in wm.items()}
    same = all(abs(tr_o[k] - tr_m[k]) < 1e-9 for k in tr_o)
    conj = all(abs(tr_o[k] - np.conj(tr_m[k])) < 1e-9 for k in tr_o)
    verdict = "isomorphic to rho_theta" if same else ("isomorphic to its conjugate" if conj else "neither")
    return {"this seat's T-exponents": exps(oT), "main's T-exponents": exps(mT),
            "this seat's S eigenvalues": [str(np.round(z, 9)) for z in np.linalg.eigvals(oS)],
            "main's S eigenvalues": [str(np.round(z, 9)) for z in np.linalg.eigvals(mS)],
            "characters (this seat, main)": {k: [str(np.round(tr_o[k], 9)), str(np.round(tr_m[k], 9))] for k in tr_o},
            "verdict": verdict,
            "holds": bool(verdict == "isomorphic to its conjugate" and exps(oT) == sorted([0.875, 0.125, 0.625]))}


def c2(oT, mT, main):
    X = np.conj(oT)
    ours = RT.forms_at("T (x) T", 3, TAU_CHECK)
    ours1 = RT.forms_at("T (x) T", 3, TAU_CHECK + 1)
    err_o = max(np.linalg.norm(Y1 - X @ Y0 @ X.T) / np.linalg.norm(Y1) for Y0, Y1 in zip(ours, ours1))
    main.FORMS[3] = main.forms(3)
    ms0, ms1 = main.basis_at(3, TAU_CHECK), main.basis_at(3, TAU_CHECK + 1)
    Ri = np.linalg.inv(mT)
    err_m = max(np.linalg.norm(Y1 - Ri.T @ Y0 @ Ri) / np.linalg.norm(Y1) for Y0, Y1 in zip(ms0, ms1))
    e_o = Counter(exps(np.kron(X, X)))
    e_m = Counter(exps(np.kron(Ri.T, Ri.T)))
    differ = e_o != e_m
    pattern = {e_o.get(0.25, 0), e_o.get(0.75, 0)} == {2, 3} and e_o.get(0.25) == e_m.get(0.75) \
        and e_o.get(0.75) == e_m.get(0.25)
    Xi = np.linalg.inv(X)
    inv_o = max(np.linalg.norm(Y1 - Xi @ Y0 @ Xi.T) / np.linalg.norm(Y1) for Y0, Y1 in zip(ours, ours1))
    inv_m = max(np.linalg.norm(Y1 - mT.T @ Y0 @ mT) / np.linalg.norm(Y1) for Y0, Y1 in zip(ms0, ms1))
    return {"this seat's forms: Y(tau+1) against X Y X^T": err_o,
            "main's forms: Y(tau+1) against rho^-T Y rho^-1": err_m,
            "read-out: the inverse actions (this seat, main)": [inv_o, inv_m],
            "dims at weight 3 (this seat, main)": [len(ours), len(ms0)],
            "this seat's 9 exponents": dict(sorted(e_o.items())), "main's 9 exponents": dict(sorted(e_m.items())),
            "holds": bool(err_o < 1e-8 and err_m < 1e-8 and differ and pattern)}


def alone(s, tau, seed):
    F = RT.forms_at("T (x) T", 3, tau)
    d = F.shape[0]
    def res(p):
        _, logs = RT.sector(RT.coupling(p, F))
        return RT.mass_res(s, logs, FW.A_MAIN)
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(300):
        r = least_squares(res, rng.normal(size=2 * d), method="trf", xtol=1e-14, ftol=1e-14, gtol=1e-14,
                          max_nfev=3000)
        c = float(np.sum(r.fun ** 2))
        if best is None or c < best[0]:
            best = (c, [float(v) for v in r.fun])
    return {"tau": [tau.real, tau.imag], "chi^2_min": best[0], "pulls": best[1]}


def main_():
    out = {"status": "W79: the two seats' weight-3 models compared (the rule W79_RULE.md first; one run)"}
    oS, oT = our_rho()
    with tempfile.TemporaryDirectory() as tmp:
        main, nfiles = load_main(tmp)
        out["main's code"] = {"ref": REF, "files extracted": nfiles}
        mS, mT = main.c35.rS, main.c35.rT
        out["C1"] = c1(oS, oT, mS, mT)
        out["C2"] = c2(oT, mT, main)
    c3 = {s: alone(s, t, 7900 + i) for i, (s, t) in enumerate(MAIN_F3.items())}
    out["C3"] = {**c3, "holds": bool(c3["d"]["chi^2_min"] < 1e-8 and c3["e"]["chi^2_min"] < 1e-8
                                      and c3["u"]["chi^2_min"] > 1)}
    out["cells"] = {k: out[k]["holds"] for k in ("C1", "C2", "C3")}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main_()
