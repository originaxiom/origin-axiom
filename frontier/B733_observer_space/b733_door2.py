#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B733 PROBE 1 -- the observer-space at DOOR 2 (A5), fully.

G_2 = PSL(2, O_3/(2)) = PSL(2, F4) = A5 (order 60).
c_2 = B701 conjugation = (w -> w^2) = F4-Frobenius mod 2 = the field automorphism.
Claim (B732): c_2 = Out(A5) = Z/2.

This script COMPUTES (not cites; E19 COMPUTE-NOT-CITE) the FULL observer-space at door 2:
 (a) the class-swap table of c_2 (which conjugacy classes swap vs fix),
 (b) the irrep-swap table of c_2 (via the full character table, computed by Burnside's
     class-sum eigenvalue method) -- confirm the two 3-dim irreps live over Q(sqrt5)=HEARING
     and are SWAPPED by c_2; the 1,4,5-dim irreps are FIXED,
 (c) the being<->hearing coupling: the SINGLE Out(A5)=Z/2 bit (from BEING=Q(sqrt-3)'s
     Frobenius) SIMULTANEOUSLY orients the hearing structure (the two Q(sqrt5) 3-irreps) --
     i.e. c_2 acts non-trivially on BOTH, so being-conjugation LOCKS to hearing-swap in one Z/2,
 (d) the observer-space dimension = dim_{F2} Out(A5) = 1 bit.

