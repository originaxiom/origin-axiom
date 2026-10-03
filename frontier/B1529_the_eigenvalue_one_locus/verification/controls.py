#!/usr/bin/env python3
"""B1529 controls, run BEFORE the seal, on banked data and on theorems only.  They read no eigenvalue multiplicity of Lambda^2
at any base point (P1's outcome), no multiplicity of the four on any state but m004 (banked by sm:B1509), and no index at any
eigenvalue-one crossing (the outcome of P4 and P5).

C1  route T against sm:B1527's Part H (the banked identity): on the ten word states, every torsion character, the five twists of
    the sealed run (lambda_c, 1, 1.7, e^{0.9i}, -1), both modules: h1(V) = g(C; kappa), h1(V*) = g(C'; 1/kappa),
    t0 = g(A; kappa), s0 = g(D; kappa) and I by Lemma F agree with the 3,740 banked Fox rows; route T's hypothesis
    H^0(F; V) = H^0(F; V*) = 0 holds on every row.  Dimensions only.
C2  sm:B1509's polynomial: on +LR (m004) at the trivial character, the four's chi_C is s^4 - 8 s^3 + 14 s^2 - 8 s + 1
    = (s - 1)^2 (s^2 - 6 s + 1) (B1509 wang_monodromy.py (b) at q = 1), with am = 2 and g = 1 at s = 1.
C3  Lemma O: for g in SL(4, C), the eigenvalue-one space of Lambda^2 g never has dimension 1 (random elements with a pair of
    eigenvalues of product one, diagonalizable and with Jordan blocks, and unipotent elements of every Jordan type).
C4  the hypothesis guard: sm:B1527's W1 at q = 17 + 12 sqrt2, mu = -1, transported to +LR (I = -1, banked): H^0(F; W1) = 0 and
    route T's g(C; 1) equals the banked h1(W1) = 1; H^0(F; W1*) != 0, so Lemma F does not apply to W1, and route T says so.
C5  route T at the exported type-one points (sm:B1527 points_for_l242e.json, 60 digits): one point per state, every banked
    X2 row there (same characters, twists and modules): h1, h1*, t0, s0 and I agree.
C6  the positive control for the four's base condition (sm:B1515 §5 (b), (d), banked): on m004's levels M_n = (LR)^n, n = 1..6,
    at the hyperbolic point and lambda = 1, route T's h1 of the twisted four is 1 at every character of M_1..M_5, and on M_6 it
    is 1 at 292 characters, 2 at 24 (all of order 8) and 3 at 4 (all of order 5).  Only the four's h1 is read (no multiplicity).
Writes controls.json and prints the record (controls_run.txt)."""
import json
import sys
import time
import warnings
from fractions import Fraction
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402

import fibre_lib as T  # noqa: E402

mp.mp.dps = 60
FL = T.load_b1527("family_lib")
L = T.load_b1527("cusp_lib")
R = T.load_b1527("run")
B1527 = T.B1527
OUT = {}
FAILED = []
MANIFOLDS = R.MANIFOLDS


def check(name, ok, detail):
    OUT[name] = {"pass": bool(ok), "detail": detail}
    if not ok:
        FAILED.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + json.dumps(detail, default=str)[:600], flush=True)


dual_mats, int_char, kappa_of, hyperbolic_mats, StateModules = T.dual_mats, T.int_char, T.kappa_of, T.hyperbolic_mats, \
    T.StateModules


