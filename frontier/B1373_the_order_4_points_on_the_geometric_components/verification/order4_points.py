#!/usr/bin/env python3
"""B1373 -- THE ORDER-4 POINTS ON THE GEOMETRIC COMPONENTS: B1372 left door 2 open only at points of the character variety of a
free-cusp member where BOTH peripheral eigenvalues on the free cusp are fourth roots of unity (Theorem C), with non-unitary global
holonomy.  On the geometric component (the deformations of the hyperbolic structure) such a point is where one peripheral element has
eigenvalue +-i -- the (2,0) or (0,2) cone-manifold point, cone angle pi along that curve -- and the other must then have eigenvalue in
{+-1, +-i}, i.e. log-holonomy in i pi Z.  This script follows the geometric component by continuation from the complete structure to the
(2,0) and the (0,2) points on every free cusp of the 35 candidate members (the other cusps kept complete), and reads the other curve's
holonomy: if its real part is non-zero the eigenvalue is non-unitary and Theorem B already forbids simultaneous cusp-fixedness; if it is
unitary but not a fourth root of unity, Theorem C forbids it.  A point survives only if H(other) in i pi Z.
Usage: python3 order4_points.py  (seconds)"""
import os, sys, json, cmath, math, warnings
warnings.filterwarnings("ignore")
import snappy

HERE = os.path.dirname(os.path.abspath(__file__))
fam = json.load(open(os.path.join(HERE, "..", "..", "B1186_family_is_112", "verification", "family_census.json")))
sys.path.insert(0, os.path.join(HERE, "..", "..", "B1369_the_siblings_in_the_sm_frame", "verification"))
import sympy as sp

def abelianise(word, gens):
    v = [0] * len(gens)
    for ch in word:
        i = gens.index(ch.lower()); v[i] += 1 if ch.islower() else -1
    return v
def free_cusps(M):
    G = M.fundamental_group(); gens = list(G.generators()); rels = G.relators()
    R = sp.Matrix([abelianise(r, gens) for r in rels]) if rels else sp.zeros(0, len(gens))
    rR = R.rank() if rels else 0; b1 = len(gens) - rR
    out = []
    for c, (mu, lam) in enumerate(G.peripheral_curves()):
        P = sp.Matrix([abelianise(mu, gens), abelianise(lam, gens)])
        if (sp.Matrix.vstack(R, P) if rels else P).rank() - rR < b1: out.append(c)
    return b1, out

def continue_to(name, c, slope, path=(30, 15, 8, 6, 5, 4, 3, 2, 1)):
    """follow the geometric component from the complete structure to the cone-manifold point with p H(curve) = 2 pi i for p = 2
    (eigenvalue +-i on that curve), by a sequence of fillings (2p, 0) or (0, 2p) with p decreasing to 1 on the same manifold object;
    returns (holonomies, solution type, volume)"""
    M = snappy.Manifold(name)
    n = M.num_cusps()
    for p in path:
        fill = [(0, 0)] * n
        fill[c] = (p * slope[0], p * slope[1])
        M.dehn_fill(fill)
    ci = M.cusp_info()[c]
    H = [complex(h) for h in ci['holonomies']]
    return H, M.solution_type(), float(M.volume())

def classify(H, slope):
    """the curve filled has H = 2 pi i / 2 = i pi (eigenvalue +-i) if converged; the other curve's eigenvalue L = e^{H_other/2}"""
    filled = H[0] if slope == (2, 0) else H[1]
    other = H[1] if slope == (2, 0) else H[0]
    converged = abs(filled - 1j * math.pi) < 1e-6
    unit = abs(other.real) < 1e-7
    fourth = unit and abs(cmath.exp(2 * other) - 1) < 1e-6         # e^{2H} = L^4 = 1
    return converged, unit, fourth, other

print("=== the (2,0) and (0,2) points of the geometric component on every free cusp of the 35 candidates ===")
rows = []; fails = []; survivors = []
for name in fam['members_B']:
    M = snappy.Manifold(name)
    b1, fc = free_cusps(M)
    for c in fc:
        for slope, label in (((2, 0), "mu of order 4"), ((0, 2), "lambda of order 4")):
            try:
                H, st, v = continue_to(name, c, slope)
                conv, unit, fourth, other = classify(H, slope)
            except Exception as e:
                fails.append((name, c, label, str(e)[:60])); continue
            geometric = st.startswith("all tetrahedra positively") or st.startswith("contains negatively")
            ok = conv and not st.startswith("contains degenerate") and not st.startswith("unrecognized") and not st.startswith("no solution")
            if not ok:
                fails.append((name, c, label, f"continuation did not converge ({st}; H = {H[0]:.4f}, {H[1]:.4f})")); continue
            verdict = ("SURVIVES: the other eigenvalue is a fourth root of unity" if fourth else
                       ("closed by Theorem C: the other eigenvalue is unitary but not a fourth root of unity" if unit else
                        "closed by Theorem B: the other eigenvalue is non-unitary"))
            rows.append((name, c, label, st, v, other, verdict))
            if fourth: survivors.append((name, c, label, other))
            print(f"  {name:11s} cusp {c} {label:18s}: {st[:32]:32s} vol {v:9.6f}  H(other) = {other.real:+.6f} {other.imag:+.6f}i  |L| = {math.exp(other.real / 2):.4f}  -> {verdict}")
