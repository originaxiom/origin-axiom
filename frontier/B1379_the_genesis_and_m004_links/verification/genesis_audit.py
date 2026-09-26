#!/usr/bin/env python3
"""B1379 -- THE GENESIS AND m004 LINKS, AUDITED.  An external web seat's genesis architecture (the owner's uploaded
checkpoints of 2026-09-25/26: a "pointed generated state space" with m004 as its ground node, the founding ratio
g = -R L^-1 generating a second ladder whose first cubic-self-hosting member is m010, and a claimed hand-choice-free
coefficient chain g -> m010 -> delta -> unique nonsplit rho -> Sym^3) checked against this record's chain with own
code.  Conventions: the uniqueness theorem's (docs/UNIQUENESS_THEOREM.md) L = [[1,1],[0,1]], R = [[1,0],[1,1]];
SnapPy's once-punctured-torus-bundle names b++w (monodromy +w) and b+-w (monodromy -w).

Sections (each asserts; the run log is genesis_audit_run.txt):
  S1 the ratio ladder, symbolic in n        S2 the ladder's manifolds, SnapPy       S3 m003 and m004: one double cover
  S4 A7 at the unbased level                S5 the m010 coefficient chain           S6 what the puncture fork is
  S7 golden against plastic                 S8 C2's content (the missing lock)      S9 the reachability census
Usage: python3 genesis_audit.py [--no-m010]"""
import sys, os, math, itertools, warnings
warnings.filterwarnings("ignore")
import sympy as sp
import numpy as np
import snappy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "B1374_the_class_index_in_the_sm_frame", "verification"))
from index_lib import GF, Rep, module, index, characters, h1_and_cocycle, reducible_rep, abelian_exponents

L = sp.Matrix([[1, 1], [0, 1]]); R = sp.Matrix([[1, 0], [1, 1]]); I2 = sp.eye(2); P = sp.Matrix([[0, 1], [1, 0]])


def s1_ladder():
    n = sp.symbols("n", integer=True, positive=True)
    g = -R * L.inv()
    Ln = sp.Matrix([[1, n], [0, 1]])
    B = sp.simplify(Ln * g); A = sp.simplify(sp.Matrix([[1, n - 1], [0, 1]]) * R)
    out = {
        "g": g.tolist(), "g^3=I": g ** 3 == I2 and g != I2, "-I=(L^2R^-1)^2": (L ** 2 * R.inv()) ** 2 == -I2,
        "B_n": B.tolist(), "A_n": A.tolist(), "L^-1 B_n L = -A_n": sp.simplify(L.inv() * B * L + A) == sp.zeros(2),
        "det(A_n-I)": sp.factor((A - I2).det()), "det(B_n-I)": sp.factor((B - I2).det()),
        "M_3=L^3g=gR^-3": L ** 3 * g == g * R.inv() ** 3,
        "M_3=g mod 3": (L ** 3 * g).applyfunc(lambda t: t % 3) == g.applyfunc(lambda t: t % 3),
        "rank(g-I) mod 3": sp.Matrix((g - I2).applyfunc(lambda t: t % 3)).rank(iszerofunc=lambda x: x % 3 == 0),
    }
    assert out["g^3=I"] and out["-I=(L^2R^-1)^2"] and out["L^-1 B_n L = -A_n"] and out["M_3=L^3g=gR^-3"]
    assert out["det(A_n-I)"] == 1 - n and out["det(B_n-I)"] == n + 3 and out["M_3=g mod 3"] and out["rank(g-I) mod 3"] == 1
    gate = [(k, abs(k - 1), k + 3) for k in range(2, 8)]
    first_ratio = min(k for k, tA, tB in gate if tB % 3 == 0); first_pos = min(k for k, tA, tB in gate if tA % 3 == 0 and tA)
    assert (first_ratio, first_pos) == (3, 4)
    return out, gate, first_ratio, first_pos


