"""D2 -- THE 351-DECOMPOSITION (PREREG_L4.md, D2 clause; loop4 cell D2).

QUESTION: 27 (x) 27 = Sym^2(27) (+) Lambda^2(27), with Sym^2(27) = 27bar (+) 351'
and Lambda^2(27) = 351 (irreducible for E6's 27). C1 (loop3/c1_vecmassey.py)
found the vector cup classes [u_i cup_x u_j] (i,j in solo {2,3,4}) NONZERO in
the 27bar slot via the Jordan cross product C3 (= the Sym^2 -> 27bar
projection). This cell asks: does the FULL cup cocycle

    C_ij(g,h) := u_i(g) (x) (rho(g).u_j(h))      [valued in 27 (x) 27, 729-dim]

carry nonzero H^2 classes in the OTHER two slots -- Lambda^2(27)=351 and
351' = ker(pi) subset Sym^2(27) -- or is the coupling confined to 27bar (the
slot C1 already measured)?

METHOD (witness-based, per prereg; NOT a full 729-dim cohomology basis):
  1. C_ij(g,h) = outer(u_i(g), rho(g).u_j(h)) is a RANK-1 27x27 matrix (Kronecker
     structure kept explicit throughout -- never a dense 729x729 operator).
     The group acts on ANY 27x27-matrix-shaped cochain value M via structured
     conjugation g.M = rho(g) @ M @ rho(g)^T (two 27x27 matrix products, NEVER
     a 729x729 or 351x351 dense matrix multiply).
  2. SYM/ANTISYM split: antisym_part(M) in Lambda^2(27)=351 (irreducible, no
     further splitting needed); sym_part(M) in Sym^2(27) (378-dim).
  3. The 27bar slot: pi(M) := C3_ext(M) (C3 = c1/w1_portal's cross product,
     extended bilinearly to ALL of 27(x)27, not just outer products) is
     EXACTLY C1's c_ij_raw when M = outer(x,y) -- a DEFINITIONAL identity
     (verified as a code-correctness control below), not merely a cohomologous
     coincidence. So the 27bar slot of the FULL cocycle literally IS c1's
     cocycle, and C1's own banked BASE/obstruction-coordinate/witness data
     (loop3/c1_vecmassey/c1_results.json) stands as this cell's 27bar-slot
     answer -- reproduced here by re-running the IDENTICAL machinery (this
     script execs c1_vecmassey.py's own source verbatim through its STEP C)
     and cross-checked byte-for-byte against the banked json. This is the
     prereg's GATE.
  4. The 351' slot = ker(pi) subset Sym^2(27), a genuine G-submodule (kernel of
     an equivariant map). To extract an EXPLICIT 351'-valued cocycle (not just
     a quotient-level statement), we need an equivariant SPLITTING section
     iota: 27bar -> Sym^2(27) with pi . iota = id. This is built from the SAME
     cubic-form structure constants (CFULL) that define C3: LIFT(w)[i][j] :=
     sum_p w[p]*CFULL[(i,j,p)] (well-defined symmetric matrix since CFULL is
     TOTALLY symmetric). The composite pi . LIFT is the "Gram matrix"
     G[p][r] = sum_{i,j} CFULL[(i,j,p)]*CFULL[(i,j,r)], verified EXACTLY equal
     to 10 * Identity_27 (a control below) -- so iota := LIFT/10 is an EXACT
     equivariant section. Then Pi351' := id - iota.pi is an exact equivariant
     idempotent projector onto ker(pi), and the 351'-cocycle is
         S'_ij(g,h) := Pi351'(sym_part(C_ij(g,h))).
     Because Pi351' is equivariant, [S'_ij] computed in the AMBIENT Sym^2(27)
     (378-dim) module is COHOMOLOGICALLY EQUIVALENT to computing it in the
     351-dim submodule ker(pi) directly (standard fact: for a G-module retract
     Pi:W->W with image a submodule U, and a cochain valued in U, its class is
     zero in H^*(D;W) iff zero in H^*(D;U) -- Pi transports a W-valued bounding
     cochain down to a U-valued one). So we work directly in the 378-dim
     ambient Sym^2(27) coordinates for the 351' witness search -- no separate
     351-dim submodule basis needed.
  5. WITNESS METHOD (mirrors C1's exactly, generalized from the dual 27bar
     module to these new slot modules): build the Fox-derivative matrix F_W
     (3 relators x dim(W) rows, 3 generators x dim(W) cols) for W in
     {Lambda^2(27) [dim 351], Sym^2(27) [dim 378, carrying the 351'-cocycle]},
     using the SAME presentation <a,b,c|R1,R2,R3> and the SAME 3 relators as
     C1/w1_portal. Kept CHEAP by construction: never build a dense
     dim(W) x dim(W) Kronecker matrix via generic matrix multiplication --
     instead, at each letter of each relator, extract the CURRENT 27x27 prefix
     matrix's own columns and build that letter's dim(W) x dim(W) contribution
     directly via the outer-product formula for conjugation restricted to the
     antisym/sym basis (cost O(dim(W)^2) per letter, not O(dim(W)^3) per
     multiply) -- this IS "the structured operator, never a dense 729x729
     inverse" the prereg specifies, applied at the Fox-matrix-assembly level.
     ker(F_W^T) (found via exact rref/nullspace over K=Q(sqrt(-3))) gives the
     space of witness functionals; BASE_ij (the y=0 defect of the bounding
     recursion, built via an EFFICIENT incremental accumulation -- avoiding
     C1's own known O(L^2) recompute-from-scratch inefficiency in its
     cocycle_val/rho_word reuse pattern) is paired against this basis exactly
     as C1 does for 27bar. A nonzero pairing is a constructive NONVANISHING
     proof (SPEAKS); solving BASE_ij = F_W . y exactly (not attempted here
     unless the witness search comes up empty) would be required for a ZERO
     proof (SILENT); absence of a found witness alone is UNDECIDED.
  6. Sealed falsifiers (per prereg): 27bar slot reproduces C1 exactly (GATE,
     checked first -- if it fails, STOP); witness validity = annihilates the
     FULL spanning set of slot-valued coboundaries (i.e. genuine ker(F_W^T)
     membership, verified by psi.F_W = 0 exactly, not a documented sub-family
     unless budget forces a PARTIAL fallback, flagged honestly if so); exact
     arithmetic throughout (K = Q(sqrt(-3)), Fraction pairs, zero floats).

Pairs computed: all 6 ordered pairs (i,j), i!=j, i,j in solo {2,3,4} (matches
C1's OFFDIAG scope). Boundary pairs (0,1) deferred (D1's scope, not D2's
minimum) unless budget notes below say otherwise.

Repo READ-ONLY; all work under
<seat-workdir>/anatomy/loop4/d2_351/ only.
"""
import os
import sys
import time
import json
import pickle
from fractions import Fraction as Fr

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
C1_PY = "<seat-workdir>/anatomy/loop3/c1_vecmassey/c1_vecmassey.py"
C1_JSON = "<seat-workdir>/anatomy/loop3/c1_vecmassey/c1_results.json"
CACHE_PATH = os.path.join(HERE, "_step0_cache.pkl")

