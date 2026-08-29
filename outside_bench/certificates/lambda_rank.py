#!/usr/bin/env python3
"""MEMO-128 CELL (the owner's GO on the bench's ranking): THE LAMBDA-TERM'S
RANK ON B0 — B1206's named CHEAPEST closer of the P^3 cut ledger, computed
on the instrument that produced the datum B1206 cites.

WHY THIS CELL, AND WHY HERE.  B1206 (banked, verdict OPEN) moves the P^3
row from "no linear conditions exist" to "exactly ONE exists; the forcing
is ONE CONDITION SHORT":
    the Higgs line P(B0)                                    dim 3
    - 1 canonical LINEAR condition   the lambda-term         dim 2
    - 1 NONLINEAR condition          det Y_d(h) = 0 (B1205)  dim 1
    points require                                           dim 0
It names three candidates for the missing condition and calls (iii) THE
LAMBDA-TERM'S OWN RANK "the cheapest": the row is banked as "2 nonzero
entries" in ONE functional, "but if the underlying map has rank 2 rather
than 1 the ledger closes immediately."  The row B1206 cites is MEMO 80's
(N.Hu.Hd : N1 -> 2 nonzero, N2 -> 0), byte-verified at B1171 — and memo
80's certificate is on this bench.  So the cheapest closer is computable
here with no new mathematics: rebuild the Jordan cubic C and the forced
roster by memo 80's own construction (imported verbatim, not re-derived —
the exhaust-before-building rule), then read the rank off the matrix.

THE PREREGISTERED FORK, AS WRITTEN BEFORE THE RUN (kept verbatim,
because the run showed it to be MIS-SPECIFIED and that is the finding):
  R-1  rank = 1  => the lambda-term supplies exactly ONE linear condition;
       B1206's ledger stands at dim 1 and the P^3 row stays PERMANENT.
  R-2  rank = 2  => TWO independent linear conditions; the ledger closes at
       dim 0 and the P^3 row flips PERMANENT -> FORCED.
  R-3  rank = 0 or >= 3 => neither; report exactly and revise the reading.

*** IN-RUN CORRECTION, FILED AT POINT OF OCCURRENCE — THE FORK IS ILL-POSED
AND ITS R-1 BRANCH IS PROVABLY EMPTY. ***  The run returns rank 2, which
under the fork as written would close the ledger.  It does NOT, and the
reason is structural rather than a patch: memo 80's Hu = two states with
t3 = -1 and +1, i.e. THE TWO SU(2) COMPONENTS OF ONE DOUBLET (its docstring
says so: "Higgs docket 4 = 2 doublets"), and likewise Hd.  Because C
conserves t3 — PROVED here by a gate over all 45 nonzero triples, exactly
parallel to memo 80's Y-conservation gate — the Hu x Hd block is forced
ANTIDIAGONAL, so its rank lies in {0, 2} and RANK 1 IS IMPOSSIBLE for any
doublet-doublet-singlet coupling.  The observed matrix is [[0,1],[-1,0]]:
the SU(2) epsilon tensor.  Rank 2 therefore measures the NONDEGENERACY OF
epsilon — the gauge group — and not a second condition.  The correct
instrument is the number of GAUGE-INVARIANT functionals, which is ONE:
N1 . eps^{ab} Hu_a Hd_b.  A fork whose two branches are "impossible" and
"always" cannot decide anything, and saying so is the honest verdict.

THE SAME TRAP, CONFIRMED ON B1206's OTHER CANDIDATE: the exotic-mass row
D.Dc.N1 returns rank 3 — and D, Dc are colour triplets, so by the parallel
COLOUR-conservation gate that block is a permutation matrix, the SU(3)
delta contraction.  Rank 3 again measures the gauge group.  ONE invariant
functional there too.

THE CELLS:
  L1  rebuild C and the roster by memo 80's construction (its own asserts
      re-run: dim 1, 45 triples, the Y-conservation gate).
  L2  THE LAMBDA MATRIX: M[i][j] = C(N, Hu_i, Hd_j) exact, for BOTH
      neutrals; print the entries and the rank over Q.
  L3  THE FULL FORM ON THE DOCKET: C(N, ., .) restricted to the whole
      Higgs docket B0 = Hu u Hd as a symmetric matrix; its rank is the
      rank of the linear map h -> C(N, ., h), which is the object B1206's
      (iii) asks about.
  L4  B1206's CANDIDATE (i) IN THE SAME CELL, since it is free here: the
      exotic-mass row D.Dc.N, its entry count and its rank.
  L5  THE VERDICT against B1206's ledger, with the SCOPE STATED: memo 80's
      roster counts STATES (Hu 2, Hd 2, docket 4) while B1206's ledger
      leans on B1161's sector table Q/dc/Hd/Hu = 3/3/4/1, which counts
      GENERATION MULTIPLICITIES.  Those are different spaces; the cell
      reports the rank it computes and says exactly which reading it
      settles and which it does not.
Gate 5 untouched: zero/nonzero patterns, ranks and counts only — no
coupling is asserted to take any value, and nothing here says the
lambda-term must vanish.
"""
import os, itertools
from fractions import Fraction as F
from collections import defaultdict, Counter

