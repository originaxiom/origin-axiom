"""CHECK 5 (P-593: 'every cusp limit a cosine ratio of the line's order'; agy Theorem 16 Part C, Theorem 22 Part A.3).
Data-free.  MAIN's code only (thc, th1, pairs, residues, line_w, sector_twists).

From check 1's factorisation, with s = a_x + a_y, beta = (b_x + b_y)/2, d = a_x - a_y, delta = b_x - b_y, dh = d - 1/2:
   P_k = C_k Theta_k / th1,  Theta_k = thc(s, beta),          C_k = i thc(d, delta/2, 0)
   P_j = C_j Theta_j / th1,  Theta_j = thc(s, beta + 1/2),    C_j = -e^{-i pi s} e^{-i pi d} thc(d, delta/2 + 1/2, 0)
   P_i = C_i Theta_i / th1,  Theta_i = thc(s + 1/2, beta),    C_i = -thc(dh, delta/2, 0)
   P_1 = C_1 Theta_1 / th1,  Theta_1 = thc(s + 1/2, beta + 1/2), C_1 = -i e^{-i pi (s + 1/2)} e^{-i pi dh} thc(dh, delta/2 + 1/2, 0)
(all theta at period tau).  Down and lepton share (s, beta) = (3 p1, -3 p2), so R_s^e / R_s^d = C_s^e / C_s^d EXACTLY:
a ratio of theta constants of the difference twist (d, delta) = ((q_L - q_R) p1, -2 (q_L - q_R) p2).  Cusp limit of
thc(a, b, 0): one leading term if ||a|| < 1/2 (modulus e^{-pi y ||a||^2}), two of equal modulus if ||a|| = 1/2, giving
2 cos(pi b) up to a phase.  So each lepton/down residue ratio tends to 0, infinity, 1, or |cos(pi b_e)/cos(pi b_d)| with
b = -(q_L - q_R) p2 (+1/2): a cosine ratio at multiples of pi p2.  Tested: (A) the explicit C_s at 10 random twists x 2 tau;
(B) the predicted cusp limits against main's residues at Im tau = 10 on 16 rational lines, both sectors' channels.
"""
import cmath, json, math, pathlib
from fractions import Fraction as Fr
import numpy as np
import mainB

B = mainB.B()
HERE = pathlib.Path(__file__).resolve().parent
rng = np.random.default_rng(593)


def consts(x, y, t):
    (ax, bx), (ay, by) = x, y
    s, beta, d, dl = ax + ay, 0.5 * (bx + by), ax - ay, bx - by; dh = d - 0.5
    th = lambda a, b, u: B.thc(a, b, u, t)
    C = {"k": 1j * th(d, dl / 2, np.array([0.0]))[0],
         "j": -cmath.exp(-1j * math.pi * s) * cmath.exp(-1j * math.pi * d) * th(d, dl / 2 + 0.5, np.array([0.0]))[0],
         "i": -th(dh, dl / 2, np.array([0.0]))[0],
         "1": -1j * cmath.exp(-1j * math.pi * (s + 0.5)) * cmath.exp(-1j * math.pi * dh) * th(dh, dl / 2 + 0.5, np.array([0.0]))[0]}
    Th = {"k": lambda u: th(s, beta, u), "j": lambda u: th(s, beta + 0.5, u),
          "i": lambda u: th(s + 0.5, beta, u), "1": lambda u: th(s + 0.5, beta + 0.5, u)}
    return C, Th


out = {}
ring = 0.27 * np.exp(2j * np.pi * (np.arange(24) + 0.3) / 24)
worst = 0.0
for t in (0.2 + 1.6j, -0.35 + 2.4j):
    for _ in range(10):
        x = (rng.uniform(-1.5, 1.5), rng.uniform(-2, 2)); y = (rng.uniform(-1.5, 1.5), rng.uniform(-2, 2))
        P = B.pairs(x, y, ring, t); T1 = B.th1(ring, t); C, Th = consts(x, y, t)
        for s in B.UNITS:
            worst = max(worst, float(np.max(np.abs(P[s] * T1 / (C[s] * Th[s](ring)) - 1))))
out["A_explicit_C_s_max_rel_err"] = worst
print("A explicit C_s max rel err", worst, flush=True)


def nz(a):
    a = Fr(a).limit_denominator(10**6); f = a - math.floor(a); return min(f, 1 - f)


def lead(a, b):
    """leading coefficient of thc(a, b, 0, tau) with e^{i pi tau ||a||^2} stripped: the n + a of minimal |n + a|"""
    a = Fr(a).limit_denominator(10**6); m = nz(a)
    ns = [n for n in range(-6, 7) if abs(n + a) == m]
    return m, sum(cmath.exp(2j * math.pi * float(n + a) * float(b)) for n in ns)


def predicted_ratio(p1, p2, s_key):
    """limit of |R_s^lepton / R_s^down| as Im tau -> infinity (None if 0 or infinity)"""
    vals = {}
    for sec in ("down", "lepton"):
        ql, qr = mainB.SECTORS[sec]
        d, half_dl = Fr(ql - qr) * p1, -Fr(ql - qr) * p2
        a = d if s_key in ("k", "j") else d - Fr(1, 2)
        b = half_dl + (Fr(1, 2) if s_key in ("j", "1") else 0)
        vals[sec] = lead(a, b)
    (md, ld), (me, le) = vals["down"], vals["lepton"]
    if md != me:
        return ("0" if me > md else "inf"), None
    if abs(ld) < 1e-12:
        return "down-leading-term-cancels", None
    return "finite", abs(le / ld)


lines = [(Fr(1, 2), Fr(1, 5)), (Fr(0), Fr(2, 7)), (Fr(1, 2), Fr(3, 10)), (Fr(2, 5), Fr(1, 10)), (Fr(1, 3), Fr(1, 7)),
         (Fr(0), Fr(1, 9)), (Fr(1, 4), Fr(1, 6)), (Fr(1, 2), Fr(1, 7)), (Fr(1, 6), Fr(2, 9)), (Fr(3, 8), Fr(1, 5)),
         (Fr(1, 2), Fr(2, 11)), (Fr(0), Fr(3, 13)), (Fr(1, 10), Fr(3, 7)), (Fr(2, 3), Fr(1, 12)), (Fr(1, 2), Fr(0)), (Fr(0), Fr(1, 4))]
rows = []
worstB = 0.0; n_finite = 0
for (p1, p2) in lines:
    for y in (10.0, 12.0):
        t = complex(0.137, y); w = B.line_w(float(p1), float(p2), t); R = {}
        for sec in ("down", "lepton"):
            x, yy = B.sector_twists(w, t, *mainB.SECTORS[sec]); R[sec] = B.residues(x, yy, t)
        for s in B.UNITS:
            kind, pred = predicted_ratio(p1, p2, s)
            num = abs(R["lepton"][s] / R["down"][s]) if abs(R["down"][s]) > 1e-250 else float("inf")
            rows.append({"line": (str(p1), str(p2)), "Im_tau": y, "channel": s, "kind": kind, "pred": pred, "main": num})
            if kind == "finite" and y == 12.0:
                n_finite += 1; worstB = max(worstB, abs(num - pred) / max(pred, 1e-12))
out["B_rows"] = rows; out["B_finite_cases_at_Im12"] = n_finite; out["B_max_rel_err_finite"] = worstB
for r in rows:
    if r["Im_tau"] == 12.0:
        print("B", r, flush=True)
print("B finite cases", n_finite, "max rel err", worstB)
(HERE / "check5_residue_constants_cusp_law_out.json").write_text(json.dumps(out, indent=1, default=str))
