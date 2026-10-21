"""W111: the checks of the surface route (P-211; main's ask, relay of 2026-10-21). The proof, W111_PROOF.md, was
committed before this script (bfd9ffadc). One run. The proof does not rest on these checks.

C1  the explicit moves on words, g = 2, 3: tau_k, tau'_k, sigma_k keep the boundary exactly; sigma_k and its stated
    inverse compose to the identity; mu' keeps the boundary exactly, inverts, and acts mod 2 as T_u, u = b1 + a2.
C2  step 2 of (a), exact (sympy): the quaternion handle and a generic Y in SL(2, C).
C3  step 4 of (a), exact (sympy): N = [[0, 1], [0, 0]] and a nilpotent X with tr(NX) = 0.
C4  (a) by numerical search at g = 2 (120 random starts) and g = 1 (60, the control).
C5  (b): H(3) at g = 1, 2 and H(5) at g = 1, an intertwiner for every explicit move; the character formula.
C6  (c): the sixteen 2^{1+4} forms at g = 2 under the explicit moves; the transvection lemma and the forms equal to 1
    on every non-zero vector, at g = 1, 2, 3.

Run: python3 the_surface_route.py -> the_surface_route.json and the_surface_route_run.txt beside it.
"""
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_surface_route.json"
RUN = HERE / "the_surface_route_run.txt"
LINES = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LINES.append(s)


# ---------------------------------------------------------------- words and the moves of the surface route

def inv(w):
    return tuple(-x for x in reversed(w))


def free(w):
    st = []
    for x in w:
        if st and st[-1] == -x:
            st.pop()
        else:
            st.append(x)
    return tuple(st)


def apply(phi, w):
    out = []
    for x in w:
        out.extend(phi.get(x, (x,)) if x > 0 else inv(phi.get(-x, (-x,))))
    return free(out)


def compose(phi, psi, n):
    return {a: apply(phi, psi.get(a, (a,))) for a in range(1, n + 1)}


def A(k):
    return 2 * k - 1


def B(k):
    return 2 * k


def comm(k):
    return (A(k), B(k), -A(k), -B(k))


def boundary(g):
    return tuple(x for k in range(1, g + 1) for x in comm(k))


def tau(k, e=1):
    return {B(k): (B(k), e * A(k))}


def taup(k, e=1):
    return {A(k): (A(k), e * B(k))}


def sigma(k):
    c = comm(k)
    return {A(k): free(c + (A(k + 1),) + inv(c)), B(k): free(c + (B(k + 1),) + inv(c)), A(k + 1): (A(k),),
            B(k + 1): (B(k),)}


def sigma_inv(k):
    c = comm(k + 1)
    return {A(k): (A(k + 1),), B(k): (B(k + 1),), A(k + 1): free(inv(c) + (A(k),) + c),
            B(k + 1): free(inv(c) + (B(k),) + c)}


GAMMA = (-B(1), A(2))


def mu_prime():
    mu = {A(1): GAMMA + (A(1),), B(2): GAMMA + (B(2),)}
    return {x: free(inv(GAMMA) + mu.get(x, (x,)) + GAMMA) for x in (A(1), B(1), A(2), B(2))}


def mu_prime_inv():
    muinv = {A(1): inv(GAMMA) + (A(1),), B(2): inv(GAMMA) + (B(2),)}
    return {x: free(GAMMA + muinv.get(x, (x,)) + inv(GAMMA)) for x in (A(1), B(1), A(2), B(2))}


def moves(g):
    ms = []
    for k in range(1, g + 1):
        ms += [(f"tau_{k}", tau(k)), (f"tau_{k}^-1", tau(k, -1)), (f"tau'_{k}", taup(k)), (f"tau'_{k}^-1", taup(k, -1))]
    for k in range(1, g):
        ms += [(f"sigma_{k}", sigma(k)), (f"sigma_{k}^-1", sigma_inv(k))]
    if g >= 2:
        ms += [("mu'", mu_prime()), ("mu'^-1", mu_prime_inv())]
    return ms


def omega2(g):
    """the intersection form mod 2 on the basis a1, b1, ..., ag, bg"""
    W = np.zeros((2 * g, 2 * g), dtype=int)
    for k in range(g):
        W[2 * k, 2 * k + 1] = W[2 * k + 1, 2 * k] = 1
    return W


def mod2(phi, n):
    M = np.zeros((n, n), dtype=int)
    for a in range(1, n + 1):
        for x in phi.get(a, (a,)):
            M[abs(x) - 1, a - 1] ^= 1
    return M


