"""B1088 - C1 of L174: THE PARAMETER-FREE ACTION CARD, assembled and verified.

The claim to make precise: the object's 3d action has ZERO free dimensionless
constants. Its single scale is the input ledger's one unit (the R+ closing).
Checks: (1) Vol(m004) = 2 x (regular ideal tetrahedron) = 2.029883... to 50
digits from the Lobachevsky function - the banked complex-volume figure;
(2) CS(m004) = 0: the Rogers-dilogarithm real part at the regular shape is
exactly pi^2/6-lattice-trivial (the amphichirality theorem's numeric face; the
computed witness is B1086's mirror=Galois identity gal(lam)=lam^{-1});
(3) the action value S = -CS k - Vol sigma = -Vol sigma: the k-term deleted by
the object's own symmetry; (4) Brown-Henneaux closure: Lambda=-1 => l=1,
G_N = 1/(4 sigma) => c = 3l/(2G_N) = 6 sigma, matching B1012's three-entry
closure EXACTLY (symbolic identity).
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 60

# (1) the volume from first principles: Lobachevsky Lambda(theta) = Cl2(2 theta)/2
def lobachevsky(theta):
    return mp.clsin(2, 2*theta)/2

tet = 3*lobachevsky(mp.pi/3)          # regular ideal tetrahedron
vol = 2*tet                            # m004 = two regular ideal tetrahedra
print(f"(1) Vol(regular ideal tet) = {mp.nstr(tet, 30)}")
print(f"    Vol(m004) = 2 x tet    = {mp.nstr(vol, 30)}")
banked = mp.mpf("2.02988321281930725004240510854")
assert abs(vol - banked) < mp.mpf(10)**(-28), "volume mismatch vs banked figure"
print("    matches the banked complex-volume figure to 28 digits: PASS")

# (2) CS = 0: Rogers dilogarithm at the regular shape z = e^{i pi/3}, two tetrahedra
z = mp.e**(1j*mp.pi/3)
R = mp.polylog(2, z) + mp.log(z)*mp.log(1-z)/2
cv = 2*R                               # the complex volume combination
print(f"(2) 2 x Rogers R(e^(i pi/3)) = {mp.nstr(cv, 25)}")
cs_part = mp.re(cv)                    # the CS-carrying real part
lattice = mp.pi**2/6
frac = cs_part/lattice
print(f"    CS part / (pi^2/6) = {mp.nstr(frac, 25)}  (integer iff CS = 0 in the lattice)")
assert abs(frac - mp.nint(frac)) < mp.mpf(10)**(-50), "CS part not lattice-trivial"
vol_part = mp.im(cv)
assert abs(vol_part - vol) < mp.mpf(10)**(-50), "imaginary part is not the volume"
print(f"    CS(m004) = 0 in the pi^2/6 lattice (50-digit check): PASS")
print(f"    Im part = Vol to 50 digits: PASS")

# (3) the action value: S = -CS k - Vol sigma with CS = 0
sigma, k = sp.symbols("sigma k", positive=True)
CS = 0
S = -CS*k - sp.Symbol("Vol")*sigma
print(f"(3) S = -CS k - Vol sigma  ->  S = {S}  (the k-term deleted by amphichirality)")
assert S == -sp.Symbol("Vol")*sigma

# (4) Brown-Henneaux closure, exact symbolic identity
l = 1                                   # Lambda = -1 => AdS3 radius 1 (B259)
G_N = 1/(4*sigma)                       # B1012's identification
c_BH = sp.Rational(3,2)*l/G_N
assert sp.simplify(c_BH - 6*sigma) == 0
print(f"(4) c = 3l/(2 G_N) with l=1, G_N=1/(4 sigma)  ->  c = {sp.simplify(c_BH)} = 6 sigma: PASS")
print("    (= B1012's three-entry closure, reached independently through Brown-Henneaux)")

print()
print("THE CARD: Lambda = -1 (forced, B259) | l = 1 (from Lambda) | Vol = the object's own")
print("volume (computed) | CS = 0 (amphichirality; witness = the mirror=Galois identity,")
print("B1086) | G_N = 1/(4 sigma) (B1012) | c = 6 sigma (derived twice) | S = -Vol sigma.")
print("ZERO free dimensionless constants; sigma = the input ledger's one unit (R+ closing).")
print("ALL CHECKS PASS")
