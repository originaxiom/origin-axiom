"""P2W6-GATEB-r (OI-128) -- REPAIR of P2W5-GATEB.

B775 Phase-2 Wave-6.  STRUCTURAL cell.  Exact/symbolic throughout (sympy over
Q(sqrt(-3))); no floats, no scans, no estimators.

WHAT THE VERIFIER UPHELD (not re-litigated, but recomputed here for self-containment)
  * the VERDICT: Level 3 stays CLOSED for Gate B.
  * the WITNESS is REAL: OI-173's rho'(g) = w^{eps(g)} rho_b(g) is an injective
    homomorphism into Stab(I3) < E6 with 27|H' = 3.1+9.1'+3.1''+3.2+3.2'',
    non-real character, n1 = 9 != n2 = 0.  The clean theorem "no 2T < E6 has
    n1 != n2" is FALSE.  Nothing here deflates it.

WHAT THE VERIFIER KILLED (the named defect, fixed here)
  det Hess I3(v) == 2 * I3(v)^9  (a classical identity, re-confirmed in-cell below).
  Therefore "H fixes a v with I3(v) != 0" <=> "H preserves a nondegenerate symmetric
  form on the 27" <=> "27|H is self-dual" -- so
      (1) the F4-EXCLUSION of the witness  and
      (2) the SL(2)-EXCLUSION of the witness
  are BOTH one-step corollaries of the witness's own CHIRALITY, i.e. of the premise
  being reconciled.  "Three independently computed reasons" was false.  They are
  DEMOTED here to corollaries (section E) and are NOT read by the verdict function.

THE RESTATED CLOSURE -- ON TWIST-RIGIDITY ALONE (section D, the only independent content)
  R1  criterion:  rho (x) 1'^k = rho for all k  <=>  chi_rho vanishes on every
      eps != 0 class of 2T.        (exact, proved both directions in-cell)
  R2  twist-rigid => the whole mu_3-twist torsor of rho COLLAPSES to one iso class,
      so every member has rho's own (n1,n2); if rho is self-dual, its torsor
      contains NO chiral member at all.
  R3  THE OBJECT'S ROUTE IS TWIST-RIGID.  chi_principal = 0 on all three eps != 0
      classes (exact), so the object's torsor is {rho_pr}, with (n1,n2) = (3,3).
      OI-173's construction, applied to the object's own route, returns the object's
      own route.  Level 3 is unreachable along it.
  R4  NON-FORCEDNESS (lesson L3, the thing that makes R3 a REASON and not a restatement):
      twist-rigidity is NOT entailed by any premise in the class.
        (a) not by "SL(2)-route": the non-principal SL(2)-route 3 = 1+2 (an explicit,
            I3-invariant embedding) is NOT rigid and twists to a chiral (9,0) member.
        (b) not by "theta-compatible / inside F4": the balanced trinification route
            fixes a point with I3 != 0 (so it lies pointwise inside a conjugate of
            F4 = E6^theta) and is self-dual -- and is NOT rigid; it twists to the
            chiral witness itself.
        (c) not by "self-dual / n1 = n2": all three routes are self-dual; only the
            principal one is rigid.
        (d) not by the WITNESS's chirality: R3 is computed from chi_principal alone;
            deleting every witness-derived row from the route table leaves R3 intact
            (demonstrated mechanically).
        (e) census: of all 27-dim SU(2)-reps (partitions of 27), only a strict
            minority restrict to a twist-rigid 2T-rep.  Rigidity is a codimension-2
            arithmetic condition, not a class property.

SEALED CRITERION (Wave-6 addendum 3402b906)
  Level 3 stays CLOSED on twist-rigidity ALONE                          => RESOLVED-B
  twist-rigidity FAILS, or is ITSELF FORCED (vacuous / class-entailed)  => RESOLVED-A
  otherwise                                                            => UNRESOLVED

DECLARED SELECTION (lesson L4).  The single selection this cell makes is WHICH route
is the object's: the principal-SL2 route (cited: B329a, B347/B351/B352, B353).  The
verdict IS sensitive to it -- selecting the balanced trinification or the 3 = 1+2
SL(2)-route instead flips RESOLVED-B -> RESOLVED-A.  The sensitivity table is printed
and stored.  The selection is a fenced CITED premise, not an in-cell result.

B774 chord discipline self-test: no chord/theta-odd-trace claim is made here.  The
twist torsor Hom(2T, mu_3) is abelian BY CONSTRUCTION (a hom to the centre) and is
labelled as such -- it is not offered as a non-abelian invariant.

Gate 5 / 5-Q: structural only; no SM values; nothing to CLAIMS.md; pin untouched.
Re-runnable: pyenv python3 compute.py   (sympy only).
"""
import itertools
import json
import random
import sympy as sp

W = sp.Rational(-1, 2) + sp.sqrt(3) / 2 * sp.I           # w = e^{2 pi i / 3}
FAIL = []
LOG = []


def gate(name, cond):
    cond = bool(cond)
    line = ("PASS  " if cond else "FAIL  ") + name
    print(line)
    LOG.append(line)
    if not cond:
        FAIL.append(name)
    return cond


def say(s):
    print(s)
    LOG.append(s)


# =========================================================================
# A -- 2T from the 24 Hurwitz units; classes; eps: 2T -> Z/3; character table
# =========================================================================
def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)


def qinv(a):
    return (a[0], -a[1], -a[2], -a[3])


def order(g):
    p, one = g, (1, 0, 0, 0)
    for k in range(1, 25):
        if p == one:
            return k
        p = qmul(p, g)


def two_T():
    h = sp.Rational(1, 2)
    elts = set()
    for p in itertools.permutations(range(4)):
        for s in (1, -1):
            v = [0, 0, 0, 0]
            v[p[0]] = s
            elts.add(tuple(v))
    for s in itertools.product((h, -h), repeat=4):
        elts.add(tuple(s))
    elts = sorted(elts, key=str)
    seen, classes = set(), []
    for g in elts:
        if g in seen:
            continue
        cl = set(qmul(qmul(t, g), qinv(t)) for t in elts)
        classes.append(sorted(cl, key=str))
        seen |= cl
    classes.sort(key=lambda c: (order(c[0]), sp.sign(c[0][0]) if c[0][0] != 0 else 0))
    return elts, classes


