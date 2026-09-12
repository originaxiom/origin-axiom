#!/usr/bin/env python3
"""ITEM 1 --- the 'slack table' computation, EXACTLY as run.

*** MISLABELLING WARNING, from the producing seat ***
This computes |kappa - 2| at SnapPy's DEFAULT generating pair only.
  - It does NOT search over generating pairs. Word-length searched = 0.
  - It does NOT check the generators are parabolic. For m004 they are not
    (tr = omega-1, modulus sqrt3, not 2).
  - Therefore the outputs are NEITHER Jorgensen numbers NOR upper bounds on them.
I presented them as 'distance off the bound' and built an ordering on it. That
labelling is withdrawn. The numbers below are exact for the quantity actually
computed: |tr[a,b] - 2| at one specific pair.
cc exhibits a pair at 9 for t12833 (< my 13) and 4 for t12835 (< my 7) --- consistent.
"""
import snappy
def kappa_at_default_pair(M):
    G = M.fundamental_group(); g = G.generators()
    if len(g) < 2: return None, None
    A = G.SL2C(g[0]); B = G.SL2C(g[1])
    tr = lambda X: complex(X[0][0] + X[1][1])
    AB = [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    x, y, z = tr(A), tr(B), tr(AB)
    return (x, y, z), x**2 + y**2 + z**2 - x*y*z - 2

FAM = ['m004','m000','m009','m136','m003','m206','m202',
       's958','v2873','t12833','t12835']
print(f"{'mfld':9s} {'|tr[a,b]-2| @ default pair':>28s}  {'tr a':>22s}  parabolic?")
for nm in FAM:
    M = snappy.Manifold(nm)
    xyz, k = kappa_at_default_pair(M)
    if k is None: continue
    par = abs(abs(xyz[0]) - 2) < 1e-9
    print(f"{nm:9s} {abs(k-2):28.9f}  {xyz[0]:+22.9f}  {par}")
print()
print("NOT an infimum over generating pairs. NOT a Jorgensen number.")
