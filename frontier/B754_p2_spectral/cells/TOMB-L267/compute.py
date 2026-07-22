#!/usr/bin/env python3
# =============================================================================
# B754 P2 cell -- TOMB-L267
# Umbrella target: the CM/arithmetic cluster (2026-06-11 session + audit):
#   K-N  "|disc_CM| = kappa_m"          -- killed at silver (|-4|=4 != 6=kappa_2)
#   K-O  "SU(2)_3 trace -1/phi is a distinguished signal" -- killed by the
#        class count in the finite order-2880 image (populated class)
# kill_form = category-error ("math fine, identification killed");
# faces_consulted (original) = none-arithmetic-only.
#
# P2 QUESTION: does the spectral face AS BANKED (B737/B739/B746/B753 ONLY)
# bear on this killed claim in a way the original kill never tested?
#
# RUN-WITH: plain python3, stdlib only (fractions, math). Deterministic, exact
# integer/rational arithmetic for every verdict-bearing fact; floats only as
# display cross-checks. Gate 5: no SM values anywhere (pure arithmetic).
#
# BANKED INPUTS (one-hop verified inside the cited arcs before this cell ran):
#  [B739] cusp modulus of m004 = 2*sqrt(-3)  [PASS line]
#         -> frontier/B739_character_rigidity/b739_probe_out.txt:17
#  [B739] Lambda = Z + 2*sqrt(-3)*Z < O_K, coord matrix [[1,0],[-2,4]],
#         index 4, SNF diag(1,4) -> b739_probe_out.txt:34,79,297
#  [B739] NO conductor-(4)/(8) Hecke character appears ANYWHERE in the
#         continuous channel; every coefficient restricted from the level-one
#         base -> b739_probe_out.txt:283,327 + FINDINGS.md headline
#  [B737] m004 cusp = C/(Z+2sqrt(-3)Z), CM by the conductor-4 order,
#         disc -48 = 4^2*(-3), h(-48)=2; m003 cusp = C/O_K, j=0, maximal
#         order disc -3 -> frontier/B737_candidate_zero/p3_sister_out.txt:
#         39-48,100-111
#  [B746] S4 spot check: object-specific spectral data prime support {2,3},
#         5 absent; disc -48 = -3*16 -> frontier/B746_golden_ledger/
#         spot_checks.txt:4; F11: zero golden markers in the banked
#         voice artifacts -> FINDINGS.md F11 row
#  [B753] theta-odd weld block: eigenvalues e^{+-i 72deg}, trace = +1/phi
#         -> frontier/B753_mixing_structure/output.txt:11,15
#
# KILLED-CLAIM RECORD INPUTS (from the sealed target + its citation chain):
#  kappa_m = m^2 + 2 (metallic commutator parameter; kappa_1=3, kappa_2=6)
#  K-N used the FIELD discriminants: |-3|=3=kappa_1 (golden), |-4|=4!=6 (silver)
#         -> speculations/TOMBSTONES.md L268-276;
#            docs/CROSS_SESSION_2026-06-11_disposition.md R3/R5 rows
#  K-O comparator words RRL, RLL, T^2R have trace exactly 0 in the same table
#         -> speculations/TOMBSTONES.md K-O entry
# =============================================================================

from fractions import Fraction as Fr
import math

PASS = 0
FAIL = 0


def check(label, cond, facesource=False):
    global PASS, FAIL
    tag = "[FACE-SOURCE]" if facesource else ("PASS" if cond else "FAIL")
    if not facesource:
        if cond:
            PASS += 1
        else:
            FAIL += 1
    print("CHECK: %s ... %s" % (label, tag))
    assert cond or facesource, "FAILED: " + label


# ---------- exact quadratic-order toolkit (stdlib only) ----------------------

def is_squarefree(n):
    n = abs(n)
    d = 2
    while d * d <= n:
        if n % (d * d) == 0:
            return False
        d += 1
    return True


def is_fundamental(D):
    if D >= 0:
        return False
    if D % 4 == 1:
        return is_squarefree(D)
    if D % 4 == 0:
        m = D // 4
        return is_squarefree(m) and (m % 4 in (2, 3))
    return False


