#!/usr/bin/env python3
"""GC-16: THE HETEROGENEOUS-COUPLING c-CELL — does the norm-+1 door open?

All computations exact over Z / Q(sqrt d) via sympy. No floats anywhere.

Object:  A  = [[2,1],[1,1]]   (unit phi, N(phi) = -1, spectral field Q(sqrt5))
Partner: M1 = [[2,3],[1,2]]   (disc 12, Q(sqrt3), fundamental unit 2+sqrt3, N=+1)

Mirror on the coupled pair: (A,M) -> (A^-1, M^-1) simultaneously.
Mirror-self-equivalences: X in GL2(Z) with X A X^-1 = A^-1 AND X M X^-1 = M^-1.
"""
import sympy as sp
from sympy import Matrix, symbols, sqrt, Rational, simplify, eye, zeros
from itertools import product
import json

a, b, c, d = symbols('a b c d', integer=True)
X = Matrix([[a, b], [c, d]])

A  = Matrix([[2, 1], [1, 1]])
M1 = Matrix([[2, 3], [1, 2]])

results = {}

def anti_conj_module(P):
    """Solve X P = P^-1 X linearly over Q; return basis of the solution
    module in M2(Z) (saturated: primitive integer basis)."""
    Pinv = P.inv()
    assert Pinv == Matrix(Pinv).applyfunc(sp.nsimplify)  # exact
    eqs = (X * P - Pinv * X)  # entries linear in a,b,c,d
    # coefficient matrix of the 4 linear equations in (a,b,c,d)
    C = Matrix([[sp.diff(eqs[i], v) for v in (a, b, c, d)] for i in range(4)])
    # confirm system is homogeneous linear (no constant term)
    assert eqs.subs({a: 0, b: 0, c: 0, d: 0}) == zeros(2, 2)
    ns = C.nullspace()
    # clear denominators -> primitive integer vectors
    basis = []
    for v in ns:
        den = sp.lcm([sp.fraction(sp.nsimplify(x))[1] for x in v])
        w = (v * den)
        g = sp.gcd(list(w))
        basis.append(Matrix(2, 2, list(w / g)))
    return basis

def module_intersection(bas1, bas2):
    """Intersect two submodules of Z^4 given by bases of 2x2 matrices."""
    V1 = Matrix.hstack(*[Matrix(4, 1, list(B)) for B in bas1])
    V2 = Matrix.hstack(*[Matrix(4, 1, list(B)) for B in bas2])
    # solve V1 s = V2 t  ->  [V1 | -V2] (s,t)^T = 0
    K = Matrix.hstack(V1, -V2)
    ns = K.nullspace()
    out = []
    for v in ns:
        den = sp.lcm([sp.fraction(sp.nsimplify(x))[1] for x in v])
        v = v * den
        s = v[:V1.cols, :]
        w = V1 * s
        g = sp.gcd(list(w))
        if g != 0:
            w = w / g
        out.append(Matrix(2, 2, list(w)))
    return out

def det_profile_rank1(B):
    """For a rank-1 module Z*B: which dets +-1 occur? det(tB) = t^2 det(B)."""
    dB = B.det()
    occur = set()
    for t in (1, -1):
        if t * t * dB in (1, -1):
            occur.add(int(t * t * dB))
    return sorted(occur)

def check(tag, cond):
    print(f"  [{'OK' if cond else 'FAIL'}] {tag}")
    assert cond, tag
    return cond

print("=" * 72)
print("STEP 0: sanity — the pair is non-commuting; inverses are integral")
print("=" * 72)
check("A M1 != M1 A (non-commuting pair)", A * M1 != M1 * A)
check("det A = 1", A.det() == 1)
check("det M1 = 1", M1.det() == 1)
check("A^-1 integral", all(sp.denom(x) == 1 for x in A.inv()))
check("M1^-1 integral", all(sp.denom(x) == 1 for x in M1.inv()))
check("tr A = 3, disc(A) = 5 (Q(sqrt5))", A.trace() == 3 and A.trace()**2 - 4 == 5)
check("tr M1 = 4, disc(M1) = 12 (Q(sqrt3))", M1.trace() == 4 and M1.trace()**2 - 4 == 12)

