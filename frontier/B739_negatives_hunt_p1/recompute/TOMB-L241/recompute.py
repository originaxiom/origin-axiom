"""B739 Stage-B recompute — TOMB-L241 (the spectral-rank cluster umbrella, K-J..K-M).

Banked kill (speculations/TOMBSTONES.md:L241, umbrella): every "rank" identification from
the CFT/quantum-chaos review session identifying spectral rank with a repo quantity is dead
(category-error; fact_basis at Stage A: ASSERTED — no computation in the tombstone itself).

E19 discipline: the discriminating facts are RE-DERIVED here as actual computations, not
cited back at the tombstone.  The umbrella's discriminating fact is the conjunction of the
four sub-facts:

  K-J  the degenerate (phi_{2,1}) block sits at a REDUCIBLE point (kappa = tr[A,B] = 2),
       the seed sits at an IRREDUCIBLE point (kappa_1 = 3 != 2) -> different points of the
       character variety -> "phi^2 = degenerate-block monodromy multiplier" is a category
       error.  Recomputed: (a) Fricke identity, (b) reducible => kappa = 2 (identically,
       and independent of the multiplier), (c) Virasoro level-2 Kac determinant => the
       h_{2,1}(c) Verma module is reducible for every c (the degenerate block IS the
       reducible object), (d) kappa_m = tr[R^m,L] = m^2+2, so kappa_1 = 3.
  K-K  gap-labeling rank of a period-k geodesic / 2-letter substitution = 2 for EVERY k
       (module Z + Z.alpha, alpha a quadratic irrational), never k.  Golden Fibonacci is
       rank 2, not rank 1 (the session's mislabel).
  K-L  the SL(n) tower eigenvalues (Sym^d of the seed matrix) generate a multiplicative
       group of free rank 1 at every n (B85 constraint note recomputed from scratch):
       Sym^d(M) spectrum = {(-1)^j phi^(d-2j)}, Sym^d(M^2) spectrum = {phi^(2(d-2j))}
       — all powers of phi (resp. phi^2); the spectral rank does not climb with n.
  K-M  built on K-K/K-L; with both premises recomputed dead (both ranks are CONSTANTS,
       2 and 1, varying with neither k nor n), the "measurable gap-labeling-rank
       prediction" has no support.  The surviving rank statement is S023's single-seed
       rank 2 (recomputed here as part of K-K).

Conventions declared (E1) — undeclared in the tombstone, chosen here:
  C1. kappa := tr[A,B] = tr(A B A^-1 B^-1), Fricke normal form x^2+y^2+z^2-xyz-2
      (repo S003).  Reducibility criterion: a reducible SL(2) pair has kappa = 2.
  C2. The seed pair realizing kappa_m: (A,B) = (R^m, L), R = [[1,1],[0,1]],
      L = [[1,0],[1,1]].  This is the unique natural parabolic pair reproducing BOTH
      sealed repo values kappa_1 = 3 (TOMBSTONES K-N) and kappa_2 = m^2+2 = 6 (K-N),
      and the E6 "monodromy trace m^2+2" (CLAIMS.md E6) via tr(M_m^2), M_m=[[m,1],[1,0]].
      (The 3-manifold peripheral-parabolic holonomy pair of S003 has kappa = -2; also
      != 2, so the K-J verdict is robust to this convention choice.)
  C3. Gap-labeling rank := rank_Z of the gap-label module Z + Z.alpha (repo S023 sealed
      form: IDOS labels in Z + Z.alpha_m, alpha_m = phi_m/(phi_m+1)).  For a general
      period-k word the frequency alpha is a Q-Moebius image of the fixed slope of the
      word matrix; rank_Z(Z + Z.beta) = 2 for ANY irrational beta in the same quadratic
      field, so the rank conclusion is independent of that choice.
  C4. The SL(n) tower := Sym^d lifts (n = d+1) of the seed substitution matrix
      M = [[1,1],[1,0]] (B85 convention: eigenvalues +-phi^(d-2j)) and of the monodromy
      M^2 (K-L's phrasing: "all powers of phi^2").  Both computed.
  C5. Word sample for K-K (deterministic, declared): all continued-fraction words
      (a_1..a_k) in {1,2}^k for k = 1..6, canonical under cyclic rotation;
      M_w = prod [[a_i,1],[1,0]].  Plus the three metallic seeds m = 1,2,3 via S023's
      alpha_m.
Determinism: no wall-clock, no randomness, no network; every equality is exact/symbolic
(sympy); no floating point anywhere.
Gate 5: pure mathematics; no SM quantities; symbolic central charge c (never a physical
value).
"""

