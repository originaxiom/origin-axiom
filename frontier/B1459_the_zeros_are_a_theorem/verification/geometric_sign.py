#!/usr/bin/env python3
"""B1459, post-seal instrument (2026-10-03, written after the sealed run): THE GEOMETRIC SIGN.

The sealed script read eps from Y T_iota Y^-1 = eps T with BOTH T and T_iota trace-normalised by the engine (tr >= 0).
Trace is conjugation-invariant, so that eps is +1 wherever tr T != 0 -- at every parabolic point.  The sealed detector
could not return -1 on its population (the E82 class).  This computes the sign the seal meant:

  iota~ : (x, y, t) -> (x^-1, y^-1, c t)   is an automorphism of pi_1(M) = F x|_Phi <t>   iff   c Phi(iota w) c^-1 = iota(Phi w)
  for w = x, y, with c a WORD of F found by free-group conjugacy (cyclic reduction and rotation).  Then the meridian of
  iota~^* rho is rho(c) T, exactly, and   Y rho(c) T Y^-1 = eps_geo T,   eps_geo = tr(rho(c) T) / tr(T).

For each of the 16 levels: c on the level (one word per level), eps_geo at every point, eps_geo(V) = eps_l eps_eta on
each of the 188 couplings; where eps_geo(V) = -1, I(V (x) eps) with meridian -T and the cusp invariants of V (x) eps
(the twisted branch of the seal's argument, on the points where it is the branch that applies).
Exit 1 if c is not found or not unique on any level, if Y rho(c) T Y^-1 is not +-T at any point, or if a twisted index
is non-zero.
"""
import sys, json, glob, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.argv = [sys.argv[0]]
import zeros_are_a_theorem as Z
from zeros_are_a_theorem import ce, mt, ix, mpmathify, inverse, exp, pi, nstr, mpf

INV = {1: (-1,), 2: (-2,)}
iota = lambda w: ce.subst(w, INV)


def cyc(w):
    """w = a w0 a^-1 with w0 cyclically reduced; returns (a, w0)"""
    w = list(ce.reduce_word(w)); a = []
    while len(w) >= 2 and w[0] == -w[-1]: a.append(w[0]); w = w[1:-1]
    return tuple(a), tuple(w)


def conjugators(u, v, kmax=3):
    """all c with c u c^-1 = v of the form b p^-1 a^-1 u^k, |k| <= kmax (every solution is one of these up to the root's powers)"""
    a, u0 = cyc(u); b, v0 = cyc(v); out = []
    if len(u0) != len(v0): return out
    for r in range(len(u0)):
        if u0[r:] + u0[:r] == v0:
            p = u0[:r]; c0 = ce.reduce_word(b + ce.inv_word(p) + ce.inv_word(a))
            for k in range(-kmax, kmax + 1):
                uk = tuple(u) * k if k >= 0 else ce.inv_word(tuple(u)) * (-k)
                out.append(ce.reduce_word(c0 + uk))
    return sorted(set(out), key=lambda c: (len(c), c))


def word_c(Phi):
    """the unique c with c Phi(iota x) c^-1 = iota(Phi x) and the same for y"""
    ux, vx = ce.inv_word(Phi[1]), iota(Phi[1]); uy, vy = ce.inv_word(Phi[2]), iota(Phi[2])
    cands = [c for c in conjugators(ux, vx) if ce.reduce_word(c + uy + ce.inv_word(c)) == vy]
    return cands


