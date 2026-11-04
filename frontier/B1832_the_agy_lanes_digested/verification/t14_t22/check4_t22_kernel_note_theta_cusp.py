"""CHECK 4 (agy Theorem 22 Parts A.1, A.3, B.1, B.2, B.4, C; Theorem 16 Part C).  Data-free.  MAIN's code only.

 B.1  pair sums at 2 tau: c_k + c_j (tau, p1, p2) = 2 c_j (2 tau, p1, 2 p2), c_1 + c_i (tau, p1, p2) = 2 c_1 (2 tau, p1, 2 p2)
      (every channel pairing is reported, so a relabelled law would show).
 B.2  sigma_b = c_j + c_k - c_1 - c_i on alpha in {1/12, 1/4, 5/12}: zero at general tau iff 12 p2 is an integer
      (tested OFF the census lines too).
 B.4  c_inf(3/8), c_inf(1/8) closed forms (Gauss digamma), and main's cA on (1/8, p2) approaching them.
 C    theta_Y = arg det Y_u + arg det Y_d under p2 -> p2 - 1 (w -> w + 1, the lane's b -> b + 1): shift 264 pi p1 mod 2 pi,
      per sector 12 pi p1 (q_L^2 + q_R^2); FR-FIB's Higgs (main's direction 'DR'), both readings of up; and the
      Diophantine lemma 66 a^2 + 1/4 not in Z (so P-323's T-step -132 pi a^2 - pi/2 is never 0 mod 2 pi).
 A.1  'all sector-dependent cusp exponents come exclusively from (q_L - q_R) alpha': the tie test R_1^up on (2/5, 0)
      against (2/5, 1/10) and (2/5, 3/10) (same alpha, same sector, different beta).
 A.3  W181 on (1/2, 1/5): the residue sub-claims at the cusp (|R_j/R_k| -> sqrt 5 in down, R_j^e = -R_j^d,
      R_i^e = R_i^d, chiral ratio -> cos(pi/5)/cos(2 pi/5)); the docstring's D formula evaluated as written.
 T16C (0, 2/7) sub-claims: |R_i^d/R_i^e| -> cos(2pi/7)/cos(3pi/7); |R_1^e/R_1^d| - 1 -> cos(3pi/7)/cos(pi/7).
"""
import cmath, itertools, json, math, pathlib
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp
import mainB

B = mainB.B()
HERE = pathlib.Path(__file__).resolve().parent
out = {}


def c_line(p1, p2, t, q=(1, 2)):
    w = B.line_w(p1, p2, t); x, y = B.sector_twists(w, t, *q); R = B.residues(x, y, t); return B.cA(x, y, t, R), R


# B.1
b1 = []
for (t, p1, p2) in [(0.17 + 1.45j, 0.4, 0.1), (0.31 + 1.3j, 1 / 7, 0.23), (-0.2 + 1.6j, 0.37, 0.61), (0.05 + 1.2j, 3 / 8, 0.0)]:
    c1, _ = c_line(p1, p2, t); c2, _ = c_line(p1, 2 * p2, 2 * t)
    pairs_ = {}
    for (a, b_) in itertools.combinations(["1", "i", "j", "k"], 2):
        for cc in ["1", "i", "j", "k"]:
            pairs_[f"c_{a}+c_{b_}(tau) - 2c_{cc}(2tau)"] = c1[a] + c1[b_] - 2 * c2[cc]
    hits = {k: v for k, v in pairs_.items() if abs(v) < 1e-8}
    b1.append({"tau": str(t), "line": (p1, p2), "zero_relations": hits,
               "claimed_kj": pairs_["c_j+c_k(tau) - 2c_j(2tau)"], "claimed_1i": pairs_["c_1+c_i(tau) - 2c_1(2tau)"]})
out["B1_pair_sums"] = b1
print("B1", json.dumps(b1, default=str)[:1500], flush=True)