from __future__ import annotations

import itertools
from functools import lru_cache
from math import gcd

import sympy as sp

phi = (1 + sp.sqrt(5)) / 2


def tr(M):
    return sp.trace(M)


def sl2_inv(M):
    """Inverse of an SL(2) matrix via the adjugate (exact; requires det = 1)."""
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[d, -b], [-c, a]])


def kappa(A, B):
    return sp.simplify(tr(A * B * sl2_inv(A) * sl2_inv(B)))


def hdr(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)


# ---------------------------------------------------------------------------
# PART 1 — K-J: "phi^2 = degenerate-block monodromy multiplier"
# ---------------------------------------------------------------------------
hdr("PART 1 (K-J): reducible block (kappa=2) vs irreducible seed (kappa=3)")

# 1a. Fricke identity tr[A,B] = x^2+y^2+z^2-xyz-2 on generic SL(2) pairs (symbolic).
a1, a2, a3, b1, b2, b3 = sp.symbols("a1 a2 a3 b1 b2 b3", nonzero=True)
A = sp.Matrix([[a1, a2], [a3, (1 + a2 * a3) / a1]])
B = sp.Matrix([[b1, b2], [b3, (1 + b2 * b3) / b1]])
x, y, z = tr(A), tr(B), tr(A * B)
lhs = tr(A * B * sl2_inv(A) * sl2_inv(B))
diff = sp.simplify(sp.cancel(lhs - (x**2 + y**2 + z**2 - x * y * z - 2)))
print(f"1a. Fricke identity  tr[A,B] - (x^2+y^2+z^2-xyz-2)  on generic SL(2)xSL(2): {diff}")
assert diff == 0

# 1b. Reducible pair (common invariant line, wlog upper triangular) => kappa = 2, identically.
la, mu, s, t = sp.symbols("lambda_ mu s t", nonzero=True)
Ared = sp.Matrix([[la, s], [0, 1 / la]])
Bred = sp.Matrix([[mu, t], [0, 1 / mu]])
k_red = kappa(Ared, Bred)
print(f"1b. kappa(reducible pair, generic diagonal multipliers lambda, mu) = {k_red}")
assert k_red == 2

# 1c. The degenerate phi_{2,1} object IS reducible: Virasoro level-2 Shapovalov form,
#     computed from the algebra (no table lookups).
h, c = sp.symbols("h c")


@lru_cache(maxsize=None)
def vbracket(word):
    """<h| L_{w1} ... L_{wr} |h> from [L_m,L_n] = (m-n)L_{m+n} + c/12 m(m^2-1) delta.

    Strategy: commute the RIGHTMOST positive mode one step to the right; terminates
    (lexicographic measure: word length, then distance of that mode from the end).
    """
    w = list(word)
    if not w:
        return sp.Integer(1)
    if w[-1] > 0:
        return sp.Integer(0)  # L_n |h> = 0 for n > 0
    if w[-1] == 0:
        return h * vbracket(tuple(w[:-1]))  # L_0 |h> = h |h>
    if w[0] < 0:
        return sp.Integer(0)  # <h| L_{-k} = 0 for k > 0
    if w[0] == 0:
        return h * vbracket(tuple(w[1:]))
    i = max(j for j, v in enumerate(w) if v > 0)  # rightmost positive; i < len(w)-1 here
    m_, n_ = w[i], w[i + 1]
    out = vbracket(tuple(w[:i] + [n_, m_] + w[i + 2:]))
    out += (m_ - n_) * vbracket(tuple(w[:i] + [m_ + n_] + w[i + 2:]))
    if m_ + n_ == 0:
        out += sp.Rational(1, 12) * c * m_ * (m_**2 - 1) * vbracket(tuple(w[:i] + w[i + 2:]))
    return sp.expand(out)


