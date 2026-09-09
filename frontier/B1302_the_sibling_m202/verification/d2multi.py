"""B1302 Q2: T-ONE-CUSP-INDEX on a manifold with SEVERAL boundary tori. Same derivation with the boundary sums: t_k = sum_i t_k^(i),
r1 = rank of the restriction Z^1(M;V) -> (+)_i H^1(T_i;V); I = (a0 - a0*) + t0* - r1; annihilator r1 + r1* = t1."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "B1297_the_spectral_cover_index", "verification"))
import d2lib as L
from d2lib import ONE, ZERO
TORUS = L.Presentation(["m", "l"], [[("m", 1), ("l", 1), ("m", -1), ("l", -1)]])
def restriction_multi(pres, rep, cusps):
    n = rep.dim; N = n * len(pres.gens)
    coh = L.cohomology_dims(pres, rep); d1 = coh["d1"]
    _, Z1 = L.rref_rank_null(d1)
    ResZ = None; B1T = None; t0 = t1 = t2 = 0
    for m, l in cusps:
        blocks = []
        for w in (m, l):
            D = L.fox(rep, w, pres.gens); blocks.append([D[g] for g in pres.gens])
        Res = L.kron_block(blocks)
        crep = L.Rep({"m": rep(m), "l": rep(l)}); cd0, cd1 = L.cochain_maps(TORUS, crep)
        tc = L.cohomology_dims(TORUS, crep); t0 += tc["h0"]; t1 += tc["h1"]; t2 += tc["h2"]
        RZ = L.mmul(Res, L.cols_from_vectors(Z1, N)) if Z1 else [[] for _ in range(2 * n)]
        # stack cusps vertically: rows = 2n per cusp; ResZ columns = Z1 basis; B1T block-diagonal
        if ResZ is None: ResZ, B1T = RZ, cd0
        else:
            ResZ = ResZ + RZ
            top = [r + [ZERO] * n for r in B1T]; bot = [[ZERO] * (len(B1T[0])) + r for r in cd0]; B1T = top + bot
    rB = L.rank(B1T); r1 = L.rank(L.hstack(ResZ, B1T)) - rB
    return dict(a0=coh["h0"], a1=coh["h1"], a2=coh["h2"], t0=t0, t1=t1, t2=t2, r1=r1)
def index_multi(pres, mats, cusps):
    V = L.Rep(mats); Vd = L.Rep(L.dual_rep(mats))
    A = restriction_multi(pres, V, cusps); B = restriction_multi(pres, Vd, cusps)
    I = (A["a0"] - B["a0"]) + B["t0"] - A["r1"]; F = A["a1"] - B["a1"]
    checks = dict(annihilator=(A["r1"] + B["r1"] == A["t1"]), t1_split=(A["t1"] == A["t0"] + B["t0"]),
                  F_formula=(F == (A["a0"] - B["a0"]) + A["r1"] - A["t0"]), euler_M=(A["a0"] - A["a1"] + A["a2"] == 0), euler_T=(A["t0"] - A["t1"] + A["t2"] == 0))
    return dict(V=A, Vstar=B, I=I, F=F, checks=checks)