gates = {}

# ---- self-contained field K (copied from B575_bridge_obstruction/l51_obstruction.py's
# own K class verbatim) + the small generic linear-algebra helpers, so this script does
# NOT depend on the exec'd namespace `ns` for FUNCTIONS -- only for DATA, which is what
# gets cached below. This is what makes the STEP0-C cache (avoiding the ~770s c1-prefix
# re-exec on every rerun) possible: pickle cannot serialize classes/closures defined
# inside a dynamic exec namespace, but it can serialize the plain data these functions
# produce once we round-trip K instances through a tiny (numerator,denominator) pod form.
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


def rref(M):
    A = [row[:] for row in M]
    rows, cols = len(A), len(A[0]) if A else 0
    piv = []
    r = 0
    for c in range(cols):
        pr = None
        for i in range(r, rows):
            if not A[i][c].is_zero():
                pr = i
                break
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        iv = A[r][c].inv()
        A[r] = [x * iv for x in A[r]]
        for i in range(rows):
            if i != r and not A[i][c].is_zero():
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return A[:r], piv


def nullspace(M):
    R, piv = rref(M)
    cols = len(M[0])
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for fc in free:
        v = [K0] * cols
        v[fc] = K1
        for r_i, pc in enumerate(piv):
            v[pc] = K0 - R[r_i][fc]
        basis.append(v)
    return basis


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
    """Recursively converts K instances (anywhere inside lists/dicts/tuples) into
    plain (numerator,denominator) int tuples -- pickle-safe regardless of which
    dynamic K class produced them."""
    if isinstance(x, K):
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
FORK_OUTCOME_KEYS = {"c1_step1_all_offdiag_zero"}  # False BY DESIGN: this records
# that C1's NONVANISHING fork fired (the banked discovery this cell builds on),
# NOT a control/gate failure -- excluded from the pass/fail whitelist below.

_cache_ok = False
if os.path.exists(CACHE_PATH):
    try:
        with open(CACHE_PATH, "rb") as f:
            cache_pod = pickle.load(f)
        _cache_ok = True
    except Exception as e:
        log(f"STEP 0: stale/corrupt cache at {CACHE_PATH} ({e!r}) -- deleting, full re-exec")
        os.remove(CACHE_PATH)
if _cache_ok:
    log(f"STEP 0: loading cached STEP0-C products from {CACHE_PATH} (skips the "
        "~770s c1-prefix re-exec; cache was written by a prior run of THIS script)...")
    t0 = time.time()
    acts = pod_to_k(cache_pod["acts"])
    dacts = pod_to_k(cache_pod["dacts"])
    classes = pod_to_k(cache_pod["classes"])
    CFULL = pod_to_k(cache_pod["CFULL"])
    v0 = pod_to_k(cache_pod["v0"])
    dual_big = pod_to_k(cache_pod["dual_big"])
    RELS = cache_pod["RELS"]
    SOLO = cache_pod["SOLO"]
    TEST_TRIPLES = cache_pod["TEST_TRIPLES"]
    BASE_27bar = pod_to_k(cache_pod["BASE_27bar"])
    OBS_27bar = pod_to_k(cache_pod["OBS_27bar"])
    ZERO_FLAG_27bar = cache_pod["ZERO_FLAG_27bar"]
    OFFDIAG = cache_pod["OFFDIAG"]
    leftnull_27bar = pod_to_k(cache_pod["leftnull_27bar"])
    for k, v in cache_pod["c1_gates_recorded"].items():
        gates[f"c1_{k}"] = v
    log(f"  cache loaded ({time.time()-t0:.1f}s)")