# ---------------------------------------------------------------------------------------------------------- C2
t0 = time.time()
G, img = FL.word_group("+", "LR")
mats = hyperbolic_mats("+", "LR")
fm = T.FibreModule("+", img, mats, 1)
(TC, slot, cond) = fm.T_C(0, 0)
p = TC.charpoly()
coeffs = [T.mp_of_acb_scalar(c) for c in p.coeffs()]
want = [1, -8, 14, -8, 1]
dev = max(abs(c - w) for c, w in zip(coeffs, want))
am = T.order_at(p, T.acb(1))
g = T.g_at(TC, mp.mpf(1))
check("C2 sm:B1509's polynomial (s-1)^2 (s^2-6s+1) on m004's four", dev < mp.mpf(10) ** -50 and am[0] == 2 and g[0] == 1,
      {"chi_C coefficients (low to high)": [mp.nstr(c, 15) for c in coeffs], "deviation": mp.nstr(dev, 3),
       "am at 1 (order, largest zero, first non-zero)": [am[0], mp.nstr(am[1], 3), mp.nstr(am[2], 3)],
       "g at 1 (g, kept, dropped)": [g[0], mp.nstr(g[1], 3), mp.nstr(g[2], 3)], "slot": slot,
       "seconds": round(time.time() - t0, 1)})

# ---------------------------------------------------------------------------------------------------------- C3
t0 = time.time()


def eig_one_dim(g4):
    W = L.wedge2(g4)
    return 6 - T.rank_mp(W - mp.eye(6), max(mp.mpf(1), mp.mnorm(W, 1)))[0]


def rand_c():
    return mp.mpc(mp.rand() - 0.5, mp.rand() - 0.5) * 2


def rand_conj(J):
    P = mp.matrix([[rand_c() for _ in range(4)] for _ in range(4)])
    return P * J * mp.inverse(P)


cases = []
mp.mp.dps = 60
import random  # noqa: E402
random.seed(29)
mp.rand = lambda: mp.mpf(random.random())
for trial in range(12):
    x, y = rand_c() + 2, rand_c() + 2
    # (x, 1/x, y, 1/y): pairs of product one; Jordan variants
    J = mp.diag([x, 1 / x, y, 1 / y])
    cases.append(("diag x 1/x y 1/y", eig_one_dim(rand_conj(J))))
    J = mp.matrix([[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, y, 0], [0, 0, 0, 1 / y]])
    cases.append(("Jordan(1,2) y 1/y", eig_one_dim(rand_conj(J))))
    J = mp.matrix([[x, 1, 0, 0], [0, x, 0, 0], [0, 0, 1 / x, 1], [0, 0, 0, 1 / x]])
    cases.append(("Jordan(x,2) Jordan(1/x,2)", eig_one_dim(rand_conj(J))))
    J = mp.diag([x, y, 1 / (x * y * y), y])
    cases.append(("generic (no product one)", eig_one_dim(rand_conj(J))))
for part in ([4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]):
    J = mp.eye(4)
    pos = 0
    for blk in part:
        for k in range(blk - 1):
            J[pos + k, pos + k + 1] = 1
        pos += blk
    cases.append(("unipotent " + str(part), eig_one_dim(rand_conj(J))))
dims = sorted(set(c[1] for c in cases))
check("C3 Lemma O: the eigenvalue-one space of Lambda^2 g never has dimension 1", 1 not in dims,
      {"dimensions seen": dims, "cases": len(cases),
       "by kind": {k: sorted(set(c[1] for c in cases if c[0] == k)) for k in sorted(set(c[0] for c in cases))},
       "seconds": round(time.time() - t0, 1)})

# ---------------------------------------------------------------------------------------------------------- C4
t0 = time.time()


def transport(mod):
    m, n = mod.M["m"], mod.M["n"]
    mi, ni = mp.inverse(m), mp.inverse(n)
    return L.Module({"a": n * mi, "b": m * ni * m * n * mi * mi, "t": m})


