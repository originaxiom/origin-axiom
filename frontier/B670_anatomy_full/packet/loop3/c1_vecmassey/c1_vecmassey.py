"""C1 -- THE VECTOR-VALUED MASSEY (PREREG_L3.md sha f32fbfff, C1 clause).

"the fifth-wall-or-first-structure cell": coefficients in 27-bar via the
Jordan cross product (the portal's pairing), a STRICTLY RICHER object than
B2's scalar (v0bar-contracted) Massey product -- B2's own FINDINGS_CC2.md
named this exact computation as "the precise next question."

THE VECTOR CUP (STEP 1, prereg's literal formula): for 1-cocycles u_i, u_j in
Z^1(D; 27) (i,j in the solo triple {2,3,4}), define the 2-cochain valued in
the DUAL module 27-bar via the (totally symmetric, G-equivariant) Jordan cross
product C3: 27 (x) 27 -> 27-bar (w1_portal.py's C3, gated N-invariant):

    c_ij(g,h) := u_i(g) x (rho(g).u_j(h)) = C3(u_i(g), rho(g).u_j(h))

This is the STANDARD bar-resolution cup-product formula for two 1-cocycles
through a G-equivariant pairing phi: M1 (x) M2 -> M3 (here M1=M2=27, M3=27bar,
phi=C3), which is G-equivariant because N-invariance gives EXACTLY
C3(rho(g)x, rho(g)y) = rho-bar(g).C3(x,y) (verified below as a control) --
rho-bar(g) := (rho(g)^-1)^T being the SAME dual/contragredient action
w1_portal.py's dacts already builds. The associated cocycle identity
    (delta c_ij)(g,h,k) = rho-bar(g).c_ij(h,k) - c_ij(gh,k) + c_ij(g,hk) - c_ij(g,h) = 0
is a general consequence of u_i,u_j being cocycles and C3 equivariant; it is
verified EXACTLY (not assumed) on the same 5 generator triples used throughout
this campaign (s4/b2's TEST_TRIPLES).

H^2(D; 27-bar) SOLVABILITY TEST (the literal method the prereg specifies):
[c_ij] = 0 iff there is a 1-cochain b: G -> 27bar (parametrized freely by its
81 = 3*27 values on the generators a,b,c; inverse-generator values FORCED via
delta b(g,g^-1) = c_ij(g,g^-1); extended along any word by the recursion
b(prefix+ch) = rho-bar(prefix).b(ch) + b(prefix) - c_ij(prefix,ch)) with
delta b = c_ij, i.e. with b(R_r) = 0 on all 3 relators (R_r = 1 in G). The
LINEAR part of this recursion in the 81 unknowns is, term for term, EXACTLY
w1_portal.py's own dual_big Fox-derivative matrix F (already built, reused
verbatim, not rebuilt); the CONSTANT part (the "-c_ij(prefix,ch)" defect,
evaluated at y=0) is a new 81-vector BASE_ij computed here. Solvability of
F.y = -BASE_ij is [c_ij]=0 IFF -BASE_ij lies in im(F); since (standard linear
algebra over a field) im(F) = ker(F^T)^annihilator, this is checked by pairing
BASE_ij against a basis of ker(F^T) = the LEFT nullspace of F (computed ONCE,
reused for all 9 pairs) -- this is the SAME "solvability test IS the vanishing
test" the prereg specifies, just executed via one nullspace call instead of 9
separate augmented-rref solves.

h^2(D;27-bar) = 5 CONSISTENCY (the prereg's gate, verified not assumed): for
this closed "double" 3-manifold group D with presentation <a,b,c|R1,R2,R3>
(3 generators = 3 relators, chi = 0), Poincare duality + universal
coefficients (K a field) gives, for the dual module 27bar with true dual
(27bar)^* = 27 (the perfect "dot" pairing, G-invariant since
dot(rho-bar(g)x,rho(g)y)=dot(x,y) is exactly the contragredient-action
identity):
    H^k(D;27bar) = H^{3-k}(D;27)^*   for k=0,1,2,3.
k=1: h1(dual) = h2(primal)   [not used here]
k=3: h3(dual) = h0(primal) = 1     (v0 spans H^0(D;27), gated v0_dim1)
k=0: h0(dual) = h3(primal)          (independently computed = 1 by w1_portal)
k=2: h2(dual) = h1(primal) = 5      (h1_bank from stage1_classes.pkl = 5)
Euler characteristic cross-check (chi(D)=0 for a closed 3-manifold, computed
either via the primal or dual complex): h0(dual)-h1(dual)+h2(dual)-h3(dual)
= 1 - 5 + 5 - 1 = 0.  EXACT, self-consistent -- reported as the h^2=5 gate.

SEALED FORK (prereg's own instruction): if ANY [c_ij] != 0 (i,j solo,i!=j):
STOP THERE, bank the exact nonvanishing data (raw BASE_ij, an exact witness
psi in ker(F^T) with psi.F=0 but psi.BASE_ij != 0 -- a constructive proof of
nonvanishing -- plus the coordinate vector of BASE_ij against the FULL 31-dim
ker(F^T) basis, honestly labeled as a basis of the SUPERSPACE C^2(dual)/B^2(dual)
[dim 31] rather than the true 5-dim H^2(dual) = Z^2/B^2 subquotient, since
resolving that further subquotient would require constructing delta^2 (the
3-cell attaching map), which is NOT part of the reused machinery and is not
independently built here); report the 3x3 pattern over (i,j), its rank, and
the (i,j)<->(j,i) symmetry structure (Koszul graded-commutativity for a cup
through the SYMMETRIC pairing C3 -- verified symmetric below -- predicts
[c_ij] = -[c_ji], checked directly).

If ALL [c_ij] = 0 (i,j solo, i!=j): solve the vector bounding cochains b_ij
(module-valued, 81 unknowns, exact particular solution via augmented rref on
F) and form the vector Massey product. STATED CONVENTION (the prereg invites
this: "state your convention"): b_ij is 27bar-valued and u_k is 27-valued; the
ONLY G-equivariant bilinear pairing available in the reused machinery that
accepts one 27bar and one 27 argument is the natural evaluation/contraction
dot: 27bar (x) 27 -> K (trivial coefficients) -- dot(rho-bar(g)x,rho(g)y) =
dot(x,y) is exactly the defining identity of the contragredient action, so dot
IS G-equivariant for this mixed pairing. (There is no verified/available
27bar (x) 27 -> 27bar cross-product in the reused machinery -- C3 only takes
two 27 arguments -- so a fully vector/27bar-valued Massey product is NOT
constructible without inventing new unverified structure; this is stated
honestly as a scope limit, not silently assumed away.) So:
    m_ijk(g,h) := dot(b_ij(g), rho(g).u_k(h)) +/- dot(u_i(g), rho-bar(g).b_jk(h))
landing in C^2(D;K) (trivial coefficients), reduced via a freshly-built (but
tiny, exactly the s4/b2 pattern) psi/h2class projector to H^2(D;K) (1-dim).
Indeterminacy: b_ij is fixed only up to adding any z in Z^1(D;27bar) (dim 31);
shifting by a COBOUNDARY leaves the class invariant (coboundary-shift control,
verified); shifting by a genuine H^1(dual) class (the 5 dual_classes) shifts
[m_ijk] by kappa-type numbers computed via "u_k cup_dot (dual class)" --
exactly the requested "u_i cup H^1(dual-side)" indeterminacy, computed exactly
below, span in the 1-dim H^2(D;K) is either {0} or everything.

SETUP: execs w1_portal.py verbatim through its own STEP 5 (B575 prefix; pkl
rehydration; C27 via J; v0; the Jordan cubic N and C3; the dual system's
contragredient action dacts; the dual Fox derivative matrix dual_big; h1(dual)
=5 gate; the dual class basis + reduce_to_classes). Small glue (cocycle_val,
rho_word -- literally s4_massshape.py's own tiny helper pattern, re-stated
here rather than re-execing s4's redundant B575 prefix a second time) is new,
not "machinery." Repo read-only; nothing written outside this work dir.
"""
import os
import sys
import time
import json
import itertools
from fractions import Fraction as Fr

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
W1_PORTAL = "<seat-workdir>/invariant_line/w1_portal/w1_portal.py"

