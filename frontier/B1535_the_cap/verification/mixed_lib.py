#!/usr/bin/env python3
"""B1535 -- the covers' own classes at a pulled-back member, route Ind (exact over K = Q(zeta_24)).  Nothing is computed on import.

A finite regular abelian cover p: M_A -> M is given by its deck characters B, a finite group of characters of pi_1 M (labels
(w0, w1; k): fibre part w, value e^{2 pi i k} at t').  At a member nu, the cover's class space is
    H^1(M_A; p*(nu^5 (x) rho)) = (+)_{chi in B} H^1(M; nu^5 chi (x) rho)            (Shapiro),
so a class is c_A = sum_chi c_chi; it is pulled back from M exactly when only c_1 is non-zero.  The induced module of the cover's
frame W_A = [[p*V, c_A p*L], [0, p*L]] (V = nu rho, L = nu^-4) is the circulant extension on M
    Ind W_A:          (+)_psi L psi  by  (+)_psi V psi,       block psi -> psi':  g -> c_{psi'/psi}(g) L(g) psi(g),
    Ind Lambda^2 W_A: (+)_psi V L psi by (+)_psi Lambda^2 V psi, block psi -> psi': g -> [v -> A(g) v ^ c_{psi'/psi}(g) L(g)] psi(g),
with A = V(g).  Both are representations exactly when each c_chi is a cocycle of nu^5 chi rho (checked on every relator).  Then
I_{M_A}(W_A) = I_M(Ind W_A) and I_{M_A}(Lambda^2 W_A) = I_M(Ind Lambda^2 W_A) (Shapiro and Mackey; sm:B1532's Lemma S), and
Theorem C's identities are read on these two modules and their duals exactly as cap_lib reads them on one term."""
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1534V = ROOT / "frontier" / "B1534_the_silver_covers" / "verification"
for p in (HERE, B1534V):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
import cap_lib as CL  # noqa: E402
import silver_lib as SL  # noqa: E402

E = CL.E


# ============================================================================================ labels and the group B
def lab(w0, w1, k):
    return (Fraction(w0) % 1, Fraction(w1) % 1, Fraction(k) % 1)


def ladd(x, y, s=1):
    return tuple((a + s * b) % 1 for a, b in zip(x, y))


def chardict(st, x):
    return SL.char(st, (x[0], x[1]), x[2])


def closure(gens):
    out = {lab(0, 0, 0)}
    frontier = list(out)
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = ladd(x, g)
                if y not in out:
                    out.add(y)
                    new.append(y)
        frontier = new
    return sorted(out)


# ============================================================================================ the circulant modules
def ind_modules(st, nu_lab, B, comps):
    """(Ind W_A, Ind Lambda^2 W_A) on M for the member nu (label), deck characters B (labels, a group) and class components
    comps[chi] (a cocycle of nu^5 chi rho, concatenated over the generators, or None)"""
    G = st["G"]
    gens, ng = G.gens, len(G.gens)
    ch = chardict(st, nu_lab)
    V = st["rho"].twist(ch)
    Lc = SL.S.power_char(ch, -4)
    psi = [chardict(st, x) for x in B]
    m = len(B)
    idx = {x: i for i, x in enumerate(B)}
    W, L2 = {}, {}
    pairs4 = E.wedge_index(4)
    for gi, g in enumerate(gens):
        A, ell = V.M[g], Lc[g]
        A2 = E.wedge2(A)
        Wg = E.zeros(5 * m, 5 * m)
        Lg = E.zeros(10 * m, 10 * m)
        for i, x in enumerate(B):
            pg = psi[i][g]
            for a in range(4):
                for b in range(4):
                    Wg[4 * i + a][4 * i + b] = A[a][b] * pg
                    Lg[6 * m + 4 * i + a][6 * m + 4 * i + b] = A[a][b] * ell * pg
            Wg[4 * m + i][4 * m + i] = ell * pg
            for a in range(6):
                for b in range(6):
                    Lg[6 * i + a][6 * i + b] = A2[a][b] * pg
        for j, y in enumerate(B):                      # source psi_j (quotient), target psi_i (sub), chi = psi_i / psi_j
            pg = psi[j][g]
            for i, x in enumerate(B):
                z = comps.get(ladd(x, y, -1))
                if z is None:
                    continue
                zg = [z[gi * 4 + a] * ell for a in range(4)]
                for a in range(4):
                    Wg[4 * i + a][4 * m + j] = zg[a] * pg
                for b in range(4):
                    col = E.wedge_vec([A[r][b] for r in range(4)], zg)
                    for a in range(6):
                        Lg[6 * i + a][6 * m + 4 * j + b] = col[a] * pg
        W[g], L2[g] = Wg, Lg
    MW, ML = E.Module(gens, W), E.Module(gens, L2)
    assert MW.check(G.rels), "Ind W_A is not a representation"
    assert ML.check(G.rels), "Ind Lambda^2 W_A is not a representation"
    assert len(pairs4) == 6
    return MW, ML


