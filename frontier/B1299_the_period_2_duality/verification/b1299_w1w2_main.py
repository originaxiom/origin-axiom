"""B1299 (b): sm:B1280 Theorem 1's step (a) on MAIN's own W1/W2 points (B71's parametrisation, B1267's points):
[A,B] = c mu^3 on W1 and [A,B] mu^3 = c on W2 with c = 1; the transpose sheet's ninth trace tr[A^T,B^T] = tr[B,A];
and, with the B1297/B1298 numeric engine on B71's fibred presentation <a,b,t | t a t^-1 = phi(a), t b t^-1 = phi(b)>,
peripheral mu = a^-1 t (w = a), lambda = [a,b]: (a0, a1, t0, t1, r1, I) at generic points -- B1267's 'rigid' and t0 = 0 => I = 0."""
import os, sys, importlib.util, json
import numpy as np
REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
spec = importlib.util.spec_from_file_location("per", os.path.join(REPO, "frontier", "B71_sl3_apoly", "peripheral.py"))
per = importlib.util.module_from_spec(spec); spec.loader.exec_module(per)
TOL = 1e-7
def nrank(M):
    if M.size == 0: return 0
    s = np.linalg.svd(M, compute_uv=False); return int(np.sum(s > TOL * max(1.0, s[0]))) if s.size else 0
def nnull(M):
    u, s, vh = np.linalg.svd(M); r = int(np.sum(s > TOL * max(1.0, s[0]))) if s.size else 0; return vh[r:].conj().T
class NRep:
    def __init__(self, ims): self.im = {(g, 1): M for g, M in ims.items()}; self.dim = next(iter(ims.values())).shape[0]
    def letter(self, g, e):
        if e == -1 and (g, -1) not in self.im: self.im[(g, -1)] = np.linalg.inv(self.im[(g, 1)])
        return self.im[(g, e)]
    def __call__(self, w):
        M = np.eye(self.dim, dtype=complex)
        for g, e in w: M = M @ self.letter(g, e)
        return M
def nfox(rep, word, gs):
    n = rep.dim; D = {g: np.zeros((n, n), dtype=complex) for g in gs}; P = np.eye(n, dtype=complex)
    for g, e in word:
        if e == 1: D[g] += P; P = P @ rep.letter(g, 1)
        else: P = P @ rep.letter(g, -1); D[g] -= P
    return D

from scipy.optimize import fsolve
def polish(A, B, coords, xtol=1e-15):
    """Newton-polish B71's realisation to machine precision (same residual as per.realize, tighter xtol)."""
    x1, x2, x3, x4, x5, x6, x7, x8 = (complex(c) for c in coords); Ai = np.linalg.inv(A)
    def resid(v):
        Bm = (v[:9] + 1j * v[9:]).reshape(3, 3); adjB = per._adjugate(Bm)
        e = np.array([np.trace(Bm) - x2, np.trace(A @ Bm) - x3, np.trace(Ai @ Bm) - x6, np.trace(adjB) - x5, np.trace(A @ adjB) - x7,
                      np.trace(Ai @ adjB) - x8, np.linalg.det(Bm) - 1.0, Bm[0, 1] - 1.0, Bm[1, 2] - 1.0], dtype=complex)
        return np.concatenate([e.real, e.imag])
    v0 = np.concatenate([B.real.ravel(), B.imag.ravel()])
    sol, info, ier, msg = fsolve(resid, v0, full_output=True, xtol=xtol)
    Bp = (sol[:9] + 1j * sol[9:]).reshape(3, 3)
    return Bp, float(np.max(np.abs(resid(sol))))

def w(s): return [(c.lower(), 1 if c.islower() else -1) for c in s]
GENS = ["a", "b", "t"]
RELS_BY_CONV = {"aab": [w("taTBAA"), w("tbTBA")],        # phi: a -> a^2 b, b -> ab ; relators t a T (aab)^-1, t b T (ab)^-1
               "aba": [w("taTABA"), w("tbTBA")]}         # phi: a -> aba,   b -> ab ; relators t a T (aba)^-1, t b T (ab)^-1
RELS = RELS_BY_CONV["aab"]
MU, LAM = w("At"), w("abAB")
def data(rep, cusp, RELS):
    n = rep.dim
    d0 = np.block([[rep.letter(g, 1) - np.eye(n)] for g in GENS]); d1 = np.block([[nfox(rep, R, GENS)[g] for g in GENS] for R in RELS])
    r0, r1 = nrank(d0), nrank(d1); a0, a1, a2 = n - r0, n * 3 - r1 - r0, n * 2 - r1
    Z1 = nnull(d1); Res = np.block([[nfox(rep, ww, GENS)[g] for g in GENS] for ww in cusp])
    m, l = rep(cusp[0]), rep(cusp[1]); cd0 = np.vstack([m - np.eye(n), l - np.eye(n)])
    crep = NRep({"m": m, "l": l}); cd1 = np.block([[nfox(crep, w("mlML"), ["m", "l"])[g] for g in ["m", "l"]]])
    t0 = n - nrank(cd0); t1 = 2 * n - nrank(cd1) - nrank(cd0)
    rr = nrank(np.hstack([Res @ Z1, cd0])) - nrank(cd0)
    return a0, a1, a2, t0, t1, rr