# B.2
b2 = []
for a in (1 / 12, 0.25, 5 / 12):
    for p2 in (0.0, 1 / 12, 1 / 6, 0.25, 1 / 3, 1 / 8, 3 / 8, 1 / 10, 1 / 24, 0.37):
        for t in (0.13 + 1.9j, 0.0 + 1.9j):
            c, _ = c_line(a, p2, t)
            sb = c["j"] + c["k"] - c["1"] - c["i"]
            b2.append({"alpha": a, "p2": p2, "12p2": 12 * p2, "tau": str(t), "sigma_b": sb})
out["B2_sigma_b"] = b2
for r in b2:
    print("B2", f"alpha={r['alpha']:.4f} p2={r['p2']:.4f} 12p2={r['12p2']:.3f} tau={r['tau']} sigma_b={r['sigma_b']:.3e}", flush=True)

# B.4
mp.mp.dps = 30
cinf = lambda nu: 2 * mp.pi * (-mp.euler - mp.log(2 * mp.pi) - (mp.digamma(nu) + mp.digamma(1 - nu)) / 2)
cf38 = 2 * mp.pi * (mp.log(8 / mp.pi) - mp.sqrt(2) * mp.log(1 + mp.sqrt(2)))
cf18 = 2 * mp.pi * (mp.log(8 / mp.pi) + mp.sqrt(2) * mp.log(1 + mp.sqrt(2)))
out["B4_closed_form_err"] = [float(abs(cinf(mp.mpf(3) / 8) - cf38)), float(abs(cinf(mp.mpf(1) / 8) - cf18))]
out["B4_values"] = [float(cf38), float(cf18)]
b4 = []
for y in (3.0, 4.0, 5.0):
    c, _ = c_line(1 / 8, 0.17, complex(0.1, y)); b4.append({"Im_tau": y, "cA": c})
out["B4_main_cA_on_(1/8,0.17)"] = b4
print("B4", out["B4_closed_form_err"], out["B4_values"], b4, flush=True)

# C: theta_Y b-step
def Y(S, R, c, L=2.36):
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    return B.coupling(S, B.weighted_M(u))
cres = []
for t in (0.19 + 1.85j, 0.37 + 2.6j):
    a = mainB.direction("DR", t); S = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK; St = B.EPS @ S.conj() @ B.EPS.T
    for (p1, p2) in [(0.4, 0.13), (1 / 7, 0.3), (0.25, 0.41), (3 / 11, 0.07), (0.62, 0.55)]:
        dets = {}
        for shift in (0, 1):
            w = B.line_w(p1, p2 - shift, t)
            for sec in ("up", "down"):
                ql, qr = mainB.SECTORS[sec]; x, y = B.sector_twists(w, t, ql, qr); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
                for rd, SS in (("S", S), ("S~", St)):
                    dets[(shift, sec, rd)] = np.linalg.det(Y(SS, R, c))
        e = lambda z: cmath.exp(1j * cmath.phase(z))
        rec = {"tau": str(t), "line": (p1, p2)}
        for sec, Q2 in (("up", 17), ("down", 5)):
            for rd in ("S", "S~"):
                ratio = dets[(1, sec, rd)] / dets[(0, sec, rd)]
                rec[f"{sec}_{rd}_err_vs_12piQ2a"] = abs(e(ratio) - cmath.exp(12j * math.pi * Q2 * p1))
        for rdu in ("S", "S~"):
            th = dets[(1, "up", rdu)] * dets[(1, "down", "S")] / (dets[(0, "up", rdu)] * dets[(0, "down", "S")])
            rec[f"thetaY_up{rdu}_downS_err_vs_264pia"] = abs(e(th) - cmath.exp(264j * math.pi * p1))
            rec[f"thetaY_up{rdu}_downS_err_vs_minus264pia"] = abs(e(th) - cmath.exp(-264j * math.pi * p1))
        cres.append(rec)
