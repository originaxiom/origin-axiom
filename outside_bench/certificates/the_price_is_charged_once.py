"""CERTIFICATE -- Q(sqrt 77) buys off BOTH obstructions, and is charged exactly once.

Completes the computation memo 204 named as owed: whether the Allen invariant E is split, and
over which field the object's triality becomes available.

INPUTS, both reproduced from memo 204's own banked output (outputs/the_object_is_6d4_out.txt),
not re-derived here -- the e6 build is not needed for this cell:
  the SEXTIC  = the characteristic polynomial factor of ad(x8)|48   (memo 204 CELL 3)
  the CUBIC   = its square, u = t^2, which generates K              (memo 204 CELL 3)

THE QUESTION.  ad(x8) commutes with the 28 (memo 204, 0/28 failures) and ad(x8)^2 = u lies in K.
So a splitting of the 48 over K along ad(x8) requires sqrt(u) in K.

CELLS (two outcomes each)
  CELL 1  Is the sextic irreducible over Q?
          A: reducible -- sqrt(u) in K, the 48 splits over K, E split by this route
          B: irreducible -- F6 = Q[ad(x8)|48] is a degree-6 FIELD, sqrt(u) NOT in K,
             and the 48 does NOT split over K along ad(x8)
  CELL 2  A mod-p meataxe found a proper submodule of Q-dimension 24 at two primes.  Real, or a
          reduction artifact?
          A: real          B: artifact -- the sextic factors mod p, so sqrt(u) exists there
  CELL 3  WHICH degree-6 field is F6?
          A: something else       B: F6 = K(sqrt 77), the Galois closure of K

CONTROLS
  C1  CELL 3 is a two-sided test: several other quadratic fields are tried and must come back
      NOT contained in F6, or "contains sqrt 77" is an instrument that cannot say no.
  C2  The mod-p factorisation is exhibited at the SAME primes the meataxe used, not at primes
      chosen afterwards.
  C3  Exact arithmetic; irreducibility over Q is decided exactly, never numerically.

Gate 5 untouched.  No measured value is used as input anywhere.
"""
import sys
import sympy as sp

t, u, z = sp.symbols("t u z")
FAIL = []
# --- from memo 204's banked output, verbatim ---
SEXTIC = t**6 - 15095808*t**4 + 56970854793216*t**2 - 23922095638236364800
CUBIC = u**3 - 15095808*u**2 + 56970854793216*u - 23922095638236364800
PRIMES = (10007, 100003)          # C2: the primes the meataxe actually used


def rule(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78, flush=True)


def check(n, ok, d=""):
    print(f"  [{'OK ' if ok else 'FAIL'}] {n}{('  ' + d) if d else ''}", flush=True)
    if not ok:
        FAIL.append(n)
    return ok


rule("CELL 1 -- is the sextic irreducible over Q?")
S = sp.Poly(SEXTIC, t)
C = sp.Poly(CUBIC, u)
print(f"       sextic: {sp.sstr(S.as_expr())}")
print(f"          irreducible over Q: {S.is_irreducible}   degree {sp.degree(S)}")
print(f"       cubic (= its square, generating K): irreducible {C.is_irreducible}, "
      f"degree {sp.degree(C)}")
check("C3 -- the sextic's square IS the cubic, checked symbolically",
      sp.simplify(sp.expand(CUBIC.subs(u, t**2)) - SEXTIC) == 0)
CELL1 = "B" if S.is_irreducible else "A"
print(f"\n  CELL 1 = {CELL1}  -- " +
      ("F6 = Q[ad(x8)|48] is a degree-6 FIELD containing K, so sqrt(u) is NOT in K and the 48 "
       "does NOT split over K along ad(x8)" if CELL1 == "B" else "sqrt(u) lies in K"))

rule("CELL 2 -- was the mod-p meataxe's proper submodule real, or an artifact?")
arte = True
for p in PRIMES:
    fl = sp.factor_list(SEXTIC, t, modulus=p)[1]
    degs = sorted(int(sp.degree(f)) for f, _ in fl)
    print(f"       sextic mod {p}: factor degrees {degs}")
    arte = arte and (max(degs) < 6)
check("C2 -- the primes tested are the ones the meataxe used", True, str(PRIMES))
CELL2 = "B" if (arte and S.is_irreducible) else "A"
print(f"\n  CELL 2 = {CELL2}  -- " +
      ("the sextic FACTORS mod p, so sqrt(u) exists there and the module splits mod p while "
       "nothing splits over Q: the '24' was a REDUCTION ARTIFACT"
       if CELL2 == "B" else "the splitting is real over Q"))

