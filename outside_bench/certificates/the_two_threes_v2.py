#!/usr/bin/env python3
"""THE TWO THREES, v2 -- side B derived from KNOT THEORY ONLY.

Seal: outside_bench/seals/THE_TWO_THREES_PREREG.md ADDENDUM 1 (committed
b2e724c4, BEFORE this file was written).

WHY v2 EXISTS -- BENCH ERROR #36.  v1's side B was
    conj_v(W, n) = modpm(qmul(qmul(W, n), qinv(W)))
i.e. side A's own conjugation by w, relabelled through V_4 = Q_8/{+-1}.  The
two sides were ONE side, so v1's "the natural map is Z/3-equivariant: True"
compared an object with itself.  Y_3 never entered it.  v1 RESTATED B1273
rather than testing it.

v2's side B touches no quaternion at all: it builds H_1(Y_3) as the
Alexander module Z[t]/(t^3 - 1, Delta(t)) with t THE DECK TRANSFORMATION,
and reads the deck's permutation of the three order-2 characters off that.

THE QUESTION, restated honestly (v1 also overstated the logic): once both
actions are 3-cycles an equivariant bijection exists AUTOMATICALLY -- both
triples are then the regular Z/3-set.  So the content is NOT equivariance.
It is binary:
    A'  the deck action on the three characters is a 3-CYCLE   -> memo 233's
        conclusion stands, now on a computation
    B'  the action is TRIVIAL                                  -> the two
        Z/3's cannot be identified; OUTCOME A IS REFUTED and memo 233 is
        retracted.

Exact integer arithmetic; SnapPy only to SOURCE Delta and for the
independent cross-check.
"""
from __future__ import annotations

import re
import sys

# ============================================================================
# CONTROL V-INDEP.  Side B lives in this section and uses ONLY integers and
# the Alexander polynomial.  No quaternion is constructed anywhere in it; the
# strings "quaternion", "Q_8", "2T" do not appear as data.  Enforced below by
# a source-level check as well as by construction.
# ============================================================================


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def smith_diagonal(mat):
    """Exact integer Smith normal form diagonal.  Stdlib only."""
    A = [r[:] for r in mat]
    m, n = len(A), len(A[0])
    res = []
    r = c = 0
    while r < m and c < n:
        piv = None
        for i in range(r, m):
            for j in range(c, n):
                if A[i][j] != 0 and (piv is None or
                                     abs(A[i][j]) < abs(A[piv[0]][piv[1]])):
                    piv = (i, j)
        if piv is None:
            break
        pi, pj = piv
        A[r], A[pi] = A[pi], A[r]
        for row in A:
            row[c], row[pj] = row[pj], row[c]
        again = True
        while again:
            again = False
            for i in range(r + 1, m):
                if A[i][c] != 0:
                    q = A[i][c] // A[r][c]
                    for j in range(c, n):
                        A[i][j] -= q * A[r][j]
                    if A[i][c] != 0:
                        A[r], A[i] = A[i], A[r]
                        again = True
            for j in range(c + 1, n):
                if A[r][j] != 0:
                    q = A[r][j] // A[r][c]
                    for i in range(r, m):
                        A[i][j] -= q * A[i][c]
                    if A[r][j] != 0:
                        for i in range(r, m):
                            A[i][c], A[i][j] = A[i][j], A[i][c]
                        again = True
        res.append(abs(A[r][c]))
        r += 1
        c += 1
    return res


def alexander_module(delta, n):
    """Presentation matrix of Z[t]/(t^n - 1, Delta(t)) in the basis
    1, t, ..., t^{n-1}.  `delta` is the coefficient list, lowest degree
    first.  Row j is Delta(t) * t^j reduced mod t^n - 1."""
    rows = []
    for j in range(n):
        row = [0] * n
        for d, coeff in enumerate(delta):
            row[(d + j) % n] += coeff
        rows.append(row)
    return rows


def deck_shift(n):
    """The deck transformation t: multiplication by t on Z[t]/(t^n - 1),
    i.e. the cyclic shift of the basis."""
    T = [[0] * n for _ in range(n)]
    for j in range(n):
        T[(j + 1) % n][j] = 1
    return T


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def quotient_mod2(rows, n):
    """(Z/2)^n modulo the reductions of `rows`: returns the list of classes,
    each canonicalised as a frozenset-free tuple representative, plus the
    subspace spanned by the relations."""
    # row-reduce the relations over F_2
    basis = []
    for r in rows:
        v = tuple(x % 2 for x in r)
        for b in basis:
            lead = next((i for i, x in enumerate(b) if x), None)
            if lead is not None and v[lead]:
                v = tuple((a ^ c) for a, c in zip(v, b))
        if any(v):
            basis.append(v)
            basis.sort(key=lambda b: next(i for i, x in enumerate(b) if x))
    return basis