def transvection(u, W):
    n = len(u)
    T = np.eye(n, dtype=int)
    for j in range(n):
        e = np.zeros(n, dtype=int)
        e[j] = 1
        T[:, j] = (e + (e @ W @ u % 2) * u) % 2
    return T


# ---------------------------------------------------------------- C1

def c1():
    res, ok = {}, True
    for g in (2, 3):
        n, D = 2 * g, boundary(g)
        ident = {a: (a,) for a in range(1, n + 1)}
        kept = {name: apply(phi, D) == D for name, phi in moves(g)}
        inverses = all(compose(sigma(k), sigma_inv(k), n) == ident and compose(sigma_inv(k), sigma(k), n) == ident
                       for k in range(1, g))
        mu_inv = compose(mu_prime(), mu_prime_inv(), n) == ident and compose(mu_prime_inv(), mu_prime(), n) == ident
        u = np.zeros(n, dtype=int)
        u[B(1) - 1] = u[A(2) - 1] = 1
        mu_mod2 = bool((mod2(mu_prime(), n) == transvection(u, omega2(g))).all())
        tau_mod2 = all(bool((mod2(tau(k), n) == transvection(np.eye(n, dtype=int)[A(k) - 1], omega2(g))).all())
                       and bool((mod2(taup(k), n) == transvection(np.eye(n, dtype=int)[B(k) - 1], omega2(g))).all())
                       for k in range(1, g + 1))
        res[f"g = {g}"] = {"boundary kept exactly": kept, "sigma inverses": inverses, "mu' inverse": mu_inv,
                           "mu' mod 2 is T_(b1 + a2)": mu_mod2, "tau_k, tau'_k mod 2 are T_(a_k), T_(b_k)": tau_mod2}
        ok = ok and all(kept.values()) and inverses and mu_inv and mu_mod2 and tau_mod2
    say("C1", "held" if ok else "FAILED", res)
    return ok, res


# ---------------------------------------------------------------- C2, C3

def c2():
    p, q, r, s = sp.symbols("p q r s")
    Am, Bm = sp.Matrix([[sp.I, 0], [0, -sp.I]]), sp.Matrix([[0, 1], [-1, 0]])
    Y = sp.Matrix([[p, q], [r, s]])
    tr = lambda m: sp.expand(m.trace())
    eqs = [tr(Bm * Am * Y) - tr(Bm * Y), tr(Bm * Am.inv() * Y) - tr(Bm * Y), tr(Am * Bm * Y) - tr(Am * Y),
           tr(Am * Bm.inv() * Y) - tr(Am * Y), Y.det() - 1]
    sols = sp.solve(eqs, [p, q, r, s], dict=True)
    got = sorted(tuple(str(sol.get(v, v)) for v in (p, q, r, s)) for sol in sols)
    ok = got == sorted([("1", "0", "0", "1"), ("-1", "0", "0", "-1")])
    res = {"solutions (p, q, r, s)": got}
    say("C2", "held" if ok else "FAILED", res)
    return ok, res


def c3():
    u, v, w = sp.symbols("u v w")
    N = sp.Matrix([[0, 1], [0, 0]])
    X = sp.Matrix([[u, v], [w, -u]])
    sols = sp.solve([X.det(), (N * X).trace()], [u, w], dict=True)
    got = [{str(k): str(val) for k, val in sol.items()} for sol in sols]
    ok = got == [{"u": "0", "w": "0"}]
    res = {"solutions": got, "so X = [[0, v], [0, 0]], proportional to N": ok}
    say("C3", "held" if ok else "FAILED", res)
    return ok, res


# ---------------------------------------------------------------- C4

def procesi_words(n):
    return [w for k in (1, 2, 3) for w in itertools.combinations(range(1, n + 1), k)]


def mat_of(params, n):
    z = params[: 4 * n] + 1j * params[4 * n:]
    mats = []
    for k in range(n):
        m = z[4 * k: 4 * k + 4].reshape(2, 2)
        mats.append(m / np.sqrt(np.linalg.det(m)))
    return mats


def word_mat(w, mats, invs):
    m = np.eye(mats[0].shape[0], dtype=complex)
    for x in w:
        m = m @ (mats[x - 1] if x > 0 else invs[-x - 1])
    return m