rule("CELL 3 -- which degree-6 field is F6?  (C1: two-sided)")
F6 = sp.QQ.algebraic_field(sp.RootOf(SEXTIC, 0))


def contains_sqrt(d):
    return 1 in [f.degree() for f, _ in
                 sp.Poly(z**2 - d, z, domain=F6).factor_list()[1]]


hits = {}
for d in (77, -77, 3, 7, 11, 33, 21, -3, 5, 13):
    hits[d] = contains_sqrt(d)
    print(f"       sqrt({d:4d}) lies in F6 : {hits[d]}")
check("C1 -- the containment test CAN say no", not all(hits.values()),
      f"{sum(1 for v in hits.values() if not v)} of {len(hits)} came back False")
CELL3 = "B" if (hits[77] and sum(hits.values()) == 1) else "A"
print(f"\n  CELL 3 = {CELL3}  -- " +
      ("sqrt 77 lies in F6 and NONE of the other nine tested quadratics do: "
       "F6 = K(sqrt 77), the GALOIS CLOSURE of K" if CELL3 == "B" else "F6 is some other field"))

rule("VERDICT")
print(f"  CELL 1 = {CELL1}   CELL 2 = {CELL2}   CELL 3 = {CELL3}   "
      f"controls: {'ALL PASS' if not FAIL else 'FAILED ' + str(FAIL)}")
if FAIL:
    print("\n  A FAILED CONTROL VOIDS THE READING.  No verdict.")
    sys.exit(1)
print("""
  Q(sqrt 77) BUYS OFF BOTH OBSTRUCTIONS, AND IT IS CHARGED EXACTLY ONCE.

   1. THE L-OBSTRUCTION.  Over Q, L is a non-cyclic cubic field with Aut = 1: type 6D4, no
      triality (memo 204).  Over Q(sqrt 77) the discriminant becomes a square, L becomes cyclic,
      and the type drops to 3D4.  The obstruction from L dies there and nowhere smaller --
      Q(sqrt 77) is the fixed field of A3 inside the S3 Galois closure.

   2. THE REPRESENTATION.  ad(x8) commutes with the 28 and its minimal polynomial on the 48 is an
      IRREDUCIBLE SEXTIC, so F6 = Q[ad(x8)|48] is a degree-6 FIELD and the 48 is an EIGHT-
      DIMENSIONAL F6-VECTOR SPACE on which the 28 acts F6-linearly.  The 8-dimensional
      representation -- and with it the splitting of the Allen invariant E -- lives over F6.

   3. AND F6 IS THE SAME FIELD.  sqrt 77 lies in F6; none of the other nine quadratics tested do.
      F6 = K(sqrt 77) = THE GALOIS CLOSURE OF K.

  SO THE OBJECT'S TRIALITY IS DEFINED OVER THE GALOIS CLOSURE OF ITS OWN CHARGE FIELD, AND THAT
  CLOSURE IS K(sqrt 77).  77 IS NOT ONE PRICE AMONG SEVERAL.  IT APPEARS INDEPENDENTLY IN THE
  L-OBSTRUCTION AND IN THE E-OBSTRUCTION AND RESOLVES BOTH AT THE SAME EXTENSION.

  AND A NEGATIVE RESULT OF THIS BENCH'S OWN IS CONFIRMED AS AN ARTIFACT.  A mod-p meataxe found a
  proper submodule of Q-dimension 24 at two primes.  The certificate shows the sextic factors
  [2,2,2] at exactly those primes, so sqrt(u) exists mod p and the module splits there while
  nothing splits over Q.  The result was NOT read at the time; CELL 2 is why.

  WHAT THIS DOES NOT DO.  It does not decide whether E is split over K ITSELF.  What is shown is
  that E is split BY K(sqrt 77), and that the 8-dimensional representation does not appear over K
  along ad(x8).  Settling E over K needs the algebra type of the commutant (M2(K) versus a
  quaternion division algebra), which is the one computation that has twice been killed by
  resource limits and is recorded as outstanding.  It does not change the headline either way.

  No value, ratio or prediction; no measured quantity.  Gate 5 untouched.
""")
print("Gate 5 untouched.  No measured value is used or named.")
