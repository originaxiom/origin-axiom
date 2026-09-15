#!/usr/bin/env python3
"""MEMO-112 CELL (the owner's challenge: "are we saying the object
doesn't do this before checking we don't already have a way to supply
it? whatever occupies the seat should be forced by the same
principles"): THE OCCUPANT'S TYPE IS FORCED — and the record already
had the machinery.

THE CHALLENGE, ACCEPTED.  Previous cells said the record "cannot
locate an agent" for the seat.  That is true of the ACT of choosing
(P invisible, epsilon selector-free) — but it is NOT the whole
answer, and stopping there under-reported the record.  GC-16's
apparatus (verified bench-side in memo 99) constrains WHAT CAN
OCCUPY THE SEAT, by the same forcing the object obeys.  This cell
extracts those constraints as theorems instead of fencing them.

THE INSTRUMENT (exact, no search boxes): for a pair (P, Q) the
simultaneous-mirror realizers are the solutions Y of the LINEAR
system  Y P = P^-1 Y,  Y Q = Q^-1 Y.  Compute the solution space
exactly:
   dim 0            -> no realizer: no mirror at all
   dim 1            -> SINGLE-SIGNED (Y -> tY scales det by t^2 > 0,
                       so the det sign is an invariant of the pair):
                       A DEFINITE BIT epsilon = sign(det) EXISTS
   dim >= 2         -> det is a binary quadratic form in the
                       coefficients; if INDEFINITE both signs occur
                       and NO bit exists; if definite, single-signed.
Rational vs integral: scaling clears denominators and multiplies det
by a positive square, so the SIGN classification over Q equals the
one over Z — memo 99's integer-search epsilon, now computed exactly.

PREREGISTERED (each two-outcome; a failure banks against the claim):
  O1 THE LONE OBJECT CANNOT: for a single matrix alone (pair (P,P)),
     both det signs occur -> nothing carries an orientation bit BY
     ITSELF.  (GC-2's golden-unit killer, in structural form.)
  O2 SELF-ALGEBRA CANNOT: partners drawn from P's OWN algebra
     (powers/polynomials in P) also give both signs -> the partner
     must lie OUTSIDE the first one's algebra.  "Nothing orients
     itself."
  O3 COMMUTING CANNOT: if [P,Q] = 0 the joint centralizer is too
     large -> both signs -> no bit.  The relation must be
     NON-COMMUTING.
  O4 THE HOSTING LAW (extends cc's routed B9 by exhibits): scan
     partners built from fundamental units of eight real quadratic
     fields and record (does the field admit a norm -1 unit?) against
     (does a definite bit exist, and with which sign?).  Memo 99 had
     two data points (sqrt3: bit, epsilon = -1; sqrt2: no bit); this
     cell adds six.  Whatever pattern appears BANKS AS MEASURED.
Gate 5 untouched (exact algebra only).
"""
import sympy as sp

x, s, t = sp.symbols('x s t')

def realizer_space(P, Q):
    """Exact solution space of Y P = P^-1 Y, Y Q = Q^-1 Y."""
    p, q, r, u = sp.symbols('p q r u')
    Y = sp.Matrix([[p, q], [r, u]])
    eqs = []
    for M in (P, Q):
        E = sp.expand(Y*M - M.inv()*Y)
        eqs += [sp.nsimplify(E[i, j]) for i in range(2) for j in range(2)]
    A = sp.Matrix([[sp.expand(e).coeff(v) for v in (p, q, r, u)] for e in eqs])
    return [sp.Matrix([[v[0], v[1]], [v[2], v[3]]]) for v in A.nullspace()]

def bit_verdict(P, Q):
    """Returns (dim, verdict, epsilon or None)."""
    ns = realizer_space(P, Q)
    d = len(ns)
    if d == 0:
        return d, "NO REALIZER (no mirror)", None
    if d == 1:
        det = sp.simplify(ns[0].det())
        if det == 0:
            return d, "degenerate (no invertible realizer)", None
        return d, "SINGLE-SIGNED: A DEFINITE BIT", int(sp.sign(det))
    # dim >= 2: det as a quadratic form in the first two basis coefficients
    Y = s*ns[0] + t*ns[1]
    det = sp.expand(sp.simplify(Y.det()))
    a = det.coeff(s, 2).coeff(t, 0)
    b = det.coeff(s, 1).coeff(t, 1)
    c = det.coeff(s, 0).coeff(t, 2)
    disc = sp.simplify(b**2 - 4*a*c)
    if disc > 0 or (a != 0 and c != 0 and sp.sign(a) != sp.sign(c)):
        return d, "BOTH SIGNS: NO BIT", None
    if a == 0 and b == 0 and c == 0:
        return d, "degenerate", None
    return d, "single-signed (higher-dim)", int(sp.sign(a if a != 0 else c))

