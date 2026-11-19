#!/usr/bin/env python3
"""W-R1: mutual reading on the weave's private records. Data-free and exact (sympy, Gaussian rationals).

    python3 -I -u wr1_mutual_reading.py

Card: relays/cards/CHAT1_W-R1_mutual_reading.md (e3771b29e; rewrapped c2eff6ba6; C4 amended f039ca4df), committed
before this script. Every check, prediction and control is the card's.

THE RECORDS. B1675's private modules V_k = ker(H^1(F2; Sym^{2k} rho_Q) -> H^1(<c>; Sym^{2k} rho_Q)) at the common point
rho_Q (a -> i, b -> j), k = 1 to 6, built with this seat's W-C3 code (w34_private_states_amendment_1.py, imported
unchanged): the cocycle space Z^1 = V + V, the coboundaries B^1, the private cocycles K, and the moves' action
(phi^* z)(x) = g^-1 z(phi(x)) with the lift g normalised by det(g)^k. V_k = K / B^1: a complement C of B^1 in K, and
each move's induced matrix A on C (Phi C = C A + B^1 beta, solved exactly).

THE TWO FACTORS, each by its own route.
  St   H^1(F2; C) = Hom(F2, C) in the basis (z(a), z(b)); a move acts by z -> z o phi (its abelianised images).
  M_k  the Q8-fixed vectors of Sym^{2k}, with the move acting by the inverse of its normalised lift (as on the
       coefficients of a cocycle).
CHECKS.
  T0   Hom_G(St (x) M_k, V_k) for G = <L, R, P, -I>: its dimension, and whether a random element of it is invertible
       (P0).
       M_k's character at the identity, at L (a transposition of S3) and at L R (a three-cycle), and its decomposition
       into S3's 1, e (sign) and s (two-dimensional).
  T1   for G = <L, R> and G = <L, R, P, -I>: dim End_G(V_k), dim Hom_G(V_k, V_k'), the invariant bilinear forms
       {W : A_g^T W A'_g = W} with their symmetric and alternating parts and a generic member's rank, the forms that P
       reverses (A_P^T W A'_P = -W) among the <L, R>-invariant ones, and Burnside's dimension on V_k.
  T2   L's and R's fixed spaces on each V_k; where both are lines and V_k has one invariant form W: W(x_L, x_R),
       R1 = W(x_L, R^2 x_L) / W(x_L, R x_L) and R2 = W(x_L, x_R)^2 / (W(x_L, P x_L) W(x_R, P x_R)).
CONTROLS. C1 W-C3's dimensions and kept classes for k <= 3; C2 B1717's End and Hom for V2, V3; C3 End_G(V2 + V2) = 4;
C4 L has no lift at W-C3's random pair.
"""
import itertools
import json
import pathlib
import random
import sys
import time

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "chat1_2026-11-11_wc3"))
import w34_private_states_amendment_1 as W  # noqa: E402  (this seat's W-C3 code; its main is not called)

T0 = time.time()
KS = (1, 2, 3, 4, 5, 6)
RHO = {'a': W.QI, 'b': W.QJ}
GENS_LR = ('L', 'R')
GENS_ALL = ('L', 'R', 'P', '-I')


def say(*a):
    print(*a, flush=True)


def stamp():
    return "[%.0f s]" % (time.time() - T0)