G = sp.Matrix(
    [
        [vbracket((1, 1, -1, -1)), vbracket((1, 1, -2))],
        [vbracket((2, -1, -1)), vbracket((2, -2))],
    ]
)
print(f"1c. level-2 Shapovalov (basis L_-1^2|h>, L_-2|h>):  G = {G.tolist()}")
kacdet = sp.factor(G.det())
print(f"    Kac determinant (level 2) = {kacdet}")
roots = sp.solve(sp.Eq(G.det(), 0), h)
roots = [sp.simplify(r) for r in roots if not r.is_zero]
h21 = [r for r in roots if sp.simplify(r - (5 - c + sp.sqrt((1 - c) * (25 - c))) / 16) == 0]
h12 = [r for r in roots if sp.simplify(r - (5 - c - sp.sqrt((1 - c) * (25 - c))) / 16) == 0]
assert len(h21) == 1 and len(h12) == 1, "Kac roots do not match h_{2,1}, h_{1,2}"
h21 = h21[0]
print(f"    nonzero roots = Kac h_(2,1), h_(1,2) = ((5-c) +- sqrt((1-c)(25-c)))/16  [verified]")
# the radical (null) vector at h = h_{2,1}: v = xi * L_-1^2 |h> + L_-2 |h>, G.v = 0
xi = sp.symbols("xi")
v = sp.Matrix([xi, 1])
sol = sp.solve((G * v)[0], xi)
assert len(sol) == 1
xi_sol = sp.simplify(sol[0])
row2 = sp.simplify((G * v)[1].subs(xi, xi_sol).subs(h, h21))
print(f"    radical vector: v = ({xi_sol}) L_-1^2|h> + L_-2|h>;  second component at h=h_(2,1): {row2}")
assert sp.simplify(xi_sol + 3 / (2 * (2 * h + 1))) == 0  # the textbook null-vector coefficient
assert row2 == 0
print("    => for EVERY c, the Verma module V(c, h_(2,1)) has a nonzero Shapovalov radical")
print("       (contravariant form) => a proper nonzero submodule => REDUCIBLE.  The")
print("       degenerate phi_(2,1) block is the block of a REDUCIBLE module; its 2-dim")
print("       monodromy point has an invariant line, hence kappa = 2 by 1b.")

# 1d. The seed's kappa: kappa_m = tr[R^m, L] symbolically in m.
m = sp.symbols("m")
R_m = sp.Matrix([[1, m], [0, 1]])  # R = [[1,1],[0,1]], R^m
L = sp.Matrix([[1, 0], [1, 1]])
kap_m = sp.expand(kappa(R_m, L))
M_m = sp.Matrix([[m, 1], [1, 0]])  # metallic substitution abelianization, det = -1
mono_tr = sp.expand(tr(M_m**2))  # the (orientable) monodromy trace, CLAIMS.md E6
print(f"1d. kappa_m = tr[R^m, L] = {kap_m};   monodromy trace tr(M_m^2) = {mono_tr}")
assert kap_m == m**2 + 2 and mono_tr == m**2 + 2
kap1 = kap_m.subs(m, 1)
print(f"    seed (golden, m=1): kappa_1 = {kap1}  (matches banked K-N value 3);  kappa_2 = {kap_m.subs(m, 2)} (matches 6)")
assert kap1 == 3
print(f"    kappa_1 = 3 != 2  =>  the seed point is IRREDUCIBLE (by 1a/1b: reducible <=> kappa=2)")
print(f"    => the block point (kappa=2) and the seed point (kappa=3) are DIFFERENT points")
print(f"       of the SL(2) character variety: the K-J identification equates two distinct")
print(f"       objects.  KILL UPHELD.")

