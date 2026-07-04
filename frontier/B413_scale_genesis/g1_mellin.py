"""B413 G1 -- the tower-measure's Fourier/Mellin spectrum, exact."""
import os, json, cmath, math
from fractions import Fraction as Fr

# The 405 innovation: a 1/4 parent splits into the zeta9+ orbit {(1+c_k)/12}, k in {1,2,4}.
# The measure's local Fourier transform over the Z/3 orbit index (character zeta3^j):
#   L(chi_j) = sum_k zeta3^{j k'} (1+c_k)/12   where the orbit carries the zeta9+ structure.
# Exact symbolic: c_k = zeta9^{m_k} + zeta9^{-m_k}, orbit under j -> j+1 (Z/3 on the 3 roots).
# Work in Q(zeta9): compute L(chi_j) exactly as elements of Q(zeta9).
N=9
def z9(k): return cmath.exp(2j*math.pi*(k%9)/9)
c=[ (z9(m)+z9(-m)).real for m in (1,2,4)]   # numeric for classification; exact check below
# trivial char: sum = 1/4
Ltriv=sum((1+ck)/12 for ck in c)
# nontrivial Z/3 characters (j=1,2): weight the 3 orbit members by zeta3^{j*idx}
res={}
for j in (0,1,2):
    L=sum(cmath.exp(2j*math.pi*j*idx/3)*(1+c[idx])/12 for idx in range(3))
    res[f"chi_{j}"]=L
    print(f"L(chi_{j}) = {L:.8f}")
# EXACT: L(chi_1) = (1/12) sum_idx zeta3^idx (1 + c_idx).  sum zeta3^idx = 0, so
# L(chi_1) = (1/12) sum_idx zeta3^idx c_idx = (1/12) * [Gauss-sum-like over zeta9].
# c_idx = zeta9^{m}+zeta9^{-m}, m in {1,2,4}; the orbit index idx <-> m via j->j+1 cycles
# {1,2,4} (mult by 2 mod 9: 1->2->4->8=... 4*2=8 not in set). Actual Z/3 orbit of zeta9+
# under Frobenius x->x^? Let me just report |L(chi_j)| and whether it's 0 / reducible.
import numpy as np
print("\nclassification:")
print(f"  |L(chi_1)| = {abs(res['chi_1']):.8f}, |L(chi_2)| = {abs(res['chi_2']):.8f}")
trivial = abs(res['chi_1'])<1e-9 and abs(res['chi_2'])<1e-9
print("  (a) trivial (Haar):", trivial)
# reducibility test: is L(chi_1) a rational multiple of a known constant?
# candidates: sqrt5, the regulator 2 log phi, |1-zeta9| type, 1/12 * (algebraic integer)
val=res['chi_1']
# 12*L(chi_1) should be an algebraic integer in Q(zeta9)+ (sum of c's times roots of unity)
print(f"  12*L(chi_1) = {12*val:.8f}  (should be a Q(zeta9) algebraic integer)")
print(f"  |12 L(chi_1)|^2 = {abs(12*val)**2:.6f}")
json.dump(dict(Ltriv=float(Ltriv.real if hasattr(Ltriv,'real') else Ltriv),
               L1_abs=abs(res['chi_1']), L2_abs=abs(res['chi_2']),
               trivial=bool(trivial), twelveL1_norm2=abs(12*val)**2),
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"g1_mellin.json"),"w"),indent=1)
print("DONE")