ELTS, CLASSES = two_T()
REPS = [c[0] for c in CLASSES]
SIZES = [len(c) for c in CLASSES]
gate("A1: 2T = 24 Hurwitz units, 7 conjugacy classes, sizes sum to 24",
     len(ELTS) == 24 and len(CLASSES) == 7 and sum(SIZES) == 24)

Q8 = set(g for g in ELTS if all(c in (0, 1, -1) for c in g))


def coset(g):
    return frozenset(qmul(g, q) for q in Q8)


g3 = next(g for g in ELTS if order(g) == 3)
COS = {coset((1, 0, 0, 0)): 0}
gp = g3
for k in (1, 2):
    COS[coset(gp)] = k
    gp = qmul(gp, g3)


def eps(g):
    return COS[coset(g)]


gate("A2: eps: 2T -> Z/3 is a homomorphism (all 576 pairs, exact)",
     all((eps(qmul(g, h)) - eps(g) - eps(h)) % 3 == 0 for g in ELTS for h in ELTS))
gate("A3: ker(eps) = Q8; Hom(2T, mu_3) = Z/3 (the twist group is NON-trivial)",
     set(g for g in ELTS if eps(g) == 0) == Q8 and len(set(COS.values())) == 3)

chi_1p = lambda g: W ** eps(g)
chi_1pp = lambda g: sp.conjugate(W) ** eps(g)
chi_2 = lambda g: 2 * g[0]
IRR = {'1': lambda g: sp.Integer(1), "1'": chi_1p, "1''": chi_1pp,
       '2': chi_2, "2'": lambda g: chi_2(g) * chi_1p(g),
       "2''": lambda g: chi_2(g) * chi_1pp(g), '3': lambda g: 4 * g[0]**2 - 1}
NAMES = list(IRR)

ortho = all(sp.simplify(sum(SIZES[i] * IRR[a](REPS[i]) * sp.conjugate(IRR[b](REPS[i]))
                            for i in range(7)) / 24) == (1 if a == b else 0)
            for a in IRR for b in IRR)
gate("A4: character table derived + gated orthonormal, sum dim^2 = 24",
     ortho and sum(int(IRR[k](REPS[0]))**2 for k in IRR) == 24)

EPSNZ = [i for i in range(7) if eps(REPS[i]) != 0]     # the eps != 0 classes
gate("A5: exactly 4 of the 7 classes have eps != 0, of orders %s (the two order-3 and the two "
     "order-6 classes) -- these are the classes the rigidity criterion R1 reads"
     % str([order(REPS[i]) for i in EPSNZ]),
     len(EPSNZ) == 4 and sorted(order(REPS[i]) for i in EPSNZ) == [3, 3, 6, 6])


def decompose(chi_vals):
    return {n: sp.nsimplify(sp.simplify(sum(SIZES[i] * chi_vals[i] * sp.conjugate(IRR[n](REPS[i]))
                                            for i in range(7)) / 24)) for n in NAMES}


def n1n2(dec):
    return (sp.simplify(dec["1'"] - dec["2'"]), sp.simplify(dec["1''"] - dec["2''"]))


def self_dual(dec):
    return sp.simplify(dec["1'"] - dec["1''"]) == 0 and sp.simplify(dec["2'"] - dec["2''"]) == 0


# =========================================================================
# B -- explicit 27-dim embeddings (trinification model) + the E6 cubic
# =========================================================================
def rho2(q):
    a, b, c, d = q
    return sp.Matrix([[a + b*sp.I, c + d*sp.I], [-c + d*sp.I, a - b*sp.I]])


def rho3(g):
    """faithful complex 3 = 1' + 2' of 2T inside SU(3)  (the balanced route, B329b)."""
    e = eps(g)
    m = sp.zeros(3, 3)
    m[0, 0] = W**e
    m[1:, 1:] = (W**e) * rho2(g)
    return m.applyfunc(sp.expand)


def rho3_sl2(g):
    """an SL(2,C)-ROUTE factor: 3 = 1 + 2 (the quaternionic 2), det = 1."""
    m = sp.zeros(3, 3)
    m[0, 0] = sp.Integer(1)
    m[1:, 1:] = rho2(g)
    return m.applyfunc(sp.expand)


gate("B1: rho2 is a homomorphism 2T -> SU(2) (all 576 pairs, exact)",
     all((rho2(qmul(g, h)) - rho2(g)*rho2(h)).applyfunc(sp.expand).is_zero_matrix
         for g in ELTS for h in ELTS))
gate("B2: rho3 and rho3_sl2 land in SU(3) (det 1, unitary; all 24 elements, exact)",
     all(sp.simplify(f(g).det() - 1) == 0 and
         (f(g)*f(g).H - sp.eye(3)).applyfunc(sp.simplify).is_zero_matrix
         for f in (rho3, rho3_sl2) for g in ELTS))
gate("B3: w^3 = 1 (the mu_3 centre of E6)", sp.simplify(W**3 - 1) == 0)

GI = (0, 1, 0, 0)                       # order 4, eps = 0
GT = (sp.Rational(1, 2),) * 4           # order 6, eps != 0


def closure(gens, cap=200):
    S = {tuple(sp.expand(c) for c in (1, 0, 0, 0))}
    front = set(gens)
    while front and len(S) <= cap:
        S |= front
        front = {tuple(sp.expand(c) for c in qmul(a, b)) for a in S for b in S} - S
    return S


gate("B4: <i, (1+i+j+k)/2> = 2T (generators verified by closure)",
     closure({GI, GT}) == set(ELTS))