# 1e. The multiplier match is non-binding: install the seed's multiplier phi^2 on a
#     reducible pair — kappa stays 2.
Ared_phi = sp.Matrix([[phi**2, 0], [0, phi**-2]])
Bred_1 = sp.Matrix([[1, 1], [0, 1]])
k_phi = sp.simplify(kappa(Ared_phi, Bred_1))
print(f"1e. kappa(reducible pair WITH multiplier phi^2 installed) = {k_phi}  (still 2, != 3)")
assert k_phi == 2

# 1f. The "3 = 3" is family-wide, hence non-discriminating (MB8): both named quantities
#     are m^2+2 for ALL m (shown in 1d), so the numeric match at m=1 (3=3) carries zero
#     evidence for the identification; the discriminating control (MB6) is kappa vs 2,
#     which the block fails.
eig_tr_1 = sp.simplify(phi**2 + phi**-2)
print(f"1f. eigenvalue-trace phi^2 + phi^-2 = {eig_tr_1} = kappa_1 = 3: the '3=3' — an")
print(f"    eigenvalue-trace vs a commutator-trace; tr(M_m^2) = tr[R^m,L] = m^2+2 for ALL m,")
print(f"    a family identity => the match discriminates nothing (MB8); the discriminating")
print(f"    test is reducibility (kappa vs 2), computed above: 2 != 3.")
assert eig_tr_1 == 3

# ---------------------------------------------------------------------------
# PART 2 — K-K: "gap-labeling rank = composition period"
# ---------------------------------------------------------------------------
hdr("PART 2 (K-K): gap-labeling rank of period-k geodesics = 2, for every k")

t_ = sp.Symbol("t")


def cf_matrix(word):
    Mw = sp.eye(2)
    for a in word:
        Mw = Mw * sp.Matrix([[a, 1], [1, 0]])
    return Mw


def canonical_rotations(k):
    seen = set()
    for w in itertools.product((1, 2), repeat=k):
        canon = min(tuple(w[i:] + w[:i]) for i in range(k))
        seen.add(canon)
    return sorted(seen)


def module_rank(alpha):
    """rank_Z of Z + Z.alpha (2 iff alpha irrational; else 1)."""
    p = sp.minimal_polynomial(alpha, t_)
    deg = int(sp.degree(p, t_))
    return deg, (1 if deg == 1 else 2)


def sqfree_part(n):
    """Squarefree part of a positive integer (deterministic)."""
    n = int(n)
    out = 1
    for prime, exp in sp.factorint(n).items():
        if exp % 2 == 1:
            out *= prime
    return out


print(f"{'k':>2} {'word':<14} {'tr':>4} {'det':>4} {'disc':>5} {'sqfree':>6} "
      f"{'minpoly deg':>11} {'rank':>4} {'claimed=k':>9} {'rank==k?':>8}")
all_ranks = []
golden_row = None
for k in range(1, 7):
    for w in canonical_rotations(k):
        Mw = cf_matrix(w)
        trw, detw = tr(Mw), Mw.det()
        disc = trw**2 - 4 * detw
        # fixed slope of the word matrix: x = (a x + b)/(c x + d), positive root
        aa, bb, cc, dd = Mw[0, 0], Mw[0, 1], Mw[1, 0], Mw[1, 1]
        alpha = ((aa - dd) + sp.sqrt(disc)) / (2 * cc)
        deg, rank = module_rank(alpha)
        all_ranks.append((k, w, rank))
        ok = "YES" if rank == k else "no"
        print(f"{k:>2} {str(w):<14} {str(trw):>4} {str(detw):>4} {str(disc):>5} "
              f"{sqfree_part(disc):>6} "
              f"{deg:>11} {rank:>4} {k:>9} {ok:>8}")
        if k == 1 and w == (1,):
            golden_row = (alpha, deg, rank)