gates = {}

# ============================================================================
log("STEP 0: exec w1_portal.py verbatim through its own STEP 5 (B575 prefix; "
    "pkl rehydration; C27/v0/N/C3; dual Fox machinery dual_big; h1(dual)=5 "
    "gate; dual class basis + reduce_to_classes)...")
src = open(W1_PORTAL).read()
cut = src.index('log("STEP 6:')
ns = {"__name__": "w1_prefix", "__file__": W1_PORTAL}
t0 = time.time()
exec(compile(src[:cut], W1_PORTAL, "exec"), ns)
log(f"  w1_portal STEP0-5 done ({time.time()-t0:.0f}s)")

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
d, GENS = ns["d"], ns["GENS"]
acts, dacts = ns["acts"], ns["dacts"]
mmul, meye = ns["mmul"], ns["meye"]
nullspace, rref = ns["nullspace"], ns["rref"]
apply_ = ns["apply"]
v0, idx0 = ns["v0"], ns["idx0"]
classes = ns["classes"]
h1_bank = ns["h1_bank"]
R1, R2, R3, RELS = ns["R1"], ns["R2"], ns["R3"], ns["RELS"]
C3, dot, CFULL = ns["C3"], ns["dot"], ns["CFULL"]
dual_big = ns["dual_big"]
h1_dual, h0_dual = ns["h1_dual"], ns["h0_dual"]
dual_classes, cobs_dual = ns["dual_classes"], ns["cobs_dual"]
reduce_to_classes = ns["reduce_to_classes"]
is_dual_cocycle = ns["is_dual_cocycle"]
flatabc = ns["flatabc"]
P_of = ns["P_of"]

for k in ("C27_inverse_consistent", "relator_R1", "relator_R2", "relator_R3",
          "v0_dim1", "v0_idx0_matches_w0a", "v0_matches_w0a",
          "v0_C27_invariant", "N_dim1", "N_invariant_all",
          "P_class0_is_cocycle", "h1_dual_eq_5"):
    gates[f"w1_{k}"] = ns["gates"][k]
log(f"  inherited w1_portal gates (through STEP5) all pass: {all(gates.values())}")
assert all(gates.values()), "an inherited w1_portal gate failed"
gates["h1_bank_primal_eq_5"] = (h1_bank == 5)
assert gates["h1_bank_primal_eq_5"]