# ---------------- the private modules
def private_module(k):
    dimV, rhoV, B, Res, rhoc = W.block_data(RHO, k)
    Q = rhoc - sp.eye(dimV)
    nsp = sp.Matrix.hstack(Res, -Q).nullspace()
    Kc = sp.Matrix.hstack(*[v[:2 * dimV, :] for v in nsp])
    Kc = sp.Matrix.hstack(*Kc.columnspace())
    Bsp = sp.Matrix.hstack(*B.columnspace())
    comp, cur = [], Bsp
    for j in range(Kc.shape[1]):
        v = Kc[:, j]
        if sp.Matrix.hstack(cur, v).rank() > cur.rank():
            comp.append(v)
            cur = sp.Matrix.hstack(cur, v)
    n = len(comp)
    A, Phi = {}, {}
    if n:
        C = sp.Matrix.hstack(*comp)
        Mbig = sp.Matrix.hstack(C, Bsp)
        for name, phi in W.MOVES.items():
            Ph = W.action_matrix(RHO, rhoV, phi, k, dimV)
            Phi[name] = Ph
            img = Ph * C
            sol, params = Mbig.gauss_jordan_solve(img)
            assert params.shape[0] == 0, (k, name)
            A[name] = sol[:n, :].applyfunc(sp.expand)
    return {"dimV": dimV, "n": n, "A": A, "Phi": Phi, "rhoV": rhoV, "B": Bsp}


def st_matrix(phi):
    rows = []
    for x in ('a', 'b'):
        na = sum(e for g, e in phi[x] if g == 'a')
        nb = sum(e for g, e in phi[x] if g == 'b')
        rows.append([na, nb])
    return sp.Matrix(rows)


def m_module(k):
    """the Q8-fixed vectors of Sym^{2k} and the moves' action on them (the inverse normalised lift)"""
    n = 2 * k
    Si, Sj = W.sym_power(W.QI, n), W.sym_power(W.QJ, n)
    fix = sp.Matrix.vstack(Si - sp.eye(n + 1), Sj - sp.eye(n + 1)).nullspace()
    if not fix:
        return 0, {}
    F = sp.Matrix.hstack(*fix)
    out = {}
    for name, phi in W.MOVES.items():
        g = W.lift(RHO, phi)
        gV = W.sym_power(g, n) / (g.det() ** k)
        img = gV.inv() * F
        sol, params = F.gauss_jordan_solve(img)
        assert params.shape[0] == 0
        out[name] = sol.applyfunc(sp.expand)
    return F.shape[1], out


def kron(A, B):
    blocks = [[A[i, j] * B for j in range(A.shape[1])] for i in range(A.shape[0])]
    return sp.Matrix(sp.BlockMatrix(blocks).as_explicit())


# ---------------- linear algebra of invariants
def solve_space(rows_fn, shape):
    """the space of matrices X (shape) with every rows_fn(X) = 0, as a list of matrices"""
    m, n = shape
    xs = sp.symbols('x0:%d' % (m * n))
    X = sp.Matrix(m, n, xs)
    eqs = []
    for E in rows_fn(X):
        eqs += [e for e in list(E) if e != 0]
    if not eqs:
        return [sp.Matrix(m, n, [1 if t == i else 0 for t in range(m * n)]) for i in range(m * n)]
    Amat, _ = sp.linear_eq_to_matrix(eqs, xs)
    ns = Amat.nullspace()
    return [sp.Matrix(m, n, list(v)) for v in ns]


def hom(Aa, Ab, gens):
    """X: V_a -> V_b with Ab_g X = X Aa_g"""
    na, nb = Aa[gens[0]].shape[0], Ab[gens[0]].shape[0]
    return solve_space(lambda X: [Ab[g] * X - X * Aa[g] for g in gens], (nb, na))


def forms(Aa, Ab, gens, signs=None):
    """W with Aa_g^T W Ab_g = s_g W"""
    na, nb = Aa[gens[0]].shape[0], Ab[gens[0]].shape[0]
    signs = signs or {}
    return solve_space(lambda X: [Aa[g].T * X * Ab[g] - signs.get(g, 1) * X for g in gens], (na, nb))


def generic(space, seed):
    if not space:
        return None
    rng = random.Random(seed)
    return sum((rng.randint(1, 97) * Xm for Xm in space), sp.zeros(*space[0].shape))


