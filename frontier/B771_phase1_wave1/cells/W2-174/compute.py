"""W2-174 / H104 -- is any omega-window assembly (A4 or 2T) realized in E6?
[B771 Phase-1 Wave-2]

SEALED CRITERION (PREREG_WAVE2.md, sealed 486ea7c8):
  realized (explicit class exhibited)                       => RESOLVED-A
  none realized (exhaustive over classified embeddings)     => RESOLVED-B

BACKGROUND.  B356 proved the chirality window at character level: faithful 27-dim
assemblies with (Sym^3 V)^G != 0 and COMPLEX (non-real) character exist ONLY for the
two omega-groups A4 (1028/1089) and 2T (70262/71192) -- the groups with Z/3
abelianization.  H104 asks whether ANY such assembly is genuinely realized in E6 =
Stab(I3), the stabilizer of the nondegenerate Cartan cubic on the 27 -- i.e. an
actual conjugacy class of embeddings, not just a character-level candidate.
Wave-1 OI-173 proposed a center-twisted 2T witness; it is IN SCOPE as a candidate,
and everything about it is RE-COMPUTED here in-cell (never cited).

WHAT THIS CELL COMPUTES (all in-cell):
  (1) 2T = 24 Hurwitz units; classes; eps: 2T -> Z/3 (abelianization); exact
      character table, gated (orthonormality, sum dim^2).
  (2) Explicit matrix models: rho2 (quaternionic 2), rho3 = 1'+2' in SU(3) (2T),
      R = SO(3) rotation rep (factors through A4 = 2T/{+-1}).
  (3) The E6 cubic I3 = det M1 + det M2 + det M3 - tr(M1 M2 M3) on the
      trinification 27; SYMBOLIC invariance of I3 under each witness generator.
  (4) TWO witnesses, one per omega-window group:
        W_2T : g |-> w^{eps(g)} . P(rho3(g), I, I)      (center-twisted, faithful 2T)
        W_A4 : g |-> w^{eps(g)} . P(R(g),    I, I)      (kernel exactly {+-1} -> faithful A4)
      Each is an injective homomorphism into Stab(I3); each 27-restriction has a
      NON-REAL character (9w on an order-3 class) => a chiral / non-sigma-stable
      class; each assembly satisfies B356's window conditions (faithful, complex,
      (Sym^3)^G != 0) -- verified in-cell at character level.
  (5) Nondegeneracy certificate: dim Stab_{gl(27,C)}(I3) = 78 = dim e6, numeric,
      2 seeds, singular-value gap reported (UNSTABLE beats forced).

VERDICT SHAPE: exhibiting either witness settles the sealed disjunction as
RESOLVED-A; the A4 witness makes the realization cover BOTH window groups.

House method: exact/symbolic (sympy) wherever possible; numerics at >= 2 seeds with
conditioning; discriminating fact computed here; Gate 5/5-Q structural language only.
Standalone: pyenv python3, sympy + numpy.  Re-runnable end-to-end.
"""
import itertools
import random
import sympy as sp
import numpy as np

W = sp.Rational(-1, 2) + sp.sqrt(3) / 2 * sp.I      # w = e^{2 pi i/3}

FAILURES = []
def gate(name, cond):
    print(("PASS  " if cond else "FAIL  ") + name)
    if not cond:
        FAILURES.append(name)

# =====================================================================================
# Part A -- 2T = 24 Hurwitz unit quaternions; classes; eps; exact character table
# =====================================================================================
def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
def qinv(a): return (a[0], -a[1], -a[2], -a[3])
def order(g):
    p, one = g, (1, 0, 0, 0)
    for k in range(1, 13):
        if p == one:
            return k
        p = qmul(p, g)
    raise RuntimeError("order > 12 impossible in 2T")

def build_2T():
    h = sp.Rational(1, 2)
    elts = set()
    for pos in range(4):
        for s in (1, -1):
            v = [0, 0, 0, 0]; v[pos] = s; elts.add(tuple(v))
    for s in itertools.product((h, -h), repeat=4):
        elts.add(tuple(s))
    elts = list(elts)
    assert len(elts) == 24
    seen, classes = set(), []
    for g in elts:
        if g in seen:
            continue
        cl = set(qmul(qmul(t, g), qinv(t)) for t in elts)
        classes.append(sorted(cl)); seen |= cl
    classes.sort(key=lambda c: (order(c[0]), c[0][0]))
    return elts, classes

