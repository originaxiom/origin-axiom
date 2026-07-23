"""OI-173 / H103 -- is Level 3 unreachable for 2T (clean theorem)?  [B771 Phase-1 Wave-1, cell 9]

SEALED CRITERION: every 2T class in E6 sigma-stable (theorem: Level 3 unreachable) => RESOLVED-A
                  a non-stable class found                                         => RESOLVED-B.

RESULT: **RESOLVED-B** -- an explicit non-sigma-stable (chiral) 2T subgroup of E6 exists.

THE WITNESS (the center-twisted trinification).  2T has abelianization Z/3 (2T/Q8), giving a
homomorphism eps: 2T -> Z/3.  The center of E6 = Stab(cubic) is mu_3 = {I, wI, w^2 I} (a scalar
preserves a cubic form iff w^3 = 1).  Twist B329's balanced trinification rho_b (2T c SU(3)_A c E6,
27|_2T = 9.1 + 3.1' + 3.1'' + 3.2' + 3.2'', real character) by the center:

        rho'(g) = w^{eps(g)} . rho_b(g)     (w = e^{2 pi i/3})

Then rho' is an injective homomorphism 2T -> E6 (verified below), equal to the trinification-route
embedding with factor reps (3 (x) 1'', 3.1', 3.1) = an UNBALANCED multi-factor route -- outside
B356's identity-3 cases (single-factor / diagonal), which is exactly the gap.  Its 27-restriction is
(27|rho_b) (x) 1' = 3.1 + 9.1' + 3.1'' + 3.2 + 3.2'', with character 9w at an order-3 class --
NON-REAL, hence 27|_H not self-conjugate, hence a non-sigma-stable class; n1 = 9 != n2 = 0.
Level 3 IS reachable; the hoped clean theorem is FALSE.

WHY B329 missed it: the principal embedding is twist-protected (its character VANISHES on the
eps != 0 classes, so (27|principal) (x) 1' ~ 27|principal); the balanced trinification is not
(chi_b = 9 resp. 3 on the order-3/order-6 classes).  The chirality window is exactly the Eisenstein
omega twist -- confirming B356's window mechanism and answering H104's realization question: the
omega-window assembly (m_1,m_1',m_1''; m_2,m_2',m_2''; m_3) = (3,9,3; 3,0,3; 0) IS realized in E6.

Honest scope: RESOLVED-B needs only the witness (the sealed disjunction).  A FULL conjugacy
classification of 2T subgroups of E6 is not performed (not needed for the two-outcome test).
Subgroup-vs-embedding nuance: sigma(H') may still be E6-conjugate to H' as an abstract SUBGROUP via
the compensating outer automorphism of 2T (chi'.alpha = conj(chi'), verified below) -- but the
sealed test is self-conjugacy of the 27-restriction, which fails INTRINSICALLY (non-real character
values on the actual elements of H'), and {n1,n2} = {9,0} != {n,n} under every identification.

Everything exact/symbolic (sympy) except the nondegeneracy certificate for the cubic (the stabilizer
Lie algebra of I3 in gl(27,C) has complex dimension 78 = dim e6), which is numeric at 2 seeds with
the singular-value gap reported.  Firewalled: structural only, no SM values, nothing to CLAIMS.
Standalone: pyenv python3, sympy + numpy.
"""
import itertools
import sympy as sp
import numpy as np

W = sp.Rational(-1, 2) + sp.sqrt(3) / 2 * sp.I          # w = e^{2 pi i / 3}

FAILURES = []
def gate(name, cond):
    print(("PASS  " if cond else "FAIL  ") + name)
    if not cond:
        FAILURES.append(name)

# =====================================================================================
# Part A -- 2T = 24 Hurwitz unit quaternions; classes; character table  (B329 machinery)
# =====================================================================================
def _qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
def _qinv(a): return (a[0], -a[1], -a[2], -a[3])
def _order(g):
    p, one = g, (1, 0, 0, 0)
    for k in range(1, 13):
        if p == one: return k
        p = _qmul(p, g)

def two_T():
    h = sp.Rational(1, 2)
    elts = set()
    for p in itertools.permutations(range(4)):
        for s in (1, -1):
            v = [0, 0, 0, 0]; v[p[0]] = s; elts.add(tuple(v))
    for s in itertools.product((h, -h), repeat=4):
        elts.add(tuple(s))
    elts = list(elts); assert len(elts) == 24
    seen, classes = set(), []
    for g in elts:
        if g in seen: continue
        cl = set(_qmul(_qmul(t, g), _qinv(t)) for t in elts)
        classes.append(sorted(cl)); seen |= cl
    classes.sort(key=lambda c: (_order(c[0]), c[0][0]))
    return elts, classes

