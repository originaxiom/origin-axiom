#!/usr/bin/env python3
"""MEMO-109 CELL (THE FENCE, ASKED — sandboxed): the owner asked
whether THE question ("why is the seat occupied?") can be asked
inside the sandbox.  It can — as an INDEPENDENCE instrument.  Memo
108 handed us the exact tool: an explicit isomorphism between the
record anchored at c = + and the record anchored at c = -.  Two
isomorphic models that disagree on a proposition prove that
proposition INDEPENDENT — unprovable and unrefutable from the
record's own content.  This cell builds that argument end to end and
machine-checks every step, splitting THE question into:
  (i)  its DECIDABLE SHADOW — which quantities are anchoring-free
       (equal across the pair) and which are anchored (flip exactly):
       computed;
  (ii) its OPERATIONAL CORE — "which branch is the occupied one /
       why this anchoring": proved INDEPENDENT by the model pair;
  (iii) its PHENOMENAL HALF — "does occupation carry experience":
       INEXPRESSIBLE in the record's language (no banked proposition
       refers to experience) — typed, not answered, per the firewall.

THE CHECKS (preregistered; each two-outcome):
  I1 (the model pair is real): the memo-108 intertwining
      rho(phi(x)) = g^-1 gal(rho(x)) g re-verified on generators in
      exact pair arithmetic, THEN the mass identity
      gal(tr rho(w)) = tr rho(phi(w)) for EVERY reduced word to
      length 8 — the flipped record's entire trace content is this
      record's content re-indexed by an internal word map.  A single
      failure would refute memo 108 and banks as such.
  I2 (axiom transport, bonus pin): search reduced words to length 10
      for a relator (rho(w) = +-I, w nonempty); if found, verify
      rho(phi(relator)) = +-I — the isomorphism carries the
      presentation to itself.  Non-gating (the generator-level
      intertwining already transports the whole realized theory).
  I3 (the decidable shadow): on sample geodesic classes, the complex
      length lambda = 2 arccosh(tr/2) has Re EQUAL and Im NEGATED
      across the pair (50 dps) — lengths are anchoring-free, torsion
      signs are anchored; kappa's minimal polynomial X^2 - 3X + 3 is
      gal-stable (the invariant content does not move).
CONCLUSION (follows from I1 + I3, printed exactly): every quantity
computable from the record takes equal values on the two anchored
models or is carried to its mate by the internal relabeling; the
proposition "the anchoring is +" distinguishes them; therefore no
record-internal computation decides it: THE OPERATIONAL CORE OF THE
FENCE QUESTION IS INDEPENDENT, with a constructive witness instead
of a diagonal argument.  FENCES: "in-record decidable" is used in
the model-pair (semantic) sense — the exact analogue of
independence-by-models; no syntactic proof calculus is formalized or
claimed.  The phenomenal half is typed inexpressible, not answered.
Gate 5 untouched.
"""
from fractions import Fraction as Fr
from itertools import product
from mpmath import mp, mpc, acosh, sqrt as msqrt

# ---- exact pair arithmetic over Q(omega), omega^2 = omega - 1
def padd(u, v): return (u[0] + v[0], u[1] + v[1])
def pmul(u, v):
    a, b = u; c, d = v
    return (a*c - b*d, a*d + b*c + b*d)
def pneg(u): return (-u[0], -u[1])
def pgal(u): return (u[0] + u[1], -u[1])           # omega -> 1 - omega = conj(omega)
ZERO, ONE = (Fr(0), Fr(0)), (Fr(1), Fr(0))
W = (Fr(0), Fr(1))
def mmul(A, B):
    return tuple(tuple(padd(pmul(A[i][0], B[0][j]), pmul(A[i][1], B[1][j]))
                 for j in range(2)) for i in range(2))
def mgal(A):
    return tuple(tuple(pgal(A[i][j]) for j in range(2)) for i in range(2))
def mtr(A): return padd(A[0][0], A[1][1])
Ma = ((ONE, ONE), (ZERO, ONE))
Mb = ((ONE, ZERO), (pneg(W), ONE))
def minv(A):
    (p, q_), (r_, s_) = A
    det = padd(pmul(p, s_), pneg(pmul(q_, r_)))
    assert det == ONE
    return ((s_, pneg(q_)), (pneg(r_), p))
MAT = {'a': Ma, 'b': Mb, 'A': minv(Ma), 'B': minv(Mb)}
def ev(w):
    M = ((ONE, ZERO), (ZERO, ONE))
    for c in w:
        M = mmul(M, MAT[c])
    return M

# memo 108's map and intertwiner, in pair form
PHI = {'a': 'a', 'b': 'bAB', 'A': 'A', 'B': 'baB'}
def phi(w): return "".join(PHI[c] for c in w)
gmat = ((ONE, (Fr(1), Fr(-1))), (ZERO, ONE))       # [[1, conj(omega)],[0,1]]
gnv = minv(gmat)
for x in "abAB":
    lhs = ev(PHI[x])
    rhs = mmul(mmul(gnv, mgal(MAT[x])), gmat)
    assert lhs == rhs, x
