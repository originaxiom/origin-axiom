#!/usr/bin/env python3
"""MEMO-92 CELL: THE TWIST MEETS THE MIRROR — the beat parity of the
hierarchy carrier, computed exactly on the lane's 27.  Campaign THE
SECOND HALF, the census's closing instrument for candidate 4 (the
Hermitian gauge choice) — THE_FRAME_CENSUS.md's flagship.

BACKGROUND (banked): B928 characterizes the value arc's Hermitian twist
as an AFFINE SIGN CHARACTER on the 27's weights:
    D2tw = -(-1)^<a*, w>,  a* = s(chi_-)  [their coordinates: (1,0,1,0,1,1)]
with FLIP COUNT 11 (the "eleven-flip diagonal"; B916: no un-shifted
character matches — the affine polarity is essential).  The canonical
gauge is generation-degenerate ((x+3)^3, B923); the ENTIRE generation
hierarchy is carried by this one diagonal.  The census (candidate 4)
could not type the gauge choice: sigma_chi- is not c, but whether the
choice is priced to the observer column was undecided.  The record's
own decision instrument is the parity x dimension law (B1168): mirror-
even and dimensionless => object-canonical; mirror-odd => observer
column.  The lane's beat Omega = exp(rho27(q e)) o gal is the banked
carrier realization of the mirror/c-leg (memos 31-33, 46; B1174), so
BEAT PARITY = MIRROR PARITY, computable here and nowhere else (the main
corpus has no action of c on the 27 — wave-1 klein lane's finding).

COORDINATE-ROBUST DESIGN (cc's a* lives in their B883 basis; the lane
must not depend on their numbering): enumerate ALL 128 affine sign
diagonals D_{a,eps}(w) = eps*(-1)^<a,w> (a in F_2^6, eps = +-1) on the
lane's 27, in the lane's own weight coordinates.  The D2tw CLASS is
identified by its basis-independent signature: polarity eps = -1 with
FLIP COUNT 11 (B928/B916).  For every candidate in that class, decide
beat parity exactly: Omega D Omega^-1 = U D U^-1 (gal acts trivially
on a rational diagonal), so D is BEAT-EVEN iff U D = D U in the exact
pair field.  (Omega D Omega^-1 = -D is impossible: 27 is odd, traces
obstruct.)

TWO PARTS, PREREGISTERED:
  PART 1 (class survey, three-outcome A/B/C): every affine class with
     D2tw's banked signatures (polarity -1; 11 flips; flip weight-sums
     {-1 x2, 0 x7, +1 x2}) gets its beat parity; unanimity decides,
     a mixed table falls through to Part 2.
  PART 2 (the decisive transport): B916's results.json banks the flip
     set as ELEVEN EXPLICIT WEIGHT VECTORS (vendored below verbatim,
     with a* = (1,0,1,0,1,1), polarity -1, from B928's Q1a).  Transport
     them into the lane by coordinate permutation (+- global negation):
     assert the embedding exists, count the distinct transported flip
     sets, cross-check B928's affine-character formula end-to-end in
     lane coordinates, and decide the beat parity of the ACTUAL D2tw.
  OUTCOME A: beat-EVEN => the hierarchy carrier is MIRROR-EVEN; being
     dimensionless, the parity x dimension law (B1168) puts it OBJECT-
     side: the gauge choice is NOT an observer-column bit; census
     candidate 4 typed NOT-FRAME, and free-vs-forced moves to the
     object's side of the ledger.
  OUTCOME B: beat-BROKEN => mirror-odd datum, priced to the observer
     column — the hierarchy is observer-carried (relay to cc).
  Ambiguous transport (0 or several distinct sets) banks as a
     dictionary request to cc.
ALSO BANKED EN ROUTE: the beat-parity law for all 128 affine classes
(criterion <a, shift(r0)> mod 2, verified matrix-vs-formula) and the
flip-count histogram.  Machine decides.  Gate 5 untouched.
"""
import os
from fractions import Fraction as Fr
from itertools import product

SCR = os.path.dirname(os.path.abspath(__file__))
CERT = os.environ.get("BENCH_CERT") or SCR
src = open(os.path.join(CERT, "twisted_double.py")).read()
cut = src.index("# ---------------- stage 4")
exec(src[:cut])

# ---- the 27's weights in the lane's own coordinates (coroot eigenvalues)
H = [rho27_Q(hv) for hv in ([Fr(1) if k == i else Fr(0) for k in range(DIM)] for i in range(N))]
wt = [tuple(H[i][a][a] for i in range(N)) for a in range(27)]
assert all(all(x == int(x) for x in w) for w in wt)
wtZ = [tuple(int(x) for x in w) for w in wt]

