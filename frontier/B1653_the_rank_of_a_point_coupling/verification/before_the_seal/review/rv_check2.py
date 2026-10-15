"""Reviewer check 2: the lines (both conventions), U4 thresholds, U5's double-precision floor, the rotation-invariance
test of the line convention, and the contour residue at large twists."""
import sys, itertools
sys.path.insert(0, ".")
import numpy as np
from rv_core import *

om = mp.exp(2 * J * mp.pi / 3); tg = mp.mpc("0.13", "1.07")
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
third = mp.mpf(1) / 3; ninth = mp.mpf(1) / 9; half = mp.mpf(1) / 2


def lp_instr(p, q, t): return p * t + q          # the instrument's line_point
def lp_phase(p, q, t): return p * t - q          # holonomy phases (p along 1, q along tau) -> Jacobian point


def sector_ub_de(wl, sec):
    f1, f2 = SECT[sec]
    w1, w2 = SIXY[f1] * wl, SIXY[f2] * wl
    return w1 + w2, w1 - w2


def rel_sector(wl, sec, t):
    ub, de = sector_ub_de(wl, sec)
    return rel_rr(closed_R(ub, de, t))


# --- is the minimum set rotation-invariant in each convention?  W59: 3w at (1/3,1/3), (2/3,2/3), the fixed points
def in_lattice(z, t, tol=mp.mpf(10) ** -30):
    b = mp.im(z) / mp.im(t); a = mp.re(z) - b * mp.re(t)
    return abs(a - mp.nint(a)) < tol and abs(b - mp.nint(b)) < tol

print("== is 3w (W59's Higgs minimum) a fixed point of z -> omega z, mod the lattice? ==")
for name, lp in (("instrument p tau + q", lp_instr), ("phases p tau - q", lp_phase)):
    for (p, q) in [(third, third), (2 * third, 2 * third)]:
        z = lp(p, q, om)
        print(f"  {name:22s} (p,q)=({float(p):.3f},{float(q):.3f}): omega z - z in lattice: {in_lattice(om * z - z, om)}")

higgs = []
for base in [(ninth, ninth), (2 * ninth, 2 * ninth)]:
    for i in range(3):
        for j in range(3):
            higgs.append((base[0] + i * third, base[1] + j * third))

print("\n== U4(d) at omega, W59's 18 Higgs lines, both conventions: min/max |R.R|/|R|^2 ==")
for name, lp in (("instrument p tau + q", lp_instr), ("phases p tau - q", lp_phase)):
    q_vals = []; l_vals = []
    for (p, q) in higgs:
        wl = lp(p, q, om)
        q_vals += [rel_sector(wl, "up", om), rel_sector(wl, "down", om)]
        l_vals.append(rel_sector(wl, "lep", om))
    print(f"  {name:22s} quarks min {mp.nstr(min(q_vals),4)} max {mp.nstr(max(q_vals),4)} | leptons max {mp.nstr(max(l_vals),3)}")
    print(f"     at (1/9,1/9): up {mp.nstr(rel_sector(lp(ninth,ninth,om),'up',om),6)}, down {mp.nstr(rel_sector(lp(ninth,ninth,om),'down',om),6)}")

print("\n== U4(c) half-periods (both taus) and U4(b) 3-torsion at omega ==")
for t in (om, tg):
    vals = []
    for (p, q) in [(0, half), (half, 0), (half, half)]:
        wl = lp_instr(p, q, t)
        vals += [rel_sector(wl, s, t) for s in SECT]
    print(f"  tau={mp.nstr(t,4)}: half-period min {mp.nstr(min(vals),4)}")
v3 = []
for (i, j) in [(i, j) for i in range(3) for j in range(3) if (i, j) != (0, 0)]:
    wl = lp_instr(i * third, j * third, om)
    v3 += [rel_sector(wl, s, om) for s in SECT]
print("  3-torsion at omega: max", mp.nstr(max(v3), 3))

print("\n== a contour residue at a large-twist line (e^c at a Higgs line), against the closed form ==")
def twist_of(w, t): return (mp.im(w) / mp.im(t), 2 * (mp.re(w) - mp.re(t) * mp.im(w) / mp.im(t)))
def residues(x, y, t, rad=mp.mpf("0.02"), N=96):
    acc = {s: 0 for s in "1ijk"}
    for m in range(N):
        z = rad * mp.exp(2 * J * mp.pi * m / N); P = pairings(x, y, z, t)
        for s in acc: acc[s] += P[s] * z
    return {s: acc[s] / N for s in acc}
wl = lp_instr(2 * ninth + 2 * third, 2 * ninth + 2 * third, om)   # the largest twists
for sec in ("lep", "down"):
    f1, f2 = SECT[sec]
    x, y = twist_of(SIXY[f1] * wl, om), twist_of(SIXY[f2] * wl, om)
    R = residues(x, y, om); ub, de = sector_ub_de(wl, sec); Rc = closed_R(ub, de, om)
    lam = R["k"] / Rc["k"]
    err = max(abs(R[s] - lam * Rc[s]) for s in "ijk") / max(abs(R[s]) for s in "ijk")
    print(f"  {sec}: twists x={[mp.nstr(v,5) for v in x]} y={[mp.nstr(v,5) for v in y]}; contour vs closed-form direction {mp.nstr(err,3)};"
          f" rel_rr contour {mp.nstr(rel_rr(R),4)}")

print("\n== U5: the instrument's procedure (numpy SVD, complex128) on null cases ==")
rng = np.random.default_rng(1653)
for _ in range(5):
    for __ in range(2):
        rng.uniform(-0.5, 0.5); rng.uniform(-1, 1)
dirs = [rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(20)]

def takagi_min_ratio(R, a):
    Rv = np.array([complex(R[s]) for s in "ijk"]); av = np.array(a, dtype=complex)
    Y = np.outer(av, Rv) + np.outer(Rv, av) - (av @ Rv) * np.eye(3)
    sv = np.linalg.svd(Y, compute_uv=False)
    return float(sv[-1] / sv[0])

cases = [(0, "down", True), (lp_instr(third, 0, om), "down", True)]
cases += [(lp_instr(0, half, om), s, False) for s in SECT]
cases += [(lp_instr(ninth, ninth, om), "lep", True), (lp_instr(ninth, ninth, om), "down", False)]
nulls = []; lifts = []
for (wl, sec, null) in cases:
    ub, de = sector_ub_de(wl, sec); R = closed_R(ub, de, om)
    r = [takagi_min_ratio(R, a) for a in dirs]
    (nulls if null else lifts).extend(r)
    print(f"  {sec:5s} null={null}: min/max of sigma_min/sigma_max over 20 a: {min(r):.3e} / {max(r):.3e}")
print(f"  U5 as coded: null max {max(nulls):.3e} (< 1e-20 required) ; lifted min {min(lifts):.3e} (> 1e-8 required)")

# the same in mpmath at 40 digits
def takagi_min_ratio_mp(R, a):
    Rv = mp.matrix([R[s] for s in "ijk"]); av = mp.matrix([mp.mpc(complex(c).real, complex(c).imag) for c in a])
    Y = av * Rv.T + Rv * av.T - (av.T * Rv)[0] * mp.eye(3)
    S = mp.svd_c(Y, compute_uv=False)
    return max(S) and min(S) / max(S)
print("  mpmath svd_c on the first null case, first 3 a:", [mp.nstr(takagi_min_ratio_mp(closed_R(*sector_ub_de(0, 'down'), om), a), 3) for a in dirs[:3]])