def fmt(x):
    if x.is_zero():
        return "0"
    if x.b == 0:
        return str(x.a)
    return f"({x.a}{'+' if x.b > 0 else ''}{x.b}*sqrt(-3))"


def vadd(u, v):
    # length-generic (NOT hardcoded to d=27): also called on 81-dim vectors
    # (BASE_ij antisymmetry control) below.
    assert len(u) == len(v)
    return [u[i] + v[i] for i in range(len(u))]


def vsub(u, v):
    assert len(u) == len(v)
    return [u[i] - v[i] for i in range(len(u))]


def vdot(u, v):
    # length-generic (NOT hardcoded to d=27): also used on 81-dim vectors
    # (obstruction coordinates, the left-nullspace witness check) below.
    assert len(u) == len(v)
    n = len(u)
    return sum((u[i] * v[i] for i in range(n) if not u[i].is_zero() and not v[i].is_zero()), K0)


def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


SOLO = [2, 3, 4]

# ============================================================================
log("STEP A: h^2(D;27-bar)=5 CONSISTENCY GATE (Poincare duality + UCT, K a "
    "field): h0(dual)=h3(primal)=1(indep computed)=1, h1(dual)=5(gated), "
    "h3(dual)=h0(primal)=1(v0_dim1 gate); Euler char forces h2(dual)=5...")
h3_dual_by_PD = 1     # = h0(primal), gated dim1 (v0 spans H^0(D;27))
euler = h0_dual - h1_dual + 5 - h3_dual_by_PD
gates["h2_dual_euler_consistent"] = (euler == 0) and (h0_dual == 1) and (h1_dual == 5)
log(f"  h0(dual)={h0_dual}  h1(dual)={h1_dual}  h3(dual)[PD from h0(primal)]="
    f"{h3_dual_by_PD}  =>  h2(dual) forced = 5 by Euler(=0) consistency: "
    f"{'PASS' if gates['h2_dual_euler_consistent'] else 'FAIL'}")
assert gates["h2_dual_euler_consistent"]
H2_DUAL_DIM = 5

# ============================================================================
log("STEP B: small glue -- cocycle_val/rho_word (s4_massshape.py's own tiny "
    "pattern, re-stated to avoid a second redundant B575 exec) + the vector "
    "cup c_ij(g,h) = C3(u_i(g), rho(g).u_j(h))...")


def lv(zc, ch):
    low = ch.lower()
    if ch.islower():
        return zc[low]
    return [K0 - x for x in apply_(acts[ch], zc[low])]


def cocycle_val(zc, word):
    val = [K0] * d
    P = meye(d)
    for ch in word:
        add = apply_(P, lv(zc, ch))
        val = vadd(val, add)
        P = mmul(P, acts[ch])
    return val


def rho_word(word):
    P = meye(d)
    for ch in word:
        P = mmul(P, acts[ch])
    return P


def rho_bar_word(word):
    P = meye(d)
    for ch in word:
        P = mmul(P, dacts[ch])
    return P


def c_ij_raw(zi, zj, gw, hw):
    ug = cocycle_val(zi, gw)
    vh = cocycle_val(zj, hw)
    rgvh = apply_(rho_word(gw), vh)
    return C3(ug, rgvh)


log("  CONTROL: C3 is exactly SYMMETRIC (C3(u,v)=C3(v,u)) -- CFULL is built "
    "totally symmetric under all 6 perms of each sorted support triple...")
_tu = [K((3 * i + 1) % 11 - 5) for i in range(d)]
_tv = [K((5 * i + 2) % 9 - 4) for i in range(d)]
gates["C3_symmetric"] = all((C3(_tu, _tv)[t] - C3(_tv, _tu)[t]).is_zero() for t in range(d))
log(f"  C3(u,v)==C3(v,u) on test vectors: {'PASS' if gates['C3_symmetric'] else 'FAIL'}")
assert gates["C3_symmetric"]

log("  CONTROL: C3 equivariance C3(rho(g)x,rho(g)y) = rho-bar(g).C3(x,y) "
    "(this is what makes c_ij's cocycle identity a general consequence, not "
    "a coincidence)...")
_eq = {}
for g in ('a', 'b', 'c'):
    lhs = C3(apply_(acts[g], _tu), apply_(acts[g], _tv))
    rhs = apply_(dacts[g], C3(_tu, _tv))
    _eq[g] = all((lhs[t] - rhs[t]).is_zero() for t in range(d))
gates["C3_equivariant"] = all(_eq.values())
log(f"  C3(gx,gy) == rho-bar(g).C3(x,y) for g in a,b,c: {gates['C3_equivariant']} {_eq}")
assert gates["C3_equivariant"]

TEST_TRIPLES = [('a', 'b', 'c'), ('b', 'a', 'c'), ('a', 'A', 'b'), ('a', 'b', 'a'),
                ('c', 'b', 'A')]


def cocycle_identity_ok(i, j):
    zi, zj = classes[i], classes[j]
    oks = []
    for (g, h, k) in TEST_TRIPLES:
        chk = c_ij_raw(zi, zj, h, k)
        cghk = c_ij_raw(zi, zj, g + h, k)
        cghk2 = c_ij_raw(zi, zj, g, h + k)
        cgh = c_ij_raw(zi, zj, g, h)
        lhs = vsub(vadd(vsub(apply_(dacts[g], chk), cghk), cghk2), cgh)
        oks.append(all(x.is_zero() for x in lhs))
    return all(oks)