# ---- the banked beat's unipotent part (jordan_beat's construction, verbatim)
r0 = ROOTS[0]
E27p = toF(rho27_Q(evec(r0)))
U = nilexp(E27p, QQ)
# the root's weight shift in lane coordinates, read off the matrix itself:
shift = None
for a in range(27):
    for b in range(27):
        if E27p[a][b] != (Fr(0), Fr(0)):
            s = tuple(int(wt[a][i] - wt[b][i]) for i in range(N))
            assert shift is None or shift == s, "generator not weight-homogeneous"
            shift = s
assert shift is not None
print(f"lane weight coordinates ready; beat root r0 shift vector = {shift}")

def pmatmul(A, B):
    return [[sum27(A, B, i, j) for j in range(27)] for i in range(27)]
def sum27(A, B, i, j):
    s = (Fr(0), Fr(0))
    for k in range(27):
        a = A[i][k]
        if a == (Fr(0), Fr(0)):
            continue
        b = B[k][j]
        if b == (Fr(0), Fr(0)):
            continue
        s = fadd(s, fmul(a, b))
    return s

def diagmat(signs):
    Z = (Fr(0), Fr(0))
    return [[(Fr(signs[i]), Fr(0)) if i == j else Z for j in range(27)] for i in range(27)]

results = {}
hist = {}
for avec in product((0, 1), repeat=N):
    par = [sum(avec[i]*wtZ[w][i] for i in range(N)) % 2 for w in range(27)]
    evens = par.count(0)
    # criterion prediction: beat-even iff <a, shift> even
    pred_even = (sum(avec[i]*shift[i] for i in range(N)) % 2 == 0)
    for eps in (-1, +1):
        # D(w) = eps * (-1)^<a,w>; flips = # entries equal to -1
        signs = [eps*(1 if p == 0 else -1) for p in par]
        flips = signs.count(-1)
        D = diagmat(signs)
        even = pmatmul(U, D) == pmatmul(D, U)
        assert even == pred_even, (avec, eps, "criterion mismatch")
        results[(avec, eps)] = (flips, even)
        hist[flips] = hist.get(flips, 0) + 1

print("criterion VERIFIED on all 128: beat-even  <=>  <a, shift(r0)> even (matrix = formula)")
print(f"flip-count histogram over the 128 affine classes: {dict(sorted(hist.items()))}")

# ---- the D2tw class: polarity eps=-1, flip count 11 (B928/B916 signature),
# refined by B916's second basis-robust invariant: the FLIP WEIGHT-SUMS are
# {-1 x2, 0 x7, +1 x2} (the coordinate-sum Sum_i <w, alpha_i^vee> is invariant
# under simple-root relabeling, so it transports between the two stacks).
TARGET_SUMS = sorted([-1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 1])
def flipsums(avec, eps):
    par = [sum(avec[i]*wtZ[w][i] for i in range(N)) % 2 for w in range(27)]
    signs = [eps*(1 if p == 0 else -1) for p in par]
    return sorted(sum(wtZ[w]) for w in range(27) if signs[w] == -1)

klass11 = [(a, e) for (a, e), (fl, ev) in results.items() if e == -1 and fl == 11]
klass = [(a, e) for (a, e) in klass11 if flipsums(a, e) == TARGET_SUMS]
print(f"\n11-flip eps=-1 candidates: {len(klass11)}; of these, matching B916's")
print(f"flip weight-sum signature {{-1 x2, 0 x7, +1 x2}}: {len(klass)}")
verds = sorted({results[k][1] for k in klass})

for (a, e) in klass:
    print(f"   a={a}: beat-{'EVEN' if results[(a, e)][1] else 'BROKEN'}")

if len(klass) == 0:
    print("\nOUTCOME: NO 11-flip affine class exists in the lane's coordinates —")
    print("a convention clash with B928's basis; banks as a dictionary request to cc.")
elif verds == [True]:
    print("\nOUTCOME A: every candidate in the D2tw class is beat-EVEN — the")
    print("hierarchy carrier is MIRROR-EVEN.  With dimensionlessness, the parity")
    print("law (B1168) puts it OBJECT-side: the Hermitian gauge choice is NOT an")
    print("observer-column bit.  Census candidate 4: typed NOT-FRAME; the")
    print("free-vs-forced question moves to the object's side of the ledger.")
elif verds == [False]:
    print("\nOUTCOME B: every candidate in the D2tw class is beat-BROKEN — the")
    print("twist does not survive the mirror: a mirror-odd datum, PRICED TO THE")
    print("OBSERVER COLUMN.  The generation hierarchy is carried by an observer-")
    print("column datum.  Census candidate 4: typed FRAME; relay to cc.")