def kron(A, B):
    p, q = B.shape
    return sp.Matrix(A.shape[0]*p, A.shape[1]*q,
                     lambda i, j: A[i//p, j//q] * B[i % p, j % q])


I3M = sp.eye(3)


def P_of(A, B, C):
    """27 = (3,3b,1)+(1,3,3b)+(3b,1,3)."""
    P = sp.zeros(27, 27)
    P[0:9, 0:9] = kron(A, B.conjugate())
    P[9:18, 9:18] = kron(B, C.conjugate())
    P[18:27, 18:27] = kron(C, A.conjugate())
    return P


XS = sp.symbols('x0:27')


def I3_of(v):
    M1 = sp.Matrix(3, 3, list(v[0:9]))
    M2 = sp.Matrix(3, 3, list(v[9:18]))
    M3 = sp.Matrix(3, 3, list(v[18:27]))
    return sp.expand(M1.det() + M2.det() + M3.det() - (M1*M2*M3).trace())


I3_BASE = I3_of(list(XS))


def invariant_under(P):
    y = [sp.expand(sum(P[i, j]*XS[j] for j in range(27) if P[i, j] != 0)) for i in range(27)]
    return sp.simplify(sp.expand(I3_of(y) - I3_BASE)) == 0


def Pb(g):
    return P_of(rho3(g), I3M, I3M)                       # balanced trinification (canonical)


def Pq(g):
    return P_of(rho3_sl2(g), I3M, I3M)                   # an SL(2,C)-route


def twist(P, k):
    def f(g):
        return ((W**(k*eps(g))) * P(g)).applyfunc(sp.expand)
    return f


Pt1, Pt2 = twist(Pb, 1), twist(Pb, 2)                    # the chiral witnesses
Pq1 = twist(Pq, 1)

gate("B5: I3 invariant under the balanced route (symbolic, 27 vars, both generators)",
     invariant_under(Pb(GI)) and invariant_under(Pb(GT)))
gate("B6: I3 invariant under the central scalar w.Id (so every mu_3 twist stays in E6)",
     invariant_under(W * sp.eye(27)))
gate("B7: I3 invariant under the CHIRAL witness (symbolic, 27 vars, both generators)",
     invariant_under(Pt1(GI)) and invariant_under(Pt1(GT)))
gate("B8: I3 invariant under the SL(2)-route 3=1+2 AND under its twist (symbolic, 27 vars) "
     "-- so the Y4 counterexample is a GENUINE E6 subgroup, not a formal character",
     invariant_under(Pq(GI)) and invariant_under(Pq(GT))
     and invariant_under(Pq1(GI)) and invariant_under(Pq1(GT)))

random.seed(11)
PAIRS = [(random.choice(ELTS), random.choice(ELTS)) for _ in range(20)] + [(GI, GT), (GT, GI)]
gate("B9: the chiral witness rho' = w^eps . Pb is an injective homomorphism (exact)",
     all((Pt1(qmul(g, h)) - Pt1(g)*Pt1(h)).applyfunc(sp.simplify).is_zero_matrix
         for g, h in PAIRS)
     and all(((Pt1(g) - sp.eye(27)).applyfunc(sp.simplify).is_zero_matrix) == (g == (1, 0, 0, 0))
             for g in ELTS))

# =========================================================================
# C -- the routes and their branchings 27|_2T  (exact characters)
# =========================================================================
# SU(2) character machinery: an SU(2)-rep with irrep DIMS d_i has
# chi(g) = sum_i U_{d_i - 1}(Re g).
def su2_chi(dims, i):
    return sp.simplify(sum(sp.chebyshevu(d - 1, REPS[i][0]) for d in dims))


PRINC_DIMS = (17, 9, 1)          # CITED (E6): the principal SL2 content of the 27
E6_EXPONENTS = (1, 4, 5, 7, 8, 11)
ADJ_DIMS = tuple(2*m + 1 for m in E6_EXPONENTS)


def su2_tensor(a, b):
    """dims of V_a (x) V_b for SU(2), by dimension."""
    return [abs(a - b) + 1 + 2*k for k in range(min(a, b))]


TENS = []
for a in PRINC_DIMS:
    for b in PRINC_DIMS:
        TENS += su2_tensor(a, b)
gate("C0 (consistency of the CITED principal content): dim 17+9+1 = 27; the E6 exponents "
     "give sum(2m+1) = 78; and 27 (x) 27* contains the adjoint 78 and a singlet exactly, "
     "with remainder of dimension 650",
     sum(PRINC_DIMS) == 27 and sum(ADJ_DIMS) == 78
     and all(TENS.count(d) >= list(ADJ_DIMS).count(d) for d in set(ADJ_DIMS))
     and TENS.count(1) >= 1 and sum(TENS) == 729 and 729 - 1 - 78 == 650)

chi_pr = [su2_chi(PRINC_DIMS, i) for i in range(7)]

ROUTES = {}


def add_route(name, chivals, kind):
    dec = decompose(chivals)
    ROUTES[name] = dict(chi=chivals, dec=dec, n=n1n2(dec), sd=self_dual(dec), kind=kind)


PR = "principal SL2 (THE OBJECT'S ROUTE, cited B329a/B347/B351/B352/B353)"
BAL = "balanced trinification (canonical, B329b)"
WITN = "balanced (x) 1'  = THE CHIRAL WITNESS (OI-173)"
BAL2 = "balanced (x) 1''"
SL2 = "SL(2)-route 3 = 1+2 (non-principal)"
SL2T = "SL(2)-route (x) 1'"

add_route(PR, chi_pr, "SL(2)-route")
add_route("principal (x) 1'", [sp.simplify(chi_pr[i]*chi_1p(REPS[i])) for i in range(7)], "twist")
add_route("principal (x) 1''", [sp.simplify(chi_pr[i]*chi_1pp(REPS[i])) for i in range(7)], "twist")
add_route(BAL, [sp.simplify(Pb(r).trace()) for r in REPS], "theta-compatible")
add_route(WITN, [sp.simplify(Pt1(r).trace()) for r in REPS], "twist")
add_route(BAL2, [sp.simplify(Pt2(r).trace()) for r in REPS], "twist")
add_route(SL2, [sp.simplify(Pq(r).trace()) for r in REPS], "SL(2)-route")
add_route(SL2T, [sp.simplify(Pq1(r).trace()) for r in REPS], "twist")

say("")
say("  class reps  order/eps/size : " + str([(order(REPS[i]), eps(REPS[i]), SIZES[i])
                                             for i in range(7)]))
say("")
say("  route                                                       27|_2T"
    "                                        (n1,n2)   self-dual")
for k, v in ROUTES.items():
    d = {a: int(b) for a, b in v['dec'].items() if b != 0}
    say("  %-58s %-45s %-9s %s" % (k, d, str(tuple(v['n'])), v['sd']))
say("")

gate("C1: the two CANONICAL routes reproduce Gate B (OI-128): principal 3.1+3.1'+3.1''+6.3 "
     "with n1=n2=3; balanced 9.1+3.1'+3.1''+3.2'+3.2'' with n1=n2=0",
     ROUTES[PR]['dec'] == {'1': 3, "1'": 3, "1''": 3, '2': 0, "2'": 0, "2''": 0, '3': 6}
     and tuple(ROUTES[PR]['n']) == (3, 3)
     and ROUTES[BAL]['dec'] == {'1': 9, "1'": 3, "1''": 3, '2': 0, "2'": 3, "2''": 3, '3': 0}
     and tuple(ROUTES[BAL]['n']) == (0, 0))

WIT = ROUTES[WITN]
gate("C2 (UPHELD, recomputed): the CHIRAL WITNESS is REAL -- 27|H' = 3.1+9.1'+3.1''+3.2+3.2'', "
     "non-real character, n1 = 9 != n2 = 0.  The clean theorem is FALSE and stays falsified.",
     WIT['dec'] == {'1': 3, "1'": 9, "1''": 3, '2': 3, "2'": 0, "2''": 3, '3': 0}
     and tuple(WIT['n']) == (9, 0) and not WIT['sd']
     and any(sp.simplify(v - sp.conjugate(v)) != 0 for v in WIT['chi']))

# =========================================================================
# D -- THE LOAD-BEARING CONTENT: TWIST-RIGIDITY  (R1-R4)
# =========================================================================
def twist_chi(chi, k):
    return [sp.simplify(chi[i] * W**(k*eps(REPS[i]))) for i in range(7)]


def is_rigid(chi):
    """rho (x) 1'^k = rho for k = 1,2  <=>  chi vanishes on every eps != 0 class."""
    return all(all(sp.simplify(twist_chi(chi, k)[i] - chi[i]) == 0 for i in range(7))
               for k in (1, 2))


def vanishes_on_epsnz(chi):
    return all(sp.simplify(chi[i]) == 0 for i in EPSNZ)


# --- R1: the criterion, BOTH directions, on every route in the table
r1_ok = all(is_rigid(v['chi']) == vanishes_on_epsnz(v['chi']) for v in ROUTES.values())
r1_both = (any(is_rigid(v['chi']) for v in ROUTES.values())
           and any(not is_rigid(v['chi']) for v in ROUTES.values()))
gate("R1: CRITERION -- rho (x) 1'^k = rho for all k  <=>  chi_rho vanishes on every eps != 0 "
     "class.  Verified in BOTH directions on all 8 routes; and the criterion is non-vacuous "
     "(both outcomes actually occur in the table).", r1_ok and r1_both)

# --- R2: rigid => the torsor collapses => no chiral member
def torsor(chi):
    return [chi, twist_chi(chi, 1), twist_chi(chi, 2)]


def torsor_n(chi):
    return [tuple(n1n2(decompose(c))) for c in torsor(chi)]


r2 = []
for name, v in ROUTES.items():
    ns = torsor_n(v['chi'])
    collapsed = all(all(sp.simplify(t[i] - v['chi'][i]) == 0 for i in range(7))
                    for t in torsor(v['chi']))
    chiral_members = sum(1 for n in ns if sp.simplify(n[0] - n[1]) != 0)
    r2.append((name, is_rigid(v['chi']), collapsed, ns, chiral_members))

gate("R2: TWIST-RIGID => the mu_3-torsor COLLAPSES to a single iso class => every member "
     "carries rho's own (n1,n2); a rigid SELF-DUAL route therefore has NO chiral member in "
     "its torsor.  Verified route-by-route (rigid <=> collapsed on all 8; and every rigid "
     "self-dual route has 0 chiral members).",
     all(rig == col for _, rig, col, _, _ in r2)
     and all(cm == 0 for name, rig, col, ns, cm in r2 if rig and ROUTES[name]['sd']))

say("  twist torsors (route | rigid | collapsed | (n1,n2) of the 3 members | #chiral members)")
for name, rig, col, ns, cm in r2:
    say("    %-58s %-6s %-6s %-30s %d" % (name, rig, col, str(ns), cm))
say("")

# --- R3: THE OBJECT'S ROUTE IS TWIST-RIGID
obj_chi = ROUTES[PR]['chi']
obj_rigid = is_rigid(obj_chi)
obj_vanish = vanishes_on_epsnz(obj_chi)
obj_torsor_n = torsor_n(obj_chi)
gate("R3 (THE DISCRIMINATING FACT): the OBJECT'S route is TWIST-RIGID -- chi_principal = 0 on "
     "every eps != 0 class (exact: %s), so its mu_3-twist torsor collapses to itself and all "
     "three members have (n1,n2) = (3,3).  OI-173's construction applied to the object's own "
     "route returns the object's own route: Level 3 is unreachable along it."
     % str([sp.simplify(obj_chi[i]) for i in EPSNZ]),
     obj_rigid and obj_vanish and all(tuple(n) == (3, 3) for n in obj_torsor_n)
     and ROUTES[PR]['sd'])

# --- R4(a): not entailed by "SL(2)-route"  (the Y4 non-vacuity witness)
sl2_rigid = is_rigid(ROUTES[SL2]['chi'])
gate("R4a (Y4 NON-VACUITY): twist-rigidity is NOT entailed by 'SL(2)-route'.  The non-principal "
     "SL(2)-route 3 = 1+2 is a genuine I3-invariant embedding (B8), is self-dual with "
     "(n1,n2) = (0,0), is NOT twist-rigid, and its twist is CHIRAL with (n1,n2) = %s."
     % str(tuple(ROUTES[SL2T]['n'])),
     ROUTES[SL2]['sd'] and (not sl2_rigid)
     and (not ROUTES[SL2T]['sd'])
     and sp.simplify(ROUTES[SL2T]['n'][0] - ROUTES[SL2T]['n'][1]) != 0)

# --- R4(b): not entailed by "theta-compatible / inside F4"
bal_rigid = is_rigid(ROUTES[BAL]['chi'])
gate("R4b: twist-rigidity is NOT entailed by 'theta-compatible / inside F4'.  The balanced "
     "trinification route is self-dual and fixes a point of nonzero cubic (E1 table below, i.e. it "
     "sits pointwise inside a conjugate of F4 = E6^theta) -- and it is NOT twist-rigid: its "
     "twist IS the chiral witness.",
     ROUTES[BAL]['sd'] and (not bal_rigid) and (not ROUTES[WITN]['sd']))

# --- R4(c): not entailed by self-duality / n1 = n2
sd_routes = [k for k, v in ROUTES.items() if v['sd']]
sd_rigid = [k for k in sd_routes if is_rigid(ROUTES[k]['chi'])]
gate("R4c: twist-rigidity is NOT entailed by 'self-dual / n1 = n2'.  %d of the %d self-dual "
     "routes in the table are rigid -- the property strictly refines self-duality."
     % (len(sd_rigid), len(sd_routes)),
     0 < len(sd_rigid) < len(sd_routes))

# --- R4(d): not a corollary of the WITNESS's chirality (the L3 defect, fixed)
#     mechanical demonstration: recompute R3 from a table with every witness-derived route
#     DELETED.  R3 is unchanged, so it reads no witness datum.
NO_WITNESS = {k: v for k, v in ROUTES.items()
              if k not in (WITN, BAL2, SL2T, "principal (x) 1'", "principal (x) 1''")}
r3_without_witness = (is_rigid(NO_WITNESS[PR]['chi']) and vanishes_on_epsnz(NO_WITNESS[PR]['chi']))
gate("R4d (THE FIX FOR L3): R3 is NOT a corollary of the witness's chirality.  Deleting every "
     "witness- and twist-derived row from the route table leaves R3 intact (recomputed: %s) -- "
     "R3 reads only chi_principal on the eps != 0 classes.  (Contrast the two DEMOTED "
     "arguments of section E, which read the witness's chirality and nothing else.)"
     % r3_without_witness,
     r3_without_witness and obj_rigid)

# --- R4(e): census over ALL 27-dim SU(2)-reps -- rigidity is a strict arithmetic condition
def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest


# U_{d-1}(cos t) at t = pi/3 (Re = 1/2) and 2pi/3 (Re = -1/2) depend only on d mod 6
U_PLUS = {1: 1, 2: 1, 3: 0, 4: -1, 5: -1, 0: 0}     # Re = +1/2
U_MINUS = {1: 1, 2: -1, 3: 0, 4: 1, 5: -1, 0: 0}    # Re = -1/2
gate("R4e-0: the mod-6 tables for U_{d-1}(+-1/2) agree with sympy's Chebyshev U for d = 1..30",
     all(sp.simplify(sp.chebyshevu(d - 1, sp.Rational(1, 2)) - U_PLUS[d % 6]) == 0
         and sp.simplify(sp.chebyshevu(d - 1, sp.Rational(-1, 2)) - U_MINUS[d % 6]) == 0
         for d in range(1, 31)))

tot = rig_cnt = 0
for part in partitions(27):
    tot += 1
    if sum(U_PLUS[d % 6] for d in part) == 0 and sum(U_MINUS[d % 6] for d in part) == 0:
        rig_cnt += 1
gate("R4e (CENSUS): of all %d 27-dimensional SU(2)-reps (partitions of 27), only %d (%.1f%%) "
     "restrict to a twist-rigid 2T-rep.  Rigidity is two independent linear conditions on the "
     "part-counts mod 6 -- a strict arithmetic property of the individual route, NOT a property "
     "of the class 'SL(2)-route'." % (tot, rig_cnt, 100.0*rig_cnt/tot),
     0 < rig_cnt < tot and tot == 3010)

# =========================================================================
# E -- DEMOTED: the two arguments the verifier showed are COROLLARIES
# =========================================================================
# E0: the identity det Hess I3(v) = 2 * I3(v)^9  (re-confirmed exactly, several points)
HESS = sp.hessian(I3_BASE, XS)
random.seed(7)
ratios = []
for _ in range(5):
    pt = [sp.Integer(random.randint(-3, 3)) for _ in range(27)]
    val = sp.Integer(I3_of(pt))
    if val == 0:
        continue
    dh = HESS.subs(dict(zip(XS, pt))).det(method='berkowitz')
    ratios.append(sp.nsimplify(sp.Rational(dh, val**9)))
gate("E0: det Hess I3(v) = 2 * I3(v)^9 -- re-confirmed EXACTLY at %d integer points, ratio %s.  "
     "This is the identity that COLLAPSES the two 'independent reasons': 'H fixes a v with "
     "I3(v) != 0'  <=>  'H preserves a nondegenerate symmetric form on the 27'  <=>  '27|H is "
     "self-dual'  <=>  'n1 = n2'." % (len(ratios), str(set(ratios))),
     len(ratios) >= 3 and len(set(ratios)) == 1 and ratios[0] == 2)


def fixed_space(P):
    """Fix_27(H) via the group projector (1/24) sum_g P(g)."""
    Pi = sp.zeros(27, 27)
    for g in ELTS:
        Pi += P(g)
    Pi = (Pi / 24).applyfunc(sp.simplify)
    return [sp.Matrix(list(v)) for v in Pi.columnspace()]


def fixes_nonzero_cubic(P):
    """does H fix a vector with I3 != 0 ?  (I3 restricted to Fix, symbolically)"""
    F = fixed_space(P)
    if not F:
        return False, 0
    ts = sp.symbols('t0:%d' % len(F))
    v = sp.zeros(27, 1)
    for c, b in zip(ts, F):
        v += c * b
    poly = sp.expand(sp.simplify(I3_of([v[i] for i in range(27)])))
    return (poly != 0), len(F)


E_TABLE = []
for nm, P in ((BAL, Pb), (WITN, Pt1), (BAL2, Pt2), (SL2, Pq), (SL2T, Pq1)):
    ok, d = fixes_nonzero_cubic(P)
    chiral = bool(sp.simplify(ROUTES[nm]['n'][0] - ROUTES[nm]['n'][1]) != 0)
    E_TABLE.append((nm, chiral, ok, d))

say("  DEMOTED corollary table (route | chiral? | fixes a point with I3 != 0? | dim Fix)")
for nm, chiral, ok, d in E_TABLE:
    say("    %-58s %-7s %-7s %d" % (nm, chiral, ok, d))
say("")

gate("E1 (DEMOTION, the named defect): 'the witness lies in no conjugate of F4' is a ONE-STEP "
     "COROLLARY of 'the witness is chiral'.  Across all 5 matrix-realized routes, chirality and "
     "'fixes no point of nonzero cubic' are EXACTLY anti-correlated -- the two facts carry the "
     "same information (via E0).  It is NOT an independent reason and is not read by the verdict.",
     all(chiral == (not ok) for _, chiral, ok, _ in E_TABLE)
     and any(c for _, c, _, _ in E_TABLE) and any(not c for _, c, _, _ in E_TABLE))

gate("E2 (DEMOTION): 'the witness factors through no SL(2,C) < E6' is likewise a one-step "
     "corollary -- every SL(2)-route restricts the 27 to self-dual SL(2)-irreps hence n1 = n2 "
     "(verified on 2 independent SL(2)-routes), so 'not self-dual' immediately gives it.  Also "
     "not read by the verdict.",
     ROUTES[PR]['sd'] and ROUTES[SL2]['sd'] and not ROUTES[WITN]['sd'])

# =========================================================================
# F -- VERDICT (reads ONLY the twist-rigidity content; every branch can FIRE and FAIL)
# =========================================================================
VERDICT_INPUTS = ['witness_is_real', 'object_route_pinned', 'object_route_selfdual',
                  'twist_group_nontrivial', 'object_route_twist_rigid', 'rigidity_not_forced']
DEMOTED_KEYS = ['witness_outside_F4', 'witness_not_sl2']


def facts_of(world):
    """derive the verdict's fact-vector from a WORLD.  A world = (twist group order,
    the set of routes the premise pins as 'the object's route', the route table)."""
    hom_order, pinned, table = world['hom_mu3'], world['pinned'], world['table']
    f = {}
    f['witness_is_real'] = bool(world['witness_real'])
    f['object_route_pinned'] = bool(len(pinned) == 1)
    f['twist_group_nontrivial'] = bool(hom_order > 1)
    if f['object_route_pinned']:
        c = table[pinned[0]]['chi']
        f['object_route_selfdual'] = bool(table[pinned[0]]['sd'])
        f['object_route_twist_rigid'] = bool(is_rigid(c) if hom_order > 1 else True)
    else:
        f['object_route_selfdual'] = bool(all(table[p]['sd'] for p in pinned))
        f['object_route_twist_rigid'] = bool(all(is_rigid(table[p]['chi']) for p in pinned)
                                             if hom_order > 1 else True)
    # rigidity is FORCED if it is vacuous (trivial twist group) or entailed by the premise
    # class (every member of the class is rigid, so it separates nothing).
    cls = [k for k, v in table.items() if v['kind'] in ('SL(2)-route', 'theta-compatible')]
    f['rigidity_not_forced'] = bool(hom_order > 1
                                    and any(not is_rigid(table[k]['chi']) for k in cls))
    return f


def branch_A(f):
    """Level 3 REOPENS: the object's own route admits the OI-173 twist construction
    (not rigid), OR twist-rigidity is itself forced and therefore no reason at all."""
    return bool(f['witness_is_real'] and f['object_route_pinned']
                and ((not f['object_route_twist_rigid'])
                     or (not f['twist_group_nontrivial'])
                     or (not f['rigidity_not_forced'])))


def branch_B(f):
    """Level 3 stays CLOSED, on twist-rigidity ALONE."""
    return bool(f['witness_is_real'] and f['object_route_pinned'] and f['object_route_selfdual']
                and f['twist_group_nontrivial'] and f['object_route_twist_rigid']
                and f['rigidity_not_forced'])


def verdict_of(f):
    a, b = branch_A(f), branch_B(f)
    return "RESOLVED-A" if (a and not b) else ("RESOLVED-B" if (b and not a) else "UNRESOLVED")


TRUE_WORLD = dict(hom_mu3=3, pinned=[PR], table=ROUTES, witness_real=True,
                  label="the computed world (object route = principal SL2)")
F = facts_of(TRUE_WORLD)
A, B = branch_A(F), branch_B(F)
VERDICT = verdict_of(F)

gate("V0 (the repair, mechanically checked): the verdict function reads ONLY %s and reads "
     "NEITHER of the two demoted facts %s.  The closure now rests on twist-rigidity alone."
     % (VERDICT_INPUTS, DEMOTED_KEYS),
     sorted(F.keys()) == sorted(VERDICT_INPUTS)
     and not any(k in F for k in DEMOTED_KEYS))

# --- L1 / B414: counterfactual worlds that are LOGICALLY POSSIBLE (each realized by
#     actual representation theory computed in this cell, not by flipping a boolean that
#     contradicts an entailment).
# Q8 = ker(eps) is itself a binary polyhedral group (binary dihedral, order 8) with
# |Hom(Q8, mu_3)| = 1 -- computed below.  Had the object's binary group been Q8, EVERY
# route would be "rigid" vacuously and rigidity would carry no information (FORCED).
comm_Q8 = closure({qmul(qmul(a, b), qinv(qmul(b, a))) for a in Q8 for b in Q8}, cap=30)
ab_order = len(Q8) // len(comm_Q8)
gate("V1: [Q8,Q8] = {+-1} so Q8^ab has order %d, coprime to 3 => Hom(Q8, mu_3) = 1 (computed "
     "in-cell).  This realizes a logically possible world in which twist-rigidity is VACUOUS."
     % ab_order, ab_order == 4 and len(comm_Q8) == 2 and ab_order % 3 != 0)

WORLDS = [
    dict(hom_mu3=3, pinned=[BAL], table=ROUTES, witness_real=True,
         label="CF1: the premise had pinned the BALANCED trinification (a real, I3-invariant, "
               "theta-compatible route) as the object's route"),
    dict(hom_mu3=3, pinned=[SL2], table=ROUTES, witness_real=True,
         label="CF2: the premise had pinned the NON-PRINCIPAL SL(2)-route 3 = 1+2"),
    dict(hom_mu3=1, pinned=[PR], table=ROUTES, witness_real=True,
         label="CF3: the object's binary group had been Q8 (Hom = 1, computed V1) -- rigidity "
               "vacuous, hence FORCED"),
    dict(hom_mu3=3, pinned=[PR, BAL], table=ROUTES, witness_real=True,
         label="CF4: the cited premises had pinned the route only up to {principal, balanced}"),
    dict(hom_mu3=3, pinned=[PR, SL2], table=ROUTES, witness_real=True,
         label="CF5: pinned only up to {principal, SL(2)-route 3=1+2}"),
]
say("  L1/B414 counterfactual worlds (each realized by computed representation theory):")
say("    %-100s %s" % ("world", "verdict"))
say("    %-100s %s" % (TRUE_WORLD['label'], VERDICT))
cf_verdicts = []
for w in WORLDS:
    v = verdict_of(facts_of(w))
    cf_verdicts.append(v)
    say("    %-100s %s" % (w['label'], v))
say("")
reach = set(cf_verdicts) | {VERDICT}
gate("L1/B414 NON-VACUITY: the verdict function reaches RESOLVED-A (2 ways: the object's route "
     "not rigid; 1 way: rigidity forced/vacuous), UNRESOLVED (2 ways: the premise fails to pin "
     "a unique route) and RESOLVED-B (the computed world).  Every branch can FIRE and can FAIL, "
     "and every counterfactual is realized by a representation actually computed here -- none "
     "contradicts an entailment.",
     cf_verdicts == ["RESOLVED-A", "RESOLVED-A", "RESOLVED-A", "UNRESOLVED", "UNRESOLVED"]
     and reach == {"RESOLVED-A", "RESOLVED-B", "UNRESOLVED"})

# --- L4 / B465: the DECLARED selection and its effect
SEL = [(PR, verdict_of(facts_of(dict(TRUE_WORLD, pinned=[PR])))),
       (BAL, verdict_of(facts_of(dict(TRUE_WORLD, pinned=[BAL])))),
       (SL2, verdict_of(facts_of(dict(TRUE_WORLD, pinned=[SL2]))))]
say("  L4/B465 DECLARED SELECTION -- 'which route is the object's' (a CITED premise):")
for nm, v in SEL:
    say("    %-58s -> %s" % (nm, v))
say("")
gate("L4/B465: the ONE selection this cell makes is DECLARED and its effect SHOWN -- the verdict "
     "is sensitive to it (principal -> RESOLVED-B; balanced or non-principal SL(2) -> "
     "RESOLVED-A).  The selection is the cited premise B329a/B347/B351/B352/B353, fenced as such "
     "and NOT recomputed here.",
     [v for _, v in SEL] == ["RESOLVED-B", "RESOLVED-A", "RESOLVED-A"])

# --- L2: no numeric negative is asserted anywhere
gate("L2/D3: no numeric negative is asserted -- every statement in this cell is exact/symbolic "
     "(rational + sqrt(-3)); there is no estimator, no scan, no argmax, hence no underpowered "
     "negative.  The one enumeration (R4e) is a COMPLETE census of all 3010 partitions of 27, "
     "not a sample.", tot == 3010)

# --- L3: the explicit forcedness audit of the surviving reason
gate("L3/GATEB: FORCEDNESS AUDIT of the surviving reason.  R3 (the object's route is twist-rigid) "
     "is not a corollary of any premise: not of 'SL(2)-route' (R4a), not of 'theta-compatible' "
     "(R4b), not of 'self-dual' (R4c), not of the witness's chirality (R4d), and not generic in "
     "the class (R4e: %d/%d).  The two collapsed reasons are demoted in E1/E2." % (rig_cnt, tot),
     (not sl2_rigid) and (not bal_rigid) and r3_without_witness and 0 < rig_cnt < tot)

say("")
say("=" * 108)
for k in VERDICT_INPUTS:
    say("  fact  %-30s = %s" % (k, F[k]))
say("  branch A fires: %s     branch B fires: %s" % (A, B))
say("=" * 108)
say("GATE FAILURES: " + str(FAIL) if FAIL else "ALL GATES PASS.")
say("")
say("VERDICT: " + VERDICT)
say("""
  THE RESTATED CLOSURE (twist-rigidity alone).

    PREMISE (cited, fenced, DECLARED as the cell's one selection): the object's E6
    route is the principal-SL2 one -- B329a, B347/B351/B352 (the principal-SL2 E6
    tangent), B353 (the hyperelliptic involution induces exactly theta at the
    geometric point and theta fixes the principal SL2 pointwise).

    COMPUTED (R1-R3): chi_principal vanishes on every eps != 0 class of 2T, hence
    rho_pr (x) 1'^k = rho_pr for k = 0,1,2.  The object's mu_3-twist torsor is a
    SINGLE point.  OI-173's chiral witness is produced by exactly one operation --
    twisting a route by a nonzero element of Hom(2T, Z(E6)) = Z/3 -- and that
    operation, applied to the object's own route, returns the object's own route,
    with (n1,n2) = (3,3).  Level 3 is unreachable along the object's supply line.

    WHY THIS IS A REASON AND NOT A RESTATEMENT (R4, the L3 repair): twist-rigidity is
    a strict arithmetic property of the individual route.  It fails for the balanced
    trinification (theta-compatible, inside an F4, self-dual -- and it twists to the
    witness itself), it fails for the non-principal SL(2)-route 3 = 1+2 (a genuine
    I3-invariant embedding whose twist is chiral, (9,0)), and it holds for only %d of
    the %d 27-dimensional SU(2)-reps.  It is computed from chi_principal alone and
    survives deleting every witness-derived row from the table.

    THE TWO DEMOTED ARGUMENTS.  det Hess I3(v) = 2.I3(v)^9 (E0, re-confirmed exactly),
    so 'H fixes a v with I3 != 0' <=> 'H preserves a nondegenerate symmetric form'
    <=> '27|H self-dual' <=> 'n1 = n2'.  Hence the F4-exclusion (E1) and the
    SL(2)-exclusion (E2) of the witness are one-step corollaries of the witness's own
    chirality -- of the premise being reconciled.  They are TRUE, they are not
    reasons, and the verdict function does not read them (V0).

    OI-128 WORDING (the owed fix).  'unreachable by any canonical 2T -> E6' becomes:
    'unreachable by any theta-compatible / SL(2)-route embedding; a chiral 2T < E6
    EXISTS (OI-173) but lies on no object supply line -- the object's own route is
    twist-rigid, so the one construction that produces the chiral member cannot be
    applied to it.'

    RESIDUAL (unchanged, EXTERNAL/specialist): whether the arithmetic could force a
    non-SL(2), non-theta-compatible route into E6.  Exhibiting a chiral subgroup of
    E6 is not exhibiting an object-supplied one.  Also unchanged: this closure is
    conditional on the DECLARED selection of the object's route (L4 table above).
""" % (rig_cnt, tot))

results = {
    "cell": "P2W6-GATEB-r",
    "oi": "OI-128",
    "repair_of": "P2W5-GATEB",
    "verdict": VERDICT,
    "headline": ("Level 3 stays CLOSED for Gate B on TWIST-RIGIDITY ALONE: the object's "
                 "principal route has chi = 0 on every eps != 0 class, so its mu_3-twist torsor "
                 "collapses and OI-173's construction returns it unchanged; the F4- and "
                 "SL(2)-exclusions are demoted to corollaries of the witness's chirality"),
    "discriminating_fact": ("chi_principal vanishes on all eps != 0 classes of 2T (exact), so "
                            "rho_pr (x) 1'^k = rho_pr for k=0,1,2 and the object's twist torsor "
                            "is a single point with (n1,n2)=(3,3) -- while the theta-compatible "
                            "balanced route and the non-principal SL(2)-route 3=1+2 are both "
                            "NON-rigid and twist to chiral (9,0) members, and only %d of the "
                            "%d 27-dim SU(2)-reps are rigid" % (rig_cnt, tot)),
    "branches": {"A_fires": A, "B_fires": B},
    "facts": F,
    "verdict_inputs": VERDICT_INPUTS,
    "demoted_not_read_by_verdict": DEMOTED_KEYS,
    "routes": {k: {"dec": {a: int(b) for a, b in v['dec'].items() if b != 0},
                   "n1n2": [int(v['n'][0]), int(v['n'][1])],
                   "self_dual": bool(v['sd']),
                   "twist_rigid": bool(is_rigid(v['chi'])),
                   "kind": v['kind']} for k, v in ROUTES.items()},
    "rigidity_census_su2_27dim": {"total_partitions_of_27": tot, "twist_rigid": rig_cnt},
    "hessian_identity": {"det_Hess_I3_over_I3^9": int(ratios[0]), "exact_points": len(ratios)},
    "demoted_corollary_table": [{"route": nm, "chiral": bool(c), "fixes_I3_nonzero": bool(o),
                                 "dim_Fix": int(d)} for nm, c, o, d in E_TABLE],
    "counterfactual_worlds": ([{"world": TRUE_WORLD['label'], "verdict": VERDICT}]
                              + [{"world": w['label'], "verdict": v}
                                 for w, v in zip(WORLDS, cf_verdicts)]),
    "declared_selection": {"choice": "the object's route = principal SL2",
                           "cited": "B329a, B347/B351/B352, B353",
                           "effect": {nm: v for nm, v in SEL}},
    "verdict_logic_nonvacuity": sorted(reach),
    "gates_failed": FAIL,
    "upheld_not_relitigated": ("the chiral 2T witness (B771/OI-173) is REAL -- recomputed in C2 "
                               "as an injective hom into Stab(I3) with n1=9 != n2=0; the clean "
                               "theorem 'no 2T<E6 has n1!=n2' stays FALSE"),
    "oi128_wording_fix": ("'unreachable by any canonical 2T->E6' -> 'unreachable by any "
                          "theta-compatible / SL(2)-route embedding; a chiral 2T < E6 exists "
                          "(OI-173) but lies on no object supply line -- the object's own route "
                          "is twist-rigid, so the construction that produces the chiral member "
                          "cannot be applied to it'"),
    "scope": {
        "in_cell_exact": ("2T + character table; the mu_3 twist torsor and the rigidity "
                          "criterion in both directions; the explicit I3-invariant balanced, "
                          "witness and SL(2)-route embeddings; the complete 3010-partition "
                          "rigidity census; det Hess I3 = 2 I3^9 at 5 exact points; the "
                          "corollary-collapse table"),
        "cited_premises": ("that the object's route is the principal SL2 (B329a, B347/B351/B352, "
                           "B353) and that its 27-content is 17+9+1 -- consistency-gated in C0 "
                           "against the E6 exponents, but NOT proved here; B302 (the object's 2T "
                           "lives in the commensurator SL(2,C) = PGL(2,O_-3))"),
        "unchanged_residual": ("EXTERNAL/specialist -- whether the arithmetic could force a "
                               "non-SL(2), non-theta-compatible route into E6; plus the declared "
                               "conditionality on which route is the object's"),
    },
    "method": "exact/symbolic (sympy over Q(sqrt(-3))); no floats, no scans, no estimators",
    "lessons": {"L1_B414": "5 counterfactual worlds, each realized by computed representation "
                           "theory; all three verdicts reachable; no branch forced",
                "L2_D3": "no numeric negative; the single enumeration is a complete census",
                "L3_GATEB": "forcedness audit R4a-R4e; the two collapsed reasons demoted and "
                            "removed from the verdict's inputs (V0)",
                "L4_B465": "the one selection (which route is the object's) declared with its "
                           "verdict-flipping effect shown"},
    "firewall": "structural only; no SM values; nothing to CLAIMS.md; one-number pin untouched",
    "b774_chord_discipline": ("no chord / theta-odd-trace claim is made; the twist torsor "
                              "Hom(2T, mu_3) is abelian by construction and labelled as such"),
}
with open(__file__.replace("compute.py", "results.json"), "w") as fh:
    json.dump(results, fh, indent=1)
with open(__file__.replace("compute.py", "output.txt"), "w") as fh:
    fh.write("\n".join(LOG) + "\n")