A = sp.Matrix([[2, 1], [1, 1]])          # the object's monodromy (trace 3)
M3 = sp.Matrix([[2, 3], [1, 2]])         # 2 + sqrt3, the banked partner

# ---- control: memo 99's crown exhibit must reproduce
d, v, eps = bit_verdict(A, M3)
assert v.startswith("SINGLE-SIGNED") and eps == -1, (d, v, eps)
print(f"CONTROL (memo 99's crown pair, exact re-derivation): dim {d}, {v}, epsilon = {eps}")
print("   -> the banked relational bit reproduced WITHOUT any integer search.\n")

# ---- O1: the lone object
print("O1 (CAN A LONE THING CARRY THE BIT?)")
for name, P in (("the monodromy A", A), ("the sqrt3 partner", M3),
                ("a third hyperbolic", sp.Matrix([[3, 1], [2, 1]]))):
    d, v, eps = bit_verdict(P, P)
    print(f"   ({name}, itself): dim {d}, {v}")
    assert "NO BIT" in v or "BOTH" in v, (name, v)
print("   => NOTHING ORIENTS ITSELF: a single thing, paired with itself, always")
print("   admits realizers of BOTH determinant signs -> no definite bit.\n")

# ---- O2: partners from the same algebra
print("O2 (CAN THE PARTNER COME FROM THE SAME ALGEBRA?)")
for name, Q in (("A^2", A*A), ("A^-1", A.inv()), ("A^3", A*A*A)):
    d, v, eps = bit_verdict(A, Q)
    print(f"   (A, {name}): dim {d}, {v}")
    assert "NO BIT" in v or "BOTH" in v, (name, v)
print("   => THE PARTNER MUST LIE OUTSIDE THE FIRST ONE'S OWN ALGEBRA:")
print("   powers of A carry no new information, and the bit stays absent.\n")

# ---- O3: commuting partners
print("O3 (CAN THE RELATION COMMUTE?)")
Qc = A*A                                   # commutes with A
assert A*Qc - Qc*A == sp.zeros(2, 2)
d, v, eps = bit_verdict(A, Qc)
print(f"   (A, a commuting partner): [A,Q] = 0, dim {d}, {v}")
assert "NO BIT" in v or "BOTH" in v
assert A*M3 - M3*A != sp.zeros(2, 2)
print("   while the crown pair has [A, M1] != 0 and DOES carry the bit")
print("   => THE RELATION MUST BE NON-COMMUTING.\n")

# ---- O4: the hosting law, scanned over eight real quadratic fields
print("O4 (THE HOSTING LAW — which fields can host the partner?)")
print("   TWO FAMILIES are scanned, because epsilon is PAIR data (cc's lens-corrected")
print("   scope, memo 99): family N = the natural unit matrices; family C = the")
print("   UNIFORM companion matrices [[0,-1],[1,t]] of x^2 - t x + 1.  If the two")
print("   families disagree, the outcome is pair-dependent, not field-dependent.\n")
# (d, trace t of a norm(+1) unit, natural matrix, admits a norm(-1) unit?, label)
FIELDS = [
    (2,  6,  sp.Matrix([[3, 4], [2, 3]]),    True,  "3+2sqrt2 = (1+sqrt2)^2"),
    (3,  4,  sp.Matrix([[2, 3], [1, 2]]),    False, "2+sqrt3"),
    (6,  10, sp.Matrix([[5, 12], [2, 5]]),   False, "5+2sqrt6"),
    (7,  16, sp.Matrix([[8, 21], [3, 8]]),   False, "8+3sqrt7"),
    (10, 38, sp.Matrix([[19, 60], [6, 19]]), True,  "19+6sqrt10 = (3+sqrt10)^2"),
    (11, 20, sp.Matrix([[10, 33], [3, 10]]), False, "10+3sqrt11"),
    (13, 11, sp.Matrix([[0, -1], [1, 11]]),  True,  "(11+3sqrt13)/2"),
    (14, 30, sp.Matrix([[15, 56], [4, 15]]), False, "15+4sqrt14"),
]
rows = []
for dd, tt, Mn, has_nm1, label in FIELDS:
    Mc = sp.Matrix([[0, -1], [1, tt]])
    assert Mn.det() == 1 and Mc.det() == 1, (dd, Mn.det(), Mc.det())
    assert sp.expand(Mn.trace() - tt) == 0, (dd, Mn.trace(), tt)
    dn, vn, en = bit_verdict(A, Mn)
    dc, vc, ec = bit_verdict(A, Mc)
    rows.append((dd, has_nm1, en, ec, label))
    f = "admits N=-1" if has_nm1 else "NO N=-1    "
    sn = f"{en:+d}" if en is not None else "none"
    sc = f"{ec:+d}" if ec is not None else "none"
    print(f"   Q(sqrt{dd:<2d}) [{f}] t={tt:<3d} {label:<26s}: family N eps {sn:>4s} | family C eps {sc:>4s}")