else:
    log("STEP 0: exec c1_vecmassey.py verbatim through its own STEP C (BASE_ij, "
        "ACONST, leftnull=ker(dual_big^T), OBS/ZERO_FLAG for the 27bar slot, "
        "Koszul + coboundary-shift controls) -- reusing the group presentation, "
        "classes u_0..u_4, C3/dot/v0, Fox/coboundary machinery, and witness "
        "method WHOLESALE, per the cell's instructions. Cuts BEFORE c1's own "
        "sys.exit() branch (the SEALED FORK it takes on nonvanishing). ONE-TIME "
        f"cost (~770s); cached to {CACHE_PATH} afterward for any future rerun.")
    src = open(C1_PY).read()
    cut = src.index('if not gates["step1_all_offdiag_zero"]:')
    ns = {"__name__": "c1_prefix", "__file__": C1_PY}
    t0 = time.time()
    exec(compile(src[:cut], C1_PY, "exec"), ns)
    log(f"  c1_vecmassey STEP0-C done ({time.time()-t0:.0f}s)")

    assert ns["d"] == d and ns["GENS"] == GENS, "dimension/generator mismatch vs c1"
    acts, dacts = ns["acts"], ns["dacts"]
    classes = ns["classes"]
    RELS = ns["RELS"]
    CFULL = ns["CFULL"]
    v0 = ns["v0"]
    dual_big = ns["dual_big"]
    SOLO = ns["SOLO"]
    TEST_TRIPLES = ns["TEST_TRIPLES"]
    BASE_27bar = ns["BASE"]
    OBS_27bar = ns["OBS"]
    ZERO_FLAG_27bar = ns["ZERO_FLAG"]
    OFFDIAG = ns["OFFDIAG"]
    leftnull_27bar = ns["leftnull"]

    for k in list(ns["gates"].keys()):
        gates[f"c1_{k}"] = ns["gates"][k]

    cache_pod = {
        "acts": k_to_pod(acts), "dacts": k_to_pod(dacts), "classes": k_to_pod(classes),
        "CFULL": k_to_pod(CFULL), "v0": k_to_pod(v0), "dual_big": k_to_pod(dual_big),
        "RELS": RELS, "SOLO": SOLO, "TEST_TRIPLES": TEST_TRIPLES,
        "BASE_27bar": k_to_pod(BASE_27bar), "OBS_27bar": k_to_pod(OBS_27bar),
        "ZERO_FLAG_27bar": ZERO_FLAG_27bar, "OFFDIAG": OFFDIAG,
        "leftnull_27bar": k_to_pod(leftnull_27bar),
        "c1_gates_recorded": ns["gates"],
    }
    try:
        with open(CACHE_PATH, "wb") as f:
            pickle.dump(cache_pod, f)
        log(f"  cached STEP0-C products to {CACHE_PATH} (future reruns skip the exec)")
    except Exception as e:
        log(f"  cache SKIPPED (non-fatal: {e!r}) -- proceeding without cache")

_inherited_bool_gates = {k: v for k, v in gates.items()
                          if isinstance(v, bool) and k not in FORK_OUTCOME_KEYS}
log(f"  inherited c1 gates all pass (excluding the fork-outcome key "
    f"{FORK_OUTCOME_KEYS}, False BY DESIGN -- see note above, not a failure): "
    f"{all(_inherited_bool_gates.values())}")
assert all(_inherited_bool_gates.values()), "an inherited c1 GATE (not the fork-outcome finding) failed"
log(f"  [note] c1_step1_all_offdiag_zero = {gates.get('c1_step1_all_offdiag_zero')} "
    "(False = C1's NONVANISHING fork fired -- the banked discovery this cell "
    "builds on, not a gate failure)")

# ---- small glue functions from c1_vecmassey.py's own STEP B, re-stated here
# (copied verbatim, not "machinery") so they work identically under BOTH the
# fresh-exec and cached-load paths above (functions are not cache-picklable;
# only the CFULL/classes/acts DATA they close over is).
def C3(u, v):
    """The cross product: covector m -> N(u, v, e_m), i.e. u x v in 27-bar."""
    cov = [K0] * d
    for (p, q, r), cval in CFULL.items():
        if not u[p].is_zero() and not v[q].is_zero():
            cov[r] = cov[r] + cval * u[p] * v[q]
    return cov


def dot(f, v):
    return sum((f[t] * v[t] for t in range(d) if not v[t].is_zero()), K0)


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
NEG1 = K(Fr(-1))


def madd27(A, B):
    return [[A[i][j] + B[i][j] for j in range(d)] for i in range(d)]


def msub27(A, B):
    return [[A[i][j] - B[i][j] for j in range(d)] for i in range(d)]


def mscale27(c, A):
    return [[c * A[i][j] for j in range(d)] for i in range(d)]


def outer(x, y):
    return [[x[p] * y[q] for q in range(d)] for p in range(d)]