def main():
    out = dict(levels=[], points=0, eps_geo_plus=0, eps_geo_minus=0, factor_signs={"+1": 0, "-1": 0}, twisted=[], failures=[])
    for f in sorted(glob.glob(str(Z.RUN / "complete_*.json"))):
        d = json.load(open(f)); L = mt.Level(d["state"], d["k"]); z = exp(2j * pi / L.N)
        cs = word_c(L.Phi)
        lev = dict(state=d["state"], k=d["k"], c=cs[0] if len(cs) == 1 else cs, rows=[])
        if len(cs) != 1: out["failures"].append(dict(level=lev, failure="c not unique or not found: %d" % len(cs))); out["levels"].append(lev); continue
        c = cs[0]
        # the automorphism check, exactly, on both generators
        assert ce.reduce_word(c + ce.inv_word(L.Phi[1]) + ce.inv_word(c)) == iota(L.Phi[1]) and ce.reduce_word(c + ce.inv_word(L.Phi[2]) + ce.inv_word(c)) == iota(L.Phi[2])
        cache = {}
        def point(key):
            if key not in cache:
                P = d["points"][str(key)]; p = (mpmathify(P["X"]), mpmathify(P["Y"]), mpmathify(P["Z"])); B = L.curve(key).B
                p = ce.newton(B.Phi, p, B.sig, 2 - ce.kappa(p)); g = ce.rep(p); T = ce.intertwiner(B.Phi, g, B.sig)
                gi = {1: inverse(g[1]), 2: inverse(g[2])}; M = ce.wordmat(c, g) * T                 # the meridian of iota~^* rho
                # (gi, M) is a module with the same sign character: check it
                for w, s in ((1, B.sig[0]), (2, B.sig[1])):
                    e = M * gi[w] * inverse(M) - s * ce.wordmat(B.Phi[w], gi); assert max(abs(e[i, j]) for i in range(2) for j in range(2)) < mpf(10) ** (-25), "pullback is not a module"
                Y = Z.conj_to((gi[1], gi[2]), (g[1], g[2])); R = Y * M * inverse(Y)
                e = None
                for s in (1, -1):
                    if max(abs((R - s * T)[i, j]) for i in range(2) for j in range(2)) < mpf(10) ** (-25): e = s
                tr_ratio = ce.tr(M) / ce.tr(T)
                cache[key] = (B, g, T, e, nstr(tr_ratio, 6))
            return cache[key]
        for cp in d["couplings"]:
            if "cusp_cusp" not in cp or cp.get("extension_point") != "parabolic" or cp.get("higgs_point") != "parabolic": continue
            l, eta, A1 = tuple(cp["l"]), tuple(cp["eta"]), tuple(cp["A1"])
            Bl, gl, Tl, el, rl = point(l); Be, ge, Te, ee, re_ = point(eta)
            row = dict(l=list(l), eta=list(eta), A1=list(A1), eps_geo_l=el, eps_geo_eta=ee, trace_ratio_l=rl, trace_ratio_eta=re_)
            if el is None or ee is None: row["failure"] = "Y rho(c) T Y^-1 is not +-T"; out["failures"].append(row); lev["rows"].append(row); continue
            out["factor_signs"]["+1" if el == 1 else "-1"] += 1; out["factor_signs"]["+1" if ee == 1 else "-1"] += 1
            eps = el * ee; row["eps_geo"] = eps; out["points"] += 1
            if eps == 1: out["eps_geo_plus"] += 1
            else:
                out["eps_geo_minus"] += 1
                ax = z ** A1[0] / (Bl.v[0] * Be.v[0]); ay = z ** A1[1] / (Bl.v[1] * Be.v[1])
                h = {1: ax * mt.kron(gl[1], ge[1]), 2: ay * mt.kron(gl[2], ge[2])}; T = mt.kron(Tl, Te)
                I2, a2, b2 = ix.index(L.Phi, h, -T); row["index_of_V_eps"] = int(I2); row["cusp_invariants_of_V_eps"] = Z.cusp_invariants(h, -T, L.Phi)
                row["gap"] = (nstr(a2["gaps"][1][0], 4), nstr(a2["gaps"][1][1], 4)); out["twisted"].append(dict(state=d["state"], k=d["k"], **row))
                if I2 != 0: row["failure"] = "I(V eps) != 0"; out["failures"].append(row)
            lev["rows"].append(row)
        out["levels"].append(lev)
        print("%s level %d: c = %s; %d points, eps_geo = +1 on %d, -1 on %d; factor signs %s" % (d["state"], d["k"], "".join({1: "x", -1: "X", 2: "y", -2: "Y"}[a] for a in c) or "1",
              len(lev["rows"]), sum(1 for r in lev["rows"] if r.get("eps_geo") == 1), sum(1 for r in lev["rows"] if r.get("eps_geo") == -1),
              dict(((s, sum(1 for r in lev["rows"] for kk in ("eps_geo_l", "eps_geo_eta") if r.get(kk) == s)) for s in (1, -1)))), flush=True)
    ok = not out["failures"] and out["points"] == 188
    out["pass"] = bool(ok)
    json.dump(out, open(HERE / "geometric_sign.json", "w"), indent=1, default=str)
    print("points %d, eps_geo +1 %d, -1 %d, factor signs %s, twisted indices %s, failures %d" % (out["points"], out["eps_geo_plus"], out["eps_geo_minus"], out["factor_signs"],
          sorted(set(t["index_of_V_eps"] for t in out["twisted"])), len(out["failures"])))
    print("VERDICT geometric-sign: %s" % ("PASS" if ok else "FAIL")); return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
