#!/usr/bin/env python3
"""W15, part 2: THE WEAVE'S OWN EXTENSIONS. A parity line extended by a twisted spin doublet along a weave class.

The weave's vacuum has two kinds of class at a thread's resolving tick, both defined by the joint action alone:
  - the parity lines (W8): for each non-zero parity p, the character B_p = chi_p (x) beta_p of the tick-3 group, with
    beta_p the value on the stable letter that makes B_p trivial on the cusp. By Lemma V, h^1(B_p) = 1, and its class
    l_p is on the end;
  - the twisted spin doublets (W9, W10): A = rho_Q (x) chi_q (x) kappa, for q zero or a parity, every class interior.
An extension class c in H^1(A (x) B_p^*) gives the rank-three module X = [[A, c B_p], [0, B_p]]. Every ingredient is the
weave's, so X is defined on every odd-trace thread at once.

The prediction (the B1297 identity, on the page): A is acyclic on the cusp (rho_Q([a, b]) = -1), B_p is cusp-trivial
and h^0 vanishes for X and X*, so
    I(X) = h0(T; X*) - r1(X) = 1 - [c u l_p = 0] = [c u l_p != 0],   and I(X*) = -I(X).
A non-zero index on the weave's own modules needs the cup product of a spin class with a parity line.

The census, by rule (named before the run):
  (a) every odd-trace state of GENESIS to length 6 (twelve) at tick 3; every parity p; every q in {0, p1, p2, p3}; every
      kappa in the 24th roots of unity where H^1(A (x) B_p^*) is non-zero; every basis class of that group and one
      generic combination;
  (b) the same on +-LR and +-LLRLRR at two further primes (a guard against an accident mod p);
  (c) every odd-trace state of length 8 (twenty; odd trace forces even length) under the reduced rule q = 0 and kappa a
      fourth root of unity. Nothing is cut by it: at tick 3 rho_Q (x) chi_q is conjugate to rho_Q by a unit quaternion
      (the stable letter acts by a scalar), so the four q give isomorphic modules, which (a) confirms; and by the hand
      theorem the act's eigenvalues at tick 3 are fourth roots of unity.
sm:B1374's engine (index_lib, over GF(p), p = 1 mod 24) reads I(X), with its two identity checks on every reading.

    python3 the_weave_extension.py   ->  the_weave_extension.json beside it
"""
import json
import random
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_class_index_orbits as W  # noqa: E402  (sm:B1506's engine carried to any state)

LV, IL, CL, CP = W.LV, W.IL, W.CL, W.CP
PARITIES = {"p1": (-1, 1), "p2": (1, -1), "p3": (-1, -1)}      # chi(a), chi(b) for (1, 0), (0, 1), (1, 1)
QS = {"0": (1, 1), **PARITIES}
STATES = ["+LR", "-LR", "+LLLR", "-LLLR", "+LLLLLR", "-LLLLLR", "+LLLRLR", "-LLLRLR", "+LLLRRR", "-LLLRRR", "+LLRLRR",
          "-LLRLRR"]
STATES8 = [s + w for w in ["LLLLLLLR", "LLLLLRLR", "LLLLLRRR", "LLLLRLRR", "LLLLRRLR", "LLLRLLRR", "LLLRLRRR", "LLLRRLLR",
                           "LLRLLRLR", "LLRLRLRR"] for s in "+-"]


