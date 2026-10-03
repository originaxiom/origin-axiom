#!/usr/bin/env python3
"""B1459, post-seal control (2026-10-03, written after the run): the eps = -1 branch never fired on the population
(eps = +1 at all 376 factors), so the sealed script never exercised the twisted branch of the argument.  This runs it
on one level anyway, and shows the sign detector's two branches are separated.

On -LLRLR level 1 (12 points), for each coupling V = rho_l (x) rho_eta (x) chi:
  C1  the cusp of V fixes >= 1 vector (t0 > 0: the detector cusp_invariants can return non-zero);
  C2  the cusp of V (x) eps, meridian -T, fixes none;
  C3  I(V (x) eps) = 0 by the index instrument -- the claim the seal made for the branch, computed not cited;
  C4  at each factor, |Y T_iota Y^-1 + T| is of order 1 (the -1 branch of sign_of_iota is far from firing).
Exit 1 if any check fails.
"""
import sys, json, glob, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.argv = [sys.argv[0]]  # keep the main module from reading --quick
import zeros_are_a_theorem as Z
from zeros_are_a_theorem import ce, mt, ix, mpmathify, inverse, exp, pi, nstr, mpf


def main():
    f = sorted(glob.glob(str(Z.RUN / "complete_*.json")))[3]
    d = json.load(open(f)); L = mt.Level(d["state"], d["k"]); z = exp(2j * pi / L.N)
    out = dict(state=d["state"], k=d["k"], rows=[], margins={})
    cache = {}
    def point(c):
        key = tuple(c)
        if key not in cache:
            P = d["points"][str(key)]; p = (mpmathify(P["X"]), mpmathify(P["Y"]), mpmathify(P["Z"])); B = L.curve(key).B
            p = ce.newton(B.Phi, p, B.sig, 2 - ce.kappa(p))
            g = ce.rep(p); T = ce.intertwiner(B.Phi, g, B.sig)
            gi = {1: inverse(g[1]), 2: inverse(g[2])}; Ti = ce.intertwiner(B.Phi, gi, B.sig)
            Y = Z.conj_to((gi[1], gi[2]), (g[1], g[2])); R = Y * Ti * inverse(Y)
            plus = max(abs((R - T)[i, j]) for i in range(2) for j in range(2)); minus = max(abs((R + T)[i, j]) for i in range(2) for j in range(2))
            out["margins"][str(key)] = dict(residual_plus=nstr(plus, 4), residual_minus=nstr(minus, 4))
            cache[key] = (B, g, T, plus, minus)
        return cache[key]
    ok = True
    for c in d["couplings"]:
        if "cusp_cusp" not in c or c.get("extension_point") != "parabolic" or c.get("higgs_point") != "parabolic": continue
        l, eta, A1 = tuple(c["l"]), tuple(c["eta"]), tuple(c["A1"])
        Bl, gl, Tl, pl, ml = point(l); Be, ge, Te, pe, me = point(eta)
        ax = z ** A1[0] / (Bl.v[0] * Be.v[0]); ay = z ** A1[1] / (Bl.v[1] * Be.v[1])
        h = {1: ax * mt.kron(gl[1], ge[1]), 2: ay * mt.kron(gl[2], ge[2])}; T = mt.kron(Tl, Te)
        t0 = Z.cusp_invariants(h, T, L.Phi); t0e = Z.cusp_invariants(h, -T, L.Phi)
        I2, a2, b2 = ix.index(L.Phi, h, -T)
        row = dict(l=list(l), eta=list(eta), A1=list(A1), cusp_invariants_V=t0, cusp_invariants_V_eps=t0e, index_V_eps=int(I2),
                   gap=(nstr(a2["gaps"][1][0], 4), nstr(a2["gaps"][1][1], 4)))
        row["C1"] = t0 >= 1; row["C2"] = t0e == 0; row["C3"] = I2 == 0; row["C4"] = min(ml, me) > mpf("0.5") and max(pl, pe) < mpf(10) ** (-25)
        ok = ok and all(row[k] for k in ("C1", "C2", "C3", "C4")); out["rows"].append(row)
    out["points"] = len(out["rows"]); out["pass"] = bool(ok)
    json.dump(out, open(HERE / "twisted_branch_control.json", "w"), indent=1, default=str)
    print("%s level %d: %d points; C1 %d, C2 %d, C3 %d, C4 %d" % (d["state"], d["k"], len(out["rows"]), *[sum(1 for r in out["rows"] if r[k]) for k in ("C1", "C2", "C3", "C4")]))
    print("sign margins: residual to +T <= %s, residual to -T >= %s" % (
        max(out["margins"].values(), key=lambda m: float(m["residual_plus"]))["residual_plus"], min(out["margins"].values(), key=lambda m: float(m["residual_minus"]))["residual_minus"]))
    print("VERDICT twisted-branch-control: %s" % ("PASS" if ok else "FAIL")); return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
