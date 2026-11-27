#!/usr/bin/env python3
"""SM-R290 POST HOC (written after the sealed run; disclosed on the page): why E's determinant-law check failed at
j = 15. Hypothesis: the j = 15 invariant coupling is antisymmetric in (Q, u^c), so det M = 0 identically and the
sealed relative residual divides noise by noise. Reuses run.py's functions unchanged; data-free.
  python3 -B posthoc_e.py <main checkout>"""
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.argv = [sys.argv[0], sys.argv[1], "run"]
import run as R  # noqa: E402

rho_H = R.higgs_rho(sys.argv[1])
G = R.closure({g: (R.RHO_T[g], rho_H[g], R.CHI[g]) for g in ("t", "s")})
rng = np.random.default_rng(290)
for j in (3, 15):
    P = sum(np.kron(np.kron(a, a), b * c ** j) for a, b, c in G) / len(G)
    Yt = (P.T @ (rng.normal(size=27) + 1j * rng.normal(size=27))).reshape(3, 3, 3)
    sym = np.abs(Yt - Yt.transpose(1, 0, 2)).max() / np.abs(Yt).max()
    asym = np.abs(Yt + Yt.transpose(1, 0, 2)).max() / np.abs(Yt).max()
    h = rng.normal(size=3) + 1j * rng.normal(size=3)
    M = np.einsum("ijk,k->ij", Yt, h)
    absres = max(abs(np.linalg.det(np.einsum("ijk,k->ij", Yt, c ** j * b @ h)) * np.linalg.det(a) ** 2
                     - np.linalg.det(M)) for a, b, c in G)
    print("j=%d: |Y - Y^T(Q,u)|/|Y| %.1e, |Y + Y^T(Q,u)|/|Y| %.1e, |det M| %.2e, |M| %.2e, worst absolute "
          "residual %.1e" % (j, sym, asym, abs(np.linalg.det(M)), np.abs(M).max(), absres))
