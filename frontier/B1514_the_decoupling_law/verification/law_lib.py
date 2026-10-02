"""B1514 -- THE DECOUPLING LAW: route T, the relative triple product.  Library; no sealed quantity is computed on import.

The question (B1513 leads 1 and 2).  B1513 found that the projective triplet's chiral 10' does not couple to its own Higgs class.
Is "a chiral state does not couple to a Higgs class of its background" a law of the harmonic frame?  The tower has a second chiral
mechanism, B1511's case (b): a 10bar' per member on M4, M5 and M6 (B1511, B1512).  This library reads those members.

The member (B1511 Section 1).  On G_n = <x, y, t | t g t^-1 = phi^n(g)>, a character nu = (nu_F, lam) with nu_F(x) = zeta_N^a,
nu_F(y) = zeta_N^b and nu(t) = lam.  V = nu (x) rho_q, L = nu^-4 (a line, trivial on the cusp), V_eta = nu^5 (x) rho_q = V (x) L*, c a
class of V_eta, and W1 = [[V, c L], [0, L]]: W1(g) = [[V(g), c(g) L(g)], [0, L(g)]].  x generates H^1(L).
The sectors in B1509's dictionary: the 10bar' with W1, the 10' with W1*, the 5'_H with Lambda^2 W1, the 5bar'_H with Lambda^2 W1*.
The couplings:
  - the 10bar' sector, 10bar'.10bar'.5bar'_H: B'(a, a') = <hbar u a u a'> through (eta, u, v) -> eta(u ^ v) on Lambda^2 W1* (x) W1 (x) W1;
  - the 10' sector, 10'.10'.5'_H: B(f, f') = <h u f u f'> through (omega, f, g) -> (f ^ g)(omega) on Lambda^2 W1 (x) W1* (x) W1*.
Both are B1513's relative triple product (higgs_lib.triple): the first slot is the Higgs class, relative because Lambda^2 W1 and
Lambda^2 W1* are acyclic on the cusp.

This is route T.  Route L (lift_route.py, the lifting criterion on B1513's independent audit) shares no code with it."""
import importlib.util
import sys
from pathlib import Path

import flint
import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
VER13 = ROOT / "frontier/B1513_the_triplets_higgs_sector/verification"
sys.path.insert(0, str(VER13))
import higgs_lib as H  # noqa: E402

T = H.T
q = T.Q
B1512_RUN = ROOT / "frontier/B1512_the_self_coincident_orbits/verification/census_run.txt"
B1511_RUN = ROOT / "frontier/B1511_the_projective_tower/verification/tower_census_run.txt"


