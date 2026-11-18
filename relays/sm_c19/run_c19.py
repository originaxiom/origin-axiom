#!/usr/bin/env python3
"""SM-C19: which operation exchanges frame D1's two Higgs ground modes (the +-pi/6 eigenvectors of U_M, B1957)?
Card relays/cards/SM_C19_which-bit-is-the-higgs-ground-bit.md, pushed before this run.  Main's level6_higgs.py imported
unchanged for U_M, T6, S6, the lift group and the transport; data-free.
    python3 run_c19.py MAIN_CHECKOUT"""
import importlib.util
import itertools
import json
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
CHK = MAIN / "frontier/B1957_the_seats_claims_register/verification/checks"
sys.path.insert(0, str(CHK))
spec = importlib.util.spec_from_file_location("l6", CHK / "level6_higgs.py")
L6 = importlib.util.module_from_spec(spec); spec.loader.exec_module(L6)
UM, T6, S6, Z3, X3 = L6.UM, L6.T6, L6.S6, L6.Z3, L6.X3
k = np.arange(6)
P = np.zeros((6, 6)); P[(-k) % 6, k] = 1                       # k -> -k
I6 = np.eye(6)


def eig_pm(U):
    ev, V = np.linalg.eig(U); ph = np.angle(ev) / np.pi
    vp = V[:, np.argmin(abs(ph - 1 / 6))]; vm = V[:, np.argmin(abs(ph + 1 / 6))]
    return ph, vp / np.linalg.norm(vp), vm / np.linalg.norm(vm)


def overlap(a, b):
    return float(abs(np.vdot(b, a)))


def main():
    out = {}
    ph, vp, vm = eig_pm(UM)
    out["U_M eigenphases / pi"] = sorted(np.round(ph, 6).tolist())
    # which is the modes' own transport (B1957's H3, rerun)
    tau = 0.23 + 1.37j
    W = L6.transport_g(6, (0.0, 0.0), tau, 0.0, (2, 1, 1, 1))
    out["H3 rerun: transport against U_M, conj U_M (up to a phase)"] = [float(L6.upto(W, UM)), float(L6.upto(W, UM.conj()))]
    # B1, B2: lift elements and parity
    ops = {"Z3": Z3, "X3": X3, "Z3X3": Z3 @ X3, "P": P}
    res = {}
    for name, A in ops.items():
        res[name] = {"||[A, U_M]||": float(np.abs(A @ UM - UM @ A).max()),
                     "|<v-|A v+>|": overlap(A @ vp, vm), "|<v+|A v+>|": overlap(A @ vp, vp)}
    out["B1/B2"] = res
    # B3: antiunitaries A conj(.) built from the record's operators: A conj(U_M) A^-1 = U_M ?
    gens = {"1": I6, "P": P, "Z3": Z3, "X3": X3, "T6": T6, "S6": S6, "T6^-1": T6.conj().T, "S6^-1": S6.conj().T}
    found = []
    names = list(gens)
    for r in (1, 2, 3):
        for combo in itertools.product(names, repeat=r):
            A = I6.astype(complex)
            for c in combo:
                A = A @ gens[c]
            # equality up to an overall phase of the operator
            lhs = A @ UM.conj() @ np.linalg.inv(A)
            idx = np.unravel_index(np.argmax(abs(UM)), UM.shape); phs = lhs[idx] / UM[idx]
            if abs(abs(phs) - 1) < 1e-9 and np.abs(lhs - phs * UM).max() < 1e-9:
                found.append({"A": "*".join(combo), "phase": [phs.real, phs.imag],
                              "|<v-|A conj(v+)>|": overlap(A @ vp.conj(), vm), "|<v+|A conj(v+)>|": overlap(A @ vp.conj(), vp)})
        if found:
            break
    out["B3 antiunitaries found (shortest words)"] = found[:8]
    out["B3 count"] = len(found)
    (HERE / "c19_results.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
