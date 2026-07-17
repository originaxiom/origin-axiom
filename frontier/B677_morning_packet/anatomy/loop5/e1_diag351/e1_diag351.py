"""E1 -- THE LAMBDA^2 DIAGONAL (PREREG_L5.md E1 clause; loop5 cell E1).

D2 (loop4/d2_351) proved the vector cup [u_i cup u_j], i!=j in solo {2,3,4},
NONZERO in all three slots of 27(x)27 = 27bar (+) 351' (+) 351, and found the
GRADED SIGN RULE: the Lambda^2(27)=351 slot classes are SYMMETRIC under
i<->j ([c_ij]=[c_ji] there, not antisymmetric) -- so the 351-slot DIAGONAL
[c_ii] carries NO Koszul kill and may be nonzero. This cell computes the
351-slot component of [u_i cup u_i] for ALL FIVE classes i=0..4 (boundary
0,1 included -- D2 did only solo off-diagonal 2,3,4).

METHOD: identical Kronecker-cup / antisym-projection / witness machinery as
d2_351.py, TRIMMED to the Lambda^2(27) slot only (this cell has no business
with 27bar or 351' = Sym^2 complement, so their construction -- C3, the Gram
matrix, the iota splitting, and the S351p Fox matrix + its own ~70min
leftnull -- is not rebuilt here; skipping it is the main efficiency measure
along with the two below):
  1. STEP 0 execs c1_vecmassey.py verbatim, but CUT EARLIER than d2_351.py's
     own cut -- right before c1's own "STEP C" (27bar-slot BASE_ij/leftnull
     construction, ~450s of the ~700s d2_351.py STEP0 cost) -- since none of
     that 27bar-slot data is needed here; only acts, classes (all 5), RELS,
     SOLO, TEST_TRIPLES survive from the earlier STEP A/B section (~156s).
  2. d2_351.py's own STEP-1-through-10 pipeline is reused for the Lambda^2
     slot: build_slot_foxmat, base_vec_slot (generalized here to accept
     explicit z-cochain dicts instead of class indices, so the SAME code
     path serves classes[i],classes[j] pairs AND a coboundary-shifted
     cochain for the shift-invariance control), the witness search
     (obstruction_coords/find_witness/witness_valid) -- all copied verbatim
     in spirit, adapted only to drop the mode dispatch (antisym only).
     ONE BUG FIX vs d2_351.py: its own "conj_matrix_via_columns matches
     brute-force" spot-check recomputed the FULL dim x dim matrix once PER
     COMPARED COLUMN inside a list comprehension (recorded as an
     unexplained ~6536s gap in d2_351.py's own run log, STEP4->STEP5) --
     fixed here to compute it once per test and index into it.
  3. ker(F_L351^T) (dim 351x351... no: dim 1053x1053, 3 relators x 351) is
     recomputed via the SAME modular-discovery + exact-certificate method
     (e1_modnull.py, a verbatim copy of d2_modnull.py) -- the ~70min step
     the prereg's brief flags as expensive and asks to persist; done here
     and immediately dumped to a plain-Fraction-string-pair JSON cache
     (_leftnull_L351.json) so a rerun (if a later step needs debugging)
     does not repeat it.
  4. GATE (sealed falsifier, checked BEFORE any diagonal verdict is trusted):
     recompute ALL SIX of D2's banked off-diagonal L351 witnesses (not just
     the two named in the brief) against the fresh leftnull basis and
     cross-check byte-for-byte vs loop4/d2_351/d2_results.json. STOP if any
     mismatch.
  5. Diagonal BASE_ii, i=0..4: obstruction coords against the (gated) L351
     leftnull. Nonzero pairing => SELF-SPEAKS (witness exhibited, validity
     checked via psi.F_L351=0). Zero across the FULL (certified-complete)
     leftnull basis => attempt an EXACT coboundary solve F_L351.y=BASE_ii
     via e1_modnull.modular_solve_multi (modular discovery + CRT + rational
     reconstruction + exact verification over K) => SELF-SILENT if solved
     and verified; UNDECIDED only if that solve itself fails to close.
  6. Controls: slot cocycle identity delta(C_L351_ii)=0 on TEST_TRIPLES for
     EACH i=0..4 (also a raw-1-cocycle delta(u_i)=0 spot check, since
     classes 0,1 were never covered by c1_vecmassey's own solo-only cocycle
     gate); coboundary-shift invariance for ONE diagonal pair (i=2, matching
     the C1/D2 convention of shifting classes[2]) -- BOTH cup-factors shift
     simultaneously here (i=j), a strictly stronger test than the
     off-diagonal single-factor shift C1/D2 used; exactness (K=Q(sqrt(-3))
     Fraction pairs throughout, zero floats, by construction).

Set env var E1_SMOKE=1 to run a fast validation path: STEP0 + Fox-matrix
build + spot-check + ALL BASE_ij/BASE_ii constructions + cocycle-identity
controls, WITHOUT the ~60min modular leftnull/solve steps -- exits after
printing diagnostics. Used to shake out bugs before the full run.

Repo READ-ONLY (reads loop3/c1_vecmassey.py, loop4/d2_351/d2_results.json --
both under seat-work, not the origin-axiom repo); all writes confined to
<seat-workdir>/anatomy/loop5/e1_diag351/ only.
"""
import os
import sys
import time
import json
import pickle
import random
from fractions import Fraction as Fr

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
C1_PY = "<seat-workdir>/anatomy/loop3/c1_vecmassey/c1_vecmassey.py"
D2_JSON = "<seat-workdir>/anatomy/loop4/d2_351/d2_results.json"
CACHE_PATH = os.path.join(HERE, "_step0_cache.pkl")
LEFTNULL_CACHE_PATH = os.path.join(HERE, "_leftnull_L351.json")