else:
    print("\nPART 1 RESULT: the signature class is parity-MIXED — the banked")
    print("signatures alone do not pin D2tw; falling through to PART 2 (the")
    print("explicit flip-vector transport), as preregistered.")




# ================= PART 2: THE DECISIVE TRANSPORT =================
# B916 frontier/B916_lambda_bridge/results.json, key H_prime_diag_vs_H_plus
# (vendored verbatim; provenance: main @ B1187 sweep, 2026-08-28):
#   "flip_count": 11, "same_as_B912_D_diag": false, and the flip set:
CC_FLIPS = [(0,0,0,0,-1,1), (-1,-1,1,0,0,0), (-1,1,1,-1,0,0), (-1,0,0,1,-1,0),
            (-1,0,0,0,0,1), (1,0,-1,0,1,-1), (0,0,1,0,-1,0), (0,0,1,-1,0,1),
            (0,-1,0,1,-1,1), (0,1,0,0,-1,1), (-1,0,1,0,0,0)]
# B928 Q1a (same provenance): a* = (1,0,1,0,1,1), polarity -1, unique in 128.
CC_ASTAR = (1,0,1,0,1,1)

from itertools import permutations as _perms
S = set(wtZ)
good = []
for pi in _perms(range(N)):
    for neg in (1, -1):
        T = [tuple(neg*v[pi[i]] for i in range(N)) for v in CC_FLIPS]
        if set(T) <= S:
            good.append((pi, neg, frozenset(T)))
distinct = sorted({t for (_, _, t) in good}, key=sorted)
print(f"\nPART 2: embeddings of B916's flip set into the lane's weight system: {len(good)}")
print(f"   distinct transported flip SETS: {len(distinct)}")
assert len(distinct) == 1, "transport ambiguous — dictionary request to cc"
assert any(pi == tuple(range(N)) and neg == 1 for (pi, neg, _) in good), \
    "identity does not embed — coordinate conventions differ"
print("   the IDENTITY permutation embeds: cc's B883 weight coordinates and the")
print("   lane's crystal coordinates AGREE — no dictionary needed.")
T = distinct[0]
idx = {w: i for i, w in enumerate(wtZ)}
signsD2 = [(-1 if wtZ[i] in T else 1) for i in range(27)]
# cross-check B928's formula end-to-end in lane coordinates:
parA = [sum(CC_ASTAR[i]*wtZ[w][i] for i in range(N)) % 2 for w in range(27)]
formula = [-(1 if p == 0 else -1) for p in parA]     # D2 = -(-1)^<a*,w>
assert formula == signsD2, "affine-character formula mismatch vs the flip set"
print("   B928's formula VERIFIED in lane coordinates: D2 = -(-1)^<a*,w>,")
print(f"   a* = {CC_ASTAR} — flip set and formula agree entrywise (27/27).")
D2 = diagmat(signsD2)
even_comm = all(not (E27p[a][b] != (Fr(0), Fr(0)) and signsD2[a] != signsD2[b])
                for a in range(27) for b in range(27))
even_full = pmatmul(U, D2) == pmatmul(D2, U)
assert even_comm == even_full
print(f"   beat parity of THE actual D2tw: {'EVEN' if even_full else 'BROKEN'}")
if even_full:
    print("""
OUTCOME A — THE HIERARCHY CARRIER IS MIRROR-EVEN.  Omega D2 Omega^-1 =
D2 exactly (both the commutator criterion and the full unipotent
conjugation, exact pair arithmetic).  D2tw is dimensionless and mirror-
even: by the record's own parity x dimension law (B1168) it sits on the
OBJECT'S side of the boundary.  Census candidate 4 is typed: the
Hermitian gauge choice is NOT an observer-column bit — the generation
hierarchy is NOT carried by observer frame data.  What remains of the
gauge crux is an OBJECT-side question (is the twist forced?), which is
a different, attackable problem — relayed to cc with this cell.""")
else:
    print("""
OUTCOME B — the twist breaks under the mirror: a mirror-odd datum,
priced to the observer column; the hierarchy is observer-carried.
Relay to cc.""")
print("""Fences: Part 1's class survey shows the two banked signatures alone do
NOT pin the class (15 candidates, mixed parity) — the decision needed
B916's explicit flip vectors; that dependence is now a vendored pin.
The beat is the lane's banked mirror realization (memos 31-33/46,
B1174's c-leg).  Gate 5 untouched.""")
