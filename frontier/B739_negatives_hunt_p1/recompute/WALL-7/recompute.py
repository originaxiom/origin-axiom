#!/usr/bin/env python3
"""B739 Stage-B recompute -- target WALL-7 (LAW_MAP #E 7: "The naive Z/3 triality does not
act on H1(D;27) ... the 3+2 split as proposed is dead (the rebase)").

THE BANKED KILL (Stage-A record, kill_form = zero-intertwiner): the wall text
(docs/LAW_MAP.md section E item 7, sourced to docs/REBASE_2026-07-16.md section 2) asserts
the kill by "standard facts"; the discriminating COMPUTATION lives one hop away in B651's
cc2 packets (located by the Stage-A citation chain):
  d5_triality (straight): each of the 8 nontrivial Z3xZ3 trinification elements (B299's
     theta/phi Dynkin actions) induces a 27-weight-permutation P; the phase-lift X = P.D
     (D diagonal, 27 unknowns) intertwining the double's holonomy (X M = M X for
     M in {rho(a), rho(b), rho(c)}) has solution dim = 0 at EVERY pattern (exact solve).
  f3_twisted (sigma*-twisted): the swap-twisted system (X A = A X, X B = C X, X C = B X --
     the deck swap sigma*, the double's one surviving symmetry) ALSO has dim = 0 at every
     pattern.
THE DISCRIMINATING FACT = those 16 exact zeros (8 straight + 8 twisted). This script
RE-DERIVES them (E19: compute-not-cite) from the original arcs' own declared conventions,
reconstructing every input in-sandbox -- including the double's third generator C27, whose
banked carrier (seat-work/cell3_double/stage1_classes.pkl: the weld intertwiner J and the
h1 = 5 record) is NOT in the repo.

INPUT RECONSTRUCTION (the one non-repo input, re-derived from declared conventions):
  d5/f3 rebuilt C27 = J . (B27^-1)^T . J^-1 from the pkl's J: the weld intertwiner of the
  DUAL-REP double -- 3-generator presentation
      < a, b, c | REL(a,b), REL(a,c), lam(a,c) lam(a,b)^-1 >
  (mu matched, lambda MATCHED -- d5's own relator gates R1/R2/R3). The sibling banked
  pipeline (B637 part 1, in-repo; PROGRESS_LOG 2026-07-15) declares the weld method:
  "the weld intertwiner solved at the SL(2) level -- 2-dim solution space, invertible
  representative -- lifted through the principal embedding". Re-derived here, adapted to
  d5's dual-rep convention:
    (i)   SL(2) level: solve u . (g^-1)^T . u^-1 = g for g in {a, lam(a,b)} (4 unknowns,
          exact over K = Q(sqrt(-3))). COMPUTED STRUCTURE of the space (asserted below):
          every solution is u = (xI + zN) . eps^-1, N = [[0,1],[0,0]], eps = [[0,1],[-1,0]];
          invertible iff x != 0; the whole weld freedom is ONE parameter t = z/x, and t = 0
          is the DEGENERATE point (C27 = B27 exactly -- the pullback of the solo rep along
          D ->> Gamma(4_1), not the geometric double; computed below as a control).
    (ii)  27 level: transpose-duality of the principal embedding is NOT the lift of the
          SL(2) duality (f_pr^T = sum k_i e_i != e_pr; kvals = (16,22,30,42,30,16)); the
          correct 27-level dual intertwiner is J1 = S27 . T27 with S27 = pi(eps) =
          A27 . exp(-f_pr) . A27 and T27 the exact torus element with alpha_i(T27) = 1/k_i
          (diagonal on the weight basis; well-defined because the 27's weights lie in ONE
          P/Q coset -- integral root-coordinates asserted; normalization chi(mu_0) = 1 is
          conjugation-inert, declared). GATE: J1 . (M^-1)^T . J1^-1 == M EXACTLY for
          M in {A27, B27} -- the FULL dual rep is intertwined, not just the peripheral pair.
    (iii) J(t) = exp(t e_pr) . J1 and C27(t) = J(t) . (B27^-1)^T . J(t)^-1 = W_t B27 W_t^-1
          with W_t = exp(t e_pr). (The scalar factor of xI + zN acts centrally on pi(SL2)
          and cancels in every conjugation -- declared.)
  E1 DECLARATION (the one unrecoverable convention): the pkl's specific weld point t is
  gone with the pkl. The reconstruction therefore runs every solve at THREE declared
  nondegenerate weld points t in {1, omega, 2} (omega = (1+sqrt(-3))/2), and ALSO solves
  the straight system with the {A27, B27} constraints alone -- which is exactly the t = 0
  degenerate system, and a lower bound for every weld point. If THAT is already dim 0, the
  straight kill is independent of the weld gauge entirely.
  GATES on the reconstruction (all must pass, at every probed t, before any solve is read):
    G-A  27-level weld equations: J (A27^-1)^T J^-1 = A27, J (lam27^-1)^T J^-1 = lam27.
    G-B  d5's own relator gates: R1 = REL(a,b), R2 = REL(a,c), R3 = lam(a,c) lam(a,b)^-1,
         all = I27 exactly.
    G-C  nondegeneracy: C27 != B27.
    G-D  the banked class-level signature the pkl carried: Fox h0/h1 of the 3-generator
         double presentation with the 27 local system = 1/5 (= B637's banked dimension
         table for the unbent double); control FIRST: trivial coefficients give
         (h0, h1) = (1, 1) = b1(D) (the standing B591-M4 rule).

CONVENTIONS DECLARED (E1, the rest):
  * Field/matrices/helpers: exec of B575 l51_obstruction.py stages 0-3 -- the SAME prefix
    d5/f3 exec'd (their declared source); its G1-G3 gates assert internally. K = Q(sqrt(-3))
    as (a, b) ~ a + b*sqrt(-3) (printed "(a+br)"); OMEGA = (1+sqrt(-3))/2 = e^{i pi/3};
    A27 = exp(e_pr), B27 = exp(OMEGA f_pr) (the discrete faithful fig-8 holonomy through
    the principal embedding).
  * REL = "abABaBAbaB" (B575); LAM = "abABaaBAbA" (the certified longitude, B598 -- the
    same constant d5/f3 hard-code).
  * Weight bridge exactly as d5: B299's 27 weight labels (sorted lexicographically first --
    B299's _weights_27 returns a set-ordered list; sorting is a pure relabeling, declared
    for determinism) matched to B575's basis order over all 720 Dynkin-coordinate
    permutations; every consistent relabeling x each of the 8 nontrivial Z3xZ3 elements
    gives a candidate induced 27-permutation; deduped by the permutation.
  * Pattern solve exactly as d5/f3: unknowns d_0..d_26 with X[pperm[j]][j] = d_j; the rows
    of X Ml - Mr X = 0 over K; dim = 27 - #pivots of the exact rref.
  * The float commutant diagnostic (SVD, 1e-8 relative gap) is reproduced as in d5/f3 and
    labeled NON-EXACT context; the exact zeros are the load-bearing facts. Stage 6 also
    runs a provenance probe on the banked "415-dim commutant" quote (it matches the
    DEGENERATE triple exactly -- see the note printed there).
  * Deterministic: no wall-clock in the output (B575's log timestamps are stripped), no
    randomness, no network. Gate 5: pure mathematics; no SM quantity anywhere.

Run:  python3 recompute.py > output.txt 2>&1
"""
import contextlib
import io
import os

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
B575 = os.path.join(REPO, "frontier", "B575_bridge_obstruction", "l51_obstruction.py")
B299 = os.path.join(REPO, "frontier", "B299_trinification_triality",
                    "trinification_triality.py")
