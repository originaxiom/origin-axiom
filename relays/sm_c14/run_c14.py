"""SM-C14 -- run as sealed (card relays/cards/SM_C14_m000-in-the-harmonic-and-apex-frames.md).

Parts: C2 (hyperbolic check), C5 (R40 on m010), HE-1 (the vacuum's first-order deformation), HE-2 (F-HE's count at q = 1
on the odd levels), C3/C4 (duality, transfer), plants P1-P3, AP-1 (the associative check), AP-2 (cusp shapes).
Writes c14_results.json.  Data-free: no number here is compared with anything measured."""
import json
import sys
import time
from math import gcd
from pathlib import Path

import c14_lib as L

HERE = Path(__file__).resolve().parent
OUT = {}
T0 = time.time()
NPRIMES = 3
LEVELS_ODD = [1, 3, 5, 7]


def log(*a):
    print(*a, flush=True)


def per(R, lev):
    return L.peripheral(R, lev)


def wrep(F, R, n):
    return R.tensor_char(L.w_char(F, n))


def index_pair(R, lev, F, n):
    """I = n(R) - n(R*), I_w = n(R) - n(R* (x) w); C3 checked on R"""
    a = per(R, lev)
    d = per(R.dual(), lev)
    dw = per(wrep(F, R.dual(), n), lev)
    partner = dw if not lev["orientable"] else d
    c3 = a["r1"] + partner["r1"] == a["h1P"]
    return {"I": a["n"] - d["n"], "I_w": a["n"] - dw["n"], "n": a["n"], "n*": d["n"], "n*w": dw["n"], "C3": c3}


# =========================================================================================== C2: the hyperbolic check
def c2():
    import sympy as sp
    s3 = sp.sqrt(-3)
    z = (1 + s3) / 2
    zb = (1 - s3) / 2
    A = sp.Matrix([[1 + z, 1], [-1, 0]])
    B = sp.Matrix([[zb, -zb], [-zb, 1]])
    M = sp.Matrix([[-zb, 0], [zb, 1]])
    cj = lambda X: X.applyfunc(lambda e: sp.expand(sp.conjugate(e)))
    T2 = (M * cj(M)).applyfunc(sp.expand)
    Ai, Bi = A.inv(), B.inv()
    mu = (Ai * Bi * Ai * T2).applyfunc(sp.simplify)          # level 2's mu = ABAt
    lam = (A * B * Ai * Bi).applyfunc(sp.simplify)
    trm, trl = sp.simplify(mu.trace() / sp.sqrt(mu.det())), sp.simplify(lam.trace())
    comm = sp.simplify((mu * lam - lam * mu).norm()) == 0
    z0 = sp.simplify((lam[0, 0] - lam[1, 1]) / (2 * lam[1, 0]))
    C = sp.Matrix([[0, -1], [1, -z0]])
    def transl(P):
        Q = (C * P * C.inv()).applyfunc(sp.simplify)
        return sp.simplify(Q[0, 1] / Q[0, 0])
    tm, tl = transl(mu / sp.sqrt(mu.det())), transl(lam)
    shape = complex(sp.N(tl / tm))
    import snappy
    s4 = complex(snappy.Manifold("m004").cusp_info()[0]["shape"])
    return {"tr mu (normalised)": str(trm), "tr lam": str(trl), "mu, lam commute": comm,
            "translation ratio lam/mu": [shape.real, shape.imag], "reduced": reduce_shape(shape),
            "SnapPy m004 shape": [s4.real, s4.imag], "SnapPy reduced": reduce_shape(s4),
            "C2 holds": abs(complex(*reduce_shape(shape)) - complex(*reduce_shape(s4))) < 1e-9
            and str(trl) in ("2", "-2")}


def reduce_shape(t):
    t = complex(t)
    if t.imag < 0:
        t = t.conjugate()
    for _ in range(200):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-12:
            t = -1 / t
        else:
            break
    if abs(t.real + 0.5) < 1e-12:
        t = complex(0.5, t.imag)
    return [t.real, t.imag]