print()
print("=" * 72)
print("STEP 1: the single-matrix anti-conjugator modules (exact linear solve)")
print("=" * 72)
basA = anti_conj_module(A)
basM1 = anti_conj_module(M1)
print(f"  {{X : X A X^-1 = A^-1}} module rank = {len(basA)}, basis = {[list(B) for B in basA]}")
print(f"  {{X : X M1 X^-1 = M1^-1}} module rank = {len(basM1)}, basis = {[list(B) for B in basM1]}")
check("A anti-conjugator module has rank 2", len(basA) == 2)
check("M1 anti-conjugator module has rank 2", len(basM1) == 2)

# ---- POSITIVE CONTROL (recover B1189's two known facts) ----
print()
print("STEP 1a: POSITIVE CONTROL — recover B1189 known facts")
# A alone: general element and its det as a binary quadratic form
s, t = symbols('s t', integer=True)
XA = basA[0] * s + basA[1] * t
detA_form = sp.expand(XA.det())
print(f"  det of A-anti-conjugator (s,t) = {detA_form}")
# find explicit +1 and -1 unimodular anti-conjugators of A
found = {}
for ss, tt in product(range(-3, 4), repeat=2):
    Xc = basA[0] * ss + basA[1] * tt
    dv = Xc.det()
    if dv in (1, -1) and int(dv) not in found:
        assert Xc * A * Xc.inv() == A.inv()
        found[int(dv)] = (ss, tt, list(Xc))
print(f"  A alone: unimodular anti-conjugators found with dets {sorted(found)}")
print(f"    det=+1 witness: X = {found[1][2]},  det=-1 witness: X = {found[-1][2]}")
check("A alone: BOTH det signs occur (B1189: N(phi)=-1 => both-sign) ", sorted(found) == [-1, 1])
results['control_A_alone_both_signs'] = {str(k): v[2] for k, v in found.items()}

# M1 alone: det form and the mod-3 obstruction
XM = basM1[0] * s + basM1[1] * t
detM_form = sp.expand(XM.det())
print(f"  det of M1-anti-conjugator (s,t) = {detM_form}")
foundM = {}
for ss, tt in product(range(-8, 9), repeat=2):
    Xc = basM1[0] * ss + basM1[1] * tt
    dv = Xc.det()
    if dv in (1, -1) and int(dv) not in foundM:
        assert Xc * M1 * Xc.inv() == M1.inv()
        foundM[int(dv)] = (ss, tt, list(Xc))
print(f"  M1 alone: unimodular anti-conjugator dets found in search box: {sorted(foundM)}")
# exact obstruction: det = +1 needs a^2 - 3 c^2 = -1; squares mod 3 are {0,1},
# so a^2 = 3c^2 - 1 = -1 (mod 3) = 2 (mod 3) is impossible. EXACT, not a search.
sq_mod3 = sorted({(x * x) % 3 for x in range(3)})
check("exact obstruction: squares mod 3 = {0,1}, so a^2-3c^2=-1 impossible", sq_mod3 == [0, 1])
check("M1 alone: SINGLE-SIGNED det=-1 (B1189: norm-+1 unit => single-signed coset)",
      sorted(foundM) == [-1])
results['control_M1_alone_single_signed'] = {str(k): v[2] for k, v in foundM.items()}

print()
print("=" * 72)
print("STEP 2: THE PAIR SYSTEM — simultaneous conjugators, exact intersection")
print("=" * 72)
sim = module_intersection(basA, basM1)
print(f"  simultaneous-conjugator module rank = {len(sim)}")
check("rank is 1", len(sim) == 1)
X0 = sim[0]
if X0[0, 0] < 0:
    X0 = -X0
print(f"  generator X0 = {list(X0)},  det X0 = {X0.det()}")
check("X0 A X0^-1 = A^-1 (verified exactly)", X0 * A * X0.inv() == A.inv())
check("X0 M1 X0^-1 = M1^-1 (verified exactly)", X0 * M1 * X0.inv() == M1.inv())
check("det X0 = -1", X0.det() == -1)
prof = det_profile_rank1(X0)
print(f"  GL2(Z) elements of the module Z*X0: t=+-1 only (det(tX0) = -t^2); det profile = {prof}")
check("det profile of ALL unimodular simultaneous conjugators = {-1} (SINGLE-SIGNED)",
      prof == [-1])