def s2_manifolds():
    rows = []
    for k in (2, 3, 4):
        w = "L" * (k - 1) + "R"
        for sign, tag in (("++", "+"), ("+-", "-")):
            M = snappy.Manifold("b" + sign + w)
            rows.append((k, tag + w, str(M.identify()[0]).split("(")[0], str(M.homology()), float(M.volume())))
    names = {r[1]: r[2] for r in rows}
    assert names == {"+LR": "m004", "-LR": "m003", "+LLR": "m009", "-LLR": "m010", "+LLLR": "m023", "-LLLR": "m022"}, names
    for k in (2, 3, 4):
        v = [r[4] for r in rows if r[0] == k]; assert abs(v[0] - v[1]) < 1e-9          # +w and -w: equal volume
    return rows


def s3_common_cover():
    T = snappy.Manifold("b++LRLR")
    assert str(T.identify()[0]).startswith("m206") and abs(float(T.volume()) - 2 * float(snappy.Manifold("m004").volume())) < 1e-9
    out = {}
    for base in ("m004", "m003"):
        covs = [C for C in snappy.Manifold(base).covers(2) if C.cover_info().get("type") == "cyclic"]
        out[base] = [C.is_isometric_to(T) for C in covs]
        assert out[base] == [True]
    return out


def s4_A7():
    LR, RL = L * R, R * L
    conj = P * LR * P == RL
    same = snappy.Manifold("b++LR").is_isometric_to(snappy.Manifold("b++RL")) and \
        str(snappy.Manifold("b++LR").identify()[0]).startswith("m004")
    tau = sp.symbols("tau")
    def mobius_poly(X):                       # fixed points of tau -> (a tau + b)/(c tau + d): c tau^2 + (d - a) tau - b
        a, b, c, d = X[0, 0], X[0, 1], X[1, 0], X[1, 1]
        return sp.expand(c * tau ** 2 + (d - a) * tau - b)
    pLR, pRL = mobius_poly(LR), mobius_poly(RL)
    assert conj and same and sp.expand(pLR - pRL) != 0
    return conj, same, pLR, pRL


def s5_m010(primes=(601, 1201, 1321)):
    M = snappy.Manifold("m010"); G = M.fundamental_group()
    gens = list(G.generators()); rels = list(G.relators()); mu, lam = G.peripheral_curves()[0]
    N = 6; mu_ab = abelian_exponents(mu, gens); lam_ab = abelian_exponents(lam, gens)
    on = lambda c, e: sum(e[g] * c[g] for g in gens) % N
    results = []
    for p in primes:
        F = GF(p); z = F.root_of_unity(N); chars = characters(F, gens, rels, N)
        o3 = [c for c in chars if all(c[g] % 2 == 0 for g in gens) and any(c[g] for g in gens)]
        o3p = [c for c in o3 if on(c, mu_ab) == 0 and on(c, lam_ab) == 0]
        assert len(o3) == 8 and sorted(tuple(c[g] for g in gens) for c in o3p) == [(2, 0), (4, 0)]
        delta = {"a": 2, "b": 0}
        h1d, ct = h1_and_cocycle(F, gens, rels, mu, lam, {g: pow(z, delta[g], p) for g in gens})
        assert h1d == 1 and ct is not None
        roots = [c for c in chars if all((2 * c[g]) % N == delta[g] for g in gens)]
        proots = [c for c in roots if on(c, mu_ab) == 0 and on(c, lam_ab) == 0]
        ptw = [c for c in chars if on(c, mu_ab) == 0 and on(c, lam_ab) == 0]
        assert len(roots) == 4 and sorted(tuple(c[g] for g in gens) for c in proots) == [(1, 3), (4, 0)] and len(ptw) == 6
        table = {}
        for chi in proots:
            cv = {g: pow(z, chi[g], p) for g in gens}
            rho = reducible_rep(F, gens, cv, ct); rho0 = reducible_rep(F, gens, cv, {g: 0 for g in gens})
            assert Rep(F, gens, rho).check_relators(rels)
            for m in range(5):
                for psi in ptw:
                    pv = {g: pow(z, psi[g], p) for g in gens}
                    V = Rep(F, gens, module(F, gens, rho, m, pv)); assert V.check_relators(rels)
                    I = index(V, rels, mu, lam)[0]
                    I0 = index(Rep(F, gens, module(F, gens, rho0, m, pv)), rels, mu, lam)[0]
                    table[(tuple(chi[g] for g in gens), m, tuple(psi[g] for g in gens))] = (I, I0)
        # the claims
        assert all(I == 0 for (c, m, s), (I, I0) in table.items() if m <= 2)                       # Sym^0..2: silent
        assert all(I0 == 0 for (I, I0) in table.values())                                           # semisimple: silent
        for chi in ((1, 3), (4, 0)):
            fire3 = {s: I for (c, m, s), (I, I0) in table.items() if c == chi and m == 3 and I}
            assert fire3 == {chi: +1, tuple((-x) % N for x in chi): -1}, (chi, fire3)            # chi Sym^3 rho_chi = +1, chi^-1: -1
            fire4 = {s: I for (c, m, s), (I, I0) in table.items() if c == chi and m == 4 and I}
            assert sorted(fire4.values()) == [-1, +1]                                               # Sym^4 fires too
        results.append((p, table))
    return gens, rels, (mu, lam), results


