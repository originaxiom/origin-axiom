"""B666 cell W3-4 (L98) -- DESIGN CALIBRATION (pre-seal, declared).

Runs ONLY on control points strictly OUTSIDE the target plateau grid
[0.80, 1.55] (the N3 precedent: calibrate the new estimator on non-target
reference points, then seal).  No target grid point is touched.

Questions this calibration answers (each fixes one prereg choice):
  C1. Is the max-MST-edge partition MACROSCOPIC (n_small >= 5% L) at the
      controls, or an outlier cut?  -> fixes the primary-label rule.
  C2. Is the label x = n_small/L DEPTH-STABLE across depths 12..15?
      -> fixes the depth-agreement tolerance delta_tol.
  C3. How close is e2/e1 to 1 (degeneracy)?  -> fixes the degeneracy guard.
  C4. Is the label invariant under 1e-10 eigenvalue perturbation (5 seeds)?
      -> substantiates the zero-jitter claim.

Controls: kappa in {0.60, 1.90} (below/above the plateau; 1.90 is N3's own
reference point).  Depths 12, 13, 14, 15 (L = 377, 610, 987, 1597).
"""
import time

import numpy as np

from l98_lib import provenance_gate, metallic_word, spectrum, gap_labels

provenance_gate()
print("provenance gate: metallic_word/spectrum verbatim vs packet lib_banked.py  PASS")

CONTROLS = (0.60, 1.90)
DEPTHS = (12, 13, 14, 15)

print("\n== C1/C2/C3: labels at the controls, depths 12..15 ==")
print(f"{'kappa':>6} {'depth':>5} {'L':>5} {'e1':>10} {'x=ns/L':>9} {'ns':>5} "
      f"{'e2/e1':>7}  top-5 (ns/L)")
store = {}
for kap in CONTROLS:
    mu = np.sqrt(2.0 - kap)
    for d in DEPTHS:
        t0 = time.time()
        w = metallic_word(d, 1)
        ev = spectrum(w, 1j * mu, periodic=True)
        rows, ratio = gap_labels(ev, top=5)
        e1, ns, x = rows[0]
        store[(kap, d)] = (rows, ratio, ev)
        tops = " ".join(f"{r[2]:.4f}" for r in rows)
        print(f"{kap:6.2f} {d:5d} {len(w):5d} {e1:10.5f} {x:9.5f} {ns:5d} "
              f"{ratio:7.4f}  [{tops}]  ({time.time()-t0:.1f}s)")

print("\n== C2 summary: per-kappa depth scatter of the primary label x ==")
for kap in CONTROLS:
    xs = [store[(kap, d)][0][0][2] for d in DEPTHS]
    print(f"  kappa={kap:.2f}: x by depth = {[f'{v:.5f}' for v in xs]}, "
          f"max pairwise |dx| = {max(xs)-min(xs):.5f}")

print("\n== C4: perturbation stability (eigenvalues + N(0,1e-10), 5 seeds) ==")
for kap in CONTROLS:
    for d in (13, 14):
        rows0, _, ev = store[(kap, d)]
        ns0 = rows0[0][1]
        ok = True
        for seed in range(5):
            rng = np.random.default_rng(seed)
            pert = ev + (rng.normal(size=len(ev)) +
                         1j * rng.normal(size=len(ev))) * 1e-10
            rows, _ = gap_labels(pert, top=1)
            if rows[0][1] != ns0:
                ok = False
        print(f"  kappa={kap:.2f} depth={d}: n_small invariant under 5 seeded "
              f"1e-10 perturbations: {ok}")

print("\ncalibration done")