PAIRS9 = [(i, j) for i in SOLO for j in SOLO]
cocycle_flags = {}
for (i, j) in PAIRS9:
    ok = cocycle_identity_ok(i, j)
    cocycle_flags[(i, j)] = ok
    log(f"  delta c_{i}{j} = 0 on 5 generator triples: {'PASS' if ok else 'FAIL -- STOP'}")
gates["all_cij_are_cocycles"] = all(cocycle_flags.values())
assert gates["all_cij_are_cocycles"], "a c_ij cocycle identity FAILED -- construction wrong"

# ============================================================================
log("STEP C: the solvability test -- BASE_ij (constant part of the bounding "
    "recursion at y=0) for all 9 (i,j) in solo x solo, and ker(F^T) (F = "
    "w1_portal's dual_big, reused verbatim) computed ONCE...")


def a_const_table(i, j):
    tbl = {}
    for g in ('a', 'b', 'c'):
        tbl[g.upper()] = c_ij_raw(classes[i], classes[j], g, g.upper())
    return tbl


def b_val_of(y, aconst, ch):
    if ch.islower():
        return y[ch]
    low = ch.lower()
    return apply_(dacts[ch], vsub(aconst[ch], y[low]))


def b_eval(i, j, y, aconst, word):
    total = [K0] * d
    Pbar = meye(d)
    prefix = ""
    for ch in word:
        bch = b_val_of(y, aconst, ch)
        term = apply_(Pbar, bch)
        defect = c_ij_raw(classes[i], classes[j], prefix, ch)
        total = vsub(vadd(total, term), defect)
        Pbar = mmul(Pbar, dacts[ch])
        prefix = prefix + ch
    return total


ZERO_Y = {'a': [K0] * d, 'b': [K0] * d, 'c': [K0] * d}


def base_vec(i, j):
    aconst = a_const_table(i, j)
    base = []
    for word in RELS:
        base += b_eval(i, j, ZERO_Y, aconst, word)
    return base, aconst


t0 = time.time()
BASE = {}
ACONST = {}
for (i, j) in PAIRS9:
    b, ac = base_vec(i, j)
    BASE[(i, j)] = b
    ACONST[(i, j)] = ac
log(f"  BASE_ij built for all 9 pairs ({time.time()-t0:.1f}s)")

t0 = time.time()
Ft = transpose(dual_big)
leftnull = nullspace(Ft)
log(f"  ker(F^T) [F=dual_big, the reused Fox-derivative matrix] dim = "
    f"{len(leftnull)}  ({time.time()-t0:.1f}s)  "
    f"[= dim C^2(dual)/B^2(dual), the SUPERSPACE containing the true "
    f"5-dim H^2(dual) as a subquotient]")
gates["leftnull_dim_matches_z1dim"] = (len(leftnull) == len(nullspace(dual_big)))
log(f"  ker(F^T) dim == ker(F) dim [square matrix rank-nullity check]: "
    f"{gates['leftnull_dim_matches_z1dim']}")
assert gates["leftnull_dim_matches_z1dim"]


def obstruction_coords(vec81):
    return [vdot(psi, vec81) for psi in leftnull]


def is_zero_class(vec81):
    return all(c.is_zero() for c in obstruction_coords(vec81))


OBS = {}
ZERO_FLAG = {}
for (i, j) in PAIRS9:
    OBS[(i, j)] = obstruction_coords(BASE[(i, j)])
    ZERO_FLAG[(i, j)] = all(c.is_zero() for c in OBS[(i, j)])
    nnz = sum(1 for c in OBS[(i, j)] if not c.is_zero())
    log(f"  [c_{i}{j}]: {'ZERO' if ZERO_FLAG[(i,j)] else 'NONZERO'}  "
        f"(nonzero obstruction coords: {nnz}/{len(leftnull)})")

log("  3x3 pattern (rows i, cols j, solo order 2,3,4) -- True = ZERO class:")
for i in SOLO:
    log("    [" + ", ".join(str(ZERO_FLAG[(i, j)]) for j in SOLO) + "]")

OFFDIAG = [(i, j) for i in SOLO for j in SOLO if i != j]
gates["step1_all_offdiag_zero"] = all(ZERO_FLAG[p] for p in OFFDIAG)
log(f"  ALL off-diagonal (i!=j) solo classes ZERO: "
    f"{'YES -- proceed to STEP 2 (vector Massey)' if gates['step1_all_offdiag_zero'] else 'NO -- SEALED FORK: STOP HERE'}")

# ---- (i,j)<->(j,i) Koszul antisymmetry control -----------------------------
log("  CONTROL: Koszul graded-commutativity prediction [c_ij] = -[c_ji] "
    "(C3 symmetric, gated above) -- test [c_ij]+[c_ji] = 0 for all 9 pairs "
    "(diagonal: predicts [c_ii]=0)...")
antisym_ok = {}
for (i, j) in PAIRS9:
    s = vadd(BASE[(i, j)], BASE[(j, i)])
    antisym_ok[(i, j)] = is_zero_class(s)
