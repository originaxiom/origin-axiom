#!/usr/bin/env python3
"""B1368 -- THE OBJECT'S OWN STANDARD-MODEL CONNECTIONS: flat E6(C) connections of m004 that leave the Standard Model unbroken, their
bulk zero modes, and their chiral index in the seat's frame (B1351).

Any flat E6(C) connection commuting with the Standard Model has image in c(SM) = SL(2)_beta x C*^2 (B1364, B1366); the geometric
representation (Zariski-dense in SL(2,C)) can sit only in SL(2)_beta.  So the family is
    rho_{s,t} = (rho_geom into SL(2)_beta) x (the character a, b -> exp(2 pi i (s Y + t gamma)) on the SU(6) weights),
and the 78 and the 27 decompose into sectors (spin j of SL(2)_beta) x (a weight w of the character):
    78 = (3,1) + (1,35) + (2,20),   27 = (1,15) + (2,6bar).
Computed here, exactly over Q(omega) (sympy):
  (A) the Riley representation a -> [[1,1],[0,1]], b -> [[1,0],[u,1]], u = 1 + omega; the relator a w b^-1 w^-1, w = b a^-1 b^-1 a; the
      longitude lambda = w w*, w* = a b^-1 a^-1 b: tr rho(lambda) (Calegari: -2), rho(lambda) unipotent up to sign;
  (B) the SM-reaching condition on (s, t): the 22 non-SM roots of SU(6) must carry a non-trivial character; the sector census;
  (C) Fox calculus on <a, b | r> for the three sector types with a character z: spin 0 (C_z), spin 1/2 (V_2 x C_z), spin 1 (Ad rho):
      h^0, h^1 as functions of z; the Alexander polynomial and the twisted Alexander polynomial of the geometric representation;
  (D) cusp-fixedness of every sector type: the joint fixed space of (Phi(mu), Phi(lambda));
  (E) the index in B1351's frame: N_w = -chi(boundary^+; L_w), non-zero only on a cusp-fixed non-trivial sector -> which SM-charged
      sectors can carry it.
Usage: python3 sm_connections_of_m004.py"""
import itertools, cmath, math
from fractions import Fraction as Fr
import sympy as sp
import numpy as np

# ---------------------------------------------------------------- (A) the knot group and the geometric representation, exact
omega = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2          # e^{2 pi i / 3}
u = 1 + omega                                                # e^{i pi / 3}
RA = sp.Matrix([[1, 1], [0, 1]]); RB = sp.Matrix([[1, 0], [u, 1]])
W = [2, -1, -2, 1]; WSTAR = [1, -2, -1, 2]
REL = [1] + W + [-2] + [-x for x in reversed(W)]             # a w b^-1 w^-1
LONG = W + WSTAR                                             # lambda = w w*
def word_matrix(word, Ma, Mb):
    M = sp.eye(Ma.shape[0])
    for L in word:
        X = Ma if abs(L) == 1 else Mb
        if L < 0: X = X.inv()
        M = M * X
    return sp.simplify(M)
rel_ok = sp.simplify(word_matrix(REL, RA, RB) - sp.eye(2)) == sp.zeros(2)
LAM = word_matrix(LONG, RA, RB)
tr_lam = sp.simplify(LAM.trace())
print("=== (A) the geometric representation of pi_1(m004) (Riley, u = 1 + omega) ===")
print(f"  relator a w b^-1 w^-1 holds: {rel_ok}; longitude lambda = w w*: trace {tr_lam} (Calegari's -2), lambda = {LAM.tolist()}, commutes with a: {sp.simplify(LAM * RA - RA * LAM) == sp.zeros(2)}")
lam_plus_one_nilpotent = sp.simplify((LAM + sp.eye(2)) ** 2) == sp.zeros(2)
print(f"  lambda + 1 is nilpotent (lambda = -(unipotent)): {lam_plus_one_nilpotent}; eigenvalues of lambda on V_2: {LAM.eigenvals()}")

# ---------------------------------------------------------------- (B) the E6 side: c(SM), the SM-reaching condition, the sectors
def roots_e6():
    R = []
    for i in range(5):
        for j in range(i + 1, 5):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [Fr(0)] * 5; v[i] = Fr(si); v[j] = Fr(sj); R.append((tuple(v), Fr(0)))
    for signs in itertools.product((1, -1), repeat=5):
        if signs.count(-1) % 2 == 0:
            w = tuple(Fr(s, 2) for s in signs); R.append((w, Fr(1))); R.append((tuple(-x for x in w), Fr(-1)))
    return R
