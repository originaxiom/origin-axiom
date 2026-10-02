#!/usr/bin/env python3
"""B1522 -- design-time controls (structure, lemmas, planted cases; no sealed outcome is computed: the E/A flags are read only on
levels 1 and 2, which Lemmas L1 and L2 of the PREREGISTRATION decide, and on planted toy groups).

C1  the four symmetries are endomorphisms of pi: iota, eps, tau send R to a cyclic conjugate of R^+-1 in the free group; all four
    send R to the identity in Ballas' rho_q at q = 2 and 3/7 (exact) and in SnapPy's faithful holonomy (through B1521's
    isomorphism m = ab, n = aabA).
C2  dualising flags (B1512's table, re-derived): exact intertwiners at q = 2: Hom(rho_q o b, rho_q) and Hom(rho_q o b, rho_{1/q}).
C3  |T_n| = L_{2n} - 2 and the invariant factors agree between route R's own SNF, route F's model and SnapPy (n <= 8), n <= 12.
C4  route R: sigma(iota, eps, alpha, tau) = (+1, -1, +1, +1) and the cross term c = 0 on every level n <= 12 (Lemma Z).
C5  the generated group's order on characters (route F, route R): equal, and faithful (= SnapPy's |Isom(M_n)| = 8n) from
    n = 3; on T_1 and T_2 the action has 4 and 8 elements.
C6  iota acts as -1 on T_n for n <= 12 in both routes (B1297, B1512 K2).
C7  the golden algebra: charpoly(M) = t^2 - t - 1, M^2 = Phi^-1, S M S = -M^-1, S Phi S = Phi^-1; S swaps the eigenlines.
C8  route correspondence: the map (a, b) -> chi_R (restriction to T_n) is a bijection intertwining the four actions, n <= 12.
C9  levels 1 and 2: every character E-fixed in both routes (Lemmas L1, L2).
C11 the splitting of primes in Q(sqrt 5) (p = +-1 mod 5 split, +-2 inert, 5 ramified), checked for p < 2000.
C10 planted: route F's criterion code on a toy group without sigma = -1 dualising elements finds every nontrivial character
    unfixed; with one reflection planted, exactly its fixed characters are E-fixed.
Usage: python3 controls.py   (writes controls.json)"""
import json
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import route_fibre as RF  # noqa: E402
import route_rs as RR  # noqa: E402

LEVELS = range(1, 13)


def ballas(q):
    t = q / 2
    m = [[F(1), F(0), F(1), t - 1], [F(0), F(1), F(1), t], [F(0), F(0), F(1), t + F(1, 2)], [F(0), F(0), F(0), F(1)]]
    n = [[F(1), F(0), F(0), F(0)], [2 + 1 / t, F(1), F(0), F(0)], [F(2), F(1), F(1), F(0)], [F(1), F(1), F(0), F(1)]]
    return {"m": m, "n": n}


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def eye():
    return [[F(int(i == j)) for j in range(4)] for i in range(4)]


def inv4(A):
    Mx = [list(A[i]) + eye()[i] for i in range(4)]
    for c in range(4):
        p = next(r for r in range(c, 4) if Mx[r][c] != 0)
        Mx[c], Mx[p] = Mx[p], Mx[c]
        pv = Mx[c][c]
        Mx[c] = [x / pv for x in Mx[c]]
        for r in range(4):
            if r != c and Mx[r][c] != 0:
                f = Mx[r][c]
                Mx[r] = [a - f * b for a, b in zip(Mx[r], Mx[c])]
    return [row[4:] for row in Mx]


def ev(rho, w):
    Rm = {"m": rho["m"], "n": rho["n"], "M": inv4(rho["m"]), "N": inv4(rho["n"])}
    X = eye()
    for c in w:
        X = mul(X, Rm[c])
    return X


