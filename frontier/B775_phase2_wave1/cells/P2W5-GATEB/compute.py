"""P2W5-GATEB (OI-128) -- Gate-B / chiral-2T reconciliation: does Level 3 reopen?

B775 Phase-2 Wave-5.  STRUCTURAL cell.  Everything below is recomputed in-cell
(2T, its character table, the explicit 27-dim embeddings, the E6 cubic) -- nothing
is transcribed from B326/B327/B329/B356/B771-OI-173.

THE COLLISION
  OI-128 (Gate B, from B327+B329): BOTH canonical 2T -> E6 routes (quaternionic
  SU(2) and complex trinification) give n1 = n2, so Level 3 (split light
  generations) is unreachable "by any canonical embedding"; the residual is a
  chiral (non-sigma-stable) embedding "for which no natural candidate exists".
  B771-P2 / OI-173: a chiral candidate DOES exist -- the center-twisted
  trinification rho'(g) = w^{eps(g)} rho_b(g) -- with 27|_2T non-self-conjugate
  and n1 = 9 != n2 = 0.

SEALED CRITERION
  the chiral embedding reopens Level 3 for Gate B                      => RESOLVED-A
  it fails Gate B's own sigma-stability requirement, Level 3 stays closed => RESOLVED-B
  otherwise                                                            => UNRESOLVED

WHAT IS ACTUALLY COMPUTED HERE (the discriminating facts, all in-cell)
  T1  self-duality of 27|H  =>  n1 = n2                                  (exact)
  T2  H fixes v in 27 with nondegenerate Hessian of the cubic  =>  27|H
      carries an invariant nondegenerate symmetric form  =>  self-dual  =>  n1 = n2
      (this is the "H sits inside a conjugate of F4 = E6^theta" register,
      proved WITHOUT citing Stab(v) = F4)
  T3  every SL(2,C)-route  =>  27|H self-dual  =>  n1 = n2               (exact)
  X1  the chiral witness H': Fix_27(H') is 3-dimensional, every fixed vector has
      RANK <= 1, and the cubic I3 vanishes IDENTICALLY on Fix(H')
      => H' lies in NO conjugate of F4 = E6^theta                        (symbolic)
      (contrast: the balanced route fixes a rank-3 point, I3 = 1, Hessian
      determinant nonzero -- it sits pointwise inside a conjugate of F4)
  X2  27|H' is not self-dual => H' factors through no SL(2,C) subgroup of E6
  Y   THE TWIST TORSOR.  The three embeddings {rho, rho (x) 1', rho (x) 1''} form
      a torsor under Hom(2T, Z(E6)) = Hom(2T, mu_3) = Z/3, and complex conjugation
      (= the E6 diagram involution sigma = theta on the 27) INVERTS the torsor.
      Hence: if rho is sigma-stable, exactly ONE member of its torsor is
      sigma-stable -- the untwisted one -- unless the torsor COLLAPSES.
      Computed: the balanced trinification torsor = {n1=n2=0 (sigma-stable),
      (9,0), (0,9)} (the two chiral members swapped by sigma); the PRINCIPAL
      torsor COLLAPSES (chi vanishes on every eps != 0 class), so the object's
      own route is twist-RIGID: it has no chiral member at all.

THE RECONCILIATION (why this is a reconciliation and not a re-run of OI-173)
  OI-173 is right about E6 and wrong about Gate B only if Gate B is read as the
  bare question "does SOME 2T < E6 have n1 != n2".  Gate B's sigma-stability
  register is not an extra axiom: it is the object's amphichirality.  B353
  certified that the figure-eight's hyperelliptic involution induces EXACTLY the
  E6 diagram involution theta on the tangent at the geometric point, and that
  theta fixes the principal SL2 pointwise.  The object's 2T is a finite subgroup
  of its commensurator SL(2,C) = PGL(2,O_-3) (B302), i.e. an SL(2)-route.  T3
  closes every SL(2)-route; Y shows that the principal route cannot even be
  twisted; and the only way to reach the chiral witness is to CHOOSE a nonzero
  element of Hom(2T, mu_3) = Z/3 -- a chirality choice that theta inverts and an
  amphichiral object cannot make.  The witness is a genuine E6 fact that sits off
  every supply line the object has.

Exact/symbolic throughout (sympy over Q(sqrt(-3))); the only floating point is a
cross-check of an exact result.  No SM values, nothing to CLAIMS.md.
Re-runnable: pyenv python3 compute.py   (sympy + numpy).
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
    for k in range(1, 13):
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
gate("A3: ker(eps) = Q8 (the abelianization 2T/Q8 = Z/3)",
     set(g for g in ELTS if eps(g) == 0) == Q8)

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


def decompose(chi_vals):
    return {n: sp.nsimplify(sp.simplify(sum(SIZES[i] * chi_vals[i] * sp.conjugate(IRR[n](REPS[i]))
                                            for i in range(7)) / 24)) for n in NAMES}


def n1n2(dec):
    return (sp.simplify(dec["1'"] - dec["2'"]), sp.simplify(dec["1''"] - dec["2''"]))


def self_dual(dec):
    """27|H self-conjugate <=> multiplicities invariant under complex conjugation
    of irreps (1' <-> 1'', 2' <-> 2''; 1, 2, 3 real)."""
    return sp.simplify(dec["1'"] - dec["1''"]) == 0 and sp.simplify(dec["2'"] - dec["2''"]) == 0


# =========================================================================
# B -- explicit SU(3) factors and the 27 (trinification basis) + the cubic
# =========================================================================
def rho2(q):
    a, b, c, d = q
    return sp.Matrix([[a + b*sp.I, c + d*sp.I], [-c + d*sp.I, a - b*sp.I]])


def rho3(g):
    """the faithful complex 3 = 1' + 2' of 2T inside SU(3)  (B329's route (b))."""
    e = eps(g)
    m = sp.zeros(3, 3)
    m[0, 0] = W**e
    m[1:, 1:] = (W**e) * rho2(g)
    return m.applyfunc(sp.expand)


def rho3_sl2(g):
    """an SL(2,C)-ROUTE factor: 3 = 1 + 2 (the quaternionic 2), det = det rho2 = 1."""
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
gate("B3: w^3 = 1 (the mu_3 centre of E6: a scalar preserves a cubic iff w^3 = 1)",
     sp.simplify(W**3 - 1) == 0)

GI = (0, 1, 0, 0)                       # order 4, eps = 0
GT = (sp.Rational(1, 2),) * 4           # order 6, eps != 0


def closure(gens):
    S = {(1, 0, 0, 0)}
    front = set(gens)
    while front:
        S |= front
        front = {qmul(a, b) for a in S for b in S} - S
    return S


gate("B4: <i, (1+i+j+k)/2> = 2T (generators verified by closure)",
     closure({GI, GT}) == set(ELTS))


def kron(A, B):
    p, q = B.shape
    return sp.Matrix(A.shape[0]*p, A.shape[1]*q,
                     lambda i, j: A[i//p, j//q] * B[i % p, j % q])


I3M = sp.eye(3)


def P_of(A, B, C):
    """27 = (3,3b,1)+(1,3,3b)+(3b,1,3):  M1 -> A M1 B^dag, M2 -> B M2 C^dag, M3 -> C M3 A^dag."""
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

gate("B5: I3 is invariant under the balanced route on both generators (symbolic, 27 vars)",
     invariant_under(Pb(GI)) and invariant_under(Pb(GT)))
gate("B6: I3 is invariant under the central scalar w.Id (so every twist stays in E6)",
     invariant_under(W * sp.eye(27)))
gate("B7: I3 is invariant under the CHIRAL witness on both generators (symbolic, 27 vars)",
     invariant_under(Pt1(GI)) and invariant_under(Pt1(GT)))
gate("B8: I3 invariant under the SL(2)-route on both generators (symbolic, 27 vars)",
     invariant_under(Pq(GI)) and invariant_under(Pq(GT)))

# homomorphism + injectivity of the witness (exact, on a generated sample)
random.seed(11)
PAIRS = [(random.choice(ELTS), random.choice(ELTS)) for _ in range(25)] + [(GI, GT), (GT, GI)]
gate("B9: the chiral witness rho' = w^eps . Pb is a homomorphism (exact, 27 sampled pairs "
     "+ both generator pairs; structural from A2+B1+B3)",
     all((Pt1(qmul(g, h)) - Pt1(g)*Pt1(h)).applyfunc(sp.simplify).is_zero_matrix
         for g, h in PAIRS))
gate("B10: the chiral witness is injective (Pt1(g) = Id only for g = 1; all 24, exact)",
     all(((Pt1(g) - sp.eye(27)).applyfunc(sp.simplify).is_zero_matrix) == (g == (1, 0, 0, 0))
         for g in ELTS))

# =========================================================================
# C -- the branchings 27|_2T for every route (exact characters)
# =========================================================================
# the principal route: 27 = V(16)+V(8)+V(0) of the principal SL2 (chi = U_n(Re q))
chi_pr = [sp.simplify(sum(sp.chebyshevu(n, REPS[i][0]) for n in (16, 8, 0))) for i in range(7)]

ROUTES = {}


def add_route(name, chivals):
    dec = decompose(chivals)
    ROUTES[name] = dict(chi=chivals, dec=dec, n=n1n2(dec), sd=self_dual(dec))


add_route("principal SU(2) (canonical, B329a)", chi_pr)
add_route("principal (x) 1'", [sp.simplify(chi_pr[i]*chi_1p(REPS[i])) for i in range(7)])
add_route("principal (x) 1''", [sp.simplify(chi_pr[i]*chi_1pp(REPS[i])) for i in range(7)])
add_route("balanced trinification (canonical, B329b)", [sp.simplify(Pb(r).trace()) for r in REPS])
add_route("balanced (x) 1'  = THE CHIRAL WITNESS", [sp.simplify(Pt1(r).trace()) for r in REPS])
add_route("balanced (x) 1''", [sp.simplify(Pt2(r).trace()) for r in REPS])
add_route("SL(2)-route 3 = 1+2", [sp.simplify(Pq(r).trace()) for r in REPS])
add_route("SL(2)-route (x) 1'", [sp.simplify(Pq1(r).trace()) for r in REPS])

say("")
say("  class reps            : " + str([tuple(str(c) for c in r) for r in REPS]))
say("  orders / eps / sizes  : " + str([order(r) for r in REPS]) + " / "
    + str([eps(r) for r in REPS]) + " / " + str(SIZES))
say("")
say("  route                                     27|_2T                                        "
    "(n1,n2)   self-dual")
for k, v in ROUTES.items():
    d = {a: b for a, b in v['dec'].items() if b != 0}
    say("  %-41s %-45s %-9s %s" % (k, d, str(tuple(v['n'])), v['sd']))
say("")

gate("C1: the two CANONICAL routes reproduce Gate B (OI-128): principal 3.1+3.1'+3.1''+6.3 "
     "with n1=n2=3, balanced trinification 9.1+3.1'+3.1''+3.2'+3.2'' with n1=n2=0",
     ROUTES["principal SU(2) (canonical, B329a)"]['dec'] ==
     {'1': 3, "1'": 3, "1''": 3, '2': 0, "2'": 0, "2''": 0, '3': 6}
     and tuple(ROUTES["principal SU(2) (canonical, B329a)"]['n']) == (3, 3)
     and ROUTES["balanced trinification (canonical, B329b)"]['dec'] ==
     {'1': 9, "1'": 3, "1''": 3, '2': 0, "2'": 3, "2''": 3, '3': 0}
     and tuple(ROUTES["balanced trinification (canonical, B329b)"]['n']) == (0, 0))

WIT = ROUTES["balanced (x) 1'  = THE CHIRAL WITNESS"]
gate("C2: the CHIRAL WITNESS reproduces OI-173: 27|H' = 3.1+9.1'+3.1''+3.2+3.2'', "
     "character non-real, n1 = 9 != n2 = 0  (so the witness is REAL -- it is not being deflated)",
     WIT['dec'] == {'1': 3, "1'": 9, "1''": 3, '2': 3, "2'": 0, "2''": 3, '3': 0}
     and tuple(WIT['n']) == (9, 0) and not WIT['sd']
     and any(sp.simplify(v - sp.conjugate(v)) != 0 for v in WIT['chi']))

# =========================================================================
# D -- T1 / T3: the sigma-stability theorems (exact, non-vacuously demonstrated)
# =========================================================================
# T1: self-dual  =>  n1 = n2.   Demonstrated on every route AND on random multiplicity vectors
# (so the implication is exercised, not asserted), plus its contrapositive on the witness.
random.seed(3)
rand_sd = []
for _ in range(400):
    m = {n: random.randint(0, 5) for n in NAMES}
    m["1''"] = m["1'"]
    m["2''"] = m["2'"]
    rand_sd.append(m)
gate("T1: self-dual 27|H  =>  n1 = n2  (exercised on 400 random self-dual multiplicity "
     "vectors + all 8 routes; and n1 != n2 => NOT self-dual on the witness)",
     all(n1n2(m)[0] == n1n2(m)[1] for m in rand_sd)
     and all((not v['sd']) or v['n'][0] == v['n'][1] for v in ROUTES.values())
     and (WIT['n'][0] != WIT['n'][1] and not WIT['sd']))

# T1 must be able to FAIL: a non-self-dual vector with n1 != n2 must exist (the witness is one)
gate("T1-nonvacuity: the self-duality test is not vacuous -- both outcomes occur among the "
     "computed routes (self-dual routes exist AND non-self-dual routes exist)",
     any(v['sd'] for v in ROUTES.values()) and any(not v['sd'] for v in ROUTES.values()))

# T3: every SL(2,C)-route is self-dual (all SL(2,C) irreps are self-dual, so any restriction
# of the 27 to an SL(2,C) < E6 has real character).  Verified concretely on two independent
# SL(2)-routes: the principal one and the 3 = 1+2 trinification-factor one.
gate("T3: every SL(2,C)-route gives a SELF-DUAL 27|_2T hence n1 = n2 -- verified on two "
     "independent SL(2)-routes (principal; and 3 = 1+2 inside a trinification factor)",
     ROUTES["principal SU(2) (canonical, B329a)"]['sd']
     and ROUTES["SL(2)-route 3 = 1+2"]['sd']
     and tuple(ROUTES["SL(2)-route 3 = 1+2"]['n']) == (0, 0)
     and all(sp.simplify(c - sp.conjugate(c)) == 0
             for c in ROUTES["SL(2)-route 3 = 1+2"]['chi'] + chi_pr))

# X2: the witness is NOT an SL(2)-route (its 27-restriction is not self-dual)
gate("X2: the chiral witness factors through NO SL(2,C) subgroup of E6 "
     "(27|H' non-self-dual, while every SL(2)-restriction is self-dual by T3)",
     not WIT['sd'])

# =========================================================================
# E -- T2 / X1: the F4 = E6^theta register, computed (fixed points of the cubic)
# =========================================================================
def fixed_space(P):
    """exact basis of {v in C^27 : P(g) v = v for all g in 2T}  (two generators suffice)."""
    M = sp.Matrix.vstack((P(GI) - sp.eye(27)).applyfunc(sp.expand),
                         (P(GT) - sp.eye(27)).applyfunc(sp.expand))
    return M.nullspace()


def quad_form_matrix(vnum):
    """Hessian (x2) of I3 at the point vnum: the invariant symmetric bilinear form B_v."""
    shifted = I3_of([vnum[i] + XS[i] for i in range(27)])
    poly = sp.Poly(sp.expand(shifted), *XS)
    Q = sp.zeros(27, 27)
    for mono, coeff in poly.terms():
        deg = sum(mono)
        if deg != 2:
            continue
        idx = [i for i, e in enumerate(mono) for _ in range(e)]
        i, j = idx
        if i == j:
            Q[i, i] = 2*coeff
        else:
            Q[i, j] += coeff
            Q[j, i] += coeff
    return Q


FIX_B = fixed_space(Pb)
FIX_T = fixed_space(Pt1)
say("  dim Fix_27(balanced canonical) = %d      dim Fix_27(chiral witness) = %d"
    % (len(FIX_B), len(FIX_T)))

gate("E1: dim Fix_27 matches the multiplicity of the trivial irrep in each branching "
     "(balanced 9, witness 3) -- the fixed-space computation is consistent with C",
     len(FIX_B) == ROUTES["balanced trinification (canonical, B329b)"]['dec']['1']
     and len(FIX_T) == WIT['dec']['1'])

# --- the balanced canonical route: a RANK-3 fixed point, nondegenerate Hessian
cB = sp.symbols('a0:%d' % len(FIX_B))
vB_gen = [sp.expand(sum(cB[k]*FIX_B[k][i] for k in range(len(FIX_B)))) for i in range(27)]
I3_on_FixB = sp.expand(I3_of(vB_gen))
gate("E2: the CUBIC DOES NOT VANISH on Fix_27(balanced): I3|Fix is a nonzero polynomial",
     sp.simplify(I3_on_FixB) != 0)

# an explicit rank-3 fixed point of the balanced route
vB = None
for trial in range(60):
    sub = {c: sp.Integer(random.randint(-3, 3)) for c in cB}
    cand = [sp.simplify(x.subs(sub)) for x in vB_gen]
    if sp.simplify(I3_of(cand)) != 0:
        vB = cand
        break
QB = quad_form_matrix(vB)
detQB = sp.simplify(QB.det())
say("  balanced: explicit fixed point with I3(v) = %s ; det(Hess I3 at v) = %s"
    % (sp.simplify(I3_of(vB)), detQB))
gate("T2: the balanced canonical route fixes a point v with I3(v) != 0 AND nondegenerate "
     "Hessian => 27|H carries an INVARIANT NONDEGENERATE symmetric bilinear form => "
     "27|H self-dual => n1 = n2 (this is the H < F4 = E6^theta register)",
     sp.simplify(I3_of(vB)) != 0 and detQB != 0
     and ROUTES["balanced trinification (canonical, B329b)"]['sd'])

# --- the chiral witness: EVERY fixed point has rank <= 1 and I3 vanishes identically
cT = sp.symbols('b0:%d' % len(FIX_T))
vT = [sp.expand(sum(cT[k]*FIX_T[k][i] for k in range(len(FIX_T)))) for i in range(27)]
I3_on_FixT = sp.simplify(sp.expand(I3_of(vT)))
MT = [sp.Matrix(3, 3, vT[0:9]), sp.Matrix(3, 3, vT[9:18]), sp.Matrix(3, 3, vT[18:27])]
minors = []
for M in MT:
    for i in range(2):
        for j in range(2):
            for a in range(i+1, 3):
                for b in range(j+1, 3):
                    minors.append(sp.simplify(sp.expand(M[i, j]*M[a, b] - M[i, b]*M[a, j])))
gate("X1a: the cubic VANISHES IDENTICALLY on the whole fixed space of the chiral witness "
     "(symbolic in %d free parameters): I3|Fix(H') == 0" % len(FIX_T),
     I3_on_FixT == 0)
gate("X1b: every fixed vector of the chiral witness has RANK <= 1 in each Jordan block "
     "(all 2x2 minors vanish symbolically) -- the fixed locus is a rank-1 cone",
     all(m == 0 for m in minors))

# and the Hessian is degenerate at every sampled fixed point (exact integer determinants)
dets = []
for trial in range(4):
    sub = {c: sp.Integer(random.randint(-4, 4)) for c in cT}
    pt = [sp.simplify(x.subs(sub)) for x in vT]
    dets.append(sp.simplify(quad_form_matrix(pt).det()))
say("  chiral witness: det(Hess I3) at 4 sampled fixed points = " + str(dets))
gate("X1c: the invariant symmetric form B_v is DEGENERATE at every sampled fixed point of "
     "the chiral witness (4 exact samples) -- no invariant nondegenerate form from Fix",
     all(d == 0 for d in dets))

gate("X1: THE DISCRIMINATING FACT -- the chiral witness lies in NO conjugate of "
     "F4 = E6^theta (it fixes no point of nonzero cubic), while the canonical balanced route "
     "lies pointwise INSIDE one.  The chiral witness is exactly the embedding that escapes "
     "the theta-fold the object certifies (B353).",
     I3_on_FixT == 0 and all(m == 0 for m in minors)
     and sp.simplify(I3_of(vB)) != 0 and detQB != 0)

# =========================================================================
# F -- Y: the mu_3 twist torsor and how sigma (= theta) acts on it
# =========================================================================
# sigma swaps 27 <-> 27bar, i.e. acts on characters by complex conjugation.
# chi_{rho (x) 1'^k} = chi_rho . w^{k eps}; conjugating sends k -> -k.
gate("Y1: sigma INVERTS the mu_3 twist torsor: conj(chi_{rho(x)1'^k}) = "
     "conj(chi_rho).w^{-k eps} -- verified exactly for rho = balanced, k = 0,1,2",
     all(sp.simplify(sp.conjugate(ROUTES["balanced trinification (canonical, B329b)"]['chi'][i]
                                  * W**(k*eps(REPS[i])))
                     - sp.conjugate(ROUTES["balanced trinification (canonical, B329b)"]['chi'][i])
                     * sp.conjugate(W)**(k*eps(REPS[i]))) == 0
         for i in range(7) for k in (0, 1, 2)))

bal_torsor = ["balanced trinification (canonical, B329b)",
              "balanced (x) 1'  = THE CHIRAL WITNESS", "balanced (x) 1''"]
pr_torsor = ["principal SU(2) (canonical, B329a)", "principal (x) 1'", "principal (x) 1''"]
n_sd_bal = sum(1 for k in bal_torsor if ROUTES[k]['sd'])
n_sd_pr = sum(1 for k in pr_torsor if ROUTES[k]['sd'])
pr_collapse = all(all(sp.simplify(ROUTES[pr_torsor[0]]['chi'][i] - ROUTES[k]['chi'][i]) == 0
                      for i in range(7)) for k in pr_torsor)
bal_collapse = all(all(sp.simplify(ROUTES[bal_torsor[0]]['chi'][i] - ROUTES[k]['chi'][i]) == 0
                       for i in range(7)) for k in bal_torsor)
swap_ok = all(sp.simplify(sp.conjugate(ROUTES["balanced (x) 1'  = THE CHIRAL WITNESS"]['chi'][i])
                          - ROUTES["balanced (x) 1''"]['chi'][i]) == 0 for i in range(7))
say("  twist torsors: balanced -> %d/3 sigma-stable (collapsed: %s) ; principal -> %d/3 "
    "sigma-stable (collapsed: %s)" % (n_sd_bal, bal_collapse, n_sd_pr, pr_collapse))

gate("Y2: the BALANCED torsor is a genuine Z/3 torsor with EXACTLY ONE sigma-stable member "
     "-- the untwisted canonical one; the two chiral members ((n1,n2) = (9,0) and (0,9)) are "
     "exchanged by sigma",
     n_sd_bal == 1 and not bal_collapse and swap_ok
     and ROUTES["balanced trinification (canonical, B329b)"]['sd']
     and tuple(ROUTES["balanced (x) 1''"]['n']) == (0, 9))

gate("Y3: the PRINCIPAL torsor COLLAPSES (chi_principal = 0 on every eps != 0 class), so the "
     "object's own route is TWIST-RIGID: all three twists are the same embedding, n1 = n2 = 3, "
     "no chiral member exists at all",
     pr_collapse and n_sd_pr == 3
     and all(sp.simplify(chi_pr[i]) == 0 for i in range(7) if eps(REPS[i]) != 0)
     and tuple(ROUTES["principal (x) 1'"]['n']) == (3, 3))

# the SL(2)-route 3 = 1+2 shows the twist CAN produce a chiral member from a non-principal
# SL(2)-route -- so Y3 is a property of the principal route, not a triviality.
gate("Y4-nonvacuity: the twist is NOT inert in general -- the non-principal SL(2)-route "
     "3 = 1+2 twists to a chiral embedding (%s), so Y3 is a genuine property of the "
     "PRINCIPAL route, not a tautology"
     % str(tuple(ROUTES["SL(2)-route (x) 1'"]['n'])),
     not ROUTES["SL(2)-route (x) 1'"]['sd']
     and ROUTES["SL(2)-route (x) 1'"]['n'][0] != ROUTES["SL(2)-route (x) 1'"]['n'][1])

# Hom(2T, mu_3) = Z/3 and theta acts on it by inversion: the only theta-fixed twist is 0.
homs = [k for k in (0, 1, 2)]
theta_fixed_twists = [k for k in homs if (k + k) % 3 == 0]
gate("Y5: Hom(2T, Z(E6)) = Hom(2T, mu_3) = Z/3 and theta acts by inversion k -> -k; the ONLY "
     "theta-fixed twist is k = 0.  An amphichiral object (theta = its own hyperelliptic "
     "involution, B353) can only select the untwisted, sigma-stable member.",
     theta_fixed_twists == [0])

# =========================================================================
# G -- VERDICT (every branch can FIRE and can FAIL)
# =========================================================================
# The facts the verdict reads (all computed above):
F = {}
F['witness_is_real'] = bool(WIT['n'][0] != WIT['n'][1] and not WIT['sd'])          # OI-173 stands
F['selfdual_forces_equal'] = bool(all((not v['sd']) or v['n'][0] == v['n'][1]
                                      for v in ROUTES.values()))                   # T1
F['sl2_routes_closed'] = bool(ROUTES["principal SU(2) (canonical, B329a)"]['sd']
                              and ROUTES["SL(2)-route 3 = 1+2"]['sd'])             # T3
F['witness_not_sl2'] = bool(not WIT['sd'])                                         # X2
F['witness_outside_F4'] = bool(I3_on_FixT == 0 and all(m == 0 for m in minors))    # X1
F['canonical_inside_F4'] = bool(sp.simplify(I3_of(vB)) != 0 and detQB != 0)        # T2
F['torsor_has_sigma_fixed_member'] = bool(n_sd_bal >= 1 and n_sd_pr >= 1)          # Y2/Y3
F['object_route_twist_rigid'] = bool(pr_collapse and n_sd_pr == 3)                 # Y3
F['theta_fixes_only_trivial_twist'] = bool(theta_fixed_twists == [0])              # Y5

def branch_A(f):
    """the chiral embedding REOPENS Level 3 for Gate B.  Fires if the witness sits on a supply
    line Gate B actually has -- i.e. if the witness were sigma-compatible (inside an F4, or an
    SL(2)-route), OR if the object's own routes had NO sigma-stable member (a chiral twist would
    then be FORCED), OR if the object's own route could be twisted to a chiral member."""
    return bool(f['witness_is_real'] and (
        (not f['witness_outside_F4']) or (not f['witness_not_sl2'])
        or (not f['torsor_has_sigma_fixed_member'])
        or (not f['object_route_twist_rigid'])))


def branch_B(f):
    """the chiral embedding FAILS Gate B's own sigma-stability requirement, Level 3 stays closed."""
    return bool(f['witness_is_real'] and f['selfdual_forces_equal'] and f['sl2_routes_closed']
                and f['witness_not_sl2'] and f['witness_outside_F4'] and f['canonical_inside_F4']
                and f['torsor_has_sigma_fixed_member'] and f['object_route_twist_rigid']
                and f['theta_fixes_only_trivial_twist'] and not branch_A(f))


def verdict_of(f):
    a, b = branch_A(f), branch_B(f)
    return "RESOLVED-A" if (a and not b) else ("RESOLVED-B" if (b and not a) else "UNRESOLVED")


A, B = branch_A(F), branch_B(F)
VERDICT = verdict_of(F)

# --- MB12 / B414 non-vacuity of the VERDICT LOGIC ITSELF: each branch must be able to FIRE
# and to FAIL.  Exhibit explicit counterfactual fact-vectors that land on each verdict.
cf_A1 = dict(F, witness_outside_F4=False)                 # witness inside an F4  -> reopens
cf_A2 = dict(F, object_route_twist_rigid=False,
             torsor_has_sigma_fixed_member=False)         # no sigma-stable member -> forced chiral
cf_A3 = dict(F, witness_not_sl2=False)                    # witness IS an SL(2)-route -> reopens
cf_U1 = dict(F, witness_is_real=False)                    # witness broken -> neither branch
cf_U2 = dict(F, canonical_inside_F4=False)                # B's premise fails, A does not fire
reach = {verdict_of(cf) for cf in (cf_A1, cf_A2, cf_A3, cf_U1, cf_U2, F)}
gate("MB12/B414: the verdict logic is NON-VACUOUS -- explicit counterfactual fact-vectors reach "
     "RESOLVED-A (3 distinct ways), RESOLVED-B (the computed one) and UNRESOLVED (2 ways); "
     "no branch is unreachable and none is forced",
     verdict_of(cf_A1) == "RESOLVED-A" and verdict_of(cf_A2) == "RESOLVED-A"
     and verdict_of(cf_A3) == "RESOLVED-A" and verdict_of(cf_U1) == "UNRESOLVED"
     and verdict_of(cf_U2) == "UNRESOLVED" and reach == {"RESOLVED-A", "RESOLVED-B", "UNRESOLVED"})

say("")
say("=" * 96)
for k, v in F.items():
    say("  fact  %-34s = %s" % (k, v))
say("  branch A fires: %s     branch B fires: %s" % (A, B))
say("=" * 96)
if FAIL:
    say("GATE FAILURES: " + str(FAIL))
else:
    say("ALL GATES PASS.")
say("")
say("VERDICT: " + VERDICT)
say("""
  RECONCILIATION.  OI-173's chiral 2T < E6 is REAL and is reproduced here in full
  (C2): rho'(g) = w^{eps(g)} rho_b(g) is an injective homomorphism into Stab(I3)
  with 27|H' = 3.1 + 9.1' + 3.1'' + 3.2 + 3.2'', non-real character, n1 = 9 != n2 = 0.
  It refutes the CLEAN THEOREM 'no 2T < E6 has n1 != n2'.  It does NOT reopen Gate B,
  for three independently computed reasons:

    (1) F4-EXCLUSION (X1).  Gate B's sigma is the object's own amphichirality: B353
        certified that the figure-eight's hyperelliptic involution induces exactly the
        E6 diagram involution theta at the geometric point, and theta fixes the
        principal SL2 pointwise -- the object's E6 datum is theta-fixed, i.e. lands in
        F4 = E6^theta.  Computed here: the canonical balanced route fixes a point of
        the 27 with I3 = nonzero and NONDEGENERATE Hessian (so 27|H carries an invariant
        nondegenerate symmetric form => self-dual => n1 = n2, T2), whereas the chiral
        witness's ENTIRE fixed space is a rank-1 cone on which I3 vanishes identically
        -- it lies in no conjugate of F4 at all.  The witness is precisely the embedding
        that escapes the theta-fold.

    (2) SL(2)-EXCLUSION (T3/X2).  The object's 2T is a finite subgroup of its
        commensurator SL(2,C) = PGL(2,O_-3) (the Eisenstein/Hurwitz units, B302) -- an
        SL(2)-route.  Every SL(2,C)-route restricts the 27 to a sum of self-dual
        SL(2)-irreps, hence n1 = n2 (verified on two independent SL(2)-routes).  The
        witness is not self-dual, so it factors through no SL(2,C) < E6.

    (3) THE TWIST TORSOR IS THETA-INVERTED (Y).  Reaching the witness from a canonical
        route means CHOOSING a nonzero element of Hom(2T, Z(E6)) = Z/3.  sigma = theta
        inverts that torsor (Y1/Y5): the only theta-fixed choice is the trivial one, and
        the two chiral members are exchanged by theta ((n1,n2) = (9,0) <-> (0,9)).  An
        amphichiral object cannot make that choice -- it is a chirality choice, exactly
        the kind the object's amphichirality forbids.  And the object's actual route (the
        principal SL2 used by B347/B351/B352/B353) is TWIST-RIGID: chi vanishes on every
        eps != 0 class, so its torsor collapses and has no chiral member at all (Y3) --
        while a non-principal SL(2)-route DOES twist to a chiral member (Y4), so Y3 is a
        real property of the object's route, not a tautology.

  NET.  Level 3 stays CLOSED for Gate B.  OI-128's statement must be re-worded once
  ('unreachable by any canonical embedding' -> 'unreachable by any theta-compatible /
  SL(2)-route embedding; a chiral 2T < E6 exists but sits off every supply line the
  object has').  The residual is UNCHANGED and is the one OI-173 already flagged: whether
  the arithmetic could force a non-SL(2), non-theta-compatible route.  That residual is
  EXTERNAL/specialist and is not reopened by the witness -- exhibiting a chiral subgroup
  of E6 is not exhibiting an object-supplied one.
""")

results = {
    "cell": "P2W5-GATEB",
    "oi": "OI-128",
    "verdict": VERDICT,
    "headline": ("the chiral 2T is real in E6 but lies in NO conjugate of F4 = E6^theta and in "
                 "no SL(2,C) route; theta inverts the mu_3 twist torsor and the object's "
                 "principal route is twist-rigid -- Level 3 stays closed for Gate B"),
    "discriminating_fact": ("Fix_27(chiral witness) is a 3-dim RANK-1 cone on which the E6 cubic "
                            "vanishes identically (symbolic), so the witness fixes no point of "
                            "nonzero cubic and lies in no conjugate of F4 = E6^theta; the "
                            "canonical balanced route fixes a rank-3 point (I3 != 0, "
                            "det Hess != 0) and therefore carries an invariant nondegenerate "
                            "symmetric form => self-dual => n1 = n2"),
    "branches": {"A_fires": A, "B_fires": B},
    "facts": F,
    "routes": {k: {"dec": {a: int(b) for a, b in v['dec'].items() if b != 0},
                   "n1n2": [int(v['n'][0]), int(v['n'][1])],
                   "self_dual": bool(v['sd'])} for k, v in ROUTES.items()},
    "fix_dims": {"balanced_canonical": len(FIX_B), "chiral_witness": len(FIX_T)},
    "torsors": {"balanced_sigma_stable_members": n_sd_bal, "balanced_collapsed": bal_collapse,
                "principal_sigma_stable_members": n_sd_pr, "principal_collapsed": pr_collapse},
    "verdict_logic_nonvacuity": sorted(reach),
    "gates_failed": FAIL,
    "scope": {
        "in_cell_exact": ("2T + character table; all 8 explicit 27-dim embeddings and the E6 cubic; "
                          "T1/T2/T3, X1/X2, Y1-Y5; the F4-exclusion of the chiral witness"),
        "cited_premises": ("that the OBJECT supplies only theta-compatible / SL(2)-routes: "
                           "B353 (the hyperelliptic involution induces exactly theta at the "
                           "geometric point; theta fixes the principal SL2 pointwise), "
                           "B302 (the object's 2T lives in the commensurator SL(2,C) = "
                           "PGL(2,O_-3)), B347/B351/B352 (the principal-SL2 E6 tangent). "
                           "These are banked elsewhere and are NOT recomputed here."),
        "unchanged_residual": ("EXTERNAL/specialist -- whether the arithmetic could force a "
                               "non-SL(2), non-theta-compatible route into E6.  Not reopened by "
                               "the witness: a chiral subgroup of E6 is not an object-supplied one."),
        "wording_fix_owed": ("OI-128 'unreachable by any canonical 2T->E6' -> 'unreachable by any "
                             "theta-compatible / SL(2)-route embedding; a chiral 2T < E6 exists "
                             "(OI-173) but lies in no F4 and on no object supply line'"),
    },
    "method": "exact/symbolic (sympy over Q(sqrt(-3))); no numerics, no scans, no estimators",
    "firewall": "structural only; no SM values; nothing to CLAIMS.md; one-number pin untouched",
}
with open(__file__.replace("compute.py", "results.json"), "w") as fh:
    json.dump(results, fh, indent=1)
with open(__file__.replace("compute.py", "output.txt"), "w") as fh:
    fh.write("\n".join(LOG) + "\n")