ELTS, CLASSES = two_T()
REPS  = [c[0] for c in CLASSES]
SIZES = [len(c) for c in CLASSES]
gate("A1: 2T has 24 elements, 7 classes, sizes sum 24",
     len(ELTS) == 24 and len(CLASSES) == 7 and sum(SIZES) == 24)

# eps : 2T -> Z/3  (the abelianization 2T/Q8), via cosets of Q8
Q8 = set(g for g in ELTS if all(c in (0, 1, -1) for c in g))
def _coset(g): return frozenset(_qmul(g, q) for q in Q8)
g0 = next(g for g in ELTS if _order(g) == 3)
_COS = {_coset((1, 0, 0, 0)): 0}
gp = g0
for k in (1, 2):
    _COS[_coset(gp)] = k; gp = _qmul(gp, g0)
def eps(g): return _COS[_coset(g)]

gate("A2: eps is a homomorphism 2T -> Z/3 (all 576 pairs)",
     all((eps(_qmul(g, h)) - eps(g) - eps(h)) % 3 == 0 for g in ELTS for h in ELTS))
gate("A3: ker eps = Q8 (so -1, order-4 elts have eps=0; order-3/6 elts have eps!=0)",
     set(g for g in ELTS if eps(g) == 0) == Q8)

# character table (7 irreps: 1, 1', 1'', 2, 2', 2'', 3) -- B329's construction
chi_1p  = lambda g: W ** eps(g)
chi_1pp = lambda g: sp.conjugate(W) ** eps(g)
chi_2   = lambda g: 2 * g[0]
IRREPS = {'1': lambda g: sp.Integer(1), "1'": chi_1p, "1''": chi_1pp,
          '2': chi_2, "2'": lambda g: chi_2(g) * chi_1p(g),
          "2''": lambda g: chi_2(g) * chi_1pp(g), '3': lambda g: 4 * g[0]**2 - 1}

ortho = all(sp.simplify(sum(SIZES[i] * IRREPS[a](REPS[i]) * sp.conjugate(IRREPS[b](REPS[i]))
                            for i in range(7)) / 24) == (1 if a == b else 0)
            for a in IRREPS for b in IRREPS)
gate("A4: character table orthonormal, sum dim^2 = 24",
     ortho and sum(int(IRREPS[k](REPS[0]))**2 for k in IRREPS) == 24)

def decompose(chi_vals):
    """chi_vals = values of a character on the 7 class REPS -> dict of multiplicities."""
    return {name: sp.nsimplify(sp.simplify(sum(SIZES[i] * chi_vals[i] * sp.conjugate(chi(REPS[i]))
                                               for i in range(7)) / 24))
            for name, chi in IRREPS.items()}

def n1n2(dec):
    return sp.simplify(dec["1'"] - dec["2'"]), sp.simplify(dec["1''"] - dec["2''"])

# =====================================================================================
# Part B -- explicit matrix reps: rho2 (quaternionic 2), rho3 = 1' + 2'  in SU(3)
# =====================================================================================
def rho2(q):
    a, b, c, d = q
    return sp.Matrix([[a + b*sp.I, c + d*sp.I], [-c + d*sp.I, a - b*sp.I]])

gate("B1: rho2 is a homomorphism (all 576 pairs, exact)",
     all((rho2(_qmul(g, h)) - rho2(g)*rho2(h)).applyfunc(sp.expand).is_zero_matrix
         for g in ELTS for h in ELTS))
gate("B2: rho2 faithful (rho2(g)=I only for g=1)",
     all((rho2(g) - sp.eye(2)).applyfunc(sp.expand).is_zero_matrix == (g == (1, 0, 0, 0))
         for g in ELTS))
gate("B3: w^3 = 1 exactly (the mu_3 scalar preserves any cubic form)",
     sp.simplify(W**3 - 1) == 0)

def rho3(g):
    """3 = 1' + 2' : block diag(w^eps, w^eps * rho2).  det = w^{3 eps} = 1."""
    e = eps(g)
    m = sp.zeros(3, 3)
    m[0, 0] = W**e
    m[1:, 1:] = (W**e) * rho2(g)
    return m.applyfunc(sp.expand)

