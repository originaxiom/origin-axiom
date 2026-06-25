"""B209 -- the classical/quantum boundary, sharpest form: the icosahedral tiling's exterior algebra
Lambda*(R^6) decomposes into exactly the BOSONIC A5 irreps; the 4 SPINORIAL irreps of the double
cover 2I -- the ones that complete affine E8 -- are ABSENT (they need the quantum/spin lift).

The icosahedral quasicrystal lives in 6D (cut-and-project Z^6 -> R^3); A5 (icosahedral rotation group)
acts on R^6 = 3 + 3' (physical + perpendicular 3-spaces). The exterior algebra Lambda*(R^6) (dim 2^6=64)
carries the tiling's topological invariants. Result (computed from characters, not hardcoded):
  every A5 irrep (dims 1,3,3,4,5) appears with multiplicity EXACTLY 4 -> total 4*16 = 64.
  the 4 spinorial 2I irreps {2,2',4',6} (dims 2,2,4,6) are ABSENT -- Lambda* of an honest A5 rep
  (center -I acts trivially) contains only A5 irreps.
2I = A5 (5 bosonic irreps) + {spinorial} (4 irreps); the 4 spinorial = exactly the affine-E8 nodes
missing from A5. So: classical tiling sees A5 (B206 PSL level); the spin/quantum lift sees 2I=E8 (SL
level); the boundary is precisely these 4 spinorial irreps. FIREWALL: representation theory; the
'K-theory of the tiling' framing is a one-way hook (the actual K-groups are a separate computation),
NOT a physics claim. Nothing to CLAIMS.md. Connects B206."""
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
# A5 character table on classes (e, (12)(34), (123), C5a, C5b); the two 3-dim irreps carry phi:
SIZES = [1, 15, 20, 12, 12]
ORDERS = [1, 2, 3, 5, 5]
A5_IRREPS = {
    "1":  [1, 1, 1, 1, 1],
    "3":  [3, -1, 0, PHI, 1 - PHI],
    "3'": [3, -1, 0, 1 - PHI, PHI],
    "4":  [4, 0, 1, -1, -1],
    "5":  [5, 1, -1, 0, 0],
}
# chi of R^6 = 3 + 3', and its values on powers g^j of a class rep (to recover eigenvalues):
CHI6 = [6, -2, 0, 1, 1]
POWER_CHI6 = {0: [6], 1: [6, -2], 2: [6, 0, 0], 3: [6, 1, 1, 1, 1], 4: [6, 1, 1, 1, 1]}
# 2I irreps minus A5 irreps = the spinorial ones (center acts as -1), completing affine E8:
SPINORIAL_2I_DIMS = [2, 2, 4, 6]


def lambda_star_char(ci):
    """chi_{Lambda* R^6}(g) = det(I + rho_6(g)) = prod (1+eigenvalue), from the power-characters."""
    n, pc = ORDERS[ci], POWER_CHI6[ci]
    z = np.exp(2j * np.pi / n)
    det = 1 + 0j
    for k in range(n):
        mult = round((sum(pc[j] * z ** (-j * k) for j in range(n)) / n).real)
        det *= (1 + z ** k) ** mult
    return round(det.real)


def decompose():
    chiLS = [lambda_star_char(ci) for ci in range(5)]
    mults = {name: round(sum(SIZES[i] * chiLS[i] * ch[i] for i in range(5)) / 60)
             for name, ch in A5_IRREPS.items()}
    return chiLS, mults


if __name__ == "__main__":
    chiLS, mults = decompose()
    print("chi_{Lambda*(R^6)} on A5 classes =", chiLS, "(= det(I+rho_6) per class)")
    print("decomposition into A5 irreps:", mults)
    total = sum(mults[n] * A5_IRREPS[n][0] for n in mults)
    print(f"total dim = {total} = 2^6 ; every A5 irrep has multiplicity 4")
    print(f"SPINORIAL 2I irreps (dims {SPINORIAL_2I_DIMS}) -- the affine-E8 nodes beyond A5 -- are ABSENT.")
    assert chiLS == [64, 0, 4, 4, 4]
    assert all(v == 4 for v in mults.values()) and total == 64
    print("=> classical tiling sees A5 (5 bosonic irreps); the spin/quantum lift adds 2I's 4 spinorial")
    print("   irreps to complete E8 (B206). The boundary is exactly those 4 irreps. ALL CHECKS PASS")