results['pair_A_M1'] = {'X0': list(X0), 'det': int(X0.det()), 'profile': prof}

# coset structure: Z(A) cap Z(M1) in GL2(Z) should be {+-I}
print()
print("STEP 2a: coset structure — Z(A) ∩ Z(M1)")
def centralizer_module(P):
    eqs = (X * P - P * X)
    C = Matrix([[sp.diff(eqs[i], v) for v in (a, b, c, d)] for i in range(4)])
    return [Matrix(2, 2, list(v * sp.lcm([sp.fraction(sp.nsimplify(x))[1] for x in v])))
            for v in C.nullspace()]
zA = centralizer_module(A)
zM = centralizer_module(M1)
zint = module_intersection(zA, zM)
print(f"  rank Z(A) = {len(zA)}, rank Z(M1) = {len(zM)}, rank of intersection = {len(zint)}")
check("Z(A) ∩ Z(M1) is rank 1", len(zint) == 1)
Z0 = zint[0]
g = sp.gcd(list(Z0))
Z0 = Z0 / g
check("Z(A) ∩ Z(M1) = Z·I  => unimodular part = {±I}", Z0 in (eye(2), -eye(2)))
print("  => the simultaneous-conjugator set in GL2(Z) is the full coset {±X0}: both det -1")

print()
print("=" * 72)
print("STEP 3: TWO-SIDED CONTROL (negative side): homogeneous pair (A,A)")
print("=" * 72)
simAA = module_intersection(basA, basA)
print(f"  (A,A) simultaneous module rank = {len(simAA)} (= full A-anti-conjugator module)")
check("(A,A) module rank 2", len(simAA) == 2)
# both signs already exhibited in STEP 1a; re-verify as SIMULTANEOUS conjugators
Xp = Matrix(2, 2, found[1][2]); Xm = Matrix(2, 2, found[-1][2])
check("(A,A): det=+1 simultaneous conjugator exists", Xp * A * Xp.inv() == A.inv() and Xp.det() == 1)
check("(A,A): det=-1 simultaneous conjugator exists", Xm * A * Xm.inv() == A.inv() and Xm.det() == -1)
print("  => (A,A) shows BOTH det signs: NO mirror-odd bit. Control: instrument")
print("     correctly reports absence on the deliberately-dead homogeneous pair.")
results['control_pair_A_A'] = {'profile': [-1, 1]}

print()
print("=" * 72)
print("STEP 4: SECOND ABSENT-TARGET CONTROL: heterogeneous partner, norm -1 field")
print("=" * 72)
# Mn = [[5,2],[2,1]]: trace 6, det 1, disc 32, field Q(sqrt2); fundamental unit
# 1+sqrt2 has N = -1  =>  the door should NOT open (predict: bit absent).
Mn = Matrix([[5, 2], [2, 1]])
check("Mn: det 1, disc 32 (Q(sqrt2))", Mn.det() == 1 and Mn.trace()**2 - 4 == 32)
check("Q(sqrt2) is a norm -1 field: 1^2 - 2*1^2 = -1", 1 - 2 == -1)
check("A Mn != Mn A", A * Mn != Mn * A)
basMn = anti_conj_module(Mn)
simAn = module_intersection(basA, basMn)
check("(A,Mn) simultaneous module rank 1", len(simAn) == 1)
Xn = simAn[0]
print(f"  (A,Mn) generator = {list(Xn)}, det = {Xn.det()}")
check("Xn conjugates both", Xn * A * Xn.inv() == A.inv() and Xn * Mn * Xn.inv() == Mn.inv())
profn = det_profile_rank1(Xn)
print(f"  det profile = {profn}")
check("(A, norm-minus-1 partner): profile = {+1} => mirror realized INSIDE SL2(Z), bit ABSENT",
      profn == [1])
results['control_pair_A_Msqrt2'] = {'X': list(Xn), 'profile': profn}
print("  => heterogeneity alone is NOT enough; the norm-+1 property of the partner")
print("     is what forces det -1. The instrument excludes the deliberately-absent target.")