def dot(a, b): return sum(x * y for x, y in zip(a[0], b[0])) + Fr(3, 4) * a[1] * b[1]
def vec(*xs): return (tuple(Fr(x) for x in xs[:5]), Fr(xs[5]))
R = roots_e6()
sm_roots = [vec(1,-1,0,0,0,0), vec(-1,1,0,0,0,0), vec(0,1,-1,0,0,0), vec(0,-1,1,0,0,0), vec(1,0,-1,0,0,0), vec(-1,0,1,0,0,0), vec(0,0,0,1,-1,0), vec(0,0,0,-1,1,0)]
Y = vec(Fr(-1,3), Fr(-1,3), Fr(-1,3), Fr(1,2), Fr(1,2), 0)
beta = vec(Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), 1)
gamma = vec(Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), Fr(-5, 3))
W27 = []
for signs in itertools.product((1, -1), repeat=5):
    if signs.count(-1) % 2 == 1: W27.append((tuple(Fr(s, 2) for s in signs), Fr(1, 3)))
for k in range(5):
    for s in (1, -1):
        v = [Fr(0)] * 5; v[k] = Fr(s); W27.append((tuple(v), Fr(-2, 3)))
W27.append((tuple([Fr(0)] * 5), Fr(4, 3)))
def sm_type(w):
    col = any(dot(w, s) != 0 for s in sm_roots[:6]); wk = dot(w, sm_roots[6]) != 0
    return ("colour" if col else "1", "doublet" if wk else "1", dot(Y, w))
print("\n=== (B) the E6 side ===")
spin78 = {}
for r in R:
    j2 = int(abs(dot(r, beta)))            # 2 x spin = |beta . alpha| in {0, 1, 2}
    spin78.setdefault(j2, []).append(r)
print(f"  78 by SL(2)_beta spin: spin 0 roots {len(spin78[0])} (+5 Cartan = 35), spin 1/2 roots {len(spin78[1])} (= 20 doublets), spin 1 roots {len(spin78[2])} (+1 Cartan = (3,1))")
spin27 = {}
for w in W27:
    spin27.setdefault(int(abs(dot(w, beta))), []).append(w)
print(f"  27 by spin: spin 0 weights {len(spin27[0])} (the 15), spin 1/2 weights {len(spin27[1])} (= 6 doublets)")
perp = spin78[0]; nonsm = [r for r in perp if r not in sm_roots]
print(f"  SM-reaching condition: the {len(nonsm)} non-SM roots of SU(6) need exp(2 pi i (s Y.alpha + t gamma.alpha)) != 1; the (Y, gamma) pairings of these roots:")
pairs = sorted(set((dot(Y, r), dot(gamma, r)) for r in nonsm))
print(f"    {[(str(p), str(q)) for p, q in pairs]} -> {len(pairs)} distinct lines s Y.alpha + t gamma.alpha in Z removed from C^2: the family is 2-complex-dimensional")
# the SM content of the spin-0 and spin-1/2 sectors of the 78 and the 27 (by SM type of the weight)
from collections import Counter
print(f"  spin-0 SM-charged sectors of the 78 (the 22 roots): {dict(Counter(sm_type(r) for r in nonsm))}")
print(f"  spin-1/2 sectors of the 78 (20 doublets, one weight per doublet): {dict(Counter(sm_type(r) for r in spin78[1] if dot(r, beta) == 1))}")
print(f"  spin-0 sectors of the 27 (15): {dict(Counter(sm_type(w) for w in spin27[0]))}")
print(f"  spin-1/2 sectors of the 27 (6 doublets): {dict(Counter(sm_type(w) for w in spin27[1] if dot(w, beta) == 1))}")

# ---------------------------------------------------------------- (C) Fox calculus on <a, b | r> with a character z, exact
z = sp.symbols('z')
def fox(word, gen, Ma, Mb):
    n = Ma.shape[0]; D = sp.zeros(n, n); P = sp.eye(n)
    for L in word:
        X = Ma if abs(L) == 1 else Mb
        if L < 0: X = X.inv()
        if abs(L) == gen:
            D = D + (P if L > 0 else -P * X)
        P = P * X
    return sp.simplify(D)
def cohomology(Ma, Mb, at=None):
    """h^0, h^1 of <a, b | r> with the representation a -> Ma, b -> Mb (exact); optionally evaluated at z = at"""
    n = Ma.shape[0]
    d1 = sp.Matrix.hstack(fox(REL, 1, Ma, Mb), fox(REL, 2, Ma, Mb))
    d0 = sp.Matrix.vstack(Ma - sp.eye(n), Mb - sp.eye(n))
    if at is not None:
        d1 = d1.subs(z, at); d0 = d0.subs(z, at)
    d1 = sp.simplify(d1); d0 = sp.simplify(d0)
    assert sp.simplify(d1 * d0) == sp.zeros(n, n)
    r1, r0 = d1.rank(simplify=True), d0.rank(simplify=True)
    return n - r0, 2 * n - r1 - r0, d1, d0
