#!/usr/bin/env python3
"""W149 — the cone and the defect: M's isotropic conic as the level-4 curve, R's line map, the quarter-turn bound on
every section's on-cone coordinate, and the quartic census in the record's frame (the rule: W149_RULE.md, committed
and pushed before this script).

  C1  the special lines: O = the projective group of <rho(S), rho(T)> (W134's rho_exact), each element taken as
      det(g) g; it preserves h.h; the isotropic eigenlines of its non-identity elements, deduplicated, with their
      stabilizer orders (equalities exact by sympy, inequalities by 50-digit evaluation with a margin of 1e-6); 2 000
      random points of the conic, stabilizer trivial with a margin of 1e-8
  C2  R (W146's R_and_DR, explicit theta series) at 30 digits: R.R / |R|^2 at 20 random tau; the T- and S-laws
      projectively; the stabilizers of [R(i)] and [R(omega)]; [R(iy)] approaching one Z4-line (y = 2, 4, 6, 8, 10);
      along tau = iy (y = 2, ..., 6) |s_R| / |q_4| against 2 sqrt 2 and R's far-null part over its leading one, read
      both against |s_R|^2 / 2 and, as in the scratch values the rule cites, against 4 e^{-pi y} (both must hold)
  C3  rho(T) in the line coordinates (sympy): diag(e^{2 pi i/8}, e^{2 pi i 3/8}, e^{2 pi i 7/8}); the exponent
      differences; on R, F2, dR and F_a (a = 6, ..., 26) the least-squares slope of ln|delta| against y over
      y = 4, ..., 8, against -pi/2 - k pi; |delta_dR| / |delta_R| approaching 2 (y = 4, 6, 8)
  C4  V = -|a|^2 + |a|^4 + lam |a.a|^2 + c sum |a_u|^4 on 400 draws of (lam, c) in [-0.45, 0.45]^2, 20 BFGS starts
      each; the least minimum classified by (y, A) = (|a.a|^2, sum |a_u|^4) / |a|^4 to 1e-6 against the four
      vertices; draws within 1e-3 of a line where two vertex values tie are set aside and counted
  R   read-outs: main's committed target.json (B1743, at W146's pinned revision, sha-checked): delta, epsilon, I,
      epsilon + delta^2 / 2 and the I it gives; the slope of ln|delta| on the L2 rows; the 26 lines' (y, A); R's Z4-line

    python3 -B the_cone_and_the_defect.py      # writes the_cone_and_the_defect.json beside itself
"""
import contextlib
import hashlib
import io
import itertools
import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_higgs_invariant_dichotomy as W146  # noqa: E402  (R_and_DR, F_a, lines, the target's pin)
    import the_bridge_e6_su3 as BR  # noqa: E402  (W134: rho_exact)

OUT = HERE / "the_cone_and_the_defect.json"
mp.mp.dps = 30
J = mp.mpc(0, 1)
PI = mp.pi
SQ2 = mp.sqrt(2)


def s(x, n=6):
    return mp.nstr(x, n)


# ---------------------------------------------------------------- C1

def group_O():
    rS, rT = BR.rho_exact()
    z = sp.exp(sp.I * sp.pi / 4)
    P, L = sp.simplify(rS / z), sp.simplify(rT / z)
    elems, frontier = {sp.ImmutableMatrix(sp.eye(3))}, [sp.ImmutableMatrix(sp.eye(3))]
    while frontier:
        new = []
        for g in frontier:
            for h in (P, L):
                k = sp.ImmutableMatrix(g * h)
                if k not in elems:
                    elems.add(k)
                    new.append(k)
        frontier = new
    rot = {sp.ImmutableMatrix(g.det() * g) for g in elems}
    return sorted(rot, key=lambda m: str(list(m))), len(elems)


def num(v, dps=50):
    """a sympy vector at dps digits, through strings (sympy integers have no _mpf_)"""
    with mp.workdps(dps):
        out = []
        for x in v:
            xv = sp.N(x, dps + 5)
            out.append(mp.mpc(mp.mpf(str(sp.re(xv))), mp.mpf(str(sp.im(xv)))))
        return out