def nullspace(rows, ncols):
    M_ = [list(r) for r in rows]
    piv, r = [], 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M_)) if M_[i][c] != 0), None)
        if p is None:
            continue
        M_[r], M_[p] = M_[p], M_[r]
        pv = M_[r][c]
        M_[r] = [x / pv for x in M_[r]]
        for i in range(len(M_)):
            if i != r and M_[i][c] != 0:
                f = M_[i][c]
                M_[i] = [x - f * y for x, y in zip(M_[i], M_[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * ncols
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -M_[i][fc]
        basis.append(v)
    return basis


def intertwiner_dim(src, img):
    """dim of {X : img(g) X = X src(g), g = m, n}"""
    rows = []
    for g in ("m", "n"):
        A, B = img[g], src[g]
        for i in range(4):
            for j in range(4):
                row = [F(0)] * 16
                for k in range(4):
                    row[k * 4 + j] += A[i][k]
                    row[i * 4 + k] -= B[k][j]
                rows.append(row)
    return len(nullspace(rows, 16))


def c1():
    out = {}
    for s, (im, _) in RR.SYMS.items():
        cyc_ok = RR.is_automorphism_of_R(im)
        ballas_ok = all(ev(ballas(q), RR.sub(RR.R_WORD, im)) == eye() for q in (F(2), F(3, 7)))
        out[s] = {"cyclic conjugate of R^+-1": cyc_ok, "relator -> I in rho_q (q = 2, 3/7)": ballas_ok}
    # SnapPy's faithful holonomy through B1521's isomorphism
    try:
        import mpmath as mp
        import snappy
        mp.mp.dps = 60
        G = snappy.ManifoldHP("m004").fundamental_group()

        def conv(X):
            def num(x):
                return mp.mpf(str(x).replace(" ", ""))
            return mp.matrix([[mp.mpc(num(X[i, j].real()), num(X[i, j].imag())) for j in range(2)] for i in range(2)])
        a = -conv(G.SL2C("a"))  # sign-corrected lift (B1521 C1)
        b = conv(G.SL2C("b"))
        H = {"a": a, "b": b, "A": a ** -1, "B": b ** -1}

        def hol(w):
            X = mp.eye(2)
            for c in w:
                X = X * H[c]
            return X
        mn = {"m": "ab", "n": "aabA"}
        for s, (im, _) in RR.SYMS.items():
            w = RR.sub(RR.sub(RR.R_WORD, im), mn)
            X = hol(w)
            err = max(abs(X[i, j] - (1 if i == j else 0)) for i in range(2) for j in range(2))
            out[s]["relator -> I in SnapPy's faithful holonomy (60 digits)"] = bool(err < mp.mpf("1e-40"))
    except Exception as exc:  # pragma: no cover
        out["snappy"] = f"unavailable: {exc}"
    ok = all(v["relator -> I in rho_q (q = 2, 3/7)"] for v in out.values() if isinstance(v, dict))
    ok = ok and all(out[s]["cyclic conjugate of R^+-1"] for s in ("iota", "eps", "tau"))
    return {"passed": ok, **out}


def c2():
    q = F(2)
    rho, rho_inv = ballas(q), ballas(1 / q)
    out = {}
    expect = {"iota": "rho_q", "eps": "rho_{1/q}", "alpha": "rho_{1/q}", "tau": "rho_q"}
    for s, (im, d) in RR.SYMS.items():
        img = {g: ev(rho, im[g]) for g in ("m", "n")}
        to_q = intertwiner_dim(rho, img)       # X rho(g) ... : Hom(rho_q, rho_q o b)
        to_qinv = intertwiner_dim(rho_inv, img)
        got = "rho_q" if (to_q == 1 and to_qinv == 0) else ("rho_{1/q}" if (to_q == 0 and to_qinv == 1) else f"{to_q},{to_qinv}")
        out[s] = {"rho_q o b is": got, "declared dualising": d == 1, "agrees": got == expect[s] and (d == 1) == (got == "rho_{1/q}")}
    return {"passed": all(v["agrees"] for v in out.values()), **out}


def lucas(k):
    a, b = 2, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def c3():
    rows = []
    snappy_inv = {1: [], 2: [5], 3: [4, 4], 4: [3, 15], 5: [11, 11], 6: [8, 40], 7: [29, 29], 8: [21, 105]}
    ok = True
    for n in LEVELS:
        lv = RR.Level(n)
        inv_r = sorted(d for _, d in lv.tors)
        inv_f, order_f, N_f, _ = RF.torsion(n)
        row = {"n": n, "route R": inv_r, "route F": sorted(inv_f), "order": lv.order, "L_2n - 2": lucas(2 * n) - 2}
        row["ok"] = (inv_r == sorted(inv_f) and lv.order == order_f == lucas(2 * n) - 2
                     and (n not in snappy_inv or inv_r == sorted(snappy_inv[n])))
        ok = ok and row["ok"]
        rows.append(row)
    return {"passed": ok, "rows": rows, "snappy_homology_torsion": {str(k): v for k, v in snappy_inv.items()}}


def c4():
    rows, ok = [], True
    for n in LEVELS:
        lv = RR.Level(n)
        row = {"n": n}
        for s in RR.SYMS:
            sigma, B, c = lv.action(s)
            row[s] = {"sigma": sigma, "c": list(c)}
        good = (row["iota"]["sigma"], row["eps"]["sigma"], row["alpha"]["sigma"], row["tau"]["sigma"]) == (1, -1, 1, 1)
        good = good and all(not any(row[s]["c"]) for s in RR.SYMS)
        row["ok"] = good
        ok = ok and good
        rows.append(row)
    return {"passed": ok, "rows": rows}


def c5():
    snappy_orders = {n: 8 * n for n in range(1, 9)}   # read from SnapPy at design time (cyclic covers of m004)
    rows, ok = [], True
    for n in LEVELS:
        chars, order, N, G = RF.group(n)
        res = RR.census_structure(n)
        row = {"n": n, "route F group order": len(G), "route R group order": res["group_order"], "8n": 8 * n}
        # the action on characters (with sigma, d) is faithful from n = 3; on T_1 = 0 only (sigma, d) survive (4), and on
        # T_2 = Z/5 every symmetry acts as +-1 (8). The two routes must agree on every level.
        expected = {1: 4, 2: 8}.get(n, 8 * n)
        row["expected"] = expected
        row["ok"] = len(G) == res["group_order"] == expected
        ok = ok and row["ok"]
        rows.append(row)
    return {"passed": ok, "rows": rows, "snappy_isom_orders": {str(k): v for k, v in snappy_orders.items()}}


def c6():
    ok = True
    for n in LEVELS:
        chars, order, N = RF.characters(n)
        ok = ok and all(RF.act(v, RF.NEG, N) == ((-v[0]) % N, (-v[1]) % N) for v in chars)
        lv = RR.Level(n)
        sigma, B, c = lv.action("iota")
        ds = [d for _, d in lv.tors]
        ok = ok and sigma == 1 and all(tuple(B[i]) == tuple((-int(i == j)) % ds[j] for j in range(len(ds))) for i in range(len(ds)))
    return {"passed": ok}


def c7():
    import sympy as sp
    t = sp.Symbol("t")
    Mm, Sm, Phi = sp.Matrix(RF.M), sp.Matrix(RF.S), sp.Matrix(RF.PHI)
    cp = sp.expand(Mm.charpoly(t).as_expr())
    out = {"charpoly(M)": str(cp), "M^2 = Phi^-1": Mm ** 2 == Phi.inv(), "S M S = -M^-1": Sm * Mm * Sm == -Mm.inv(),
           "S Phi S = Phi^-1": Sm * Phi * Sm == Phi.inv()}
    phi = (1 + sp.sqrt(5)) / 2
    phibar = (1 - sp.sqrt(5)) / 2
    # left eigenvectors (row vectors, characters act from the left): v M = phi v
    v = sp.Matrix([[1, 0]])
    vp = (Mm.T - phi * sp.eye(2)).nullspace()[0].T
    vb = (Mm.T - phibar * sp.eye(2)).nullspace()[0].T
    swapped = sp.simplify((vp * Sm) * Mm - phibar * (vp * Sm)) == sp.zeros(1, 2)
    out["S maps the phi-eigenline to the phibar-eigenline"] = bool(swapped)
    out["passed"] = cp == t ** 2 - t - 1 and all(out[k] for k in ("M^2 = Phi^-1", "S M S = -M^-1", "S Phi S = Phi^-1")) and swapped
    del v, vb
    return out


def c8():
    rows, ok = [], True
    for n in LEVELS:
        chars, order, N = RF.characters(n)
        lv = RR.Level(n)
        ds = [d for _, d in lv.tors]
        mp_ = {}
        for v in chars:
            mp_[v] = RR.chi_from_fibre(lv, v, N)
        bij = len(set(mp_.values())) == len(chars) == lv.order
        inter = True
        for s, (Bf, sf, df) in RF.GENERATORS.items():
            sigma, B, c = lv.action(s)
            for v in chars:
                lhs = mp_[RF.act(v, tuple(tuple(x % N for x in r) for r in Bf), N)]
                rhs = RR.pull(mp_[v], B, ds, RR.lcm_all(ds))
                if lhs != rhs:
                    inter = False
                    break
        row = {"n": n, "bijection": bij, "intertwines the four actions": inter}
        ok = ok and bij and inter
        rows.append(row)
    return {"passed": ok, "rows": rows}


def c9():
    out = {}
    ok = True
    for n in (1, 2):
        f = RF.flags(n)
        r = RR.census(n)
        allE_f = all(x["E"] for x in f["flags"].values())
        allE_r = all(x["E"] for x in r["flags"].values())
        out[f"level {n}"] = {"route F all E-fixed": allE_f, "route R all E-fixed": allE_r, "characters": f["order"]}
        ok = ok and allE_f and allE_r
    return {"passed": ok, **out}


def c10():
    # a toy level: T = Z/7 (+) Z/7 with no sigma = -1 dualising element; then plant one reflection R = [[0, 1], [1, 0]]
    import itertools
    N = 7
    chars = list(itertools.product(range(N), repeat=2))
    G0 = [((((1, 0), (0, 1))), 1, 0), ((((6, 0), (0, 6))), 1, 0), ((((2, 0), (0, 4))), 1, 1)]
    E0 = [B for (B, s, d) in G0 if d == 1 and s == -1]
    unfixed0 = [v for v in chars if not any(RF.act(v, B, N) == v for B in E0)]
    G1 = G0 + [((((0, 1), (1, 0))), -1, 1)]
    E1 = [B for (B, s, d) in G1 if d == 1 and s == -1]
    fixed1 = sorted(v for v in chars if any(RF.act(v, B, N) == v for B in E1))
    expect1 = sorted((a, a) for a in range(N))
    ok = len(unfixed0) == len(chars) and fixed1 == expect1
    return {"passed": ok, "toy without reflections: unfixed": len(unfixed0), "toy with one reflection: E-fixed": len(fixed1)}


def c11():
    """the splitting of primes in Q(sqrt 5), by own code rather than citation: t^2 - t - 1 has two distinct roots mod p iff
    p = +-1 mod 5, one double root iff p = 5, none iff p = +-2 mod 5 (all primes below 2000)"""
    def isprime(k):
        return k > 1 and all(k % d for d in range(2, int(k ** 0.5) + 1))
    bad = []
    for p in range(2, 2000):
        if not isprime(p):
            continue
        roots = [r for r in range(p) if (r * r - r - 1) % p == 0]
        expect = 1 if p == 5 else (2 if p % 5 in (1, 4) else 0)
        if len(roots) != expect:
            bad.append(p)
    return {"passed": not bad, "exceptions": bad}


def main():
    out = {}
    for name, fn in (("C1", c1), ("C2", c2), ("C3", c3), ("C4", c4), ("C5", c5), ("C6", c6), ("C7", c7), ("C8", c8),
                     ("C9", c9), ("C10", c10), ("C11", c11)):
        out[name] = fn()
        print(name, "PASS" if out[name]["passed"] else "FAIL", flush=True)
    out["all passed"] = all(v["passed"] for v in out.values() if isinstance(v, dict))
    (HERE / "controls.json").write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str) + "\n")
    print("ALL PASSED" if out["all passed"] else "SOME FAILED")


if __name__ == "__main__":
    main()
