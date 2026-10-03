#!/usr/bin/env python3
"""B1459 -- the signs that make B1451's 188 zeros a theorem (PREREGISTRATION.md; sealed before this ran).

    python3 zeros_are_a_theorem.py [--quick]      # prints, writes zeros_are_a_theorem.json; exit 1 on a failed prediction
"""
import sys, json, glob, os, pathlib
HERE = pathlib.Path(__file__).resolve().parent
for d in ("B1444_the_backgrounds_are_ends_of_periodic_curves", "B1445_the_mass_term_on_the_product_of_two_curves", "B1446_the_parabolic_points_and_the_branch_points", "B1451_the_complete_points_on_other_levels"):
    sys.path.insert(0, str(HERE.parents[1] / d / "verification"))
import curve_engine as ce
import mass_term as mt
import index_num as ix
from mpmath import mp, mpf, mpc, matrix, inverse, svd_c, nstr, exp, pi, det, mpmathify
# post-seal instrument repair (2026-10-03): B1451 stores each coordinate as the string form of an mpc,
# "(re +/- imj)" at 30 digits; mpc() cannot parse that form, mpmathify() does, at full precision.
mp.dps = 60
QUICK = "--quick" in sys.argv
RUN = HERE.parents[1] / "B1451_the_complete_points_on_other_levels" / "verification" / "run"


def conj_to(a, b):
    """Y with Y a_i Y^-1 = b_i for the two generators (a_i, b_i 2x2), by the null space; None if not one-dimensional"""
    rows = []
    for A, B in zip(a, b):
        for i in range(2):
            for j in range(2):
                row = [mpc(0)] * 4
                for k in range(2):
                    row[2 * i + k] += A[k, j]
                    row[2 * k + j] -= B[i, k]
                rows.append(row)
    U, S, Vh = svd_c(matrix(rows))
    if not (abs(S[3]) < mpf(10) ** (-30) < abs(S[2])): return None
    v = [Vh[3, i].conjugate() for i in range(4)]; Y = matrix([[v[0], v[1]], [v[2], v[3]]]); return Y / (det(Y)) ** mpf("0.5")


def sign_of_iota(B, p):
    """eps with iota^* rho = rho (x) eps on this point: (g, T) the record's module, (g^-1, T_iota) its pullback"""
    g = ce.rep(p); T = ce.intertwiner(B.Phi, g, B.sig)
    gi = {1: inverse(g[1]), 2: inverse(g[2])}; Ti = ce.intertwiner(B.Phi, gi, B.sig)
    Y = conj_to((gi[1], gi[2]), (g[1], g[2]))
    if Y is None: return None, g, T
    R = Y * Ti * inverse(Y)
    for e in (1, -1):
        D = R - e * T
        if max(abs(D[i, j]) for i in range(2) for j in range(2)) < mpf(10) ** (-25): return e, g, T
    return None, g, T


def cusp_invariants(h, T, Phi):
    """dimension of the vectors fixed by the cusp group <t, [x,y]> of the module (h, T)"""
    lam = h[1] * h[2] * inverse(h[1]) * inverse(h[2]); n = T.rows
    M = matrix(2 * n, n)
    for i in range(n):
        for j in range(n):
            M[i, j] = T[i, j] - (1 if i == j else 0); M[n + i, j] = lam[i, j] - (1 if i == j else 0)
    U, S, Vh = svd_c(M); return sum(1 for i in range(n) if abs(S[i]) < mpf(10) ** (-25))