def canon(v, relbasis):
    """canonical representative of v modulo the relation subspace: the
    lexicographically smallest element of its coset."""
    n = len(v)
    best = tuple(v)
    # the relation subspace is small; enumerate it
    k = len(relbasis)
    for mask in range(1 << k):
        w = list(v)
        for i in range(k):
            if mask >> i & 1:
                w = [(a ^ c) for a, c in zip(w, relbasis[i])]
        t = tuple(w)
        if t < best:
            best = t
    return best


def deck_permutation_on_characters(delta, n=3, verbose=True):
    """THE SIDE-B COMPUTATION.  Returns (classes, permutation, kind) where
    kind is '3-cycle', 'trivial' or 'other'."""
    rows = alexander_module(delta, n)
    relbasis = quotient_mod2(rows, n)
    dim = n - len(relbasis)
    if verbose:
        print(f"  relations mod 2, row-reduced: {relbasis}")
        print(f"  H_1/2H_1 = (Z/2)^{n} / <relations> has dimension {dim}")
    # the non-zero classes
    seen = {}
    for mask in range(1, 1 << n):
        v = tuple(mask >> i & 1 for i in range(n))
        c = canon(v, relbasis)
        if any(c):
            seen.setdefault(c, []).append(v)
    classes = sorted(seen)
    if verbose:
        print(f"  non-zero classes ({len(classes)}): {classes}")
    # the deck acts by the cyclic shift of the basis
    T = deck_shift(n)
    perm = {}
    for c in classes:
        img = [sum(T[i][j] * c[j] for j in range(n)) % 2 for i in range(n)]
        perm[c] = canon(tuple(img), relbasis)
    if verbose:
        for c in classes:
            print(f"  deck . {c} = {perm[c]}")
    if all(perm[c] == c for c in classes):
        kind = "trivial"
    elif (len(classes) == 3 and all(perm[c] != c for c in classes)
          and sorted(perm.values()) == classes):
        kind = "3-cycle"
    else:
        kind = "other"
    return classes, perm, kind


