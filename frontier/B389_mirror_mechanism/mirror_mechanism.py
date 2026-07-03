"""B389 -- M1/M2 on the banked table + M3 operator check."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, "..", "B367_value_map", "step0_tables.json")))["1,2"]
o1, o2 = 20, 12
def get(a, b):
    r = T.get(f"{a % o1},{b % o2}")
    return tuple(Fr(x) for x in r) if r else (Fr(0),)*4
def tau3(t): return (t[0], t[1], -t[2], -t[3])

cells = [tuple(map(int, k.split(","))) for k in T]
m1 = all(get(-a, -b) == get(a, b) for (a, b) in cells)
# also check support closure under inversion
m1_supp = all(f"{(-a) % o1},{(-b) % o2}" in T for (a, b) in cells)
m2 = all(get(-a, b) == tau3(get(a, b)) for (a, b) in cells)
print("M1 inversion law t(-a,-b) = t(a,b):", m1, " (support closed:", m1_supp, ")")
print("M2 a-flip law t(-a,b) = tau3(t(a,b)):", m2)

# M3: [S, Par] with S = F (g scalar drops)
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
import cyclo_engine as E
N = 15
F = [[E.e15((i * j) % 15) for j in range(N)] for i in range(N)]
FP = [[F[i][(-j) % N] for j in range(N)] for i in range(N)]     # F . Par (col-permute)
PF = [[F[(-i) % N][j] for j in range(N)] for i in range(N)]     # Par . F (row-permute)
m3 = all(FP[i][j] == PF[i][j] for i in range(N) for j in range(N))
print("M3 [S, Par] = 0 (F.Par == Par.F):", m3)
json.dump(dict(M1=m1, M1_support_closed=m1_supp, M2=m2, M3=m3),
          open(os.path.join(HERE, "mirror_mechanism.json"), "w"), indent=1)
print("DONE")