def burnside(Amats):
    """the dimension of the algebra the matrices (and their inverses) generate, by an exact incremental echelon"""
    n = Amats[0].shape[0]
    gens = list(Amats) + [M.inv() for M in Amats]
    piv = []

    def reduce(v):
        v = list(v)
        for p, b in piv:
            c = v[p]
            if c != 0:
                v = [sp.expand(x - c * y) for x, y in zip(v, b)]
        return v

    def add(M):
        v = reduce(list(M))
        for i, x in enumerate(v):
            if x != 0:
                piv.append((i, [sp.expand(y / x) for y in v]))
                return True
        return False

    add(sp.eye(n))
    frontier = [sp.eye(n)]
    while frontier and len(piv) < n * n:
        new = []
        for M in frontier:
            for g in gens:
                P_ = (g * M).applyfunc(sp.expand)
                if add(P_):
                    new.append(P_)
        frontier = new
    return len(piv)


def sym_alt(space):
    if not space:
        return 0, 0
    S = [(Xm + Xm.T) for Xm in space]
    Aa = [(Xm - Xm.T) for Xm in space]
    rs = sp.Matrix.hstack(*[Xm.reshape(Xm.shape[0] * Xm.shape[1], 1) for Xm in S]).rank()
    ra = sp.Matrix.hstack(*[Xm.reshape(Xm.shape[0] * Xm.shape[1], 1) for Xm in Aa]).rank()
    return rs, ra


def s3_decomp(chi1, chiL, chiLR):
    # S3: classes id (1), transpositions (3), 3-cycles (2); characters 1 = (1,1,1), e = (1,-1,1), s = (2,0,-1)
    m1 = sp.nsimplify((chi1 + 3 * chiL + 2 * chiLR) / 6)
    me = sp.nsimplify((chi1 - 3 * chiL + 2 * chiLR) / 6)
    ms = sp.nsimplify((2 * chi1 - 2 * chiLR) / 6)
    return m1, me, ms