import itertools
GRID = [1.7, 2.3, 2.7, 3.3, 4.1]                      # B1267's own grid: main's banked points
rows = []; worst_c = 0.0; worst_ninth = 0.0; worst_rel = 0.0
for name, fn, kind in (("W1", per.W1, "[A,B] = c mu^3"), ("W2", per.W2, "[A,B] mu^3 = c")):
    got = 0
    for p, q in itertools.product(GRID, repeat=2):
        if got >= 12: break
        out = per.realize(fn(p, q))
        if out is None: continue
        A, B = out; B, pres_ = polish(A, B, fn(p, q)); t, res, wmat = per.monodromy(A, B, with_conjugator=True, tol=1e-6)
        if t is None: continue
        mu = np.linalg.inv(wmat) @ t; comm = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B); mu3 = np.linalg.matrix_power(mu, 3)
        X = comm @ np.linalg.inv(mu3) if name == "W1" else comm @ mu3
        c = np.trace(X) / 3; dev = np.max(np.abs(X - c * np.eye(3)))
        ninth = abs(np.trace(A.T @ B.T @ np.linalg.inv(A.T) @ np.linalg.inv(B.T)) - np.trace(B @ A @ np.linalg.inv(B) @ np.linalg.inv(A)))
        rep = NRep({"a": A, "b": B, "t": t})
        conv = next((c for c, RR in RELS_BY_CONV.items() if max(np.max(np.abs(rep(R) - np.eye(3))) for R in RR) < 1e-6), None)
        if conv is None: continue
        RELS = RELS_BY_CONV[conv]; rel = max(np.max(np.abs(rep(R) - np.eye(3))) for R in RELS)
        a0, a1, a2, t0, t1, r1 = data(rep, [MU, LAM], RELS)
        repd = NRep({g: np.linalg.inv(M).T for g, M in {"a": A, "b": B, "t": t}.items()}); b0, b1, b2, s0, s1, r1s = data(repd, [MU, LAM], RELS)
        I = (a0 - b0) + s0 - r1
        rows.append(dict(comp=name, conv=conv, polish_resid=pres_, p=[p.real, p.imag], q=[q.real, q.imag], c=[c.real, c.imag], c_dev=float(dev), ninth=float(ninth), rel=float(rel), a=(a0, a1, a2), t=(t0, t1), r1=r1, r1s=r1s, I=int(I)))
        worst_c = max(worst_c, abs(c - 1)); worst_dev_ratio = max(globals().get('worst_dev_ratio', 0.0), dev / max(10 * rel, 1e-9) * 10)   # non-scalar <= max(10 x relator residual, 1e-9): ratio <= 10; globals()['worst_dev_ratio'] = worst_dev_ratio; worst_ninth = max(worst_ninth, ninth); worst_rel = max(worst_rel, rel); got += 1
        print(f"{name} point {got:2d}: c = {c:.12f} (non-scalar {dev:.1e}); |tr[A^T,B^T]-tr[B,A]| = {ninth:.1e}; relators {rel:.1e}; a=({a0},{a1},{a2}) t=({t0},{t1}) r1={r1} r1*={r1s} I={I}")
print(f"\nQ1: worst |c-1| = {worst_c:.2e} (registered: <= 1e-9); non-scalar part of [A,B] mu^(-+3): max {max(r['c_dev'] for r in rows):.1e}, vs realisation residual max {max(max(r['polish_resid'], r['rel']) for r in rows):.1e} (reported, not a criterion); worst ninth-trace identity {worst_ninth:.2e}; worst relator {worst_rel:.2e}")
print("    a1 = 0 (rigid) at every generic point:", all(r["a"][1] == 0 for r in rows), " t0 = 0 and I = 0 everywhere:", all(r["t"][0] == 0 and r["I"] == 0 for r in rows))
json.dump(rows, open("b1299_w1w2_main.json", "w"), indent=1)
assert len(rows) >= 20, ("vacuous: too few points survived", len(rows))
print("points tested:", len(rows), {r["comp"] for r in rows}, "conventions:", {r["conv"] for r in rows})
print("Q1:", "PASS" if len(rows) >= 20 and worst_c < 1e-9 and worst_ninth < 1e-9 and all(r["a"][1] == 0 and r["t"][0] == 0 and r["I"] == 0 for r in rows) else "FAIL")