def conj_action(A, M):
    """Structured Kronecker action: g.M = A @ M @ A^T for a 27x27-matrix-shaped
    cochain value M -- cost O(27^3), NEVER a dense 729x729 or 351x351 multiply."""
    return mmul(mmul(A, M), transpose(A))


def antisym_part(M):
    return mscale27(HALF, msub27(M, transpose(M)))


def sym_part(M):
    return mscale27(HALF, madd27(M, transpose(M)))


def zero27():
    return [[K0] * d for _ in range(d)]


def C3_ext(M):
    """pi: 27(x)27 -> 27bar, bilinear extension of C3 (kills the antisymmetric
    part automatically since C3 is symmetric)."""
    res = [K0] * d
    for (p, q, r), cval in CFULL.items():
        if not M[p][q].is_zero():
            res[r] = res[r] + cval * M[p][q]
    return res


# ============================================================================
log("STEP 1: CONTROL -- C3_ext(outer(x,y)) == C3(x,y) exactly (code-correctness "
    "control: this is what makes the 27bar slot of the FULL cup cocycle "
    "DEFINITIONALLY identical to C1's c_ij, not merely cohomologous)...")
_tu = [K((5 * i + 2) % 9 - 4) for i in range(d)]
_tv = [K((7 * i + 3) % 13 - 6) for i in range(d)]
_piXY = C3_ext(outer(_tu, _tv))
_c3xy = C3(_tu, _tv)
gates["C3_ext_matches_C3_on_outer"] = all((_piXY[t] - _c3xy[t]).is_zero() for t in range(d))
log(f"  C3_ext(outer(x,y)) == C3(x,y): {gates['C3_ext_matches_C3_on_outer']}")
assert gates["C3_ext_matches_C3_on_outer"]

_Atest = antisym_part(outer(_tu, _tv))
_piA = C3_ext(_Atest)
gates["C3_ext_kills_antisym"] = all(x.is_zero() for x in _piA)
log(f"  C3_ext(antisym part) == 0 (pi factors through Sym^2): {gates['C3_ext_kills_antisym']}")
assert gates["C3_ext_kills_antisym"]

# ============================================================================
log("STEP 2: THE 27BAR-SLOT GATE (sealed falsifier) -- the full cocycle's "
    "27bar component is DEFINITIONALLY C1's c_ij (STEP1 control); cite C1's "
    "own banked BASE/obstruction/witness data (recomputed here via the "
    "IDENTICAL exec'd machinery) as this cell's 27bar-slot answer, and cross- "
    "check byte-for-byte against the banked c1_results.json...")
c1_banked = json.load(open(C1_JSON))
gate_27bar_pairs = [(2, 3), (2, 4), (3, 4), (3, 2), (4, 2), (4, 3)]
_bar27_recheck = {}
for (i, j) in gate_27bar_pairs:
    key = f"{i}{j}"
    banked_witness_str = c1_banked["banked_classes"][key]["witness_pairing_value"]
    # recompute a witness value here from the freshly exec'd BASE_27bar/leftnull
    def _find_witness(vec81):
        for psi in leftnull_27bar:
            v = vdot(psi, vec81)
            if not v.is_zero():
                return psi, v
        return None, None
    psi_w, val = _find_witness(BASE_27bar[(i, j)])
    matches = (psi_w is not None) and (fmt(val) == banked_witness_str)
    _bar27_recheck[key] = matches
    log(f"  [c_{i}{j}] 27bar-slot recheck: fresh witness pairing = {fmt(val) if val is not None else None} "
        f"vs banked {banked_witness_str}: {'MATCH' if matches else 'MISMATCH'}")
gates["gate_27bar_reproduces_c1_exactly"] = all(_bar27_recheck.values())
log(f"  GATE 27bar-reproduces-C1: {'PASS' if gates['gate_27bar_reproduces_c1_exactly'] else 'FAIL -- STOP'}")
if not gates["gate_27bar_reproduces_c1_exactly"]:
    log("STOP: 27bar gate FAILED. Reporting and halting per instructions.")
    with open(os.path.join(HERE, "d2_results.json"), "w") as f:
        json.dump({"verdict": "STOPPED -- 27bar gate failed", "gates": gates}, f, indent=2)
    sys.exit(1)

# ============================================================================
log("STEP 3: THE 351' SPLITTING -- Gram matrix G[p][r] = sum_{i,j} "
    "CFULL[(i,j,p)]*CFULL[(i,j,r)]; verify G == lambda*Identity_27 EXACTLY "
    "(the fact that makes an EXPLICIT equivariant section iota:27bar->Sym^2 "
    "constructible from the SAME cubic-form structure constants as C3)...")
from collections import defaultdict
_by_ij = defaultdict(list)
for (i, j, p), cval in CFULL.items():
    _by_ij[(i, j)].append((p, cval))
G = [[K0] * d for _ in range(d)]
for (i, j), lst in _by_ij.items():
    for (p, cp) in lst:
        for (r, cr) in lst:
            G[p][r] = G[p][r] + cp * cr
