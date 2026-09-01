#!/usr/bin/env python3
"""R15 stage 2 (exact, flint): censuses, enhancement cubic, wall slopes, SMT landing.

Root-evaluation method throughout: e6 decomposes under the toral C; a weight-line
survives a measurement iff its weight evaluates to zero on the measured element.
All polynomials here are computed EXACTLY over Q by interpolation of flint charpolys
and factored over Z. Still blind to the arc's solvers.
"""
import pickle, sys, json
from fractions import Fraction
from math import gcd, lcm
from flint import fmpz_mat, fmpq_mat, fmpz_poly, nmod_mat, nmod_poly, fmpq, fmpz

HERE = __file__.rsplit("/", 1)[0]
D = pickle.load(open(HERE + "/r15_e6_data.pkl", "rb"))
DIM = D["TAB_dims"]

ads = {}
scales = {}
for n, M in D["ads"].items():
    n = int(n)
    F = [[Fraction(x) for x in row] for row in M]
    dens = [f.denominator for row in F for f in row if f]
    L = 1
    for d in dens:
        L = lcm(L, d)
    nums = [abs(int(f * L)) for row in F for f in row if f]
    g = 0
    for x in nums:
        g = gcd(g, x)
    g = g or 1
    scales[n] = Fraction(L, g)
    ads[n] = [[int(f * L) // g for f in row] for row in F]
print("scale factors g_int = fac*g_defn:", {n: str(scales[n]) for n in scales})

A8, A14, A16, A22 = (fmpz_mat(ads[n]) for n in (8, 14, 16, 22))

def vstack(mats):
    rows = []
    for M in mats:
        rows += M.tolist()
    return fmpz_mat(rows)

def nullity(M):
    return M.ncols() - M.rank()

# ---------------- exact /Q censuses ----------------
cen = {"z(g8)": nullity(A8), "z(g14)": nullity(A14), "z(g16)": nullity(A16),
       "z(g22)": nullity(A22),
       "z(Pi)=core": nullity(vstack([A8, A16])),
       "CentC": nullity(vstack([A8, A14, A16, A22]))}
print("[exact /Q] censuses:", cen)

# ---------------- charpoly interpolation helper ----------------
def lowest_coeff_poly(build, deg_bound, lam_index):
    """build(s) -> fmpz_mat; returns exact Fraction-coeff list of the polynomial
    s |-> coeff of x^lam_index in charpoly(build(s)), degree <= deg_bound."""
    pts = list(range(-(deg_bound // 2 + 1), deg_bound // 2 + 2))
    vals = []
    for s in pts:
        cp = build(s).charpoly()
        c = int(cp[lam_index])
        vals.append(Fraction(c))
    # Lagrange interpolation (exact)
    n = len(pts)
    coeffs = [Fraction(0)] * n
    for i, (xi, yi) in enumerate(zip(pts, vals)):
        # basis poly prod_{j!=i} (x - xj)/(xi - xj)
        num = [Fraction(1)]
        den = Fraction(1)
        for j, xj in enumerate(pts):
            if j == i:
                continue
            num = [Fraction(0)] + num  # multiply by x
            for k in range(len(num) - 1):
                num[k] -= Fraction(xj) * num[k + 1]
            den *= Fraction(xi - xj)
        w = yi / den
        for k in range(len(num)):
            coeffs[k] += w * num[k]
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs

def to_fmpz_poly(coeffs):
    L = 1
    for c in coeffs:
        L = lcm(L, c.denominator)
    ints = [int(c * L) for c in coeffs]
    g = 0
    for x in ints:
        g = gcd(g, x)
    g = g or 1
    return fmpz_poly([x // g for x in ints])

# ---------------- the FIRST measurement pencil: x(rho) = g8 + rho g16 ----------
# generic nullity on e6 is 30 (the plane stratum is at rho-infinity etc.); coeff of
# lambda^30 vanishes exactly at enhancement rho.
q1 = lowest_coeff_poly(lambda s: A8 + A16 * s, 48, 30)
P1 = to_fmpz_poly(q1)
fac1 = P1.factor()
print("x-pencil: coeff_lambda^30 factors:")
for f, m in fac1[1]:
    print("   deg", f.degree(), "mult", m, ":", f)
cubics = [(f, m) for f, m in fac1[1] if f.degree() == 3]
assert len(cubics) == 1, cubics
MU_MINE, mu_mult = cubics[0]
print("MY enhancement cubic:", MU_MINE, " multiplicity", mu_mult)

# banked B877 cubic for the convention diff
MU_BANKED = fmpz_poly([2197, -4769856, -2075673600, 500716339200])
# check MU_MINE(rho) ~ MU_BANKED(c*rho) up to scalar, for rational c
a3, a2, a1, a0 = [int(MU_MINE[k]) for k in (3, 2, 1, 0)]
b3, b2, b1, b0 = [int(MU_BANKED[k]) for k in (3, 2, 1, 0)]
# mu_banked(c rho) = b3 c^3 rho^3 + b2 c^2 rho^2 + b1 c rho + b0 ; ratio vs mine:
# need b3 c^3 / a3 = b2 c^2 / a2 = b1 c / a1 = b0/a0
cands = set()
if a1 and b1:
    c = Fraction(b0 * a1, a0 * b1)
    cands.add(c)
for c in cands:
    ok = (Fraction(b3) * c**3 * a0 == Fraction(b0) * a3 and
          Fraction(b2) * c**2 * a0 == Fraction(b0) * a2 and
          Fraction(b1) * c * a0 == Fraction(b0) * a1)
    print("convention scale rho_banked = rho_mine *", c, "->", "MATCH" if ok else "no")

# ---------------- z(x1) exactly over F = Q[rho]/MU_MINE: restriction of scalars ----
mu_monic_den = int(MU_MINE[3])
# companion matrix of MU_MINE (as acting on Q[rho]/mu): use monic version with
# rational entries -> scale trick: work with matrix over Q via fmpq_mat.
mu_c = [Fraction(int(MU_MINE[k]), mu_monic_den) for k in range(3)]
C3 = [[Fraction(0), Fraction(0), -mu_c[0]],
      [Fraction(1), Fraction(0), -mu_c[1]],
      [Fraction(0), Fraction(1), -mu_c[2]]]

def kron(Aint, B3):
    """A (fmpz_mat) tensor B3 (3x3 Fractions) -> list of Fraction rows"""
    At = Aint.tolist()
    n = Aint.nrows()
    out = []
    for i in range(n):
        for bi in range(3):
            row = []
            for j in range(n):
                a = int(At[i][j])
                for bj in range(3):
                    row.append(a * B3[bi][bj])
            out.append(row)
    return out

I3 = [[Fraction(1 if i == j else 0) for j in range(3)] for i in range(3)]
M1 = kron(A8, I3)
M2 = kron(A16, C3)
big = [[M1[i][j] + M2[i][j] for j in range(3 * DIM)] for i in range(3 * DIM)]
# clear denominators row-wise for fmpz_mat
rowsint = []
for row in big:
    L = 1
    for x in row:
        L = lcm(L, x.denominator)
    rowsint.append([int(x * L) for x in row])
BIG = fmpz_mat(rowsint)
nb = nullity(BIG)
print("[exact /Q] restriction-of-scalars nullity of ad(x1) over F:", nb, "=> dim_F z(x1) =", nb // 3)
assert nb % 3 == 0

# ---------------- restricted operators on N = z(x1) (as Q-space, dim nb) --------
NS, nnull = BIG.nullspace()
assert nnull == nb
Ncols = [[Fraction(int(NS[i, j])) for j in range(nb)] for i in range(3 * DIM)]
NB = fmpq_mat([[fmpq(x.numerator, x.denominator) for x in row] for row in Ncols])

def restrict(Aint):
    """restriction of A (x) I3 to column space of NB: solve NB R = (A(x)I3) NB"""
    MB = fmpq_mat(kron_q(Aint))
    RHS = MB * NB
    # find pivot rows of NB
    R, _ = NB.rref()
    piv = []
    r = 0
    for j in range(R.ncols()):
        if r < R.nrows() and R[r, j] != 0:
            piv.append(j)
            r += 1
    # actually need pivot ROWS: rref of transpose
    Rt, _ = NB.transpose().rref()
    piv = []
    r = 0
    for j in range(Rt.ncols()):
        if r < Rt.nrows() and Rt[r, j] != 0:
            piv.append(j)
            r += 1
    P = fmpq_mat([[fmpq(1) if j == p else fmpq(0) for j in range(NB.nrows())] for p in piv])
    S = P * NB   # nb x nb, invertible
    T = P * RHS
    return S.solve(T)

def kron_q(Aint):
    At = Aint.tolist()
    n = Aint.nrows()
    out = []
    for i in range(n):
        for bi in range(3):
            row = []
            for j in range(n):
                a = int(At[i][j])
                for bj in range(3):
                    row.append(fmpq(a) if bi == bj else fmpq(0))
            out.append(row)
    return out

R14 = restrict(A14)
R16 = restrict(A16)

def q_to_z(Q):
    """fmpq_mat -> integer matrix (cleared common denominator) as fmpz_mat + den"""
    rows = Q.tolist()
    L = 1
    for row in rows:
        for x in row:
            L = lcm(L, int(x.q))
    return fmpz_mat([[int(x.p) * (L // int(x.q)) for x in row] for row in rows]), L

R14z, d14 = q_to_z(R14)
R16z, d16 = q_to_z(R16)
# common integer scale: use D = lcm(d14,d16): pencil D*(R14 + s R16)
DD = lcm(d14, d16)
R14i = R14z * (DD // d14)
R16i = R16z * (DD // d16)
print("restricted 138x138 operators built (denominators", d14, d16, ")")

# generic nullity of the restricted pencil (= 3 * dim z(x1, generic y)):
import random
random.seed(1)
gnul = nullity(R14i + R16i * 12345)
print("generic joint nullity on N (Q-dim):", gnul, "=> dim_F z(x1, y_generic) =", gnul // 3)

q2 = lowest_coeff_poly(lambda s: R14i + R16i * s, nb - gnul, gnul)
P2 = to_fmpz_poly(q2)
fac2 = P2.factor()
print("joint pencil on z(x1): lowest-coeff factors (slope polynomial):")
for f, m in fac2[1]:
    print("   deg", f.degree(), "mult", m, ":", f)

# ---------------- the y-alone pencil on all of e6 (for the real-line scan diff) ---
q3 = lowest_coeff_poly(lambda s: A14 + A16 * s, 66, 12)
P3 = to_fmpz_poly(q3)
fac3 = P3.factor()
print("y-pencil on e6: coeff_lambda^12 factors:")
for f, m in fac3[1]:
    print("   deg", f.degree(), "mult", m, ":", f)

with open(HERE + "/r15_exact_out.json", "w") as fh:
    json.dump({"censuses": cen,
               "mu_mine": [int(MU_MINE[k]) for k in range(4)],
               "x_pencil_factors": [[ [int(f[k]) for k in range(f.degree()+1)], m] for f, m in fac1[1]],
               "joint_factors": [[ [int(f[k]) for k in range(f.degree()+1)], m] for f, m in fac2[1]],
               "y_pencil_factors": [[ [int(f[k]) for k in range(f.degree()+1)], m] for f, m in fac3[1]],
               "dimF_z_x1": nb // 3, "generic_joint_dimF": gnul // 3,
               "scales": {n: str(scales[n]) for n in scales}}, fh, indent=1)
print("saved r15_exact_out.json")
