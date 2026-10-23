#!/usr/bin/env python3
"""SM READING BRANCHES (data-free; committed before its run; it re-implements a read-only check the second referee pass
ran in its scratch area, so that the note can cite a committed source).  Under the Standard Model's reading (up sees
conj h, down and leptons h) on the stored grid, for DR, F_6 and F_22 in both orientations (classed by the leading null
line of h, n or n-bar): medians of |V_ud|, |V_us|, |V_cb|, |V_ub|, the up light state's overlap with n-bar, and up
m2/m3, by Im tau band.
    python3 -B sm_reading_branches.py      # writes sm_reading_branches.json"""
import json, math, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
st = np.load(HERE / "channel_store_two_higgs.npz"); U, H = st["U"], st["H"]
I = json.loads((HERE / "channel_store_two_higgs_index.json").read_text())
tasks, DIRS = I["tasks"], I["dirs"]
F1 = np.array([0, 1, -1j]) / math.sqrt(2); F3 = np.array([0, 1, 1j]) / math.sqrt(2)


def cross(h):
    return np.array([[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]])


def closed(u4, h):
    w, u = u4[0], u4[1:]
    return np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + w * cross(h)


res = {}
for p, (k, re_t, im_t) in enumerate(tasks):
    band = "2.0-2.5" if im_t < 2.5 else ("2.5-3.0" if im_t < 3.0 else "3.0-3.5")
    for ih in range(2):
        for d in ("dR", "F_6", "F_22"):
            for h in (H[p, DIRS.index(d)], np.conj(H[p, DIRS.index(d)])):
                lead = "n" if abs(np.vdot(F3, h)) >= abs(np.vdot(F1, h)) else "n-bar"
                Yu, Yd = closed(U[p, 0, ih], np.conj(h)), closed(U[p, 1, ih], h)
                Uu = np.linalg.svd(Yu)[0][:, ::-1]; Ud = np.linalg.svd(Yd)[0][:, ::-1]; V = np.abs(np.conj(Uu.T) @ Ud)
                su = np.linalg.svd(Yu, compute_uv=False)
                res.setdefault(f"{d}, h led by {lead}, Im tau {band}", []).append([V[0, 0], V[0, 1], V[1, 2], V[0, 2], abs(np.vdot(F1, Uu[:, 0])), su[1] / su[0]])
out = {"columns": ["|V_ud|", "|V_us|", "|V_cb|", "|V_ub|", "|<n-bar, up light state>|", "up m2/m3"],
       "medians": {k: np.median(np.array(v), axis=0).round(3).tolist() for k, v in sorted(res.items())}}
(HERE / "sm_reading_branches.json").write_text(json.dumps(out, indent=1) + "\n")
print("written")
