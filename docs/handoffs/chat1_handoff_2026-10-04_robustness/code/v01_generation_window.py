"""TIER 1. Generation window for a world built on E6 27s.
CP floor (Kobayashi-Maskawa) + asymptotic-freedom ceiling.  Two routes for the 27's colour content."""
from fractions import Fraction as F
print("CP phases (N-1)(N-2)/2 :", {N:(N-1)*(N-2)//2 for N in range(1,7)}, "-> N >= 3")
# route 1: SM-component count of one 27
r1 = 2+1+1+1+1          # Q(3,2)=2, u^c, d^c, D, D^c  (colour-triplet Weyl)
# route 2: trinification 27 = (3b,3,1)+(1,3b,3)+(3,1,3b): coloured dims 9+9
r2 = (9+9)//3
assert r1==r2==6, "27 colour content disagrees between routes"
nD = r1//2                                     # Dirac flavours per generation
ceil = max(N for N in range(1,30) if 11-F(2,3)*nD*N>0)
print(f"27 colour content: route1={r1}, route2={r2} triplet Weyl -> {nD} Dirac/gen")
print(f"asymptotic freedom beta0 = 11 - 2N > 0  ->  N <= {ceil}")
for ns in (1,2):
    c=max(N for N in range(1,30) if 11-F(2,3)*nD*N-F(1,6)*ns*N>0)
    print(f"  with {ns} coloured scalar triplet(s)/gen -> N <= {c}  (ceiling only TIGHTENS)")
print("WINDOW: N in {3,4,5}; minimum = 3")