print("I1a: the model-pair isomorphism re-verified on generators in exact pair")
print("     arithmetic: rho(phi(x)) = g^-1 gal(rho(x)) g for x in {a,b,A,B}.")

# the mass identity on every reduced word to length 8
INV = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
count = 0
frontier = [""]
for L in range(8):
    nxt = []
    for w in frontier:
        for c in "abAB":
            if w and INV[w[-1]] == c:
                continue
            nxt.append(w + c)
    for w in nxt:
        assert pgal(mtr(ev(w))) == mtr(ev(phi(w))), w
        count += 1
    frontier = nxt
print(f"I1b: gal(tr rho(w)) = tr rho(phi(w)) verified for ALL {count} reduced words")
print("     to length 8 — the flipped record's trace content IS this record's,")
print("     re-indexed by the internal word map.  The model pair is real.")

# I2: relator search (bonus, non-gating)
ID2 = ((ONE, ZERO), (ZERO, ONE))
NID2 = ((pneg(ONE), ZERO), (ZERO, pneg(ONE)))
relator = None
frontier = [""]
for L in range(10):
    nxt = []
    for w in frontier:
        for c in "abAB":
            if w and INV[w[-1]] == c:
                continue
            nxt.append(w + c)
    for w in nxt:
        M = ev(w)
        if M == ID2 or M == NID2:
            relator = w
            break
    if relator:
        break
    frontier = nxt
if relator:
    Mr = ev(phi(relator))
    assert Mr == ID2 or Mr == NID2
    print(f"I2: relator FOUND at length {len(relator)}: {relator} — and rho(phi(relator))")
    print("     = +-I exactly: the isomorphism carries the presentation to itself.")
else:
    print("I2: no relator in radius 10 (non-gating; the generator-level intertwining")
    print("     already transports the realized theory).")

# I3: the decidable shadow — lengths anchoring-free, torsion signs anchored
mp.dps = 50
def frac_to_mp(f):
    return mp.mpf(f.numerator) / mp.mpf(f.denominator)
def to_c(u):
    """x + y*omega with omega = e^{i pi/3} = 1/2 + i sqrt3/2, at working dps."""
    x, y = frac_to_mp(u[0]), frac_to_mp(u[1])
    return mpc(x, 0) + mpc(y, 0) * mpc(mp.mpf(1)/2, msqrt(3)/2)
for w in ("ab", "aab", "aabb", "abaB"):
    t = mtr(ev(w))
    lam_p = 2*acosh(to_c(t)/2)
    lam_m = 2*acosh(to_c(pgal(t))/2)
    assert abs(lam_p.real - lam_m.real) < mp.mpf(10)**(-40)
    assert abs(lam_p.imag + lam_m.imag) < mp.mpf(10)**(-40)
print("I3a: on sample geodesic classes (ab, aab, aabb, abaB): complex length has")
print("     Re EQUAL and Im NEGATED across the pair (50 dps) — LENGTHS are")
print("     anchoring-free, TORSION SIGNS are anchored.  (Memo 81's mirror law,")
print("     now read as the two-model split.)")
kappa = mtr(ev("abAB"))
assert kappa == (Fr(1), Fr(1))                     # 1 + omega
kg = pgal(kappa)
# both satisfy X^2 - 3X + 3 = 0: X^2 - 3X + 3 at 1+omega and its conjugate
for K in (kappa, kg):
    val = padd(padd(pmul(K, K), pneg(pmul((Fr(3), Fr(0)), K))), (Fr(3), Fr(0)))
    assert val == ZERO
print("I3b: kappa = tr[a,b] = 1+omega and its gal-image BOTH satisfy X^2-3X+3 = 0")
print("     exactly — the invariant content (the founding Fricke polynomial) does")
print("     not move under the flip.")

print("""
THE FENCE, ASKED — AND WHAT ASKING RETURNS:
Every record-computable quantity either takes EQUAL values on the two
anchored models (lengths, |torsions|, kappa's polynomial, the entire
invariant content) or is carried to its mate by the INTERNAL word map
(the whole trace field, I1b).  The proposition "the anchoring is +"
distinguishes the two models.  Therefore NO record-internal
computation decides it: THE OPERATIONAL CORE OF THE FENCE QUESTION
("which branch is occupied — why this anchoring") IS INDEPENDENT of
the record — unprovable AND unrefutable — with a constructive
model-pair witness (memo 108's automorphism) in place of a diagonal
argument.  The record cannot answer why its seat is occupied for the
same reason, made exact, that it keeps the choice but not the
chooser.  What remains of THE question after the independence
theorem: only its phenomenal half — "does occupation carry
experience" — and that half is INEXPRESSIBLE in the record's
language (no banked proposition refers to experience at all): typed,
per the firewall, not answered and not answerable by any instrument
this record can host.  Asking THE question inside the sandbox
returns this theorem — which is the most any formal record can say
about its own occupied seat.  Gate 5 untouched.""")