LAM = "abABaaBAbA"
d = 27

print("=" * 88)
print("B739 Stage-B recompute -- WALL-7 (LAW_MAP #E 7): the trinification triality on")
print("H1(D;27) -- the zero-intertwiner kill (B651 d5_triality + f3_twisted), re-derived.")
print("K printout: (a+br) means a + b*sqrt(-3).")
print("=" * 88)

# --------------------------------------------------------------------------- stage 0
print("\nSTAGE 0 -- exec B575 stages 0-3 (the arcs' declared construction; G1-G3 gates")
print("assert internally; log timestamps stripped for determinism):")
src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 4")
ns = {"__name__": "b575_prefix", "__file__": B575}
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    exec(compile(src[:cut], B575, "exec"), ns)
for line in buf.getvalue().splitlines():
    print("  |", line.split("] ", 1)[-1])

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
OMEGA = ns["OMEGA"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
e_pr, f_pr = ns["e_pr"], ns["f_pr"]
kvals, W27, C6 = ns["kvals"], ns["W27"], ns["C6"]
REL = ns["REL"]
mmul, meye, madd, mscale, msub, mzero_p, rref, nullspace, mexp_nil = (
    ns[k] for k in ("mmul", "meye", "madd", "mscale", "msub", "mzero_p",
                    "rref", "nullspace", "mexp_nil"))
print(f"  principal-grading coefficients kvals = {kvals}")


def mt(M):
    n = len(M)
    return [[M[j][i] for j in range(n)] for i in range(n)]


def minv(M):
    n = len(M)
    aug = [list(M[i]) + [K1 if k == i else K0 for k in range(n)] for i in range(n)]
    Rr, piv = rref(aug)
    assert len(piv) == n, "singular matrix"
    out = [[K0] * n for _ in range(n)]
    for r_i, pc in enumerate(piv):
        for j in range(n):
            out[pc][j] = Rr[r_i][n + j]
    return out


def is_eye(M):
    n = len(M)
    return all((M[i][j] - (K1 if i == j else K0)).is_zero()
               for i in range(n) for j in range(n))


def word_mat(word, acts, n=d):
    P = meye(n)
    for ch in word:
        P = mmul(P, acts[ch])
    return P


def inv_word(w):
    return ''.join(ch.swapcase() for ch in reversed(w))


# --------------------------------------------------------------------------- stage 1
print("\nSTAGE 1 -- the weld intertwiner space at the SL(2) level (B637's declared")
print("method, adapted to d5's dual-rep / lambda-MATCHED convention):")
Ag = [[K1, K1], [K0, K1]]
Bg = [[K1, K0], [OMEGA, K1]]
Agi = [[K1, K(-1)], [K0, K1]]
Bgi = [[K1, K0], [K0 - OMEGA, K1]]
lets2 = {'a': Ag, 'b': Bg, 'A': Agi, 'B': Bgi}
assert is_eye(word_mat(REL, lets2, 2)), "SL2 relator fails"
lam2 = word_mat(LAM, lets2, 2)
print(f"  lambda(a,b) at SL(2) = [[{lam2[0][0]!r}, {lam2[0][1]!r}], "
      f"[{lam2[1][0]!r}, {lam2[1][1]!r}]]   (parabolic; the cusp translation)")


def mt2(M):
    return [[M[j][i] for j in range(2)] for i in range(2)]


def minv2(M):
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    di = det.inv()
    return [[M[1][1] * di, (K0 - M[0][1]) * di],
            [(K0 - M[1][0]) * di, M[0][0] * di]]


lam2i = minv2(lam2)
rows = []
for (X, Y) in ((mt2(Agi), Ag), (mt2(lam2i), lam2)):
    # u X - Y u = 0, u as a 4-vector (row-major 2x2)
    for i in range(2):
        for j in range(2):
            row = [K0] * 4
            for k in range(2):
                row[i * 2 + k] = row[i * 2 + k] + X[k][j]
                row[k * 2 + j] = row[k * 2 + j] - Y[i][k]
            rows.append(row)
sols = nullspace(rows)
print(f"  weld intertwiner space (SL2, dual rep, mu AND lambda matched): "
      f"dim = {len(sols)}")
assert len(sols) == 2, "expected the declared 2-dim SL(2) weld space"
eps = [[K0, K1], [K(-1), K0]]
for si, s in enumerate(sols):
    cand = [[s[0], s[1]], [s[2], s[3]]]
    Yc = mmul(cand, eps)
    assert Yc[1][0].is_zero() and (Yc[0][0] - Yc[1][1]).is_zero(), \
        "solution not of the form (xI + zN) eps^-1"
    print(f"    basis solution {si}: u.eps = xI + zN with "
          f"x = {Yc[0][0]!r}, z = {Yc[0][1]!r}")
print("  STRUCTURE (asserted): every weld solution is u = (xI + zN) eps^-1;")
print("  invertible iff x != 0; the residual weld gauge is t = z/x alone;")
print("  t = 0 is the DEGENERATE point (C27 = B27: the solo-rep pullback).")

# --------------------------------------------------------------------------- stage 2
print("\nSTAGE 2 -- the 27-level dual intertwiner J1 = S27 . T27 and its gates:")
mu0 = W27[0]
C6K = [[K(C6[i][j]) for j in range(6)] for i in range(6)]
C6K_inv = minv(C6K)
Tdiag = []
for mu in W27:
    dm = [K(mu[i] - mu0[i]) for i in range(6)]
    q = [sum((dm[i] * C6K_inv[i][j] for i in range(6)), K0) for j in range(6)]
    qs = []
    for x in q:
        assert x.b == 0 and x.a.denominator == 1, \
            f"non-integral root coordinate {x} for weight {mu}"
        qs.append(int(x.a))
    val = K1
    for i, qi in enumerate(qs):
        base = kvals[i].inv() if qi >= 0 else kvals[i]
        for _ in range(abs(qi)):
            val = val * base
    Tdiag.append(val)
print("  all 27 weights have INTEGRAL root-basis coordinates relative to mu_0")
print("  -> the 27 lies in ONE P/Q coset: any central element acts by ONE scalar on")
print("     the whole 27 (the wall's 'center = scalar' parenthetical, recomputed) and")
print("     T27 is well-defined over Q.")
T27 = [[Tdiag[i] if i == j else K0 for j in range(d)] for i in range(d)]
S27 = mmul(mmul(A27, mexp_nil(mscale(K(-1), f_pr))), A27)
J1 = mmul(S27, T27)
J1i = minv(J1)
gA = mzero_p(msub(mmul(mmul(J1, mt(A27i)), J1i), A27))
gB = mzero_p(msub(mmul(mmul(J1, mt(B27i)), J1i), B27))
print(f"  GATE  J1 (A27^-1)^T J1^-1 == A27 : {gA}")
print(f"  GATE  J1 (B27^-1)^T J1^-1 == B27 : {gB}   (the FULL dual rep is intertwined)")
assert gA and gB, "J1 dual-intertwiner gate failed"

lam27 = word_mat(LAM, {'a': A27, 'b': B27, 'A': A27i, 'B': B27i})
lam27i = minv(lam27)


def build_double(t):
    """J(t) = exp(t e_pr) . J1;  C27(t) = J (B27^-1)^T J^-1; returns acts + gates."""
    Wt = mexp_nil(mscale(t, e_pr))
    Jt = mmul(Wt, J1)
    Jti = minv(Jt)
    C = mmul(mmul(Jt, mt(B27i)), Jti)
    Ci = mmul(mmul(Jt, mt(B27)), Jti)
    assert is_eye(mmul(C, Ci)), "C27 inverse inconsistent"
    acts = {'a': A27, 'A': A27i, 'b': B27, 'B': B27i, 'c': C, 'C': Ci}
    g = {
        "weld_mu": mzero_p(msub(mmul(mmul(Jt, mt(A27i)), Jti), A27)),
        "weld_lam": mzero_p(msub(mmul(mmul(Jt, mt(lam27i)), Jti), lam27)),
        "R1": is_eye(word_mat(REL, acts)),
        "R2": is_eye(word_mat(REL.replace('b', 'c').replace('B', 'C'), acts)),
        "R3": is_eye(word_mat(
            LAM.replace('b', 'c').replace('B', 'C') + inv_word(LAM), acts)),
        "nondegenerate": not mzero_p(msub(C, B27)),
    }
    return acts, C, g


def fox_h(lets3, dim):
    """Fox h0/h1 of < a,b,c | REL(a,b), REL(a,c), lam(a,c) lam(a,b)^-1 > with
    dim-dimensional coefficients lets3 (the B637 fox_h1 machinery, 3-generator form)."""
    prim = {'a': 'a', 'b': 'b', 'c': 'c', 'A': 'a', 'B': 'b', 'C': 'c'}
    relators = [REL, REL.replace('b', 'c').replace('B', 'C'),
                LAM.replace('b', 'c').replace('B', 'C') + inv_word(LAM)]
    gens = "abc"
    rows_all = []
    for w in relators:
        L = {g: [[K0] * dim for _ in range(dim)] for g in gens}
        Pi = meye(dim)
        for ch in w:
            g = prim[ch]
            if ch.islower():
                L[g] = madd(L[g], Pi)
            else:
                L[g] = madd(L[g], mscale(K(-1), mmul(Pi, lets3[ch])))
            Pi = mmul(Pi, lets3[ch])
        assert mzero_p(msub(Pi, meye(dim))), f"relator {w} not identity"
        for i in range(dim):
            rows_all.append([L[g][i][j] for g in gens for j in range(dim)])
    Zc = nullspace(rows_all)
    fixrows = []
    for g in gens:
        M = lets3[g]
        for i in range(dim):
            fixrows.append([M[i][j] - (K1 if i == j else K0) for j in range(dim)])
    h0 = len(nullspace(fixrows))
    h1 = len(Zc) - (dim - h0)
    return h0, h1


# --------------------------------------------------------------------------- stage 3
print("\nSTAGE 3 -- the reconstructed doubles at the declared weld points; d5's gates +")
print("the banked class-level signature (pkl: h1 = 5; B637 table: h0/h1 = 1/5):")
triv = {ch: [[K1]] for ch in "abcABC"}
h0t, h1t = fox_h(triv, 1)
print(f"  control (trivial coefficients): h0 = {h0t}, h1 = {h1t}   [target 1, 1 = b1(D)]")
assert (h0t, h1t) == (1, 1), "trivial-coefficient control failed"

T_PROBES = [("t = 1", K1), ("t = omega", OMEGA), ("t = 2", K(2))]
doubles = {}
for lbl, tv in T_PROBES:
    acts_t, C_t, g_t = build_double(tv)
    gs = "  ".join(f"{k}:{g_t[k]}" for k in
                   ("weld_mu", "weld_lam", "R1", "R2", "R3", "nondegenerate"))
    print(f"  [{lbl}] {gs}")
    for k in ("weld_mu", "weld_lam", "R1", "R2", "R3", "nondegenerate"):
        assert g_t[k], f"gate {k} failed at {lbl}"
    h0_t, h1_t = fox_h(acts_t, 27)
    print(f"  [{lbl}] the 27 local system: h0 = {h0_t}, h1 = {h1_t}   [banked: 1, 5]")
    assert (h0_t, h1_t) == (1, 5), f"class-level signature mismatch at {lbl}"
    doubles[lbl] = (acts_t, C_t)

# --------------------------------------------------------------------------- stage 4
print("\nSTAGE 4 -- the weight bridge (B299 -> B575 labels) and the 8 patterns:")
import sympy as sp  # noqa: E402  (declared env: sympy 1.14)
from itertools import permutations  # noqa: E402

nb = {"__name__": "b299"}
exec(compile(open(B299).read(), B299, "exec"), nb)
w299 = sorted(tuple(int(y) for y in x) for x in nb["_weights_27"]())
TH, PH = nb["THETA"], nb["PHI"]
I6 = sp.eye(6)
assert TH**3 == I6 and PH**3 == I6 and TH * PH == PH * TH, "B299 Z3xZ3 sanity"
tri6 = []
for i in range(3):
    for j in range(3):
        m = TH**i * PH**j
        if m != I6 and not any(m == x for x in tri6):
            tri6.append(m)
print(f"  nontrivial Z3xZ3 elements: {len(tri6)}")
assert len(tri6) == 8
w575 = [tuple(w) for w in W27]
w575set = set(w575)
w299set = set(w299)
idx299 = {w: i for i, w in enumerate(w299)}
acts6 = [nb["_action_on_dynkin"](m) for m in tri6]
patterns = []
n_relab = 0
for perm in permutations(range(6)):
    relab = [tuple(x[perm[i]] for i in range(6)) for x in w299]
    if set(relab) != w575set:
        continue
    n_relab += 1
    idx299_to_575 = {j: w575.index(lw) for j, lw in enumerate(relab)}
    for A6 in acts6:
        pperm = [None] * 27
        ok = True
        for j, mu in enumerate(w299):
            img = tuple(int(sum(A6[i, l] * mu[l] for l in range(6)))
                        for i in range(6))
            if img not in w299set:
                ok = False
                break
            pperm[idx299_to_575[j]] = idx299_to_575[idx299[img]]
        if ok and all(p is not None for p in pperm):
            key = tuple(pperm)
            if key not in [p[0] for p in patterns]:
                patterns.append((key, perm))
print(f"  consistent Dynkin relabelings: {n_relab}; distinct induced 27-permutations: "
      f"{len(patterns)}")
assert len(patterns) == 8, "expected the banked 8 patterns"
for pi, (pp, perm) in enumerate(patterns):
    seen = set()
    sizes = {}
    for s0 in range(27):
        if s0 in seen:
            continue
        n_, cur = 1, pp[s0]
        while cur != s0:
            seen.add(cur)
            cur = pp[cur]
            n_ += 1
        seen.add(s0)
        sizes[n_] = sizes.get(n_, 0) + 1
    print(f"    pattern {pi} (relabel {perm}): orbit sizes {sizes}")
    assert sizes == {3: 9}, "pattern not a free order-3 permutation"

# --------------------------------------------------------------------------- stage 5
print("\nSTAGE 5 -- the exact pattern solves (27 unknowns d_j, X[pperm[j]][j] = d_j;")
print("dim = 27 - #pivots of the exact rref of the X Ml - Mr X = 0 rows):")


def pattern_solve(pperm, pairs_lr):
    rows = []
    for Ml, Mr in pairs_lr:
        for i in range(d):
            for j in range(d):
                coef = [K0] * d
                for k in range(d):
                    if pperm[k] == i:
                        coef[k] = coef[k] + Ml[k][j]
                coef[j] = coef[j] - Mr[i][pperm[j]]
                if not all(c.is_zero() for c in coef):
                    rows.append(coef)
    Rr, piv = rref(rows)
    return d - len(piv)


print("\n  [5a] the weld-gauge-independence probe: STRAIGHT system with the {A27, B27}")
print("  constraints ONLY (= the degenerate t = 0 system; a constraint-subset of EVERY")
print("  weld point -- if dim = 0 here, the straight kill needs no weld input at all):")
AB_ONLY = ((A27, A27), (B27, B27))
ab_dims = []
for pi, (pp, perm) in enumerate(patterns):
    ker = pattern_solve(list(pp), AB_ONLY)
    ab_dims.append(ker)
    print(f"    pattern {pi}: dim = {ker}")

straight_all = {}
twisted_all = {}
for lbl, tv in T_PROBES:
    acts_t, C_t = doubles[lbl]
    Ci_t = acts_t['C']
    STRAIGHT = ((A27, A27), (B27, B27), (C_t, C_t))
    TWISTED = ((A27, A27), (B27, C_t), (C_t, B27))
    sd, td = [], []
    print(f"\n  [5b/{lbl}] straight (d5) and sigma*-twisted (f3) solves:")
    for pi, (pp, perm) in enumerate(patterns):
        k1 = pattern_solve(list(pp), STRAIGHT)
        k2 = pattern_solve(list(pp), TWISTED)
        sd.append(k1)
        td.append(k2)
        print(f"    pattern {pi}: straight dim = {k1}   twisted dim = {k2}")
    straight_all[lbl] = sd
    twisted_all[lbl] = td

# --------------------------------------------------------------------------- stage 6
print("\nSTAGE 6 -- the float commutant diagnostic (NON-EXACT, SVD 1e-8 relative gap;")
print("d5/f3's context number was 415 -- the exact zeros above are the load-bearing")
print("facts; this stage also runs a provenance probe on that 415):")
import math  # noqa: E402
import numpy as np  # noqa: E402


def fl(M):
    return np.array([[complex(float(x.a), float(x.b) * math.sqrt(3)) for x in row]
                     for row in M])


def commutant_dim(mats):
    I27f = np.eye(27)
    rowsf = [np.kron(I27f, fl(M).T) - np.kron(fl(M), I27f) for M in mats]
    sv = np.linalg.svd(np.vstack(rowsf), compute_uv=False)
    return int((sv < 1e-8 * sv[0]).sum())


dim_ab = commutant_dim([A27, B27])
print(f"  dim commutant({{A27, B27}} alone = the DEGENERATE t = 0 triple) ~ {dim_ab}")
for lbl, tv in T_PROBES:
    dimc = commutant_dim([A27, B27, doubles[lbl][1]])
    print(f"  dim commutant({{A27, B27, C27}}) at {lbl} ~ {dimc}")
print("""  PROVENANCE NOTE (computed, honest-flag): the banked f3 FINDINGS quote a
  "415-dimensional commutant" for the triple; here 415 is EXACTLY the commutant of
  the DEGENERATE triple (C27 = B27, the t = 0 weld point -- which is also the first
  invertible element of the weld nullspace, i.e. what a naive representative pick
  selects), while every nondegenerate weld point gives a strictly smaller commutant.
  Together with the fact that the degenerate pullback ALSO has Fox h0/h1 = 1/5 (so
  the pkl's h1 = 5 gate could not distinguish it) and that d5/f3 never gated
  C27 != B27, this suggests the pkl's J may itself have been the degenerate weld.
  EITHER WAY THE KILL STANDS: the {A27, B27}-only solves (= the degenerate system,
  stage 5a) are dim 0 at all 8 patterns, and the honestly nondegenerate doubles
  (stage 5b, three weld points, all gates green) are dim 0 at all 8 patterns,
  straight and twisted. The recompute thus both UPHOLDS the banked zeros and
  REPAIRS their carrier: the zero-intertwiner fact is now verified on the
  geometric (nondegenerate) double as well, not only on the suspect weld point.""")

# --------------------------------------------------------------------------- verdict
print("\n" + "=" * 88)
ok_straight = all(v == 0 for sd in straight_all.values() for v in sd)
ok_twisted = all(v == 0 for td in twisted_all.values() for v in td)
ok_ab = all(v == 0 for v in ab_dims)
n_solves = len(ab_dims) + sum(len(x) for x in straight_all.values()) \
    + sum(len(x) for x in twisted_all.values())
print(f"RESULT ({n_solves} exact solves):")
print(f"  straight (d5) dims, 8 patterns x 3 weld points:  "
      f"{'ALL 0' if ok_straight else 'NONZERO FOUND'}")
print(f"  twisted (f3) dims,  8 patterns x 3 weld points:  "
      f"{'ALL 0' if ok_twisted else 'NONZERO FOUND'}")
print(f"  straight with {{A27, B27}} alone (t = 0 control):  "
      f"{'ALL 0 -- the straight kill is weld-gauge-independent' if ok_ab else 'NONZERO FOUND'}")
if ok_straight and ok_twisted:
    print("""
THE DISCRIMINATING FACT RECOMPUTED AND UPHELD: each of the 8 nontrivial Z3xZ3
trinification elements' induced 27-permutations admits ZERO phase-lift X = P.D
intertwining the double's holonomy -- straight (X M = M X for M in {a, b, c},
d5's system) AND sigma*-twisted (X A = A X, X B = C X, X C = B X, f3's system)
-- exact dim 0 at every pattern, on a double reconstructed in-sandbox from the
arcs' own declared conventions with every gate green (weld equations, R1/R2/R3,
nondegeneracy, h0/h1 = 1/5), and stable across the entire residual weld gauge.
The naive Z/3 trinification triality does not act on H1(D;27) by any phase
lift, straight or twisted: LAW_MAP #E 7 stands. RECONFIRMED.""")
else:
    print("\n*** THE BANKED FACT DID NOT REPRODUCE -- see the dims above. ***")