# ============================================================================================ the members
def reduce_char(ab, N):
    """(a, b) mod N -> the same character with N its exact order"""
    from math import gcd
    g = gcd(gcd(ab[0] % N, ab[1] % N), N)
    return (ab[0] % N // g, ab[1] % N // g), N // g


def pw(dom, v, k):
    r = dom.one
    if k < 0:
        v, k = dom.one / v, -k
    for _ in range(k):
        r = r * v
    return r


def line(G, dom, vals):
    return H.Module(G, {g: DomainMatrix([[vals[g]]], (1, 1), dom) for g in G.gens})


def twisted(G, rho, vals):
    return H.Module(G, {g: rho[g] * vals[g] for g in G.gens})


class Member:
    """one case-(b) member: the modules, the classes c and x, and W1"""

    def __init__(self, G, field, rho, ab, N, lam, c_coeffs=None):
        (a, b), Nr = reduce_char(ab, N)
        dom = field.dom
        self.G, self.field, self.dom = G, field, dom
        self.nu = {"x": field.unit(a, Nr), "y": field.unit(b, Nr), "t": lam}
        self.char = ((a, b), Nr)
        self.V = twisted(G, rho, self.nu)
        self.Lv = {g: pw(dom, v, -4) for g, v in self.nu.items()}
        self.L = line(G, dom, self.Lv)
        self.Veta = twisted(G, rho, {g: pw(dom, v, 5) for g, v in self.nu.items()})
        self.VL = twisted(G, rho, {g: pw(dom, v, -3) for g, v in self.nu.items()})          # V (x) L = nu^-3 rho
        self.c_basis, self.h1_Veta = H.h1_basis(self.Veta)
        self.x_basis, self.h1_L = H.h1_basis(self.L)
        if c_coeffs is None:
            self.c = self.c_basis[0]
        else:
            k1, k2 = (dom.convert(sp.Integer(k)) if not hasattr(k, "parent") else k for k in c_coeffs)
            self.c = H.Cocycle(self.Veta, {g: self.c_basis[0].v[g] * k1 + self.c_basis[1].v[g] * k2 for g in G.gens})
        self.x = self.x_basis[0]
        mats = {}
        for g in G.gens:
            Lg = DomainMatrix([[self.Lv[g]]], (1, 1), dom)
            top = self.V.rep.M[g].hstack(self.c.v[g] * Lg)
            bot = DomainMatrix.zeros((1, 4), dom).hstack(Lg)
            mats[g] = top.vstack(bot)
        self.W1 = H.Module(G, mats)
        self.W1d = self.W1.dual()
        self.L2W = self.W1.wedge2()
        self.L2Wd = self.W1d.wedge2()
        self.L2V = self.V.wedge2()


def h_data(mod):
    """(h0, h1, h2) on G_n (chi = 0, so h2 = h1 - h0)"""
    a0, a1, *_ = H.cohomology_data(mod)
    return {"h0": a0, "h1": a1, "h2": a1 - a0}


def cusp_acyclic(mod):
    """no eigenvalue 1 on the longitude: H*(cusp torus; mod) = 0"""
    I = DomainMatrix.eye(mod.d, mod.dom)
    return T.dm_rank(mod.rho(H.ELL) - I) == mod.d


# ============================================================================================ the couplings
def coupling_tensor(G, C, z, higgs_mod, slot_mod, form):
    """Y(h, a_i, a_j) for h in a basis of H^1(higgs_mod) and a_i, a_j in a basis of H^1(slot_mod)"""
    hs, _ = H.h1_basis(higgs_mod)
    As, _ = H.h1_basis(slot_mod)
    return [[[H.triple(G, C, z, h, ai, aj, form) for aj in As] for ai in As] for h in hs], len(hs), len(As)


def all_zero(tensor, dom):
    return all(v == dom.zero for M in tensor for row in M for v in row)


def symmetric(tensor):
    return all(M[i][j] == M[j][i] for M in tensor for i in range(len(M)) for j in range(len(M)))


def control_triple(G, C, z, mem):
    """the positive control <y u x u c> for y in a basis of H^1(V*) (relative), through (phi, s, w) -> s phi(w): non-zero iff
    x u c != 0 in H^2(V) (duality; V* is acyclic on the cusp), which is B1511 Theorem A's firing condition"""
    ys, _ = H.h1_basis(mem.V.dual())
    form = H.form_permuted(H.form_line_pairing(), (2, 1, 0))
    return [H.triple(G, C, z, y, mem.x, mem.c, form) for y in ys]


def interior_count(mod):
    return len(H.interior_classes(mod))


# ============================================================================================ invariant forms (flint, GF(p))
def nmod_of(M, p):
    return flint.nmod_mat(M.shape[0], M.shape[1], [int(M[i, j].element) % p for i in range(M.shape[0]) for j in range(M.shape[1])], p)


def kron(A, B, p):
    a, b = A.nrows(), B.nrows()
    return flint.nmod_mat(a * b, a * b, [int(A[i1, j1]) * int(B[i2, j2]) % p for i1 in range(a) for i2 in range(b)
                                         for j1 in range(a) for j2 in range(b)], p)


def form_space(Wk, Wi, Wj, p):
    """invariant trilinear forms on Lambda^2 Wk* (x) Wi (x) Wj = invariant vectors of Lambda^2 Wk (x) Wi* (x) Wj* (dual action):
    returns (dimension, basis as lists of 250 residues in the order (pair of Wk, index of Wi, index of Wj))"""
    L2 = Wk.wedge2()
    blocks = []
    for g in Wk.G.gens:
        A = nmod_of(L2.rep.M[g], p)
        Bi = nmod_of(T.dm_inv(Wi.rep.M[g]).transpose(), p)
        Bj = nmod_of(T.dm_inv(Wj.rep.M[g]).transpose(), p)
        Kr = kron(kron(A, Bi, p), Bj, p)
        nn = Kr.nrows()
        blocks.append([[(int(Kr[a, b]) - (1 if a == b else 0)) % p for b in range(nn)] for a in range(nn)])
    nn = len(blocks[0])
    stacked = flint.nmod_mat(3 * nn, nn, [x for B in blocks for row in B for x in row], p)
    X, nullity = stacked.nullspace()
    basis = [[int(X[r, c]) for r in range(nn)] for c in range(nullity)]
    return nullity, basis


def form_from_vector(vec, dom):
    """the trilinear form (eta, u, v) -> sum vec[(P, i, j)] eta_P u_i v_j on Lambda^2 W* (x) W (x) W"""
    vals = [dom.convert(sp.Integer(v)) for v in vec]

    def F(eta, u, v):
        e, uu, vv = eta.to_list(), u.to_list(), v.to_list()
        tot = dom.zero
        idx = 0
        for P in range(10):
            for i in range(5):
                for j in range(5):
                    c = vals[idx]
                    idx += 1
                    if c != dom.zero:
                        tot += c * e[P][0] * uu[i][0] * vv[j][0]
        return tot
    return F


# ============================================================================================ the populations (banked records)
def populations():
    """the case-(b) members through level 6, read from B1511's and B1512's records: a list of
    {level, label, orbits: {name: [(a, b), ...]}, N, lam, factor}"""
    import json
    out = []
    r11 = json.loads(B1511_RUN.read_text(encoding="utf-8"))
    for orb in r11["C1"]["4"]:
        if orb["lam"] != "1":
            continue
        for f in orb["factors"]:
            if f["factor"] == "q**2 - 7*q + 1":
                out.append({"level": 4, "label": f"M4 orbit {orb['orbit'][0]}", "orbits": {str(orb["orbit"][0]): [tuple(m) for m in orb["orbit"]]},
                            "N": 15, "lam": "1", "factor": f["factor"]})
    r12 = json.loads(B1512_RUN.read_text(encoding="utf-8"))
    classes = {}
    for lev in ("level_5", "level_6"):
        for cl in r12["A"]["classes"][lev]["classes"]:
            classes[(int(lev[-1]), tuple(cl["orbits"]))] = ({str(m["orbit_index"]): [tuple(x) for x in m["orbit"]] for m in cl["members"]},
                                                             r12["A"]["classes"][lev]["N"])
    for d in r12["D"]:
        key = (int(d["level"]), tuple(d["class_orbits"]))
        orbits, N = classes[key]
        out.append({"level": int(d["level"]), "label": f"M{d['level']} {list(key[1])} lam = {d['lam']}", "orbits": orbits, "N": N,
                    "lam": d["lam"], "factor": d["factor"], "banked_h1": d["h1 (L, V_nu, V_eta, V_eta*) values"]})
    return out


def lam_value(field, lam):
    dom = field.dom
    if lam == "1":
        return dom.one
    if lam == "-1":
        return -dom.one
    if field.kind == "gf":
        i = field.iota
        assert i is not None
        return dom(i if lam == "i" else (-i) % field.p)
    return field.unit(1 if lam == "i" else 3, 4)