Everything in-sandbox; F4 = O_3/(2) with w^2 = w+1 (char 2, since -w-1 == w+1 mod 2).
"""

import itertools
import numpy as np

OUT = []
def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    OUT.append(s)

# ---------------------------------------------------------------------------
# F4 = O_3/(2).  Represent x = a + b*w, a,b in F2, encoded as int  x = a | (b<<1).
#   0 -> (0,0)=0,  1 -> (1,0)=1,  w -> (0,1)=2,  1+w -> (1,1)=3.
#   w^2 = w + 1  (in F2: -w-1 = w+1).
# ---------------------------------------------------------------------------
def bits(x):        # x -> (a,b)
    return (x & 1, (x >> 1) & 1)

def fadd(x, y):     # componentwise mod 2  == XOR
    return x ^ y

def fmul(x, y):
    a, b = bits(x); c, d = bits(y)
    r0 = (a*c + b*d) & 1                 # constant term (uses w^2 -> +1 for b*d)
    r1 = (a*d + b*c + b*d) & 1           # w-coefficient  (uses w^2 -> +w for b*d)
    return r0 | (r1 << 1)

def ffrob(x):       # Frobenius x -> x^2
    return fmul(x, x)

F4 = [0, 1, 2, 3]
NAMES = {0: "0", 1: "1", 2: "w", 3: "1+w"}

# sanity: field axioms + Frobenius = the nontrivial Galois generator swapping w<->1+w
assert sorted(ffrob(x) for x in F4) == [0, 1, 2, 3]          # bijection
assert ffrob(0) == 0 and ffrob(1) == 1                      # fixes F2
assert ffrob(2) == 3 and ffrob(3) == 2                      # swaps w <-> 1+w
assert all(fmul(x, y) == fmul(y, x) for x in F4 for y in F4)
# Frobenius is a field automorphism:
assert all(ffrob(fmul(x, y)) == fmul(ffrob(x), ffrob(y)) for x in F4 for y in F4)
assert all(ffrob(fadd(x, y)) == fadd(ffrob(x), ffrob(y)) for x in F4 for y in F4)

# ---------------------------------------------------------------------------
# SL(2,F4) = PSL(2,F4) = A5  (char 2: center of SL is trivial, so PSL=SL=PGL).
# Matrix M = (a,b,c,d) for [[a,b],[c,d]], det = a d + b c (char 2) = 1.
# ---------------------------------------------------------------------------
def mdet(M):
    a, b, c, d = M
    return fadd(fmul(a, d), fmul(b, c))

def mmul(M, N):
    a, b, c, d = M; e, f, g, h = N
    return (fadd(fmul(a, e), fmul(b, g)),
            fadd(fmul(a, f), fmul(b, h)),
            fadd(fmul(c, e), fmul(d, g)),
            fadd(fmul(c, f), fmul(d, h)))

def mfrob(M):                                   # apply F4-Frobenius entrywise  = c_2
    return tuple(ffrob(x) for x in M)

G = [M for M in itertools.product(F4, repeat=4) if mdet(M) == 1]
IDX = {M: i for i, M in enumerate(G)}
N = len(G)
ID = (1, 0, 0, 1)

log("=" * 78)
log("B733 PROBE 1 -- observer-space at DOOR 2 (A5 = PSL(2,F4) = PSL(2,O_3/(2)))")
log("=" * 78)
log(f"|G| = |SL(2,F4)| = {N}   (expected 60; char 2 => PSL=SL=PGL, center trivial)")
assert N == 60

# element order
def morder(M):
    P, k = M, 1
    while P != ID:
        P = mmul(P, M); k += 1
    return k

# trace of a matrix (F4 element) -- distinguishes 5A/5B
def mtrace(M):
    a, b, c, d = M
    return fadd(a, d)

# ---------------------------------------------------------------------------
# Conjugacy classes.
# ---------------------------------------------------------------------------
def minv(M):
    # det=1 => inverse of [[a,b],[c,d]] is [[d,b],[c,a]] (char 2, -1=1)
    a, b, c, d = M
    return (d, b, c, a)

# verify inverse
assert all(mmul(M, minv(M)) == ID for M in G)

seen = [False] * N
classes = []          # list of frozensets of indices
for i, M in enumerate(G):
    if seen[i]:
        continue
    orb = set()
    for X in G:
        c = mmul(mmul(X, M), minv(X))
        orb.add(IDX[c])
    for j in orb:
        seen[j] = True
    classes.append(frozenset(orb))

classes.sort(key=lambda s: (morder(G[min(s)]), len(s), min(s)))
CLASS_OF = {}
for ci, s in enumerate(classes):
    for j in s:
        CLASS_OF[j] = ci
reps = [G[min(s)] for s in classes]
sizes = [len(s) for s in classes]
orders = [morder(r) for r in reps]

log("")
log("(0) CONJUGACY CLASSES of A5:")
log(f"    #classes = {len(classes)}  (expected 5)")
log("    idx  order  size  rep-trace   label")
labels = []
for ci in range(len(classes)):
    o, sz, tr = orders[ci], sizes[ci], mtrace(reps[ci])
    if o == 1:   lab = "1  (id)"
    elif o == 2: lab = "2A (double-transposition)"
    elif o == 3: lab = "3A (3-cycle)"
    elif o == 5: lab = "5A" if tr == 2 else "5B"   # trace w vs 1+w (B732)
    else:        lab = "?"
    labels.append(lab)
    log(f"    {ci:>3}  {o:>5}  {sz:>4}   {NAMES[tr]:>6}     {lab}")
assert sorted(sizes) == [1, 12, 12, 15, 20]
assert sorted(orders) == [1, 2, 3, 5, 5]

# identify the two order-5 classes
five_classes = [ci for ci in range(len(classes)) if orders[ci] == 5]
assert len(five_classes) == 2

# ---------------------------------------------------------------------------
# (a) c_2 = Frobenius : is it an automorphism?  which classes does it swap / fix?
# ---------------------------------------------------------------------------
log("")
log("(a) c_2 = F4-Frobenius (w -> w^2) acting on A5:")

# c_2 maps G -> G (det preserved) and is a bijection
assert all(mfrob(M) in IDX for M in G)
assert len({mfrob(M) for M in G}) == N
# homomorphism (checked on ALL 3600 ordered pairs)
assert all(mfrob(mmul(M, K)) == mmul(mfrob(M), mfrob(K)) for M in G for K in G)
# order 2 as a map (Frob^2 = id on F4)
assert all(mfrob(mfrob(M)) == M for M in G)
log("    c_2 is a bijective homomorphism G->G, of order 2  (VERIFIED on all pairs).")

# class permutation induced by c_2
class_perm = []
for ci in range(len(classes)):
    img = CLASS_OF[IDX[mfrob(reps[ci])]]
    class_perm.append(img)
log("    class permutation induced by c_2:")
for ci in range(len(classes)):
    tag = "FIX" if class_perm[ci] == ci else f"SWAP-> {labels[class_perm[ci]]}"
    log(f"       {labels[ci]:<28} -> {labels[class_perm[ci]]:<28} [{tag}]")

fixed_classes  = [ci for ci in range(len(classes)) if class_perm[ci] == ci]
moved_classes  = [ci for ci in range(len(classes)) if class_perm[ci] != ci]
# c_2 must swap exactly the two order-5 classes, fix 1,2,3
assert set(moved_classes) == set(five_classes)
assert class_perm[five_classes[0]] == five_classes[1]
assert class_perm[five_classes[1]] == five_classes[0]
log("    => c_2 SWAPS the two order-5 classes (5A<->5B) and FIXES {1, 2A, 3A}.")
log("    => an INNER automorphism preserves every conjugacy class; c_2 moves 5A/5B,")
log("       so c_2 is OUTER.  Out(A5)=Z/2 (field automorphism) => c_2 GENERATES it.")

# ---------------------------------------------------------------------------
# Full CHARACTER TABLE of A5 by Burnside's class-sum eigenvalue method (COMPUTED).
#   Class algebra structure constants a_{ijk}:  K_i K_j = sum_k a_{ijk} K_k.
#   a_{ijk} = #{ x in C_i : x^{-1} z_k in C_j },  z_k a fixed rep of C_k.
#   Central chars omega satisfy  A_i omega = omega(K_i) omega, (A_i)_{jk}=a_{ijk};
#   the A_i commute -> common eigenvectors -> all central chars -> characters.
# ---------------------------------------------------------------------------
nc = len(classes)
class_elems = [list(s) for s in classes]

A = np.zeros((nc, nc, nc))     # A[i][j][k] = a_{ijk}
for k in range(nc):
    zk = reps[k]
    zk_inv_targets = {}
    # for each x in C_i, need class of x^{-1} z_k
    for i in range(nc):
        cnt = [0] * nc
        for xi in class_elems[i]:
            x = G[xi]
            prod = mmul(minv(x), zk)         # x^{-1} z_k
            cnt[CLASS_OF[IDX[prod]]] += 1
        for j in range(nc):
            A[i][j][k] = cnt[j]

# random real combination of the commuting A_i -> simple spectrum -> eigenvectors
rng = np.random.default_rng(20260720)
M_comb = sum(rng.normal() * A[i] for i in range(nc))
evals, evecs = np.linalg.eig(M_comb)
# eigenvectors should be common eigenvectors of all A_i (real central chars)
id_class = orders.index(1)     # class index of identity

char_rows = []
for t in range(nc):
    omega = evecs[:, t].real.copy()
    # normalize so identity-class component = 1  (omega(id)=chi(1)/chi(1)=1)
    omega = omega / omega[id_class]
    # chi(1) = sqrt(|G| / sum_k |omega_k|^2 / |C_k|)
    denom = sum(abs(omega[k])**2 / sizes[k] for k in range(nc))
    chi1 = np.sqrt(N / denom)
    chi = np.array([chi1 * omega[k] / sizes[k] for k in range(nc)])
    char_rows.append(chi.real)

# sort rows by degree
char_rows.sort(key=lambda r: round(r[id_class], 6))
char = np.array(char_rows)

def approx(x):
    # recognize small integers and (1 +/- sqrt5)/2
    phi  = (1 + np.sqrt(5)) / 2
    phib = (1 - np.sqrt(5)) / 2
    for val, name in [(phi, "(1+v5)/2"), (phib, "(1-v5)/2")]:
        if abs(x - val) < 1e-6:
            return name
    if abs(x - round(x)) < 1e-6:
        return str(int(round(x)))
    return f"{x:.4f}"

log("")
log("(b) CHARACTER TABLE of A5 (computed by Burnside class-sum eigenvalues):")
header = "     dim  |  " + "  ".join(f"{labels[ci].split()[0]:>8}" for ci in range(nc))
log(header)
deg_list = []
for r in char:
    deg = int(round(r[id_class]))
    deg_list.append(deg)
    row = f"     {deg:>3}  |  " + "  ".join(f"{approx(r[ci]):>8}" for ci in range(nc))
    log(row)
assert sorted(deg_list) == [1, 3, 3, 4, 5], f"degrees {deg_list}"

# verify orthonormality of the computed table (row orthogonality)
Wt = np.array(sizes) / N
for a_ in range(nc):
    for b_ in range(nc):
        ip = sum(Wt[k] * char[a_][k] * char[b_][k] for k in range(nc))
        assert abs(ip - (1.0 if a_ == b_ else 0.0)) < 1e-6, (a_, b_, ip)
log("    (row-orthonormality of the computed table VERIFIED to 1e-6.)")

# ---------------------------------------------------------------------------
# irrep permutation induced by c_2:  chi -> chi o c_2, i.e. permute the class
# columns by class_perm and see which irrep row it becomes.
# ---------------------------------------------------------------------------
log("")
log("    irrep permutation induced by c_2  (chi |-> chi o c_2 = columns permuted by 5A<->5B):")
irrep_perm = []
for a_ in range(nc):
    permuted = np.array([char[a_][class_perm[k]] for k in range(nc)])
    # find matching row
    match = None
    for b_ in range(nc):
        if np.allclose(permuted, char[b_], atol=1e-6):
            match = b_; break
    assert match is not None
    irrep_perm.append(match)
    tag = "FIX" if match == a_ else "SWAP"
    log(f"       chi_{deg_list[a_]}  (row {a_})  ->  chi_{deg_list[match]}  (row {match})   [{tag}]")

# which rows are the two 3-dim irreps?
three_rows = [i for i in range(nc) if deg_list[i] == 3]
assert len(three_rows) == 2
r3a, r3b = three_rows
# c_2 must swap them, and fix 1,4,5
assert irrep_perm[r3a] == r3b and irrep_perm[r3b] == r3a, "3-dim irreps not swapped!"
for i in range(nc):
    if deg_list[i] in (1, 4, 5):
        assert irrep_perm[i] == i, f"chi_{deg_list[i]} not fixed!"

# confirm the two 3-dim irreps carry Q(sqrt5) exactly on the two order-5 classes
log("")
log("    the two 3-dim irreps on the order-5 classes (5A,5B):")
for i in three_rows:
    vals = "  ".join(f"{labels[ci].split()[0]}={approx(char[i][ci])}" for ci in five_classes)
    log(f"       chi_3 (row {i}):  {vals}")
# check the values are exactly {(1+v5)/2, (1-v5)/2} split
phi  = (1 + np.sqrt(5)) / 2
phib = (1 - np.sqrt(5)) / 2
vA = sorted(char[r3a][ci] for ci in five_classes)
assert abs(min(vA) - phib) < 1e-6 and abs(max(vA) - phi) < 1e-6
log("    => the two 3-dim irreps are Gal(Q(sqrt5)/Q)-CONJUGATE (char = (1+-sqrt5)/2 on 5-cycles),")
log("        file over Q(sqrt5) = HEARING, and c_2 SWAPS them.  chi_1,chi_4,chi_5 are FIXED.")

# ---------------------------------------------------------------------------
# (c) THE BEING<->HEARING COUPLING.
# ---------------------------------------------------------------------------
log("")
log("(c) BEING <-> HEARING COUPLING (the key structural finding):")
log("    - the ONE nontrivial element c_2 of Out(A5)=Z/2 comes from BEING = Q(sqrt-3):")
log("      it is the Frobenius w->w^2 of O_3/(2)=F4, i.e. Gal(Q(sqrt-3) locally) mod 2.")
log("    - c_2 acts NON-TRIVIALLY on the BEING side (swaps the two order-5 classes 5A/5B), AND")
log("    - c_2 acts NON-TRIVIALLY on the HEARING side (swaps the two Q(sqrt5) 3-dim irreps).")
being_nontrivial   = (len(moved_classes) > 0)
hearing_nontrivial = (irrep_perm[r3a] != r3a)
log(f"      being-side nontrivial:   {being_nontrivial}   (5A/5B swapped)")
log(f"      hearing-side nontrivial: {hearing_nontrivial}   (the two 3-irreps swapped)")
log("    - Out(A5) has ORDER 2: there is exactly ONE nontrivial swap-bit. Since it moves BOTH")
log("      the being-structure and the hearing-structure, the two orientations CANNOT be chosen")
log("      independently -- they are LOCKED to the single bit. (If Out were (Z/2)^2 they could be")
log("      independent; being Z/2 forces the lock, and the lock is non-vacuous because c_2 fixes")
log("      NEITHER side -- it genuinely orients both at once.)")
assert being_nontrivial and hearing_nontrivial
log("    => the single observer bit at door 2 SIMULTANEOUSLY orients being (Q(sqrt-3)) and")
log("       hearing (Q(sqrt5)).  being . hearing meet in the one Z/2.")

# ---------------------------------------------------------------------------
# ADVERSARIAL VERIFICATION (3-skeptic).
# ---------------------------------------------------------------------------
log("")
log("--- adversarial verification ---")

# Skeptic 1: "the being-swap and hearing-swap could be independent accidents."
# NO: chi -> chi o c_2 is DETERMINED by the class permutation. The two 3-irreps are the
# UNIQUE irreps whose values differ on 5A vs 5B; so ANY automorphism swapping 5A/5B is
# FORCED to swap {chi_3, chi_3'} and to fix every irrep constant on {5A,5B}. Verify that
# the 3-irreps are exactly the irreps that separate 5A from 5B:
separates = [i for i in range(nc) if abs(char[i][five_classes[0]] - char[i][five_classes[1]]) > 1e-6]
assert set(separates) == set(three_rows), separates
log("  [S1] the two 3-irreps are the UNIQUE irreps separating 5A from 5B => the being-swap")
log("       (on classes) MECHANICALLY forces the hearing-swap (on irreps) via chi|->chi o c_2.")
log("       The coupling is FORCED, not coincidental.")

# Skeptic 2: "maybe Out(A5) is bigger than Z/2, so the bit-count is > 1."
# Compute |Aut(A5)| in-sandbox by counting automorphisms (word-map consistency BFS from a
# fixed generating pair), then |Out| = |Aut|/|Inn|, |Inn| = |A5| (A5 centerless).
def find_generating_pair():
    for i in range(N):
        if morder(G[i]) != 5:
            continue
        for j in range(N):
            if morder(G[j]) != 2:
                continue
            # BFS closure of <G[i],G[j]>
            gens = [G[i], G[j]]
            seen_c = {ID}
            frontier = [ID]
            while frontier:
                x = frontier.pop()
                for g in gens:
                    y = mmul(x, g)
                    if y not in seen_c:
                        seen_c.add(y); frontier.append(y)
            if len(seen_c) == N:
                return G[i], G[j]
    return None
a_gen, b_gen = find_generating_pair()

def is_automorphism(a2, b2):
    # define map by right-mult BFS from ID; img[ID]=ID; check consistency on every edge.
    img = {ID: ID}
    frontier = [ID]
    while frontier:
        x = frontier.pop()
        ix = img[x]
        for g, g2 in ((a_gen, a2), (b_gen, b2)):
            y = mmul(x, g)
            iy = mmul(ix, g2)
            if y in img:
                if img[y] != iy:
                    return False           # not well-defined => not a homomorphism
            else:
                img[y] = iy; frontier.append(y)
    return len(set(img.values())) == N     # bijective => automorphism

aut_count = 0
for i in range(N):
    for j in range(N):
        if is_automorphism(G[i], G[j]):
            aut_count += 1
inn = N                                     # |Inn(A5)| = |A5/Z(A5)| = 60 (centerless)
assert G[0]  # keep linter quiet
out_order = aut_count // inn
log(f"  [S2] |Aut(A5)| = {aut_count} (computed in-sandbox), |Inn(A5)| = {inn} (A5 centerless),")
log(f"       => |Out(A5)| = {aut_count}//{inn} = {out_order}.  Out(A5) is EXACTLY Z/2.")
assert aut_count == 120 and out_order == 2
log("       So <c_2> = Out(A5) fully; there is NO further outer bit at door 2. bit-count = 1 EXACT.")

# Skeptic 3: "the Q(sqrt5) reading might be spurious (base rate)."
# The 3-irrep values on 5A/5B are the EXACT algebraic numbers (1+-sqrt5)/2, not a numerical
# near-match; and Q(sqrt5) is forced (A5=PSL(2,5); the 5-cycle character field is Q(zeta5)^+
# = Q(sqrt5)). Confirmed exactly above (|val - (1+-sqrt5)/2| < 1e-6, and they are the roots
# of x^2 - x - 1, a genuine quadratic irrationality -- not a coincidence).
disc_ok = abs((char[r3a][five_classes[0]]**2 - char[r3a][five_classes[0]] - 1)) < 1e-6
assert disc_ok
log("  [S3] the 3-irrep 5-cycle value satisfies x^2 - x - 1 = 0 EXACTLY (golden, Q(sqrt5)) --")
log("       an exact quadratic irrationality, not a small-group numerical coincidence (E20 clear).")

# ---------------------------------------------------------------------------
# (d) OBSERVER-SPACE DIMENSION = bit-count.
# ---------------------------------------------------------------------------
log("")
log("(d) OBSERVER-SPACE at door 2 = torsor of c_2-symmetry-breakings:")
log("    the arithmetic outer-symmetry is <c_2> = Out(A5) = Z/2  (|Out|=2 computed above).")
log("    an observer = a section = a choice of a side of Out(A5) = ONE binary swap-choice.")
log("    observer-space = Z/2 torsor => dim_{F2} = 1 bit.  (BOUNDED, small.)")
bit_count = 1

# ---------------------------------------------------------------------------
# VERDICT
# ---------------------------------------------------------------------------
log("")
log("=" * 78)
log("VERDICT (door 2):")
log("  swap table:  c_2 SWAPS {5A<->5B} and {chi_3 <-> chi_3'}; FIXES {1,2A,3A} and {chi_1,chi_4,chi_5}.")
log("  being<->hearing: the SINGLE Out(A5)=Z/2 bit couples the being-swap (5A/5B, Q(sqrt-3)-Frobenius)")
log("                   to the hearing-swap (the two Q(sqrt5) 3-irreps) -- both nontrivial, one bit.")
log("  bit-count:   1 bit.")
log("  OUTCOME A: a SMALL BOUNDED F2-structure -- exactly 1 observer bit at door 2, coupling")
log("             being & hearing.  NOT larger/unbounded.")
log("=" * 78)

# write output file
with open(__file__.rsplit("/", 1)[0] + "/b733_door2_out.txt", "w") as f:
    f.write("\n".join(OUT) + "\n")
