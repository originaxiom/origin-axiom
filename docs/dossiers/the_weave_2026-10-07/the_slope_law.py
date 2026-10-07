#!/usr/bin/env python3
"""W14 of the weave: the slope law for F-CI's class index, and F-CI's census on every odd-trace state to length six at the
weave's resolving tick.

THE SLOPE LAW (PROVED; checked here against sm:B1506's engine). Let M be a hyperbolic once-punctured-torus bundle with
cusp torus T and peripheral pair (mu, l) = (u^-1 t, [a, b]). Let G be the group of characters of pi_1(M) trivial on T.
  (i)   Every non-trivial chi in G has h^1(M; chi) = 1. Its class c_chi restricts to T with c_chi(l) != 0. Its slope is
        s(chi) = c_chi(mu) / c_chi(l). The fibration class e has e(l) = 0.
  (ii)  For non-trivial lambda, alpha in G with beta = alpha - lambda non-trivial, the doublet V = [[alpha, c_lambda beta],
        [0, beta]] (sm:B1374's F-CI modules) has class index
            I(V) = [s(alpha) = s(lambda)] - [s(beta) = s(lambda)].
  (iii) If lambda, alpha or beta is trivial, I(V) = 0.
Proof.
  (i)   chi is non-trivial on the fibre F (a character trivial on F and on mu is trivial). H^1(F; chi) is one-dimensional
        and restricts isomorphically to the fibre's boundary circle, since H^2(F, dF; chi) = H_0(F; chi) = 0. The
        monodromy commutes with that restriction and acts trivially on the boundary circle's cohomology (chi(mu) = 1). So
        it fixes H^1(F; chi), and the Wang sequence gives h^1(M; chi) = 1 with c_chi(l) != 0.
  (ii)  Use main's B1297 identity: I(V) = h0(V) - h0(V*) + h0(T; V*) - r1(V).
        - h0(V) = h0(V*) = 0.
        - V restricted to T is unipotent and non-split, because c_lambda(l) != 0. So h0(T; V*) = 1.
        - The sequence 0 -> alpha -> V -> beta -> 0 gives h1(V) = 1 + [c_lambda u c_beta = 0] and
          r1(V) = [s(alpha) != s(lambda)] + [c_lambda u c_beta = 0].
        - H^2(M; alpha) -> H^2(T; C) is an isomorphism: both are one-dimensional, and the map is onto since
          H^3(M, dM; alpha) = H_0(M; alpha) = 0. So c_lambda u c_beta = 0 iff c_lambda|T ^ c_beta|T = 0, that is, iff
          s(beta) = s(lambda).
        - Hence I = 1 - [s(alpha) != s(lambda)] - [s(beta) = s(lambda)].
  (iii) lambda = 0: the extension is by e. alpha = 0: the index is [s(e) = s(lambda)] = 0, since e(l) = 0 != c_lambda(l).
        beta = 0: the index is -[c_lambda u e = 0]. Both vanish by sm:B1509's T3, since the monodromy is the identity on
        the one-dimensional H^1(F; .).
Corollary (the signs). (lambda, alpha) -> (-lambda, beta) reverses the index, since s(-chi) = s(chi): the image of
restriction is a Lagrangian line, which equals its annihilator. On backgrounds this is
(lambda, kappa, psi_Y) -> (-lambda, kappa + lambda, psi_Y). So generation-shaped backgrounds pair with opposite signs,
and main's B1434 P6, signs split equally on every level, is a theorem.

THE CENSUS. F-CI's backgrounds (lambda, kappa, psi_Y), with sector characters
alpha_s = s_Y psi_Y + s_g kappa + (1 - s_g)/2 lambda, are found inside G:
  - kappa = alpha_d - 2 psi_Y and 5 psi_Y = alpha_d - alpha_L;
  - psi_Y's value on the base drops out of every alpha_s;
  - "lifted" is lambda in 2G.
A slope is a tuple over three primes above 20 000; two slopes are equal when they agree at every prime. Single small
primes merge slopes by chance on the larger levels; the tuple does not.

What this script does:
  (1) The law against the engine. On +-LR and +-LLLR at tick 3, every candidate module of sm:B1506's census is read.
      Its engine index is compared with the slope law's.
  (2) The census on all twelve odd-trace states of GENESIS to length six at tick 3. Where a state is in main's B1434
      range, its row is compared with B1434's.
  (3) The sign pairing, checked on every class found.
  (4) The weave's three parities. They are one deck orbit, so they lie in one slope class. If that class is exactly the
      three, then for a parity p and any alpha, either alpha and alpha - p are both parities (index 1 - 1 = 0) or
      neither has p's slope (index 0). So no doublet with a parity as its extension character fires. This script
      records, on every state, the size of the parities' class and the number of firing modules with a parity as the
      extension character. The summary key asks for both (a class of exactly three, and no firing), so it is false
      when a class is larger even if nothing fires.

    python3 the_slope_law.py   ->  the_slope_law.json beside it (four processes)
"""
import itertools
import json
import math
import sys
import time
from collections import Counter, defaultdict
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_class_index_orbits as W  # noqa: E402  (sm:B1506's engine carried to any state; B1434's rows)