n_words = len(all_ranks)
n_rank2 = sum(1 for _, _, r in all_ranks if r == 2)
n_match = sum(1 for kk, _, r in all_ranks if r == kk)
print(f"\n    words tested: {n_words} (k=1..6, entries in {{1,2}}, cyclic-canonical)")
print(f"    rank = 2 for {n_rank2}/{n_words} words — CONSTANT, independent of k")
print(f"    'rank = k' holds for {n_match}/{n_words} words — only the k=2 stratum, where any")
print(f"    constant-2 matches trivially; it FAILS for every word with k != 2.")
assert n_rank2 == n_words

alpha_g, deg_g, rank_g = golden_row
print(f"\n    golden Fibonacci ([1] period k=1): alpha = {sp.radsimp(alpha_g)} = phi,")
print(f"    minpoly {sp.minimal_polynomial(alpha_g, t_)} (degree {deg_g}) => rank {rank_g}, NOT 1:")
print(f"    the session's 'golden is rank 1' mislabel is refuted, and rank 2 != period 1")
print(f"    kills the identification at the seed itself.")
assert rank_g == 2

# S023 sealed cross-check: alpha_m = phi_m/(phi_m+1), fields Q(sqrt5), Q(sqrt2), Q(sqrt13)
print("\n    S023 metallic seeds (sealed convention alpha_m = phi_m/(phi_m+1)):")
for mm in (1, 2, 3):
    phim = (mm + sp.sqrt(mm**2 + 4)) / 2
    alpham = sp.radsimp(phim / (phim + 1))
    deg, rank = module_rank(alpham)
    sqf = sqfree_part(mm**2 + 4)
    print(f"      m={mm}: alpha_{mm} in Q(sqrt({sqf})), minpoly degree {deg} => rank {rank}"
          f"   [S023 sealed field Q(sqrt({sqf}))]")
    assert rank == 2
print("    substitution word length varies with m; the rank does not: 2, 2, 2.  KILL UPHELD.")

# ---------------------------------------------------------------------------
# PART 3 — K-L: "rank = SL(n) tower depth"
# ---------------------------------------------------------------------------
hdr("PART 3 (K-L): SL(n) tower eigenvalues, multiplicative free rank = 1 at every n")

X, Y, lam = sp.symbols("X Y lam")


def sym_power(M2, d):
    """Sym^d of a 2x2 matrix via the action on binary forms of degree d."""
    aa, bb, cc, dd = M2[0, 0], M2[0, 1], M2[1, 0], M2[1, 1]
    S = sp.zeros(d + 1, d + 1)
    for j in range(d + 1):
        img = sp.expand((aa * X + bb * Y) ** (d - j) * (cc * X + dd * Y) ** j)
        pol = sp.Poly(img, X, Y)
        for i in range(d + 1):
            S[i, j] = pol.coeff_monomial(X ** (d - i) * Y**i)
    return S


M = sp.Matrix([[1, 1], [1, 0]])  # golden seed substitution matrix, eigenvalues phi, -1/phi
M2 = M * M  # the monodromy [[2,1],[1,1]], eigenvalues phi^2, phi^-2

print("Tower A: Sym^d(M),  M = [[1,1],[1,0]]  (B85 convention)")
print(f"{'n':>3} {'d':>3} {'predicted spectrum':<38} {'verified':>8} {'mult. free rank':>15} "
      f"{'claimed n-1':>11} {'claimed n':>9}")
for d in range(1, 8):
    n = d + 1
    S = sym_power(M, d)
    preds = [(-1) ** j * phi ** (d - 2 * j) for j in range(d + 1)]
    p_char = S.charpoly(lam).as_expr()
    ok = all(sp.simplify(sp.radsimp(sp.expand(p_char.subs(lam, pr)))) == 0 for pr in preds)
    exps = [d - 2 * j for j in range(d + 1)]
    # distinctness is exact: |pred_j| = phi^(d-2j), phi > 1, and the integer exponents
    # d-2j are strictly decreasing in j, so the d+1 predicted roots are pairwise distinct
    distinct = len(set(exps)) == d + 1
    g = 0
    for e in exps:
        g = gcd(g, abs(e))
    freerank = 1 if g > 0 else 0
    lbl = "{(-1)^j phi^(d-2j), j=0..%d}" % d
    print(f"{n:>3} {d:>3} {lbl:<38} {str(ok and distinct):>8} {freerank:>15} {n-1:>11} {n:>9}")
    assert ok and distinct and freerank == 1