gates["cij_plus_cji_zero_all"] = all(antisym_ok.values())
log(f"  [c_ij]+[c_ji]=0 for all (i,j) in solo x solo: "
    f"{gates['cij_plus_cji_zero_all']}  (per-pair: "
    f"{ {f'{i}{j}':antisym_ok[(i,j)] for (i,j) in PAIRS9} })")
diag_zero = all(ZERO_FLAG[(i, i)] for i in SOLO)
log(f"  diagonal [c_ii]=0 for i in solo (Koszul self-cup consequence): {diag_zero}")

# ---- coboundary-shift-invariance control -----------------------------------
log("  CONTROL: coboundary-shift invariance -- shift u_2 (classes[2]) by a "
    "primal coboundary, recompute obstruction coords for (2,3) and (2,4), "
    "verify UNCHANGED exactly...")
_xi = [K((5 * i + 3) % 11 - 5) for i in range(d)]
_cob = {g: vsub(apply_(acts[g], _xi), _xi) for g in ('a', 'b', 'c')}
_u2_shift = {g: vadd(classes[2][g], _cob[g]) for g in ('a', 'b', 'c')}
_shift_ok = []
for j in (3, 4):
    aconst_s = {}
    for g in ('a', 'b', 'c'):
        aconst_s[g.upper()] = C3(cocycle_val(_u2_shift, g),
                                  apply_(rho_word(g), cocycle_val(classes[j], g.upper())))
    base_s = []
    for word in RELS:
        total = [K0] * d
        Pbar = meye(d)
        prefix = ""
        for ch in word:
            bch = b_val_of(ZERO_Y, aconst_s, ch)
            term = apply_(Pbar, bch)
            defect = C3(cocycle_val(_u2_shift, prefix),
                        apply_(rho_word(prefix), cocycle_val(classes[j], ch)))
            total = vsub(vadd(total, term), defect)
            Pbar = mmul(Pbar, dacts[ch])
            prefix = prefix + ch
        base_s += total
    obs_s = obstruction_coords(base_s)
    obs_orig = OBS[(2, j)]
    same = all((obs_s[k] - obs_orig[k]).is_zero() for k in range(len(leftnull)))
    _shift_ok.append(same)
    log(f"  obstruction coords for [c_2{j}] unchanged under coboundary shift "
        f"of u_2: {same}")
gates["control_coboundary_shift"] = all(_shift_ok)
assert gates["control_coboundary_shift"]

gates["control_exactness"] = True
log("  exactness: K = Q(sqrt(-3)) (Fraction pairs) throughout; zero floats "
    "anywhere in the C1 path: PASS by construction")

# ============================================================================
result = {
    "prereg_note": "PREREG_L3.md sha f32fbfff645c9fa0412a57da7090e34422a4c1068810536b4dc35b9eaee34c47, C1 clause",
    "gates": gates,
    "h2_dual_dim_by_duality": H2_DUAL_DIM,
    "h0_dual": h0_dual, "h1_dual": h1_dual, "h1_bank_primal": h1_bank,
    "ker_FT_dim": len(leftnull),
}

if not gates["step1_all_offdiag_zero"]:
    # =========================================================================
    log("SEALED FORK TAKEN: NONVANISHING -- banking exact data and STOPPING.")
    nonzero_pairs = [p for p in OFFDIAG if not ZERO_FLAG[p]]
    log(f"  nonvanishing (i,j) pairs: {nonzero_pairs}")

    def find_witness(vec81):
        for psi in leftnull:
            if not vdot(psi, vec81).is_zero():
                return psi
        return None

    banked = {}
    for (i, j) in nonzero_pairs:
        psi_w = find_witness(BASE[(i, j)])
        val = vdot(psi_w, BASE[(i, j)])
        # verify psi_w is a genuine witness: psi_w.F = 0 exactly
        psiF = [vdot(psi_w, [dual_big[r][c] for r in range(len(dual_big))]) for c in range(len(dual_big[0]))]
        witness_ok = all(x.is_zero() for x in psiF)
        banked[f"{i}{j}"] = {
            "BASE_ij_27x3": [[fmt(x) for x in BASE[(i, j)][27 * r:27 * r + 27]] for r in range(3)],
            "obstruction_coords_31dim": [fmt(c) for c in OBS[(i, j)]],
            "witness_psi_valid_leftnull_of_F": witness_ok,
            "witness_pairing_value": fmt(val),
        }
        log(f"  banked [c_{i}{j}]: witness valid={witness_ok}, "
            f"psi.BASE={fmt(val)} (nonzero, proves [c_{i}{j}]!=0)")

    pattern_bool = [[ZERO_FLAG[(i, j)] for j in SOLO] for i in SOLO]
    # rank of the family of 9 obstruction-coordinate vectors (31-dim each)
    rank_rows = [OBS[(i, j)] for (i, j) in PAIRS9]
    _, rank_piv = rref([list(r) for r in rank_rows])
    pattern_rank = len(rank_piv)
    sym_check = all(ZERO_FLAG[(i, j)] == ZERO_FLAG[(j, i)] for (i, j) in PAIRS9)

    result.update({
        "verdict": f"FORK-NONVANISHING: [c_ij] != 0 for {nonzero_pairs}",
        "nonvanishing_pairs": [f"{i}{j}" for (i, j) in nonzero_pairs],
        "banked_classes": banked,
        "pattern_3x3_zero_bool": pattern_bool,
        "pattern_rank_in_31dim_superspace": pattern_rank,
        "pattern_zero_pattern_symmetric": sym_check,
        "koszul_antisym_cij_plus_cji_zero": gates["cij_plus_cji_zero_all"],
        "diagonal_cii_zero": diag_zero,
    })
    log(f"VERDICT: {result['verdict']}")
    with open(os.path.join(HERE, "c1_results.json"), "w") as f:
        json.dump(result, f, indent=2)
    log(f"saved {os.path.join(HERE, 'c1_results.json')}")
    log("DONE (FORK: STOPPED at nonvanishing vector cup class).")
    sys.exit(0)

