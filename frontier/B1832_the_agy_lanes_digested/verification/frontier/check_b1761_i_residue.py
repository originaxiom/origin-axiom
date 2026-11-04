"""agy:B1761 (data-free parts), on MAIN's b1656_funcs: where does the up sector's i-channel residue vanish identically in tau?

Claims checked:
 (a) R_i(X, Y) is proportional to theta_2(.)theta_2(.) of the sum and difference twists (agy writes theta_2((x+y)/2) theta_2((x-y)/2)
     in its own normalisation) -- tested here as |R_i| = C(tau) N(X+Y) N(X-Y), N(z) = |theta_2(z|tau)| exp(-pi (Im z)^2 / Im tau),
     at generic complex X, Y;
 (b) B1784's wording of the reusable fact: "the up sector's i-residue vanishes at every tau exactly when 5w == 1/2";
     agy's C1: R_i^up == 0, R_i^down != 0, R_j^up R_k^up != 0, a not in {0, 1/2}  <=>  5w == 1/2 (mod Z + Z tau), w != 1/2;
 (c) agy's count: exactly 10 of main's 662 census lines (B1726's 266 + B1755's 396) satisfy C1;
 (d) agy:B1761 Thm 2's numbers at tau = 0.3145 + 3.0345i (I(u_up) and ||R_jk||/|R_1| on the a = 1/5 and a = 2/5 orbits) and
     agy:B1759 Thm 2.2's c_s ranges on (2/5, 1/10) at B1757's four strip points.  (NUMERIC frame quantities; no data read.)
Exhaustive over every torsion point w = (j/N) tau + k/N, N <= 20, up to w -> -w, at three tau."""
import json, math, pathlib, sys, importlib.util
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _main_frame import B, SECT, ROOT

Bf = B()
OUT = {}
TAUS = [0.137 + 1.31j, -0.271 + 1.83j, 0.3145 + 3.0345j]


def Ri(sec, a, b, t):
    w = float(a) * t + float(b); ql, qr = SECT[sec]
    x, y = Bf.sector_twists(w, t, ql, qr); return Bf.residues(x, y, t)


def is_half(z_a, z_b):
    """z = z_a tau + z_b (rationals) == 1/2 mod Z + Z tau"""
    return (z_a % 1) == 0 and (z_b % 1) == Fr(1, 2)


# --- (a) factorisation of R_i ----------------------------------------------------------------------------------
def N2(z, t):
    q = mp.exp(1j * mp.pi * mp.mpc(t.real, t.imag))
    return float(abs(mp.jtheta(2, mp.pi * mp.mpc(z.real, z.imag), q)) * mp.exp(-mp.pi * (z.imag) ** 2 / t.imag))


rng = np.random.default_rng(7)
fac = []
for t in TAUS[:2]:
    rat = []
    for _ in range(10):
        X = complex(rng.uniform(-1, 1), rng.uniform(-1, 1)); Y = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
        R = Bf.residues(Bf.twist_of(X, t), Bf.twist_of(Y, t), t)
        rat.append(abs(R["i"]) / (N2(X + Y, t) * N2(X - Y, t)))
    fac.append({"tau": [t.real, t.imag], "ratio_min": min(rat), "ratio_max": max(rat), "rel_spread": (max(rat) - min(rat)) / max(rat)})
    print("(a) tau=%.3f%+.3fi: |R_i| / [N(X+Y) N(X-Y)] over 10 random complex (X, Y): %.12f .. %.12f (rel spread %.1e)"
          % (t.real, t.imag, min(rat), max(rat), (max(rat) - min(rat)) / max(rat)))
OUT["factorisation"] = fac

# --- (b) the zero set over all torsion points of order <= 20 ----------------------------------------------------
pts, seen = [], set()
for Nn in range(1, 21):
    for j in range(Nn):
        for k in range(Nn):
            a, b = Fr(j, Nn), Fr(k, Nn); key = min((a, b), ((-a) % 1, (-b) % 1))
            if key not in seen: seen.add(key); pts.append(key)
print("(b) %d torsion points (order <= 20, up to sign)" % len(pts))
zero_up, c1_set, mism = [], [], []
for a, b in pts:
    zu = all(abs(Ri("up", a, b, t)["i"]) < 1e-11 for t in TAUS[:2])
    pred5 = is_half(5 * a, 5 * b); pred3 = is_half(3 * a, 3 * b)
    if zu != (pred5 or pred3): mism.append((str(a), str(b), zu, pred5, pred3))
    if zu:
        zero_up.append((str(a), str(b), pred5, pred3))
        t = TAUS[0]; Ru = Ri("up", a, b, t); Rd = Ri("down", a, b, t)
        c1 = (a not in (0, Fr(1, 2))) and abs(Rd["i"]) > 1e-8 and abs(Ru["j"]) > 1e-8
        if c1: c1_set.append((str(a), str(b)))