def wedge(v, w):
    return [v[1] * w[2] - v[2] * w[1], v[2] * w[0] - v[0] * w[2], v[0] * w[1] - v[1] * w[0]]


def parallel_exact(v, w):
    return all(sp.simplify(sp.expand(x)) == 0 for x in wedge(v, w))


def parallel_num(v, w, dps=50):
    with mp.workdps(dps):
        a, b = num(v, dps), num(w, dps)
        return mp.sqrt(sum(abs(x) ** 2 for x in wedge(a, b))) / mp.sqrt(sum(abs(x) ** 2 for x in a) *
                                                                         sum(abs(x) ** 2 for x in b))


def same_line(v, w):
    d = parallel_num(v, w)
    if d > mp.mpf("1e-6"):
        return False
    return parallel_exact(v, w)


def isotropic_lines_of(g):
    out = []
    for val, mult, vecs in sp.Matrix(g).eigenvects():
        if len(vecs) == 1:
            v = list(vecs[0])
            if sp.simplify(sp.expand(sum(x * x for x in v))) == 0:
                out.append(v)
        elif len(vecs) == 2:
            u, w = list(vecs[0]), list(vecs[1])
            t = sp.symbols("t")
            uu = sp.simplify(sum(x * x for x in u))
            uw = sp.simplify(sum(x * y for x, y in zip(u, w)))
            ww = sp.simplify(sum(y * y for y in w))
            if ww == 0:
                out.append(w)
            for r in sp.solve(sp.Eq(uu + 2 * t * uw + t ** 2 * ww, 0), t):
                out.append([sp.simplify(x + r * y) for x, y in zip(u, w)])
    return out


def stabilizer(G, v):
    return sum(1 for g in G if same_line(list(sp.Matrix(g) * sp.Matrix(v)), v))


def C1(rng):
    G, n_lin = group_O()
    ident = sp.ImmutableMatrix(sp.eye(3))
    preserve = all(sp.simplify(g.T * g - sp.eye(3)) == sp.zeros(3, 3) for g in G)
    cands = []
    for g in G:
        if g != ident:
            cands += isotropic_lines_of(g)
    lines = []
    for v in cands:
        if not any(same_line(v, w) for w in lines):
            lines.append(v)
    stabs = [stabilizer(G, v) for v in lines]
    counts = {str(k): stabs.count(k) for k in sorted(set(stabs))}
    h0 = [0, 1, sp.I]
    h0_in = [stabs[i] for i, v in enumerate(lines) if same_line(v, h0)]
    # random points of the conic: h0 + s e1 - (s^2/2) conj h0, with h0, conj h0 unnormalised as (0, 1, +-i)/sqrt 2
    Gn = [np.array(sp.Matrix(g).evalf(), dtype=complex) for g in G if g != ident]
    e1, a0, b0 = np.array([1, 0, 0], complex), np.array([0, 1, 1j]) / np.sqrt(2), np.array([0, 1, -1j]) / np.sqrt(2)
    worst_null, least_wedge = 0.0, np.inf
    for _ in range(2000):
        sv = complex(rng.normal(), rng.normal()) * 10 ** rng.uniform(-1, 1)
        h = a0 + sv * e1 - sv * sv / 2 * b0
        h = h / np.linalg.norm(h)
        worst_null = max(worst_null, abs(h @ h))
        for g in Gn:
            least_wedge = min(least_wedge, np.linalg.norm(np.cross(g @ h, h)))
    yA = []
    for v, k in zip(lines, stabs):
        a = num(v, 30)
        n2 = sum(abs(x) ** 2 for x in a)
        yA.append({"stabilizer": k, "y": s(abs(sum(x * x for x in a)) ** 2 / n2 ** 2, 8),
                   "A": s(sum(abs(x) ** 4 for x in a) / n2 ** 2, 8)})
    res = {"the generated group (linear), order": n_lin, "projective elements det(g) g": len(G),
           "every element preserves h.h": bool(preserve), "candidate isotropic eigenlines": len(cands),
           "distinct special lines": len(lines), "stabilizer order: number of lines": counts,
           "h0's stabilizer": h0_in, "random conic points: max |h.h|": "%.2e" % worst_null,
           "random conic points: least |g h ^ h| over g != 1": "%.3e" % least_wedge}
    ok = (len(G) == 24 and preserve and len(lines) == 26 and counts == {"2": 12, "3": 8, "4": 6}
          and h0_in == [4] and least_wedge > 1e-8)
    return res, bool(ok), G, lines, stabs, yA