def ind_four(MW, ML, m):
    """the four modules of Theorem C at a cover, submodule first"""
    return {"E": (MW, 4 * m),
            "E*": (CL.permuted(MW.dual(), list(range(4 * m, 5 * m)) + list(range(4 * m))), m),
            "L2": (ML, 6 * m),
            "L2*": (CL.permuted(ML.dual(), list(range(6 * m, 10 * m)) + list(range(6 * m))), 4 * m)}


def reading_mods(G, mods, direct=True):
    """cap_lib.reading's quantities and identities on four given modules (name -> (module, dS))"""
    L = {nm: CL.les(G, md, dS, direct) for nm, (md, dS) in mods.items()}
    idx = {nm: E.class_index(G, md)["I"] for nm, (md, dS) in mods.items()}
    pieces = {}
    for nm, (md, dS) in mods.items():
        S, Q = CL.blocks(md, dS)
        pieces[nm] = (E.class_index(G, S)["I"], E.class_index(G, Q)["I"])
    k = L["L2"]["rk d0_P"]
    nQ2s = L["L2*"]["S"]["n"]
    nV, nL = L["E"]["S"]["n"], L["E"]["Q"]["n"]
    b0 = L["E"]["rk d0"]
    lemma_e = {}
    for a, b in (("E", "E*"), ("L2", "L2*")):
        lemma_e[a] = idx[a] == (pieces[a][0] + pieces[a][1] + (L[a]["rk d1"] - L[b]["rk d1"]) +
                                (L[b]["rk d0"] - L[a]["rk d0"]) + (L[a]["rk d0_P"] - L[b]["rk d0_P"]))
    checks = {
        "the duals' indices": idx["E*"] == -idx["E"] and idx["L2*"] == -idx["L2"],
        "d1: matrix = dimensions": (not direct) or all(L[nm]["rk d1 (matrix)"] == L[nm]["rk d1"] for nm in L),
        "Lemma E assembled from the pieces": all(lemma_e.values()),
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
            "rk d1": {nm: L[nm]["rk d1"] for nm in L}, "checks": checks, "all": all(checks.values())}


def ind_reading(st, nu_lab, B, comps, direct=True):
    MW, ML = ind_modules(st, nu_lab, B, comps)
    return reading_mods(st["G"], ind_four(MW, ML, len(B)), direct)


# ============================================================================================ the class spaces
def components(st, nu_lab, B):
    """for each chi in B: the Cohomology of nu^5 chi rho (its h^1, interior basis and representatives)"""
    ch = chardict(st, nu_lab)
    out = {}
    for x in B:
        Veta = st["rho"].twist(SL.S.power_char(ch, 5)).twist(chardict(st, x))
        C = E.Cohomology(st["G"], Veta)
        out[x] = C
    return out


def combo(C, coeffs):
    """the cocycle sum coeffs_i reps_i of a Cohomology C (coeffs in K)"""
    return C.combine([E.K.of(c) for c in coeffs])


def interior_cocycle(C, coeffs=None):
    """an interior cocycle of C: the combination of C's interior basis with the given coefficients (default all 1)"""
    ints = C.interior()
    if not ints:
        return None
    coeffs = coeffs or [1] * len(ints)
    x = [E.ZERO] * len(C.reps)
    for c, v in zip(coeffs, ints):
        x = [a + E.K.of(c) * b for a, b in zip(x, v)]
    return C.combine(x)