only5 = [z for z in zero_up if z[2] and not z[3]]; only3 = [z for z in zero_up if z[3] and not z[2]]; both = [z for z in zero_up if z[2] and z[3]]
OUT["zero_set"] = {"n_points": len(pts), "n_zero_up": len(zero_up), "mismatch_vs_(5w==1/2 or 3w==1/2)": mism,
                   "zero_only_5w": [z[:2] for z in only5], "zero_only_3w": [z[:2] for z in only3], "zero_both": [z[:2] for z in both],
                   "C1_set": c1_set}
print("    R_i^up == 0 at both tau on %d points; mismatches against {5w == 1/2} u {3w == 1/2}: %d" % (len(zero_up), len(mism)))
print("    from 5w == 1/2 only: %d  %s" % (len(only5), [z[:2] for z in only5]))
print("    from 3w == 1/2 only (all three sectors' R_i vanish there): %d  %s" % (len(only3), [z[:2] for z in only3]))
print("    both: %s" % [z[:2] for z in both])
print("    C1 set (agy's: also R_i^down != 0, R_j^up != 0, a not in {0, 1/2}): %d  %s" % (len(c1_set), c1_set))
# 3w == 1/2 lines: check that R_i vanishes in every sector there
for a, b in [(Fr(z[0]), Fr(z[1])) for z in only3][:6]:
    print("      3w-line (%s, %s): |R_i| up/down/lep at tau0 = %.1e %.1e %.1e" % (a, b, *[abs(Ri(s, a, b, TAUS[0])["i"]) for s in SECT]))

# --- (c) agy's count on main's 662 census lines --------------------------------------------------------------------
def _load(name, rel):
    sp = importlib.util.spec_from_file_location(name, ROOT / rel); m = importlib.util.module_from_spec(sp); sys.modules[name] = m; sp.loader.exec_module(m); return m
K26 = _load("b1726_census_chk", "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
K55 = _load("b1755_census_chk", "frontier/B1755_the_six_on_the_lines_of_order_13_to_20/verification/census.py")
L = [(Fr(a), Fr(b)) for a, b in K26.lines()] + [(Fr(a), Fr(b)) for a, b in K55.lines()]
c1_census = []
t = 0.3145 + 3.0345j
for a, b in L:
    Ru = Ri("up", a, b, t); Rd = Ri("down", a, b, t)
    if (a not in (0, Fr(1, 2))) and abs(Ru["i"]) < 1e-11 and abs(Ru["j"]) > 1e-8 and abs(Rd["i"]) > 1e-8:
        c1_census.append((str(a), str(b), math.lcm(a.denominator, b.denominator)))
OUT["census"] = {"n_lines": len(L), "C1_at_tau_probe": c1_census}
print("(c) main's census: %d lines; C1 at tau = 0.3145+3.0345i: %d  %s" % (len(L), len(c1_census), c1_census))

# --- (d) agy's numbers at its probe point and on the strip -------------------------------------------------------
def inv_and_ratio(a, b, t):
    R = Ri("up", a, b, t); u = np.array([R["i"], R["j"], R["k"]])
    return float(abs(u @ u) / np.vdot(u, u).real), float(math.hypot(abs(R["j"]), abs(R["k"])) / abs(R["1"]))
orb = {}
for a in (Fr(1, 5), Fr(2, 5)):
    vals = [inv_and_ratio(a, Fr(k, 10), t) for k in (1, 3, 5, 7, 9)]
    orb[str(a)] = {"I_up": [min(v[0] for v in vals), max(v[0] for v in vals)], "jk_over_1": [min(v[1] for v in vals), max(v[1] for v in vals)]}
    print("(d) orbit a=%s at tau=0.3145+3.0345i: I(u_up) %.5f .. %.5f ; ||R_jk||/|R_1| %.3f .. %.3f" % (a, *orb[str(a)]["I_up"], *orb[str(a)]["jk_over_1"]))
OUT["orbits"] = orb
strip = [0.3145 + 3.0345j, (1 + 1j * math.sqrt(84)) / 3, 0.3145 + 3.10j, 0.3145 + 2.95j]
cs_rows = []
for t in strip:
    w = 0.4 * t + 0.1; ql, qr = SECT["down"]; x, y = Bf.sector_twists(w, t, ql, qr); R = Bf.residues(x, y, t); c = Bf.cA(x, y, t, R)
    xu, yu = Bf.sector_twists(w, t, *SECT["up"]); Ru = Bf.residues(xu, yu, t); u = np.array([Ru["i"], Ru["j"], Ru["k"]])
    cs_rows.append({"tau": [t.real, t.imag], "c": c, "abs_R_i_up": abs(Ru["i"]), "I_u_up": float(abs(u @ u) / np.vdot(u, u).real)})
    print("    strip tau=%.4f%+.4fi: c_1 %.4f c_i %.4f c_j %.4f c_k %.4f (c_j - c_k %.4f); |R_i^up| %.1e; I(u_up) %.4f"
          % (t.real, t.imag, c["1"], c["i"], c["j"], c["k"], c["j"] - c["k"], abs(Ru["i"]), cs_rows[-1]["I_u_up"]))
OUT["strip"] = cs_rows
json.dump(OUT, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1, default=str)
print("exit 0")