def s6_puncture():
    M = snappy.Manifold("m004"); S = snappy.Manifold("m004"); S.dehn_fill((0, 1))
    assert str(M.homology()) == str(S.homology()) == "Z"
    return str(M.homology()), str(S.homology()), S.solution_type()


def s7_golden_plastic():
    def minroot(k, top):
        best = (9.0, None)
        for ent in itertools.product(range(top + 1), repeat=k * k):
            A = np.array(ent).reshape(k, k)
            if abs(round(np.linalg.det(A))) != 1: continue
            if not (np.linalg.matrix_power(A, k * k) > 0).all(): continue             # primitive
            r = max(abs(np.linalg.eigvals(A)))
            if 1 + 1e-9 < r < best[0] - 1e-12: best = (r, A.tolist())
        return best
    r2, r3 = minroot(2, 2), minroot(3, 1)
    phi = (1 + 5 ** 0.5) / 2
    plastic = float(sp.nsolve(sp.Symbol("x") ** 3 - sp.Symbol("x") - 1, 1.3))
    assert abs(r2[0] - phi) < 1e-12 and abs(r3[0] - plastic) < 1e-9 and r3[0] < r2[0]
    return r2, r3


def s8_c2():
    phi = (1 + sp.sqrt(5)) / 2
    cf = list(itertools.islice(sp.continued_fraction_iterator(phi), 25))
    assert cf == [1] * 25
    def lagrange(alpha, k=40):                     # q^2 |alpha - p/q| over convergents -> 1/Lagrange value
        its = list(itertools.islice(sp.continued_fraction_iterator(alpha), k))
        h, hp, q, qp = 1, 0, 0, 1
        vals = []
        for a in its:
            h, hp = a * h + hp, h; q, qp = a * q + qp, q
            vals.append(float(abs(alpha - sp.Rational(h, q)) * q ** 2))
        return 1 / min(vals[-10:])
    lg = {"phi": lagrange(phi), "sqrt2": lagrange(sp.sqrt(2)), "silver 1+sqrt2": lagrange(1 + sp.sqrt(2)),
          "(1+sqrt13)/2": lagrange((1 + sp.sqrt(13)) / 2), "sqrt3": lagrange(sp.sqrt(3))}
    assert abs(lg["phi"] - 5 ** 0.5) < 1e-3 and all(v > 8 ** 0.5 - 1e-3 for k, v in lg.items() if k != "phi")
    return cf[:8], lg