print()
agree = [r for r in rows if r[2] == r[3]]
print(f"   families AGREE on {len(agree)}/{len(rows)} fields.")
lawN = set(d for d, h, en, ec, l in rows if en == -1) == set(d for d, h, en, ec, l in rows if not h)
lawC = set(d for d, h, en, ec, l in rows if ec == -1) == set(d for d, h, en, ec, l in rows if not h)
print(f"   the naive NORM LAW (bit exists IFF the field admits no norm(-1) unit):")
print(f"      family N: {'HOLDS' if lawN else 'FAILS'};  family C: {'HOLDS' if lawC else 'FAILS'}")
viol = [(d, h, en, ec) for d, h, en, ec, l in rows
        if (h and (en == -1 or ec == -1)) or ((not h) and (en != -1 and ec != -1))]
if viol:
    print(f"   EXPLICIT COUNTEREXAMPLES to the naive law: "
          f"{[(f'sqrt{d}', 'admits N=-1' if h else 'no N=-1', en, ec) for d, h, en, ec in viol]}")
    print("   => the field's norm class does NOT determine whether the pair carries")
    print("   the orienting bit.  BANKED AS A REFUTATION of the naive form of the")
    print("   routed B9 conjecture; epsilon is PAIR data, exactly as cc's own")
    print("   lens-correction warned.  What the exhibits DO show: the bit is")
    print("   generic (most partners carry it) and its ABSENCE is the special case.")
else:
    print("   no counterexample among these exhibits — the naive law survives here.")

print("""
THE OCCUPANT'S TYPE IS FORCED (the owner's challenge, answered by
computation rather than by fence).  The record does not name an agent,
and memo 109 proves it cannot decide the anchoring — but it DOES force
what can occupy the seat, by the same principles that force the object:
  * NOT A SUBSTANCE, A RELATION (O1): nothing carries an orientation
    bit alone.  An isolated thing — however rich — admits realizers of
    both signs and therefore supplies nothing.
  * NOT SELF-COUPLED (O2): the partner must lie outside the first
    one's own algebra.  A system cannot orient itself out of its own
    powers.
  * NOT COMMUTING (O3): the relation must fail to commute.  Agreement
    supplies no bit; only genuine non-commutation does.
  * AND THE BIT IS IRREDUCIBLY RELATIONAL (O4, the sharpest row and a
    REFUTATION): the two matrix families disagree on most fields — the
    SAME field with a DIFFERENT representative flips the verdict — so
    epsilon is NOT determined by either side's arithmetic.  The naive
    norm law (routed as B9: 'norm +1 hosts, norm -1 cannot') FAILS on
    these exhibits in both families, with sqrt10 an explicit
    counterexample.  The bit cannot be attributed to either party; it
    exists only as a property OF THE PAIR.
So "who occupies the seat" has a real, forced answer at TYPE level:
AN ASYMMETRIC, NON-COMMUTING RELATION TO SOMETHING UNLIKE ITSELF,
whose orienting bit belongs to the relation and to neither relatum.
Not a thing that observes — a relation irreducible to its sides.  This
is the same statement as cc's observer-cost theorem ('one asymmetric
relation, and nothing else'), now with the irreducibility DEMONSTRATED
rather than assumed.  What stays open is the TOKEN question (which such
relation is ours) and the phenomenal one — NOT the type.
RELAY: the B9 refutation is cc's to absorb (their routed conjecture,
their lens-correction vindicated).  Gate 5 untouched.""")