print(f"\n  points followed: {len(rows)}; closed by Theorem B (non-unitary other eigenvalue): {sum(1 for r in rows if 'Theorem B' in r[6])}; closed by Theorem C: {sum(1 for r in rows if 'Theorem C' in r[6])}; survivors: {len(survivors)} {survivors}")
print(f"  continuations that did not converge on the coarse path: {len(fails)}")
for f in fails: print(f"    {f}")

# ---------------------------------------------------------------- the failures: a fine real path on the original triangulation, deterministic
# (SnapPy's randomize() is seeded by the wall clock, so randomised triangulations are not reproducible and are not used here)
print("\n=== the failures on a fine path: cone angle pi / p with p from 3 to 1 in steps of 1/64 on the original triangulation ===")
DEGENERATE = ("contains degenerate", "unrecognized", "no solution")
def fine_path(name, c, slope, step=1.0 / 64, approach=(30, 15, 8, 6, 5, 4, 3)):
    """coarse approach to p = 3, then steps of 1/64 down to p = 1; returns the trace of (p, solution type, H, volume) and stops at the
    first degenerate step (the wall)"""
    M = snappy.Manifold(name); n = M.num_cusps(); trace = []
    def step_to(p):
        fill = [(0, 0)] * n; fill[c] = (p * slope[0], p * slope[1]); M.dehn_fill(fill)
        H = [complex(h) for h in M.cusp_info()[c]['holonomies']]
        trace.append((p, M.solution_type(), H, float(M.volume())))
    for p in approach[:-1]: step_to(p)
    k = 0
    while True:
        p = approach[-1] - k * step
        if p < 1.0 - 1e-9: break
        step_to(p)
        if trace[-1][1].startswith(DEGENERATE): break
        k += 1
    return trace
resolved = []; still = []
for (name, c, label, msg) in fails:
    slope = (2, 0) if label.startswith("mu") else (0, 2)
    tr = fine_path(name, c, slope)
    good = [t for t in tr if not t[1].startswith(DEGENERATE)]
    p_last, st_last, H_last, v_last = good[-1]
    other_of = lambda H: H[1] if slope == (2, 0) else H[0]
    filled_of = lambda H: H[0] if slope == (2, 0) else H[1]
    reached = abs(p_last - 1.0) < 1e-9 and abs(filled_of(H_last) - 1j * math.pi) < 1e-6
    tail = [abs(other_of(t[2]).real) for t in good[-8:]]
    monotone = all(tail[i] < tail[i + 1] for i in range(len(tail) - 1))
    if reached:
        other = other_of(H_last); unit = abs(other.real) < 1e-7; fourth = unit and abs(cmath.exp(2 * other) - 1) < 1e-6
        verdict = "SURVIVES" if fourth else ("Theorem C" if unit else "Theorem B")
        resolved.append((name, c, label, "converged", p_last, verdict))
        print(f"  {name:11s} cusp {c} {label:18s}: converged on the fine path, {st_last[:30]}, H(other) = {other.real:+.4f} {other.imag:+.4f}i -> {verdict}")
        continue
    wall = tr[-1]; p_wall = wall[0]
    # the wall lies within 1/16 of p = 1 (cone angle pi) or of p = 3/2 (cone angle 2 pi / 3) in every case; the bucket names the target
    angle = ("pi" if 1.0 - 1e-9 <= p_wall <= 1.0625 + 1e-9 else ("2pi/3" if 1.5 - 1e-9 <= p_wall <= 1.5625 + 1e-9 else f"pi/{p_wall:.4f}"))
    resolved.append((name, c, label, "degenerates", p_wall, angle, monotone, tail[-1]))
    print(f"  {name:11s} cusp {c} {label:18s}: degenerates near cone angle {angle:5s} (wall p = {p_wall:.4f}; last non-degenerate p = {p_last:.4f}, "
          f"|Re H(other)| = {tail[-1]:6.2f}, vol {v_last:.4f}); |Re H(other)| over the last 8 steps {'monotone increasing' if monotone else 'NOT monotone'} "
          f"{tail[0]:.2f} -> {tail[-1]:.2f}; at the wall step {abs(other_of(wall[2]).real):.1f}")
n_conv = sum(1 for r in resolved if r[3] == "converged"); n_surv = sum(1 for r in resolved if r[3] == "converged" and r[5] == "SURVIVES")
n_deg = sum(1 for r in resolved if r[3] == "degenerates")
n_pi = sum(1 for r in resolved if r[3] == "degenerates" and r[5] == "pi"); n_23 = sum(1 for r in resolved if r[3] == "degenerates" and r[5] == "2pi/3")
n_mono = sum(1 for r in resolved if r[3] == "degenerates" and r[6])
print(f"\n  failures resolved on the fine path: {len(resolved)} (converged: {n_conv}, survivors: {n_surv}; degenerate before or at cone angle pi: {n_deg} -- "
      f"wall within 1/16 of p = 1 (cone angle pi): {n_pi}, within 1/16 of p = 3/2 (cone angle 2pi/3): {n_23}, elsewhere: {n_deg - n_pi - n_23}); "
      f"|Re H(other)| monotone increasing on the approach: {n_mono} of {n_deg}")
if n_deg:
    lo = min(r[7] for r in resolved if r[3] == "degenerates"); hi = max(r[7] for r in resolved if r[3] == "degenerates")
    print(f"  |Re H(other)| at the last non-degenerate step: from {lo:.2f} to {hi:.2f}")
print("DONE")
