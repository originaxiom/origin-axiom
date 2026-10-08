#!/usr/bin/env python3
"""B1614 -- THE OBSERVER LAYER ON THE WEAVE.  The record's observer layer (B752-B1184: a self-name, no private states,
no self-signing, one mirror-odd class) was computed on m004, one thread.  Re-posed on the weave, exactly:
 A1  QP-1, a self-name: the joint fixed points of L and R on the character variety (Fricke coordinates x, y, z = tr a,
     tr b, tr ab; L: (x, z, xz - y), R: (z, y, yz - x)); which are irreducible (kappa = x^2 + y^2 + z^2 - xyz - 2 != 2).
 A2  QP-2, private states, per local system at the common point (a -> i, b -> j): for E in {the trivial line, the three
     parity lines chi_p, the doublet rho_Q, the three matter blocks chi_p (x) rho_Q (W10's V), the adjoint Ad rho_Q}:
     dim H^1(F2; E), dim H^1(<c>; E) for the puncture loop c = [a, b], the rank of the restriction, and the private
     (interior) part = its kernel.  Group cohomology of the free group: Z^1 = E^2, B^1 = {(rho(a)v - v, rho(b)v - v)},
     H^1(<c>; E) = E / (rho(c) - 1)E, the restriction z -> z(c) by the cocycle rule.
 A3  QP-4, self-signing: the rule sigma (a -> ab, b -> a) fixes the common point (its Fricke action), normalises the
     moves (sigma L sigma^-1, sigma R sigma^-1 in SL(2, Z) = <L, R>), and reverses W21's form on V (B1610's module) --
     so it exchanges the two sheets, and no structure invariant under it chooses one (B1327).
 A4  the one-class question: the weave's mirror-odd bits as Z/2-characters of the generators {L, R, P, iota, sigma}:
     the sheet (whether the move reverses W21's form; = det on H_1), CP-oddness (whether it maps T to T-bar), the McKay
     orientation (the sign of its permutation of the three parities); which coincide; the rank of the span.
 A5  (the reading's cell, firewalled) the holonomy's even and odd parts on the matter triplet T: for L, R, LR and the
     puncture loop, chi_T(g) and its odd part Im chi_T(g) (the part that flips under g -> g^-1).
Writes observer_on_the_weave.json."""
import json, pathlib, sys, os, importlib.util, itertools
import numpy as np, sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("hands", FRONTIER / "B1610_the_hands_on_the_founding_torsor" / "verification" / "hands_on_the_torsor.py")
H = importlib.util.module_from_spec(spec); spec.loader.exec_module(H)
W = H.W
out = {}

# ---- A1
x, y, z = sp.symbols("x y z")
Lf = (x, z, x * z - y); Rf = (z, y, y * z - x)
sols = sp.solve([sp.Eq(a, b) for a, b in zip(Lf, (x, y, z))] + [sp.Eq(a, b) for a, b in zip(Rf, (x, y, z))], [x, y, z], dict=True)
kap = lambda s: sp.simplify(s[x] ** 2 + s[y] ** 2 + s[z] ** 2 - s[x] * s[y] * s[z] - 2)
out["A1"] = {"joint_fixed_points": [{str(k): str(v) for k, v in s.items()} for s in sols],
             "kappa": [str(kap(s)) for s in sols], "irreducible": [bool(kap(s) != 2) for s in sols]}

# ---- A2
I2 = np.eye(2, dtype=complex); qi = np.array([[1j, 0], [0, -1j]]); qj = np.array([[0, 1], [-1, 0]], dtype=complex)
def adj(g):
    basis = [qi, qj, qi @ qj]; M = np.zeros((3, 3), dtype=complex)
    for k, X in enumerate(basis):
        Y = g @ X @ np.linalg.inv(g)
        for l, Bm in enumerate(basis): M[l, k] = np.trace(Bm.conj().T @ Y) / 2      # the coefficient on the unit Bm
    return M
def cohom(ra, rb):
    n = ra.shape[0]; inv = np.linalg.inv
    rc = ra @ rb @ inv(ra) @ inv(rb)
    B = np.vstack([ra - np.eye(n), rb - np.eye(n)])                      # v -> (rho(a)v - v, rho(b)v - v)
    h1 = 2 * n - np.linalg.matrix_rank(B, tol=1e-9)
    # z(c) for c = a b a^-1 b^-1:  z(c) = z(a) + rho(a) z(b) - rho(a b a^-1) z(a) - rho(c) z(b)
    Za = np.eye(n) - ra @ rb @ inv(ra); Zb = ra - rc
    ev = np.hstack([Za, Zb])                                               # Z^1 = E^2 -> E
    im = rc - np.eye(n)
    rk_im = np.linalg.matrix_rank(im, tol=1e-9)
    U, s, Vh = np.linalg.svd(im); Qim = U[:, :rk_im]
    proj = np.eye(n) - Qim @ Qim.conj().T                                  # E -> E / im(rho(c) - 1)
    puncture = n - rk_im
    rk = np.linalg.matrix_rank(proj @ ev, tol=1e-9)
    return {"dim": n, "H1": int(h1), "H1_puncture": int(puncture), "restriction_rank": int(rk), "private": int(h1 - rk),
            "rho_c_is_minus_one": bool(np.allclose(rc, -np.eye(n)))}