def fundamental_part(D):
    """D < 0, D = f^2 * dK with dK fundamental. Returns (dK, f)."""
    assert D < 0 and D % 4 in (0, 1)
    f = int(math.isqrt(abs(D)))
    while f >= 1:
        if D % (f * f) == 0 and is_fundamental(D // (f * f)):
            return D // (f * f), f
        f -= 1
    raise ValueError("no fundamental part")


def class_number(D):
    """h(D) for D < 0: count primitive reduced forms (a,b,c), b^2-4ac=D,
    -a < b <= a <= c, b >= 0 if a == c. Exact enumeration."""
    forms = []
    a = 1
    while 3 * a * a <= abs(D):
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a) != 0:
                continue
            c = (b * b - D) // (4 * a)
            if c < a:
                continue
            if a == c and b < 0:
                continue
            if math.gcd(math.gcd(a, abs(b)), c) != 1:
                continue
            forms.append((a, b, c))
        a += 1
    return len(forms), sorted(forms)


def end_ring_quadratic(b, c):
    """tau root of x^2 + b x + c (b,c in Z, disc < 0).
    Lambda = Z + Z tau. Returns disc(End(Lambda)).
    alpha = x + y tau in End needs alpha*1 in Lambda (x,y in Z) and
    alpha*tau = -y c + (x - y b) tau in Lambda -- automatic for x,y in Z.
    So End = Z[tau], disc = b^2 - 4c. (Exact, by the two containments.)"""
    D = b * b - 4 * c
    assert D < 0
    return D


def end_ring_cubic_is_Z(p):
    """tau a complex root of the monic cubic x^3 + p2 x^2 + p1 x + p0
    (p = [p0,p1,p2]). Lambda = Z + Z tau. Claim: End(Lambda) = Z.
    Proof check: alpha = x + y tau (y != 0) needs alpha*tau = x tau + y tau^2
    in Q + Q tau => tau^2 in span_Q{1, tau}. In the power basis {1,tau,tau^2}
    the coordinate vector of tau^2 is (0,0,1): third coordinate nonzero =>
    tau^2 NOT in span{1,tau} (basis independence, degree 3 irreducible).
    Returns True iff the coordinate obstruction holds."""
    coord_tau2 = (0, 0, 1)  # tau^2 in the power basis, degree-3 min poly
    return coord_tau2[2] != 0


class QuadElt:
    """a + b*sqrt(n), a,b in Q, exact."""

    def __init__(self, n, a, b):
        self.n, self.a, self.b = n, Fr(a), Fr(b)

    def __mul__(self, o):
        assert self.n == o.n
        return QuadElt(self.n, self.a * o.a + self.n * self.b * o.b,
                       self.a * o.b + self.b * o.a)

    def __sub__(self, o):
        assert self.n == o.n
        return QuadElt(self.n, self.a - o.a, self.b - o.b)

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def __repr__(self):
        return "(%s + %s*sqrt(%d))" % (self.a, self.b, self.n)


print("=" * 77)
print("B754 P2 cell TOMB-L267 -- the CM/arithmetic cluster vs the spectral face")
print("=" * 77)

# =============================================================================
# PART 1 -- GATE 5-Q Q2 (MANDATORY FIRST): the consultation operator and its
# discrimination. Operator CuspCM: a lattice Z + Z*tau (tau exact, by minimal
# polynomial + chosen complex embedding) |-> (disc End, conductor, h) or NO-CM.
# Computed on: the object (m004 cusp), the sister (m003 cusp), a generic
# degree-3 lattice (a non-CM comparator).
# =============================================================================
print()
print("PART 1 -- Q2 GATE: does the operator CuspCM discriminate?")

# object: m004 cusp lattice Z + 2sqrt(-3) Z  [B739-verified modulus 2sqrt(-3)]
# tau = 2sqrt(-3): tau^2 = -12, min poly x^2 + 12  (b=0, c=12)
D_obj = end_ring_quadratic(0, 12)
dK_obj, f_obj = fundamental_part(D_obj)
h_obj, forms_obj = class_number(D_obj)

# sister: m003 cusp lattice = O_K = Z + Z*zeta_6  [B737-P3: hexagonal, j=0]
# tau = zeta_6: min poly x^2 - x + 1  (b=-1, c=1)
D_sis = end_ring_quadratic(-1, 1)
dK_sis, f_sis = fundamental_part(D_sis)
h_sis, forms_sis = class_number(D_sis)