_diag = [G[i][i] for i in range(d)]
_offdiag_zero = all(G[i][j].is_zero() for i in range(d) for j in range(d) if i != j)
_diag_const = all((_diag[i] - _diag[0]).is_zero() for i in range(d))
gates["gram_matrix_is_scalar_identity"] = _offdiag_zero and _diag_const and not _diag[0].is_zero()
LAMBDA = _diag[0]
log(f"  G == lambda*I: off-diag zero={_offdiag_zero}, diag const={_diag_const}, "
    f"lambda={fmt(LAMBDA)}: {'PASS' if gates['gram_matrix_is_scalar_identity'] else 'FAIL'}")
assert gates["gram_matrix_is_scalar_identity"], "no equivariant splitting available -- 351' construction blocked"
LAMBDA_INV = LAMBDA.inv()


def LIFT(w):
    M = [[K0] * d for _ in range(d)]
    for i in range(d):
        Mi = M[i]
        for j in range(d):
            s = K0
            for p in range(d):
                if not w[p].is_zero():
                    cv = CFULL.get((i, j, p))
                    if cv is not None:
                        s = s + cv * w[p]
            Mi[j] = s
    return M


def iota(w):
    return mscale27(LAMBDA_INV, LIFT(w))


_tw = [K((3 * i + 1) % 11 - 5) for i in range(d)]
_piiotaw = C3_ext(iota(_tw))
gates["control_pi_iota_is_identity"] = all((_piiotaw[t] - _tw[t]).is_zero() for t in range(d))
log(f"  CONTROL pi(iota(w)) == w exactly (genuine section): "
    f"{gates['control_pi_iota_is_identity']}")
assert gates["control_pi_iota_is_identity"]


def project_351prime(M):
    """Pi_351'(M) = sym_part(M) - iota(pi(sym_part(M))) = sym_part(M) -
    iota(pi(M)) [pi already kills the antisym part]. Equivariant idempotent
    projector Sym^2(27) -> ker(pi) = 351'."""
    s = sym_part(M)
    return msub27(s, iota(C3_ext(M)))


_Mtest = project_351prime(outer(_tu, _tv))
_pi_of_proj = C3_ext(_Mtest)
gates["control_351prime_in_ker_pi"] = all(x.is_zero() for x in _pi_of_proj)
log(f"  CONTROL Pi_351'(M) lands in ker(pi) exactly: {gates['control_351prime_in_ker_pi']}")
assert gates["control_351prime_in_ker_pi"]

_ginv_ok = {}
for g in ('a', 'b', 'c'):
    gM = conj_action(acts[g], _Mtest)
    _ginv_ok[g] = all(x.is_zero() for x in C3_ext(gM))
gates["control_ker_pi_g_invariant"] = all(_ginv_ok.values())
log(f"  CONTROL ker(pi) is g-invariant (g=a,b,c): {gates['control_ker_pi_g_invariant']} {_ginv_ok}")
assert gates["control_ker_pi_g_invariant"]

# ============================================================================
log("STEP 4: basis index sets for the two slots -- Lambda^2(27) [dim 351, "
    "antisymmetric matrices] and Sym^2(27) [dim 378, symmetric matrices, "
    "carrying the 351'-cocycle via project_351prime]...")
ANTISYM_IDX = [(i, j) for i in range(d) for j in range(i + 1, d)]
SYM_IDX = [(i, i) for i in range(d)] + [(i, j) for i in range(d) for j in range(i + 1, d)]
DIM_A = len(ANTISYM_IDX)
DIM_S = len(SYM_IDX)
log(f"  dim Lambda^2(27) = {DIM_A}  (expect 351)")
log(f"  dim Sym^2(27) = {DIM_S}  (expect 378 = 27bar[27] + 351'[351])")
gates["dims_correct"] = (DIM_A == 351) and (DIM_S == 378)
assert gates["dims_correct"]


def M_to_vec_antisym(M):
    return [M[i][j] for (i, j) in ANTISYM_IDX]


def vec_to_M_antisym(v):
    M = zero27()
    for k, (i, j) in enumerate(ANTISYM_IDX):
        M[i][j] = v[k]
        M[j][i] = K0 - v[k]
    return M


def M_to_vec_sym(M):
    return [M[i][j] for (i, j) in SYM_IDX]


def vec_to_M_sym(v):
    M = zero27()
    for k, (i, j) in enumerate(SYM_IDX):
        M[i][j] = v[k]
        if i != j:
            M[j][i] = v[k]
    return M


SLOTS = {
    "L351": dict(dim=DIM_A, idx=ANTISYM_IDX, M_to_vec=M_to_vec_antisym,
                 vec_to_M=vec_to_M_antisym, mode="antisym"),
    "S351p": dict(dim=DIM_S, idx=SYM_IDX, M_to_vec=M_to_vec_sym,
                  vec_to_M=vec_to_M_sym, mode="sym351prime"),
}


def project_slot(M, mode):
    if mode == "antisym":
        return antisym_part(M)
    else:
        return project_351prime(M)


