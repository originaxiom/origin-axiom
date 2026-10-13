#!/usr/bin/env python3
"""B1642, post-seal (labelled): why R4 failed. Y_pq = Res F_p^T eps F_q is ANTISYMMETRIC (the quaternion units anticommute:
C_q^-1 C_p = -C_p^-1 C_q), so Y = [v]_x for the vector v of its entries, its singular values are (|v|, |v|, 0) and its null
vector is v itself.  Checked at 3 random tau with the sealed instrument's own functions (copied, unchanged)."""
import json, pathlib
import mpmath as mp
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
src = open(HERE / "residue_coupling.py").read()
head = src.split("rng = np.random.default_rng(1642)")[0]          # the instrument's definitions, before any cell runs
ns = {"__file__": str(HERE / "residue_coupling.py")}; exec(compile(head, "residue_coupling_defs", "exec"), ns)
th, residue, BLOCKS, EPS = ns["th"], ns["residue"], ns["BLOCKS"], ns["EPS"]
rng = np.random.default_rng(16420)
out = []
for _ in range(3):
    t = mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(0.7, 1.8))
    Y = np.zeros((3, 3), dtype=complex)
    for a, (_, Ca) in enumerate(BLOCKS):
        for b, (_, Cb) in enumerate(BLOCKS):
            Y[a, b] = complex(residue(Ca.T * EPS * Cb, t))
    v = np.array([Y[2, 1], Y[0, 2], Y[1, 0]])                      # Y = [v]_x, so Y v = 0
    s_ = np.linalg.svd(Y, compute_uv=False)
    eta3 = complex(2 * mp.pi * (mp.exp(1j * mp.pi * t / 12) * mp.fprod(1 - mp.exp(2j * mp.pi * t * n) for n in range(1, 200))) ** 3)
    out.append({"antisym_rel": float(np.abs(Y + Y.T).max() / np.abs(Y).max()),
                "sv_over_norm_v": [round(float(x / np.linalg.norm(v)), 12) for x in s_],
                "Y_v_rel": float(np.linalg.norm(Y @ v) / (np.linalg.norm(Y) * np.linalg.norm(v))),
                "moduli_of_v_times_2pi_eta3": sorted(round(float(abs(x * eta3)), 10) for x in v),
                "moduli_theta_sq": sorted(round(float(abs(th(n, 0, t)) ** 2), 10) for n in (2, 3, 4))})
json.dump(out, open(HERE / "post_seal_residue.json", "w"), indent=1)
print(json.dumps(out, indent=1))
