#!/usr/bin/env python3
"""W152 — the Higgs as a qubit state: R is the square of the theta qubit, the modular group moves it by the weave's
Clifford gates, the cone's special lines are the stabilizer and magic states, and every direction is a squared qubit
plus its weighted antipode with I = 2r/(1 + r^2) (the rule: W152_RULE.md, committed and pushed before this script).

  psi0 = (eps, theta) = (Theta2(2 tau), Theta3(2 tau)), direct sums (W146's thetas at 2 tau). In W146's lines
  (l1, l3, l7), S_h = [[l3, -l1], [-l1, -l7]]; Sym^2 of (a, b) is (l1, l3, l7) = (-ab, a^2, -b^2); g acts by g S g^T.

  K1  (l1, l3, l7)(R) = eta^-3 (-eps theta, eps^2, -theta^2) at 20 random tau (Im tau in [0.9, 4]), to 1e-25 of |R|
  K2  psi0(tau + 1) = g_T psi0(tau), psi0(-1/tau) = sqrt(-i tau) g_S psi0(tau) at the same tau, to 1e-25; the
      projective group <g_T, g_S> has 24 elements; Sym^2 g_T and Sym^2 g_S equal rho(T) and rho(S) (W134's
      rho_exact, in W146's lines) projectively, to 1e-25; U = e^{i pi Z/4} carries (g_T, g_S g_T^-1 g_S^-1) to
      (e^{i pi Z/4}, e^{-i pi Y/4}) projectively (sympy, exact)
  K3  Sym^2 of the 6 stabilizer, 8 F-type and 12 H-type states against W149's 26 lines (group_O, isotropic_lines_of,
      stabilizer), one to one, projectively to 1e-40 (W149's parallel_num at 50 digits), with stabilizer orders 4, 3, 2
      on both sides
  K4  sympy: det S_h = -h.h and ||S_h||^2 = 2|h|^2; on 2 000 random h: I (from x, y, z) against 2r/(1 + r^2) (r from
      S_h's singular values) to 1e-25; under each of the 24 projective elements r unchanged and u1 moved by the
      element, to 1e-25 (the u1 check set aside for r > 0.999)
  K5  along tau = iy, y = 4, ..., 8, for the 24 objects (W146's 12 record forms and their conjugates): R, F2 and
      conjugates r < 1e-25; the other null-led ones: (ln r(8) - ln r(4))/4 within 1e-3 of -pi and
      1 - |<u1, s>| < 1e-6 at y = 8, s = (1, 0) for an l3 lead and (0, 1) for an l7 lead; the e1-led ones 1 - r < 1e-3
      at y = 8
  R   read-outs: on B1743's ten rows, r, u1's Bloch angle from (1, 0), the nearest special state and its angle, and
      R's own Bloch angle from its nearest stabilizer state at the row's tau; the L2 slopes of ln r and of the angle

  The singular values of the 2 x 2 matrix S come from H = S S^dagger: sigma1^2 is H's top eigenvalue and
  sigma2 = |det S| / sigma1 (no cancellation), so r = |det S| / sigma1^2.

    python3 -B the_higgs_as_a_qubit.py      # writes the_higgs_as_a_qubit.json beside itself
"""
import contextlib
import hashlib
import io
import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_higgs_invariant_dichotomy as W146  # noqa: E402  (thetas, eta_pow, record_form, lines, conj, the pin)
    import the_cone_and_the_defect as W149  # noqa: E402  (group_O, isotropic_lines_of, stabilizer, parallel_num)

OUT = HERE / "the_higgs_as_a_qubit.json"
mp.mp.dps = 50
J = mp.mpc(0, 1)
PI = mp.pi
SQ2 = mp.sqrt(2)
TOL = mp.mpf(10) ** -25


def s(x, n=6):
    return mp.nstr(x, n)


def psi0(tau):
    t = W146.thetas(2 * tau)
    return [t[0], t[1]]


def M2(rows):
    return [[mp.mpc(x) for x in r] for r in rows]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def tr(A):
    return [[A[j][i] for j in range(2)] for i in range(2)]


def app(A, v):
    return [A[0][0] * v[0] + A[0][1] * v[1], A[1][0] * v[0] + A[1][1] * v[1]]


def S_of(l):
    l1, l3, l7 = l
    return [[l3, -l1], [-l1, -l7]]


def lines_of_S(S):
    return [-S[0][1], S[0][0], -S[1][1]]


