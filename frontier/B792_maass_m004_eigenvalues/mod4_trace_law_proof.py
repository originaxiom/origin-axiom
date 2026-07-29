r"""PROOF of the mod-4 trace law: Gamma_41 is congruence of level (4).

The observed law (trace_norm_split.py, cutoff 6.0): every m004 geodesic
trace norm is == 0 or 3 (mod 4), never 1. Here it is PROVED by finite
computation, via the stronger structural statement:

  THEOREM 1 (congruence).  Gamma_41 = ker-preimage of an index-12
  subgroup Hbar <= SL(2, Z[w]/4)/{+-I}  (E21 guard: the TRUE
  PSL(2,Z[w]/4) has center order 4 and order 960; the index-12
  argument runs in SL/{+-I}, order 1920 — chat1's catch 2026-07-29).  In particular Gamma(4) <= Gamma_41:
  the figure-eight knot group IS a congruence subgroup, of level (2)^2.
  (B790 established it is NOT principal congruence; this pins the
  actual congruence structure. B791's coset-image order 1920 is
  explained: 1920 = |SL(2, Z[w]/4)/{+-I}|.)

  THEOREM 2 (trace law).  {N(tr gamma) mod 4 : gamma in Gamma_41}
  is contained in {0, 3}.  Every m004 geodesic trace norm is == 0 or
  3 mod 4 — at EVERY cutoff, not just 6.0.

Proof method, all in-sandbox, no citations:
  (a) BFS the subgroup H = <A, B> mod 4 inside SL(2, Z[w]/4).
  (b) BFS the full group from the Bianchi generators
      T = [[1,1],[0,1]], U = [[1,w],[0,1]], S = [[0,-1],[1,0]]
      mod 4; if that closure has order 3840 = |SL(2, Z[w]/4)|, the
      reduction PSL(2,O3) -> SL(2, Z[w]/4)/{+-I} is SURJECTIVE
      (verified, not cited).
  (c) If [SL(2,Z[w]/4)/{+-I} : Hbar] = 12 = [PSL(2,O3) : Gamma_41], then
      Gamma_41 <= preimage(Hbar), both index 12, hence EQUAL, hence
      Gamma_41 >= Gamma(4).  Theorem 1.
  (d) Enumerate traces of H; norms mod 4.  Theorem 2 (the trace of any
      gamma in Gamma_41 mod 4 is the trace of its image in H; the norm
      mod 4 of a + bw depends only on (a,b) mod 4; geodesic traces are
      +-tr(gamma) and N(-x) = N(x)).

Gate 5-Q.
"""
from itertools import product

# ---- the ring R = Z[w]/4, elements (a, b) = a + b w, w^2 = -1 - w ----

def radd(x, y):
    return ((x[0] + y[0]) % 4, (x[1] + y[1]) % 4)


def rmul(x, y):
    a, b = x
    c, d = y
    return ((a * c - b * d) % 4, (a * d + b * c - b * d) % 4)


def rneg(x):
    return ((-x[0]) % 4, (-x[1]) % 4)


ZERO, ONE = (0, 0), (1, 0)
W = (0, 1)


def mmul(M, N):
    (a, b), (c, d) = M[0], M[1]
    (e, f), (g, h) = N[0], N[1]
    return (
        (radd(rmul(a, e), rmul(b, g)), radd(rmul(a, f), rmul(b, h))),
        (radd(rmul(c, e), rmul(d, g)), radd(rmul(c, f), rmul(d, h))),
    )


def bfs(gens):
    seen = set(gens)
    frontier = list(gens)
    while frontier:
        nxt = []
        for M in frontier:
            for g in gens:
                P = mmul(M, g)
                if P not in seen:
                    seen.add(P)
                    nxt.append(P)
        frontier = nxt
    return seen


def mat(rows):
    return tuple(tuple(r) for r in rows)


# ---- generators mod 4 ----
# Riley: A = [[1,1],[0,1]], B = [[1,0],[-w,1]]; inverses
A = mat([[ONE, ONE], [ZERO, ONE]])
Ai = mat([[ONE, (3, 0)], [ZERO, ONE]])
B = mat([[ONE, ZERO], [rneg(W), ONE]])
Bi = mat([[ONE, ZERO], [W, ONE]])

# Bianchi group generators: T, U (parabolic), S (inversion)
T = A
U = mat([[ONE, W], [ZERO, ONE]])
S = mat([[ZERO, rneg(ONE)], [ONE, ZERO]])
Ti, Ui = Ai, mat([[ONE, rneg(W)], [ZERO, ONE]])
Si = mat([[ZERO, ONE], [rneg(ONE), ZERO]])

print("=" * 72)
print("STEP (a): H = <A, B> mod 4")
print("=" * 72)
H = bfs([A, Ai, B, Bi])
print(f"  |H| = {len(H)}")
MINUS_I = mat([[(3, 0), ZERO], [ZERO, (3, 0)]])
has_minus = MINUS_I in H
print(f"  -I in H: {has_minus}")
Hbar = len(H) // (2 if has_minus else 1)
print(f"  |Hbar| in SL(2, Z[w]/4)/(+-I): {Hbar}")
print()