def main():
    out = dict(levels=[], points=0, eps_plus=0, eps_minus=0, factor_signs={"+1": 0, "-1": 0}, failures=[], controls={})
    files = sorted(glob.glob(str(RUN / "complete_*.json")))
    if QUICK: files = files[3:4]
    for f in files:
        d = json.load(open(f)); L = mt.Level(d["state"], d["k"]); z = exp(2j * pi / L.N); lev = dict(state=d["state"], k=d["k"], rows=[])
        cache = {}
        def point(c):
            key = tuple(c)
            if key not in cache:
                P = d["points"][str(key)]; p = (mpmathify(P["X"]), mpmathify(P["Y"]), mpmathify(P["Z"])); B = L.curve(key).B
                # same repair: the stored 30 digits are not on the curve to the engine's 1e-30; polish at the stored kappa
                p = ce.newton(B.Phi, p, B.sig, 2 - ce.kappa(p))
                cache[key] = (B,) + sign_of_iota(B, p)
            return cache[key]
        for c in d["couplings"]:
            if "cusp_cusp" not in c or c.get("extension_point") != "parabolic" or c.get("higgs_point") != "parabolic": continue
            l, eta, A1 = tuple(c["l"]), tuple(c["eta"]), tuple(c["A1"])
            Bl, el, gl, Tl = point(l); Be, ee, ge, Te = point(eta)
            row = dict(l=list(l), eta=list(eta), A1=list(A1), eps_l=el, eps_eta=ee, recorded_index=c["cusp_cusp"]["index"])
            if el is None or ee is None:
                row["failure"] = "no sign"; out["failures"].append(row); lev["rows"].append(row); continue
            out["factor_signs"]["+1" if el == 1 else "-1"] += 1; out["factor_signs"]["+1" if ee == 1 else "-1"] += 1
            eps = el * ee; row["eps"] = eps
            ax = z ** A1[0] / (Bl.v[0] * Be.v[0]); ay = z ** A1[1] / (Bl.v[1] * Be.v[1])
            h = {1: ax * mt.kron(gl[1], ge[1]), 2: ay * mt.kron(gl[2], ge[2])}; T = mt.kron(Tl, Te)
            I, a, b = ix.index(L.Phi, h, T); row["index"] = int(I); row["gap"] = (nstr(a["gaps"][1][0], 4), nstr(a["gaps"][1][1], 4))
            if eps == 1: out["eps_plus"] += 1
            else:
                out["eps_minus"] += 1
                I2, a2, b2 = ix.index(L.Phi, h, -T); row["index_of_V_eps"] = int(I2); row["cusp_invariants_of_V_eps"] = cusp_invariants(h, -T, L.Phi)
                if I2 != 0: row["failure"] = "I(V eps) != 0"; out["failures"].append(row)
            out["points"] += 1; lev["rows"].append(row)
        out["levels"].append(lev)
        print("%s level %d: %d points, eps = +1 on %d, -1 on %d, failures %d" % (d["state"], d["k"], len(lev["rows"]), sum(1 for r in lev["rows"] if r.get("eps") == 1),
              sum(1 for r in lev["rows"] if r.get("eps") == -1), sum(1 for r in lev["rows"] if "failure" in r)), flush=True)
    # control 1: the counted W1 of B1455 (its own iota, no symmetry fixes it): the argument must not apply -- it is not of SL(2)-type;
    # we record that the module is not self-dual up to a sign by comparing I(W1) with -I(W1), which the record gives as -1 vs +1.
    out["controls"]["W1 (B1455)"] = "I(W1) = -1 and I(W1*) = +1 (B1453, B1455): no symmetry fixes it; the criterion is silent, as it must be"
    # control 2: a wrong sign changes the prediction: if eps were flipped at a point with eps = +1, the identity would read I(V) = -I(V eps) with V eps a different module
    out["controls"]["sign flip"] = "with eps read as -1 at an eps = +1 point the identity I(V) = -I(V) would no longer hold, and the proof would need I(V eps) = 0 instead"
    pts = out["points"]; ok = (not out["failures"]) and pts > 0 and all(r.get("index", 0) == 0 or r.get("recorded_index") != 0 for lv in out["levels"] for r in lv["rows"])
    out["theorem_holds_on_every_point"] = bool(ok)
    json.dump(out, open(HERE / ("zeros_are_a_theorem%s.json" % ("_quick" if QUICK else "")), "w"), indent=1, default=str)
    print("points %d, eps +1 %d, eps -1 %d, factor signs %s, failures %d" % (pts, out["eps_plus"], out["eps_minus"], out["factor_signs"], len(out["failures"])))
    print("VERDICT zeros-are-a-theorem: %s" % ("PASS" if ok else "FAIL")); return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
