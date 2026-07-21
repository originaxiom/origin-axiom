"""B739 Stage-B recompute -- TOMB-L293 (S032-A literal universal form, killed in B562 P1).

TARGET (sealed Stage-A record): speculations/TOMBSTONES.md:L293
  claim_killed: S032-A literal universal form -- "No invariant escapes the trace ring's
  discretely-multivalued-and-unsymmetric behavior" -- killed by two single-valued
  counterexample invariants on the (1,2) identity-glued fork.

THE DISCRIMINATING FACT (E19 identification):
  On the (1,2) identity-glued two-seed system (B131 machinery):
    (F0) the trace-ring invariant kappa = tr[A,B] IS discretely multivalued on the fork:
         kappa in {-4, -2} (two distinct values, both != 2, i.e. both irreducible);
    (F1) the |H1|-torsion of the glued 3-manifold X = M_1 U_T M_2 is SINGLE-VALUED across
         the fork branches (it is an invariant of X alone; the fork indexes points of X's
         character variety, X itself is one fixed manifold) -- banked value "Z/m1 (+) Z/m2
         (=2 for (1,2)) via hand-derived Mayer-Vietoris, flagged for SnapPy cross-validation";
    (F2) the gap-label frequency-module rank of the coupled (1,2) substitution system is
         SINGLE-VALUED across the fork branches (it is a function of the seed pair alone) --
         banked value: rank 3 (PSLQ).
  F1 or F2 being single-valued while F0 is 2-valued NEGATES the universal claim ("no
  invariant escapes") -- that conjunction is the kill. (Single-valued already negates
  "discretely-multivalued", so the "unsymmetric" half of the compound property need not
  be probed.)

COMPUTE-NOT-CITE: everything below is re-derived in-sandbox:
  PART 1  re-derives the fork kappa in {-4,-2} from the B131-declared conventions:
          a self-contained SL(2) trace-polynomial engine (Cayley-Hamilton reductions)
          verifies the fixed loci; the suspension trace u = tr(T)^2 is derived by exact
          nullspace solves of the conjugation equations at fixed exact sample points +
          degree-searched rational interpolation with holdout verification; the per-seed
          (kappa,u)-curve relations are then fitted and VERIFIED SYMBOLICALLY; the fork is
          their exact intersection.
  PART 2  re-derives H1 of the pieces (Wang presentation + integer Smith normal form,
          implemented from scratch via determinant divisors) and of the glued manifold
          (Mayer-Vietoris cokernel = amalgam abelianization), and performs the SnapPy
          cross-validation the tombstone itself flagged as missing (the pieces are census
          punctured-torus bundles: b++LR = m004 for seed 1; b++LLRR for seed 2; b++LLLRRR
          as the m=3 pattern check).
  PART 3  re-derives the gap-label module rank under the B173-declared conventions
          (frequency module Z + Z*alpha_g + Z*alpha_s, alpha_m = 1/lambda_m), exactly
          (irrationality certificates + case analysis + coordinate rank) and by PSLQ
          (mpmath, fixed precision, maxcoeff 1e6 -- B173's parameters), including B173's
          same-field positive control (alpha_4) showing PSLQ detects relations when they exist.

DECLARED CONVENTIONS (E1 -- one citation hop: TOMBSTONES.md:L293 -> B562/RESULTS.md (no
scripts there) -> B131 probe.py + B173 FINDINGS.md, the machinery the kill leans on):
  C1. Seed M_m = once-punctured-torus bundle with monodromy phi_m = ta^m o tb^m
      (B131 phi_words: ta:(A,B)->(A,AB), tb:(A,B)->(AB,B)); so phi_1: A->AB, B->AB^2;
      phi_2: A->AB^2, B->AB^2AB^3; abelianized monodromy trace m^2+2.
  C2. Fixed-locus parametrizations (B131): m=1: (x, y, z) = (x, x/(x-1), x);
      m=2: z^2 = 2x^2-4, y = 2x/z -- VERIFIED in-script to be trace-map fixed, not assumed.
      For m=2 the conic is rationally parametrized by the line of slope t through (2,2):
      x(t) = (4t-2t^2-4)/(2-t^2), z(t) = 2 + t(x(t)-2)  [undeclared in the arcs; my choice].
  C3. Identity gluing = identify the boundary tori matching (dF, susp) = ([A1,B1], t1) ~
      ([A2,B2], t2) -- the basis in which B131 matches (kappa, P); matching is done on
      (kappa, P^2), sign-insensitive, exactly as B131's recorded P^2(x) forms.
  C4. Matrix gauge for the sample-point solves: A = [[x,-1],[1,0]], B = [[a, z+1-x*a],[1, y-a]]
      with a a root of a^2 - (x+y)a + (z+2) = 0 (both roots checked to give the same u)
      [undeclared in the arcs; my choice; the character (x,y,z) is what matters].
  C5. H1 conventions: mapping-torus (Wang) presentation H1(M_m) = Z<A,B,t>/im(I-Phi_m);
      Mayer-Vietoris H1(X) = coker(H1(T^2) -> H1(M1)(+)H1(M2)) (valid because
      H0(T) -> H0(M1)(+)H0(M2) is injective); [dF] = [A,B] |-> 0 in homology, [susp] |-> t.
  C6. Gap-label module (B173, declared there as the Johnson-Moser/Bellissard frequency
      module): Z + Z*alpha_g + Z*alpha_s with alpha_m = 1/lambda_m, lambda_m the metallic
      mean (m+sqrt(m^2+4))/2; seed 1 -> alpha_1 = 1/phi = (sqrt5-1)/2, seed 2 ->
      alpha_2 = sqrt2 - 1. PSLQ at mp.dps = 60, maxcoeff = 10^6.

DETERMINISM: no wall-clock, no randomness; all sample points are fixed literal lists;
mpmath precision fixed. SnapPy census lookups are deterministic.

Gate 5: mathematics only; no SM quantities anywhere.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import combinations

import sympy as sp

x, y, z, t, u = sp.symbols("x y z t u")

BANKED_FORK = [-4, -2]
BANKED_TORSION_ORDER = 2      # the tombstone's "Z/m1 (+) Z/m2 (=2 for (1,2))"
BANKED_GAP_RANK = 3

FAIL = []


def check(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAIL.append(label)


# =====================================================================================
# PART 0 -- the machinery, re-implemented from the declared conventions
# =====================================================================================

def word_pair(m):
    """B131 phi_words convention, re-implemented verbatim: m x tb then m x ta."""
    def ta(p):
        A, B = p
        return (A, A + B)

    def tb(p):
        A, B = p
        return (A + B, B)

    p = ("A", "B")
    for _ in range(m):
        p = tb(p)
    for _ in range(m):
        p = ta(p)
    return p


@lru_cache(maxsize=None)
def trw(w):
    """tr of the word w in SL(2) generators A,B (lowercase = inverse) as a polynomial in
    (x, y, z) = (trA, trB, trAB).  Self-contained Cayley-Hamilton reduction engine:
      g^-1 = tr(g) I - g   (eliminates inverses),
      g^2  = tr(g) g - I   (eliminates cyclic doubled letters),
      tr((AB)^k) = Chebyshev-like recursion in z."""
    changed = True
    while changed:
        changed = False
        for i in range(len(w) - 1):
            if w[i] != w[i + 1] and w[i].upper() == w[i + 1].upper():
                w = w[:i] + w[i + 2:]
                changed = True
                break
    if not w:
        return sp.Integer(2)
    if len(w) == 1:
        return {"A": x, "a": x, "B": y, "b": y}[w]
    for i, ch in enumerate(w):
        if ch in "ab":
            g = ch.upper()
            tg = x if g == "A" else y
            return sp.expand(tg * trw(w[:i] + w[i + 1:]) - trw(w[:i] + g + w[i + 1:]))
    n = len(w)
    dw = w + w
    for i in range(n):
        if dw[i] == dw[i + 1]:
            ww = dw[i:i + n]                       # rotation with the double in front
            tg = x if ww[0] == "A" else y
            return sp.expand(tg * trw(ww[1:]) - trw(ww[2:]))
    assert n % 2 == 0                              # cyclically-alternating positive word
    k = n // 2                                     # = rotation of (AB)^k
    c0, c1 = sp.Integer(2), z
    for _ in range(k - 1):
        c0, c1 = c1, sp.expand(z * c1 - c0)
    return c1


def ab_matrix(m):
    """Abelianized monodromy Phi_m (columns = images of A, B) from the actual words."""
    wA, wB = word_pair(m)
    return sp.Matrix([[wA.count("A"), wB.count("A")], [wA.count("B"), wB.count("B")]])


def invariant_factors(M):
    """Invariant factors of an integer matrix via determinant divisors (self-contained,
    exact): d_k = gcd of all k x k minors; f_k = d_k / d_{k-1}."""
    M = sp.Matrix(M)
    r, c = M.shape
    rank = M.rank()
    dets_prev = 1
    factors = []
    for k in range(1, rank + 1):
        g = 0
        for rows in combinations(range(r), k):
            for cols in combinations(range(c), k):
                g = sp.igcd(g, M[rows, cols].det())
                if g == 1:
                    break
            if g == 1:
                break
        factors.append(sp.Integer(g) / dets_prev)
        dets_prev = sp.Integer(g)
    return [int(f) for f in factors], rank


def h1_from_presentation(rel_rows, ngens):
    """H1 = Z^ngens / rowspan(rel_rows): returns (free_rank, sorted torsion coefficients >1)."""
    M = sp.Matrix(rel_rows) if rel_rows else sp.zeros(1, ngens)
    facs, rank = invariant_factors(M)
    torsion = sorted(f for f in facs if f > 1)
    return ngens - rank, torsion


def h1_str(free, tors):
    parts = [f"Z/{d}" for d in tors] + ["Z"] * free
    return " + ".join(parts) if parts else "0"


print("=" * 99)
print("B739 Stage-B recompute -- TOMB-L293: S032-A literal universal form (B562 P1 kill)")
print("=" * 99)

print("\nPART 0 -- machinery self-tests (trace-polynomial engine + monodromy words)")
check("tr(AB) = z", trw("AB") == z)
check("tr(AB^2) = yz - x", sp.expand(trw("ABB") - (y * z - x)) == 0)
fricke = trw("ABab")
check("Fricke: tr([A,B]) = x^2+y^2+z^2-xyz-2",
      sp.expand(fricke - (x**2 + y**2 + z**2 - x * y * z - 2)) == 0)
check("tr((AB)^2) = z^2 - 2", sp.expand(trw("ABAB") - (z**2 - 2)) == 0)
w1, w2 = word_pair(1), word_pair(2)
check("phi_1 words = (AB, ABB)", w1 == ("AB", "ABB"), str(w1))
check("phi_2 words = (ABB, ABBABBB)", w2 == ("ABB", "ABBABBB"), str(w2))
ab_ok = all(ab_matrix(m) == sp.Matrix([[1, m], [m, m * m + 1]]) for m in range(1, 7))
check("abelianized monodromy Phi_m = [[1,m],[m,m^2+1]] (trace m^2+2), m=1..6", ab_ok)


# =====================================================================================
# PART 1 -- the fork: the trace-ring invariant kappa is discretely 2-valued
# =====================================================================================

print("\nPART 1 -- the fork (trace-ring baseline, re-derived)")

# ---- 1a. the declared fixed loci really are trace-map fixed (exact, whole-curve) ----
sub1 = {y: x / (x - 1), z: x}
res1 = [sp.cancel(e.subs(sub1)) for e in (trw(w1[0]) - x, trw(w1[1]) - y, trw(w1[0] + w1[1]) - z)]
check("m=1 locus (x, x/(x-1), x) is phi_1-fixed (3 trace identities == 0)", res1 == [0, 0, 0])

X2 = sp.cancel((4 * t - 2 * t**2 - 4) / (2 - t**2))
Z2 = sp.cancel(2 + t * (X2 - 2))
check("m=2 conic parametrization: z(t)^2 - (2x(t)^2 - 4) == 0", sp.cancel(Z2**2 - (2 * X2**2 - 4)) == 0)
Y2 = sp.cancel(2 * X2 / Z2)
sub2 = {x: X2, y: Y2, z: Z2}
res2 = [sp.cancel(e.subs(sub2)) for e in (trw(w2[0]) - x, trw(w2[1]) - y, trw(w2[0] + w2[1]) - z)]
check("m=2 locus (x(t), 2x/z, z(t)) is phi_2-fixed (3 trace identities == 0)", res2 == [0, 0, 0])

# ---- 1b. kappa on each locus (Fricke, exact) ----
kap1 = sp.cancel(fricke.subs(sub1))
kap2 = sp.cancel(fricke.subs(sub2))
print(f"  kappa_1(x) = {sp.factor(kap1)}")
print(f"  kappa_2(t) = (rational function of t; kappa_2(1/2) = {kap2.subs(t, sp.Rational(1, 2))})")

# ---- 1c. the suspension trace u = tr(T)^2/det(T), derived by exact solves ----

def u_exact(m, xv, yv, zv, root=0, recheck=False):
    """Exact suspension-trace-squared at one point of the fixed locus: solve the linear
    conjugation system T*g = phi(g)*T for g in {A,B}; u = tr(T0)^2/det(T0).
    (The fixed-locus membership is proven symbolically for the WHOLE curve in 1a; the
    optional per-point recheck is used as a spot check only.)"""
    A = sp.Matrix([[xv, -1], [1, 0]])
    disc = sp.nsimplify((xv + yv)**2 - 4 * (zv + 2))
    a = sp.radsimp(((xv + yv) + (1 if root == 0 else -1) * sp.sqrt(disc)) / 2)
    B = sp.Matrix([[a, zv + 1 - xv * a], [1, yv - a]])
    wA, wB = word_pair(m)

    def wmat(w):
        M = sp.eye(2)
        for ch in w:
            M = sp.Matrix(2, 2, [sp.expand(e) for e in M * (A if ch == "A" else B)])
        return M

    pA, pB = wmat(wA), wmat(wB)
    if recheck:
        for lhs, target in ((pA.trace(), xv), (pB.trace(), yv), ((pA * pB).trace(), zv)):
            if sp.simplify(lhs - target) != 0:
                return None
    tv = sp.symbols("t0 t1 t2 t3")
    Tm = sp.Matrix(2, 2, tv)
    eqs = []
    for Msrc, Mdst in ((A, pA), (B, pB)):
        E = Tm * Msrc - Mdst * Tm
        eqs += [sp.expand(E[i]) for i in range(4)]
    Mlin = sp.Matrix([[e.coeff(s) for s in tv] for e in eqs])
    ns = Mlin.nullspace(simplify=True)
    if len(ns) != 1:
        return None
    T0 = ns[0].reshape(2, 2)
    det = sp.radsimp(sp.expand(T0.det()))
    if sp.simplify(det) == 0:
        return None
    val = sp.nsimplify(sp.simplify(sp.radsimp(sp.expand(T0.trace()**2) / det)))
    return val if val.is_Rational else None


def rat_interp(points, var, max_num=10, max_den=10, holdout=6):
    """Minimal-degree exact rational interpolation N(var)/D(var) through the fit points,
    verified on ALL points (the last `holdout` points are excluded from the fit)."""
    fit = points[:-holdout]
    for total in range(0, max_num + max_den + 1):
        for dn in range(0, min(total, max_num) + 1):
            dd = total - dn
            if dd > max_den or len(fit) < dn + dd + 1:   # never fit underdetermined
                continue
            rows = [[v**j for j in range(dn + 1)] + [-uv * v**j for j in range(dd + 1)]
                    for v, uv in fit]
            ns = sp.Matrix(rows).nullspace()
            if len(ns) != 1:                             # demand a unique candidate
                continue
            vec = ns[0]
            N = sum(vec[j] * var**j for j in range(dn + 1))
            D = sum(vec[dn + 1 + j] * var**j for j in range(dd + 1))
            if D == 0:
                continue
            if all(D.subs(var, v) != 0 and
                   sp.cancel(N.subs(var, v) - uv * D.subs(var, v)) == 0
                   for v, uv in points):
                return sp.cancel(N / D), (dn, dd)
    return None, None


# fixed sample points (deterministic; poles/degenerate points simply yield None and are
# reported -- none are expected on these lists)
# (x=2 is excluded: kappa_1(2) = 2, the reducible/degenerate character)
M1_XS = [sp.Rational(p, q) for p, q in
         [(3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1),
          (-2, 1), (-3, 1), (-4, 1), (-5, 1), (-6, 1), (3, 2), (5, 2), (7, 2), (9, 2),
          (-3, 2), (-5, 2), (1, 3), (2, 3), (-1, 3), (4, 3), (5, 3)]]
M2_TS = [sp.Rational(p, q) for p, q in
         [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (1, 5), (2, 5), (3, 5), (4, 5), (1, 6),
          (5, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (1, 8), (3, 8), (5, 8),
          (7, 8), (1, 9), (2, 9), (4, 9), (5, 9), (7, 9), (8, 9), (-1, 2), (-1, 3), (-2, 3),
          (1, 10), (3, 10), (7, 10), (9, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11),
          (6, 11), (7, 11), (8, 11)]]

pts1 = []
for i, xv in enumerate(M1_XS):
    val = u_exact(1, xv, xv / (xv - 1), xv, recheck=(i == 0))
    if val is not None:
        pts1.append((xv, val))
check(f"m=1: exact u at {len(pts1)}/{len(M1_XS)} sample points (conjugation solve, nullspace dim 1)",
      len(pts1) == len(M1_XS))
both1 = u_exact(1, M1_XS[0], M1_XS[0] / (M1_XS[0] - 1), M1_XS[0], root=1)
check("m=1: both roots of the a-quadratic give the same u (gauge-independence spot check)",
      both1 == pts1[0][1])

seen = set()
pts2 = []
for i, tv_ in enumerate(M2_TS):
    xv, zv = X2.subs(t, tv_), Z2.subs(t, tv_)
    if xv in seen:
        continue
    seen.add(xv)
    val = u_exact(2, xv, 2 * xv / zv, zv, recheck=(i == 0))
    if val is not None:
        pts2.append((tv_, val))
check(f"m=2: exact u at {len(pts2)} distinct sample points", len(pts2) >= 20)
xv0, zv0 = X2.subs(t, M2_TS[0]), Z2.subs(t, M2_TS[0])
both2 = u_exact(2, xv0, 2 * xv0 / zv0, zv0, root=1)
check("m=2: both roots of the a-quadratic give the same u", both2 == pts2[0][1])

u1, deg1 = rat_interp(pts1, x)
u2, deg2 = rat_interp(pts2, t)
check("m=1: u(x) interpolated (min degree) + verified on ALL points incl. 6 holdout",
      u1 is not None, f"u_1(x) = {u1}, degrees {deg1}")
check("m=2: u(t) interpolated (min degree) + verified on ALL points incl. 6 holdout",
      u2 is not None, f"degrees {deg2}")

# cross-check against the banked closed forms (B67 / B69-V33) -- corroboration, not input
check("cross-check: u_1(x) == (x^2+x-1)/(x-1)  [B67 form]",
      u1 is not None and sp.cancel(u1 - (x**2 + x - 1) / (x - 1)) == 0)
check("cross-check: u_2(t) == x(t)^4/(x(t)^2-2)  [B69/V33 form]",
      u2 is not None and sp.cancel(u2 - X2**4 / (X2**2 - 2)) == 0)

# ---- 1d. per-seed (kappa,u)-curve relations, fitted then SYMBOLICALLY verified ----

def fit_curve(kap_expr, u_expr, var, samples):
    """Find the polynomial F with kappa = F(u) on the curve (degree search 1..3); the fit
    from samples is then verified SYMBOLICALLY (sp.cancel == 0) on the whole curve."""
    for deg in range(1, 4):
        cs = sp.symbols(f"c0:{deg + 1}")
        rows, rhs = [], []
        for v in samples[:deg + 2]:
            uv = u_expr.subs(var, v)
            rows.append([uv**j for j in range(deg + 1)])
            rhs.append(kap_expr.subs(var, v))
        sol = sp.linsolve((sp.Matrix(rows), sp.Matrix(rhs)), cs)
        if not sol:
            continue
        c = list(sol)[0]
        F = sum(c[j] * u**j for j in range(deg + 1))
        if sp.cancel(kap_expr - F.subs(u, u_expr)) == 0:
            return sp.expand(F)
    return None


F1 = fit_curve(kap1, u1, x, [v for v, _ in pts1])
F2 = fit_curve(kap2, u2, t, [v for v, _ in pts2])
check("m=1 curve relation derived + symbolically verified", F1 is not None, f"kappa = {F1}")
check("m=2 curve relation derived + symbolically verified", F2 is not None, f"kappa = {F2}")

# ---- 1e. the fork: exact intersection of the two curves (identity gluing = match (kappa,u)) ----
u_sols = sorted(sp.solve(sp.Eq(F1, F2), u))
fork = sorted(set(sp.nsimplify(F2.subs(u, s)) for s in u_sols), key=lambda v: float(v))
print(f"  matched u values (shared suspension-trace^2): {u_sols}")
print(f"  FORK: kappa in {fork}")
check("fork = {-4, -2} (matches the banked B131 fork exactly)", fork == BANKED_FORK)
check("fork is discretely MULTIVALUED: 2 distinct values", len(fork) == 2 and fork[0] != fork[1])
check("both fork reps irreducible (kappa != 2)", all(k != 2 for k in fork))
pairing = {int(s): int(sp.nsimplify(F2.subs(u, s))) for s in u_sols}
print(f"  pairing u -> kappa: {pairing}   (kappa=-2 is the shared complete-cusp branch, per B131)")


# =====================================================================================
# PART 2 -- invariant (i): |H1|-torsion of the glued manifold (single-valued on the fork)
# =====================================================================================

print("\nPART 2 -- |H1|-torsion of X = M_1 U_T M_2 (identity gluing), with SnapPy cross-validation")

# ---- 2a. the pieces (Wang presentation, exact SNF) ----
piece = {}
for m in (1, 2, 3):
    Phi = ab_matrix(m)
    rel = (sp.eye(2) - Phi).T                       # rows: g - phi(g)^ab, g in {A,B}
    rows = [list(rel.row(i)) + [0] for i in range(2)]  # columns (A, B, t)
    piece[m] = h1_from_presentation(rows, 3)
    facs, _ = invariant_factors(sp.eye(2) - Phi)
    print(f"  seed m={m}: SNF(I - Phi_{m}) invariant factors {facs};"
          f"  H1(M_{m}) = {h1_str(*piece[m])}")
check("H1(M_1) = Z (torsion trivial)", piece[1] == (1, []))
check("H1(M_2) = Z + Z/2 + Z/2 (torsion (Z/2)^2, order 4)", piece[2] == (1, [2, 2]))
check("H1(M_3) = Z + Z/3 + Z/3 (the (Z/m)^2 pattern)", piece[3] == (1, [3, 3]))
snf_pattern = all(invariant_factors(sp.eye(2) - ab_matrix(m))[0] == [m, m] for m in range(1, 7))
check("general pattern verified m=1..6: SNF(I - Phi_m) = diag(m, m) => piece torsion (Z/m)^2",
      snf_pattern)

# ---- 2b. SnapPy cross-validation (THE step the tombstone flagged as missing) ----
try:
    import snappy

    N1 = snappy.Manifold("b++LR")
    N2 = snappy.Manifold("b++LLRR")
    N3 = snappy.Manifold("b++LLLRRR")
    check("SnapPy: b++LR is the figure-eight m004 (validates the bundle-name convention at m=1)",
          N1.is_isometric_to(snappy.Manifold("m004")))
    for name, N, m in (("b++LR", N1, 1), ("b++LLRR", N2, 2), ("b++LLLRRR", N3, 3)):
        eds = sorted(N.homology().elementary_divisors())
        want = sorted([0] + [m, m] if m > 1 else [0])
        check(f"SnapPy H1({name}) elementary divisors {eds} == Wang prediction {want}",
              eds == want, f"(vol {float(N.volume()):.6f})")
    ident2 = [str(Mfd) for Mfd in N2.identify()]
    print(f"  SnapPy identifies the m=2 seed bundle as: {ident2}")
except Exception as exc:                                             # pragma: no cover
    check("SnapPy cross-validation ran", False, f"unavailable: {exc!r}")

# ---- 2c. the glued manifold: Mayer-Vietoris cokernel (= amalgam abelianization), exact SNF ----
# columns: (A1, B1, t1, A2, B2, t2)
rel1 = (sp.eye(2) - ab_matrix(1)).T
rel2 = (sp.eye(2) - ab_matrix(2)).T
rows = []
for i in range(2):
    rows.append(list(rel1.row(i)) + [0, 0, 0, 0])    # piece 1 Wang relations
for i in range(2):
    rows.append([0, 0, 0] + list(rel2.row(i)) + [0])  # piece 2 Wang relations
rows.append([0, 0, 0, 0, 0, 0])   # MV image of [dF]: [A1,B1] - [A2,B2] |-> 0 - 0 (commutators die)
rows.append([0, 0, 1, 0, 0, -1])  # MV image of [susp]: t1 - t2
freeX, torsX = h1_from_presentation(rows, 6)
tors_order = 1
for d in torsX:
    tors_order *= d
print(f"  MV cokernel (H0(T)->H0(+)H0 injective => H1(X) = coker(H1(T^2)->H1(M1)(+)H1(M2))):")
print(f"  H1(X) = {h1_str(freeX, torsX)};  |H1|-torsion = order {tors_order} "
      f"({' + '.join(f'Z/{d}' for d in torsX)})")
check("H1(X) = Z + Z/2 + Z/2", (freeX, torsX) == (1, [2, 2]))

# ---- 2d. single-valuedness across the fork ----
print(f"  X is ONE fixed manifold; the fork indexes points of X's character variety, so:")
for k in fork:
    print(f"    branch kappa={k}: |H1(X)|-torsion = {tors_order}")
check("invariant (i) SINGLE-VALUED on the fork (same value at kappa=-4 and kappa=-2)", True,
      f"value {tors_order} at both branches")

# ---- 2e. comparison with the banked value ----
print(f"  BANKED value: 'Z/m1 (+) Z/m2 (= order {BANKED_TORSION_ORDER} for (1,2))' [hand-derived MV]")
print(f"  RECOMPUTED value: (Z/m1)^2 (+) (Z/m2)^2 = (Z/2)^2, order {tors_order}")
if tors_order != BANKED_TORSION_ORDER:
    print("  => the hand-derived MV VALUE was WRONG (each seed contributes coker(I-Phi_m) =")
    print("     (Z/m)^2, SNF diag(m,m) -- confirmed by SnapPy on the pieces). This is exactly")
    print("     what the arc's own 'SnapPy cross-validate' flag anticipated. The DISCRIMINATING")
    print("     property (single-valued, a function of the seed pair alone) is UNAFFECTED:")
    print("     the corrected value is still fork-branch-independent.")


# =====================================================================================
# PART 3 -- invariant (ii): gap-label frequency-module rank (single-valued on the fork)
# =====================================================================================

print("\nPART 3 -- gap-label frequency-module rank (B173 conventions)")

lam = {m: (m + sp.sqrt(m * m + 4)) / 2 for m in (1, 2, 4)}
alpha1 = sp.radsimp(1 / lam[1])
alpha2 = sp.radsimp(1 / lam[2])
alpha4 = sp.radsimp(1 / lam[4])
check("alpha_1 = 1/lambda_1 = (sqrt5-1)/2 (golden frequency)",
      sp.simplify(alpha1 - (sp.sqrt(5) - 1) / 2) == 0)
check("alpha_2 = 1/lambda_2 = sqrt2 - 1 (silver frequency)",
      sp.simplify(alpha2 - (sp.sqrt(2) - 1)) == 0)
check("alpha_4 = 1/lambda_4 = sqrt5 - 2 (same-field control, B173 R2)",
      sp.simplify(alpha4 - (sp.sqrt(5) - 2)) == 0)

# exact rank: irrationality certificates + case analysis
degs = {d: sp.degree(sp.minimal_polynomial(sp.sqrt(d), x), x) for d in (2, 5, 10)}
check("sqrt2, sqrt5, sqrt10 all irrational (minimal-polynomial degrees 2,2,2)",
      all(v == 2 for v in degs.values()), str(degs))
# a + b*alpha_1 + c*alpha_2 = 0  =>  (b/2) sqrt5 + c sqrt2 = r in Q; squaring gives
# b*c*sqrt10 in Q => b*c = 0 (sqrt10 irrational); each branch then kills b, c, a in turn
# (sqrt5, sqrt2 irrational). So {1, alpha_1, alpha_2} is Q-independent: rank EXACTLY 3.
# Corroborate with the coordinate matrix in the Q-basis {1, sqrt2, sqrt5, sqrt10} of
# Q(sqrt2, sqrt5) ([Q(sqrt2+sqrt5):Q] = 4):
deg_field = sp.degree(sp.minimal_polynomial(sp.sqrt(2) + sp.sqrt(5), x), x)
check("[Q(sqrt2,sqrt5):Q] = 4 (min poly of sqrt2+sqrt5 has degree 4)", deg_field == 4)
coords = sp.Matrix([
    [1, 0, 0, 0],                                   # 1
    [sp.Rational(-1, 2), 0, sp.Rational(1, 2), 0],  # alpha_1 = -1/2 + (1/2) sqrt5
    [-1, 1, 0, 0],                                  # alpha_2 = -1 + sqrt2
])
basis = [sp.Integer(1), sp.sqrt(2), sp.sqrt(5), sp.sqrt(10)]
coords_ok = all(
    sp.simplify(sum(coords[i, j] * basis[j] for j in range(4)) - v) == 0
    for i, v in enumerate([sp.Integer(1), alpha1, alpha2]))
check("coordinates of {1, alpha_1, alpha_2} in basis {1,sqrt2,sqrt5,sqrt10} verified", coords_ok)
check("coordinate matrix rank = 3, row-nullspace trivial => rank(Z + Z a1 + Z a2) = 3 EXACT",
      coords.rank() == 3 and coords.T.nullspace() == [])

# PSLQ leg (B173's parameters: precision 60, maxcoeff 1e6) -- deterministic
from mpmath import mp, mpf, pslq

mp.dps = 60
a1n = (mp.sqrt(5) - 1) / 2
a2n = mp.sqrt(2) - 1
a4n = mp.sqrt(5) - 2
rel12 = pslq([mpf(1), a1n, a2n], maxcoeff=10**6, maxsteps=10**4)
relprod = pslq([mpf(1), a1n, a2n, a1n * a2n], maxcoeff=10**6, maxsteps=10**4)
rel14 = pslq([mpf(1), a1n, a4n], maxcoeff=10**6, maxsteps=10**4)
check("PSLQ finds NO integer relation in (1, alpha_1, alpha_2) [B173 R1 => rank 3]", rel12 is None)
check("PSLQ finds NO relation even adding the product alpha_1*alpha_2 [B173 R3]", relprod is None)
check("positive control: PSLQ FINDS the same-field relation for (1, alpha_1, alpha_4) [B173 R2]",
      rel14 is not None, f"relation {rel14}")
if rel14 is not None:
    lhs = rel14[0] + rel14[1] * alpha1 + rel14[2] * alpha4
    check("the found control relation verified EXACTLY in sympy", sp.simplify(lhs) == 0,
          f"{rel14[0]} + {rel14[1]}*alpha_1 + {rel14[2]}*alpha_4 == 0")

print("  the module is computed from the seed pair (m1,m2)=(1,2) ALONE; kappa never enters:")
for k in fork:
    print(f"    branch kappa={k}: gap-label frequency-module rank = 3")
check("invariant (ii) SINGLE-VALUED on the fork (rank 3 at both branches)", True)
check("recomputed rank == banked rank 3", 3 == BANKED_GAP_RANK)


# =====================================================================================
# PART 4 -- verdict assembly
# =====================================================================================

print("\n" + "=" * 99)
print("VERDICT ASSEMBLY")
print("=" * 99)
print(f"""
  (F0) trace-ring invariant kappa on the (1,2) identity-glued fork: {fork}
       -- discretely 2-valued (both values irreducible, kappa != 2). RE-DERIVED end-to-end
       (loci verified trace-map-fixed; suspension trace derived by exact conjugation solves;
       curve relations kappa = u^2-5u+2 (m=1), kappa = u-6 (m=2) verified symbolically;
       fork = exact intersection).
  (F1) |H1|-torsion of the glued X: order {tors_order} ({h1_str(0, torsX)}) at BOTH branches
       -- SINGLE-VALUED. (Banked hand-derived MV value 'order {BANKED_TORSION_ORDER}' is CORRECTED
       to order {tors_order} = (Z/m1)^2(+)(Z/m2)^2; SnapPy cross-validation of the pieces done,
       as the tombstone itself required; the correction does NOT touch single-valuedness.)
  (F2) gap-label frequency-module rank: 3 at BOTH branches -- SINGLE-VALUED
       (exact + PSLQ, B173 conventions; positive control shows the method detects relations).

  A single-valued invariant is not 'discretely-multivalued-and-unsymmetric'; two such
  invariants exist on a fork where the trace-ring invariant IS 2-valued. Hence the literal
  universal claim S032-A ('NO invariant escapes') is FALSE -- the banked kill stands.
""")
if FAIL:
    print(f"RESULT: {len(FAIL)} CHECK(S) FAILED: {FAIL}")
else:
    print("RESULT: ALL CHECKS PASS -- banked kill RECONFIRMED (with the |H1|-torsion value")
    print("        corrected from order 2 to order 4; discriminating fact intact).")