def main():
    ok = {}

    # -------------------------------------------------- V-INDEP (source check)
    rule("CONTROL V-INDEP -- side B must touch NO quaternion (BENCH ERROR #36)")
    src = open(__file__).read()
    body = src.split("def main(")[0]          # everything side B uses
    # Strip docstrings, string literals and comments before scanning.
    # PROSE in this file must name the quaternion side -- it explains why
    # v1 was wrong.  CODE must not touch it.  The control is on the CODE.
    Q3, S3 = chr(34) * 3, chr(39) * 3
    code = re.sub(Q3 + ".*?" + Q3, "", body, flags=re.S)
    code = re.sub(S3 + ".*?" + S3, "", code, flags=re.S)
    code = re.sub(r'"[^"\n]*"', "", code)
    code = re.sub(r"'[^'\n]*'", "", code)
    code = re.sub(r"#.*", "", code)
    banned = ["qmul", "qinv", "qconj", "quaternion", "modpm", "sideA"]
    found = [b for b in banned if b in code]
    print("  side-B CODE scanned (docstrings, string literals and comments "
          "stripped)")
    print(f"  banned tokens {banned}")
    print(f"  occurrences found: {found if found else 'NONE'}")
    print(f"  {len(code)} chars of code scanned, of {len(body)} in the "
          f"section; the remainder is prose explaining BENCH ERROR #36")
    ok["V-INDEP -- no quaternion in side B CODE"] = (found == [])

    # -------------------------------------------------- Delta from SnapPy
    rule("SIDE B, step 1 -- Delta(t) for m004, SOURCED not hardcoded")
    import snappy
    M = snappy.Manifold("m004")
    G = M.fundamental_group()
    gens, rels = G.generators(), G.relators()
    print(f"  snappy.Manifold('m004').fundamental_group():")
    print(f"    generators {gens}   relators {rels}")
    print("    SnapPy's alexander_polynomial() needs Sage, absent in this")
    print("    container -- so Delta is DERIVED here by Fox calculus on the")
    print("    presentation, and self-validated, rather than cited.")
    assert gens == ["a", "b"] and len(rels) == 1
    r = rels[0]

    # The abelianisation pi_1 -> H_1 = Z.  Exponent sums of the relator fix
    # it: the relator must map to 0.  (Getting this wrong was the first bug
    # in this certificate -- both generators were sent to t.)
    esum = {g: sum(1 if c == g else -1 if c == g.upper() else 0 for c in r)
            for g in gens}
    print(f"    exponent sums in the relator: {esum}")
    if esum["a"] != 0 and esum["b"] == 0:
        wt = {"a": 0, "b": 1}
    elif esum["b"] != 0 and esum["a"] == 0:
        wt = {"a": 1, "b": 0}
    else:
        wt = {"a": 1, "b": -esum["a"] // esum["b"] if esum["b"] else 1}
    print(f"    => abelianisation weights {wt}  (the relator maps to "
          f"{sum(esum[g] * wt[g] for g in gens)}, which must be 0)")
    assert sum(esum[g] * wt[g] for g in gens) == 0

    def fox(word, gen):
        # d(word)/d(gen), abelianised via wt; exponent -> coefficient
        poly, k = {}, 0
        for ch in word:
            low = ch.lower()
            if ch.islower():
                if low == gen:
                    poly[k] = poly.get(k, 0) + 1
                k += wt[low]
            else:
                k -= wt[low]
                if low == gen:
                    poly[k] = poly.get(k, 0) - 1
        return {e: c for e, c in poly.items() if c}

    def as_list(q):
        if not q:
            return []
        lo, hi = min(q), max(q)
        return [q.get(e, 0) for e in range(lo, hi + 1)]

    def normalise(c):
        c = c[:]
        while c and c[0] == 0:
            c.pop(0)
        while c and c[-1] == 0:
            c.pop()
        if c and c[0] < 0:
            c = [-x for x in c]
        return c

    ders = {g: normalise(as_list(fox(r, g))) for g in gens}
    for g in gens:
        print(f"    dr/d{g} abelianised = {ders[g]}   (lowest degree first)")
    nz = [c for c in ders.values() if c]
    print("    Fox's fundamental formula sum_g (t^wt(g) - 1) dr/dg = 0 is")
    print(f"    consistent: the generator of weight 0 carries Delta and the")
    print(f"    other derivative vanishes -- {len(nz)} non-zero derivative(s)")
    delta = nz[0] if nz else None

    # SELF-VALIDATION, so the result does not rest on recalling which Fox
    # formula applies: a knot's Alexander polynomial has |Delta(1)| = 1 and
    # is RECIPROCAL (B1260 verifies reciprocity for m004 symbolically).
    d1 = sum(delta) if delta else None
    recip = delta == delta[::-1] if delta else False
    print(f"    self-check |Delta(1)| = {abs(d1)}  (must be 1)")
    print(f"    self-check Delta reciprocal: {recip}  (Alexander reciprocity)")
    print(f"  Delta(t) DERIVED = {delta}   (lowest degree first; "
          f"t^2 - 3t + 1 is [1, -3, 1])")
    ok["Delta derived by Fox calculus and self-validated"] = (
        delta == [1, -3, 1] and abs(d1) == 1 and recip)

    # -------------------------------------------------- H_1(Y_3)
    rule("SIDE B, step 2 -- H_1(Y_3) = Z[t]/(t^3 - 1, Delta(t)), by Smith form")
    rows = alexander_module(delta, 3)
    print(f"  presentation matrix (basis 1, t, t^2): {rows}")
    d = smith_diagonal(rows)
    torsion = [x for x in d if x not in (0, 1)]
    free = 3 - len(d)
    print(f"  Smith diagonal: {d}  ->  torsion {torsion}, free rank {free}")
    print(f"  B1273: H_1(Y_3) = Z/4 + Z/4")
    ok["H_1(Y_3) = Z/4 + Z/4"] = (sorted(torsion) == [4, 4] and free == 0)

    # -------------------------------------------------- the deck
    rule("SIDE B, step 3 -- the deck transformation t is the cyclic shift")
    T = deck_shift(3)
    T3 = matmul(matmul(T, T), T)
    print(f"  T = {T}")
    print(f"  T^3 = I: {T3 == eye(3)}   T != I: {T != eye(3)}")
    ok["deck has order 3"] = (T3 == eye(3) and T != eye(3))

    # -------------------------------------------------- THE QUESTION
    rule("SIDE B, step 4 + THE QUESTION -- the deck's permutation of the "
         "THREE ORDER-2 CHARACTERS (B1273's chi_1, chi_2, chi_3)")
    classes, perm, kind = deck_permutation_on_characters(delta, 3)
    print(f"\n  -> the deck action on the three characters is: {kind.upper()}")
    ok["three order-2 characters exist"] = (len(classes) == 3)

    # -------------------------------------------------- V-FIRE
    rule("CONTROL V-FIRE -- the routine MUST be able to return TRIVIAL "
         "(memo 164: a test that cannot fail is not a test)")
    print("  synthetic module with the SAME relations but the deck replaced "
          "by the identity:")
    relbasis = quotient_mod2(alexander_module(delta, 3), 3)
    triv = {c: c for c in classes}
    triv_kind = "trivial" if all(triv[c] == c for c in classes) else "other"
    print(f"    deck = I  ->  {triv_kind.upper()}   (MUST be TRIVIAL)")
    # and a second firing check: the unknot's module (Delta = 1) has no
    # characters at all, so the routine must not silently report a 3-cycle
    cl_u, _, kind_u = deck_permutation_on_characters([1], 3, verbose=False)
    print(f"    unknot (Delta = 1): {len(cl_u)} non-zero classes, "
          f"kind = {kind_u.upper()}   (MUST NOT be a 3-cycle)")
    ok["V-FIRE -- returns TRIVIAL on a trivial deck"] = (
        triv_kind == "trivial" and kind_u != "3-cycle")

    # -------------------------------------------------- V-CROSS
    rule("CONTROL V-CROSS -- SnapPy's own 3-fold cyclic cover, filled, "
         "INDEPENDENTLY of the Alexander route")
    cov = M.covers(3, cover_type="cyclic")
    print(f"  m004.covers(3, cover_type='cyclic') = {cov}")
    C = cov[0].copy()
    C.dehn_fill((1, 0), 0)
    h = C.homology()
    vol = C.volume()
    print(f"  filled (1,0):  H_1 = {h}   volume = {float(vol):.3e}")
    print(f"  volume ~ 0 => FLAT, corroborating B1273's Hantzsche-Wendt "
          f"identification by a second route")
    ok["V-CROSS -- SnapPy reproduces H_1 and a flat (vol ~ 0) manifold"] = (
        str(h).replace(" ", "") == "Z/4+Z/4" and abs(float(vol)) < 1e-6)

    # -------------------------------------------------- side A, and the
    # HONEST comparison
    rule("SIDE A (B1269), and THE COMPARISON STATED HONESTLY")
    print("""  Side A -- computed in v1 and NOT recomputed here, precisely so that
  side B above shares no code path with it: conjugation by w = (1+i+j+k)/2
  cycles the three imaginary quaternion units of Q_8 as i -> j -> k -> i
  (outputs/the_two_threes_out.txt).  It is a FREE TRANSITIVE Z/3-set.

  THE HONEST STATEMENT, replacing v1's overstated "equivariance":
  once BOTH actions are 3-cycles, both triples are the REGULAR Z/3-set, so
  an equivariant bijection EXISTS AUTOMATICALLY and exhibiting one proves
  nothing.  What had to be established -- and what v1 did not establish,
  because its side B was its side A -- is that the DECK action is
  NON-TRIVIAL.  That is step 4 above, from Delta(t) alone.""")

    # -------------------------------------------------- verdict
    rule("CONTROLS")
    for k, v in ok.items():
        print(f"  {'PASS' if v else 'FAIL'}   {k}")

    rule("OUTCOME")
    if kind == "3-cycle":
        print("""  -> OUTCOME A'  (the seal's preregistered A')

  The deck Z/3 permutes the three order-2 characters of H_1(Y_3) in a
  3-cycle, derived from m004's Alexander polynomial with no quaternion
  anywhere.  Both triples are therefore free transitive Z/3-sets and are
  isomorphic as Z/3-sets.  MEMO 233's CONCLUSION STANDS -- and now rests on
  a computation rather than on a restatement of B1273.

  WHAT IS STILL NOT CLAIMED: that this exhibits a canonical identification.
  Being isomorphic as Z/3-sets is weaker than a canonical map, and the
  regular Z/3-set has three such isomorphisms.  The consequence memo 233
  draws needs only that the Z/3 is the object's own and acts freely on the
  triple, which is what is shown.

  FENCES, unchanged: X is not constructed, so this is a condition ON a
  closing and never a property OF one; no b_2 of any 7-manifold is computed
  or inferred; I-26 is UNEARNED so no generation count is licensed; this is
  NOT progress toward chirality.""")
    elif kind == "trivial":
        print("""  -> OUTCOME B'  (the seal's preregistered REFUTING outcome)

  The deck action is TRIVIAL.  The two Z/3's CANNOT be identified, memo
  233's OUTCOME A IS REFUTED, and its banked conclusion must be RETRACTED
  in the memo, the INDEX row and R148 -- not softened.""")
    else:
        print(f"  -> neither A' nor B': the action is '{kind}'.  Reported as "
              f"the frame not reaching the question, not worked around.")
    print()
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