PAR = [(1, 0), (0, 1), (1, 1)]
chi = lambda p: (np.array([[(-1) ** p[0]]], dtype=complex), np.array([[(-1) ** p[1]]], dtype=complex))
A2 = {"trivial": cohom(np.eye(1, dtype=complex), np.eye(1, dtype=complex))}
for p in PAR: A2[f"parity line {p}"] = cohom(*chi(p))
A2["doublet rho_Q"] = cohom(qi, qj)
for p in PAR:
    ca, cb = chi(p); A2[f"matter block chi{p} x rho_Q"] = cohom(ca[0, 0] * qi, cb[0, 0] * qj)
A2["adjoint Ad rho_Q"] = cohom(adj(qi), adj(qj))
out["A2"] = A2

# ---- A3
sig = {"a": "ab", "b": "a"}
sx, sy, sz = z, x, sp.expand(x * z - y)          # Fricke action of sigma: tr(sigma a) = tr(ab) = z, tr(sigma b) = tr a = x, tr(sigma(ab)) = tr(aba) = x z - y
fixed_common = [sp.simplify(e.subs({x: 0, y: 0, z: 0})) for e in (sx, sy, sz)]
Ms = np.array([[1, 1], [1, 0]]); Lm = np.array([[1, 1], [0, 1]]); Rm = np.array([[1, 0], [1, 1]])
conj = lambda A: Ms @ A @ np.round(np.linalg.inv(Ms)).astype(int)
r = H.read_rule("sigma", sig)
out["A3"] = {"sigma_on_common_point": [str(v) for v in fixed_common], "fixes_common_point": all(v == 0 for v in fixed_common),
             "sigma_L_sigma_inv": conj(Lm).tolist(), "sigma_R_sigma_inv": conj(Rm).tolist(),
             "conjugates_have_det_1": bool(round(np.linalg.det(conj(Lm))) == 1 and round(np.linalg.det(conj(Rm))) == 1),
             "sigma_on_form": r["form_on_V"], "exchanges_the_sheets": r["form_on_V"] == "reverses"}

# ---- A4
gens = {"L": {"a": "a", "b": "ab"}, "R": {"a": "ab", "b": "b"}, "P": {"a": "b", "b": "a"}, "iota": {"a": "A", "b": "B"}, "sigma": sig}
lifts = {"L": W.ML, "R": W.MR, "P": W.MP, "iota": W.MS}
def sheet(nm, m):
    if nm in lifts: return -1 if H.form_action(lifts[nm]) == "reverses" else 1
    return -1 if H.read_rule(nm, m)["form_on_V"] == "reverses" else 1
def det(m): return int(round(np.linalg.det(H.h1mat(m))))
def sgn(m):
    A = H.h1mat(m) % 2; pts = [(1, 0), (0, 1), (1, 1)]
    perm = [pts.index(tuple(int(v) for v in (A @ np.array(p)) % 2)) for p in pts]
    inv_ = sum(1 for i, j in itertools.combinations(range(3), 2) if perm[i] > perm[j]); return (-1) ** inv_
TB = H.PIECES["T"]
def cp_odd(nm, m):
    if nm not in lifts: return sheet(nm, m)
    M = lifts[nm]; img = M @ TB; Tb = H.PIECES["Tbar"]
    in_T = np.allclose(TB @ (TB.conj().T @ img), img, atol=1e-8); in_Tb = np.allclose(Tb @ (Tb.conj().T @ img), img, atol=1e-8)
    return 1 if in_T else (-1 if in_Tb else 0)
tab = {nm: {"sheet": sheet(nm, m), "det": det(m), "cp_odd": cp_odd(nm, m), "mckay_sign": sgn(m)} for nm, m in gens.items()}
vecs = [[0 if tab[nm][k] == 1 else 1 for nm in gens] for k in ("sheet", "cp_odd", "mckay_sign")]
def rank_gf2(rows):
    rows = [r[:] for r in rows]; rk = 0; ncol = len(rows[0])
    for c in range(ncol):
        piv = next((i for i in range(rk, len(rows)) if rows[i][c]), None)
        if piv is None: continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        for i in range(len(rows)):
            if i != rk and rows[i][c]: rows[i] = [(u + v) % 2 for u, v in zip(rows[i], rows[rk])]
        rk += 1
    return rk
rank2 = rank_gf2(vecs)
out["A4"] = {"table": tab, "sheet_equals_det": all(t["sheet"] == t["det"] for t in tab.values()),
             "sheet_equals_cp": all(t["sheet"] == t["cp_odd"] for t in tab.values()),
             "mckay_equals_sheet": all(t["sheet"] == t["mckay_sign"] for t in tab.values()),
             "rank_of_the_odd_bits_over_F2": rank2}

# ---- A5 (reading cell)
def chiT(M): return complex(np.trace(TB.conj().T @ M @ TB))
comm_moves = W.ML @ W.MR @ np.linalg.inv(W.ML) @ np.linalg.inv(W.MR)
A5 = {}
for nm, M in (("L", W.ML), ("R", W.MR), ("LR", W.ML @ W.MR), ("the commutator of the moves L R L^-1 R^-1", comm_moves)):
    v = chiT(M); A5[nm] = {"chi_T": [round(v.real, 6), round(v.imag, 6)], "odd_part_Im": round(v.imag, 6), "abs": round(abs(v), 6)}
A5["the puncture loop c = [a, b] (its holonomy on every matter block, from A2)"] = {"is_minus_one": all(A2[f"matter block chi{p} x rho_Q"]["rho_c_is_minus_one"] for p in PAR), "odd_part_Im": 0.0}
out["A5"] = A5
json.dump(out, open(HERE / "observer_on_the_weave.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str))