# =========================================================================================== C5: R40 on m010
def sym3(Mx, p):
    """Sym^3 of a 2x2 matrix (route T's substitution convention): column k = image of X^(3-k) Y^k"""
    def mul(P, Q):
        out = [0] * (len(P) + len(Q) - 1)
        for i, a in enumerate(P):
            for j, b in enumerate(Q):
                out[i + j] = (out[i + j] + a * b) % p
        return out
    X = [Mx[0][0], Mx[1][0]]          # X -> M00 X + M10 Y   (coefficients by power of Y)
    Y = [Mx[0][1], Mx[1][1]]
    cols = []
    for k in range(4):
        P = [1]
        for _ in range(3 - k):
            P = mul(P, X)
        for _ in range(k):
            P = mul(P, Y)
        cols.append(P)
    return [[cols[c][r] for c in range(4)] for r in range(4)]


def c5():
    out = []
    for p in L.primes_for(12, 2):
        F = L.GF(p, 12)
        inv2 = pow(2, p - 2, p)
        for u in ((1 + F.s3) * inv2 % p, (1 - F.s3) * inv2 % p):
            Am = [[0, 1], [p - 1, 1]]
            Bm = [[0, u * u % p], [u, p - 2]]
            V = {"a": L.mscale(sym3(Am, p), u, p), "b": L.mscale(sym3(Bm, p), p - 1, p)}
            Lv = {"a": u * u % p, "b": 1}
            W = {g: [V[g][i] + [0] for i in range(4)] + [[0] * 4 + [Lv[g]]] for g in "ab"}
            lev = {"rels": ["aabaBaaBab"], "mu": "AbAA", "lam": "babA", "prel": "mlML", "orientable": True}
            Wr = L.Rep(F, W)
            assert Wr.check(lev["rels"])
            L2 = L.rep_apply(Wr, L.wedge2)
            iw = per(Wr, lev)["n"] - per(Wr.dual(), lev)["n"]
            il = per(L2, lev)["n"] - per(L2.dual(), lev)["n"]
            out.append({"p": p, "u": u, "I(W)": iw, "I(L2W)": il})
    return {"rows": out, "C5 holds": all(r["I(W)"] == 1 and r["I(L2W)"] == 1 for r in out)}


# =========================================================================================== HE-1: V9
def he1():
    rows = {}
    for n in [1, 2, 3, 4, 5, 6, 7]:
        lev = L.level(n)
        per_p = []
        for p in L.primes_for(12, NPRIMES):
            F = L.GF(p, 12)
            R = L.rho1(F, n)
            assert R.check(lev["rels"])
            S = L.rep_apply(R, L.sym2)
            C = L.char_rep(F, {"a": 1, "b": 1, "t": 1})
            Sw, Cw = wrep(F, S, n), wrep(F, C, n)
            d = {k: per(m, lev) for k, m in (("S", S), ("C", C), ("Sw", Sw), ("Cw", Cw))}
            row = {"h0(S)": d["S"]["h0"], "h0(Sw)": d["Sw"]["h0"],
                   "h1(V9)": d["S"]["h1"] - d["C"]["h1"], "r1(V9)": d["S"]["r1"] - d["C"]["r1"],
                   "h1(V9 w)": d["Sw"]["h1"] - d["Cw"]["h1"], "r1(V9 w)": d["Sw"]["r1"] - d["Cw"]["r1"],
                   "h1P(V9)": d["S"]["h1P"] - d["C"]["h1P"], "h1P(V9 w)": d["Sw"]["h1P"] - d["Cw"]["h1P"],
                   "h1(C)": d["C"]["h1"], "h1(Cw)": d["Cw"]["h1"]}
            partnerS = d["Sw"] if not lev["orientable"] else d["S"]
            row["C3 (S)"] = d["S"]["r1"] + partnerS["r1"] == d["S"]["h1P"]
            # plants: P2 as sealed (rho_1(t) -> -rho_1(t): S^2 is unchanged) and as intended (V9 twisted by w)
            Rm = L.Rep(F, {"a": R.M["a"], "b": R.M["b"], "t": L.mscale(R.M["t"], p - 1, p)})
            Sm = L.rep_apply(Rm, L.sym2)
            row["P2 sealed form: h1(S^2 of rho_1 w) - h1(C)"] = per(Sm, lev)["h1"] - d["C"]["h1"]
            # P3: the torus formula on this cusp
            t3 = L.peripheral_torus_formula(S, lev)
            t3w = L.peripheral_torus_formula(Sw, lev)
            row["P3 C3 under the torus formula"] = t3["r1"] + (t3w if not lev["orientable"] else t3)["r1"] == t3["h1P"]
            per_p.append(row)
        same = all(r == per_p[0] for r in per_p)
        rows[n] = dict(per_p[0], primes_agree=same)
        log("HE-1 level", n, {k: v for k, v in rows[n].items()})
    # C4 for V9: h1(2n) = h1(n; V9) + h1(n; V9 w)
    rows["C4 (V9)"] = {f"{n}->{2 * n}": rows[2 * n]["h1(V9)"] == rows[n]["h1(V9)"] + rows[n]["h1(V9 w)"] for n in (1, 2, 3)}
    return rows