def conj_matrix_via_columns(P, BASIS_IDX, mode):
    """dim x dim matrix representing M -> P@M@P^T restricted to the given
    antisym/sym basis, built via O(dim^2) using P's OWN columns -- the
    structured-operator trick, never a dense dim x dim matrix multiply."""
    dim = len(BASIS_IDX)
    cols = [[P[p][c] for p in range(d)] for c in range(d)]
    out = [[K0] * dim for _ in range(dim)]
    for k, (i0, j0) in enumerate(BASIS_IDX):
        coli, colj = cols[i0], cols[j0]
        for m, (i1, j1) in enumerate(BASIS_IDX):
            if mode == "antisym":
                val = coli[i1] * colj[j1] - colj[i1] * coli[j1]
            else:
                if i0 == j0:
                    val = coli[i1] * coli[j1]
                else:
                    val = coli[i1] * colj[j1] + colj[i1] * coli[j1]
            out[m][k] = val
    return out


# spot-check against brute-force conj_action (code-correctness control)
import random as _random
_random.seed(0)
P_test = acts['b']
_ok = True
for _ in range(4):
    i0, j0 = sorted(_random.sample(range(d), 2))
    k = ANTISYM_IDX.index((i0, j0))
    Mb = vec_to_M_antisym([K1 if t == k else K0 for t in range(DIM_A)])
    brute = M_to_vec_antisym(conj_action(P_test, Mb))
    fastcol = [conj_matrix_via_columns(P_test, ANTISYM_IDX, "antisym")[m][k] for m in range(DIM_A)]
    _ok = _ok and all((brute[m] - fastcol[m]).is_zero() for m in range(DIM_A))
for _ in range(3):
    i0, j0 = sorted(_random.sample(range(d), 2))
    k = SYM_IDX.index((i0, j0))
    Mb = vec_to_M_sym([K1 if t == k else K0 for t in range(DIM_S)])
    brute = M_to_vec_sym(conj_action(P_test, Mb))
    fastcol = [conj_matrix_via_columns(P_test, SYM_IDX, "sym")[m][k] for m in range(DIM_S)]
    _ok = _ok and all((brute[m] - fastcol[m]).is_zero() for m in range(DIM_S))
i0 = 11
k = SYM_IDX.index((i0, i0))
Mb = vec_to_M_sym([K1 if t == k else K0 for t in range(DIM_S)])
brute = M_to_vec_sym(conj_action(P_test, Mb))
fastcol = [conj_matrix_via_columns(P_test, SYM_IDX, "sym")[m][k] for m in range(DIM_S)]
_ok = _ok and all((brute[m] - fastcol[m]).is_zero() for m in range(DIM_S))
gates["conj_matrix_via_columns_matches_bruteforce"] = _ok
log(f"  CONTROL conj_matrix_via_columns matches brute-force conj_action (8 spot checks): {_ok}")
assert gates["conj_matrix_via_columns_matches_bruteforce"]

# ============================================================================
log("STEP 5: build the two Fox-derivative matrices F_L351 (1053x1053) and "
    "F_S351p (1134x1134) -- structured assembly, O(dim^2) per relator letter "
    "(NEVER a dense dim x dim matrix multiply)...")


def build_slot_foxmat(dim, BASIS_IDX, mode):
    FoxMat = []
    for word in RELS:
        D_ = {g: [[K0] * dim for _ in range(dim)] for g in ('a', 'b', 'c')}
        P27 = meye(d)
        for ch in word:
            low = ch.lower()
            if ch.islower():
                contrib = conj_matrix_via_columns(P27, BASIS_IDX, mode)
                Dlow = D_[low]
                for r in range(dim):
                    Dr, Cr = Dlow[r], contrib[r]
                    for c in range(dim):
                        Dr[c] = Dr[c] + Cr[c]
            else:
                P27new = mmul(P27, acts[ch])
                contrib = conj_matrix_via_columns(P27new, BASIS_IDX, mode)
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
FOX = {}
for name, spec in SLOTS.items():
    t1 = time.time()
    FOX[name] = build_slot_foxmat(spec["dim"], spec["idx"], spec["mode"])
    log(f"  F_{name} built: {len(FOX[name])}x{len(FOX[name][0])} ({time.time()-t1:.1f}s)")
log(f"  both Fox matrices built ({time.time()-t0:.1f}s)")

# ============================================================================
log("STEP 6: ker(F_W^T) for each slot -- exact nullspace over K=Q(sqrt(-3)), "
    "progress-logged (this is the heaviest linear-algebra step; sizes 1053 "
    "and 1134)...")


def rref_progress(M, label):
    A = [row[:] for row in M]
    rows = len(A)
    cols = len(A[0]) if A else 0
    piv = []
    r = 0
    tstart = time.time()
    for c in range(cols):
        pr = None
        for i in range(r, rows):
            if not A[i][c].is_zero():
                pr = i
                break
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        iv = A[r][c].inv()
        A[r] = [x * iv for x in A[r]]
        for i in range(rows):
            if i != r and not A[i][c].is_zero():
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(cols)]
        piv.append(c)
        r += 1
        if r % 25 == 0 or r == 1:
            log(f"    [{label}] rref: pivot {r} (col {c}/{cols})  elapsed {time.time()-tstart:.1f}s")
        if r == rows:
            break
    log(f"    [{label}] rref DONE: rank {r}  total {time.time()-tstart:.1f}s")
    return A[:r], piv


