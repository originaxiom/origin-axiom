"""W79, POST HOC (labelled; written after W79's read-out). W79 found the two seats' triplets isomorphic (C1 failed as
worded: not conjugate), this seat's up sector unable to fit at main's tau where main's fits (C3 held), and main's
forms off the T-law this seat read from main's docstring by a relative error of exactly 2, an overall sign (C2 failed
as worded). This finds which law main's forms actually obey, and compares the two weight-3 spaces directly.

  PH1  the phase c in Y(tau + 1) = c rho^-T Y(tau) rho^-1 that main's forms obey, at weights 3, 5 and 7
       (c from {1, -1, i, -i}), and this seat's forms' phase under its own law, at tau = 0.1 + 3i
  PH2  the two weight-3 spaces compared: an intertwiner P with P rho_theta(g) = rho_T(g) P for g = S, T (this seat's
       rho_T is its W52 one); main's forms carried into this seat's frame as Y -> conj(P) Y conj(P)^T and also as
       Y -> P Y P^T; the principal angles between the carried span and this seat's span, at three tau

Main's code is used read-only, extracted from 60c5470ae as in W79.

Run: python3 the_two_seats_weight_three_posthoc.py  ->  the_two_seats_weight_three_posthoc.json beside it.
"""
import json
import sys
import tempfile
from pathlib import Path

import numpy as np
from scipy.linalg import null_space, subspace_angles

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_rank_thirteen_structures as RT  # noqa: E402
import the_two_seats_weight_three as W79  # noqa: E402

OUT = HERE / "the_two_seats_weight_three_posthoc.json"
TAU0 = complex(0.1, 3.0)
TAUS = [complex(0.1, 3.0), complex(-0.2, 1.7), complex(0.3, 6.6)]
PHASES = {"1": 1, "-1": -1, "i": 1j, "-i": -1j}


def best_phase(Y0s, Y1s, act):
    errs = {}
    for name, c in PHASES.items():
        errs[name] = max(float(np.linalg.norm(Y1 - c * act(Y0)) / np.linalg.norm(Y1)) for Y0, Y1 in zip(Y0s, Y1s))
    name = min(errs, key=errs.get)
    return {"phase": name, "error": errs[name], "all": errs}


def intertwiner(mS, mT, oS, oT):
    """P (3 x 3) with P m(g) = o(g) P for g = S, T: the null space of the stacked linear map"""
    I3 = np.eye(3)
    rows = []
    for m, o in ((mS, oS), (mT, oT)):
        rows.append(np.kron(I3, m.T) - np.kron(o, I3))            # vec(P m) - vec(o P), row-major vec
    N = null_space(np.vstack(rows))
    return N


def main_():
    out = {"status": "W79 POST HOC (labelled): which T-law main's forms obey, and the two weight-3 spaces compared"}
    oS, oT = W79.our_rho()
    with tempfile.TemporaryDirectory() as tmp:
        main, _ = W79.load_main(tmp)
        mS, mT = main.c35.rS, main.c35.rT
        Ri = np.linalg.inv(mT)
        ph1 = {}
        for k in (3, 5, 7):
            main.FORMS[k] = main.forms(k)
            ph1[f"main, weight {k}"] = best_phase(main.basis_at(k, TAU0), main.basis_at(k, TAU0 + 1),
                                                  lambda Y: Ri.T @ Y @ Ri)
            X = np.conj(oT)
            ph1[f"this seat, weight {k}"] = best_phase(RT.forms_at("T (x) T", k, TAU0),
                                                       RT.forms_at("T (x) T", k, TAU0 + 1), lambda Y: X @ Y @ X.T)
        out["PH1"] = ph1
        N = intertwiner(mS, mT, oS, oT)
        out["PH2"] = {"intertwiner dimension": int(N.shape[1])}
        if N.shape[1] >= 1:
            P = N[:, 0].reshape(3, 3)
            P = P / abs(np.linalg.det(P)) ** (1 / 3)
            unitary_err = float(np.linalg.norm(P @ P.conj().T / (P @ P.conj().T)[0, 0] - np.eye(3)))
            angles = {}
            for name, carry in (("conj(P) Y conj(P)^T", lambda Y: np.conj(P) @ Y @ np.conj(P).T),
                                ("P Y P^T", lambda Y: P @ Y @ P.T)):
                per_tau = []
                for t in TAUS:
                    A = np.array([carry(Y).reshape(9) for Y in main.basis_at(3, t)]).T
                    B = np.array([Y.reshape(9) for Y in RT.forms_at("T (x) T", 3, t)]).T
                    per_tau.append([float(a) for a in subspace_angles(A, B)])
                angles[name] = per_tau
            out["PH2"].update({"P unitary up to scale (error)": unitary_err,
                               "principal angles (radians) at the three tau": angles,
                               "tau": [[t.real, t.imag] for t in TAUS]})
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main_()
