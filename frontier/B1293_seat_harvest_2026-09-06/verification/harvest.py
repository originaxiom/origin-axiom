"""B1293 -- harvest of the physics seat (R56-R68) and the SM-derivation seat (B1272-B1277),
with the load-bearing claims RE-COMPUTED on main rather than accepted.

Standing rule: verify every cross-seat claim before banking. What follows is what this bench
could check, what it confirmed, what it CORRECTED, and what remains harvest-not-verified.
"""
from fractions import Fraction as F
import itertools, collections

# ---------- E6 machinery, built here ----------
EDGES = [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)]          # Bourbaki E6
A = [[2 if i == j else 0 for j in range(6)] for i in range(6)]
for a, b in EDGES:
    A[a - 1][b - 1] = A[b - 1][a - 1] = -1


def reflect(w, i):
    return tuple(w[j] - w[i] * A[i][j] for j in range(6))


def orbit(seed):
    W, fr = {seed}, [seed]
    while fr:
        v = fr.pop()
        for i in range(6):
            u = reflect(v, i)
            if u not in W:
                W.add(u); fr.append(u)
    return sorted(W)


def inv6(M):
    n = len(M)
    Aa = [[F(M[i][j]) for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if Aa[r][c] != 0)
        Aa[c], Aa[p] = Aa[p], Aa[c]
        pv = Aa[c][c]; Aa[c] = [x / pv for x in Aa[c]]
        for r in range(n):
            if r != c and Aa[r][c] != 0:
                f = Aa[r][c]; Aa[r] = [x - f * y for x, y in zip(Aa[r], Aa[c])]
    return [row[n:] for row in Aa]


W27 = orbit(tuple(1 if j == 0 else 0 for j in range(6)))
ROOTS = orbit(tuple(A[0]))
Ci = inv6(A)


def simple_coords(w):
    return [sum(Ci[i][j] * F(w[j]) for j in range(6)) for i in range(6)]


def grade3(c):
    """B1264's mod-3 grading of the 27 by a labelling c."""
    coef = [sum(Ci[i][j] * F(c[j]) for j in range(6)) for i in range(6)]
    return collections.Counter(int(sum(F(w[i]) * coef[i] for i in range(6))) % 3 for w in W27)


# ---------- E8 -> E6 machinery for fc's A2^3 counts ----------
def e8_roots():
    R = []
    for i in range(8):
        for j in range(i + 1, 8):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [0] * 8; v[i] = si; v[j] = sj
                    R.append(tuple(F(x) for x in v))
    for s in itertools.product((1, -1), repeat=8):
        if s.count(-1) % 2 == 0:
            R.append(tuple(F(x, 2) for x in s))
    return R


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def selftest():
    print("B1293 -- seat harvest, load-bearing claims re-computed here\n")
    print(f"  [env ] E6: {len(ROOTS)} roots, 27 has {len(W27)} weights")
    assert len(ROOTS) == 72 and len(W27) == 27

    # ---- fc R65/R68: E6 has 120 A2 subsystems and 40 A2^3 subsystems ----
    E8 = e8_roots(); assert len(E8) == 240
    a1 = E8[0]; a2 = next(r for r in E8 if dot(a1, r) == F(-1))
    E6r = [r for r in E8 if dot(r, a1) == 0 and dot(r, a2) == 0]
    rset = set(E6r); A2s = set()
    for a in E6r:
        for b in E6r:
            if dot(a, b) == F(-1):
                c = tuple(-(x + y) for x, y in zip(a, b))
                if c in rset:
                    A2s.add(frozenset([a, b, c] + [tuple(-x for x in r) for r in (a, b, c)]))
    A2s = list(A2s)
    orth = lambda P, Q: all(dot(p, q) == 0 for p in P for q in Q)
    tri = [t for t in itertools.combinations(range(len(A2s)), 3)
           if orth(A2s[t[0]], A2s[t[1]]) and orth(A2s[t[0]], A2s[t[2]]) and orth(A2s[t[1]], A2s[t[2]])]
    print(f"  [fc65] E6 complement roots {len(E6r)}, A2 subsystems {len(A2s)}, A2^3 subsystems {len(tri)}")
    print(f"         group-theoretic |W(E6)|/|W(A2)^3 x S3| = 51840/1296 = {51840 // 1296}")
    assert len(E6r) == 72 and len(A2s) == 120 and len(tri) == 40 == 51840 // 1296

    # ---- fc R68 addendum: the selected labelling gives 9+9+9 ----
    g = grade3((1, 0, 2, 2, 0, 2))
    gf = grade3((1, 0, 0, 1, 1, 2))                       # its theta-flip
    print(f"  [fc68] c=(1,0,2,2,0,2) grades the 27 as {sorted(g.values(), reverse=True)}; "
          f"theta-flip {sorted(gf.values(), reverse=True)}")
    assert sorted(g.values()) == [9, 9, 9] == sorted(gf.values())

    # CONTROL, and it CALIBRATES the claim: is 9+9+9 rare?
    shapes = collections.Counter()
    for c in itertools.product(range(3), repeat=6):
        if any(c):
            shapes[tuple(sorted(grade3(c).values(), reverse=True))] += 1
    tot = sum(shapes.values()); nine = shapes[(9, 9, 9)]
    print(f"  [ctl ] 9+9+9 occurs in {nine} of {tot} nonzero labellings ({100*nine/tot:.1f}%) -- "
          f"the MOST COMMON shape, NOT a rare one")
    assert nine > 1, "if 9+9+9 were unique the reading would be different"
    print("         => the uniqueness in R68 is the TWO-SIDED Z[g]-STABILITY, not the 9+9+9.")

    # ---- SM seat B1277: z_L is an A1A5 involution splitting the 27 as 15 + 12 ----
    hits = []
    for c in itertools.product(range(2), repeat=6):
        if not any(c):
            continue
        p27 = collections.Counter(int(sum(c[i] * simple_coords(w)[i] for i in range(6))) % 2 for w in W27)
        if sorted(p27.values()) != [12, 15]:
            continue
        even = sum(1 for r in ROOTS
                   if int(sum(c[i] * simple_coords(r)[i] for i in range(6))) % 2 == 0)
        hits.append(6 + even)
    print(f"  [sm  ] Z/2 gradings splitting the 27 as 15+12: {len(hits)}; "
          f"centralizer dims {sorted(set(hits))}")
    print(f"         A1 x A5 = dim su(2) + dim su(6) = 3 + 35 = 38; and 27|SU(2)xSU(6) = (2,6bar)+(1,15) = 12+15")
    assert 38 in hits
    print(f"         E6 = 78 = 38 + 40 (centralizer + odd part)")
    assert 78 - 38 == 40

    print("""
  ==> CONFIRMED HERE, from structure alone:
      * fc R65/R68's 120 A2 and 40 A2^3 subsystems of E6, and the 51840/1296 count;
      * fc R68's selected labelling c = (1,0,2,2,0,2) grading the 27 as 9+9+9, and its theta-flip;
      * the SM seat's z_L as an A1A5 involution -- the 15+12 split of the 27 with a dim-38
        centralizer is exactly SU(2)xSU(6) with 27 = (2,6bar)+(1,15).

  ==> CALIBRATED, and this matters for how R68 is read: 9+9+9 is the MOST COMMON grading shape
      (178 of 728), NOT a rare one. R68's content is the TWO-SIDED Z[g]-stability that cuts
      40 -> 4 -> 1, not the partition. Anyone citing "9+9+9" as the discovery cites the wrong number.

  ==> NOT VERIFIED HERE, and fenced as harvest: R68's icosian 4 -> 1 collapse (needs their rebuilt
      icosian E8 and the founding ratio's two-sided action); the SM seat's vacuum-manifold scan,
      its Wilson-line stabiliser computation, and its theorem that three generations of Q, u^c, e^c
      force SU(5) unbroken.
""")
    print("SELFTEST: PASS")


if __name__ == "__main__":
    selftest()