print("\nTower B: Sym^d(M^2),  M^2 = [[2,1],[1,1]]  (K-L phrasing: 'all powers of phi^2')")
print(f"{'n':>3} {'d':>3} {'predicted spectrum':<38} {'verified':>8} {'mult. free rank':>15}")
for d in range(1, 8):
    n = d + 1
    S = sym_power(M2, d)
    preds = [phi ** (2 * (d - 2 * j)) for j in range(d + 1)]
    p_char = S.charpoly(lam).as_expr()
    ok = all(sp.simplify(sp.radsimp(sp.expand(p_char.subs(lam, pr)))) == 0 for pr in preds)
    exps_b = [2 * (d - 2 * j) for j in range(d + 1)]
    distinct = len(set(exps_b)) == d + 1  # exact: distinct integer exponents, phi > 1
    g = 0
    for e in exps_b:
        g = gcd(g, abs(e))
    freerank = 1 if g > 0 else 0
    lbl = "{phi^(2(d-2j)), j=0..%d}" % d
    print(f"{n:>3} {d:>3} {lbl:<38} {str(ok and distinct):>8} {freerank:>15}")
    assert ok and distinct and freerank == 1

print("\n    Both towers: every Sym^d eigenvalue is +-phi^(d-2j) (resp. phi^(2(d-2j))),")
print("    the multiplicative group generated is <phi^g> x <-1> — FREE RANK 1 at every n")
print("    (B85 constraint note recomputed).  Claimed 'rank = SL(n) rank n-1' fails for")
print("    every n >= 3 (1 != n-1); claimed 'rank = tower depth n' fails for every n >= 2.")
print("    At n=2 the 'n-1' reading degenerately agrees (1=1) — the m=1-style trap; the")
print("    identification has no discriminating power there and fails wherever it does.")
print("    KILL UPHELD.")

# ---------------------------------------------------------------------------
# PART 4 — K-M: the prediction built on K-K/K-L
# ---------------------------------------------------------------------------
hdr("PART 4 (K-M): the 'measurable gap-labeling-rank prediction' built on K-K/K-L")
print("    Recomputed premises: gap-label rank == 2 (constant in the period k, Part 2);")
print("    tower multiplicative rank == 1 (constant in the depth n, Part 3).  A prediction")
print("    that reads either rank as VARYING with k or n is contradicted by both computed")
print("    constants; with its premises dead the prediction falls (logical fold — nothing")
print("    further to compute).  The surviving rank statement is the field-multiplicity")
print("    direction (S023/L16): single seed rank 2, recomputed in Part 2; the multi-seed")
print("    multiplicity claim is L16's own thread, outside this tombstone.  KILL UPHELD.")

# ---------------------------------------------------------------------------
hdr("VERDICT")
print("RECONFIRMED — all four identifications of the spectral-rank cluster recompute dead:")
print("  K-J: block kappa = 2 (reducible, every c; multiplier-independent) vs seed")
print("       kappa_1 = 3 (irreducible) — different character-variety points; 2 != 3.")
print(f"  K-K: gap-label rank = 2 for all {n_words} tested words, k = 1..6 (and the 3 metallic")
print("       seeds); never = k except degenerately at k = 2; golden is rank 2, not 1.")
print("  K-L: tower multiplicative free rank = 1 at every n = 2..8, both tower")
print("       conventions; never = n-1 (n >= 3), never = n.")
print("  K-M: premises dead by computation; prediction unsupported.")
print("The umbrella kill (TOMB-L241) is upheld by computation, not citation.")