class Tick3:
    def __init__(self, sw, F, z):
        # the presentation alone (W.StatePres would also list every character of the level, which at length 8 is
        # billions of tuples): <a, b, t | t x t^-1 = phi^3(x)>, the peripheral pair (u^-1 t, [a, b])
        sign = 1 if sw[0] == "+" else -1
        phi3 = CL.power(CP.word_aut(sw[1:], sign), 3)
        u = CL.peripheral_u(phi3)
        self.gens = ["a", "b", "t"]
        self.rels = ["taT" + LV.inv(W.to_str(phi3[1])), "tbT" + LV.inv(W.to_str(phi3[2]))]
        self.mu, self.lam = LV.inv(W.to_str(u)) + "t", "abAB"
        self.F, self.z = F, z
        p = F.p
        i4 = pow(z, 6, p)
        self.Mi = [[i4, 0], [0, p - i4]]
        self.Mj = [[0, 1], [p - 1, 0]]
        self.len_rel = max(len(r) for r in self.rels)

    def char_val(self, chi, beta, word):
        v = 1
        for ch in word:
            g = ch.lower()
            x = {"a": chi[0], "b": chi[1], "t": beta}[g] % self.F.p
            v = v * (x if ch.islower() else self.F.inv(x)) % self.F.p
        return v

    def B(self, par):
        """the parity character made trivial on the cusp: its value on t is chosen so that B(mu) = 1"""
        chi = PARITIES[par]
        # B(mu) for beta = 1, then beta = 1 / that (mu has t-exponent 1)
        base = self.char_val(chi, 1, self.mu)
        beta = self.F.inv(base)
        val = {"a": chi[0] % self.F.p, "b": chi[1] % self.F.p, "t": beta}
        assert self.char_val(chi, beta, self.mu) == 1 and self.char_val(chi, beta, self.lam) == 1
        return val

    def A_mats(self, q, kexp):
        """rho_Q (x) chi_q with t -> z^kexp I"""
        F = self.F
        cq = QS[q]
        k = pow(self.z, kexp % 24, F.p)
        return {"a": F.scale(cq[0] % F.p, self.Mi), "b": F.scale(cq[1] % F.p, self.Mj), "t": [[k, 0], [0, k]]}

    def tensor_scalar(self, mats, val):
        """mats (x) (1/val): the 2 x 2 module times the inverse of a character"""
        F = self.F
        return {g: F.scale(F.inv(val[g]), mats[g]) for g in self.gens}

    def h1_basis(self, rep):
        """a basis of H^1 as cocycles (dicts gen -> vector), complementing the coboundaries"""
        F, gens, d = self.F, self.gens, rep.d
        d1 = F.vstack(*[F.hstack(*[rep.fox(r)[g] for g in gens]) for r in self.rels])
        Z = F.nullspace(d1, len(gens) * d)
        Bcols = [[F.sub(rep.M[g], F.eye(d))[r][i] for g in gens for r in range(d)] for i in range(d)]  # (rho(g) - 1) e_i
        basis, cur = [], [v for v in Bcols if any(v)]
        r0 = F.rank(cur) if cur else 0
        for zv in Z:
            if F.rank(cur + [zv]) > r0:
                cur.append(zv)
                r0 += 1
                basis.append(zv)
        return basis

    def extension(self, A, Bval, cvec):
        F, d = self.F, 2
        out = {}
        for gi, g in enumerate(self.gens):
            c = cvec[gi * d:(gi + 1) * d]
            b = Bval[g]
            out[g] = [[A[g][0][0], A[g][0][1], c[0] * b % F.p],
                      [A[g][1][0], A[g][1][1], c[1] * b % F.p],
                      [0, 0, b]]
        return out


