#!/usr/bin/env python3
"""B1615 -- POST-SEAL (disclosed): the sealed C4 sampled the one family it found (the second triplet of T-bar (x) T with
its vacuum along RRL's two-dimensional fixed space) at 25 random points.  Its range decides C4's second clause (does any
residual-aligned vacuum reach the charged leptons' ratios m_e/m_tau ~ 2.9e-4, m_mu/m_tau ~ 0.059?).  Scanned here densely
over the projective fixed space v = Qf (cos t, e^{i p} sin t), t in [0, pi/2], p in [0, 2 pi): the range of m1/m3 and
m2/m3, and the family's closest approach to the charged leptons' point.  Writes post_seal_family_scan.json."""
import json, pathlib, importlib.util
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cw", HERE / "couplings_on_the_weave.py"); cw = importlib.util.module_from_spec(spec); spec.loader.exec_module(cw)
mats = [np.kron(A.conj(), A) for A in cw.T]
pieces, _ = cw.cp.decompose(mats, 9)
out = {}
for n, P in enumerate(pieces):
    Q, _ = np.linalg.qr(P); d = Q.shape[1]
    if d != 3: continue
    Cs = [Q[:, k].reshape(3, 3) for k in range(d)]
    M = Q.conj().T @ np.kron(cw.element("RRL").conj(), cw.element("RRL")) @ Q
    ev, V = np.linalg.eig(M); fixed = V[:, [i for i, e in enumerate(ev) if abs(e - 1) < 1e-7]]
    if fixed.shape[1] != 2: continue
    Qf, _ = np.linalg.qr(fixed); pts = []
    for t in np.linspace(0, np.pi / 2, 721):
        for p in np.linspace(0, 2 * np.pi, 721, endpoint=False):
            v = Qf @ np.array([np.cos(t), np.exp(1j * p) * np.sin(t)])
            s = np.sort(np.linalg.svd(sum(v[k] * Cs[k] for k in range(d)), compute_uv=False))
            if s[2] > 1e-12: pts.append((s[0] / s[2], s[1] / s[2]))
    a = np.array(pts); target = np.array([2.9e-4, 0.059])
    dist = np.sqrt(((np.log10(np.maximum(a, 1e-12)) - np.log10(target)) ** 2).sum(axis=1))
    k = int(np.argmin(dist))
    out[f"piece {n}"] = {"points": len(pts), "m1_m3_range": [float(a[:, 0].min()), float(a[:, 0].max())],
                         "m2_m3_range": [float(a[:, 1].min()), float(a[:, 1].max())],
                         "closest_to_charged_leptons": {"ratios": [float(a[k, 0]), float(a[k, 1])], "log10_distance": float(dist[k])},
                         "sum_rule_m1_plus_m2_over_m3": [float((a[:, 0] + a[:, 1]).min()), float((a[:, 0] + a[:, 1]).max())]}
json.dump(out, open(HERE / "post_seal_family_scan.json", "w"), indent=1); print(json.dumps(out, indent=1))
