#!/usr/bin/env python3
"""B1535 -- THE CAP, route E: Theorem C's identities for sm:B1515's frame on any presentation with one cusp subgroup, exact over
K = Q(zeta_24) with sm:B1530's exact_lib (banked; its class_index asserts B1297's identity, the annihilator identity and sm:B1527's
Lemma E at every call).  Nothing is computed on import.

For an extension 0 -> S -> E -> Q -> 0 (S the first dS coordinates), the long exact sequences on M and on the cusp P give, from
dimensions alone:
    rk d0   = h0(S) + h0(Q) - h0(E)
    rk d1   = h1(S) + h1(Q) - h1(E) - rk d0
    rk d0_P = t0(S) + t0(Q) - t0(E)                   (t0 = h0 on P)
and Lemma E gives I(E) = I(S) + I(Q) + (rk d1_E - rk d1_E*) + (rk d0_E* - rk d0_E) + (rk d0_P,E - rk d0_P,E*).

Theorem C (PREREGISTRATION section 3), at a finite-order member and any class, for the frame's four modules
(E = W (x) chi, E* its dual, L2 = Lambda^2 W (x) chi, L2* its dual; on E: V = nu chi rho, L = nu^-4 chi; on L2: S_2 = nu^2 chi
Lambda^2 rho, Q_2 = nu^-3 chi rho -- the twist multiplies Lambda^2 W, it is not squared):
    I(S) = I(Q) = 0 for every piece (unitary pieces, sm:B1515 Lemma 2);
    Lambda^2:  rk d0 = rk d0* = 0;  rk d1_L2 = 0;  rk d0_P,L2* = 0;  k := rk d0_P,L2;
               I(L2) = k - rk d1_L2*,  with  k <= rk d1_L2* <= k + n(Q_2*);  so  -n(Q_2*) <= I(L2) <= 0;
    W:         rk d0_E* = 0;  rk d0_P,E* = 0;  rk d0_P,E = k;  rk d1_E <= n(V);  rk d1_E* <= k + n(L);
               I(E) = -b0 + k + rk d1_E - rk d1_E*,  b0 = rk d0_E;  so  I(E) >= -b0 - n(L).
An independent rank: d1 read directly as a matrix (the S-part of the Fox coboundary of a lifted Q-cocycle, paired with the
annihilator of im d1_S), compared with the rank from the dimensions."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1530V = ROOT / "frontier" / "B1530_the_interior_extensions" / "verification"
if str(B1530V) not in sys.path:
    sys.path.insert(0, str(B1530V))
import exact_lib as E  # noqa: E402

PAIRS5 = E.wedge_index(5)                                   # exact_lib's wedge2 basis order on Lambda^2 of a 5-dim module
SUB2 = [a for a, (i, j) in enumerate(PAIRS5) if j < 4]      # Lambda^2 V
QUO2 = [a for a, (i, j) in enumerate(PAIRS5) if j == 4]     # V wedge e5 = V (x) L


# ============================================================================================ the four modules, submodule first
def permuted(mod, order):
    return E.Module(mod.gens, {g: [[mod.M[g][i][j] for j in order] for i in order] for g in mod.gens})


def blocks(mod, dS):
    """(S, Q) of a block upper-triangular module whose submodule is the first dS coordinates"""
    d = mod.d
    for g in mod.gens:
        for i in range(dS, d):
            for j in range(dS):
                assert mod.M[g][i][j].is_zero(), "not block upper-triangular"
    S = E.Module(mod.gens, {g: [row[:dS] for row in mod.M[g][:dS]] for g in mod.gens})
    Q = E.Module(mod.gens, {g: [row[dS:] for row in mod.M[g][dS:]] for g in mod.gens})
    return S, Q


def four(W, chi=None):
    """the frame's four modules at the term (W (x) chi, Lambda^2 W (x) chi): name -> (module, dS).  The twist multiplies
    Lambda^2 W, not W before the wedge: Lambda^2 (W (x) chi) = Lambda^2 W (x) chi^2 is a different term (Lemma S twists each module
    of the cover by the deck characters)."""
    Wx = W.twist(chi) if chi is not None else W
    L2 = W.wedge2().twist(chi) if chi is not None else W.wedge2()
    return {"E": (Wx, 4),
            "E*": (permuted(Wx.dual(), [4, 0, 1, 2, 3]), 1),
            "L2": (permuted(L2, SUB2 + QUO2), 6),
            "L2*": (permuted(L2.dual(), QUO2 + SUB2), 4)}


# ============================================================================================ the long exact sequences
def _dims(C):
    return {"h0": C.a0, "h1": C.h1, "t0": C.t0, "n": C.n, "r1": C.r1}


def fox_all(G, mod):
    return [E.fox_blocks(mod, r)[0] for r in G.rels]


def annihilator(G, Smod):
    """rows f with f . d1_S = 0: coordinates on H^2(S) = C^2(S) / im d1_S (a presentation 2-complex)"""
    dS = Smod.d
    fox = fox_all(G, Smod)
    cols = []
    for g in G.gens:
        for k in range(dS):
            col = []
            for Kb in fox:
                col += [Kb[g][i][k] for i in range(dS)]
            cols.append(col)
    return E.nullspace(cols, dS * len(G.rels)) if cols else []


def phi(G, mod, dS, y, fox):
    """the S-part of the Fox coboundary of the lift (0, y) of a Q-cocycle y, over every relator"""
    dQ = mod.d - dS
    out = []
    for Kb in fox:
        acc = [E.ZERO] * dS
        for gi, g in enumerate(G.gens):
            yg = y[gi * dQ:(gi + 1) * dQ]
            for j in range(dQ):
                if yg[j].is_zero():
                    continue
                for i in range(dS):
                    acc[i] = acc[i] + Kb[g][i][dS + j] * yg[j]
        out += acc
    return out


def d1_matrix(G, mod, dS, CQ, F=None):
    """d1 : H^1(Q) -> H^2(S) as a matrix (rows: the annihilator's coordinates; columns: CQ's representatives)"""
    S, _ = blocks(mod, dS)
    F = annihilator(G, S) if F is None else F
    fox = fox_all(G, mod)
    cols = [phi(G, mod, dS, y, fox) for y in CQ.reps]
    return [[sum((x * z for x, z in zip(f, v)), E.ZERO) for v in cols] for f in F]


def les(G, mod, dS, direct=True):
    """the dimensions of S, Q, E and the connecting ranks; with direct=True also d1's rank read as a matrix"""
    S, Q = blocks(mod, dS)
    CS, CQ, CE = E.Cohomology(G, S), E.Cohomology(G, Q), E.Cohomology(G, mod)
    s, q, e = _dims(CS), _dims(CQ), _dims(CE)
    rk0 = s["h0"] + q["h0"] - e["h0"]
    rk1 = s["h1"] + q["h1"] - e["h1"] - rk0
    rk0P = s["t0"] + q["t0"] - e["t0"]
    out = {"S": s, "Q": q, "E": e, "rk d0": rk0, "rk d1": rk1, "rk d0_P": rk0P}
    if direct:
        F = annihilator(G, S)
        assert len(F) == s["h1"] - s["h0"], ("Euler characteristic of S", len(F), s)
        M = d1_matrix(G, mod, dS, CQ, F)
        out["rk d1 (matrix)"] = E.rank(M, len(CQ.reps)) if M and CQ.reps else 0
        out["h2(S)"] = len(F)
    return out