# ---- L1: memo 80's construction, imported VERBATIM (not re-derived)
SCR = os.path.dirname(os.path.abspath(__file__))
src = open(SCR + "/yukawa_texture.py").read()
cut = src.index("# full triple census")
exec(compile(src[:cut], "yukawa_texture.py[prefix]", "exec"))
print("\nL1 — memo 80's cubic and roster rebuilt in-run (its own asserts re-run above).")

# ---- L2: the lambda matrix, both neutrals
def rank_Q(M):
    A = [row[:] for row in M]
    m = len(A); n = len(A[0]) if m else 0
    r = 0
    for col in range(n):
        p = next((i for i in range(r, m) if A[i][col] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][col]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][col] != 0:
                f = A[i][col]
                A[i] = [x - f*y for x, y in zip(A[i], A[r])]
        r += 1
    return r

print(f"\nL2 — THE LAMBDA MATRIX  M[i][j] = C(N, Hu_i, Hd_j)   "
      f"(Hu {Hu}, Hd {Hd}):")
lam_rank = {}
for nm in ("N1", "N2"):
    Nst = MULT[nm][0]
    M = [[Cval(Nst, hu, hd) for hd in Hd] for hu in Hu]
    nz = sum(1 for row in M for v in row if v != 0)
    rk = rank_Q(M)
    lam_rank[nm] = (rk, nz)
    print(f"    {nm} (state {Nst}):")
    for i, hu in enumerate(Hu):
        print(f"        Hu={hu}: " + "  ".join(f"{str(M[i][j]):>4s}" for j in range(len(Hd))))
    print(f"        nonzero entries: {nz}     RANK over Q: {rk}")

# ---- L3: the full form on the whole Higgs docket
B0 = list(Hu) + list(Hd)
print(f"\nL3 — THE FULL FORM ON THE DOCKET  B0 = Hu u Hd = {B0} (dim {len(B0)}):")
doc_rank = {}
for nm in ("N1", "N2"):
    Nst = MULT[nm][0]
    G = [[Cval(Nst, a, b) for b in B0] for a in B0]
    sym = all(G[i][j] == G[j][i] for i in range(len(B0)) for j in range(len(B0)))
    rk = rank_Q(G)
    doc_rank[nm] = rk
    print(f"    {nm}: symmetric {sym}, RANK over Q: {rk}")
    for i, a in enumerate(B0):
        print(f"        {a:>3d}: " + "  ".join(f"{str(G[i][j]):>4s}" for j in range(len(B0))))

# ---- L4: B1206's candidate (i), free here
print(f"\nL4 — B1206's CANDIDATE (i), the exotic-mass row  D.Dc.N  "
      f"(D {Dst}, Dc {Dcst}):")
for nm in ("N1", "N2"):
    Nst = MULT[nm][0]
    E = [[Cval(Nst, d, dc) for dc in Dcst] for d in Dst]
    nz = sum(1 for row in E for v in row if v != 0)
    rk = rank_Q(E)
    print(f"    {nm}: {nz} nonzero entries, RANK over Q: {rk}")
    for i, d in enumerate(Dst):
        print(f"        D={d}: " + "  ".join(f"{str(E[i][j]):>4s}" for j in range(len(Dcst))))

# ---- L5: THE CONSERVATION GATES (what makes the verdict structural)
print("\nL5 — THE CONSERVATION GATES (the reason rank is the wrong instrument):")
bad_t3 = [t for t in triples if Cval(*t) != 0 and sum(t3[x] for x in t) != 0]
assert not bad_t3, bad_t3
print(f"    t3-CONSERVATION GATE: all {sum(1 for t in triples if Cval(*t)!=0)}"
      f" nonzero C triples have t3 summing to 0: PASS")
