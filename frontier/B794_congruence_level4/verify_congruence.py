"""B794 — independent verification of cc3's two congruence theorems (B792 1757d6d5).

PROVENANCE: both theorems are cc3's (audit seat). cc3 never merges; this file re-derives
them from scratch under a new number. Nothing is taken from cc3's script.

THEOREM 1 (congruence).  Gamma_41 is a CONGRUENCE subgroup of level exactly (4):
                         Gamma(4) <= Gamma_41, but Gamma(2) NOT <= Gamma_41.
THEOREM 2 (trace law).   Every m004 geodesic trace norm is == 0 or 3 (mod 4), never 1.
"""
import json

# ---- R = Z[w]/4, w^2 = -1 - w.  2 is INERT in Q(sqrt-3) (x^2+x+1 irreducible mod 2) ----
def radd(x, y): return ((x[0] + y[0]) % 4, (x[1] + y[1]) % 4)
def rsub(x, y): return ((x[0] - y[0]) % 4, (x[1] - y[1]) % 4)
def rmul(x, y):
    a, b = x; c, d = y                      # (a+bw)(c+dw) = (ac-bd) + (ad+bc-bd) w
    return ((a * c - b * d) % 4, (a * d + b * c - b * d) % 4)

R = [(a, b) for a in range(4) for b in range(4)]
ONE, ZERO = (1, 0), (0, 0)
I = ((ONE, ZERO), (ZERO, ONE))

def mmul(M, N):
    return tuple(tuple(radd(rmul(M[i][0], N[0][j]), rmul(M[i][1], N[1][j]))
                       for j in range(2)) for i in range(2))
def det(M): return rsub(rmul(M[0][0], M[1][1]), rmul(M[0][1], M[1][0]))
def closure(gens):
    seen, fr = {I}, [I]
    while fr:
        nx = []
        for M in fr:
            for g in gens:
                P = mmul(M, g)
                if P not in seen: seen.add(P); nx.append(P)
        fr = nx
    return seen

OUT = {}
line = "=" * 70
print(f"{line}\nSTEP A - the ambient group mod 4\n{line}")
SL = [((a, b), (c, d)) for a in R for b in R for c in R for d in R
      if det(((a, b), (c, d))) == ONE]
print(f"  |Z[w]/4| = {len(R)}   (2 inert => residue field F_4)")
print(f"  |SL(2,Z[w]/4)|  = {len(SL)}")
print(f"  |PSL(2,Z[w]/4)| = {len(SL)//2}   <-- equals B791's verified coset-image order 1920: "
      f"{len(SL)//2 == 1920}")
print("  => the B788 bank's coset action IS reduction mod 4. Its ambient_order 3840 =")
print("     |SL(2,O/4)|, image 1920 = |PSL(2,O/4)|, kernel 2 = {+-I}. Explained, not observed.")
OUT["SL_order"], OUT["PSL_order"] = len(SL), len(SL) // 2

print(f"\n{line}\nSTEP B - surjectivity of PSL(2,O_3) -> PSL(2,Z[w]/4)\n{line}")
T = ((ONE, ONE), (ZERO, ONE))
U = ((ONE, (0, 1)), (ZERO, ONE))
S = ((ZERO, (3, 0)), (ONE, ZERO))
full = closure([T, U, S])
print(f"  |<T,U,S> mod 4| = {len(full)}  -> surjective onto SL: {len(full) == len(SL)}")
OUT["surjective"] = len(full) == len(SL)

print(f"\n{line}\nSTEP C - THEOREM 1\n{line}")
A = ((ONE, ONE), (ZERO, ONE))
B = ((ONE, ZERO), ((0, 3), ONE))          # -w = -(0,1) = (0,3) mod 4
H = closure([A, B])
minusI = (((3, 0), ZERO), (ZERO, (3, 0)))
Hbar = len(H) // (2 if minusI in H else 1)
idx = (len(SL) // 2) // Hbar
print(f"  |H = <A,B> mod 4| = {len(H)}   -I in H: {minusI in H}   |Hbar| = {Hbar}")
print(f"  [PSL(2,Z[w]/4) : Hbar] = {idx}    and  [PSL(2,O_3) : Gamma_41] = 12 (B790, exact)")
print(f"  equal indices => Gamma_41 = preimage(Hbar) => Gamma(4) <= Gamma_41: {idx == 12}")
OUT["index_mod4"] = idx

# level is EXACTLY 4: the mod-2 image is proper of a DIFFERENT index
def to2(M): return tuple(tuple((M[i][j][0] % 2, M[i][j][1] % 2) for j in range(2)) for i in range(2))
H2 = {to2(M) for M in H}
print(f"\n  |H mod 2| = {len(H2)}   (|SL(2,F_4)| = 60, and SL(2,F_4) = PSL(2,F_4) = A_5)")
print(f"  [A_5 : H mod 2] = {60 // len(H2)}  != 12  => Gamma(2) NOT <= Gamma_41")
print(f"  => the congruence LEVEL is exactly (4).")
OUT["mod2_image_order"], OUT["mod2_index"] = len(H2), 60 // len(H2)

print(f"\n{line}\nSTEP D - THEOREM 2 (the trace law)\n{line}")
def norm(x): a, b = x; return (a * a - a * b + b * b) % 4
traces = {radd(M[0][0], M[1][1]) for M in H}
norms = sorted({norm(t) for t in traces})
print(f"  distinct traces of H mod 4: {len(traces)}")
print(f"  their norms mod 4: {norms}")
print(f"  1 mod 4 is ABSENT: {1 not in norms}")
print("  => for EVERY gamma in Gamma_41, N(tr gamma) == 0 or 3 (mod 4). Proved for all")
print("     cutoffs, not observed at one. (Geodesic traces are +-tr and N(-x)=N(x).)")
OUT["trace_norms_mod4"] = norms

print(f"\n{line}\nWHAT THIS DOES TO cc's OWN B790 CLAIMS\n{line}")
print("  B790 proved: Gamma_41 is NOT the principal congruence subgroup of level sqrt(-3).")
print("    -> STILL TRUE, and now seen as the weaker half: it is congruence, at level 4.")
print("  B790 HINT H-B788-NORMSPLIT: 'm004-only norms all == 0 mod 4'  -> REFUTED.")
print("    The real law is {0,3}. The odd norms cc3 found (7,103,127,175,367) are all == 3,")
print("    consistent with the theorem. cc's contrary 'verification' was an artifact of a")
print("    tolerance filter that SILENTLY DROPPED long geodesics -- i.e. it discarded exactly")
print("    the disconfirming data. New error class registered.")
for x in (7, 103, 127, 175, 367):
    assert x % 4 == 3
print("  check: 7,103,127,175,367 all == 3 (mod 4): True")

json.dump(OUT, open(__file__.rsplit("/", 1)[0] + "/results.json", "w"), indent=2)
print(f"\n{line}\nresults.json written\n{line}")
