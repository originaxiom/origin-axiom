#!/usr/bin/env python3
"""B1367 -- THE DOUBLET-TRIPLET PINCER: with E6-symmetric couplings among any number of 27s, every vacuum with a light up-type Higgs
doublet has an equal number of light exotic colour triplets D, and every attempt to lift a D through a nu^c VEV lifts a lepton doublet.

The E6 cubic on the 27 in trinification form, 27 = Q (3, 3bar, 1) + Q^c (3bar, 1, 3) + L (1, 3, 3bar):
    I(Phi) = det L + det Q + det Q^c + sum_{i,a,al} Q[i][a] L[a][al] Q^c[al][i]  (= Tr(Q L Q^c)),
polarised into its symmetric trilinear form d(x, y, z).  With n copies 27_g and an arbitrary symmetric coupling tensor lambda_{ghk},
W = sum lambda_{ghk} d(27_g, 27_h, 27_k) and the mass matrices at a vacuum where only the Standard-Model singlets N_g, nu^c_g have VEVs
are the Hessian M_{AB} = 6 D(e_A, e_B, v).  Computed here for n = 3, 4, 6, for coupling tensors of several patterns (the deck's hollow
pattern, generic, diagonal, random masks) and for every support pattern of the VEVs with random complex values:
  * the doublet block (rows H_u; columns H_d, L) and the triplet block (rows D; columns Dbar, d^c) have equal generation-rank,
    so  light H_u doublets = light D triplets  -- the pincer;
  * the lepton block: each nu^c VEV pairs lepton doublets with up-Higgs doublets exactly as it pairs D with d^c.
Usage: python3 pincer.py"""
import itertools, random
import numpy as np
random.seed(7); np.random.seed(7)

# ---------------------------------------------------------------- the 27 in trinification form and the E6 cubic
# slots: L[a][al] (a: SU(3)_L, al: SU(3)_R); Q[i][a]; Qc[al][i].  Standard-Model names from the cubic's own terms (see FINDINGS):
#   L[a][0] = H_u (a<2), L[2][0] = e^c;  L[a][1] = H_d, L[2][1] = nu^c;  L[a][2] = L (lepton doublet), L[2][2] = N;
#   Q[i][a<2] = Q,  Q[i][2] = D;   Qc[0][i] = u^c,  Qc[1][i] = d^c,  Qc[2][i] = Dbar.
def I(Phi):
    Q, Qc, L = Phi
    return np.linalg.det(L) + np.linalg.det(Q) + np.linalg.det(Qc) + np.trace(Q @ L @ Qc)   # sum_{i,a,al} Q[i][a] L[a][al] Qc[al][i]
def add(*Ps):
    return tuple(sum(P[k] for P in Ps) for k in range(3))
def d(x, y, z):
    """the symmetric trilinear form of the cubic I (polarisation identity)"""
    return (I(add(x, y, z)) - I(add(x, y)) - I(add(x, z)) - I(add(y, z)) + I(x) + I(y) + I(z)) / 6
def zero():
    return (np.zeros((3, 3), complex), np.zeros((3, 3), complex), np.zeros((3, 3), complex))
def unit(block, r, c):
    P = zero(); P[block][r, c] = 1.0; return P
# field slots (block, row, col) for the doublets and triplets
Hu = [(2, a, 0) for a in range(2)]; Hd = [(2, a, 1) for a in range(2)]; Ld = [(2, a, 2) for a in range(2)]
Dq = [(0, i, 2) for i in range(3)]; Dbar = [(1, 2, i) for i in range(3)]; dc = [(1, 1, i) for i in range(3)]
Nslot = (2, 2, 2); nuslot = (2, 2, 1)
# sanity: the cubic's own pairings -- N H_u H_d, N D Dbar, nu^c L H_u, nu^c D d^c are the non-zero couplings among these slots
def coup(A, B, C):
    return d(unit(*A), unit(*B), unit(*C))
print("=== the E6 cubic's pairings (d(e_A, e_B, e_C) on unit slots) ===")
print(f"  N H_u^1 H_d^2 = {coup(Nslot, Hu[0], Hd[1]):+.3f}, N H_u^2 H_d^1 = {coup(Nslot, Hu[1], Hd[0]):+.3f}, N H_u^1 L^2 = {coup(Nslot, Hu[0], Ld[1]):+.3f} (N pairs H_u with H_d, not with L)")
print(f"  N D_1 Dbar_1 = {coup(Nslot, Dq[0], Dbar[0]):+.3f}, N D_1 d^c_1 = {coup(Nslot, Dq[0], dc[0]):+.3f} (N pairs D with Dbar)")
print(f"  nu^c L^1 H_u^2 = {coup(nuslot, Ld[0], Hu[1]):+.3f}, nu^c H_d^1 H_u^2 = {coup(nuslot, Hd[0], Hu[1]):+.3f} (nu^c pairs L with H_u)")
print(f"  nu^c D_1 d^c_1 = {coup(nuslot, Dq[0], dc[0]):+.3f}, nu^c D_1 Dbar_1 = {coup(nuslot, Dq[0], Dbar[0]):+.3f} (nu^c pairs D with d^c)")

