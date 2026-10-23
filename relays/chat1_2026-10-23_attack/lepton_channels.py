#!/usr/bin/env python3
"""LEPTON CHANNELS (data-free; committed before its run).  On the stored grid (the ten (2/5, k/10) lines):
  L1  the leptons' four channel weights against the down quarks', up to one complex factor, for every sign pattern on
      (u_1, u_i, u_j, u_k): the best pattern on order-5 and on order-10 lines and its largest relative deviation;
  L2  the consequence for the masses, checked directly for the record's Higgs directions (DR, F_6, F_22, F_-2, each as
      stored and conjugated): on order-5 lines the lepton singular values equal the down quarks'; on order-10 lines they
      equal the down quarks' with h -> P h, P = diag(-1, 1, 1) (the Higgs's e1 part reversed).  Largest relative
      differences of the singular-value ratios.
    python3 -B lepton_channels.py      # writes lepton_channels.json"""
import json, math, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
st = np.load(HERE / "channel_store_two_higgs.npz"); U, H = st["U"], st["H"]
I = json.loads((HERE / "channel_store_two_higgs_index.json").read_text())
DIRS = I["dirs"]


def cross(h):
    return np.array([[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]])


def closed(u4, h):
    w, u = u4[0], u4[1:]
    return np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + w * cross(h)


signs = [np.array([a, b, c, d]) for a in (1, -1) for b in (1, -1) for c in (1, -1) for d in (1, -1)]
L1 = {"order 5": {}, "order 10": {}}
L2 = {"order 5: lep vs down": 0.0, "order 10: lep vs down with h -> P h": 0.0, "order 10: lep vs down (no reversal), smallest relative difference seen": 1e9}
P = np.diag([-1.0, 1.0, 1.0]).astype(complex)
for p, (k, re_t, im_t) in enumerate(I["tasks"]):
    o = "order 5" if k % 2 == 0 else "order 10"
    for ih in range(2):
        dn, lp = U[p, 1, ih], U[p, 2, ih]
        for sg in signs:
            x = sg * dn; c = np.vdot(x, lp) / np.vdot(x, x)
            e = float(np.max(np.abs(lp - c * x)) / np.max(np.abs(lp)))
            key = str(sg.tolist()); L1[o][key] = max(L1[o].get(key, 0.0), e)
        for d in ("dR", "F_6", "F_22", "F_-2"):
            for h in (H[p, DIRS.index(d)], np.conj(H[p, DIRS.index(d)])):
                se = np.linalg.svd(closed(lp, h), compute_uv=False); se = se[1:] / se[0]
                sd = np.linalg.svd(closed(dn, h), compute_uv=False); sd = sd[1:] / sd[0]
                if o == "order 5":
                    L2["order 5: lep vs down"] = max(L2["order 5: lep vs down"], float(np.max(np.abs(se / sd - 1))))
                else:
                    sp = np.linalg.svd(closed(dn, P @ h), compute_uv=False); sp = sp[1:] / sp[0]
                    L2["order 10: lep vs down with h -> P h"] = max(L2["order 10: lep vs down with h -> P h"], float(np.max(np.abs(se / sp - 1))))
                    L2["order 10: lep vs down (no reversal), smallest relative difference seen"] = min(L2["order 10: lep vs down (no reversal), smallest relative difference seen"], float(np.max(np.abs(se / sd - 1))))
out = {"L1 best sign patterns (u_1, u_i, u_j, u_k) up to one complex factor, largest relative deviation": {o: sorted(v.items(), key=lambda kv: kv[1])[:2] for o, v in L1.items()},
       "L2 singular-value ratios, largest relative difference": L2}
(HERE / "lepton_channels.json").write_text(json.dumps(out, indent=1) + "\n")
print("written")