def s9_reachability():
    src = [1, 2, 4, 6, 12, 18, 34, 58, 106, 186, 350]            # the source's mixed_cyclic_states, lengths 2..12
    mine = []
    for k in range(2, 13):
        seen = set(); mixed = 0; rotate_ok = True
        for w in itertools.product("LR", repeat=k):
            s = "".join(w); c = min(s[i:] + s[:i] for i in range(k))
            if c in seen: continue
            seen.add(c)
            if "L" in c and "R" in c:
                mixed += 1
                rotate_ok &= any((c[i:] + c[:i]).startswith(("LR", "RL")) for i in range(k))
        assert rotate_ok
        mine.append(mixed)
    assert mine == src
    return mine


if __name__ == "__main__":
    out, gate, fr, fp = s1_ladder()
    print("=== S1 the ratio ladder (symbolic in n) ===")
    for k, v in out.items(): print(f"  {k}: {v}")
    print("  cubic gate (n, |det(A_n-I)|, det(B_n-I)):", gate, f"-> ratio side first at n={fr} (m010), positive side at n={fp} (m023)")
    print("=== S2 the ladder's manifolds (SnapPy) ===")
    for r in s2_manifolds(): print(f"  n={r[0]} {r[1]:7s} = {r[2]:5s} H1 {r[3]:12s} vol {r[4]:.10f}")
    print("=== S3 m004 and m003 share one cyclic double cover, b++LRLR = m206 ===")
    print("  ", s3_common_cover())
    conj, same, pLR, pRL = s4_A7()
    print("=== S4 A7 at the unbased level ===")
    print(f"  P LR P = RL: {conj}; b++LR = b++RL = m004: {same}; based Mobius polynomials differ: LR {pLR}, RL {pRL} (B979 stands)")
    if "--no-m010" not in sys.argv:
        print("=== S5 the m010 coefficient chain (three primes) ===")
        gens, rels, (mu, lam), res = s5_m010()
        print(f"  m010: gens {gens} rels {rels} mu {mu} lam {lam}")
        for p, table in res:
            fire = sorted((c, m, s, I) for (c, m, s), (I, I0) in table.items() if I)
            print(f"  p={p}: peripheral-trivial cubic line {{(2,0),(4,0)}}; h1(pi;delta)=1; lifts chi in {{(1,3),(4,0)}}; firing modules (chi, m, psi, I): {fire}")
        print("  Sym^0,1,2 silent under all six twists and both lifts; Sym^3 fires exactly at psi = chi^{+-1} (chi Sym^3 rho_chi = +1 for BOTH lifts);")
        print("  Sym^4 fires too (psi = chi^{+-2}); every semisimplification silent")
    h, hs, st = s6_puncture()
    print("=== S6 the puncture fork: invisible to the torsion-free axiom ===")
    print(f"  H1(m004) = {h}; H1(m004(0,1)) = {hs} (the closed torus bundle, {st})")
    r2, r3 = s7_golden_plastic()
    print("=== S7 golden against plastic ===")
    print(f"  minimal Perron root, primitive unimodular 2x2 (binary): {r2[0]:.12f} at {r2[1]}")
    print(f"  minimal Perron root, primitive unimodular 3x3 (ternary): {r3[0]:.12f} at {r3[1]}  (the plastic number)")
    print("  C1 (Morse-Hedlund: minimal aperiodic complexity p(n) = n+1, so p(1) = 2) forces a binary alphabet: plastic is excluded upstream of C2")
    cf, lg = s8_c2()
    print("=== S8 C2's content ===")
    print(f"  continued fraction of phi: {cf}...; Lagrange values {({k: round(v, 6) for k, v in lg.items()})} (sqrt5 = {5**0.5:.6f}, sqrt8 = {8**0.5:.6f})")
    print("=== S9 the reachability census ===")
    print("  mixed cyclic L/R states, lengths 2..12:", s9_reachability(), "(= the source's table; every one rotates to begin LR or RL)")
    print("DONE")
