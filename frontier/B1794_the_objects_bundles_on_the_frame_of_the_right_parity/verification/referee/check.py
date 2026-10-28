"""Referee re-check for P-401 draft (independent of the draft's script).
1. H_1 of m004(p,q) on a grid; b1>0 iff p=0.  2. solution types on a grid (exceptional set).
3. framing check: meridian/longitude in H_1.  4. integral Kunneth for H^2(X;Z), H^4(X;Z).
5. trivialisation identity numerically for sigma = Sym^2 (PSL-rep) and sigma = id (SL only)."""
import snappy, math, itertools, random
import numpy as np
from math import gcd

M0 = snappy.Manifold("m004")
print("m004 H1:", M0.homology(), " cusp_info shape:", M0.cusp_info(0)["shape"])
G = M0.fundamental_group()
print("peripheral words (meridian, longitude):", G.peripheral_curves())
# abelianise: H1 = Z; the image of each generator
print("pi1 gens:", G.generators(), " relators:", G.relators())

bad = []
rows = []
for p in range(-12, 13):
    for q in range(0, 13):
        if (p, q) == (0, 0) or gcd(abs(p), q) != 1:
            continue
        if q == 0 and p != 1:
            continue
        if p == 0 and q != 1:
            continue
        N = snappy.Manifold("m004"); N.dehn_fill((p, q))
        H = N.homology()
        ed = H.elementary_divisors()
        b1 = sum(1 for c in ed if c == 0)
        order = 0 if b1 else (math.prod(ed) if ed else 1)
        ok = (b1 == 1) if p == 0 else (b1 == 0 and order == abs(p))
        if not ok:
            bad.append((p, q, str(H)))
        st = N.solution_type()
        rows.append((p, q, str(H), st))
print("grid fillings checked:", len(rows), " H1 = Z/|p| (b1>0 iff p=0) failures:", bad)
nonhyp = sorted({(p, q) for p, q, H, st in rows if st != "all tetrahedra positively oriented"})
print("non-geometric solution types on grid:", nonhyp)
# retry non-geometric with randomisation to separate triangulation artefacts from exceptional slopes
still = []
for p, q in nonhyp:
    good = False
    for k in range(30):
        N = snappy.Manifold("m004"); N.dehn_fill((p, q)); N.randomize()
        if N.solution_type() == "all tetrahedra positively oriented":
            good = True; break
    if not good:
        still.append((p, q))
print("still non-geometric after 30 randomisations:", still)

# 4. integral Kunneth.  Cohomology groups as lists (free rank, torsion list)
def kunneth(HA, HB, n):
    # HA[i] = (rank, [torsion]) cohomology; returns H^n(AxB) = sum_{i+j=n} A^i (x) B^j + sum_{i+j=n+1} Tor(A^i,B^j)
    rank = 0; tors = []
    for i in range(len(HA)):
        j = n - i
        if 0 <= j < len(HB):
            ra, ta = HA[i]; rb, tb = HB[j]
            rank += ra * rb
            tors += ta * rb + tb * ra + [gcd(a, b) for a in ta for b in tb]
        j = n + 1 - i
        if 0 <= j < len(HB):
            ra, ta = HA[i]; rb, tb = HB[j]
            tors += [gcd(a, b) for a in ta for b in tb]
    return rank, sorted(t for t in tors if t > 1)
SO3 = [(1, []), (0, []), (0, [2]), (1, [])]
for p in [5, 6, 7, 8]:
    Mc = [(1, []), (0, []), (0, [p]), (1, [])]   # closed QHS with H1 = Z/p
    print("closed filling H1=Z/%d:  H^2(X;Z) =" % p, kunneth(Mc, SO3, 2), " H^4(X;Z) =", kunneth(Mc, SO3, 4), " H^6 =", kunneth(Mc, SO3, 6))
Mcusp = [(1, []), (1, []), (0, []), (0, [])]     # knot complement: H^2 = H_1(M,dM) = 0 (meridian surjects), H^3 = 0
print("cusped m004: H^2(X;Z) =", kunneth(Mcusp, SO3, 2), " H^4(X;Z) =", kunneth(Mcusp, SO3, 4))
print("rational Betti closed:", [kunneth([(1,[]),(0,[]),(0,[5]),(1,[])], SO3, n)[0] for n in range(7)])
print("rational Betti cusped:", [kunneth(Mcusp, SO3, n)[0] for n in range(7)])

# 5. trivialisation identity
rng = np.random.default_rng(7)
def rsl2():
    A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    return A / np.sqrt(np.linalg.det(A))
def sym2(A):
    a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
    # action on quadratic forms basis x^2, xy, y^2 under (x,y) -> (ax+cy, bx+dy)  (a homomorphism up to convention)
    return np.array([[a*a, a*c, c*c], [2*a*b, a*d + b*c, 2*c*d], [b*b, b*d, d*d]])
g, h = rsl2(), rsl2()
hom = np.allclose(sym2(g @ h), sym2(g) @ sym2(h)) or np.allclose(sym2(g @ h), sym2(h) @ sym2(g))
print("sym2 multiplicative (some order):", hom, " even in -1:", np.allclose(sym2(-g), sym2(g)))
for name, sig in [("id (2-dim, SL only)", lambda A: A), ("Sym2 (PSL rep)", sym2)]:
    if name.startswith("Sym2") and not np.allclose(sym2(g @ h), sym2(g) @ sym2(h)):
        sig0 = sig; sig = lambda A, s=sig0: s(A.T).T  # fix order convention
    gam, gg = rsl2(), rsl2()
    v = rng.normal(size=sig(gg).shape[0]) + 0j
    lhs = np.linalg.solve(sig(gam @ gg), sig(gam) @ v)
    rhs = np.linalg.solve(sig(gg), v)
    print("  phi(gamma g, sigma(gamma) v) == phi(g, v) for sigma =", name, ":", np.allclose(lhs, rhs))
    # on PSL: g ~ -g; phi(-g, v) == phi(g, v)?
    print("    well defined on PSL (phi(-g,v)==phi(g,v)):", np.allclose(np.linalg.solve(sig(-gg), v), rhs))
print("check exit 0")