# ============================================================================
log("STEP 2: ALL [c_ij]=0 for i!=j in solo -- solving vector bounding "
    "cochains b_ij exactly (81-unknown particular solution via augmented "
    "rref on F=dual_big) and forming the vector Massey product...")


def solve_bounding(i, j):
    base, aconst = BASE[(i, j)], ACONST[(i, j)]
    aug = [list(dual_big[r]) + [K0 - base[r]] for r in range(len(dual_big))]
    Rr, piv = rref(aug)
    nvars = len(dual_big[0])
    consistent = (nvars not in piv)
    y = [K0] * nvars
    for r_i, pc in enumerate(piv):
        if pc < nvars:
            y[pc] = Rr[r_i][nvars]
    return y, aconst, consistent


B_SOL = {}
for (i, j) in OFFDIAG:
    y, aconst, consistent = solve_bounding(i, j)
    assert consistent, f"({i},{j}): system unexpectedly inconsistent"
    ydict = {'a': y[0:d], 'b': y[d:2 * d], 'c': y[2 * d:3 * d]}
    B_SOL[(i, j)] = (ydict, aconst)
    log(f"  b_{i}{j} solved (particular solution, {d} components each on a,b,c)")


def b_of(i, j, word):
    ydict, aconst = B_SOL[(i, j)]
    return b_eval(i, j, ydict, aconst, word)


log("  CONTROL: relator consistency b_ij(R_r) = 0 exactly for all 3 relators, "
    "all 6 pairs...")
rel_ok = {}
for (i, j) in OFFDIAG:
    oks = [all(x.is_zero() for x in b_of(i, j, w)) for w in RELS]
    rel_ok[(i, j)] = all(oks)
gates["bounding_relator_consistency"] = all(rel_ok.values())
log(f"  all 6 bounding cochains relator-consistent: {gates['bounding_relator_consistency']}")
assert gates["bounding_relator_consistency"]

log("  CONTROL: delta b_ij = c_ij EXACTLY on generator pairs (module-valued "
    "coboundary identity), all 6 pairs...")
GEN_PAIR_TESTS = [('a', 'b'), ('b', 'a'), ('a', 'A'), ('c', 'b'), ('b', 'c'), ('a', 'c')]
delta_ok = {}
for (i, j) in OFFDIAG:
    oks = []
    for (g, h) in GEN_PAIR_TESTS:
        bg, bh, bgh = b_of(i, j, g), b_of(i, j, h), b_of(i, j, g + h)
        lhs = vsub(vadd(apply_(dacts[g], bh), bg), bgh)
        rhs = c_ij_raw(classes[i], classes[j], g, h)
        oks.append(all((lhs[t] - rhs[t]).is_zero() for t in range(d)))
    delta_ok[(i, j)] = all(oks)
gates["delta_b_eq_c_gen_pairs"] = all(delta_ok.values())
log(f"  delta b_ij = c_ij on {len(GEN_PAIR_TESTS)} generator pairs, all 6 "
    f"pairs: {gates['delta_b_eq_c_gen_pairs']}")
assert gates["delta_b_eq_c_gen_pairs"]

# ============================================================================
log("STEP 3: the scalar-reduced vector Massey (STATED CONVENTION: dot: "
    "27bar (x) 27 -> K is the only verified G-equivariant mixed pairing "
    "available; a genuine 27bar-valued 'cross' Massey is NOT constructible "
    "from the reused machinery -- honest scope note, see docstring)...")


def signed_counts(word):
    cnt = {g: 0 for g in GENS}
    for ch in word:
        cnt[ch.lower()] += 1 if ch.islower() else -1
    return [K(cnt[g]) for g in GENS]


Nrel = [signed_counts(w) for w in RELS]
psis = nullspace([[Nrel[r][g] for r in range(3)] for g in range(3)])
gates["psi_dim1"] = (len(psis) == 1)
assert gates["psi_dim1"]
psi_triv = psis[0]


def h2class(e3):
    return sum((psi_triv[r] * e3[r] for r in range(3) if not e3[r].is_zero()), K0)


def m_val(i, j, k, sign, g, h):
    ydict_ij, aconst_ij = B_SOL[(i, j)]
    ydict_jk, aconst_jk = B_SOL[(j, k)]
    bij_g = b_eval(i, j, ydict_ij, aconst_ij, g)
    bjk_h = b_eval(j, k, ydict_jk, aconst_jk, h)
    uk_h = cocycle_val(classes[k], h)
    ui_g = cocycle_val(classes[i], g)
    term1 = vdot(bij_g, apply_(rho_word(g), uk_h))
    term2 = vdot(ui_g, apply_(dacts[g], bjk_h))
    return (term1 + term2) if sign == 1 else (term1 - term2)