gate("B4: rho3 lands in SU(3): det=1 and unitary, all 24 elements (exact)",
     all(sp.simplify(rho3(g).det() - 1) == 0 and
         (rho3(g) * rho3(g).H - sp.eye(3)).applyfunc(sp.simplify).is_zero_matrix
         for g in ELTS))
# rho3 hom is structural: diag of (w^eps, w^eps rho2) with eps and rho2 homs and w^3=1
# (gates A2+B1+B3); spot-verify exactly on 40 pairs anyway:
import random as _rnd
_rnd.seed(0)
_pairs = [(_rnd.choice(ELTS), _rnd.choice(ELTS)) for _ in range(40)]
gate("B5: rho3 hom (structural from A2+B1+B3; exact spot-check on 40 pairs)",
     all((rho3(_qmul(g, h)) - rho3(g)*rho3(h)).applyfunc(sp.simplify).is_zero_matrix
         for g, h in _pairs))
gate("B6: char(rho3) = chi_1' + chi_2' on all 7 classes (the B329 embedding)",
     all(sp.simplify(rho3(r).trace() - (chi_1p(r) + chi_2(r)*chi_1p(r))) == 0 for r in REPS))

# generators of 2T (for the symbolic invariance checks): closure check
GI = (0, 1, 0, 0)                                  # order 4, eps = 0
GT = (sp.Rational(1, 2),) * 4                      # order 6, eps != 0
def closure(gens):
    S = {(1, 0, 0, 0)}
    frontier = set(gens)
    while frontier:
        S |= frontier
        frontier = {_qmul(a, b) for a in S for b in S} - S
    return S
gate("B7: <i, (1+i+j+k)/2> = 2T (generators verified by closure)",
     closure({GI, GT}) == set(ELTS))

