#!/usr/bin/env python3
"""W17: THE WEAVE'S FIVE ON THE THREAD ITSELF. The spin doublet extended by the parity triplet at tick 1, with the
determinant condition of F-HE's SU(5)', read with F-HE's pair.

On an odd-trace thread M (tick 1) the common point gives rho_Q: pi_1(M) -> 2T (W3), with t -> g in 2T. The weave's two
basic modules are then irreducible on M:
  - the spin doublet D = rho_Q (the 2 of 2T);
  - the parity triplet P = Ad(rho_Q), the conjugation action on the quaternion units (W4's triplet, the 3 of 2T).
Their sum has the shape of the Standard Model's 5 = (1, 2) + (3, 1). For a rank-five module with trivial determinant
(F-HE reads W as the 5 of SU(5)', W1 in sm:B1509's notation), the twists by a character nu of the base must satisfy
det = nu^(2a + 3b) = 1, and the choice a = 3, b = -2 is the hypercharge ratio of the 5: the doublet carries nu^3 and the
triplet nu^-2. An extension class c in H^1(M; Hom(P nu^-2, D nu^3)) glues them:

    W(nu, c) = [[D nu^3, c P nu^-2], [0, P nu^-2]].

The rule (named before the run): every odd-trace state of GENESIS to length 8 (32: twelve to length 6, twenty of length
8), tick 1; both lifts of t; nu a 24th root of unity at which H^1(M; Hom(P nu^-2, D nu^3)) is non-zero; every basis
class and one generic combination; W and its dual (the other order). sm:B1374's engine reads (I(W), I(Lambda^2 W)) over GF(p), p = 1 mod 24. No dictionary is
claimed: GENESIS FK11 is as it was.

    python3 the_weaves_five_tick1.py   ->  the_weaves_five_tick1.json beside it
"""
import json
import random
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_weave_extension as WE  # noqa: E402
import the_weaves_five as FV  # noqa: E402

IL, LV, CL, CP, W = WE.IL, WE.LV, WE.CL, WE.CP, WE.W


def quat_mat(F, z, q):
    """the 2 x 2 matrix of a quaternion w + x i + y j + v k with i -> diag(i4, -i4), j -> [[0, 1], [-1, 0]],
    k = ij -> [[0, i4], [i4, 0]], over GF(p); the coordinates are in {0, +-1, +-1/2} for 2T"""
    p = F.p
    i4 = pow(z, 6, p)

    def g(c):
        num = round(2 * c)
        assert abs(2 * c - num) < 1e-9
        return num * F.inv(2) % p
    w, x, y, v = (g(c) for c in q)
    return [[(w + x * i4) % p, (y + v * i4) % p], [(-y + v * i4) % p, (w - x * i4) % p]]


def adjoint(q):
    """the 3 x 3 matrix of x -> q x q^-1 on (i, j, k), from the quaternion product; integer for 2T"""
    cols = []
    for e in ((0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)):
        r = CP.qmul(CP.qmul(q, e), CP.qconj(q))
        cols.append([round(r[1]), round(r[2]), round(r[3])])
    return [[cols[j][i] for j in range(3)] for i in range(3)]


class Tick1:
    def __init__(self, sw, F, z):
        sign = 1 if sw[0] == "+" else -1
        self.phi = CP.word_aut(sw[1:], sign)
        u = CL.peripheral_u(self.phi)
        self.gens = ["a", "b", "t"]
        self.rels = ["taT" + LV.inv(W.to_str(self.phi[1])), "tbT" + LV.inv(W.to_str(self.phi[2]))]
        self.mu, self.lam = LV.inv(W.to_str(u)) + "t", "abAB"
        self.F, self.z = F, z
        self.lifts = CP.extend(self.phi)

    def D(self, g, nexp):
        """rho_Q with t -> g, times nu^3 (nu = z^nexp)"""
        F, z = self.F, self.z
        s = pow(z, 3 * nexp % 24, F.p)
        base = {"a": quat_mat(F, z, CP.QI), "b": quat_mat(F, z, CP.QJ), "t": quat_mat(F, z, g)}
        base["t"] = F.scale(s, base["t"])
        return base

    def P(self, g, nexp):
        """Ad(rho_Q) with t -> Ad(g), times nu^-2"""
        F, z = self.F, self.z
        s = pow(z, (-2 * nexp) % 24, F.p)
        m = {"a": adjoint(CP.QI), "b": adjoint(CP.QJ), "t": adjoint(g)}
        out = {k: [[x % F.p for x in row] for row in v] for k, v in m.items()}
        out["t"] = F.scale(s, out["t"])
        return out