ELTS, CLASSES = build_2T()
REPS = [c[0] for c in CLASSES]
SIZES = [len(c) for c in CLASSES]
ORDERS = [order(r) for r in REPS]
gate("A1: 2T has 24 elements, 7 conjugacy classes, sizes sum to 24",
     len(ELTS) == 24 and len(CLASSES) == 7 and sum(SIZES) == 24)

# eps: 2T -> Z/3 via cosets of Q8 = [2T,2T]
Q8 = set(g for g in ELTS if all(c in (0, 1, -1) for c in g))
def coset(g): return frozenset(qmul(g, q) for q in Q8)
g3 = next(g for g in ELTS if order(g) == 3)
COS = {coset((1, 0, 0, 0)): 0, coset(g3): 1, coset(qmul(g3, g3)): 2}
def eps(g): return COS[coset(g)]

gate("A2: eps is a homomorphism 2T -> Z/3 (all 576 pairs, exact)",
     all((eps(qmul(g, h)) - eps(g) - eps(h)) % 3 == 0 for g in ELTS for h in ELTS))
gate("A3: ker eps = Q8 (contains -1 and every order-4 element)",
     set(g for g in ELTS if eps(g) == 0) == Q8)

chi_1p = lambda g: W ** eps(g)
chi_1pp = lambda g: sp.conjugate(W) ** eps(g)
chi_2 = lambda g: 2 * g[0]
IRREPS = {'1': lambda g: sp.Integer(1), "1'": chi_1p, "1''": chi_1pp,
          '2': chi_2, "2'": lambda g: chi_2(g) * chi_1p(g),
          "2''": lambda g: chi_2(g) * chi_1pp(g), '3': lambda g: 4 * g[0]**2 - 1}

ortho = all(sp.simplify(sum(SIZES[i] * IRREPS[a](REPS[i]) * sp.conjugate(IRREPS[b](REPS[i]))
                            for i in range(7)) / 24) == (1 if a == b else 0)
            for a in IRREPS for b in IRREPS)
gate("A4: 2T character table orthonormal + sum dim^2 = 24 (exact)",
     ortho and sum(int(IRREPS[k](REPS[0]))**2 for k in IRREPS) == 24)

def decompose(chi_vals):
    """chi_vals on the 7 class REPS -> multiplicity dict (exact)."""
    return {name: sp.nsimplify(sp.simplify(sum(SIZES[i] * chi_vals[i]
                                               * sp.conjugate(chi(REPS[i]))
                                               for i in range(7)) / 24))
            for name, chi in IRREPS.items()}

# =====================================================================================
# Part B -- matrix models: rho2, rho3 = 1'+2' (2T in SU(3)); R = SO(3) (A4 model)
# =====================================================================================
def rho2(q):
    a, b, c, d = q
    return sp.Matrix([[a + b*sp.I, c + d*sp.I], [-c + d*sp.I, a - b*sp.I]])

gate("B1: rho2 is a homomorphism (all 576 pairs, exact)",
     all((rho2(qmul(g, h)) - rho2(g)*rho2(h)).applyfunc(sp.expand).is_zero_matrix
         for g in ELTS for h in ELTS))
gate("B2: rho2 faithful",
     all(((rho2(g) - sp.eye(2)).applyfunc(sp.expand).is_zero_matrix) == (g == (1, 0, 0, 0))
         for g in ELTS))

def rho3(g):
    """1' + 2' block form: diag(w^eps, w^eps rho2(g)); det = w^{3 eps} = 1."""
    e = eps(g)
    m = sp.zeros(3, 3)
    m[0, 0] = W**e
    m[1:, 1:] = (W**e) * rho2(g)
    return m.applyfunc(sp.expand)

gate("B3: w^3 = 1 exactly", sp.simplify(W**3 - 1) == 0)
gate("B4: rho3 lands in SU(3) (det 1, unitary), all 24 elements, exact",
     all(sp.simplify(rho3(g).det() - 1) == 0 and
         (rho3(g)*rho3(g).H - sp.eye(3)).applyfunc(sp.simplify).is_zero_matrix
         for g in ELTS))