q = 17 + 12 * mp.sqrt(2)
Bq = L.ballas(q)
A = L.Module({g: -1 * Bq.M[g] for g in ("m", "n")})
z, nz = L.cocycle_generator(L.BALLAS, A)
W1 = transport(L.extension(A, z))
W1m = {g: W1.M[g] for g in "abt"}
fox = L.class_index(G, W1)
fmW = T.FibreModule("+", img, W1m, 1)
fmWd = T.FibreModule("+", img, dual_mats(W1m), 1)
(TCw, slotw, condw) = fmW.T_C(0, 0)
gW = T.g_at(TCw, mp.mpf(1))
f0, f0d = fmW.fibre_invariants(0, 0), fmWd.fibre_invariants(0, 0)
check("C4 hypothesis guard: W1 on +LR", fox["I"] == -1 and f0 == 0 and f0d >= 1 and gW[0] == fox["V"]["h1"] == 1,
      {"Fox I(W1)": fox["I"], "Fox h1(W1)": fox["V"]["h1"], "route T g(C; 1)": gW[0], "H0(F; W1)": f0, "H0(F; W1*)": f0d,
       "Lemma F applies": f0 == 0 and f0d == 0, "seconds": round(time.time() - t0, 1)})

# ---------------------------------------------------------------------------------------------------------- C1
t0 = time.time()
c1 = {"rows": 0, "agree": 0, "hypothesis holds": 0, "disagreements": [], "smallest kept": mp.mpf(1),
      "largest dropped": mp.mpf(0), "smallest slot conditioning": mp.mpf(1)}
for sign, word in MANIFOLDS:
    name = R.name_of(sign, word)
    banked = json.loads((B1527 / ("run_" + name + ".json")).read_text())["H"]["rows"]
    Gm, imgm = FL.word_group(sign, word)
    matsm = hyperbolic_mats(sign, word)
    chars, D = FL.torsion_characters(imgm)
    SM = StateModules(sign, imgm, matsm, D)
    for u in chars:
        i, j = int_char(u, D)
        lc = R.lambda_c(sign, u)
        lams = [("lambda_c", lc)] + [(mp.nstr(x, 6), x) for x in R.EXTRA_LAMBDAS if abs(x - lc) > mp.mpf(10) ** -30]
        for lname, lam in lams:
            kap = kappa_of(sign, i, j, D, lam)
            for mod in ("4", "L2"):
                b = [r for r in banked if r["u"] == [str(u[0]), str(u[1])] and r["lambda"] == lname and r["module"] == mod]
                assert len(b) == 1, (name, u, lname, mod, len(b))
                b = b[0]
                rt = SM.row(mod, i, j, kap)
                want = {"h1": b["V"]["h1"], "h1*": b["V*"]["h1"], "t0": b["V"]["t0"], "s0": b["V*"]["t0"], "I": b["I"]}
                got = {k: rt[k] for k in want}
                c1["rows"] += 1
                if got == want:
                    c1["agree"] += 1
                else:
                    c1["disagreements"].append({"state": sign + word, "u": [str(u[0]), str(u[1])], "lambda": lname,
                                                "module": mod, "route T": got, "banked": want})
                if rt["H0(F; V), H0(F; V*)"] == [0, 0]:
                    c1["hypothesis holds"] += 1
                if rt["kept"] is not None:
                    c1["smallest kept"] = min(c1["smallest kept"], rt["kept"])
                if rt["dropped"] is not None:
                    c1["largest dropped"] = max(c1["largest dropped"], rt["dropped"])
                c1["smallest slot conditioning"] = min(c1["smallest slot conditioning"], rt["slot conditioning"])
    print(f"  C1 {sign}{word}: D = {D}, rows so far {c1['rows']}, agree {c1['agree']}", flush=True)
c1["seconds"] = round(time.time() - t0)
for k in ("smallest kept", "largest dropped", "smallest slot conditioning"):
    c1[k] = mp.nstr(c1[k], 3)
check("C1 route T reproduces sm:B1527's Part H (3,740 rows)",
      c1["rows"] == 3740 and c1["agree"] == c1["rows"] and c1["hypothesis holds"] == c1["rows"], c1)