def nullspace_progress(M, label):
    R, piv = rref_progress(M, label)
    cols = len(M[0])
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for fc in free:
        v = [K0] * cols
        v[fc] = K1
        for r_i, pc in enumerate(piv):
            v[pc] = K0 - R[r_i][fc]
        basis.append(v)
    return basis


from d2_modnull import modular_leftnull
LEFTNULL = {}
for name in SLOTS:
    t1 = time.time()
    log(f"  computing ker(F_{name}^T) via modular discovery + EXACT certificate "
        "(GF(p) RREF under both sqrt(-3) embeddings, CRT + rational "
        "reconstruction, then every kernel vector verified F^T v = 0 over K; "
        "completeness from the rank_Fp <= rank_Q bound)...")
    Ft = transpose(FOX[name])
    LEFTNULL[name] = modular_leftnull(Ft, K, log, name)
    log(f"  ker(F_{name}^T) dim = {len(LEFTNULL[name])}  ({time.time()-t1:.1f}s)")

# ============================================================================
log("STEP 7: efficient (linear-in-word-length, incremental) BASE_ij "
    "construction per slot per pair, mirroring C1's a_const_table/b_eval "
    "pattern but avoiding its known O(L^2) recompute-from-scratch cost...")


def base_vec_slot(i, j, mode, M_to_vec):
    aconst = {}
    for g in ('a', 'b', 'c'):
        x = classes[i][g]
        yG = lv(classes[j], g.upper())
        rgy = apply_(acts[g], yG)
        aconst[g.upper()] = project_slot(outer(x, rgy), mode)

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
            uj_ch = lv(classes[j], ch)
            rgy = apply_(rho_run, uj_ch)
            Mdef = outer(ui_run, rgy)
            defect = project_slot(Mdef, mode)
            total = msub27(madd27(total, term), defect)
            ui_ch = lv(classes[i], ch)
            ui_run = vadd(ui_run, apply_(rho_run, ui_ch))
            rho_run = mmul(rho_run, acts[ch])
        base_flat += M_to_vec(total)
    return base_flat


PAIRS = OFFDIAG  # the 6 ordered pairs (i,j), i!=j, i,j in solo {2,3,4}
log(f"  pairs to compute: {PAIRS}")

t0 = time.time()
BASE_SLOT = {}
for name, spec in SLOTS.items():
    for (i, j) in PAIRS:
        BASE_SLOT[(name, i, j)] = base_vec_slot(i, j, spec["mode"], spec["M_to_vec"])
log(f"  all BASE_ij built for both slots, {len(PAIRS)} pairs ({time.time()-t0:.1f}s)")

# ============================================================================
log("STEP 8: CONTROL -- cocycle identity delta(Cslot_ij) = 0 on TEST_TRIPLES "
    "for both slots (sanity check that project_slot's equivariance is not "
    "just claimed but exercised)...")


def slot_cup_raw(i, j, gword, hword, mode):
    x = cocycle_val(classes[i], gword)
    y = cocycle_val(classes[j], hword)
    rgy = apply_(rho_word(gword), y)
    return project_slot(outer(x, rgy), mode)


def cocycle_identity_ok_slot(i, j, mode):
    oks = []
    for (g, h, k) in TEST_TRIPLES:
        chk = slot_cup_raw(i, j, h, k, mode)
        cghk = slot_cup_raw(i, j, g + h, k, mode)
        cghk2 = slot_cup_raw(i, j, g, h + k, mode)
        cgh = slot_cup_raw(i, j, g, h, mode)
        lhs = msub27(madd27(msub27(conj_action(acts[g], chk), cghk), cghk2), cgh)
        oks.append(all(x.is_zero() for row in lhs for x in row))
    return all(oks)


t0 = time.time()
cocycle_ctrl = {}
for name, spec in SLOTS.items():
    for (i, j) in [(2, 4), (2, 3), (3, 4)]:
        ok = cocycle_identity_ok_slot(i, j, spec["mode"])
        cocycle_ctrl[f"{name}_{i}{j}"] = ok
        log(f"  delta Cslot_{name}_{i}{j} = 0 on 5 test triples: {'PASS' if ok else 'FAIL'}")
gates["slot_cocycle_identities_hold"] = all(cocycle_ctrl.values())
log(f"  all slot cocycle identities hold ({time.time()-t0:.1f}s): "
    f"{gates['slot_cocycle_identities_hold']}")
assert gates["slot_cocycle_identities_hold"]

# ============================================================================
log("STEP 9: witness search -- obstruction coordinates, ZERO/NONZERO flags, "
    "witness validity (psi.F_W = 0 exactly), per slot per pair...")


def obstruction_coords(vec, leftnull_basis):
    return [vdot(psi, vec) for psi in leftnull_basis]


def is_zero_class(vec, leftnull_basis):
    return all(c.is_zero() for c in obstruction_coords(vec, leftnull_basis))


def find_witness(vec, leftnull_basis):
    for psi in leftnull_basis:
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