random.seed(0)
PAIRS40 = [(random.choice(ELTS), random.choice(ELTS)) for _ in range(40)]
gate("B5: rho3 hom (structural from A2+B1+B3; exact spot-check, 40 pairs)",
     all((rho3(qmul(g, h)) - rho3(g)*rho3(h)).applyfunc(sp.simplify).is_zero_matrix
         for g, h in PAIRS40))
gate("B6: char(rho3) = chi_1' + chi_2' on all classes (faithful complex 3 of 2T)",
     all(sp.simplify(rho3(r).trace() - (chi_1p(r) + chi_2(r)*chi_1p(r))) == 0
         for r in REPS))

def rotR(q):
    """SO(3) rotation matrix of a unit quaternion (factors through A4 = 2T/{+-1})."""
    a, b, c, d = q
    return sp.Matrix([
        [a*a + b*b - c*c - d*d, 2*(b*c - a*d),        2*(b*d + a*c)],
        [2*(b*c + a*d),         a*a - b*b + c*c - d*d, 2*(c*d - a*b)],
        [2*(b*d - a*c),         2*(c*d + a*b),         a*a - b*b - c*c + d*d]]).applyfunc(sp.expand)

gate("B7: R lands in SO(3) subset SU(3) (det 1, orthogonal real), all 24, exact",
     all(sp.simplify(rotR(g).det() - 1) == 0 and
         (rotR(g)*rotR(g).T - sp.eye(3)).applyfunc(sp.simplify).is_zero_matrix
         for g in ELTS))
gate("B8: R is a homomorphism (exact spot-check, 40 pairs)",
     all((rotR(qmul(g, h)) - rotR(g)*rotR(h)).applyfunc(sp.simplify).is_zero_matrix
         for g, h in PAIRS40))
gate("B9: ker R = {+-1} exactly (R factors through a FAITHFUL A4)",
     set(g for g in ELTS if (rotR(g) - sp.eye(3)).applyfunc(sp.simplify).is_zero_matrix)
     == {(1, 0, 0, 0), (-1, 0, 0, 0)})
gate("B10: eps factors through A4 (eps(-g) = eps(g) for all g)",
     all(eps((-g[0], -g[1], -g[2], -g[3])) == eps(g) for g in ELTS))

# generators of 2T, verified by closure
GI = (0, 1, 0, 0)                       # order 4, eps = 0
GT = (sp.Rational(1, 2),) * 4           # order 6, eps != 0
def closure(gens):
    S = {(1, 0, 0, 0)}
    frontier = set(gens)
    while frontier:
        S |= frontier
        frontier = {qmul(a, b) for a in S for b in S} - S
    return S
gate("B11: <i, (1+i+j+k)/2> = 2T (closure)", closure({GI, GT}) == set(ELTS))