# ---------------------------------------------------------------- C2

def R(tau):
    return W146.R_and_DR(tau)[0]


def pdist(a, b):
    """projective (sine) distance between two complex 3-vectors"""
    w = wedge(a, b)
    return mp.sqrt(sum(abs(x) ** 2 for x in w) / (sum(abs(x) ** 2 for x in a) * sum(abs(x) ** 2 for x in b)))


def apply(M, v):
    return [sum(M[i][j] * v[j] for j in range(3)) for i in range(3)]


def to_mp(g):
    return [num([g[i, j] for j in range(3)], 40) for i in range(3)]


def chart(v):
    """(delta, far over lead, which lead) in W146's line coordinates: v = l1 e1 + l3 h0/sqrt2 + l7 conj(h0)/sqrt2"""
    l1, l3, l7 = W146.lines(v)
    lead, other, name = (l3, l7, "h0") if abs(l3) >= abs(l7) else (l7, l3, "conj h0")
    return SQ2 * l1 / lead, other / lead, name


def C2(rng, G, lines, stabs):
    rS, rT = BR.rho_exact()
    MS, MT = to_mp(rS), to_mp(rT)
    worst_null, worst_T, worst_S = mp.mpf(0), mp.mpf(0), mp.mpf(0)
    for _ in range(20):
        tau = mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(0.6, 2.0))
        r = R(tau)
        worst_null = max(worst_null, abs(sum(x * x for x in r)) / sum(abs(x) ** 2 for x in r))
        worst_T = max(worst_T, pdist(R(tau + 1), apply(MT, r)))
        worst_S = max(worst_S, pdist(R(-1 / tau), apply(MS, r)))
    Gm = [to_mp(g) for g in G]

    def stab_num(v):
        return sum(1 for g in Gm if pdist(apply(g, v), v) < mp.mpf("1e-20"))

    omega = mp.exp(2 * PI * J / 3)
    st_i, st_w = stab_num(R(J)), stab_num(R(omega))
    z4 = [num(v, 30) for v, k in zip(lines, stabs) if k == 4]
    approach = []
    for y in (2, 4, 6, 8, 10):
        r = R(mp.mpc(0, y))
        d = [pdist(r, v) for v in z4]
        k = min(range(len(d)), key=lambda i: d[i])
        approach.append((y, k, d[k]))
    one_line = len({k for _, k, _ in approach}) == 1
    decreasing = all(approach[i + 1][2] < approach[i][2] for i in range(len(approach) - 1))
    consts = []
    for y in (2, 3, 4, 5, 6):
        dl, far, name = chart(R(mp.mpc(0, y)))
        q4 = mp.e ** (-PI * y / 2)
        consts.append({"y": y, "lead": name, "|s_R|/|q4|": abs(dl) / q4,
                       "|far/lead| / (|s_R|^2/2) - 1": abs(far) / (abs(dl) ** 2 / 2) - 1,
                       "|far/lead| e^{pi y}": abs(far) * mp.e ** (PI * y)})

    def rel(c, key, target):
        return abs(c[key] - target) / target

    tol = {2: mp.mpf("2e-5"), 3: mp.mpf("1e-6")}
    ok_consts = all(rel(c, "|s_R|/|q4|", 2 * SQ2) < tol[c["y"]] and abs(c["|far/lead| / (|s_R|^2/2) - 1"]) < tol[c["y"]]
                    and rel(c, "|far/lead| e^{pi y}", mp.mpf(4)) < tol[c["y"]] for c in consts if c["y"] in tol)
    res = {"max R.R / |R|^2 (20 tau)": s(worst_null, 3), "T-law, max projective distance": s(worst_T, 3),
           "S-law, max projective distance": s(worst_S, 3), "stabilizer of [R(i)]": st_i,
           "stabilizer of [R(omega)]": st_w,
           "[R(iy)] against the nearest Z4-line (y, line index, distance)": [[y, k, s(d, 4)] for y, k, d in approach],
           "chart constants along tau = iy": [{k: (s(v, 9) if not isinstance(v, (int, str)) else v)
                                              for k, v in c.items()} for c in consts]}
    ok = (worst_null < mp.mpf("1e-25") and worst_T < mp.mpf("1e-20") and worst_S < mp.mpf("1e-20") and st_i == 2
          and st_w == 3 and one_line and decreasing and approach[-1][2] < mp.mpf("1e-3") and ok_consts)
    return res, bool(ok), approach[-1][1]