print("\n=== (C) the twisted cohomology of the knot group, sector by sector ===")
# spin 0: the character z
h0, h1, d1, d0 = cohomology(sp.Matrix([[z]]), sp.Matrix([[z]]))
alex = sp.factor(sp.simplify(d1[0, 0]))
print(f"  spin 0 (character z): Fox row (d r/d a, d r/d b) at a, b -> z: ({sp.factor(d1[0,0])}, {sp.factor(d1[0,1])}); the Alexander polynomial Delta(z) = {alex}")
alex_roots = sp.solve(sp.Eq(d1[0, 0], 0), z)
print(f"    roots: {alex_roots} = phi^2, phi^-2 (golden), |z| != 1: non-unitary characters; generic h^1 = {cohomology(sp.Matrix([[z]]), sp.Matrix([[z]]), at=sp.Rational(7,3))[1]}, h^1 at the roots: {[cohomology(sp.Matrix([[z]]), sp.Matrix([[z]]), at=r)[1] for r in alex_roots]}, at z = 1: (h^0, h^1) = {cohomology(sp.Matrix([[z]]), sp.Matrix([[z]]), at=1)[:2]}")
# spin 1/2: V_2 x C_z
h0h, h1h, d1h, d0h = cohomology(z * RA, z * RB)
numer = sp.factor(sp.simplify(d1h[:, 2:4].det()))       # det Phi(d r / d b)
denom = sp.factor(sp.simplify((z * RA - sp.eye(2)).det()))
twisted = sp.factor(sp.simplify(numer / denom))
print(f"  spin 1/2 (V_2 x C_z): det Phi(d r/d b) = {numer}; det(Phi(a) - 1) = {denom}; Wada's twisted Alexander polynomial = {twisted}")
tw_roots = sp.solve(sp.Eq(sp.numer(sp.together(twisted)), 0), z)
tw_roots_num = [complex(sp.N(r)) for r in tw_roots]
print(f"    roots: {tw_roots} ~ {[f'{r.real:+.4f}{r.imag:+.4f}i' for r in tw_roots_num]}, moduli {[round(abs(r), 4) for r in tw_roots_num]}")
print(f"    generic (h^0, h^1) = {cohomology(z * RA, z * RB, at=sp.Rational(7,3))[:2]}; at the twisted roots: {[cohomology(z * RA, z * RB, at=r)[:2] for r in tw_roots]}; at z = 1 (the untwisted V_2): {cohomology(RA, RB)[:2]}; at z = -1 (the other lift): {cohomology(-RA, -RB)[:2]}")
# spin 1: Ad rho (no character)
def ad(M):
    """the adjoint action on sl_2 in the basis (e, h, f)"""
    E_ = sp.Matrix([[0, 1], [0, 0]]); H_ = sp.Matrix([[1, 0], [0, -1]]); F_ = sp.Matrix([[0, 0], [1, 0]])
    basis = [E_, H_, F_]; Minv = M.inv()
    cols = []
    for B in basis:
        X = sp.simplify(M * B * Minv)
        cols.append([X[0, 1], X[0, 0], X[1, 0]])     # coordinates in (e, h, f): X = x_e e + x_h h + x_f f -> X[0,1] = x_e, X[0,0] = x_h, X[1,0] = x_f
    return sp.Matrix(cols).T
h0a, h1a, _, _ = cohomology(ad(RA), ad(RB))
print(f"  spin 1 (Ad rho, neutral): (h^0, h^1) = ({h0a}, {h1a}) -- the hyperbolic deformation")

# ---------------------------------------------------------------- (D) cusp-fixedness: joint fixed vectors of (Phi(mu), Phi(lambda)) per sector type
def fixed_dim(Ma, Mb, at=None):
    n = Ma.shape[0]
    Mmu = Ma; Mlam = word_matrix(LONG, Ma, Mb)
    if at is not None: Mmu = Mmu.subs(z, at); Mlam = Mlam.subs(z, at)
    S = sp.Matrix.vstack(sp.simplify(Mmu - sp.eye(n)), sp.simplify(Mlam - sp.eye(n)))
    return n - S.rank(simplify=True), sp.simplify(Mlam)