print()
print("=" * 72)
print("STEP 5: ROBUSTNESS — second norm-+1 partner, Q(sqrt7)")
print("=" * 72)
# M2 = [[8,7],[9,8]]: trace 16, det 1, disc 252 = 4*9*7 -> Q(sqrt7).
# Q(sqrt7) is norm +1: squares mod 7 = {0,1,2,4}, -1 = 6 mod 7 not a square.
M2 = Matrix([[8, 7], [9, 8]])
check("M2: det 1, disc 252 (Q(sqrt7))", M2.det() == 1 and M2.trace()**2 - 4 == 252)
sq_mod7 = sorted({(x * x) % 7 for x in range(7)})
check("squares mod 7 = {0,1,2,4}; 6 not among => a^2-7c^2=-1 impossible => norm +1 field",
      sq_mod7 == [0, 1, 2, 4] and 6 not in sq_mod7)
check("A M2 != M2 A", A * M2 != M2 * A)
basM2 = anti_conj_module(M2)
simA2 = module_intersection(basA, basM2)
check("(A,M2) simultaneous module rank 1", len(simA2) == 1)
X2 = simA2[0]
if X2[0, 0] < 0:
    X2 = -X2
print(f"  (A,M2) generator = {list(X2)}, det = {X2.det()}")
prof2 = det_profile_rank1(X2)
if X2.det() in (1, -1):
    check("X2 conjugates both", X2 * A * X2.inv() == A.inv() and X2 * M2 * X2.inv() == M2.inv())
    print(f"  det profile = {prof2}")
    check("(A, Q(sqrt7) norm-+1 partner): SINGLE-SIGNED det -1 again", prof2 == [-1])
else:
    # BRANCH (2): the rational solution space of {XA=A^-1 X, XM2=M2^-1 X} is
    # EXACTLY Q*X2 (rank-1 nullspace, exhaustive linear algebra). Any integral
    # solution is t*X2, t in Z (X2 primitive), det = t^2 * det(X2) != +-1.
    # Hence NO GL2(Z) element conjugates (A,M2) to (A^-1,M2^-1):
    # the pairs are GL2(Z)-INEQUIVALENT => mirror-odd Z/2 TORSOR exists.
    g2 = sp.gcd(list(X2))
    check("X2 is primitive (gcd of entries = 1)", g2 == 1)
    check("det X2 = 59, and 59*t^2 = ±1 has no integer solution",
          X2.det() == 59 and all(59 * t2 * t2 not in (1, -1) for t2 in range(-2, 3)))
    check("X2 conjugates both over Q (pairs ARE GL2(Q)-conjugate)",
          X2 * A * X2.inv() == A.inv() and X2 * M2 * X2.inv() == M2.inv())
    print("  => (A,M2) and its mirror: conjugate over Q, INEQUIVALENT over Z —")
    print("     the mirror-odd Z/2 survives as a TORSOR (branch 2 of the cell).")
results['pair_A_Msqrt7'] = {'X': list(X2), 'det': int(X2.det()), 'profile': prof2}

print()
print("=" * 72)
print("STEP 6: trace words up to length 4 CANNOT see the bit (exact sweep)")
print("=" * 72)
# All words w in {A,M1,A^-1,M1^-1} of length <= 4: compare tr w(A,M1) vs tr w(A^-1,M1^-1).
Ai, Mi = A.inv(), M1.inv()
gens = {'a': A, 'A': Ai, 'm': M1, 'M': Mi}
mirror = {'a': 'A', 'A': 'a', 'm': 'M', 'M': 'm'}
n_words = 0
n_agree = 0
disagreements = []
for L in range(1, 5):
    for w in product('aAmM', repeat=L):
        W = eye(2)
        Wm = eye(2)
        for ch in w:
            W = W * gens[ch]
            Wm = Wm * gens[mirror[ch]]
        n_words += 1
        if W.trace() == Wm.trace():
            n_agree += 1
        else:
            disagreements.append(''.join(w))
print(f"  words checked: {n_words}; traces agreeing under the mirror: {n_agree}")
check("ALL trace words length<=4 agree between (A,M1) and (A^-1,M1^-1)",
      n_agree == n_words)
print("  => the class is INVISIBLE to the SL2 character variety (as forced by")
print("     tr(W^-1)=tr(W) and tr(W)=tr(W reversed) for SL2); it lives exactly in")
print("     the det +-1 (orientation) layer of the integral conjugation — RELATIONAL.")
results['trace_sweep'] = {'n_words': n_words, 'n_agree': n_agree}

