"""B431 -- the seam's spatial split on the boundary torus (Chat-1 GAP-2 claim: support
CONFIRMED exactly; two value-level claims CORRECTED).

The (1,2) pair seam s(a,b) (sqrt-15 components, 44 nonzero cells on Z/20 x Z/12), exact-FT'd
to the dual torus: S(x,y) = sum s(a,b) zeta60^{3ax+5by}. Exact Q(zeta60) arithmetic throughout.

CONFIRMED (support level -- the CRT gating law):
  * ACTIVE 120 / DARK 120 (exactly half the torus)
  * y = 0 mod 3: ALL dark   |   x = 0 mod 10: ALL dark
  * CRT cells (x mod 5, y mod 3): 10 cells; the two x=0-mod-5 cells carry 4/16 active,
    the eight others 14/16 (2 dark each beyond the gating lines)
  * parity (x,y) -> (-x,-y) preserves the active set; 0 fixed points (60 free orbits)

CORRECTED (value level):
  * parity partners are CONJUGATE, not equal: S(-x,-y) = conj S(x,y) and S is genuinely
    complex, so "the spatial seam is entirely parity-even" fails at the value level;
  * distinct exact values: 34 orbits, size distribution {2:24, 4:2, 8:8} (=120), not
    "18 orbits = 4x16 + 14x4".

Firewall: exact Fourier data of a theta-model invariant; "spatial" names the dual torus of the
projector indices, nothing more. No physics claim.
"""
import sys, os, json
from fractions import Fraction as Fr
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
from step0_exact_matrices import build_theta_W, matrix_order, pair_smatrix   # noqa: E402
import cyclo_engine as E                                                     # noqa: E402

def compute():
    W1 = build_theta_W(1); W2 = build_theta_W(2)
    _, p1 = matrix_order(W1); _, p2 = matrix_order(W2)
    sm = pair_smatrix(p1, p2)
    s = {(a, b): v[3] for (a, b), v in sm.items() if v[3] != 0}
    grid = {}
    for x in range(20):
        for y in range(12):
            t = E.ZERO
            for (a, b), val in s.items():
                t = E.add(t, E.scal(Fr(val), E.zeta((3*a*x + 5*b*y) % 60)))
            grid[(x, y)] = t
    active = {k for k, v in grid.items() if v != E.ZERO}
    crt = Counter(((x % 5, y % 3) for (x, y) in active))
    vals = {}
    for k in active:
        vals.setdefault(str(grid[k]), []).append(k)
    return dict(
        n_scells=len(s), active=len(active), dark=240 - len(active),
        y0mod3_dark=all((x, y) not in active for x in range(20) for y in range(12) if y % 3 == 0),
        x0mod10_dark=all((x, y) not in active for x in range(20) for y in range(12) if x % 10 == 0),
        crt_counts=sorted(crt.values()),
        parity_preserved=all(((-x) % 20, (-y) % 12) in active for (x, y) in active),
        parity_values_equal=all(grid[(x, y)] == grid[((-x) % 20, (-y) % 12)] for (x, y) in active),
        fixed_points=sum(1 for (x, y) in active if ((-x) % 20, (-y) % 12) == (x, y)),
        n_orbits=len(vals), orbit_sizes=dict(Counter(len(v) for v in vals.values())))

if __name__ == "__main__":
    r = compute()
    print(r)
    json.dump({k: (v if not isinstance(v, dict) else {str(a): b for a, b in v.items()})
               for k, v in r.items()}, open(os.path.join(HERE, "spatial_split.json"), "w"), indent=1)
    print("[written] spatial_split.json")