print("\n=== (D) cusp-fixedness (joint fixed vectors of the meridian a and the longitude w w*) ===")
for zz in [sp.Rational(7, 3), alex_roots[0], -1]:
    print(f"  spin 0, z = {zz}: fixed dim {fixed_dim(sp.Matrix([[z]]), sp.Matrix([[z]]), at=zz)[0]} (lambda acts by z^0 = 1, mu by z: fixed iff z = 1)")
print(f"  spin 0, z = 1: fixed dim {fixed_dim(sp.Matrix([[1]]), sp.Matrix([[1]]))[0]} (the trivial local system)")
for zz in [sp.Rational(7, 3), 1, -1] + tw_roots:
    fd, Ml = fixed_dim(z * RA, z * RB, at=zz)
    print(f"  spin 1/2, z = {zz}: fixed dim {fd}; Phi(lambda) = {Ml.tolist()} (eigenvalue -1 twice: never a fixed vector)")
fd1, Ml1 = fixed_dim(ad(RA), ad(RB))
print(f"  spin 1 (Ad rho): fixed dim {fd1} (the nilpotent direction e: the neutral modulus's cusp-fixed weight)")

# ---------------------------------------------------------------- (E) the index in the seat's frame
print("\n=== (E) the chiral index N_w = -chi(boundary^+; L_w) (B1351 (ii), whole-torus/annular conventions) ===")
print("  a sector carries a non-zero index only if it is cusp-fixed (otherwise H*(T^2; L_w) = 0) and non-trivial (a trivial local system has no Higgs field: N = -chi(empty) = 0).")
print("  spin-1/2 sectors ((2,20) of the 78, (2,6bar) of the 27 -- every SM-charged doublet-type weight): never cusp-fixed, because rho(lambda) = -(unipotent) has no fixed vector and the character is trivial on lambda  -> N = 0.")
print("  spin-0 sectors ((1,35) of the 78, (1,15) of the 27 -- Q, u^c, e^c, H_u, D and the SU(6) roots): cusp-fixed iff z_w = 1, i.e. the trivial local system  -> N = 0; charged with z_w != 1 -> torus acyclic -> N = 0.")
print("  spin-1 sector ((3,1): the SL(2)_beta adjoint = Ad rho): cusp-fixed and non-trivial -- the only sector that can carry an index, and it is Standard-Model-neutral.")
print("  => with the Standard Model unbroken, no SM-charged bulk sector of m004 carries a chiral index in the seat's frame: L216 negative there.")
# which SM-charged sectors can be made massless (vector-like pairs) by tuning (s, t): spin 0 at the golden characters, spin 1/2 at the twisted roots
print("\n  bonus -- the spectrum at special characters (vector-like zero modes, by the Alexander roots): a spin-0 sector of weight w is massless iff exp(2 pi i (s Y_w + t gamma_w)) in {phi^2, phi^-2};")
print("  a spin-1/2 sector iff the character hits a twisted-Alexander root; two complex parameters allow two independent weights at once, e.g. a doublet (1,2)_{1/2} weight at phi^2 with every triplet weight off the roots: the object's own doublet-triplet split (cf. B1302), vector-like.")

# ---------------------------------------------------------------- (F) the frame theorem: the 10 and the 5bar of SU(5) never share a spin
print("\n=== (F) the frame theorem: in each matter frame exactly one of the 10 and the 5bar of SU(5) sits in spin-0 sectors ===")
def su5_piece(t):
    col, wk, y = t
    if (col, wk) == ("colour", "doublet") and abs(y) == Fr(1, 6): return "10 (Q-type)"
    if (col, wk) == ("colour", "1") and abs(y) == Fr(2, 3): return "10 (u^c-type)"
    if (col, wk) == ("1", "1") and abs(y) == 1: return "10 (e^c-type)"
    if (col, wk) == ("colour", "1") and abs(y) == Fr(1, 3): return "5bar (d^c-type) / 5 (D-type)"
    if (col, wk) == ("1", "doublet") and abs(y) == Fr(1, 2): return "5bar (L-type) / 5 (H-type)"
    if (col, wk) == ("colour", "doublet") and abs(y) == Fr(5, 6): return "24 (X, Y)"
    if (col, wk) == ("1", "1") and y == 0: return "1 (N, nu^c-type)"
    return str(t)
def frame(name, spin0, spinh):
    c0 = Counter(su5_piece(sm_type(w)) for w in spin0); ch = Counter(su5_piece(sm_type(w)) for w in spinh)
    print(f"  {name}: spin-0 sectors carry {dict(c0)}; spin-1/2 sectors carry {dict(ch)}")
    ten0 = any(k.startswith("10") for k in c0); five0 = any(k.startswith("5bar") for k in c0)
    tenh = any(k.startswith("10") for k in ch); fiveh = any(k.startswith("5bar") for k in ch)
    return ten0, five0, tenh, fiveh
