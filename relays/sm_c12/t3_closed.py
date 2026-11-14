#!/usr/bin/env python3
"""SM-C12 T3 (W3): remainders on the closed torus bundles of the tick, T_{J^n}, n = 1..6 (card
relays/cards/SM_C12_the-principle-note-tested.md, pushed before this run).  Presentation <x, y, t | [x,y],
t x t^-1 = x^a y^c, t y t^-1 = x^b y^d> with J^n = [[a, b], [c, d]] (columns the images).  Modules: characters (t-value of
order | 24, every torsion character), non-split doublets over every ordered pair (alpha = beta included), and for odd n
the 2-dimensional modules induced from the orientation cover.  For each: h0 and h1 of V, V*, V (x) w, V* (x) w.
Reported: g0 = h1(V*) - h1(V); g_w = h1(V* (x) w) - h1(V); the closed-duality control g_w = h0(V* (x) w) - h0(V) (the
card's written form has the h0 terms the other way round, a slip said on the page; both are reported); and everything
again on the modules with no invariants (h0 = 0 for all four), the scope of the claim.
    python3 t3_closed.py [out.json]"""
import sys, json, math, itertools, pathlib
from fractions import Fraction as Fr
from collections import Counter
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
rng = np.random.default_rng(20261114)
TOL = 1e-8
J = np.array([[1, 1], [1, 0]], dtype=object)


def rank(M):
    if M.size == 0: return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > TOL * max(1.0, s[0])))


def null(M):
    u, s, vh = np.linalg.svd(M)
    r = int(np.sum(s > TOL * max(1.0, s[0]))) if s.size else 0
    return vh[r:].conj().T


def orth(M):
    if M.size == 0 or M.shape[1] == 0: return np.zeros((M.shape[0], 0), dtype=complex)
    u, s, vh = np.linalg.svd(M, full_matrices=False)
    return u[:, :int(np.sum(s > TOL * max(1.0, s[0])))]


def mpow(A, n):
    R = np.array([[1, 0], [0, 1]], dtype=object)
    for _ in range(n): R = R.dot(A)
    return R


def pw(g, e): return [g] * e if e >= 0 else [-g] * (-e)


def group(n):
    M = mpow(J, n); a, b, c, d = int(M[0, 0]), int(M[0, 1]), int(M[1, 0]), int(M[1, 1])
    rels = [[1, 2, -1, -2], [3, 1, -3] + pw(2, -c) + pw(1, -a), [3, 2, -3] + pw(2, -d) + pw(1, -b)]
    # check the words: t x t^-1 (x^a y^c)^-1 = t x t^-1 y^-c x^-a  (x, y commute in the group)
    return M, rels


def mat_of(rho, w):
    P = np.eye(rho[1].shape[0], dtype=complex)
    for g in w: P = P @ (rho[g] if g > 0 else np.linalg.inv(rho[-g]))
    return P


def fox(rho, w):
    d = rho[1].shape[0]; D = {k: np.zeros((d, d), dtype=complex) for k in (1, 2, 3)}; pre = np.eye(d, dtype=complex)
    for g in w:
        if g > 0: D[g] += pre; pre = pre @ rho[g]
        else: pre = pre @ np.linalg.inv(rho[-g]); D[-g] -= pre
    return np.hstack([D[1], D[2], D[3]])


def h01(rels, rho):
    d = rho[1].shape[0]
    assert all(np.allclose(mat_of(rho, r), np.eye(d), atol=1e-8) for r in rels), "not a representation"
    Z = null(np.vstack([fox(rho, r) for r in rels]))
    B = np.vstack([rho[k] - np.eye(d) for k in (1, 2, 3)]); rB = rank(B)
    return d - rB, Z.shape[1] - rB


def dual(rho): return {k: np.linalg.inv(m).T for k, m in rho.items()}
def tw(rho, w): return {k: m * w[k] for k, m in rho.items()}


def characters(M, n):
    a, b, c, d = int(M[0, 0]), int(M[0, 1]), int(M[1, 0]), int(M[1, 1])
    det = abs((a - 1) * (d - 1) - b * c); g = math.gcd(math.gcd(a - 1, b), math.gcd(c, d - 1)); e = det // g if det else 1
    out = []
    for i, j in itertools.product(range(e), repeat=2):
        tx, ty = Fr(i, e), Fr(j, e)
        if ((1 - a) * tx - c * ty) % 1 == 0 and (-b * tx + (1 - d) * ty) % 1 == 0:
            for k in range(24): out.append((tx, ty, Fr(k, 24)))
    return out


def cval(th): return {k + 1: complex(np.exp(2j * math.pi * float(th[k]))) for k in range(3)}


def doublet(rels, a, b):
    al, be = cval(a), cval(b); l = {k: al[k] / be[k] for k in (1, 2, 3)}
    lr = {k: np.array([[l[k]]]) for k in (1, 2, 3)}
    Zl = null(np.vstack([fox(lr, r) for r in rels])); Bl = orth(np.array([[l[k] - 1] for k in (1, 2, 3)]))
    if Zl.shape[1] - rank(Bl) < 1: return None
    z = Zl @ (rng.normal(size=Zl.shape[1]) + 1j * rng.normal(size=Zl.shape[1]))
    if Bl.shape[1]: z = z - Bl @ (Bl.conj().T @ z)
    if np.linalg.norm(z) < 1e-6: return None
    z = z / np.linalg.norm(z)
    return {k: np.array([[al[k], z[k - 1] * be[k]], [0, be[k]]], dtype=complex) for k in (1, 2, 3)}