# =====================================================================================
# Part C -- the 27, the cubic I3, SYMBOLIC invariance under both witnesses
# =====================================================================================
def kron(A, B):
    p, q = B.shape
    return sp.Matrix(A.shape[0]*p, A.shape[1]*q,
                     lambda i, j: A[i//p, j//q] * B[i % p, j % q])

I3M = sp.eye(3)
def P_of(A, B, C):
    """27 = (3,3b,1)+(1,3,3b)+(3b,1,3): M1 -> A M1 B^dag, M2 -> B M2 C^dag,
    M3 -> C M3 A^dag; row-major vec => kron(A, conj(B)) etc."""
    P = sp.zeros(27, 27)
    P[0:9, 0:9] = kron(A, B.conjugate())
    P[9:18, 9:18] = kron(B, C.conjugate())
    P[18:27, 18:27] = kron(C, A.conjugate())
    return P

XS = sp.symbols('x0:27')
def I3_of(v):
    M1 = sp.Matrix(3, 3, v[0:9]); M2 = sp.Matrix(3, 3, v[9:18]); M3 = sp.Matrix(3, 3, v[18:27])
    return sp.expand(M1.det() + M2.det() + M3.det() - (M1*M2*M3).trace())
I3_BASE = I3_of(list(XS))

def invariant_under(P):
    y = [sp.expand(sum(P[i, j]*XS[j] for j in range(27) if P[i, j] != 0))
         for i in range(27)]
    return sp.simplify(sp.expand(I3_of(y) - I3_BASE)) == 0

# the two witnesses (center-twisted single-factor trinification routes)
def W2T(g):  return (W**eps(g) * P_of(rho3(g), I3M, I3M)).applyfunc(sp.expand)
def WA4(g):  return (W**eps(g) * P_of(rotR(g), I3M, I3M)).applyfunc(sp.expand)

gate("C1: I3 invariant under P(rho3(i)) (untwisted, order-4 gen, symbolic)",
     invariant_under(P_of(rho3(GI), I3M, I3M)))
gate("C2: I3 invariant under P(rho3(t)), t=(1+i+j+k)/2 (untwisted, order-6 gen, symbolic)",
     invariant_under(P_of(rho3(GT), I3M, I3M)))
gate("C3: I3 invariant under the central scalar w.Id (w^3 = 1, symbolic)",
     invariant_under(W * sp.eye(27)))
gate("C4: I3 invariant under the TWISTED W2T(t) directly (symbolic)",
     invariant_under(W2T(GT)))
gate("C5: I3 invariant under P(R(i)) (A4 route, order-2 image, symbolic)",
     invariant_under(P_of(rotR(GI), I3M, I3M)))
gate("C6: I3 invariant under the TWISTED WA4(t) directly (symbolic)",
     invariant_under(WA4(GT)))
# C1-C6 + homomorphism (Part D) => both witness images lie in Stab(I3) entirely.

# =====================================================================================
# Part D -- homomorphism + injectivity at 27 dims; characters; window membership
# =====================================================================================
NUM_2T = {g: np.array([[complex(W2T(g)[i, j].evalf(18)) for j in range(27)]
                       for i in range(27)]) for g in ELTS}
NUM_A4 = {g: np.array([[complex(WA4(g)[i, j].evalf(18)) for j in range(27)]
                       for i in range(27)]) for g in ELTS}

gate("D1: W2T homomorphism, all 576 pairs (numeric < 1e-10; structural exact via A2+B5+B3)",
     max(np.abs(NUM_2T[qmul(g, h)] - NUM_2T[g] @ NUM_2T[h]).max()
         for g in ELTS for h in ELTS) < 1e-10)
gate("D2: WA4 homomorphism, all 576 pairs (numeric < 1e-10; structural exact via A2+B8+B3)",
     max(np.abs(NUM_A4[qmul(g, h)] - NUM_A4[g] @ NUM_A4[h]).max()
         for g in ELTS for h in ELTS) < 1e-10)
gate("D3: W2T injective on 2T (a genuine 2T subgroup of Stab(I3))",
     all((np.abs(NUM_2T[g] - np.eye(27)).max() < 1e-10) == (g == (1, 0, 0, 0))
         for g in ELTS))
gate("D4: ker WA4 = {+-1} exactly (a genuine FAITHFUL A4 subgroup of Stab(I3))",
     set(g for g in ELTS if np.abs(NUM_A4[g] - np.eye(27)).max() < 1e-10)
     == {(1, 0, 0, 0), (-1, 0, 0, 0)})

chi_2T = [sp.simplify(W2T(r).trace()) for r in REPS]
chi_A4 = [sp.simplify(WA4(r).trace()) for r in REPS]
dec_2T = decompose(chi_2T)
dec_A4 = decompose(chi_A4)

print("\n  class reps:", [tuple(str(c) for c in r) for r in REPS])
print("  orders:", ORDERS, " eps:", [eps(r) for r in REPS], " sizes:", SIZES)
print("  chi(27)|W2T :", chi_2T)
print("  chi(27)|WA4 :", chi_A4)
print("  27|W2T =", {k: v for k, v in dec_2T.items() if v != 0})
print("  27|WA4 =", {k: v for k, v in dec_A4.items() if v != 0})

gate("D5: 27|W2T = 3.1 + 9.1' + 3.1'' + 3.2 + 3.2'' (dims sum 27; exact)",
     dec_2T == {'1': 3, "1'": 9, "1''": 3, '2': 3, "2'": 0, "2''": 3, '3': 0})
gate("D6: 27|WA4 = 9.1' + 6.3 (A4-type: no spinor irreps; dims sum 27; exact)",
     dec_A4 == {'1': 0, "1'": 9, "1''": 0, '2': 0, "2'": 0, "2''": 0, '3': 6})

# THE DISCRIMINATING FACT: both characters NON-REAL => chiral (non-self-conjugate
# 27-restriction => non-sigma-stable class), 9w at an order-3 class in both.
def nonreal_9w(chi_vals):
    has_nonreal = any(sp.simplify(v - sp.conjugate(v)) != 0 for v in chi_vals)
    has_9w = any((sp.simplify(chi_vals[i] - 9*W) == 0
                  or sp.simplify(chi_vals[i] - 9*sp.conjugate(W)) == 0)
                 for i in range(7) if ORDERS[i] == 3)
    return has_nonreal and has_9w

gate("D7: DISCRIMINATING FACT (2T): chi non-real, = 9w at an order-3 class "
     "=> chiral (non-sigma-stable) 2T class in E6", nonreal_9w(chi_2T))
gate("D8: DISCRIMINATING FACT (A4): chi non-real, = 9w at an order-3 class "
     "=> chiral (non-sigma-stable) A4 class in E6", nonreal_9w(chi_A4))

n1_2T = (sp.simplify(dec_2T["1'"] - dec_2T["2'"]), sp.simplify(dec_2T["1''"] - dec_2T["2''"]))
gate("D9: 2T witness n1 = 9 != n2 = 0 (chirality asymmetry, Out-swap-robust as a set)",
     n1_2T[0] != n1_2T[1] and set(n1_2T) == {sp.Integer(9), sp.Integer(0)})
gate("D10: A4 witness asymmetry m(1') = 9 != m(1'') = 0",
     dec_A4["1'"] == 9 and dec_A4["1''"] == 0)

# B356 window membership, verified at character level IN-CELL:
# faithful (D3/D4) + complex (D7/D8) + (Sym^3 V)^G != 0 and (Sym^3 V*)^G != 0.
def sym3_triv(chifun, dom):
    tot = 0
    for g in dom:
        g2, g3_ = qmul(g, g), qmul(qmul(g, g), g)
        c1, c2, c3 = chifun(g), chifun(g2), chifun(g3_)
        tot += (c1**3 + 3*c1*c2 + 2*c3) / 6
    return sp.nsimplify(sp.simplify(tot / len(dom)))

CH2T = {r: chi_2T[i] for i, r in enumerate(REPS)}
CHA4 = {r: chi_A4[i] for i, r in enumerate(REPS)}
def chifun_from_class(table):
    lookup = {}
    for i, cl in enumerate(CLASSES):
        for g in cl:
            lookup[g] = table[REPS[i]]
    return lambda g: lookup[g]
f2T = chifun_from_class(CH2T); fA4 = chifun_from_class(CHA4)

s3_2T = sym3_triv(f2T, ELTS)
s3d_2T = sym3_triv(lambda g: sp.conjugate(f2T(g)), ELTS)
s3_A4 = sym3_triv(fA4, ELTS)
s3d_A4 = sym3_triv(lambda g: sp.conjugate(fA4(g)), ELTS)
print("  Sym^3 trivial mult: 2T (V, V*) =", (s3_2T, s3d_2T), " A4 (V, V*) =", (s3_A4, s3d_A4))
gate("D11: (Sym^3 V)^G and (Sym^3 V*)^G both nonzero for BOTH witnesses "
     "(the invariant cubic lives at character level; B356 window condition)",
     all(s >= 1 for s in (s3_2T, s3d_2T, s3_A4, s3d_A4)))
# D12: genuine conjunction (can fail: fails iff any constituent condition failed)
_window_2T = (all(not f.startswith(p) for f in FAILURES for p in ("D3", "D7", "D11"))
              and s3d_2T >= 1)
_window_A4 = (all(not f.startswith(p) for f in FAILURES for p in ("D4", "D8", "D11"))
              and s3d_A4 >= 1)
gate("D12: both realized assemblies are omega-window assemblies of B356 "
     "(faithful [D3/D4] + invariant cubic [D11] + complex character [D7/D8])",
     _window_2T and _window_A4)

# =====================================================================================
# Part E -- nondegeneracy: dim Stab_{gl(27,C)}(I3) = 78 = dim e6 (numeric, 2 seeds)
# =====================================================================================
def cof(M):
    return np.linalg.det(M) * np.linalg.inv(M).T

def stab_rows(seed, nsamp=900):
    rng = np.random.default_rng(seed)
    rows = np.empty((nsamp, 729), dtype=complex)
    pts = []
    for s in range(nsamp):
        M = [rng.standard_normal((3, 3)) + 1j*rng.standard_normal((3, 3)) for _ in range(3)]
        G1 = cof(M[0]) - (M[1] @ M[2]).T
        G2 = cof(M[1]) - (M[2] @ M[0]).T
        G3 = cof(M[2]) - (M[0] @ M[1]).T
        grad = np.concatenate([G1.ravel(), G2.ravel(), G3.ravel()])
        x = np.concatenate([M[0].ravel(), M[1].ravel(), M[2].ravel()])
        rows[s] = np.outer(grad, x).ravel()
        pts.append(x)
    return rows, pts

def I3_num(x):
    M1, M2, M3 = x[:9].reshape(3, 3), x[9:18].reshape(3, 3), x[18:].reshape(3, 3)
    return (np.linalg.det(M1) + np.linalg.det(M2) + np.linalg.det(M3)
            - np.trace(M1 @ M2 @ M3))

for seed in (0, 1):
    rows, pts = stab_rows(seed)
    sv = np.linalg.svd(rows, compute_uv=False)
    rank = int((sv > sv[0] * 1e-9).sum())
    nullity = 729 - rank
    gap = sv[rank - 1] / sv[rank] if rank < len(sv) else np.inf
    print(f"  [seed {seed}] Stab(I3) nullity = {nullity} (expect 78 = dim e6); "
          f"sv[{rank-1}] = {sv[rank-1]:.3e}, sv[{rank}] = {sv[rank]:.3e}, "
          f"gap ratio = {gap:.3e}")
    gate(f"E1(seed {seed}): dim Stab(I3) = 78 -- I3 is the NONDEGENERATE E6 cubic "
         f"(well-conditioned: gap > 1e6)", nullity == 78 and gap > 1e6)
    # numeric invariance of I3 under both witnesses at random points
    ok_2T = all(abs(I3_num(NUM_2T[g] @ x) - I3_num(x)) < 1e-9 * max(1.0, abs(I3_num(x)))
                for g in (GI, GT, qmul(GT, GI)) for x in pts[:4])
    ok_A4 = all(abs(I3_num(NUM_A4[g] @ x) - I3_num(x)) < 1e-9 * max(1.0, abs(I3_num(x)))
                for g in (GI, GT, qmul(GT, GI)) for x in pts[:4])
    gate(f"E2(seed {seed}): I3 numerically invariant under both witnesses at random points",
         ok_2T and ok_A4)

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
VERDICT: RESOLVED-A -- omega-window assemblies are REALIZED in E6, for BOTH window
groups, by explicit exhibited classes:

  2T witness:  g |-> w^{eps(g)} . P(rho3(g), I, I)   (center-twisted trinification)
     27|_2T = 3.1 + 9.1' + 3.1'' + 3.2 + 3.2''  (up to the omega labeling),
     character 9w at an order-3 class (NON-REAL), n1 = 9 != n2 = 0.
     [Independently confirms wave-1 OI-173's candidate end-to-end.]

  A4 witness:  g |-> w^{eps(g)} . P(R(g), I, I)      (kernel {+-1}: faithful A4)
     27|_A4 = 9.1' + 6.3, character 9w at an order-3 class (NON-REAL),
     m(1') = 9 != m(1'') = 0.   [NEW in this cell: the OTHER window group is
     realized by the same center-twist mechanism.]

  Both witnesses: injective homomorphisms into Stab(I3) (symbolic invariance on
  generators + homomorphism property), with I3 certified NONDEGENERATE
  (dim Stab = 78 = dim e6, two seeds, gap > 1e6).  Both assemblies satisfy B356's
  window conditions in-cell (faithful, complex, (Sym^3)^G != 0).

  MECHANISM (one line): Z/3 abelianization of the group composed with the mu_3
  center of E6 = the Eisenstein omega twist; exactly the groups B356's window
  permits (A4, 2T) are exactly the groups where the twist is available.

  Firewall: structural statement only (which embeddings exist), no SM values,
  nothing to CLAIMS.""")