# ---------------------------------------------------------------------------------------------------------- C5
t0 = time.time()
pts = json.loads((B1527 / "points_for_l242e.json").read_text())["manifolds"]
c5 = {"points": 0, "rows": 0, "agree": 0, "disagreements": [], "smallest kept": mp.mpf(1), "largest dropped": mp.mpf(0)}
for sign, word in MANIFOLDS:
    name = R.name_of(sign, word)
    rec = pts[sign + word]
    P0 = rec["points"][0]
    matsP = {g: mp.matrix([[mp.mpf(x) for x in row] for row in P0["matrices"][g]]) for g in "abt"}
    x2 = json.loads((B1527 / ("x2_" + name + ".json")).read_text())
    match = [p for p in x2["points"] if abs(p["frame alpha0"] - P0["banked alpha (deg)"]) < 1e-6]
    assert len(match) == 1, (name, len(match))
    rows = match[0]["index rows"]
    Gm, imgm = FL.word_group(sign, word)
    chars, D = FL.torsion_characters(imgm)
    SM = StateModules(sign, imgm, matsP, D)
    c5["points"] += 1
    lam_of = {mp.nstr(x, 6): x for x in R.P_LAMBDAS}
    for r in rows:
        u = (Fraction(r["u"][0]), Fraction(r["u"][1]))
        i, j = int_char(u, D)
        lam = lam_of[r["lambda"]]
        rt = SM.row(r["module"], i, j, kappa_of(sign, i, j, D, lam))
        want = {"h1": r["V"]["h1"], "h1*": r["V*"]["h1"], "t0": r["V"]["t0"], "s0": r["V*"]["t0"], "I": r["I"]}
        got = {k: rt[k] for k in want}
        c5["rows"] += 1
        if got == want and rt["H0(F; V), H0(F; V*)"] == [0, 0]:
            c5["agree"] += 1
        else:
            c5["disagreements"].append({"state": sign + word, "row": r["u"] + [r["lambda"], r["module"]], "route T": got,
                                        "banked": want})
        if rt["kept"] is not None:
            c5["smallest kept"] = min(c5["smallest kept"], rt["kept"])
        if rt["dropped"] is not None:
            c5["largest dropped"] = max(c5["largest dropped"], rt["dropped"])
c5["seconds"] = round(time.time() - t0)
c5["smallest kept"], c5["largest dropped"] = mp.nstr(c5["smallest kept"], 3), mp.nstr(c5["largest dropped"], 3)
check("C5 route T at the exported type-one points (X2's rows)", c5["rows"] > 0 and c5["agree"] == c5["rows"], c5)

# ---------------------------------------------------------------------------------------------------------- C6
t0 = time.time()


def order_of(u):
    from math import lcm
    return lcm(u[0].denominator, u[1].denominator)


c6 = {}
for n in range(1, 7):
    w = "LR" * n
    Gn, imgn = FL.word_group("+", w)
    chars, D = FL.torsion_characters(imgn)
    SMn = StateModules("+", imgn, hyperbolic_mats("+", w), D)
    by_h1, orders = {}, {}
    for u in chars:
        i, j = int_char(u, D)
        h1 = SMn.row("4", i, j, mp.mpf(1))["h1"]
        by_h1[h1] = by_h1.get(h1, 0) + 1
        orders.setdefault(h1, set()).add(order_of(u))
    c6["M%d" % n] = {"D": D, "h1 of the four: characters by value": dict(sorted(by_h1.items())),
                     "orders by value": {k: sorted(v) for k, v in sorted(orders.items())}}
ok6 = all(c6["M%d" % n]["h1 of the four: characters by value"] == {1: c6["M%d" % n]["D"]} for n in range(1, 6))
ok6 = ok6 and c6["M6"]["h1 of the four: characters by value"] == {1: 292, 2: 24, 3: 4} \
    and c6["M6"]["orders by value"][2] == [8] and c6["M6"]["orders by value"][3] == [5]
c6["seconds"] = round(time.time() - t0)
check("C6 sm:B1515's interior classes of the four on M6 (positive control)", ok6, c6)

(HERE / "controls.json").write_text(json.dumps({"checks": OUT, "failed": FAILED}, indent=1, default=str))
print("FAILED:", FAILED if FAILED else "none", flush=True)