# =========================================================================================== HE-2: the count at q = 1
def characters(n):
    N = L.torsion_order(n)
    K = L.lcm(max(N, 1), 12)
    lev = L.level(n)
    ex = lambda w, g: w.count(g) - w.count(g.upper())
    out = []
    for i in range(N):
        for j in range(N):
            ka, kb = i * (K // N), j * (K // N)
            if all((ex(r, "a") * ka + ex(r, "b") * kb) % K == 0 for r in lev["rels"]):
                for k in range(12):
                    out.append((i, j, k))
    return N, K, out


def class_trials(cls, p):
    out = [(f"c{k + 1}", c) for k, c in enumerate(cls)]
    if len(cls) >= 2:
        out.append(("c1+c2", {g: [(x + y) % p for x, y in zip(cls[0][g], cls[1][g])] for g in cls[0]}))
        comb = {g: v[:] for g, v in cls[0].items()}
        for k, c in enumerate(cls[1:], start=2):
            comb = {g: [(x + k * y) % p for x, y in zip(comb[g], c[g])] for g in comb}
        out.append(("generic", comb))
    return out


def he2_level(n, p, N, K, chars, plants=False):
    F = L.GF(p, K)
    lev = L.level(n)
    R = L.rho1(F, n)
    w = L.w_char(F, n)
    res = {}
    for (i, j, k) in chars:
        ka, kb, kt = i * (K // N), j * (K // N), k * (K // 12)
        chi = {"a": F.root(ka), "b": F.root(kb), "t": F.root(kt)}
        V = R.tensor_char(chi)
        assert V.check(lev["rels"])
        pv = per(V, lev)
        line = {"a": F.root(-4 * ka), "b": F.root(-4 * kb), "t": F.root(-4 * kt) * w["t"] % p}
        if plants:
            line = {"a": F.root(-4 * ka), "b": F.root(-4 * kb), "t": F.root(-4 * kt)}
        Lrep = L.char_rep(F, line)
        Linv = L.char_rep(F, {g: pow(v, p - 2, p) for g, v in line.items()})
        Veta = V.tensor_char({g: pow(v, p - 2, p) for g, v in line.items()})
        row = {"n(V)": pv["n"], "h1(V)": pv["h1"], "h1(V_eta)": None, "members": {}}
        cls = L.h1_classes(Veta, lev["rels"])
        row["h1(V_eta)"] = len(cls)
        for name, c in class_trials(cls, p):
            W1 = L.ext_with_line(V, c, Lrep)
            assert W1.check(lev["rels"])
            dets = [L.det(W1.M[g], p) for g in W1.gens]
            if plants:
                res[(i, j, k, name)] = {"det W1": dets}
                continue
            assert all(dv == 1 for dv in dets), "C1: det W1"
            row["members"][f"W1 {name}"] = {"W": index_pair(W1, lev, F, n),
                                            "L2W": index_pair(L.rep_apply(W1, L.wedge2), lev, F, n)}
        if plants:
            continue
        clsd = L.h1_classes(Veta.dual(), lev["rels"])
        for name, c in class_trials(clsd, p):
            W2s = L.ext_with_line(V.dual(), c, Linv)
            assert W2s.check(lev["rels"])
            W2 = W2s.dual()
            assert all(L.det(W2.M[g], p) == 1 for g in W2.gens), "C1: det W2"
            row["members"][f"W2 {name}"] = {"W": index_pair(W2, lev, F, n),
                                            "L2W": index_pair(L.rep_apply(W2, L.wedge2), lev, F, n)}
        # C3 on V itself
        partner = per(wrep(F, V.dual(), n), lev) if not lev["orientable"] else per(V.dual(), lev)
        row["C3 (V)"] = pv["r1"] + partner["r1"] == pv["h1P"]
        res[(i, j, k)] = row
    return res


def he2():
    out = {}
    for n in LEVELS_ODD:
        t = time.time()
        N, K, chars = characters(n)
        per_p = []
        for p in L.primes_for(K, NPRIMES):
            per_p.append(he2_level(n, p, N, K, chars))
        same = all(per_p[0] == r for r in per_p[1:])
        base = per_p[0]
        members = {key: r for key, r in base.items() if r["members"]}
        gen_shaped = []
        for key, r in members.items():
            for mname, m in r["members"].items():
                for pair in ("I", "I_w"):
                    if m["W"][pair] == m["L2W"][pair] != 0:
                        gen_shaped.append([list(key), mname, pair, m["W"][pair]])
        summary = {
            "torsion order": N, "K": K, "characters": len(chars), "primes agree": same,
            "n(V) non-zero at": [list(k) for k, r in base.items() if r["n(V)"]],
            "h1(V) non-zero at": [[list(k), r["h1(V)"]] for k, r in base.items() if r["h1(V)"]],
            "members (h1(V_eta) > 0)": len(members),
            "member indices": {str(list(k)): {mn: {"I(W)": m["W"]["I"], "I_w(W)": m["W"]["I_w"],
                                                   "I(L2W)": m["L2W"]["I"], "I_w(L2W)": m["L2W"]["I_w"]}
                                              for mn, m in r["members"].items()} for k, r in members.items()},
            "generation-shaped": gen_shaped,
            "C3 on every module": all(r["C3 (V)"] and all(m["W"]["C3"] and m["L2W"]["C3"] for m in r["members"].values())
                                      for r in base.values()),
            "seconds": round(time.time() - t, 1)}
        out[n] = summary
        log("HE-2 level", n, {k: v for k, v in summary.items() if k != "member indices"})
    return out


def c4():
    """h1(level 2n; pi*V) = h1(n; V) + h1(n; V w), every character of levels 1 and 3"""
    ok, rows = True, 0
    for n in (1, 3):
        N, K, chars = characters(n)
        p = L.primes_for(K, 1)[0]
        F = L.GF(p, K)
        R, R2 = L.rho1(F, n), L.rho1(F, 2 * n)
        lev, lev2 = L.level(n), L.level(2 * n)
        for (i, j, k) in chars:
            ka, kb, kt = i * (K // N), j * (K // N), k * (K // 12)
            chi = {"a": F.root(ka), "b": F.root(kb), "t": F.root(kt)}
            chi2 = {"a": chi["a"], "b": chi["b"], "t": chi["t"] * chi["t"] % p}
            V, V2 = R.tensor_char(chi), R2.tensor_char(chi2)
            assert V2.check(lev2["rels"])
            h = per(V, lev)["h1"] + per(wrep(F, V, n), lev)["h1"]
            ok &= per(V2, lev2)["h1"] == h
            rows += 1
    return {"rows": rows, "C4 holds": ok}


def p1():
    """L = nu^-4 without w: the determinant check must fire at every odd level (on members)"""
    out = {}
    for n in LEVELS_ODD[:3]:
        N, K, chars = characters(n)
        p = L.primes_for(K, 1)[0]
        r = he2_level(n, p, N, K, chars, plants=True)
        fired = [k for k, v in r.items() if any(dv != 1 for dv in v["det W1"])]
        out[n] = {"W1 built": len(r), "det != 1": len(fired)}
    return out


# =========================================================================================== AP-1: associative planes
def ap1():
    import numpy as np
    from scipy.linalg import expm
    terms = [((1, 2, 3), 1), ((1, 4, 5), 1), ((1, 6, 7), 1), ((2, 4, 6), 1), ((2, 5, 7), -1), ((3, 4, 7), -1), ((3, 5, 6), -1)]
    phi = np.zeros((7, 7, 7))
    import itertools
    for (i, j, k), s in terms:
        for perm in itertools.permutations(range(3)):
            idx = [(i, j, k)[q] - 1 for q in perm]
            sign = np.linalg.det(np.eye(3)[list(perm)])
            phi[tuple(idx)] = s * sign
    def act(X):       # X . phi (derivation)
        return (np.einsum("ai,ajk->ijk", X, phi) + np.einsum("aj,iak->ijk", X, phi) + np.einsum("ak,ija->ijk", X, phi))
    basis = []
    for a in range(7):
        for b in range(7):
            E = np.zeros((7, 7)); E[a, b] = 1; basis.append(E)
    def null(Mat):
        _, sv, vt = np.linalg.svd(Mat, full_matrices=True)
        r = int((sv > 1e-10).sum())
        return list(vt[r:])
    Mx = np.array([act(E).ravel() for E in basis]).T
    g2 = [v.reshape(7, 7) for v in null(Mx)]
    dim_g2 = len(g2)
    # the subalgebra fixing e1, e2, e3 pointwise
    A = np.array([np.concatenate([X[:, 0], X[:, 1], X[:, 2]]) for X in g2]).T
    su2 = [sum(c * X for c, X in zip(v, g2)) for v in null(A)]
    rows = []
    for k in range(2, 7):
        X = su2[0]
        ev = np.linalg.eigvals(X)
        th = max(abs(ev.imag))
        gk = expm(X * (2 * np.pi / k) / th)
        gphi = np.einsum("ai,bj,ck,abc->ijk", gk, gk, gk, phi)
        fixed = 7 - np.linalg.matrix_rank(gk - np.eye(7), tol=1e-9)
        rows.append({"k": k, "preserves phi": bool(np.allclose(gphi, phi)), "order k": bool(np.allclose(np.linalg.matrix_power(gk, k), np.eye(7))),
                     "fixed dimension": int(fixed), "phi(e1, e2, e3)": float(phi[0, 1, 2])})
    # the stabiliser of the plane in g2, exponentiated: det on the plane
    A2 = np.array([np.concatenate([X[3:, 0], X[3:, 1], X[3:, 2]]) for X in g2]).T
    stab = [sum(c * X for c, X in zip(v, g2)) for v in null(A2)]
    rng = np.random.default_rng(14)
    dets = []
    for _ in range(200):
        X = sum(rng.normal() * Y for Y in stab)
        g = expm(X)
        dets.append(float(np.linalg.det(g[:3, :3])))
    # a reflection of the plane with any orthogonal map on the normal space: the e123 coefficient flips
    Rf = np.eye(7); Rf[0, 0] = -1
    Bq, _ = np.linalg.qr(rng.normal(size=(4, 4)))
    Rf[3:, 3:] = Bq
    coef = float(np.einsum("ai,bj,ck,abc->ijk", Rf, Rf, Rf, phi)[0, 1, 2])
    return {"dim g2": dim_g2, "dim su(2) fixing the plane": len(su2), "dim stabiliser of the plane": len(stab), "Z_k": rows,
            "det on the plane over 200 stabiliser elements": [min(dets), max(dets)],
            "e123 coefficient after a plane reflection": coef,
            "AP-1 holds": all(r["preserves phi"] and r["fixed dimension"] == 3 and abs(abs(r["phi(e1, e2, e3)"]) - 1) < 1e-12 for r in rows)}


# =========================================================================================== AP-2: cusp shapes
def ap2():
    import snappy
    M = snappy.Manifold("m000")
    vol = float(M.volume())
    out = {"m000 volume": vol, "levels": {}}
    for n in range(1, 9):
        if n == 1:
            covs = [M]
        else:
            covs = M.covers(n, cover_type="cyclic")
        rows = []
        for C in covs:
            info = C.cusp_info()[0]
            sh = info.get("shape") if hasattr(info, "get") else info["shape"]
            t = complex(sh)
            red_ = reduce_shape(t)
            pred = 2 * 3 ** 0.5 / (n if n % 2 else n // 2)
            pred = max(pred, 1 / pred)
            rows.append({"orientable": C.is_orientable(), "volume / vol(m000)": float(C.volume()) / vol,
                         "shape": [t.real, t.imag], "reduced": red_,
                         "rectangular": abs(red_[0]) < 1e-9, "hexagonal": abs(complex(*red_) - complex(0.5, 3 ** 0.5 / 2)) < 1e-9,
                         "modulus as sealed (2 sqrt3 / n at odd n, 2 sqrt3 / (n/2) at even n, or inverse)": pred,
                         "modulus matches": abs(red_[1] - pred) < 1e-9})
        out["levels"][n] = rows
        log("AP-2 level", n, rows)
    return out


if __name__ == "__main__":
    parts = sys.argv[1:] or ["c2", "c5", "he1", "c4", "p1", "he2", "ap1", "ap2"]
    for part in parts:
        t = time.time()
        OUT[part] = globals()[part]()
        log(f"== {part} done in {time.time() - t:.1f} s")
        (HERE / f"c14_{part}.json").write_text(json.dumps(OUT[part], indent=1, default=str))
    if len(parts) == 8:
        (HERE / "c14_results.json").write_text(json.dumps(OUT, indent=1, default=str))
    log(f"total {time.time() - T0:.1f} s")