def sym2(v):
    a, b = v
    return [-a * b, a * a, -b * b]


def vnorm(v):
    return mp.sqrt(sum(abs(x) ** 2 for x in v))


def pdist(a, b):
    """projective distance of two vectors (or flattened matrices): min_c |a - c b| / |a|"""
    bb = sum(abs(x) ** 2 for x in b)
    c = sum(mp.conj(y) * x for x, y in zip(a, b)) / bb
    return vnorm([x - c * y for x, y in zip(a, b)]) / vnorm(a)


def flat(A):
    return [x for row in A for x in row]


def takagi(S):
    """r = sigma2/sigma1 and u1 (unit) of a 2 x 2 complex symmetric S, from H = S S^dagger"""
    H = mul(S, [[mp.conj(S[j][i]) for j in range(2)] for i in range(2)])
    t = (H[0][0] + H[1][1]).real
    d = abs(S[0][0] * S[1][1] - S[0][1] * S[1][0])
    disc = mp.sqrt(max((H[0][0] - H[1][1]).real ** 2 + 4 * abs(H[0][1]) ** 2, mp.mpf(0)))
    lam1 = (t + disc) / 2
    r = d / lam1
    c1 = [H[0][1], lam1 - H[0][0]]
    c2 = [lam1 - H[1][1], H[1][0]]
    u = c1 if vnorm(c1) >= vnorm(c2) else c2
    n = vnorm(u)
    return r, [x / n for x in u]


def overlap(u, v):
    return abs(sum(mp.conj(x) * y for x, y in zip(u, v))) / (vnorm(u) * vnorm(v))


# ---------------------------------------------------------------- the group on the qubit

G_T = M2([[J, 0], [0, 1]])
G_S = M2([[-1 / SQ2, 1 / SQ2], [1 / SQ2, 1 / SQ2]])


def canon(A):
    f = next(x for x in flat(A) if abs(x) > mp.mpf("1e-10"))
    return [[x / f for x in row] for row in A]


def key(A):
    """rounded floats: tiny numerical zeros round to 0.0 (and -0.0 == 0.0 hashes alike)"""
    return tuple((round(float(x.real), 10), round(float(x.imag), 10)) for x in flat(canon(A)))


def qubit_group():
    I2 = M2([[1, 0], [0, 1]])
    elems, frontier = {key(I2): I2}, [I2]
    while frontier:
        new = []
        for g in frontier:
            for h in (G_T, G_S):
                k = mul(g, h)
                kk = key(k)
                if kk not in elems:
                    elems[kk] = k
                    new.append(k)
        frontier = new
    return list(elems.values())


def sym2_matrix(g):
    """the 3 x 3 matrix of S -> g S g^T on (l1, l3, l7)"""
    cols = []
    for e in ([1, 0, 0], [0, 1, 0], [0, 0, 1]):
        Sp = mul(mul(g, S_of([mp.mpc(x) for x in e])), tr(g))
        cols.append(lines_of_S(Sp))
    return [[cols[j][i] for j in range(3)] for i in range(3)]


def rho_lines():
    rS, rT = W149.BR.rho_exact()
    Ml = sp.Matrix([[1, 0, 0], [0, 1, -sp.I], [0, 1, sp.I]])
    out = []
    for r in (rT, rS):
        m = (Ml * r * Ml.inv()).evalf(60)
        out.append([[mp.mpc(str(sp.re(m[i, j])), str(sp.im(m[i, j]))) for j in range(3)] for i in range(3)])
    return out


# ---------------------------------------------------------------- K1, K2

def taus(rng, n=20):
    return [mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(0.9, 4.0)) for _ in range(n)]


def K1(ts):
    worst = mp.mpf(0)
    for t in ts:
        l = W146.lines(W146.R_and_DR(t)[0])
        e, th = psi0(t)
        f = W146.eta_pow(t, -3)
        pred = [f * x for x in sym2([e, th])]
        worst = max(worst, vnorm([a - b for a, b in zip(l, pred)]) / vnorm(l))
    return {"worst |lines(R) - eta^-3 Sym^2 psi0| / |R|": s(worst, 3)}, bool(worst < TOL)