SMOKE = bool(os.environ.get("E1_SMOKE"))

gates = {}


# ---- self-contained field K (same construction as d2_351.py / b575_prefix's
# own K, copied verbatim) + generic linear-algebra helpers -----------------
class K:
    __slots__ = ('a', 'b')

    def __init__(s, a=0, b=0):
        s.a = a if isinstance(a, Fr) else Fr(a)
        s.b = b if isinstance(b, Fr) else Fr(b)

    def __add__(s, o): return K(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return K(s.a - o.a, s.b - o.b)
    def __neg__(s): return K(-s.a, -s.b)
    def __mul__(s, o): return K(s.a * o.a - 3 * s.b * o.b, s.a * o.b + s.b * o.a)

    def inv(s):
        dd = s.a * s.a + 3 * s.b * s.b
        return K(s.a / dd, -s.b / dd)

    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def is_zero(s): return s.a == 0 and s.b == 0
    def __repr__(s): return f"({s.a}+{s.b}r)" if s.b else f"({s.a})"


K0, K1 = K(0), K(1)
d = 27
GENS = ['a', 'b', 'c']


def mzero(n, m):
    return [[K0] * m for _ in range(n)]


def meye(n):
    M = mzero(n, n)
    for i in range(n):
        M[i][i] = K1
    return M


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    Bt = list(zip(*B))
    out = []
    for i in range(n):
        Ai = A[i]
        row = []
        for j in range(m):
            Bj = Bt[j]
            s = K0
            for t in range(k):
                x = Ai[t]
                if not x.is_zero():
                    y = Bj[t]
                    if not y.is_zero():
                        s = s + x * y
            row.append(s)
        out.append(row)
    return out


def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def apply_(M, v):
    return [sum((M[i][k] * v[k] for k in range(len(v)) if not v[k].is_zero()), K0)
            for i in range(len(M))]


def vadd(u, v):
    return [u[i] + v[i] for i in range(len(u))]


def vsub(u, v):
    return [u[i] - v[i] for i in range(len(u))]


def vdot(u, v):
    n = len(u)
    return sum((u[i] * v[i] for i in range(n) if not u[i].is_zero() and not v[i].is_zero()), K0)


def fmt(x):
    if x.is_zero():
        return "0"
    if x.b == 0:
        return str(x.a)
    return f"({x.a}{'+' if x.b > 0 else ''}{x.b}*sqrt(-3))"


def k_to_pod(x):
    """Recursively converts K-LIKE instances (duck-typed by class name, NOT
    isinstance against OUR OWN K class -- the actual data produced by the
    exec'd c1/w1/B575 prefix chain are instances of a DIFFERENT (but
    structurally identical) K class defined inside that dynamic exec
    namespace; isinstance would silently fail to match it, which is exactly
    why d2_351.py's own STEP0 cache-write failed with a PicklingError
    ("Can't pickle <class 'b575_prefix.K'>") -- fixed here) into plain
    (numerator,denominator) int tuples, pickle-safe regardless of which
    dynamic K class produced them."""
    if type(x).__name__ == "K" and hasattr(x, "a") and hasattr(x, "b"):
        return ("K", x.a.numerator, x.a.denominator, x.b.numerator, x.b.denominator)
    if isinstance(x, list):
        return [k_to_pod(e) for e in x]
    if isinstance(x, dict):
        return {kk: k_to_pod(v) for kk, v in x.items()}
    if isinstance(x, tuple):
        return tuple(k_to_pod(e) for e in x)
    return x


def pod_to_k(x):
    if isinstance(x, tuple) and len(x) == 5 and x[0] == "K":
        return K(Fr(x[1], x[2]), Fr(x[3], x[4]))
    if isinstance(x, list):
        return [pod_to_k(e) for e in x]
    if isinstance(x, dict):
        return {kk: pod_to_k(v) for kk, v in x.items()}
    if isinstance(x, tuple):
        return tuple(pod_to_k(e) for e in x)
    return x


# ============================================================================
log("STEP 0: exec c1_vecmassey.py verbatim, cut EARLIER than d2_351.py's own "
    "cut -- right before c1's STEP C (27bar-slot BASE_ij/leftnull; not needed "
    "here) -- so only acts, classes (all 5), RELS, SOLO, TEST_TRIPLES survive "
    "from c1's STEP A/B (~156s of c1's own ~700s total, per its own run log).")

_cache_ok = False
if os.path.exists(CACHE_PATH):
    try:
        with open(CACHE_PATH, "rb") as f:
            cache_pod = pickle.load(f)
        _cache_ok = True
    except Exception as e:
        log(f"  stale/corrupt cache at {CACHE_PATH} ({e!r}) -- deleting, full re-exec")
        os.remove(CACHE_PATH)

if _cache_ok:
    log(f"  loading cached STEP0 products from {CACHE_PATH}...")
    t0 = time.time()
    acts = pod_to_k(cache_pod["acts"])
    classes = pod_to_k(cache_pod["classes"])
    RELS = cache_pod["RELS"]
    SOLO = cache_pod["SOLO"]
    TEST_TRIPLES = cache_pod["TEST_TRIPLES"]
    for k, v in cache_pod["c1_gates_recorded"].items():
        gates[f"c1_{k}"] = v
    log(f"  cache loaded ({time.time()-t0:.1f}s)")
else:
    src = open(C1_PY).read()
    cut = src.index('log("STEP C:')
    ns = {"__name__": "c1_prefix_e1", "__file__": C1_PY}
    t0 = time.time()
    exec(compile(src[:cut], C1_PY, "exec"), ns)
    log(f"  c1_vecmassey STEP0-B done ({time.time()-t0:.0f}s)")

    assert ns["d"] == d and ns["GENS"] == GENS, "dimension/generator mismatch vs c1"
    acts = ns["acts"]
    classes = ns["classes"]
    RELS = ns["RELS"]
    SOLO = ns["SOLO"]
    TEST_TRIPLES = ns["TEST_TRIPLES"]
    for k in list(ns["gates"].keys()):
        gates[f"c1_{k}"] = ns["gates"][k]

    cache_pod = {
        "acts": k_to_pod(acts), "classes": k_to_pod(classes),
        "RELS": RELS, "SOLO": SOLO, "TEST_TRIPLES": TEST_TRIPLES,
        "c1_gates_recorded": ns["gates"],
    }
    try:
        with open(CACHE_PATH, "wb") as f:
            pickle.dump(cache_pod, f)
        log(f"  cached STEP0 products to {CACHE_PATH} (future reruns skip the exec)")
    except Exception as e:
        log(f"  cache SKIPPED (non-fatal: {e!r}) -- proceeding without cache")

assert len(classes) == 5, f"expected 5 classes (H^1 dim), got {len(classes)}"
assert SOLO == [2, 3, 4], f"unexpected SOLO={SOLO}"
BOUNDARY_BORN = [0, 1]
SOLO_INHERITED = [2, 3, 4]
ALL_I = [0, 1, 2, 3, 4]

_inherited_bool_gates = {k: v for k, v in gates.items() if isinstance(v, bool)}
log(f"  inherited c1 (STEP A/B only, no fork-outcome key at this cut) gates "
    f"all pass: {all(_inherited_bool_gates.values())}")
assert all(_inherited_bool_gates.values()), "an inherited c1 gate failed"

# ---- small glue functions, restated verbatim (not cache-picklable; only the
# CFULL-free acts/classes DATA they close over is) --------------------------


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


HALF = K(Fr(1, 2))


def madd27(A, B):
    return [[A[i][j] + B[i][j] for j in range(d)] for i in range(d)]


def msub27(A, B):
    return [[A[i][j] - B[i][j] for j in range(d)] for i in range(d)]


def mscale27(c, A):
    return [[c * A[i][j] for j in range(d)] for i in range(d)]


def outer(x, y):
    return [[x[p] * y[q] for q in range(d)] for p in range(d)]


def conj_action(A, M):
    """Structured Kronecker action: g.M = A @ M @ A^T -- cost O(27^3), NEVER
    a dense 351x351 multiply."""
    return mmul(mmul(A, M), transpose(A))


def antisym_part(M):
    return mscale27(HALF, msub27(M, transpose(M)))


def zero27():
    return [[K0] * d for _ in range(d)]


# ============================================================================
log("STEP 1: Lambda^2(27) basis index set (dim 351, antisymmetric matrices)...")
ANTISYM_IDX = [(i, j) for i in range(d) for j in range(i + 1, d)]
DIM_A = len(ANTISYM_IDX)
log(f"  dim Lambda^2(27) = {DIM_A}  (expect 351)")
gates["dim_L351_correct"] = (DIM_A == 351)
assert gates["dim_L351_correct"]


def M_to_vec_antisym(Mm):
    return [Mm[i][j] for (i, j) in ANTISYM_IDX]


def vec_to_M_antisym(v):
    Mm = zero27()
    for k, (i, j) in enumerate(ANTISYM_IDX):
        Mm[i][j] = v[k]
        Mm[j][i] = K0 - v[k]
    return Mm


def conj_matrix_via_columns(P, BASIS_IDX):
    """dim x dim matrix representing M -> P@M@P^T restricted to the antisym
    basis, built via O(dim^2) using P's OWN columns -- the structured-operator
    trick, never a dense dim x dim matrix multiply. Computed ONCE per call
    (the d2_351.py spot-check called this inside a per-column list
    comprehension -- an unexplained ~6536s cost in that script's own run log,
    STEP4->STEP5 -- fixed here by computing it once and indexing)."""
    dim = len(BASIS_IDX)
    cols = [[P[p][c] for p in range(d)] for c in range(d)]
    out = [[K0] * dim for _ in range(dim)]
    for k, (i0, j0) in enumerate(BASIS_IDX):
        coli, colj = cols[i0], cols[j0]
        for m, (i1, j1) in enumerate(BASIS_IDX):
            val = coli[i1] * colj[j1] - colj[i1] * coli[j1]
            out[m][k] = val
    return out


log("  CONTROL: conj_matrix_via_columns matches brute-force conj_action "
    "(spot checks, computed ONCE per test -- the d2_351.py bug fixed)...")
random.seed(0)
_ok = True
FASTMAT_TEST = {}
for g in ('a', 'b', 'c'):
    FASTMAT_TEST[g] = conj_matrix_via_columns(acts[g], ANTISYM_IDX)
for _ in range(8):
    g = random.choice(('a', 'b', 'c'))
    i0, j0 = sorted(random.sample(range(d), 2))
    k = ANTISYM_IDX.index((i0, j0))
    Mb = vec_to_M_antisym([K1 if t == k else K0 for t in range(DIM_A)])
    brute = M_to_vec_antisym(conj_action(acts[g], Mb))
    fastcol = [FASTMAT_TEST[g][m][k] for m in range(DIM_A)]
    _ok = _ok and all((brute[m] - fastcol[m]).is_zero() for m in range(DIM_A))
gates["conj_matrix_via_columns_matches_bruteforce"] = _ok
log(f"  CONTROL conj_matrix_via_columns matches brute-force conj_action (8 spot checks): {_ok}")
assert gates["conj_matrix_via_columns_matches_bruteforce"]

# ============================================================================
log("STEP 2: build F_L351 (1053x1053) Fox-derivative matrix -- structured "
    "assembly, O(dim^2) per relator letter (NEVER a dense dim x dim multiply)...")


def build_slot_foxmat(dim, BASIS_IDX):
    FoxMat = []
    for word in RELS:
        D_ = {g: [[K0] * dim for _ in range(dim)] for g in ('a', 'b', 'c')}
        P27 = meye(d)
        for ch in word:
            low = ch.lower()
            if ch.islower():
                contrib = conj_matrix_via_columns(P27, BASIS_IDX)
                Dlow = D_[low]
                for r in range(dim):
                    Dr, Cr = Dlow[r], contrib[r]
                    for c in range(dim):
                        Dr[c] = Dr[c] + Cr[c]
            else:
                P27new = mmul(P27, acts[ch])
                contrib = conj_matrix_via_columns(P27new, BASIS_IDX)
                Dlow = D_[low]
                for r in range(dim):
                    Dr, Cr = Dlow[r], contrib[r]
                    for c in range(dim):
                        Dr[c] = Dr[c] - Cr[c]
            P27 = mmul(P27, acts[ch])
        for r in range(dim):
            FoxMat.append(D_['a'][r] + D_['b'][r] + D_['c'][r])
    return FoxMat


t0 = time.time()
FOX_L351 = build_slot_foxmat(DIM_A, ANTISYM_IDX)
log(f"  F_L351 built: {len(FOX_L351)}x{len(FOX_L351[0])} ({time.time()-t0:.1f}s)")
gates["fox_L351_square_1053"] = (len(FOX_L351) == 1053 and len(FOX_L351[0]) == 1053)
assert gates["fox_L351_square_1053"]

# ============================================================================
log("STEP 3: base_vec_slot (BASE_ij, the constant defect of the bounding "
    "recursion at y=0) -- generalized to accept explicit z-cochain dicts "
    "(not just class indices) so the shift-invariance control can reuse it "
    "directly with a coboundary-shifted cochain in place of classes[i]...")


def base_vec_slot(zi, zj):
    aconst = {}
    for g in ('a', 'b', 'c'):
        x = zi[g]
        yG = lv(zj, g.upper())
        rgy = apply_(acts[g], yG)
        aconst[g.upper()] = antisym_part(outer(x, rgy))

    base_flat = []
    for word in RELS:
        total = zero27()
        rho_run = meye(d)
        ui_run = [K0] * d
        for ch in word:
            if ch.islower():
                bch = zero27()
            else:
                low = ch.lower()
                diff = aconst[ch]
                bch = conj_action(acts[ch], diff)
            term = conj_action(rho_run, bch)
            uj_ch = lv(zj, ch)
            rgy = apply_(rho_run, uj_ch)
            Mdef = outer(ui_run, rgy)
            defect = antisym_part(Mdef)
            total = msub27(madd27(total, term), defect)
            ui_ch = lv(zi, ch)
            ui_run = vadd(ui_run, apply_(rho_run, ui_ch))
            rho_run = mmul(rho_run, acts[ch])
        base_flat += M_to_vec_antisym(total)
    return base_flat


def slot_cup_raw(zi, zj, gword, hword):
    x = cocycle_val(zi, gword)
    y = cocycle_val(zj, hword)
    rgy = apply_(rho_word(gword), y)
    return antisym_part(outer(x, rgy))


def cocycle_identity_ok_slot(zi, zj):
    oks = []
    for (g, h, kk) in TEST_TRIPLES:
        chk = slot_cup_raw(zi, zj, h, kk)
        cghk = slot_cup_raw(zi, zj, g + h, kk)
        cghk2 = slot_cup_raw(zi, zj, g, h + kk)
        cgh = slot_cup_raw(zi, zj, g, h)
        lhs = msub27(madd27(msub27(conj_action(acts[g], chk), cghk), cghk2), cgh)
        oks.append(all(x.is_zero() for row in lhs for x in row))
    return all(oks)


def raw_cocycle_ok(zi):
    """delta(u_i)(g,h) = rho(g).u_i(h) + u_i(g) - u_i(gh) = 0 on generator
    pairs -- a direct sanity check that classes[i] IS a genuine Z^1(D;27)
    cocycle, independent of the cup construction. Not part of d2_351.py's own
    controls (it restricted its cocycle-identity checks to SOLO x SOLO, never
    touching classes 0,1) -- added here since E1 is the first cell to use the
    boundary classes 0,1 in this specific machinery."""
    for g in ('a', 'b', 'c'):
        for h in ('a', 'b', 'c'):
            lhs = vadd(apply_(acts[g], zi[h]), zi[g])
            rhs = cocycle_val(zi, g + h)
            if not all((lhs[t] - rhs[t]).is_zero() for t in range(d)):
                return False
    return True


for i in ALL_I:
    ok = raw_cocycle_ok(classes[i])
    gates[f"raw_cocycle_u{i}_ok"] = ok
    log(f"  delta(u_{i}) = 0 on generator pairs (raw Z^1 cocycle check): {ok}")
assert all(gates[f"raw_cocycle_u{i}_ok"] for i in ALL_I), "a classes[i] failed the raw cocycle check"

if SMOKE:
    log("E1_SMOKE=1: validating BASE construction + cocycle identities for a "
        "few pairs, then exiting BEFORE the ~60min leftnull/solve steps...")
    _smoke_pairs = [(3, 4), (2, 4), (0, 0), (1, 1), (2, 2)]
    for (i, j) in _smoke_pairs:
        vec = base_vec_slot(classes[i], classes[j])
        ok = cocycle_identity_ok_slot(classes[i], classes[j])
        log(f"  [smoke] pair ({i},{j}): BASE len={len(vec)} (expect 1053), "
            f"nonzero entries={sum(1 for x in vec if not x.is_zero())}, "
            f"cocycle_identity_ok={ok}")
    log("E1_SMOKE=1: smoke test DONE, exiting (exit 0).")
    sys.exit(0)

# ============================================================================
log("STEP 4: ker(F_L351^T) -- exact nullspace over K=Q(sqrt(-3)) via modular "
    "discovery + exact certificate (e1_modnull.py, verbatim d2_modnull.py "
    "logic); THE expensive step (~60-70min per the prior D2 run) -- persisted "
    "to a plain Fraction-string-pair JSON immediately after, so a rerun of "
    "this script (if a later step needs debugging) does not repeat it.")

LEFTNULL_L351 = None
if os.path.exists(LEFTNULL_CACHE_PATH):
    log(f"  loading persisted leftnull basis from {LEFTNULL_CACHE_PATH}...")
    t0 = time.time()
    with open(LEFTNULL_CACHE_PATH) as f:
        raw = json.load(f)
    LEFTNULL_L351 = [[K(Fr(a_n, a_d), Fr(b_n, b_d)) for (a_n, a_d, b_n, b_d) in vec] for vec in raw]
    log(f"  loaded {len(LEFTNULL_L351)} vectors ({time.time()-t0:.1f}s) -- "
        "spot re-verifying 20 random vectors against fresh F_L351^T (full basis "
        "was exactly verified at write time; this is a load-time sanity check, "
        "not a re-derivation)...")
    random.seed(1)
    Ft_L351 = transpose(FOX_L351)
    idxs = random.sample(range(len(LEFTNULL_L351)), min(20, len(LEFTNULL_L351)))
    spot_ok = True
    for vi in idxs:
        v = LEFTNULL_L351[vi]
        for row in Ft_L351:
            s = K0
            for j in range(len(v)):
                if not v[j].is_zero():
                    s = s + row[j] * v[j]
            if not s.is_zero():
                spot_ok = False
                break
        if not spot_ok:
            break
    gates["leftnull_L351_cache_spotcheck"] = spot_ok
    log(f"  spot re-verify (20 vectors): {'PASS' if spot_ok else 'FAIL -- discarding cache, recomputing'}")
    if not spot_ok:
        LEFTNULL_L351 = None
        os.remove(LEFTNULL_CACHE_PATH)

if LEFTNULL_L351 is None:
    from e1_modnull import modular_leftnull
    Ft_L351 = transpose(FOX_L351)
    t1 = time.time()
    LEFTNULL_L351 = modular_leftnull(Ft_L351, K, log, "L351")
    log(f"  ker(F_L351^T) dim = {len(LEFTNULL_L351)}  ({time.time()-t1:.1f}s)")
    pod = [[[v.a.numerator, v.a.denominator, v.b.numerator, v.b.denominator] for v in vec]
           for vec in LEFTNULL_L351]
    with open(LEFTNULL_CACHE_PATH, "w") as f:
        json.dump(pod, f)
    log(f"  persisted leftnull basis ({len(LEFTNULL_L351)} vectors) to {LEFTNULL_CACHE_PATH}")

gates["ker_FT_L351_dim_397"] = (len(LEFTNULL_L351) == 397)
log(f"  ker(F_L351^T) dim = {len(LEFTNULL_L351)} (D2 banked: 397): "
    f"{'MATCH' if gates['ker_FT_L351_dim_397'] else 'MISMATCH'}")
assert gates["ker_FT_L351_dim_397"], "leftnull dimension does not match D2's banked 397 -- STOP"


def obstruction_coords(vec, basis):
    return [vdot(psi, vec) for psi in basis]


def find_witness(vec, basis):
    for psi in basis:
        v = vdot(psi, vec)
        if not v.is_zero():
            return psi, v
    return None, None


def witness_valid(psi, FoxMat):
    dim_total = len(FoxMat)
    for c in range(len(FoxMat[0])):
        col = [FoxMat[r][c] for r in range(dim_total)]
        if not vdot(psi, col).is_zero():
            return False
    return True


# ============================================================================
log("STEP 5: GATE (sealed falsifier) -- recompute ALL SIX of D2's banked "
    "off-diagonal L351 witnesses against the FRESH leftnull basis and cross- "
    "check byte-for-byte vs loop4/d2_351/d2_results.json. STOP if any mismatch.")

d2_banked = json.load(open(D2_JSON))
OFFDIAG = [(i, j) for i in SOLO for j in SOLO if i != j]

BASE_CACHE = {}
gate_results = {}
for (i, j) in OFFDIAG:
    vec = base_vec_slot(classes[i], classes[j])
    BASE_CACHE[(i, j)] = vec
    obs = obstruction_coords(vec, LEFTNULL_L351)
    zero_flag = all(c.is_zero() for c in obs)
    fresh_witness = None
    valid = None
    if not zero_flag:
        psi_w, val = find_witness(vec, LEFTNULL_L351)
        valid = witness_valid(psi_w, FOX_L351)
        fresh_witness = fmt(val)
    banked_entry = d2_banked["slot_results"]["L351"][f"{i}{j}"]
    banked_witness = banked_entry["witness_pairing_value"]
    match = (fresh_witness == banked_witness)
    gate_results[f"{i}{j}"] = {
        "fresh_witness": fresh_witness, "banked_witness": banked_witness,
        "witness_valid": valid, "match": match,
    }
    log(f"  [c_{i}{j}] L351 GATE recheck: fresh={fresh_witness} vs banked={banked_witness}: "
        f"{'MATCH' if match else 'MISMATCH'}  (witness_valid={valid})")

gates["gate_L351_reproduces_d2_all_six_offdiag"] = all(v["match"] for v in gate_results.values())
log(f"  GATE L351-reproduces-D2 (all 6 off-diagonal pairs): "
    f"{'PASS' if gates['gate_L351_reproduces_d2_all_six_offdiag'] else 'FAIL -- STOP'}")
if not gates["gate_L351_reproduces_d2_all_six_offdiag"]:
    log("STOP: L351 off-diagonal reproduction GATE FAILED. Reporting and halting per instructions.")
    with open(os.path.join(HERE, "e1_results.json"), "w") as f:
        json.dump({"verdict": "STOPPED -- L351 offdiag reproduction gate failed",
                   "gates": gates, "gate_recheck": gate_results}, f, indent=2)
    sys.exit(1)

# ============================================================================
log("STEP 6: THE DIAGONAL -- BASE_ii, obstruction coords, witness search, "
    "for i = 0,1,2,3,4 (boundary 0,1 included).")

DIAG_RESULTS = {}
for i in ALL_I:
    vec = base_vec_slot(classes[i], classes[i])
    BASE_CACHE[(i, i)] = vec
    obs = obstruction_coords(vec, LEFTNULL_L351)
    zero_flag = all(c.is_zero() for c in obs)
    nnz = sum(1 for c in obs if not c.is_zero())
    entry = {
        "obstruction_dim": len(LEFTNULL_L351),
        "nonzero_obstruction_coords": nnz,
        "zero_flag": zero_flag,
        "boundary_born": (i in BOUNDARY_BORN),
    }
    if not zero_flag:
        psi_w, val = find_witness(vec, LEFTNULL_L351)
        valid = witness_valid(psi_w, FOX_L351)
        entry["verdict"] = "SELF-SPEAKS"
        entry["witness_pairing_value"] = fmt(val)
        entry["witness_valid_leftnull_of_F"] = valid
        log(f"  [c_{i}{i}]: SELF-SPEAKS  witness={fmt(val)}  valid={valid}  "
            f"(nonzero coords {nnz}/{len(LEFTNULL_L351)})")
    else:
        entry["verdict"] = "PENDING-SILENT-CHECK"
        entry["witness_pairing_value"] = None
        log(f"  [c_{i}{i}]: zero across FULL leftnull basis (nonzero coords "
            f"{nnz}/{len(LEFTNULL_L351)}) -- queued for exact coboundary solve")
    DIAG_RESULTS[i] = entry

# ============================================================================
log("STEP 7: exact coboundary solve for any PENDING-SILENT-CHECK diagonal "
    "(F_L351.y = BASE_ii over K, modular discovery + exact verification) -- "
    "SELF-SILENT if solved & verified.")

silent_candidates = [i for i in ALL_I if DIAG_RESULTS[i]["verdict"] == "PENDING-SILENT-CHECK"]
if silent_candidates:
    from e1_modnull import modular_solve_multi
    b_vecs = [BASE_CACHE[(i, i)] for i in silent_candidates]
    t1 = time.time()
    sol = modular_solve_multi(FOX_L351, b_vecs, K, log, "L351_solve")
    log(f"  coboundary solve for {len(silent_candidates)} pair(s) done ({time.time()-t1:.1f}s)")
    for idx, i in enumerate(silent_candidates):
        consistent, y = sol[idx]
        if consistent:
            DIAG_RESULTS[i]["verdict"] = "SELF-SILENT"
            DIAG_RESULTS[i]["coboundary_solved_and_exact_verified"] = True
            DIAG_RESULTS[i]["coboundary_y_dim"] = len(y)
            DIAG_RESULTS[i]["coboundary_y_nonzero_entries"] = sum(1 for t in y if not t.is_zero())
            log(f"  [c_{i}{i}]: SELF-SILENT (exact coboundary y found & verified, "
                f"{DIAG_RESULTS[i]['coboundary_y_nonzero_entries']}/{len(y)} nonzero entries)")
        else:
            DIAG_RESULTS[i]["verdict"] = "UNDECIDED"
            DIAG_RESULTS[i]["coboundary_solved_and_exact_verified"] = False
            log(f"  [c_{i}{i}]: UNDECIDED (coboundary solve did not close -- "
                "unexpected given the complete-leftnull vanishing; flagged honestly)")
else:
    log("  no PENDING-SILENT-CHECK diagonals -- skipping the solve step entirely.")

# ============================================================================
log("STEP 8: CONTROLS -- slot cocycle identity delta(C_L351_ii)=0 on "
    "TEST_TRIPLES for each i=0..4; coboundary-shift invariance on ONE "
    "diagonal pair (i=2); exactness.")

cocycle_ctrl = {}
for i in ALL_I:
    ok = cocycle_identity_ok_slot(classes[i], classes[i])
    cocycle_ctrl[i] = ok
    log(f"  delta C_L351_{i}{i} = 0 on 5 test triples: {'PASS' if ok else 'FAIL'}")
gates["slot_cocycle_identity_diag_holds_all_i"] = all(cocycle_ctrl.values())
assert gates["slot_cocycle_identity_diag_holds_all_i"], "a diagonal slot cocycle identity FAILED"

log("  CONTROL: coboundary-shift invariance on diagonal pair i=2 -- shift "
    "classes[2] by a primal coboundary in BOTH cup-factors simultaneously "
    "(a strictly stronger test than C1/D2's single-factor off-diagonal "
    "shift, since i=j means the SAME shifted cochain appears twice), "
    "recompute obstruction coords for [c_22], verify UNCHANGED exactly...")
_xi = [K((5 * t + 3) % 11 - 5) for t in range(d)]
_cob = {g: vsub(apply_(acts[g], _xi), _xi) for g in ('a', 'b', 'c')}
_u2_shift = {g: vadd(classes[2][g], _cob[g]) for g in ('a', 'b', 'c')}
base_shift_22 = base_vec_slot(_u2_shift, _u2_shift)
obs_shift = obstruction_coords(base_shift_22, LEFTNULL_L351)
obs_orig = obstruction_coords(BASE_CACHE[(2, 2)], LEFTNULL_L351)
shift_ok = all((obs_shift[k] - obs_orig[k]).is_zero() for k in range(len(LEFTNULL_L351)))
gates["control_coboundary_shift_diag22"] = shift_ok
log(f"  obstruction coords for [c_22] unchanged under simultaneous coboundary "
    f"shift of BOTH cup-factors of classes[2]: {shift_ok}")
assert gates["control_coboundary_shift_diag22"]

gates["control_exactness"] = True
log("  exactness: K = Q(sqrt(-3)) (Fraction pairs) throughout; zero floats "
    "anywhere in the E1 path: PASS by construction")

all_gates_pass = all(v for v in gates.values() if isinstance(v, bool))
log(f"ALL GATES PASS: {all_gates_pass}")

# ============================================================================
log("VERDICT ASSEMBLY")
for i in ALL_I:
    log(f"  [c_{i}{i}] (boundary_born={i in BOUNDARY_BORN}): {DIAG_RESULTS[i]['verdict']}"
        + (f"  witness={DIAG_RESULTS[i].get('witness_pairing_value')}" if DIAG_RESULTS[i]['verdict'] == 'SELF-SPEAKS' else ""))

result = {
    "prereg_note": "PREREG_L5.md E1 clause",
    "gates": gates,
    "all_gates_pass": all_gates_pass,
    "gate_offdiag_recheck_vs_d2": gate_results,
    "leftnull_L351_dim": len(LEFTNULL_L351),
    "fox_L351_size": f"{len(FOX_L351)}x{len(FOX_L351[0])}",
    "boundary_born": BOUNDARY_BORN,
    "solo_inherited": SOLO_INHERITED,
    "diagonal_results": {f"{i}{i}": DIAG_RESULTS[i] for i in ALL_I},
    "runtime_s": time.time() - T0,
}
with open(os.path.join(HERE, "e1_results.json"), "w") as f:
    json.dump(result, f, indent=2)
log(f"saved {os.path.join(HERE, 'e1_results.json')}")
log("DONE.")