def search(g, starts, seed):
    n = 2 * g
    ms = [phi for _, phi in moves(g)]
    words = procesi_words(n)

    def resid(params):
        mats = mat_of(params, n)
        invs = [np.linalg.inv(m) for m in mats]
        base = [np.trace(word_mat(w, mats, invs)) for w in words]
        out = []
        for phi in ms:
            imgs = [word_mat(phi.get(a, (a,)), mats, invs) for a in range(1, n + 1)]
            iimgs = [np.linalg.inv(m) for m in imgs]
            for w, t0 in zip(words, base):
                out.append(np.trace(word_mat(w, imgs, iimgs)) - t0)
        out = np.array(out)
        return np.concatenate([out.real, out.imag])

    rng = np.random.default_rng(seed)
    zeros, nonzeros, kinds = 0, 0, {"trivial": 0, "quaternion": 0, "other": 0}
    worst_nonzero = None
    for _ in range(starts):
        x0 = rng.normal(size=8 * n)
        try:
            sol = least_squares(resid, x0, method="lm", xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
        except Exception:
            nonzeros += 1
            continue
        r = np.max(np.abs(resid(sol.x)))
        if r < 1e-9:
            zeros += 1
            mats = mat_of(sol.x, n)
            invs = [np.linalg.inv(m) for m in mats]
            traces = np.array([np.trace(word_mat(w, mats, invs)) for w in words])
            if np.max(np.abs(traces - 2)) < 1e-6:
                kinds["trivial"] += 1
            elif g == 1 and np.max(np.abs(traces)) < 1e-6:
                kinds["quaternion"] += 1
            else:
                kinds["other"] += 1
        else:
            nonzeros += 1
            worst_nonzero = r if worst_nonzero is None else min(worst_nonzero, r)
    return {"starts": starts, "zeros": zeros, "non-zero ends": nonzeros, "zeros by kind": kinds,
            "smallest defect among the non-zero ends": worst_nonzero}


def c4():
    r2 = search(2, 120, 20261021)
    r1 = search(1, 60, 20261022)
    ok = r2["zeros"] > 0 and r2["zeros by kind"]["other"] == 0 and r2["zeros by kind"]["quaternion"] == 0 and \
        r1["zeros by kind"]["other"] == 0
    res = {"g = 2": r2, "g = 1 (control)": r1}
    say("C4", "held" if ok else "FAILED", res)
    return ok, res


# ---------------------------------------------------------------- C5

def heisenberg(p, g):
    zeta = np.exp(2j * np.pi / p)
    Xs = np.roll(np.eye(p), 1, axis=0)
    Zs = np.diag([zeta ** k for k in range(p)])
    mats = []
    for k in range(g):
        for base in (Xs, Zs):
            m = np.array([[1.0 + 0j]])
            for j in range(g):
                m = np.kron(m, base if j == k else np.eye(p))
            mats.append(m)
    return mats, zeta


def intertwiner(mats, imgs):
    d = mats[0].shape[0]
    rows = [np.kron(m.T, np.eye(d)) - np.kron(np.eye(d), im) for m, im in zip(mats, imgs)]
    S = np.vstack(rows)
    sv = np.linalg.svd(S, compute_uv=False)
    _, _, vh = np.linalg.svd(S)
    M = vh[-1].conj().reshape(d, d, order="F")
    rel = max(np.max(np.abs(M @ m - im @ M)) for m, im in zip(mats, imgs))
    return float(sv[-1]), float(sv[-2]) if len(sv) > 1 else None, float(np.linalg.cond(M)), float(rel)


def c5():
    res, ok = {}, True
    rng = np.random.default_rng(5)
    for p, g in ((3, 1), (3, 2), (5, 1)):
        mats, zeta = heisenberg(p, g)
        invs = [np.linalg.inv(m) for m in mats]
        n = 2 * g
        rows = {}
        for name, phi in moves(g):
            imgs = [word_mat(phi.get(a, (a,)), mats, invs) for a in range(1, n + 1)]
            s_min, s_next, cond, rel = intertwiner(mats, imgs)
            good = s_min < 1e-9 and cond < 1e6 and rel < 1e-9
            rows[name] = {"smallest singular value": s_min, "next": s_next, "cond(M)": cond, "residual": rel,
                          "intertwiner": good}
            ok = ok and good
        bad = 0
        for _ in range(400):
            L = int(rng.integers(1, 13))
            w = []
            while len(w) < L:
                x = int(rng.choice([s * k for k in range(1, n + 1) for s in (1, -1)]))
                if not w or w[-1] != -x:
                    w.append(x)
            m = word_mat(w, mats, invs)
            ex = [sum(np.sign(x) for x in w if abs(x) == k) % p for k in range(1, n + 1)]
            if all(e == 0 for e in ex):
                lam = m[0, 0]
                okw = np.allclose(m, lam * np.eye(m.shape[0]), atol=1e-9) and abs(lam ** p - 1) < 1e-9
            else:
                okw = abs(np.trace(m)) < 1e-9
            bad += 0 if okw else 1
        rows["character formula failures (400 random words)"] = bad
        ok = ok and bad == 0
        res[f"H({p}), g = {g}"] = rows
    say("C5", "held" if ok else "FAILED", res)
    return ok, res


# ---------------------------------------------------------------- C6

def quad_value(qb, v, W):
    """q(v) for the form with values qb on the basis and polar W, over F_2"""
    n = len(v)
    val = int(sum(v[i] * qb[i] for i in range(n)))
    for i in range(n):
        for j in range(i + 1, n):
            val += int(v[i] * v[j] * W[i, j])
    return val % 2


def c6():
    res, ok = {}, True
    # the transvection lemma and the forms equal to 1 on every non-zero vector, at g = 1, 2, 3
    for g in (1, 2, 3):
        n = 2 * g
        W = omega2(g)
        vecs = [np.array(v) for v in itertools.product((0, 1), repeat=n)]
        lemma_bad, all_one, arf1 = 0, 0, 0
        for qb in itertools.product((0, 1), repeat=n):
            qv = {tuple(v): quad_value(qb, v, W) for v in vecs}
            for u in vecs[1:]:
                T = transvection(u, W)
                keeps = all(qv[tuple((T @ v) % 2)] == qv[tuple(v)] for v in vecs)
                lemma_bad += int(keeps != (qv[tuple(u)] == 1))
            all_one += int(all(qv[tuple(v)] == 1 for v in vecs[1:]))
            arf1 += int(sum(qb[2 * k] * qb[2 * k + 1] for k in range(g)) % 2 == 1)
        res[f"g = {g}"] = {"transvection lemma failures": lemma_bad, "forms equal to 1 off zero": all_one,
                           "forms of Arf invariant 1": arf1}
        ok = ok and lemma_bad == 0 and all_one == (1 if g == 1 else 0) and arf1 == 2 ** (g - 1) * (2 ** g - 1)
    # the sixteen 2^{1+4} representations at g = 2 under the explicit moves
    Xp, Zp, I2 = np.array([[0, 1], [1, 0]], dtype=complex), np.diag([1, -1]).astype(complex), np.eye(2)
    gens = [np.kron(Xp, I2), np.kron(Zp, I2), np.kron(I2, Xp), np.kron(I2, Zp)]
    words = [()]
    for L in (1, 2, 3, 4):
        for w in itertools.product((1, -1, 2, -2, 3, -3, 4, -4), repeat=L):
            if free(w) == w:
                words.append(w)
    table = {}
    kept_by_all = []
    for qb in itertools.product((0, 1), repeat=4):
        mats = [(1j ** qb[i]) * gens[i] for i in range(4)]
        invs = [np.linalg.inv(m) for m in mats]
        base = [np.trace(word_mat(w, mats, invs)) for w in words]
        row = {}
        for name, phi in moves(2):
            imgs = [word_mat(phi.get(a, (a,)), mats, invs) for a in range(1, 5)]
            iimgs = [np.linalg.inv(m) for m in imgs]
            row[name] = all(abs(np.trace(word_mat(w, imgs, iimgs)) - t0) < 1e-9 for w, t0 in zip(words, base))
        table["".join(map(str, qb))] = row
        if all(row.values()):
            kept_by_all.append("".join(map(str, qb)))
    tau_keep = [k for k, r in table.items() if all(r[m] for m in r if m.startswith("tau"))]
    mu_keep = [k for k, r in table.items() if r["mu'"]]
    mu_pred = ["".join(map(str, qb)) for qb in itertools.product((0, 1), repeat=4) if (qb[1] + qb[2]) % 2 == 1]
    res["g = 2, the sixteen forms (q on a1 b1 a2 b2)"] = {
        "kept by every tau": tau_keep, "kept by mu'": mu_keep, "kept by every move": kept_by_all,
        "mu' keeps exactly the forms with q(b1 + a2) = 1": sorted(mu_keep) == sorted(mu_pred)}
    ok = ok and tau_keep == ["1111"] and kept_by_all == [] and sorted(mu_keep) == sorted(mu_pred)
    say("C6", "held" if ok else "FAILED", res)
    return ok, res


def main():
    out = {"status": "one run", "proof": "W111_PROOF.md (bfd9ffadc)", "cells": {}}
    for name, fn in (("C1", c1), ("C2", c2), ("C3", c3), ("C4", c4), ("C5", c5), ("C6", c6)):
        ok, res = fn()
        out["cells"][name] = bool(ok)
        out[name] = res
    say("cells:", out["cells"])
    OUT.write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    RUN.write_text("\n".join(LINES) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