def induced(M, n):
    """odd n: modules induced from characters psi of H = <x, y, t^2> fixed by M^2 and not by M"""
    M2 = M.dot(M); a2, b2, c2, d2 = int(M2[0, 0]), int(M2[0, 1]), int(M2[1, 0]), int(M2[1, 1])
    det = abs((a2 - 1) * (d2 - 1) - b2 * c2); g = math.gcd(math.gcd(a2 - 1, b2), math.gcd(c2, d2 - 1)); e = det // g
    a, b, c, d = int(M[0, 0]), int(M[0, 1]), int(M[1, 0]), int(M[1, 1])
    Minv = [[d, -b], [-c, a]] if a * d - b * c == 1 else [[-d, b], [c, -a]]
    out = []
    for i, j in itertools.product(range(e), repeat=2):
        tx, ty = Fr(i, e), Fr(j, e)
        if ((1 - a2) * tx - c2 * ty) % 1 or (-b2 * tx + (1 - d2) * ty) % 1: continue
        if ((1 - a) * tx - c * ty) % 1 == 0 and (-b * tx + (1 - d) * ty) % 1 == 0: continue        # fixed by M: skip
        for k in range(12):
            ps = lambda v: complex(np.exp(2j * math.pi * float(v[0] * tx + v[1] * ty)))
            # t^-1 x t = phi^-1(x): exponent vector M^-1 e_x
            ex_inv = (Minv[0][0], Minv[1][0]); ey_inv = (Minv[0][1], Minv[1][1])
            T2 = complex(np.exp(2j * math.pi * k / 12))
            rho = {1: np.diag([ps((1, 0)), ps(ex_inv)]), 2: np.diag([ps((0, 1)), ps(ey_inv)]),
                   3: np.array([[0, T2], [1, 0]], dtype=complex)}
            out.append((((str(tx), str(ty)), k), rho))
    return out


def classify(rows):
    out = {"modules": len(rows), "g0": dict(Counter(r["g0"] for r in rows)), "g_w": dict(Counter(r["g_w"] for r in rows)),
           "control_correct": sum(r["ctl"] for r in rows), "control_as_written": sum(r["ctl_written"] for r in rows)}
    free = [r for r in rows if r["no_invariants"]]
    out["no_invariants"] = {"modules": len(free), "g0": dict(Counter(r["g0"] for r in free)),
                            "g_w": dict(Counter(r["g_w"] for r in free))}
    return out


def row(rels, rho, w, tag):
    V, Vs, Vw, Vsw = rho, dual(rho), tw(rho, w), tw(dual(rho), w)
    (h0, h1), (h0s, h1s), (h0w, h1w), (h0sw, h1sw) = h01(rels, V), h01(rels, Vs), h01(rels, Vw), h01(rels, Vsw)
    gw = h1sw - h1
    return {"module": tag, "h0": [h0, h0s, h0w, h0sw], "h1": [h1, h1s, h1w, h1sw], "g0": h1s - h1, "g_w": gw,
            "ctl": gw == h0sw - h0, "ctl_written": gw == h0 - h0sw, "no_invariants": h0 == h0s == h0w == h0sw == 0}


def main():
    res = {}
    for n in range(1, 7):
        M, rels = group(n); w = {1: 1.0, 2: 1.0, 3: (-1.0 if n % 2 else 1.0)}
        chars = characters(M, n); rows_c, rows_d, rows_i = [], [], []
        for ch in chars:
            rows_c.append(row(rels, {k: np.array([[v]]) for k, v in cval(ch).items()}, w, [str(x) for x in ch]))
        for a_, b_ in itertools.product(chars, repeat=2):
            V = doublet(rels, a_, b_)
            if V is not None: rows_d.append(row(rels, V, w, [[str(x) for x in a_], [str(x) for x in b_]]))
        if n % 2:
            for tag, rho in induced(M, n): rows_i.append(row(rels, rho, w, tag))
        res[n] = {"orientable": n % 2 == 0, "characters": classify(rows_c), "doublets": classify(rows_d),
                  "induced": classify(rows_i) if n % 2 else None,
                  "witnesses_g0_no_invariants": [r for r in rows_c + rows_d + rows_i if r["no_invariants"] and r["g0"] != 0][:6]}
        print(n, json.dumps({k: (v if k != "witnesses_g0_no_invariants" else len(v)) for k, v in res[n].items()}), flush=True)
    allrows_ok = all(res[n][kind]["control_correct"] == res[n][kind]["modules"] for n in res for kind in ("characters", "doublets", "induced") if res[n][kind])
    w3 = not any(res[n][kind]["no_invariants"]["g0"].get(k, 0) for n in res if n % 2 for kind in ("characters", "doublets", "induced")
                 if res[n][kind] for k in res[n][kind]["no_invariants"]["g0"] if k != 0)
    res["summary"] = {"closed_duality_control_holds_everywhere": allrows_ok, "W3_happens_no_remainder_without_invariants_on_odd_n": w3}
    json.dump(res, open(sys.argv[1] if len(sys.argv) > 1 else HERE / "t3_results.json", "w"), indent=1, default=str)
    print(json.dumps(res["summary"]))


if __name__ == "__main__":
    main()