def K2(ts):
    wT, wS = mp.mpf(0), mp.mpf(0)
    for t in ts:
        p, pT, pS = psi0(t), psi0(t + 1), psi0(-1 / t)
        a = app(G_T, p)
        wT = max(wT, vnorm([x - y for x, y in zip(pT, a)]) / vnorm(p))
        b = [mp.sqrt(-J * t) * x for x in app(G_S, p)]
        wS = max(wS, vnorm([x - y for x, y in zip(pS, b)]) / vnorm(pS))
    grp = qubit_group()
    rT, rS = rho_lines()
    dT = pdist(flat(rT), flat(sym2_matrix(G_T)))
    dS = pdist(flat(rS), flat(sym2_matrix(G_S)))
    # exact: U = e^{i pi Z / 4}
    z = (1 + sp.I) / sp.sqrt(2)
    U = sp.diag(z, (1 - sp.I) / sp.sqrt(2))
    gT = sp.diag(sp.I, 1)
    gS = sp.Matrix([[-1, 1], [1, 1]]) / sp.sqrt(2)
    Z = sp.diag(1, -1)
    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    eZ = sp.cos(sp.pi / 4) * sp.eye(2) + sp.I * sp.sin(sp.pi / 4) * Z
    eY = sp.cos(sp.pi / 4) * sp.eye(2) - sp.I * sp.sin(sp.pi / 4) * Y

    def scalar(M):
        M = sp.simplify(M)
        return sp.simplify(M[0, 1]) == 0 and sp.simplify(M[1, 0]) == 0 and sp.simplify(M[0, 0] - M[1, 1]) == 0

    A = U * gT * U.inv() * eZ.inv()
    Bm = U * gS * gT.inv() * gS.inv() * U.inv() * eY.inv()
    okU = bool(scalar(A) and scalar(Bm))
    X = sp.Matrix([[0, 1], [1, 0]])
    eX = sp.cos(sp.pi / 4) * sp.eye(2) + sp.I * sp.sin(sp.pi / 4) * X
    ok_hand = bool(scalar(gS * gT.inv() * gS.inv() * eX.inv()))
    res = {"T-law worst": s(wT, 3), "S-law worst": s(wS, 3), "projective group order": len(grp),
           "Sym^2 g_T vs rho(T), projective": s(dT, 3), "Sym^2 g_S vs rho(S), projective": s(dS, 3),
           "U = e^{i pi Z/4} carries (g_T, g_S g_T^-1 g_S^-1) to (e^{i pi Z/4}, e^{-i pi Y/4})": okU,
           "g_S g_T^-1 g_S^-1 proportional to e^{i pi X/4}": ok_hand}
    ok = wT < TOL and wS < TOL and len(grp) == 24 and dT < TOL and dS < TOL and okU
    return res, bool(ok), grp


# ---------------------------------------------------------------- K3

def special_states():
    r2, r3 = sp.sqrt(2), sp.sqrt(3)
    stab = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    F = [(a / r3, b / r3, c / r3) for a in (1, -1) for b in (1, -1) for c in (1, -1)]
    H = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        for a in (1, -1):
            for b in (1, -1):
                v = [0, 0, 0]
                v[i], v[j] = a / r2, b / r2
                H.append(tuple(v))
    out = []
    for kind, vs in (("stabilizer", stab), ("F", F), ("H", H)):
        for nx, ny, nz in vs:
            st = [sp.Integer(0), sp.Integer(1)] if nz == -1 else [sp.sympify(1 + nz), sp.sympify(nx + sp.I * ny)]
            out.append((kind, (nx, ny, nz), st))
    return out


def to_xyz(l):
    l1, l3, l7 = l
    return [l1, (l3 + l7) / 2, (l7 - l3) / (2 * sp.I)]