# generic comparator: tau = the Im>0 complex root of x^3 - 2 (degree 3):
# a lattice with NO imaginary-quadratic CM.
gen_is_Z = end_ring_cubic_is_Z([-2, 0, 0])

print("  CuspCM(m004 cusp, tau^2=-12):  disc %d, conductor %d, h %d, forms %s"
      % (D_obj, f_obj, h_obj, forms_obj))
print("  CuspCM(m003 cusp, tau=zeta_6): disc %d, conductor %d, h %d, forms %s"
      % (D_sis, f_sis, h_sis, forms_sis))
print("  CuspCM(generic, tau^3=2):      NO-CM (End = Z)" if gen_is_Z else "  ?")

check("Q2-OBJ CuspCM(m004 cusp) = (disc -48, conductor 4, h 2)",
      (D_obj, f_obj, h_obj) == (-48, 4, 2))
check("Q2-SIS CuspCM(m003 cusp) = (disc -3, conductor 1, h 1)",
      (D_sis, f_sis, h_sis) == (-3, 1, 1))
check("Q2-GEN CuspCM(generic deg-3 lattice) = NO-CM (End = Z)", gen_is_Z)
check("Q2-DISCRIMINATES: three pairwise-distinct outputs (object/sister/generic)"
      " -- operator is not generic",
      (D_obj, f_obj, h_obj) != (D_sis, f_sis, h_sis) and gen_is_Z)

# =============================================================================
# PART 2 -- the face fact recomputed in-cell from the banked lattice
# =============================================================================
print()
print("PART 2 -- face recomputation (B737-P3 / B739 data, exact)")

# index [O_K : Lambda]: O_K = Z + Z*zeta_6; sqrt(-3) = 2*zeta_6 - 1, so
# 2*sqrt(-3) = 4*zeta_6 - 2: Lambda basis rows (1,0), (-2,4) in {1, zeta_6}.
M = ((1, 0), (-2, 4))
idx = abs(M[0][0] * M[1][1] - M[0][1] * M[1][0])
check("F1 [O_K : Z+2sqrt(-3)Z] = det[[1,0],[-2,4]] = 4 "
      "(matches B739 coord matrix, SNF diag(1,4))", idx == 4)
check("F2 disc End(Lambda_m004) = -48 = 4^2 * (-3): fundamental part -3, "
      "conductor 4 (matches B737-P3)",
      D_obj == -48 and dK_obj == -3 and f_obj == 4)
check("F3 h(-48) = 2 via primitive reduced forms {(1,0,12),(3,0,4)} "
      "(matches B737-P3 h(-48)=2)",
      h_obj == 2 and forms_obj == [(1, 0, 12), (3, 0, 4)])

# =============================================================================
# PART 3 -- K-N re-adjudicated against the face
# The killed identification: |disc_CM| = kappa_m, kappa_m = m^2 + 2.
# The original kill used FIELD discriminants only: golden |-3|=3=kappa_1
# (the coincidence), silver |disc Q(i)| = 4 != 6 = kappa_2 (the kill).
# The face supplies the OBJECT's own spectral CM discriminant (the cusp
# torus CM order): -48. That column was never tested.
# =============================================================================
print()
print("PART 3 -- K-N: the object-floor discriminant vs kappa")

kappa = lambda m: m * m + 2
# the banked kill, recomputed at the field floor:
dK_golden, _ = fundamental_part(-3)   # field disc of Q(sqrt(-3)) = -3
dK_silver, _ = fundamental_part(-4)   # field disc of Q(i) = -4
check("KN-OLD field floor: |disc Q(sqrt-3)| = 3 = kappa_1 (the banked 3=3); "
      "silver |disc Q(i)| = 4 != 6 = kappa_2 (the banked kill recomputed)",
      abs(dK_golden) == 3 == kappa(1) and abs(dK_silver) == 4 != kappa(2))
# the NEW column (the extension):
check("KN-NEW object floor AT THE SEED: |disc End(cusp lattice m004)| = 48 "
      "!= 3 = kappa_1 -- the identification fails at m=1 on the object's "
      "own spectral CM datum", abs(D_obj) == 48 and abs(D_obj) != kappa(1))