def cw(i):
    return (ip(W[i], pairs[COLOR][0]), ip(W[i], pairs[COLOR][1]))
bad_c = [t for t in triples if Cval(*t) != 0
         and tuple(sum(cw(x)[k] for x in t) for k in (0, 1)) != (0, 0)]
assert not bad_c, bad_c
print("    COLOUR-CONSERVATION GATE: every nonzero C triple has colour weight"
      " summing to 0: PASS")
print(f"    Hu components carry t3 = {[t3[s] for s in Hu]}, Hd components"
      f" t3 = {[t3[s] for s in Hd]} — ONE DOUBLET EACH.")
print("    => t3-conservation forces the Hu x Hd block ANTIDIAGONAL, so its")
print("       rank lies in {0, 2}: RANK 1 IS IMPOSSIBLE.  The observed block is")
print("       [[0,1],[-1,0]] — the SU(2) epsilon tensor, nondegenerate.")
print("    => colour-conservation likewise forces the D x Dc block to be a")
print("       permutation matrix: rank in {0, 3}, i.e. the SU(3) delta.")

# ---- L6: the verdict
print("\nL6 — THE VERDICT against B1206's cut ledger:")
rk1 = lam_rank["N1"][0]
print(f"    memo 80's banked row reproduced exactly: N1 -> {lam_rank['N1'][1]}"
      f" nonzero, N2 -> {lam_rank['N2'][1]} nonzero.")
print(f"    THE RANK B1206 ASKS FOR: rank of C(N1, Hu_., Hd_.) = {rk1}")
assert rk1 == 2
print("    But the preregistered fork that maps that rank to a count of")
print("    conditions is MIS-SPECIFIED: by L5 its R-1 branch is EMPTY, so the")
print("    fork's two branches are 'impossible' and 'always' and it decides")
print("    nothing.  Rank in COMPONENT space measures the gauge contraction")
print("    tensor, not the number of conditions.")
print("    THE CORRECT COUNT — gauge-invariant functionals supplied:")
print("       lambda-term  N1 . eps^{ab} Hu_a Hd_b          :  ONE")
print("       exotic mass  N1 . delta^i_j D_i Dc^j          :  ONE")
print("    ==> B1206's candidate (iii) — its own named CHEAPEST closer — is")
print("        CLOSED NEGATIVELY, and closed for a STRUCTURAL reason rather")
print("        than by a count coming out small.  Candidate (i), the")
print("        exotic-mass row, is closed negatively by the same argument in")
print("        the same cell.  B1206's ledger STANDS at dim 1: the P^3 is")
print("        still exactly one condition short.")
print("""
WHAT REMAINS OF B1206's THREE CANDIDATES (stated, not overreached):
  (i)   exotic-mass row D.Dc.N  — CLOSED NEGATIVELY here: one invariant
        functional, and its rank 3 is the colour delta.
  (ii)  doublet-triplet splitting — the record types it EXTERNAL and
        colour-choice-dependent (B298/B299, banked and re-read for this
        cell), so by B1206's own statement it cannot supply an object-side
        condition: a clean negative.
  (iii) the lambda-term's rank — CLOSED NEGATIVELY here, structurally.
ALL THREE NAMED CANDIDATES ARE NOW NEGATIVE.  That does NOT prove no
condition can exist — it proves the record's named routes are exhausted,
which is a materially different and much stronger statement than "not yet
found".  The honest consequence is that B1196's CLOSED-PERMANENT verdict
on the P^3 is HARDENED, not overturned, and any future closer must come
from a source none of the three candidates names.

SCOPE, STATED RATHER THAN GLOSSED.  This cell computes on MEMO 80's
roster, which counts STATES: Hu 2, Hd 2, Higgs docket 4 = 2 doublets.
B1206's ledger leans on B1161's sector table Q/dc/Hd/Hu = 3/3/4/1, which
counts GENERATION MULTIPLICITIES.  Those are different spaces, and
B1206's cited datum comes from the first while its ledger is built on the
second.  Under the second reading Hu is pinned and the lambda-term is one
functional by construction — the SAME answer this cell reaches on the
first, which is why the verdict is robust across the mismatch.  The
mismatch itself is filed as a cross-source finding for the primary record;
it does not change the count either way.
Gate 5 untouched: zero/nonzero patterns, ranks and counts only.""")