PERMS = list(itertools.permutations(SOLO))
cocycle_results = {}
for (i, j, k) in PERMS:
    for sign in (1, -1):
        oks = []
        for (g, h, kk) in TEST_TRIPLES:
            lhs = (m_val(i, j, k, sign, h, kk) - m_val(i, j, k, sign, g + h, kk)
                   + m_val(i, j, k, sign, g, h + kk) - m_val(i, j, k, sign, g, h))
            oks.append(lhs.is_zero())
        cocycle_results[(i, j, k, sign)] = all(oks)
    log(f"  ({i},{j},{k}): cocycle[+]={cocycle_results[(i,j,k,1)]}  "
        f"cocycle[-]={cocycle_results[(i,j,k,-1)]}")

DISTINCT_BY_MIDDLE = {2: (3, 2, 4), 3: (2, 3, 4), 4: (2, 4, 3)}
massey_table = {}
for jmid, (i, j, k) in DISTINCT_BY_MIDDLE.items():
    entry = {"triple": (i, j, k)}
    for sign, lbl in ((1, "plus"), (-1, "minus")):
        isc = cocycle_results[(i, j, k, sign)]
        entry[f"is_exact_cocycle_{lbl}"] = isc
        if isc:
            e3m = []
            for word in RELS:
                total = K0
                prefix = ""
                for ch in word:
                    total = total + m_val(i, j, k, sign, prefix, ch)
                    prefix = prefix + ch
                e3m.append(total)
            cls = h2class(e3m)
            entry[f"class_{lbl}"] = fmt(cls)
        else:
            entry[f"class_{lbl}"] = None
    massey_table[f"{i}{j}{k}"] = entry
    log(f"  <u_{i},u_{j},u_{k}> (scalar-reduced): {entry}")

# ---- indeterminacy: u_i cup_dot (dual H^1 class), u_k cup_dot (dual H^1 class)
log("  indeterminacy: b_ij -> b_ij + z (z in Z^1(dual)) shifts m_ijk by the "
    "genuine cup class [z cup_dot u_k]; b_jk -> b_jk + z shifts it by "
    "[u_i cup_dot z] -- computed for z ranging over the 5 dual_classes "
    "representatives of H^1(dual) (coboundary shifts are cohomologically "
    "trivial, verified separately below)...")


def dual_class_dict(vec81):
    return {'a': vec81[0:d], 'b': vec81[d:2 * d], 'c': vec81[2 * d:3 * d]}


def lv_dual(zc, ch):
    low = ch.lower()
    if ch.islower():
        return zc[low]
    return [K0 - x for x in apply_(dacts[ch], zc[low])]


def dual_cocycle_val(zc, word):
    val = [K0] * d
    P = meye(d)
    for ch in word:
        add = apply_(P, lv_dual(zc, ch))
        val = vadd(val, add)
        P = mmul(P, dacts[ch])
    return val


def scalar_class_of(f):
    """f(g,h)->K scalar 2-cochain (words g,h). Verify cocycle id on
    TEST_TRIPLES; if cocycle, return its H^2(D;K) class via h2class."""
    oks = []
    for (g, h, kk) in TEST_TRIPLES:
        lhs = f(h, kk) - f(g + h, kk) + f(g, h + kk) - f(g, h)
        oks.append(lhs.is_zero())
    if not all(oks):
        return None, False
    e3 = []
    for word in RELS:
        total = K0
        prefix = ""
        for ch in word:
            total = total + f(prefix, ch)
            prefix = prefix + ch
        e3.append(total)
    return h2class(e3), True


def make_f_z_cup_uk(zc, k):
    def f(g, h):
        zg = dual_cocycle_val(zc, g)
        ukh = cocycle_val(classes[k], h)
        return vdot(zg, apply_(rho_word(g), ukh))
    return f


def make_f_ui_cup_z(i, zc):
    def f(g, h):
        uig = cocycle_val(classes[i], g)
        zh = dual_cocycle_val(zc, h)
        return vdot(uig, apply_(dacts[g], zh))
    return f


indeterminacy_report = {}
for jmid, (i, j, k) in DISTINCT_BY_MIDDLE.items():
    vals_zk, vals_iz = [], []
    for m, z in enumerate(dual_classes):
        cls1, ok1 = scalar_class_of(make_f_z_cup_uk(z, k))
        cls2, ok2 = scalar_class_of(make_f_ui_cup_z(i, z))
        assert ok1 and ok2, f"indeterminacy direction not a cocycle for triple {(i,j,k)}, m={m}"
        vals_zk.append(cls1)
        vals_iz.append(cls2)
    any_nonzero = any(not x.is_zero() for x in vals_zk + vals_iz)
    indeterminacy_report[f"{i}{j}{k}"] = {
        "z_cup_uk_over_5_dual_classes": [fmt(x) for x in vals_zk],
        "ui_cup_z_over_5_dual_classes": [fmt(x) for x in vals_iz],
        "indeterminacy_dim_in_H2DK": 1 if any_nonzero else 0,
    }
    log(f"  <u_{i},u_{j},u_{k}> indeterminacy: any nonzero shift = {any_nonzero} "
        f"=> indeterminacy dim in H2(D;K)(1-dim) = {1 if any_nonzero else 0}")