f27 = frame("27 = (1,15) + (2,6bar)", spin27[0], [w for w in spin27[1] if dot(w, beta) == 1])
f78 = frame("78 = (1,35) + (2,20) (charged part)", nonsm, [r for r in spin78[1] if dot(r, beta) == 1])
print(f"  27-frame: the 10 in spin 0 ({f27[0]}), the 5bar in spin 1/2 ({f27[3]}); 78-frame: the 10 in spin 1/2 ({f78[2]}), the 5bar in spin 0 ({f78[1]})")
print("  spin-0 sectors carry a character only: cusp-fixed iff the character is trivial (no Higgs field) -> N = 0 for every flat connection of the family,")
print("  whatever the SL(2)_beta part; so in either frame one half of every generation is never chiral, and a chiral generation needs both halves.")

# ---------------------------------------------------------------- (G) the rest of the character variety: where could a spin-1/2 sector be cusp-fixed?
print("\n=== (G) the lambda-parabolic points of the character variety (tr rho(lambda) = 2), where spin-1/2 sectors could be cusp-fixed ===")
m, y = sp.symbols('m y')
A_ = sp.Matrix([[m, 1], [0, 1 / m]]); B_ = sp.Matrix([[m, 0], [-y, 1 / m]])          # Riley's normal form for a two-bridge knot group
Rm = sp.simplify(word_matrix(REL, A_, B_) - sp.eye(2))
entries = [sp.factor(sp.simplify(e)) for e in Rm]
# Riley's theorem: the relator holds iff one polynomial Phi(m, y) vanishes; take the gcd of the numerators of the entries
nums = [sp.numer(sp.together(e)) for e in entries if e != 0]
Phi = nums[0]
for q in nums[1:]:
    Phi = sp.gcd(Phi, q)
Phi = sp.factor(Phi)
print(f"  Riley polynomial Phi(m, y) = {Phi}")
Lm = sp.simplify(word_matrix(LONG, A_, B_)); trL = sp.simplify(Lm.trace())
print(f"  tr rho(lambda) as a function on the variety: {sp.factor(sp.together(trL))}")
# the geometric point: m = 1, y = -u (Riley's y here is -u for a -> [[1,1],[0,1]], b -> [[1,0],[u,1]])
print(f"  at the geometric point (m = 1, y = -u): Phi = {sp.simplify(Phi.subs({m: 1, y: -u}))}, tr lambda = {sp.simplify(trL.subs({m: 1, y: -u}))}")
# solve Phi = 0, tr lambda = 2 : eliminate y by resultant
res = sp.factor(sp.resultant(sp.numer(sp.together(Phi)), sp.numer(sp.together(trL - 2)), y))
print(f"  resultant in m of (Phi, tr lambda - 2): {res}")
sols = []
PhiN = sp.numer(sp.together(Phi)); trN = sp.numer(sp.together(trL - 2))
for fac, mult in sp.factor_list(res)[1]:
    if not fac.has(m) or fac == m: continue
    for r in sp.roots(sp.Poly(fac, m)):            # exact roots: m = +-i, (+-1 +- sqrt 5)/2
        for yy in sp.roots(sp.Poly(sp.expand(PhiN.subs(m, r)), y)):
            ok = sp.simplify(trN.subs({m: r, y: yy})) == 0
            if ok: sols.append((r, yy))
sols = sorted(set(sols), key=lambda t: (abs(complex(sp.N(t[0]))), complex(sp.N(t[0])).real, complex(sp.N(t[1])).real))
print(f"  points with tr rho(lambda) = 2: {len(sols)}")
for (mm, yy) in sols:
    Lex = sp.simplify(Lm.subs({m: mm, y: yy}))
    unip = sp.simplify(Lex - sp.eye(2)) == sp.zeros(2)
    mmc, yyc = complex(sp.N(mm)), complex(sp.N(yy))
    print(f"    m = {mm} ~ {mmc.real:+.4f}{mmc.imag:+.4f}i (|m| = {abs(mmc):.4f}), y = {yy} ~ {yyc.real:+.4f}{yyc.imag:+.4f}i, irreducible (y != 0): {sp.simplify(yy) != 0}, rho(lambda) = identity: {unip}, rho(lambda) = {Lex.tolist()}")
print("  a spin-1/2 sector with character z = m^-1 (or m) on the fixed line of rho(a) would be cusp-fixed at such a point;")
print("  these are the only points where the spin-1/2 half could be chiral; the spin-0 half is never chiral anywhere (F), so no point of the variety gives a chiral generation.")

print("\nDONE")