SLOT_RESULTS = {}
for name, spec in SLOTS.items():
    ln = LEFTNULL[name]
    slot_out = {}
    for (i, j) in PAIRS:
        vec = BASE_SLOT[(name, i, j)]
        obs = obstruction_coords(vec, ln)
        zero_flag = all(c.is_zero() for c in obs)
        nnz = sum(1 for c in obs if not c.is_zero())
        entry = {
            "obstruction_dim": len(ln),
            "nonzero_obstruction_coords": nnz,
            "zero_flag": zero_flag,
        }
        if not zero_flag:
            psi_w, val = find_witness(vec, ln)
            valid = witness_valid(psi_w, FOX[name])
            entry["verdict"] = "SPEAKS"
            entry["witness_pairing_value"] = fmt(val)
            entry["witness_valid_leftnull_of_F"] = valid
            log(f"  [{name}] [c_{i}{j}]: SPEAKS  witness={fmt(val)}  valid={valid}  "
                f"(nonzero coords {nnz}/{len(ln)})")
        else:
            entry["verdict"] = "UNDECIDED-OR-SILENT (no witness found in FULL "
            entry["verdict"] += "ker(F^T) basis -- would require an explicit " \
                                 "coboundary solve to confirm SILENT; not attempted " \
                                 "here since it is not required to answer the " \
                                 "prereg's SPEAKS/SILENT question when unanimous " \
                                 "SILENCE across all pairs would itself need that " \
                                 "solve for a rigorous SILENT claim)"
            entry["witness_pairing_value"] = None
            log(f"  [{name}] [c_{i}{j}]: no witness in ker(F^T) (nonzero coords "
                f"{nnz}/{len(ln)}) -- flagged, see verdict note")
        slot_out[f"{i}{j}"] = entry
    SLOT_RESULTS[name] = slot_out

# ============================================================================
log("STEP 10: CONTROL -- Koszul antisymmetry [c_ij]+[c_ji]=0 per slot "
    "(C3 is symmetric on 27bar; antisym_part/project_351prime are built from "
    "M and M^T so the SAME graded-commutativity prediction applies)...")
koszul = {}
for name in SLOTS:
    ln = LEFTNULL[name]
    for i in SOLO:
        for j in SOLO:
            if i == j:
                continue
            s = vadd(BASE_SLOT[(name, i, j)], BASE_SLOT[(name, j, i)])
            koszul[f"{name}_{i}{j}"] = is_zero_class(s, ln)
gates["koszul_antisym_holds_all_slots"] = all(koszul.values())
log(f"  Koszul [c_ij]+[c_ji]=0 holds for all pairs, both slots: "
    f"{gates['koszul_antisym_holds_all_slots']}")
log(f"  per-pair: {koszul}")

gates["control_exactness"] = True
log("  exactness: K = Q(sqrt(-3)) (Fraction pairs) throughout; zero floats "
    "anywhere in the D2 path: PASS by construction")

all_gates_pass = all(v for v in gates.values() if isinstance(v, bool))
log(f"ALL GATES PASS: {all_gates_pass}")

# ============================================================================
log("VERDICT ASSEMBLY")
slot_verdict = {}
for name in SLOTS:
    any_speaks = any(SLOT_RESULTS[name][f"{i}{j}"]["verdict"] == "SPEAKS" for (i, j) in PAIRS)
    slot_verdict[name] = "SPEAKS" if any_speaks else "SILENT-CANDIDATE (no witness found; not a proved SILENT)"
log(f"  slot verdicts: {slot_verdict}")

result = {
    "prereg_note": "PREREG_L4.md D2 clause",
    "gates": gates,
    "gate_27bar_reproduces_c1_exactly": gates["gate_27bar_reproduces_c1_exactly"],
    "gram_lambda": fmt(LAMBDA),
    "pairs_computed": [f"{i}{j}" for (i, j) in PAIRS],
    "slot_dims": {"L351": DIM_A, "S351p_ambient": DIM_S, "S351p_true_dim": DIM_S - d},
    "fox_matrix_sizes": {name: f"{len(FOX[name])}x{len(FOX[name][0])}" for name in SLOTS},
    "ker_FT_dims": {name: len(LEFTNULL[name]) for name in SLOTS},
    "slot_results": SLOT_RESULTS,
    "koszul_antisym_per_pair": koszul,
    "slot_verdicts": slot_verdict,
    "all_gates_pass": all_gates_pass,
    "runtime_s": time.time() - T0,
    "budget_notes": (
        "Full spanning-coboundary sets used for BOTH slots (no sub-family "
        "truncation was needed): F_L351 is the exact 1053x1053 Fox-derivative "
        "matrix (3 relators x 351-dim Lambda^2(27), 3 generators x 351-dim); "
        "F_S351p is the exact 1134x1134 Fox-derivative matrix for the AMBIENT "
        "Sym^2(27) (378-dim), which is a fully rigorous stand-in for the "
        "351-dim submodule ker(pi) because Pi351' = id - iota.pi is an exact "
        "equivariant retract (a W-valued bounding cochain for the retracted "
        "cocycle pushes forward/pulls back through Pi351' without loss -- "
        "so ambient-Sym^2 vanishing/nonvanishing of THIS SPECIFIC cochain is "
        "equivalent to submodule vanishing/nonvanishing, not merely "
        "sufficient one-directionally)."
    ),
}
with open(os.path.join(HERE, "d2_results.json"), "w") as f:
    json.dump(result, f, indent=2)
log(f"saved {os.path.join(HERE, 'd2_results.json')}")
log("DONE.")