print("=" * 72)
print("STEP (b): full group from Bianchi generators mod 4 (surjectivity)")
print("=" * 72)
G = bfs([T, Ti, U, Ui, S, Si])
print(f"  |<T, U, S> mod 4| = {len(G)}  (|SL(2, Z[w]/4)| = 3840)")
surj = (len(G) == 3840)
print(f"  reduction PSL(2,O3) -> SL(2,Z[w]/4)/(+-I) surjective: {surj}")
print(f"  |SL(2, Z[w]/4)/{{+-I}}| = {len(G) // 2} "
      f"(= B791's coset-image order 1920: {len(G) // 2 == 1920})")
# E21 guard (chat1's catch, 2026-07-29): the FULL center of SL(2,Z[w]/4)
# is {lam*I : lam^2 = 1} = {+-1, +-(1+2w)}, ORDER 4 — so the true
# |PSL(2,Z[w]/4)| = 3840/4 = 960. The order-1920 group above is
# SL/{+-I}, an intermediate quotient; that is where the index-12
# congruence argument runs (PSL(2,O3) = SL(2,O3)/{+-I} maps to it
# naturally). In the true PSL the image index is 6 — the number from
# E21's original incident, dispositioned by E23 (name the convention).
cen = [(a, b) for a in range(4) for b in range(4)
       if rmul((a, b), (a, b)) == (1, 0)]
print(f"  E21 guard: |center(SL(2,Z[w]/4))| = {len(cen)} "
      f"(lam^2=1: {cen}); true |PSL| = {len(G) // len(cen)}")
print()

print("=" * 72)
print("STEP (c): the index, and Theorem 1")
print("=" * 72)
idx = (len(G) // 2) // Hbar
print(f"  [SL(2,Z[w]/4)/{{+-I}} : Hbar] = {len(G) // 2} / {Hbar} = {idx}")
print(f"  [PSL(2, O3) : Gamma_41] = 12 (B792 Step 2, exact)")
if surj and idx == 12:
    print()
    print("  Gamma_41 <= preimage(Hbar), and both have index 12 in")
    print("  PSL(2,O3)  =>  Gamma_41 = preimage(Hbar)  =>")
    print("  THEOREM 1: Gamma(4) <= Gamma_41. The figure-eight knot")
    print("  group is a CONGRUENCE subgroup of level (2)^2 = (4).")
else:
    print("  MISMATCH — Theorem 1 NOT established; investigate.")
print()

# level exactly 4, not 2: image of H mod 2
print("Level check mod 2: ", end="")


def red2(M):
    return tuple(tuple((x[0] % 2, x[1] % 2) for x in row) for row in M)


H2 = {red2(M) for M in H}
G2 = {red2(M) for M in G}
print(f"|H mod 2| = {len(H2)}, |SL(2,F4)| = {len(G2)}")
idx2 = len(G2) // len(H2)
print(f"  [PSL(2,F4) : H mod 2] = {idx2}  (PSL(2,F4) = SL(2,F4) ~ A5)")
if idx2 > 1:
    print(f"  The mod-2 image is PROPER (order {len(H2)} = D5 < A5), of")
    print(f"  index {idx2} != 12, so Gamma(2) is NOT contained in Gamma_41")
    print("  (else Gamma_41 would equal the index-6 mod-2 preimage).")
    print("  => the congruence LEVEL is exactly (4). Consistent with")
    print("  B790's 'not principal congruence' and B737's conductor-4 /")
    print("  disc -48 cusp structure. Note A5 = PSL(2,F4) appears with")
    print("  the dihedral D5 image — the 5A/5B structure of B787's")
    print("  ambivalence argument lives at the mod-2 level of Gamma_41.")
print()

print("=" * 72)
print("STEP (d): trace enumeration, and Theorem 2")
print("=" * 72)
traces = {radd(M[0][0], M[1][1]) for M in H}
norms = sorted({(a * a - a * b + b * b) % 4 for (a, b) in traces})
print(f"  distinct traces of H mod 4: {len(traces)}")
print(f"  their norms mod 4: {norms}")
if set(norms) <= {0, 3}:
    print()
    print("  THEOREM 2: for EVERY gamma in Gamma_41, N(tr gamma) mod 4")
    print("  is in {0, 3}. All m004 geodesic trace norms avoid 1 mod 4,")
    print("  at every cutoff. The observed cutoff-6 law is PROVED.")
else:
    print("  Norm class outside {0,3} appears — law NOT provable at")
    print("  level 4; the cutoff-6 observation would be accidental.")

print()
print("Cross-checks against observed data:")
print("  - trace 3+w: ", (3 * 3 - 3 * 1 + 1 * 1) % 4, "mod 4 (= 3, the")
print("    cutoff-6 'violation' of B790's law — consistent: 3 in {0,3})")
print("  - even traces: N == 0 mod 4 (2 inert) — the B790 cutoff-5 set")