# ---------------------------------------------------------------- n copies, coupling tensors, vacua, Hessians
# structure constants of the cubic on the single-27 slots: S^N_{AB} = d(e_A, e_B, e_N), S^nu_{AB} = d(e_A, e_B, e_nu), computed once
rowsD1 = Hu; colsD1 = Hd + Ld; rowsT1 = Dq; colsT1 = Dbar + dc
def struct(rows, cols, C):
    return np.array([[d(unit(*A), unit(*B), unit(*C)) for B in cols] for A in rows])
SN_D, Snu_D = struct(rowsD1, colsD1, Nslot), struct(rowsD1, colsD1, nuslot)
SN_T, Snu_T = struct(rowsT1, colsT1, Nslot), struct(rowsT1, colsT1, nuslot)
print(f"\nstructure constants: doublet block |S^N| non-zero entries {int((abs(SN_D) > 1e-12).sum())} (N: H_u-H_d), |S^nu| {int((abs(Snu_D) > 1e-12).sum())} (nu^c: H_u-L); "
      f"triplet block |S^N| {int((abs(SN_T) > 1e-12).sum())} (N: D-Dbar), |S^nu| {int((abs(Snu_T) > 1e-12).sum())} (nu^c: D-d^c)")
def hessian_blocks(n, lam, vev):
    """the Hessian blocks for n copies with the symmetric coupling tensor lam and VEVs vev[g] = (N_g, nu_g):
    M_{(g,A),(h,B)} = 6 sum_k lam[g,h,k] (N_k S^N_{AB} + nu_k S^nu_{AB})"""
    Nv = np.array([vev[g][0] for g in range(n)]); nv = np.array([vev[g][1] for g in range(n)])
    G = 6 * (np.einsum('ghk,k->gh', lam, Nv)); Gn = 6 * (np.einsum('ghk,k->gh', lam, nv))
    MD = np.kron(G, SN_D) + np.kron(Gn, Snu_D)
    MT = np.kron(G, SN_T) + np.kron(Gn, Snu_T)
    return MD, MT
def rank(M, tol=1e-9):
    return int(np.linalg.matrix_rank(M, tol=tol))
def patterns(n):
    yield "hollow", np.array([[[1.0 if len({g, h, k}) == 3 else 0.0 for k in range(n)] for h in range(n)] for g in range(n)])
    yield "generic", (lambda T: (T + T.transpose(1, 0, 2) + T.transpose(0, 2, 1) + T.transpose(1, 2, 0) + T.transpose(2, 0, 1) + T.transpose(2, 1, 0)))(np.random.randn(n, n, n) + 1j * np.random.randn(n, n, n))
    yield "diagonal", np.array([[[1.0 if g == h == k else 0.0 for k in range(n)] for h in range(n)] for g in range(n)])
    for m in range(12):
        T = np.zeros((n, n, n))
        for g in range(n):
            for h in range(g, n):
                for k in range(h, n):
                    if random.random() < 0.5:
                        val = random.choice([1.0, -1.0, 0.5, 2.0])
                        for p in set(itertools.permutations((g, h, k))): T[p] = val
        yield f"mask{m}", T
print("\n=== the pincer over n copies, coupling patterns and every VEV support ===")
summary = {}
worst = None
for n in (3, 4, 6):
    tot = 0; viol = 0; withHu = 0; minD = None; lepton_ok = 0
    for name, lam in patterns(n):
        supports = list(itertools.product([0, 1], repeat=2 * n)) if n <= 4 else [tuple(random.randint(0, 1) for _ in range(2 * n)) for _ in range(300)]
        for sup in supports:
            vev = {g: ((np.random.randn() + 1j * np.random.randn()) * sup[2 * g], (np.random.randn() + 1j * np.random.randn()) * sup[2 * g + 1]) for g in range(n)}
            MD, MT = hessian_blocks(n, lam, vev)
            rD, rT = rank(MD), rank(MT)
            assert rD % 2 == 0 and rT % 3 == 0
            lightHu = n - rD // 2; lightD = n - rT // 3
            tot += 1
            if lightHu != lightD: viol += 1
            if lightHu >= 1:
                withHu += 1
                minD = lightD if minD is None else min(minD, lightD)
            # the lepton block: light Y = -1/2 doublets = 2n - rD/2; three light leptons and one Higgs need 2n - rD/2 >= 4
            if 2 * n - rD // 2 >= 4 and lightHu >= 1 and lightD == 0: lepton_ok += 1
    summary[n] = (tot, viol, withHu, minD, lepton_ok)
    print(f"  n = {n}: configurations {tot}; light H_u != light D: {viol}; configurations with a light H_u: {withHu}, minimum light D among them: {minD}; "
          f"configurations with a light H_u, no light D and >= 4 light Y = -1/2 doublets: {lepton_ok}")
ok = all(v[1] == 0 and v[3] == 1 and v[4] == 0 for v in summary.values())
print(f"\nTHE PINCER: light up-type Higgs doublets = light exotic triplets in every configuration; every vacuum with a Higgs has a light D: {ok}")
print("DONE")