out["C_theta_b_step"] = cres
print("C", json.dumps(cres, default=str)[:2500], flush=True)
dioph = sum(1 for s in range(1, 1001) for r in range(0, 2 * s + 1) if math.gcd(r, s) == 1 and (66 * Fr(r, s) ** 2 + Fr(1, 4)).denominator == 1)
out["C_diophantine_solutions_s_le_1000_r_le_2s"] = dioph
print("C dioph", dioph, flush=True)

# A.1 tie test
a1 = []
for p2 in (0.0, 0.2, 0.1, 0.3):
    for y in (2.0, 3.0, 4.0):
        t = complex(0.13, y); w = B.line_w(0.4, p2, t)
        rr = {}
        for sec in ("up", "down"):
            x, yy = B.sector_twists(w, t, *mainB.SECTORS[sec]); rr[sec] = B.residues(x, yy, t)
        a1.append({"line": (0.4, p2), "Im_tau": y, "abs_R1_up": abs(rr["up"]["1"]), "abs_R1_down": abs(rr["down"]["1"]),
                   "abs_Rk_up": abs(rr["up"]["k"])})
out["A1_tie_test"] = a1
for r in a1:
    print("A1", r, flush=True)

# A.3 and T16C cusp residues
cus = []
for y in (8.0, 10.0, 12.0):
    t = complex(0.125, y)
    for line in ((0.5, 0.2), (0.0, 2 / 7)):
        w = B.line_w(*line, t); rr = {}
        for sec in ("down", "lepton"):
            x, yy = B.sector_twists(w, t, *mainB.SECTORS[sec]); rr[sec] = B.residues(x, yy, t)
        d, e_ = rr["down"], rr["lepton"]
        rec = {"line": line, "Im_tau": y}
        if line == (0.5, 0.2):
            rec.update({"|Rj/Rk|_down": abs(d["j"] / d["k"]), "Rj_down/(-i sqrt5 Rk_down)": str(d["j"] / (-1j * math.sqrt(5) * d["k"])),
                        "Rj_e/Rj_d": str(e_["j"] / d["j"]), "Ri_e/Ri_d": str(e_["i"] / d["i"]),
                        "Rk_e/Rk_d": str(e_["k"] / d["k"]), "R1_e/R1_d": str(e_["1"] / d["1"]) if abs(d["1"]) > 1e-300 else None,
                        "chiral_down": abs(-d["k"] - 1j * d["j"]) / abs(-d["k"] + 1j * d["j"]),
                        "chiral_lepton": abs(-e_["k"] - 1j * e_["j"]) / abs(-e_["k"] + 1j * e_["j"])})
        else:
            rec.update({"|Ri_d/Ri_e|": abs(d["i"] / e_["i"]), "|R1_e/R1_d|-1": abs(e_["1"] / d["1"]) - 1,
                        "|Rj_e/Rj_d|": abs(e_["j"] / d["j"]), "|Rk_e/Rk_d|": abs(e_["k"] / d["k"])})
        cus.append(rec)
out["A3_T16C_cusp"] = cus
out["A3_targets"] = {"sqrt5": math.sqrt(5), "phi2=cos(pi/5)/cos(2pi/5)": math.cos(math.pi / 5) / math.cos(2 * math.pi / 5),
                     "cos2pi7/cos3pi7": math.cos(2 * math.pi / 7) / math.cos(3 * math.pi / 7),
                     "cos3pi7/cospi7": math.cos(3 * math.pi / 7) / math.cos(math.pi / 7),
                     "docstring_D=cot(pi/10)*cos(pi/5)/cos(2pi/5)": (1 / math.tan(math.pi / 10)) * math.cos(math.pi / 5) / math.cos(2 * math.pi / 5),
                     "code_D=cot(pi/10)+4cos(pi/5)": 1 / math.tan(math.pi / 10) + 4 * math.cos(math.pi / 5),
                     "cot(pi/20)": 1 / math.tan(math.pi / 20)}
for r in cus:
    print("A3/T16C", r, flush=True)
print("targets", out["A3_targets"])
(HERE / "check4_t22_kernel_note_theta_cusp_out.json").write_text(json.dumps(out, indent=1, default=str))