def K3(grp):
    G, _ = W149.group_O()
    ident = sp.ImmutableMatrix(sp.eye(3))
    cands = []
    for g in G:
        if g != ident:
            cands += W149.isotropic_lines_of(g)
    lines = []
    for v in cands:
        if not any(W149.same_line(v, w) for w in lines):
            lines.append(v)
    stabs = [W149.stabilizer(G, v) for v in lines]
    want = {"stabilizer": 4, "F": 3, "H": 2}
    matched, used, worst, ok = [], set(), mp.mpf(0), len(lines) == 26
    for kind, n, st in special_states():
        a, b = st
        vx = [sp.simplify(x) for x in to_xyz([-a * b, a * a, -b * b])]
        dists = [W149.parallel_num(vx, w) for w in lines]
        j = min(range(len(lines)), key=lambda k: dists[k])
        stq = sum(1 for g in grp if pdist(app(g, [mp.mpc(complex(sp.N(a, 30))), mp.mpc(complex(sp.N(b, 30)))]),
                                           [mp.mpc(complex(sp.N(a, 30))), mp.mpc(complex(sp.N(b, 30)))]) < 1e-12)
        worst = max(worst, dists[j])
        good = dists[j] < mp.mpf(10) ** -40 and j not in used and stabs[j] == want[kind] and stq == want[kind]
        ok = ok and good
        used.add(j)
        matched.append({"kind": kind, "Bloch": [str(x) for x in n], "W149 line": j,
                        "projective distance": s(dists[j], 3), "W149 stabilizer": stabs[j], "qubit stabilizer": stq})
    h0 = [i for i, m in enumerate(matched) if m["Bloch"] == ["0", "0", "1"]]
    h0_ok = bool(h0) and W149.same_line(lines[matched[h0[0]]["W149 line"]], [0, 1, sp.I])
    res = {"W149's distinct lines": len(lines), "states matched one to one": len(used) == 26,
           "largest projective distance": s(worst, 3), "(1, 0) goes to h0": h0_ok, "matches": matched}
    return res, bool(ok and len(used) == 26 and h0_ok)


# ---------------------------------------------------------------- K4

def K4(rng, grp, n=2000):
    a = sp.symbols("a1:4", real=True)
    b = sp.symbols("b1:4", real=True)
    x, y, z = [a[k] + sp.I * b[k] for k in range(3)]
    l1, l3, l7 = x, y - sp.I * z, y + sp.I * z
    S = sp.Matrix([[l3, -l1], [-l1, -l7]])
    ok_det = sp.expand(S.det() + (x * x + y * y + z * z)) == 0
    ab2 = lambda w: sp.expand(w * sp.conjugate(w))
    ok_norm = sp.expand(sum(ab2(e) for e in S) - 2 * (ab2(x) + ab2(y) + ab2(z))) == 0
    unit = []
    for g in grp:
        d = g[0][0] * g[1][1] - g[0][1] * g[1][0]
        f = mp.sqrt(abs(d))
        unit.append([[e / f for e in row] for row in g])
    wI, wr, wu, aside = mp.mpf(0), mp.mpf(0), mp.mpf(0), 0
    for _ in range(n):
        v = [mp.mpc(rng.normal(), rng.normal()) for _ in range(3)]
        Sv = S_of(W146.lines(v))
        r, u = takagi(Sv)
        wI = max(wI, abs(W146.inv(v) - 2 * r / (1 + r * r)))
        for g in unit:
            Sp = mul(mul(g, Sv), tr(g))
            rp, up = takagi(Sp)
            wr = max(wr, abs(rp - r))
            if r > mp.mpf("0.999"):
                aside += 1
                continue
            wu = max(wu, 1 - overlap(up, app(g, u)))
    res = {"det S_h = -h.h (sympy)": bool(ok_det), "||S_h||^2 = 2|h|^2 (sympy)": bool(ok_norm), "draws": n,
           "worst |I - 2r/(1 + r^2)|": s(wI, 3), "worst |r(g S g^T) - r(S)|": s(wr, 3),
           "worst 1 - |<u1(g S g^T), g u1(S)>|": s(wu, 3), "(draw, element) pairs set aside, r > 0.999": aside}
    return res, bool(ok_det and ok_norm and wI < TOL and wr < TOL and wu < TOL)


# ---------------------------------------------------------------- K5

def hand_lead(name):
    conj = name.startswith("conj ")
    base = name[5:] if conj else name
    if base in ("R", "dR"):
        l3, l7 = 9, -3
    else:
        a = int(base[1:])
        l3, l7 = (3 - a, 15 - a) if W146.W143.eps_of(a) == 1 else (15 - a, 3 - a)
        if 3 + 2 * a < min(l3, l7):
            return "e1"
    if conj:
        l3, l7 = l7, l3
    return "l3" if l3 < l7 else "l7"