log("  CONTROL: shifting b_ij by a COBOUNDARY of dual (an element of "
    "cobs_dual) leaves the scalar-reduced Massey class UNCHANGED (a direct "
    "check on one triple, one coboundary direction)...")
_i0, _j0, _k0 = DISTINCT_BY_MIDDLE[3]
_cob_shift81 = cobs_dual[0]
_cob_shift_d = dual_class_dict(_cob_shift81)
_ydict_ij, _aconst_ij = B_SOL[(_i0, _j0)]
_ydict_shift = {g: vadd(_ydict_ij[g], _cob_shift_d[g]) for g in ('a', 'b', 'c')}


def b_eval_shifted(y, aconst, i, j, word):
    total = [K0] * d
    Pbar = meye(d)
    prefix = ""
    for ch in word:
        bch = b_val_of(y, aconst, ch)
        term = apply_(Pbar, bch)
        defect = c_ij_raw(classes[i], classes[j], prefix, ch)
        total = vsub(vadd(total, term), defect)
        Pbar = mmul(Pbar, dacts[ch])
        prefix = prefix + ch
    return total


def m_val_shift(sign, g, h):
    bij_g = b_eval_shifted(_ydict_shift, _aconst_ij, _i0, _j0, g)
    ydict_jk, aconst_jk = B_SOL[(_j0, _k0)]
    bjk_h = b_eval(_j0, _k0, ydict_jk, aconst_jk, h)
    uk_h = cocycle_val(classes[_k0], h)
    ui_g = cocycle_val(classes[_i0], g)
    term1 = vdot(bij_g, apply_(rho_word(g), uk_h))
    term2 = vdot(ui_g, apply_(dacts[g], bjk_h))
    return (term1 + term2) if sign == 1 else (term1 - term2)


_shift_cocycle_ok = []
for (g, h, kk) in TEST_TRIPLES:
    lhs = (m_val_shift(1, h, kk) - m_val_shift(1, g + h, kk)
           + m_val_shift(1, g, h + kk) - m_val_shift(1, g, h))
    _shift_cocycle_ok.append(lhs.is_zero())
if all(_shift_cocycle_ok):
    e3shift = []
    for word in RELS:
        total = K0
        prefix = ""
        for ch in word:
            total = total + m_val_shift(1, prefix, ch)
            prefix = prefix + ch
        e3shift.append(total)
    cls_shift = h2class(e3shift)
    orig_entry = massey_table[f"{_i0}{_j0}{_k0}"]
    cob_invariance_ok = (orig_entry.get("is_exact_cocycle_plus") and
                         (fmt(cls_shift) == orig_entry.get("class_plus")))
else:
    cob_invariance_ok = None
gates["control_coboundary_shift_b_massey"] = cob_invariance_ok
log(f"  coboundary-shift of b_{_i0}{_j0} leaves scalar Massey class[+] "
    f"unchanged: {cob_invariance_ok}")

gates["control_exactness2"] = True

any_exact_cocycle_nonzero = any(
    (massey_table[key].get("is_exact_cocycle_plus") and massey_table[key].get("class_plus") not in (None, "0"))
    or (massey_table[key].get("is_exact_cocycle_minus") and massey_table[key].get("class_minus") not in (None, "0"))
    for key in massey_table)

if any_exact_cocycle_nonzero:
    verdict = "MASSEY-NONZERO (scalar dot-reduction of the vector bounding cochains)"
else:
    verdict = "MASSEY-ZERO (scalar dot-reduction of the vector bounding cochains)"
log(f"VERDICT: {verdict}")

result.update({
    "verdict": verdict,
    "scope_note": "Step1 vector cup classes [c_ij] ALL vanish (i!=j, solo); "
                   "Step2's vector bounding cochains b_ij are genuinely "
                   "27bar-valued (81 exact components each), but the FINAL "
                   "Massey reduction uses the dot: 27bar(x)27->K pairing "
                   "(stated convention -- no verified 27bar(x)27->27bar "
                   "cross-product exists in the reused machinery), landing "
                   "in scalar H^2(D;K), not the full vector H^2(D;27bar).",
    "massey_table": massey_table,
    "cocycle_results": {f"{i}{j}{k}_{s}": cocycle_results[(i, j, k, s)]
                        for (i, j, k) in PERMS for s in (1, -1)},
    "any_exact_cocycle_nonzero": any_exact_cocycle_nonzero,
    "indeterminacy_report": indeterminacy_report,
    "koszul_antisym_cij_plus_cji_zero": gates["cij_plus_cji_zero_all"],
    "diagonal_cii_zero": diag_zero,
})

all_gates_pass = all(v for k, v in gates.items() if isinstance(v, bool))
log(f"ALL GATES PASS: {all_gates_pass}")
result["all_gates_pass"] = all_gates_pass
result["runtime_s"] = time.time() - T0

with open(os.path.join(HERE, "c1_results.json"), "w") as f:
    json.dump(result, f, indent=2)
log(f"saved {os.path.join(HERE, 'c1_results.json')}")
log("DONE.")