# ============================================================================================ the cap at one module W (x) chi
def reading(G, W, chi=None, direct=True):
    """Theorem C's quantities and identities at the term (W1(c) (x) chi, Lambda^2 W1(c) (x) chi); asserts nothing, returns the
    checks"""
    mods = four(W, chi)
    L = {nm: les(G, md, dS, direct) for nm, (md, dS) in mods.items()}
    idx = {nm: E.class_index(G, md)["I"] for nm, (md, dS) in mods.items()}
    assert idx["E*"] == -idx["E"] and idx["L2*"] == -idx["L2"], ("the dual's index", idx)
    pieces = {}
    for nm, (md, dS) in mods.items():
        S, Q = blocks(md, dS)
        pieces[nm] = (E.class_index(G, S)["I"], E.class_index(G, Q)["I"])
    if direct:
        for nm in L:
            assert L[nm]["rk d1 (matrix)"] == L[nm]["rk d1"], ("d1's rank, matrix against dimensions", nm, L[nm])
    # Lemma E, assembled from the pieces (sm:B1527), for both W and Lambda^2 W
    for a, b in (("E", "E*"), ("L2", "L2*")):
        lhs = idx[a]
        rhs = (pieces[a][0] + pieces[a][1] + (L[a]["rk d1"] - L[b]["rk d1"]) + (L[b]["rk d0"] - L[a]["rk d0"]) +
               (L[a]["rk d0_P"] - L[b]["rk d0_P"]))
        assert lhs == rhs, ("Lemma E assembled from the pieces", a, lhs, rhs)
    k = L["L2"]["rk d0_P"]
    nQ2s = L["L2*"]["S"]["n"]                       # the submodule of L2* is (V L)*: n((V L)*)
    nV, nL = L["E"]["S"]["n"], L["E"]["Q"]["n"]
    b0 = L["E"]["rk d0"]
    checks = {
        "I(S) = I(Q) = 0 for every piece": all(p == (0, 0) for p in pieces.values()),
        "L2: rk d0 = rk d0* = 0": L["L2"]["rk d0"] == 0 and L["L2*"]["rk d0"] == 0,
        "L2: rk d1 = 0": L["L2"]["rk d1"] == 0,
        "L2*: rk d0_P = 0": L["L2*"]["rk d0_P"] == 0,
        "I(L2) = k - rk d1(L2*)": idx["L2"] == k - L["L2*"]["rk d1"],
        "k <= rk d1(L2*) <= k + n((VL)*)": k <= L["L2*"]["rk d1"] <= k + nQ2s,
        "W: rk d0(E*) = 0 and rk d0_P(E*) = 0": L["E*"]["rk d0"] == 0 and L["E*"]["rk d0_P"] == 0,
        "W: rk d0_P(E) = k": L["E"]["rk d0_P"] == k,
        "W: rk d1(E) <= n(V)": L["E"]["rk d1"] <= nV,
        "W: rk d1(E*) <= k + n(L)": L["E*"]["rk d1"] <= k + nL,
        "I(E) = -b0 + k + rk d1(E) - rk d1(E*)": idx["E"] == -b0 + k + L["E"]["rk d1"] - L["E*"]["rk d1"],
        "cap: -n((VL)*) <= I(L2) <= 0": -nQ2s <= idx["L2"] <= 0,
        "cap: I(E) >= -b0 - n(L)": idx["E"] >= -b0 - nL,
    }
    return {"I(W)": idx["E"], "I(L2W)": idx["L2"], "k": k, "b0": b0, "n((VL)*)": nQ2s, "n(V)": nV, "n(L)": nL,
            "rk d1": {nm: L[nm]["rk d1"] for nm in L}, "les": L, "pieces": {nm: list(p) for nm, p in pieces.items()},
            "checks": checks, "all": all(checks.values())}
