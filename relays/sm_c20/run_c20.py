#!/usr/bin/env python3
"""SM-C20: is the tick, acting on frame D1's six Higgs modes as Sigma = T6 S6 K, an antiunitary square root of U_M that
exchanges the +-pi/6 ground modes?  Card relays/cards/SM_C20_is-the-exchange-the-tick.md, pushed before this run.
Main's level6_higgs.py imported unchanged; data-free.
    python3 run_c20.py MAIN_CHECKOUT"""
import importlib.util
import json
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
CHK = pathlib.Path(sys.argv[1]).resolve() / "frontier/B1957_the_seats_claims_register/verification/checks"
sys.path.insert(0, str(CHK))
spec = importlib.util.spec_from_file_location("l6", CHK / "level6_higgs.py")
L6 = importlib.util.module_from_spec(spec); spec.loader.exec_module(L6)
UM, T6, S6 = L6.UM, L6.T6, L6.S6
inv = np.linalg.inv


def upto(A, B):
    i = np.unravel_index(np.argmax(abs(B)), B.shape); ph = A[i] / B[i]
    return float(np.abs(A - ph * B).max()), complex(ph)


ev, V = np.linalg.eig(UM); ph = np.angle(ev) / np.pi
vp = V[:, np.argmin(abs(ph - 1 / 6))]; vm = V[:, np.argmin(abs(ph + 1 / 6))]
vp, vm = vp / np.linalg.norm(vp), vm / np.linalg.norm(vm)
out = {}
out["C0 conj(T6) - T6^-1"] = float(np.abs(T6.conj() - inv(T6)).max())
out["C0 conj(S6) - S6^-1"] = float(np.abs(S6.conj() - inv(S6)).max())
A = T6 @ S6                                   # Sigma = A K
Sig2 = A @ A.conj()                           # (A K)(A K) = A conj(A)
r, phs = upto(Sig2, UM)
out["E1 Sigma^2 against U_M (residual, phase)"] = [r, [phs.real, phs.imag]]
out["E1 also against T6 S6 T6^-1 S6^-1"] = upto(Sig2, T6 @ S6 @ inv(T6) @ inv(S6))[0]
sp, sm = A @ vp.conj(), A @ vm.conj()
out["E2 |<v-|Sigma v+>|"] = float(abs(np.vdot(vm, sp)))
out["E2 |<v+|Sigma v->|"] = float(abs(np.vdot(vp, sm)))
# E3: sigma = T J with J = S R0, the same Sigma
out["E3 T (S K) equals (T S) K"] = float(np.abs(T6 @ S6 - (T6 @ S6)).max())
(HERE / "c20_results.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