def run(states=STATES, seed=7, start=20000, reduced=False):
    rng = random.Random(seed)
    p = LV.primes_for(24, k=1, start=start)[0]
    F = IL.GF(p)
    z = F.root_of_unity(24)
    res, summary = {"prime": p}, {}
    for sw in states:
        t0 = time.time()
        S = Tick3(sw, F, z)
        rows = []
        for par in PARITIES:
            Bval = S.B(par)
            Brep = IL.Rep(F, S.gens, {g: [[Bval[g]]] for g in S.gens})
            assert Brep.check_relators(S.rels)
            a0, a1, t0_, t1, r1 = IL.cohomology_data(Brep, S.rels, S.mu, S.lam)
            line = {"h1(B_p)": a1, "restricts injectively": r1 == a1}
            for q in (["0"] if reduced else QS):
                for kexp in ((0, 6, 12, 18) if reduced else range(24)):
                    A = S.A_mats(q, kexp)
                    Arep = IL.Rep(F, S.gens, A)
                    if not Arep.check_relators(S.rels):
                        continue
                    H = IL.Rep(F, S.gens, S.tensor_scalar(A, Bval))
                    basis = S.h1_basis(H)
                    if not basis:
                        continue
                    combos = [("basis", i, v) for i, v in enumerate(basis)]
                    if len(basis) > 1:
                        coef = [rng.randrange(1, p) for _ in basis]
                        combos.append(("generic", -1, [sum(c * v[j] for c, v in zip(coef, basis)) % p
                                                       for j in range(len(basis[0]))]))
                    for kind, idx, cvec in combos:
                        X = IL.Rep(F, S.gens, S.extension(A, Bval, cvec))
                        assert X.check_relators(S.rels)
                        I, dX, dXs = IL.index(X, S.rels, S.mu, S.lam)
                        rows.append({"p": par, "q": q, "kappa (24ths)": kexp, "h1(A (x) B*)": len(basis),
                                     "class": kind if kind == "generic" else f"basis {idx}", "I(X)": I,
                                     "data X (h0, h1, h0(T), r1)": list(dX), "data X*": list(dXs)})
            rows.append({"p": par, "the parity line": line})
        firing = [r for r in rows if r.get("I(X)")]
        per_par = {par: sorted({(r["q"], r["kappa (24ths)"], r["I(X)"]) for r in firing if r["p"] == par})
                   for par in PARITIES}
        summary[sw] = {"relator length": S.len_rel, "readings": sum(1 for r in rows if "I(X)" in r),
                       "non-zero": len(firing), "values": sorted({r["I(X)"] for r in firing}),
                       "per parity (q, kappa, I)": {k: [list(x) for x in v] for k, v in per_par.items()},
                       "the three parities alike": len({len(v) for v in per_par.values()}) == 1,
                       "seconds": round(time.time() - t0, 1)}
        res[sw] = rows
        print(sw, json.dumps(summary[sw]), flush=True)
    res["summary"] = summary
    return res


RULE = {"(a)": "every odd-trace state to length 6, tick 3; every p; q in {0, p1, p2, p3}; kappa in mu_24 where "
              "H^1(A (x) B_p^*) != 0; every basis class and one generic combination",
        "(b)": "the same on +-LR and +-LLRLRR at the first primes = 1 mod 24 above 50000 and 90000",
        "(c)": "every odd-trace state of length 8, tick 3; every p; q = 0; kappa a fourth root of unity; every basis class "
               "and one generic combination"}


def _one(job):
    sw, start, reduced = job
    out = run([sw], start=start, reduced=reduced)
    return sw, out["prime"], out[sw], out["summary"][sw]


def merged(pool, jobs):
    res, summary, primes = {}, {}, set()
    for sw, p, rows, summ in pool.map(_one, jobs, chunksize=1):
        res[sw], summary[sw] = rows, summ
        primes.add(p)
    assert len(primes) == 1
    res["prime"], res["summary"] = primes.pop(), summary
    return res


if __name__ == "__main__":
    from multiprocessing import Pool
    if sys.argv[1:]:                          # a partial run (states named on the command line) writes nothing
        run(sys.argv[1:])
        sys.exit(0)
    with Pool(4) as pool:
        out = merged(pool, [(sw, 20000, False) for sw in STATES])
        out["rule"] = RULE
        checks = {}
        for start in (50000, 90000):
            o = merged(pool, [(sw, start, False) for sw in ("+LR", "-LR", "+LLRLRR", "-LLRLRR")])
            checks[str(o["prime"])] = {sw: {"readings": v["readings"], "non-zero": v["non-zero"]}
                                       for sw, v in o["summary"].items()}
        out["(b) two further primes"] = checks
        out["(c) length 8, reduced rule"] = merged(pool, [(sw, 20000, True) for sw in STATES8])
    with open(HERE / "the_weave_extension.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