# =====================================================================================
# Part C -- the 27 (trinification basis), the E6 cubic I3, symbolic invariance
# =====================================================================================
def kron(A, B):
    p, q = B.shape
    return sp.Matrix(A.shape[0]*p, A.shape[1]*q,
                     lambda i, j: A[i//p, j//q] * B[i % p, j % q])

I3M = sp.eye(3)
def P_of(A, B, C):
    """27 = (3,3b,1)+(1,3,3b)+(3b,1,3): M1 -> A M1 B^dag, M2 -> B M2 C^dag, M3 -> C M3 A^dag.
    Row-major vec => blocks kron(A, conj(B)), kron(B, conj(C)), kron(C, conj(A))."""
    P = sp.zeros(27, 27)
    P[0:9,   0:9]   = kron(A, B.conjugate())
    P[9:18,  9:18]  = kron(B, C.conjugate())
    P[18:27, 18:27] = kron(C, A.conjugate())
    return P

XS = sp.symbols('x0:27')
def I3_of(v):
    M1 = sp.Matrix(3, 3, v[0:9]); M2 = sp.Matrix(3, 3, v[9:18]); M3 = sp.Matrix(3, 3, v[18:27])
    return sp.expand(M1.det() + M2.det() + M3.det() - (M1*M2*M3).trace())
I3_BASE = I3_of(list(XS))

def invariant_under(P):
    y = [sp.expand(sum(P[i, j]*XS[j] for j in range(27) if P[i, j] != 0)) for i in range(27)]
    return sp.simplify(sp.expand(I3_of(y) - I3_BASE)) == 0

def Pb(g):  return P_of(rho3(g), I3M, I3M)                     # balanced trinification (B329 (b))
def Pt(g):  return (W**eps(g) * Pb(g)).applyfunc(sp.expand)    # THE WITNESS: center-twisted

gate("C1: I3 invariant under Pb(i) (order-4 generator, symbolic X)", invariant_under(Pb(GI)))
gate("C2: I3 invariant under Pb(t), t=(1+i+j+k)/2 (order-6 generator, symbolic X)",
     invariant_under(Pb(GT)))
gate("C3: I3 invariant under the central scalar w.Id (cubic: w^3=1, symbolic X)",
     invariant_under(W * sp.eye(27)))
gate("C4: I3 invariant under the twisted Pt(t) directly (symbolic X)", invariant_under(Pt(GT)))
# C1-C4 + hom (D-gates below) => rho' = Pt lands in Stab(I3) = E6 for ALL of 2T.

# the twist is itself a trinification-route triple: (3 (x) 1'', 3.1', 3.1) in SU(3)^3
def Atw(g): return (W**(2*eps(g)) * rho3(g)).applyfunc(sp.expand)
def Btw(g): return (W**eps(g)) * I3M
gate("C5: Pt(g) = P_of(3(x)1'', 3.1', 3.1) -- an unbalanced multi-factor trinification route "
     "(exact, on both generators)",
     all((Pt(g) - P_of(Atw(g), Btw(g), I3M)).applyfunc(sp.simplify).is_zero_matrix
         for g in (GI, GT)))
gate("C6: the twisted factors have det 1 (genuine SU(3)^3 triple), all 24 elements",
     all(sp.simplify(Atw(g).det() - 1) == 0 and sp.simplify(Btw(g).det() - 1) == 0 for g in ELTS))

# =====================================================================================
# Part D -- the twisted embedding: hom + injective; characters; decomposition; n1 != n2
# =====================================================================================
NUM = {g: np.array([[complex((Pt(g))[i, j].evalf(18)) for j in range(27)]
                    for i in range(27)]) for g in ELTS}
gate("D1: rho' = Pt is a homomorphism (all 576 pairs, numeric 1e-10; structural exact via A2+B5+B3)",
     max(np.abs(NUM[_qmul(g, h)] - NUM[g] @ NUM[h]).max() for g in ELTS for h in ELTS) < 1e-10)
gate("D2: rho' injective (Pt(g)=I only for g=1) -- a genuine 2T subgroup H' of E6",
     all((np.abs(NUM[g] - np.eye(27)).max() < 1e-10) == (g == (1, 0, 0, 0)) for g in ELTS))

chi_bal = [sp.simplify(Pb(r).trace()) for r in REPS]
chi_tw  = [sp.simplify(Pt(r).trace()) for r in REPS]
dec_bal = decompose(chi_bal)
dec_tw  = decompose(chi_tw)
nb = n1n2(dec_bal); nt = n1n2(dec_tw)

print("\n  class reps (as quaternions):", [tuple(str(c) for c in r) for r in REPS])
print("  orders:", [_order(r) for r in REPS], " eps:", [eps(r) for r in REPS],
      " sizes:", SIZES)
print("  chi_27 balanced :", chi_bal)
print("  chi_27 TWISTED  :", chi_tw)
print("  balanced 27|_2T =", {k: v for k, v in dec_bal.items() if v != 0},
      "  (n1,n2) =", nb)
print("  TWISTED  27|_2T =", {k: v for k, v in dec_tw.items() if v != 0},
      "  (n1,n2) =", nt)

gate("D3: balanced baseline reproduces B329(b): 9.1+3.1'+3.1''+3.2'+3.2'', n1=n2=0",
     dec_bal == {'1': 9, "1'": 3, "1''": 3, '2': 0, "2'": 3, "2''": 3, '3': 0}
     and nb == (0, 0))
gate("D4: twisted multiplicities are nonneg integers summing to 27 (dim check)",
     all(m.is_integer and m >= 0 for m in dec_tw.values())
     and sp.simplify(dec_tw['1'] + dec_tw["1'"] + dec_tw["1''"]
                     + 2*(dec_tw['2'] + dec_tw["2'"] + dec_tw["2''"]) + 3*dec_tw['3'] - 27) == 0)
gate("D5: twisted 27|_2T = (27|balanced) (x) 1'  (the central-character twist identity, exact)",
     all(sp.simplify(chi_tw[i] - chi_bal[i]*chi_1p(REPS[i])) == 0 for i in range(7)))
gate("D6: THE DISCRIMINATING FACT -- twisted character NON-REAL (9w at an order-3 class) "
     "=> 27|_H' not self-conjugate => a non-sigma-stable 2T class in E6",
     any(sp.simplify(v - sp.conjugate(v)) != 0 for v in chi_tw)
     and any(sp.simplify(chi_tw[i] - 9*W) == 0 or sp.simplify(chi_tw[i] - 9*sp.conjugate(W)) == 0
             for i in range(7) if _order(REPS[i]) == 3))
gate("D7: n1 != n2 for the witness, {n1,n2} = {9,0} (Level 3 reachable; Out(2T)-swap-robust)",
     nt[0] != nt[1] and set(nt) == {sp.Integer(9), sp.Integer(0)})

# the multiplicity pattern (either chirality labeling, depending on the eps orientation)
pat = sorted((dec_tw['1'], dec_tw["1'"], dec_tw["1''"]))
gate("D8: witness assembly = (3,9,3; 3,0,3; 0) up to the omega labeling -- an omega-window "
     "assembly of B356, now REALIZED in E6 (answers H104's realization question: YES)",
     pat == [3, 3, 9] and sorted((dec_tw['2'], dec_tw["2'"], dec_tw["2''"])) == [0, 3, 3]
     and dec_tw['3'] == 0)

# invariant cubic seen at character level: mult of trivial in Sym^3 of V' and of its dual
def sym3_triv(chifun):
    tot = 0
    for g in ELTS:
        g2, g3 = _qmul(g, g), _qmul(_qmul(g, g), g)
        c1, c2, c3 = chifun(g), chifun(g2), chifun(g3)
        tot += (c1**3 + 3*c1*c2 + 2*c3) / 6
    return sp.nsimplify(sp.simplify(tot / 24))
chi_tw_fun = lambda g: (W**eps(g)) * (9 + 3*(chi_1p(g) + chi_1pp(g))
                                      + 3*chi_2(g)*(chi_1p(g) + chi_1pp(g)))
gate("D9: chi_tw elementwise formula consistent with matrix traces (7 classes)",
     all(sp.simplify(chi_tw_fun(REPS[i]) - chi_tw[i]) == 0 for i in range(7)))
s3, s3d = sym3_triv(chi_tw_fun), sym3_triv(lambda g: sp.conjugate(chi_tw_fun(g)))
print("  mult of trivial in Sym^3(V') =", s3, " | in Sym^3(V'^*) =", s3d,
      " (>=1: the invariant cubic I3 lives here)")
gate("D10: (Sym^3 V'^*)^{2T} != 0 (character level confirms the invariant cubic)",
     s3d >= 1 and s3 >= 1)

# the twist-protection of the principal embedding (why B329's (a) cannot be twisted chiral)
chi_pr = [sp.simplify(sum(sp.chebyshevu(2*j, REPS[i][0]) for j in (8, 4, 0))) for i in range(7)]
gate("D11: principal is twist-PROTECTED: chi_principal = 0 on every eps!=0 class, so "
     "(27|principal)(x)1' has the same (real) character",
     all(sp.simplify(chi_pr[i]) == 0 for i in range(7) if eps(REPS[i]) != 0)
     and all(sp.simplify(chi_pr[i]*chi_1p(REPS[i]) - chi_pr[i]) == 0 for i in range(7)))

# =====================================================================================
# Part E -- the subgroup-vs-embedding nuance (Out(2T) compensation), stated honestly
# =====================================================================================
u = (sp.sqrt(2)/2, sp.sqrt(2)/2, 0, 0)          # in 2O, normalizes 2T; the outer C2
def alpha(g):
    r = _qmul(_qmul(u, g), _qinv(u))
    return tuple(sp.nsimplify(sp.simplify(c)) for c in r)
img = set(alpha(g) for g in ELTS)
gate("E1: alpha = conj by (1+i)/sqrt2 maps 2T to 2T (the outer automorphism)",
     img == set(ELTS))
gate("E2: alpha swaps the eps=1 and eps=2 sectors (swaps the order-3 classes)",
     all((eps(alpha(g)) - 2*eps(g)) % 3 == 0 for g in ELTS))
gate("E3: chi_tw o alpha = conj(chi_tw) elementwise (so sigma(H') MAY be subgroup-conjugate "
     "to H' via Out-compensation; the sealed self-conjugacy test still fails intrinsically, "
     "and {n1,n2}={9,0} is swap-invariant)",
     all(sp.simplify(chi_tw_fun(alpha(g)) - sp.conjugate(chi_tw_fun(g))) == 0 for g in ELTS))

# =====================================================================================
# Part F -- nondegeneracy certificate: dim Stab_{gl(27,C)}(I3) = 78 = dim e6  (2 seeds)
# =====================================================================================
def cof(M):  # cofactor matrix: d(det)/dM_ij
    return np.linalg.det(M) * np.linalg.inv(M).T

def stab_rows(seed, nsamp=900):
    rng = np.random.default_rng(seed)
    rows = np.empty((nsamp, 729), dtype=complex)
    Xs = []
    for s in range(nsamp):
        M = [rng.standard_normal((3, 3)) + 1j*rng.standard_normal((3, 3)) for _ in range(3)]
        G1 = cof(M[0]) - (M[1] @ M[2]).T
        G2 = cof(M[1]) - (M[2] @ M[0]).T
        G3 = cof(M[2]) - (M[0] @ M[1]).T
        grad = np.concatenate([G1.ravel(), G2.ravel(), G3.ravel()])
        x = np.concatenate([M[0].ravel(), M[1].ravel(), M[2].ravel()])
        rows[s] = np.outer(grad, x).ravel()
        Xs.append((M, x))
    return rows, Xs

def I3_num(x):
    M1, M2, M3 = x[:9].reshape(3, 3), x[9:18].reshape(3, 3), x[18:].reshape(3, 3)
    return (np.linalg.det(M1) + np.linalg.det(M2) + np.linalg.det(M3)
            - np.trace(M1 @ M2 @ M3))

for seed in (0, 1):
    rows, Xs = stab_rows(seed)
    sv = np.linalg.svd(rows, compute_uv=False)
    rank = int((sv > sv[0] * 1e-9).sum())
    nullity = 729 - rank
    gap = sv[rank - 1] / sv[rank] if rank < len(sv) else np.inf
    print(f"  [seed {seed}] stabilizer nullity = {nullity} (expect 78 = dim e6);"
          f" sv[{rank-1}]={sv[rank-1]:.3e}, sv[{rank}]={sv[rank]:.3e}, gap ratio = {gap:.3e}")
    gate(f"F1(seed {seed}): dim Stab(I3) = 78 -- I3 is the nondegenerate E6 cubic, "
         f"Stab(I3) = E6 (well-conditioned: gap > 1e6)", nullity == 78 and gap > 1e6)
    # sanity: the sl3^3 (24-dim) directions annihilate the system
    rng2 = np.random.default_rng(100 + seed)
    ok_alg = True
    for _ in range(3):
        abc = []
        for _k in range(3):
            m = rng2.standard_normal((3, 3)) + 1j*rng2.standard_normal((3, 3))
            abc.append(m - np.trace(m)/3 * np.eye(3))
        a, b, c = abc
        I3n = np.eye(3)
        T = np.zeros((27, 27), dtype=complex)
        T[0:9, 0:9]     = np.kron(a, I3n) - np.kron(I3n, b.T)
        T[9:18, 9:18]   = np.kron(b, I3n) - np.kron(I3n, c.T)
        T[18:27, 18:27] = np.kron(c, I3n) - np.kron(I3n, a.T)
        ok_alg &= np.abs(rows @ T.ravel()).max() < 1e-8 * np.abs(rows).max()
    gate(f"F2(seed {seed}): sl3^3 trinification directions lie in the computed stabilizer "
         f"(sanity of the linear system)", bool(ok_alg))
    # numeric invariance of I3 under the exact witness matrices at random points
    ok_inv = True
    for g in (GI, GT, _qmul(GT, GI)):
        for (Mtriple, x) in Xs[:4]:
            ok_inv &= abs(I3_num(NUM[g] @ x) - I3_num(x)) < 1e-9 * max(1.0, abs(I3_num(x)))
    gate(f"F3(seed {seed}): I3 numerically invariant under the witness rho'(g) at random points",
         bool(ok_inv))

# =====================================================================================
# Verdict
# =====================================================================================
print("\n" + "=" * 90)
if FAILURES:
    print("GATES FAILED:", FAILURES)
    print("VERDICT: UNRESOLVED (gate failure -- see above)")
else:
    print("ALL GATES PASS.")
    print("""
VERDICT: RESOLVED-B -- a non-sigma-stable 2T class in E6 EXISTS (explicit witness).
  H' = rho'(2T), rho'(g) = w^{eps(g)} rho_b(g)  (center-twisted balanced trinification;
  equivalently the unbalanced trinification route with factor reps (3 (x) 1'', 3.1', 3.1)).
  27|_H' = 3.1 + 9.1' + 3.1'' + 3.2 + 3.2''  (up to the omega labeling), character 9w on an
  order-3 class (NON-REAL => not self-conjugate), n1 = 9 != n2 = 0.  Level 3 IS reachable;
  the hoped clean theorem 'the hierarchy is Level 4 by theorem' is FALSE.
  Mechanism: the Z/3 abelianization of 2T composed with the mu_3 center of E6 (the Eisenstein
  omega window of B356, now REALIZED); the principal embedding alone is twist-protected by the
  vanishing of its character on the eps != 0 classes.
  Unchanged: whether the ARITHMETIC (Q(sqrt-3) -> 2T) forces THIS embedding rather than a
  canonical one remains the external/specialist question (B329's residual, narrowed).""")