def K5():
    names = list(W146.RECORD) + ["conj " + n for n in W146.RECORD]
    exact = {"R", "F2", "conj R", "conj F2"}
    rows, ok = {}, True
    for n in names:
        base = n[5:] if n.startswith("conj ") else n
        rs, u8 = {}, None
        for y in (4, 5, 6, 7, 8):
            v = W146.record_form(base, mp.mpc(0, y))
            if n.startswith("conj "):
                v = W146.conj(v)
            r, u = takagi(S_of(W146.lines(v)))
            rs[y] = r
            if y == 8:
                u8 = u
        lead = hand_lead(n)
        row = {"lead (hand)": lead, "r at y = 4, 6, 8": [s(rs[y], 4) for y in (4, 6, 8)]}
        if n in exact:
            good = all(rs[y] < TOL for y in rs)
        elif lead == "e1":
            good = 1 - rs[8] < mp.mpf("1e-3")
            row["1 - r at y = 8"] = s(1 - rs[8], 3)
        else:
            slope = (mp.log(rs[8]) - mp.log(rs[4])) / 4
            st = [1, 0] if lead == "l3" else [0, 1]
            dev = 1 - overlap(u8, [mp.mpc(x) for x in st])
            row["(ln r(8) - ln r(4))/4 + pi"] = s(slope + PI, 3)
            row["1 - |<u1, s>| at y = 8"] = s(dev, 3)
            good = abs(slope + PI) < mp.mpf("1e-3") and dev < mp.mpf("1e-6")
        row["holds"] = bool(good)
        ok = ok and good
        rows[n] = row
    return {"objects": rows}, bool(ok)


# ---------------------------------------------------------------- R

def readouts():
    root = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=HERE, capture_output=True, text=True,
                               check=True).stdout.strip())
    raw = subprocess.run(["git", "show", "%s:%s" % (W146.REV_MAIN, W146.TARGET)], cwd=root, capture_output=True,
                         check=True).stdout
    sha = hashlib.sha256(raw).hexdigest()
    opt = json.loads(raw.decode("utf-8"))["optima"]
    specials = []
    for kind, n, st in special_states():
        specials.append((kind, [str(x) for x in n], [mp.mpc(complex(sp.N(x, 30))) for x in st]))
    rows, L2 = [], []
    for o in opt:
        d, e = mp.mpc(*o["delta"]), mp.mpc(*o["epsilon"])
        r, u = takagi(S_of([d / SQ2, mp.mpc(1), e]))
        ang = 2 * mp.acos(min(abs(u[0]), mp.mpf(1))) * 180 / PI
        best = max(specials, key=lambda t: overlap(u, t[2]))
        bang = 2 * mp.acos(min(overlap(u, best[2]), mp.mpf(1))) * 180 / PI
        t = mp.mpc(*o["tau"])
        rR, uR = takagi(S_of(W146.lines(W146.R_and_DR(t)[0])))
        stabR = max((sp_ for sp_ in specials if sp_[0] == "stabilizer"), key=lambda q: overlap(uR, q[2]))
        angR = 2 * mp.acos(min(overlap(uR, stabR[2]), mp.mpf(1))) * 180 / PI
        rows.append({"hor": o["hor"], "tau": o["tau"], "r": s(r, 5), "I from r": s(2 * r / (1 + r * r), 5),
                     "I recorded": o["|h.h|/|h|^2"], "Bloch angle from (1, 0), degrees": s(ang, 5),
                     "nearest special state": [best[0], best[1]], "its angle, degrees": s(bang, 5),
                     "R's angle from its nearest stabilizer state, degrees": s(angR, 5),
                     "R's nearest stabilizer state": stabR[1]})
        if o["hor"].replace("_", "").replace("₂", "2").upper() == "L2":
            L2.append((float(o["tau"][1]), float(mp.log(r)), float(ang)))
    ys = [q[0] for q in L2]
    return {"target sha256 as pinned": sha == W146.TARGET_SHA, "rows": rows,
            "L2 slope of ln r": round(float(np.polyfit(ys, [q[1] for q in L2], 1)[0]), 4),
            "L2 slope of the angle, degrees per unit Im tau": round(float(np.polyfit(ys, [q[2] for q in L2], 1)[0]), 4)}


def main():
    rng = np.random.default_rng(152)
    out = {"arc": "W152", "rule": "W152_RULE.md", "status": "one run", "python": sys.version.split()[0],
           "dps": mp.mp.dps}
    ts = taus(rng)
    out["K1"], ok1 = K1(ts)
    out["K2"], ok2, grp = K2(ts)
    out["K3"], ok3 = K3(grp)
    out["K4"], ok4 = K4(rng, grp)
    out["K5"], ok5 = K5()
    out["R"] = readouts()
    out["cells"] = {"K1": ok1, "K2": ok2, "K3": ok3, "K4": ok4, "K5": ok5}
    out["every predicted cell holds"] = bool(all(out["cells"].values()))
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every predicted cell holds:", out["every predicted cell holds"])


if __name__ == "__main__":
    main()