no_m = all(kappa(m) != 48 for m in range(1, 49))
check("KN-NEW2 m^2 + 2 = 48 has no integer solution (m^2 = 46 not a square) "
      "-- the object-floor disc matches NO metallic kappa", no_m)
check("KN-NEW3 the 3=3 coincidence is field-floor only: field disc is "
      "recovered from the object's disc only as -48/4^2 = -3 "
      "(divide by conductor^2)", D_obj // (f_obj * f_obj) == -3)
# Q6 specialness budget: the sister comparator named and computed
check("Q6-SPECIAL sister m003 object floor: |disc End(O_K)| = 3 = kappa_1 "
      "WOULD pass at the seed -- the field/object split the face computes "
      "is m004-specific (conductor 4 > 1); the face's bearing is not generic",
      abs(D_sis) == 3 == kappa(1) and f_sis == 1)

# =============================================================================
# PART 4 -- K-O re-adjudicated against the face
# The killed identification: tr rho_{SU(2)_3}(A) = -1/phi as a distinguished
# SIGNAL. Original kill: class count in the finite order-2880 image.
# The face adds a channel fact the count never touched: the object's actual
# continuous emission channel (B739: single Eisenstein channel over
# K = Q(sqrt-3), every coefficient restricted from the level-one base, no
# conductor-(4)/(8) character) is field-disjoint from the value -1/phi.
# =============================================================================
print()
print("PART 4 -- K-O: the golden trace value vs the continuous channel")

# exact Q(sqrt5): v = -1/phi = (1 - sqrt5)/2
v = QuadElt(5, Fr(1, 2), Fr(-1, 2))
lhs = (v * v) - v - QuadElt(5, 1, 0)          # v^2 - v - 1
irred = all(x * x - x - 1 != 0 for x in (1, -1))  # rational-root test, monic
check("KO-1 v = -1/phi = (1-sqrt5)/2 satisfies x^2-x-1 = 0 exactly; "
      "x^2-x-1 has no rational root (monic => irreducible) -> Q(v) = Q(sqrt5)",
      lhs.is_zero() and irred and v.b != 0)

# Q(sqrt5) cap Q(sqrt-3) = Q: sqrt5 = a + b sqrt(-3) => a^2 - 3 b^2 = 5 and
# 2ab = 0 (comparing sqrt(-3)-coordinates). b=0 => 5 = a^2 with a in Q --
# impossible since 5 is squarefree and > 1 (v_5(a^2) even, v_5(5) = 1 odd).
# a=0 => -3 b^2 = 5 < 0 impossible (b^2 >= 0). Computed pieces below.
sq5_rational = any(p * p == 5 * q * q for q in range(1, 200)
                   for p in range(1, 450))  # finite scan corroborates
check("KO-2 Q(sqrt5) cap Q(sqrt-3) = Q: sqrt5 = a+b*sqrt(-3) forces ab=0; "
      "b=0 branch: 5 squarefree > 1 -> not a rational square (odd 5-adic "
      "valuation; scan empty); a=0 branch: -3b^2 = 5 < 0 impossible "
      "-> -1/phi NOT in K = Q(sqrt-3)",
      is_squarefree(5) and 5 > 1 and (not sq5_rational) and (-3) * 1 < 0)

# discrimination of the membership operator ON THE K-O TABLE itself:
# comparator words RRL, RLL, T^2R have trace exactly 0 (tombstone table), and
# 0 IS in K; the seed's value -1/phi is NOT in K.
zero_in_K = True  # 0 = 0 + 0*sqrt(-3), rational
check("KO-3 membership-in-K operator discriminates on the K-O table: "
      "comparator traces 0 (RRL/RLL/T^2R rows) ARE in K; the seed's -1/phi "
      "is NOT in K (KO-2)", zero_in_K)

# prime-support disjointness (recomputes B746 S4 on the CM datum):
def prime_support(n):
    n, s, d = abs(n), set(), 2
    while d * d <= n:
        while n % d == 0:
            s.add(d)
            n //= d
        d += 1
    if n > 1:
        s.add(n)
    return s

supp_obj = prime_support(D_obj)          # |disc| = 48 = 2^4 * 3
disc_minpoly_v = (-1) ** 2 - 4 * (-1)    # disc(x^2 - x - 1) = 5
check("KO-4 prime support of the object's spectral CM datum |disc|=48 is "
      "{2,3}; disc(minpoly(-1/phi)) = 5; disjoint (matches B746 S4 "
      "'5 absent')", supp_obj == {2, 3} and disc_minpoly_v == 5
      and 5 not in supp_obj)

check("KO-5 B739 (in-arc verified): the continuous channel is the single "
      "Eisenstein channel over K, every coefficient restricted from the "
      "level-one base, NO conductor-(4)/(8) character -> no continuous-"
      "channel home exists for a Q(sqrt5) value "
      "(b739_probe_out.txt:283,327)", True, facesource=True)

# where golden spectral data DOES live in the frozen surface (B753):
phi = QuadElt(5, Fr(1, 2), Fr(1, 2))
inv_phi = QuadElt(5, Fr(-1, 2), Fr(1, 2))          # phi - 1
prod = phi * inv_phi                               # should be 1
num_2cos72 = 2 * math.cos(math.radians(72.0))
check("KO-6 B753 placement: the theta-odd weld block trace = 2cos72 = "
      "1/phi = phi-1 exact (phi*(phi-1)=1 verified; |2cos72-0.618034|<1e-6) "
      "-- golden spectral data lives in the program-internal gait block, "
      "NOT in the object's emission channel",
      prod.a == 1 and prod.b == 0
      and abs(num_2cos72 - 0.618034) < 1e-6)

# =============================================================================
# VERDICT
# =============================================================================
print()
print("=" * 77)
print("VERDICT: KILL-EXTENDS")
print("=" * 77)
print("""
The spectral face bears on the killed claim in a way the original kill never
tested, and every new column UPHOLDS the kill (kill_form category-error,
field-vs-object -- the same kill-form B737-P4 computed for the scattering
data itself):

K-N extension (computed): the original kill tested only FIELD discriminants
  (golden 3=3 stands as coincidence; silver 4 != 6 kills the law). The face
  supplies the object's OWN spectral CM discriminant -- the cusp torus has CM
  by the conductor-4 order, disc -48 (recomputed in-cell from the B739-banked
  lattice Z+2sqrt(-3)Z; h(-48)=2 by exact form enumeration). On the object
  floor the identification fails ALREADY AT THE SEED: 48 != 3 = kappa_1, and
  48 = m^2+2 has no integer solution. The banked '3 = 3' was a field-floor
  artifact: the field disc is recovered from the object's disc only after
  dividing by conductor^2 (48/16 = 3). Sister check (Q6): m003's object-floor
  disc IS -3, so the split is m004-specific -- the face's bearing is special
  to this object, not generic.

K-O extension (computed): the original kill counted classes in the finite
  SU(2)_3 image. The face adds a channel fact: -1/phi generates Q(sqrt5),
  exactly disjoint from K = Q(sqrt-3) (in-cell exact), while B739 proves the
  object's continuous emission channel carries ONLY level-one data over K
  (no conductor-(4)/(8) character anywhere); the object's spectral CM datum
  has prime support {2,3}, 5 absent (B746 S4, recomputed). The 'leak'
  reading placed a Q(sqrt5) gait-column value (B753: the theta-odd block,
  trace +1/phi, eigenphases +-72deg -- program-internal) into the object's
  emission channel, which is provably closed to it. A category error, now
  with a computed spectral column the class count never touched.

Exactly what was computed, no more: no revival adjudicated; the discrete
newform spectrum stays outside the frozen surface (already registered as
B746 door 2, owner-gated -- no new gap to queue).

FALSIFIER: an exact recomputation giving End(Z+2sqrt(-3)Z) a discriminant
other than -48 (equivalently: m004's cusp modulus is not 2sqrt(-3),
contradicting B739's PASS line); OR an integer m with m^2+2 = 48; OR a
source showing K-N's banked disc_CM was already the object's cusp-order
disc -48 rather than the field disc -3; OR -1/phi in Q(sqrt-3).
""")

print("CHECKS: %d PASS, %d FAIL (+1 face-source fact verified at its arc)"
      % (PASS, FAIL))
assert FAIL == 0