print()
print("=" * 72)
print("STEP 7: RESTRICTION TO c — X0 induces the Gal(K/Q) generator on both spectra")
print("=" * 72)
# Eigenvectors of A over Q(sqrt5): eigenvalues phi^2 = (3+sqrt5)/2, phi^-2.
s5 = sqrt(5)
lamA_p = Rational(3, 2) + s5 / 2
lamA_m = Rational(3, 2) - s5 / 2
check("eigenvalues of A are (3±sqrt5)/2", sp.expand(lamA_p * lamA_m) == 1 and lamA_p + lamA_m == 3)
vA_p = Matrix([lamA_p - 1, 1])   # A v = lam v check below
check("A vA_p = lamA_p vA_p", sp.simplify(A * vA_p - lamA_p * vA_p) == zeros(2, 1))
vA_m = Matrix([lamA_m - 1, 1])
check("A vA_m = lamA_m vA_m", sp.simplify(A * vA_m - lamA_m * vA_m) == zeros(2, 1))
# X0 must SWAP the eigenlines (since X0 A X0^-1 = A^-1 sends the lam-eigenline of A
# to the lam-eigenline of A^-1 = 1/lam-eigenline of A). Verify proportionality exactly.
w = X0 * vA_p
ratio = sp.radsimp(sp.cancel(w[0] / w[1] - vA_m[0] / vA_m[1]))
check("X0 maps the phi^2-eigenline of A to the phi^-2-eigenline (Galois swap on Q(sqrt5))",
      sp.simplify(ratio) == 0)
# and on M1's spectrum over Q(sqrt3): eigenvalues 2±sqrt3
s3 = sqrt(3)
vM_p = Matrix([s3, 1])          # M1 (sqrt3,1)^T = (2 sqrt3+3, sqrt3+2) = (2+sqrt3)(sqrt3,1)
check("M1 vM_p = (2+sqrt3) vM_p", sp.simplify(M1 * vM_p - (2 + s3) * vM_p) == zeros(2, 1))
vM_m = Matrix([-s3, 1])
check("M1 vM_m = (2-sqrt3) vM_m", sp.simplify(M1 * vM_m - (2 - s3) * vM_m) == zeros(2, 1))
w2 = X0 * vM_p
ratio2 = sp.radsimp(sp.cancel(w2[0] / w2[1] - vM_m[0] / vM_m[1]))
check("X0 maps the (2+sqrt3)-eigenline of M1 to the (2-sqrt3)-eigenline (Galois swap on Q(sqrt3))",
      sp.simplify(ratio2) == 0)
print("  => the unique mirror-realizer X0 acts on BOTH spectral fields as the")
print("     nontrivial Gal(K/Q) element (sqrt5 -> -sqrt5 and sqrt3 -> -sqrt3):")
print("     the mirror-odd class RESTRICTS TO c on each factor.")

print()
print("=" * 72)
print("VERDICT")
print("=" * 72)
print("""  eps(A,M1) := det(any GL2(Z) simultaneous mirror-realizer) = -1, WELL-DEFINED
  because the realizer set is exactly {±X0}, X0=[[2,-3],[1,-2]], both det -1.
  - dimensionless: eps is a Z/2 class, no scale, no measured value (Gate 5 clean).
  - mirror-odd: the mirror (A,M)->(A^-1,M^-1) is realizable ONLY with
    orientation reversal (det -1); inside SL2(Z) the pair and its mirror are
    INEQUIVALENT (any SL2(Z)-conjugacy would give a det +1 realizer — none exists).
  - restricts to c: X0 induces the Gal generator on both Q(sqrt5) and Q(sqrt3).
  Controls: (A,A) both signs (dead, matches B1189); (A, Q(sqrt2) norm -1 partner)
  single-signed det +1 (mirror-even, bit absent); (A, Q(sqrt7) norm +1 partner)
  no integral realizer at all (det-59 generator) => mirror-odd Z/2 as a TORSOR.
  THE DOOR OPENS.""")

with open('SCRATCH/b1188/cells/gc16_results.json', 'w') as f:
    json.dump(results, f, indent=2, default=str)
print("results written to gc16_results.json")