def main():
    out = {"k": {}}
    say("W-R1: mutual reading on the weave's private records. Exact; data-free.")

    # C4
    rng_np = __import__("numpy").random.default_rng(5)

    def rnd():
        a = sp.Rational(int(rng_np.integers(2, 9)), int(rng_np.integers(2, 9)))
        b = sp.Rational(int(rng_np.integers(1, 9)), int(rng_np.integers(2, 9)))
        c = sp.Rational(int(rng_np.integers(1, 9)), int(rng_np.integers(2, 9)))
        return sp.Matrix([[a, b], [c, (1 + b * c) / a]])
    rho_g = {'a': rnd(), 'b': rnd()}
    try:
        W.lift(rho_g, W.MOVES['L'])
        c4 = False
    except AssertionError:
        c4 = True
    say("C4 holds:", c4, "| L has no lift at W-C3's random pair")

    mods, Ms = {}, {}
    for k in KS:
        mods[k] = private_module(k)
        Ms[k] = m_module(k)
        say("k = %d: dim V = %d, private dim %d, dim M_k %d  %s"
            % (k, mods[k]["dimV"], mods[k]["n"], Ms[k][0], stamp()))
    ST = {name: st_matrix(phi) for name, phi in W.MOVES.items()}
    say("St: " + ", ".join("%s %s" % (nm, list(ST[nm])) for nm in ST))

    # T0 and the M_k decompositions
    t0 = {}
    for k in KS:
        n = mods[k]["n"]
        mdim, MA = Ms[k]
        if n == 0:
            t0[k] = {"n": 0, "m": mdim}
            say("T0 k = %d: no private states; dim M_k = %d" % (k, mdim))
            continue
        chi1 = mdim
        chiL = sp.nsimplify(sp.simplify(MA['L'].trace()))
        chiLR = sp.nsimplify(sp.simplify((MA['L'] * MA['R']).trace()))
        dec = s3_decomp(chi1, chiL, chiLR)
        SM = {g: kron(ST[g], MA[g]) for g in GENS_ALL}
        H = hom(SM, mods[k]["A"], GENS_ALL)
        X = generic(H, 7 + k)
        inv = X is not None and X.shape[0] == X.shape[1] and sp.simplify(X.det()) != 0
        t0[k] = {"n": n, "m": mdim, "chi": [str(chi1), str(chiL), str(chiLR)],
                 "M_k (1, e, s)": [str(d) for d in dec], "dim Hom(St x M, V)": len(H), "invertible": bool(inv)}
        say("T0 k = %d: chi_M (id, L, LR) = (%s, %s, %s), M_k = %s 1 + %s e + %s s; dim Hom_G(St (x) M_k, V_k) = %d,"
            " invertible: %s  %s" % (k, chi1, chiL, chiLR, dec[0], dec[1], dec[2], len(H), inv, stamp()))
    p0 = all(v.get("invertible", True) for v in t0.values())
    say("P0 holds:", p0)
    out["T0"] = {str(k): v for k, v in t0.items()}

    # T1
    nz = [k for k in KS if mods[k]["n"] > 0]
    T1 = {}
    for gname, gens in (("<L,R>", GENS_LR), ("<L,R,P,-I>", GENS_ALL)):
        for k in nz:
            A = mods[k]["A"]
            e = len(hom(A, A, gens))
            fs = forms(A, A, gens)
            rs, ra = sym_alt(fs)
            Wg = generic(fs, 11 + k)
            rank = Wg.rank() if Wg is not None else 0
            rev = forms(A, A, GENS_LR + ('P',), {'P': -1}) if gname == "<L,R>" else []
            bd = burnside([A[g] for g in gens])
            T1[(gname, k, k)] = {"End": e, "forms": len(fs), "symmetric": rs, "alternating": ra, "rank": rank,
                                 "P_reverses": len(rev), "burnside": bd}
            say("T1 %-10s V_%d: End %d; invariant forms %d (symmetric %d, alternating %d, a generic one's rank %d);"
                " forms P reverses %s; Burnside %d  %s"
                % (gname, k, e, len(fs), rs, ra, rank, len(rev) if gname == "<L,R>" else "-", bd, stamp()))
        for k, kk in itertools.combinations(nz, 2):
            A, AA = mods[k]["A"], mods[kk]["A"]
            h1, h2 = len(hom(A, AA, gens)), len(hom(AA, A, gens))
            fs = forms(A, AA, gens)
            T1[(gname, k, kk)] = {"Hom": [h1, h2], "forms": len(fs)}
            say("T1 %-10s V_%d, V_%d: Hom %d, %d; invariant forms between them %d" % (gname, k, kk, h1, h2, len(fs)))
    out["T1"] = {"%s|%d|%d" % key: v for key, v in T1.items()}

    # predictions P1 and P2 (as the card states them)
    pred_end = {2: 1, 3: 1, 4: 2, 5: 1, 6: 3}
    pred_hom = {}
    for k, kk in itertools.combinations(nz, 2):
        s_ = {2, 4, 5, 6}
        pred_hom[(k, kk)] = 2 if (k, kk) == (4, 6) else (1 if (k in s_ and kk in s_) or (k, kk) == (3, 6) else 0)
    pred_burn = {2: 16, 3: 4, 4: 20, 5: 16, 6: 24}
    p1 = all(T1[("<L,R>", k, k)]["End"] == pred_end[k] and T1[("<L,R,P,-I>", k, k)]["End"] == pred_end[k] for k in nz) \
        and all(T1[(g, k, kk)]["Hom"] == [pred_hom[(k, kk)]] * 2 for g in ("<L,R>", "<L,R,P,-I>")
                for k, kk in itertools.combinations(nz, 2))
    p2 = all(T1[("<L,R>", k, k)]["forms"] == pred_end[k] and T1[("<L,R>", k, k)]["symmetric"] == 0
             and T1[("<L,R>", k, k)]["alternating"] == pred_end[k] and T1[("<L,R>", k, k)]["P_reverses"] == pred_end[k]
             and T1[("<L,R,P,-I>", k, k)]["forms"] == 0 for k in nz) \
        and all(T1[("<L,R>", k, kk)]["forms"] == pred_hom[(k, kk)] and T1[("<L,R,P,-I>", k, kk)]["forms"] == 0
                for k, kk in itertools.combinations(nz, 2))
    p2nd = all(T1[("<L,R>", k, k)]["rank"] == mods[k]["n"] for k in (2, 3, 5))
    burn = all(T1[("<L,R>", k, k)]["burnside"] == pred_burn[k] for k in nz)
    say("P1 holds:", p1, "| P2 holds:", p2, "| non-degenerate where M_k is irreducible:", p2nd,
        "| Burnside as predicted:", burn)

    # T2
    T2 = {}
    for k in nz:
        A = mods[k]["A"]
        n = mods[k]["n"]
        fL = (A['L'] - sp.eye(n)).nullspace()
        fR = (A['R'] - sp.eye(n)).nullspace()
        fP = (A['P'] - sp.eye(n)).nullspace()
        T2[k] = {"fix_L": len(fL), "fix_R": len(fR), "fix_P": len(fP)}
        fs = forms(A, A, GENS_LR)
        if len(fL) == 1 and len(fR) == 1 and len(fs) == 1:
            Wf = fs[0]
            xL, xR = fL[0], fR[0]
            B = lambda u, v: sp.simplify((u.T * Wf * v)[0, 0])
            bLR = B(xL, xR)
            r1 = sp.simplify(B(xL, A['R'] ** 2 * xL) / B(xL, A['R'] * xL))
            r2 = sp.simplify(bLR ** 2 / (B(xL, A['P'] * xL) * B(xR, A['P'] * xR)))
            T2[k].update({"W(xL,xR) nonzero": bool(bLR != 0), "R1": str(r1), "R2": str(r2)})
        say("T2 V_%d: L keeps %d, R keeps %d, P keeps %d%s" % (
            k, len(fL), len(fR), len(fP),
            "; W(x_L, x_R) %s, R1 = %s, R2 = %s" % ("non-zero" if T2[k].get("W(xL,xR) nonzero") else "zero",
                                                    T2[k]["R1"], T2[k]["R2"]) if "R1" in T2[k] else ""))
    pred_fixL = {1: 0, 2: 1, 3: 0, 4: 2, 5: 1, 6: 2}
    p3 = all(T2[k]["fix_L"] == pred_fixL[k] and T2[k]["fix_R"] == pred_fixL[k] for k in nz) \
        and all(T2[k].get("W(xL,xR) nonzero") and sp.sympify(T2[k]["R1"]) == -4 and sp.sympify(T2[k]["R2"]) == -1
                for k in (2, 5))
    say("P3 holds:", p3)
    out["T2"] = {str(k): v for k, v in T2.items()}

    # controls
    c1 = [mods[k]["n"] for k in (1, 2, 3)] == [0, 4, 2] and \
        [(T2[k]["fix_L"], T2[k]["fix_R"], T2[k]["fix_P"]) for k in (2, 3)] == [(1, 1, 2), (0, 0, 1)]
    c2 = T1[("<L,R>", 2, 2)]["End"] == 1 and T1[("<L,R>", 3, 3)]["End"] == 1 and T1[("<L,R>", 2, 3)]["Hom"] == [0, 0]
    A2 = mods[2]["A"]
    D = {g: sp.diag(A2[g], A2[g]) for g in GENS_LR}
    c3 = len(hom(D, D, GENS_LR)) == 4
    say("C1 holds:", c1, "| C2 holds:", c2, "| C3 holds:", c3, "| C4 holds:", c4)
    out["verdicts"] = {"P0": p0, "P1": p1, "P2": p2, "P2_nondegenerate": p2nd, "burnside": burn, "P3": p3,
                       "C1": c1, "C2": c2, "C3": c3, "C4": c4}
    json.dump(out, open(HERE / "wr1_summary.json", "w"), indent=1, default=str)
    say("done", stamp())


if __name__ == "__main__":
    main()