def hom_rep(F, gens, Dm, Pm):
    """Hom(P, D) = D (x) P* as 6 x 6 matrices: X -> D(g) X P(g)^-1, on X in 2 x 3 matrices (row-major vec)"""
    out = {}
    for gname in gens:
        Dg, Pi = Dm[gname], F.inverse(Pm[gname])
        M = [[0] * 6 for _ in range(6)]
        for r in range(2):
            for c in range(3):
                col = 3 * r + c
                # image of the unit matrix E_rc: D E_rc P^-1, entry (i, j) = D[i][r] * Pi[c][j]
                for i in range(2):
                    for j in range(3):
                        M[3 * i + j][col] = Dg[i][r] * Pi[c][j] % F.p
        out[gname] = M
    return out


def five(F, gens, Dm, Pm, cvec):
    """W(g) = [[D(g), C(g) P(g)], [0, P(g)]], with C the 2 x 3 cocycle value (left convention, as LV.ext_rep)"""
    out = {}
    for gi, g in enumerate(gens):
        Cg = [[cvec[6 * gi + 3 * i + j] for j in range(3)] for i in range(2)]
        CP_ = F.mul(Cg, Pm[g])
        M = [[0] * 5 for _ in range(5)]
        for i in range(2):
            for j in range(2):
                M[i][j] = Dm[g][i][j]
            for j in range(3):
                M[i][2 + j] = CP_[i][j]
        for i in range(3):
            for j in range(3):
                M[2 + i][2 + j] = Pm[g][i][j]
        out[g] = M
    return out


def run(states=WE.STATES, seed=13):
    rng = random.Random(seed)
    p = LV.primes_for(24, k=1, start=20000)[0]
    F = IL.GF(p)
    z = F.root_of_unity(24)
    res, summary = {"prime": p}, {}
    for sw in states:
        t0 = time.time()
        S = Tick1(sw, F, z)
        rows = []
        for li, g in enumerate(S.lifts):
            for nexp in range(24):
                Dm, Pm = S.D(g, nexp), S.P(g, nexp)
                assert IL.Rep(F, S.gens, Dm).check_relators(S.rels) and IL.Rep(F, S.gens, Pm).check_relators(S.rels)
                H = IL.Rep(F, S.gens, hom_rep(F, S.gens, Dm, Pm))
                assert H.check_relators(S.rels)
                Sx = WE.Tick3.__new__(WE.Tick3)
                Sx.F, Sx.gens, Sx.rels = F, S.gens, S.rels
                basis = WE.Tick3.h1_basis(Sx, H)
                if not basis:
                    continue
                choices = [("basis", i, v) for i, v in enumerate(basis)]
                if len(basis) > 1:
                    coef = [rng.randrange(1, p) for _ in basis]
                    choices.append(("generic", -1, [sum(c * v[j] for c, v in zip(coef, basis)) % p
                                                    for j in range(len(basis[0]))]))
                for kind, idx, cvec in choices:
                    mats = five(F, S.gens, Dm, Pm, cvec)
                    Wr = IL.Rep(F, S.gens, mats)
                    assert Wr.check_relators(S.rels)
                    I1 = IL.index(Wr, S.rels, S.mu, S.lam)[0]
                    L2 = IL.Rep(F, S.gens, {g_: FV.wedge2(F, mats[g_]) for g_ in S.gens})
                    I2 = IL.index(L2, S.rels, S.mu, S.lam)[0]
                    dual = {g_: F.T(F.inverse(mats[g_])) for g_ in S.gens}
                    J1 = IL.index(IL.Rep(F, S.gens, dual), S.rels, S.mu, S.lam)[0]
                    J2 = IL.index(IL.Rep(F, S.gens, {g_: FV.wedge2(F, dual[g_]) for g_ in S.gens}), S.rels, S.mu,
                                  S.lam)[0]
                    rows.append({"lift": li, "nu (24ths)": nexp, "h1 of the gluing module": len(basis),
                                 "class": kind if kind == "generic" else f"basis {idx}",
                                 "W: (I(W), I(L2 W))": [I1, I2], "W*: (I, I(L2))": [J1, J2]})
        pairs = sorted({tuple(r["W: (I(W), I(L2 W))"]) for r in rows})
        dpairs = sorted({tuple(r["W*: (I, I(L2))"]) for r in rows})
        summary[sw] = {"readings": len(rows), "pairs for W": [list(x) for x in pairs], "pairs for W*": [list(x) for x in dpairs],
                       "nus (24ths)": sorted({r["nu (24ths)"] for r in rows}), "seconds": round(time.time() - t0, 1)}
        res[sw] = rows
        print(sw, json.dumps(summary[sw]), flush=True)
    res["summary"] = summary
    return res


if __name__ == "__main__":
    states = sys.argv[1:]
    if states:                                # a partial run (states named on the command line) writes nothing
        run(states)
        sys.exit(0)
    out = run(WE.STATES + WE.STATES8)
    with open(HERE / "the_weaves_five_tick1.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