# ---------------------------------------------------------------- C3

def C3():
    rS, rT = BR.rho_exact()
    Lm = sp.Matrix([[1, 0, 0], [0, 1, -sp.I], [0, 1, sp.I]])
    D = sp.simplify(Lm * rT * Lm.inv())
    want = [sp.exp(2 * sp.pi * sp.I * sp.Rational(k, 8)) for k in (1, 3, 7)]
    diag_ok = all(sp.simplify(D[i, j] - (want[i] if i == j else 0)) == 0 for i in range(3) for j in range(3))
    diffs = sorted({str((sp.Rational(1, 8) - sp.Rational(k, 8)) % 1) for k in (3, 7)})
    forms = {"R": 0, "F2": 0, "dR": 0}
    forms.update({"F%d" % a: (a - 2) // 4 for a in (6, 10, 14, 18, 22, 26)})
    ys = [4, 5, 6, 7, 8]
    slopes, worst = {}, 0.0
    for name, k in forms.items():
        ld = []
        for y in ys:
            dl, _, lead = chart(W146.record_form(name, mp.mpc(0, y)))
            ld.append(float(mp.log(abs(dl))))
        sl = float(np.polyfit(ys, ld, 1)[0])
        want_sl = -float(PI) / 2 - k * float(PI)
        slopes[name] = {"k": k, "slope": round(sl, 7), "predicted": round(want_sl, 7), "lead at y = 8": lead}
        worst = max(worst, abs(sl - want_sl))
    ratio = []
    for y in (4, 6, 8):
        tau = mp.mpc(0, y)
        rr, dd = W146.R_and_DR(tau)
        ratio.append((y, abs(chart(dd)[0]) / abs(chart(rr)[0])))
    rok = abs(ratio[-1][1] - 2) < 1e-3 and abs(ratio[-1][1] - 2) <= abs(ratio[0][1] - 2)
    res = {"rho(T) in line coordinates is diag(e^{2 pi i (1, 3, 7)/8})": bool(diag_ok),
           "e1's exponent minus each null line's, mod 1": diffs, "slopes of ln|delta| over y = 4..8": slopes,
           "max |slope - predicted|": "%.2e" % worst,
           "|delta_dR| / |delta_R| (y = 4, 6, 8)": [[y, s(r, 12)] for y, r in ratio]}
    ok = diag_ok and diffs == ["1/4", "3/4"] and worst < 1e-3 and rok
    return res, bool(ok)


# ---------------------------------------------------------------- C4

VERTS = {"6-orbit (0, 1, i)": (0.0, 0.5), "8-orbit (1, w, w^2)": (0.0, 1 / 3), "(1, 0, 0)": (1.0, 1.0),
         "(1, 1, 1)": (1.0, 1 / 3)}


def yA_of(a):
    n2 = np.vdot(a, a).real
    return abs(a @ a) ** 2 / n2 ** 2, np.sum(np.abs(a) ** 4) / n2 ** 2


def C4(rng):
    tally = {k: 0 for k in VERTS}
    tally["unclassified"], set_aside, mismatch, worst = 0, 0, 0, 0.0
    for _ in range(400):
        lam, c = rng.uniform(-0.45, 0.45, size=2)
        # the lines where two vertex values tie, as (coefficient of lam, coefficient of c); Euclidean distance
        ties = ((0, 1), (1, 0.5), (1, -1 / 6), (1, 2 / 3), (1, 0))
        if min(abs(p * lam + q * c) / np.hypot(p, q) for p, q in ties) < 1e-3:
            set_aside += 1
            rng.normal(size=(20, 6))
            continue

        def V(p, lam=lam, c=c):
            a = p[:3] + 1j * p[3:]
            n2 = np.vdot(a, a).real
            return -n2 + n2 * n2 + lam * abs(a @ a) ** 2 + c * np.sum(np.abs(a) ** 4)

        best = None
        for x0 in rng.normal(size=(20, 6)):
            r = minimize(V, x0, method="BFGS", options={"gtol": 1e-12, "maxiter": 20000})
            if best is None or r.fun < best.fun:
                best = r
        a = best.x[:3] + 1j * best.x[3:]
        y, A = yA_of(a)
        dist = {k: max(abs(y - v[0]), abs(A - v[1])) for k, v in VERTS.items()}
        k = min(dist, key=dist.get)
        if dist[k] < 1e-6:
            tally[k] += 1
            worst = max(worst, dist[k])
            vals = {kk: lam * v[0] + c * v[1] for kk, v in VERTS.items()}
            if min(vals, key=vals.get) != k:
                mismatch += 1
        else:
            tally["unclassified"] += 1
    res = {"draws": 400, "set aside (within 1e-3 of a tie)": set_aside, "classes": tally,
           "classified but not the vertex minimizing lam y + c A": mismatch,
           "largest distance to the class's vertex": "%.2e" % worst}
    ok = tally["unclassified"] == 0 and mismatch == 0 and sum(tally.values()) + set_aside == 400
    return res, bool(ok)


# ---------------------------------------------------------------- R

def readouts(yA, z4_index, lines, stabs):
    root = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=HERE, capture_output=True, text=True,
                               check=True).stdout.strip())
    raw = subprocess.run(["git", "show", "%s:%s" % (W146.REV_MAIN, W146.TARGET)], cwd=root, capture_output=True,
                         check=True).stdout
    sha = hashlib.sha256(raw).hexdigest()
    opt = json.loads(raw.decode("utf-8"))["optima"]
    rows, L2 = [], []
    for o in opt:
        d, e = complex(*o["delta"]), complex(*o["epsilon"])
        dec = e + d * d / 2
        I_rec = abs(2 * dec) / (1 + abs(d) ** 2 + abs(e) ** 2)
        rows.append({"line": o["line"], "tau": o["tau"], "hor": o["hor"], "leading": o["leading"],
                     "|delta|": round(abs(d), 5), "epsilon + delta^2/2": [round(dec.real, 5), round(dec.imag, 5)],
                     "I from delta and epsilon": round(I_rec, 5), "I recorded": o["|h.h|/|h|^2"]})
        if o["hor"].replace("_", "").replace("₂", "2").upper() == "L2":
            L2.append((float(o["tau"][1]), np.log(abs(d))))
    slope = float(np.polyfit([y for y, _ in L2], [v for _, v in L2], 1)[0]) if len(L2) >= 2 else None
    z4 = [v for v, k in zip(lines, stabs) if k == 4]
    v = num(z4[z4_index], 30)
    _, _, name = chart(v)
    return {"target sha256 as pinned": sha == W146.TARGET_SHA, "rows": rows,
            "slope of ln|delta| against Im tau, L2 rows": slope, "the bound's slope": -float(PI) / 2,
            "the 26 lines' (stabilizer, y, A)": yA, "R's Z4-line at the cusp, in W146's naming": name}


def main():
    rng = np.random.default_rng(149)
    out = {"arc": "W149", "rule": "W149_RULE.md", "status": "one run", "python": sys.version.split()[0]}
    out["C1"], ok1, G, lines, stabs, yA = C1(rng)
    out["C2"], ok2, z4_index = C2(rng, G, lines, stabs)
    out["C3"], ok3 = C3()
    out["C4"], ok4 = C4(rng)
    out["R"] = readouts(yA, z4_index, lines, stabs)
    out["cells"] = {"C1": ok1, "C2": ok2, "C3": ok3, "C4": ok4}
    out["every predicted cell holds"] = bool(all(out["cells"].values()))
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every predicted cell holds:", out["every predicted cell holds"])


if __name__ == "__main__":
    main()