LV, IL, CL, CP = W.LV, W.IL, W.CL, W.CP
SECTORS = LV.SECTORS
ODD = ["+LR", "-LR", "+LLLR", "-LLLR", "+LLLLLR", "-LLLLLR", "+LLLRLR", "-LLLRLR", "+LLLRRR", "-LLLRRR", "+LLRLRR",
       "-LLRLRR"]


class CuspTrivial:
    """G: the characters of a state's level n trivial on the cusp, as exponent tuples (a, b, t) mod N"""

    def __init__(self, sw, n):
        from sympy import Matrix
        from sympy.matrices.normalforms import smith_normal_decomp
        sign = 1 if sw[0] == "+" else -1
        phi1 = CP.word_aut(sw[1:], sign)
        phin = CL.power(phi1, n)
        u = CL.peripheral_u(phin)
        self.gens = ["a", "b", "t"]
        self.rels = ["taT" + LV.inv(W.to_str(phin[1])), "tbT" + LV.inv(W.to_str(phin[2]))]
        self.mu, self.lam = LV.inv(W.to_str(u)) + "t", "abAB"
        deck = {"a": W.to_str(phi1[1]), "b": W.to_str(phi1[2]), "t": "t"}
        self.D = [[IL.abelian_exponents(deck[g], self.gens)[h] for h in self.gens] for g in self.gens]
        ea = IL.abelian_exponents(W.to_str(phin[1]), ["a", "b"])
        eb = IL.abelian_exponents(W.to_str(phin[2]), ["a", "b"])
        Mx = Matrix.eye(2) - Matrix([[ea["a"], eb["a"]], [ea["b"], eb["b"]]])
        S, U, V = smith_normal_decomp(Mx.T)
        d = [abs(int(S[i, i])) for i in range(2)]
        assert all(d)
        self.tors = sorted(x for x in d if x > 1)
        self.N = math.lcm(12, *d)
        N = self.N
        ue = IL.abelian_exponents(W.to_str(u), ["a", "b"])
        Vl = [[int(V[i, j]) for j in range(2)] for i in range(2)]
        ranges = [[k * (N // math.gcd(d[i], N)) % N for k in range(math.gcd(d[i], N))] for i in range(2)]
        self.chars = []
        for y in itertools.product(*ranges):
            xa = (Vl[0][0] * y[0] + Vl[0][1] * y[1]) % N
            xb = (Vl[1][0] * y[0] + Vl[1][1] * y[1]) % N
            self.chars.append((xa, xb, (xa * ue["a"] + xb * ue["b"]) % N))
        assert len(set(self.chars)) == len(self.chars) == math.prod(d)
        mu_ex = IL.abelian_exponents(self.mu, self.gens)
        for c in self.chars:
            assert sum(mu_ex[g] * x for g, x in zip(self.gens, c)) % N == 0
        self.zero = (0, 0, 0)

    def pull(self, c):
        return tuple(sum(self.D[i][j] * c[j] for j in range(3)) % self.N for i in range(3))

    def add(self, *cs, coeffs=None):
        coeffs = coeffs or [1] * len(cs)
        return tuple(sum(k * c[i] for k, c in zip(coeffs, cs)) % self.N for i in range(3))


def cocycle_value(F, chi_val, coc, word):
    """c(word) for the left cocycle c(gh) = c(g) + chi(g) c(h)"""
    acc, pre = 0, 1
    for ch in word:
        g = ch.lower()
        if ch.islower():
            acc = (acc + pre * coc[g]) % F.p
            pre = pre * chi_val[g] % F.p
        else:
            pre = pre * F.inv(chi_val[g]) % F.p
            acc = (acc - pre * coc[g]) % F.p
    return acc


def slopes(gens, rels, mu, lam, chars, N, nprimes=3, start=20000):
    primes = LV.primes_for(N, k=nprimes, start=start)
    fields = [(IL.GF(p), IL.GF(p).root_of_unity(N)) for p in primes]
    out = {}
    for c in chars:
        if not any(c):
            continue
        sl = []
        for F, z in fields:
            val = {g: pow(z, x, F.p) for g, x in zip(gens, c)}
            h1, coc = IL.h1_and_cocycle(F, gens, rels, mu, lam, val)
            assert h1 == 1 and coc is not None, ("(i): h1 = 1", c, h1)
            cl = cocycle_value(F, val, coc, lam)
            assert cl != 0, ("(i): the class does not vanish on the fibre's boundary", c)
            sl.append(cocycle_value(F, val, coc, mu) * F.inv(cl) % F.p)
        out[c] = tuple(sl)
    return out, primes


def law_index(s, add, zero, lam, a):
    b = add(a, lam, coeffs=[1, -1])
    if lam == zero or a == zero or b == zero:
        return 0
    return int(s[a] == s[lam]) - int(s[b] == s[lam])


def law_check(sw, n=3):
    """every candidate of sm:B1506's census: the engine's index against the slope law's"""
    t0 = time.time()
    P = W.StatePres(sw, n)
    C = LV.Census(P, verbose=False)
    s, primes = slopes(P.gens, P.rels, P.mu, P.lam, list(C.loci), P.N, start=400)    # the engine's own primes
    zero = tuple(0 for _ in P.gens)
    bad = sum(1 for (lam, a), I in C.I.items() if law_index(s, P.add, zero, lam, a) != I)
    return {"state": sw, "candidates": len(C.I), "mismatches": bad, "seconds": round(time.time() - t0, 1)}


def census(sw, n=3):
    t0 = time.time()
    Gr = CuspTrivial(sw, n)
    s, primes = slopes(Gr.gens, Gr.rels, Gr.mu, Gr.lam, Gr.chars, Gr.N)
    zero = Gr.zero
    I = lambda lam, a: law_index(s, Gr.add, zero, lam, a)   # noqa: E731
    fifth, doubles = defaultdict(list), set()
    for c in Gr.chars:
        fifth[Gr.add(c, coeffs=[5])].append(c)
        doubles.add(Gr.add(c, coeffs=[2]))
    classes, firing = {}, 0
    for lam in Gr.chars:
        if lam == zero:
            continue
        fire = {a: v for a in Gr.chars if (v := I(lam, a))}
        firing += len(fire)
        for ad, Id in fire.items():
            for aL, IL_ in fire.items():
                if Id != IL_:
                    continue
                for y in fifth.get(Gr.add(ad, aL, coeffs=[1, -1]), []):
                    kappa = Gr.add(ad, y, coeffs=[1, -2])
                    als = tuple(Gr.add(y, kappa, lam, coeffs=[sy, sg, (1 - sg) // 2]) for (_, sy, sg) in SECTORS)
                    Is = tuple(I(lam, x) for x in als)
                    if all(Is[i] == Is[0] != 0 for i in range(5)):
                        classes[(lam, als)] = Is

    def orbit(key):
        k, cur = 0, key
        while True:
            cur = (Gr.pull(cur[0]), tuple(Gr.pull(x) for x in cur[1]))
            k += 1
            if cur == key:
                return k
    # (3) the sign pairing: (lambda, alphas) -> (-lambda, alphas - lambda) carries a class to a class of opposite sign
    paired = all(classes.get((Gr.add(lam, coeffs=[-1]), tuple(Gr.add(x, lam, coeffs=[1, -1]) for x in als)), (None,))[0]
                 == -Is[0] for (lam, als), Is in classes.items())
    nu = sum(1 for Is in classes.values() if Is[5] == Is[0])
    # the weave's three parities: the order-2 characters of G
    par = [c for c in Gr.chars if c != zero and Gr.add(c, coeffs=[2]) == zero]
    par_class = [c for c in s if s[c] == s[par[0]]] if par else []
    par_fire = sum(1 for lam in par for a in Gr.chars if I(lam, a))
    row = {"state": sw, "tick": n, "|G|": len(Gr.chars), "torsion": Gr.tors, "N": Gr.N, "primes": primes,
           "distinct slopes": len(set(s.values())), "firing": firing, "generation_shaped": len(classes),
           "lifted": sum(1 for (lam, _) in classes if lam in doubles), "nu^c with the generation's sign": nu,
           "orbit sizes": {str(k): v for k, v in sorted(Counter(orbit(k) for k in classes).items())},
           "signs": {str(k): v for k, v in sorted(Counter(Is[0] for Is in classes.values()).items())},
           "every class paired with its opposite": bool(paired),
           "the parities": {"how many": len(par), "their slope class has": len(par_class),
                            "firing modules with a parity as the extension character": par_fire},
           "seconds": round(time.time() - t0, 1)}
    if sw in W.B1434:
        row["B1434"] = list(W.B1434[sw])
        row["agrees with B1434"] = (row["generation_shaped"], row["lifted"], nu) == W.B1434[sw]
    print(json.dumps(row), flush=True)
    return row


if __name__ == "__main__":
    with Pool(4) as pool:
        law = pool.map(law_check, ["+LR", "-LR", "+LLLR", "-LLLR"])
        rows = pool.map(census, ODD)
    res = {"(1) the slope law against sm:B1506's engine": law,
           "(2) the census, every odd-trace state to length 6, tick 3": {r["state"]: r for r in rows},
           "the law held at every candidate": bool(all(x["mismatches"] == 0 for x in law)),
           "every state carries generation-shaped backgrounds": bool(all(r["generation_shaped"] > 0 for r in rows)),
           "every in-range row agrees with B1434": bool(all(r.get("agrees with B1434", True) for r in rows)),
           "(3) every class paired with its opposite": bool(all(r["every class paired with its opposite"] for r in rows)),
           "(4) the parities: one slope class of exactly three, and no firing module on a parity": bool(all(
               r["the parities"]["how many"] == 3 == r["the parities"]["their slope class has"]
               and r["the parities"]["firing modules with a parity as the extension character"] == 0 for r in rows))}
    with open(HERE / "the_slope_law.json", "w") as f:
        json.dump(res, f, indent=1)
    print(json.dumps({k: v for k, v in res.items() if not k.startswith("(2)") and not k.startswith("(1)")}))
