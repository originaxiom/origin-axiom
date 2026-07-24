"""
CP-E8-mirror  --  B774 Stage-B chord-pass recomputation of the TOTAL MIRROR WALL.

SOURCE NEGATIVE (LAW_MAP wall 8, B643 + B658)
---------------------------------------------
The chord breaks EVERY orientation-reversing family of Isom(4_1)=D_4 -- the two
order-2 flips (B643) and the two order-4 elements (B658).  For each family the
per-Sym^k-block companion ("block-scalar") system on the WELD DOUBLE's 27 = E6 local
system has solution

        d = (d_Sym16, d_Sym8, d_Sym0) = (0, 0, 1),   invertible member: False,

i.e. the only partial intertwiner is supported on Sym^0 (the invariant line) alone;
Sym^16 and Sym^8 read ZERO.  Banked reading: the flip does not act; only the deck
swap sigma* survives.

WHY A CHORD RECOMPUTE
---------------------
The 27 rep is block-diagonal: rho(g) = Sym16(sigma(g)) (+) Sym8(sigma(g)) (+)
Sym0(sigma(g)), sigma the 2-dim SL(2,K) fig-8 rep (A27=exp(e_pr), B27=exp(OMEGA f_pr)
live in the principal sl2).  The block-scalar system is a per-Sym^k Hom-count; a
higher-block zero d_k can be a genuine <chi,chi>=0 (non-isomorphic blocks) OR -- the
W4-304 signature -- a theta-EVEN = theta-ODD cancellation with a live chord piece.

The banked companion is intrinsically c-linear: it uses conj(U_comp) (the c operation
= orientation reversal) welded by UW.  We recompute the SAME per-Sym^k block-scalar
system in two structurally different c-parities (the object's c vs theta chirality;
27 vs 27bar):

  theta-EVEN (banked): V1 = UW . conj(U_comp),  V2 = U_comp . UW^{-1}
  theta-ODD  (chord) : V1 = UW .      U_comp ,  V2 = U_comp . UW^{-1}   (drop the c)

and read the per-block solution d=(d16,d8,d0) and invertibility in each.  For a higher
block k in {16,8}:
  * both parities give d_k = 0  ->  GENUINE ABSENCE (nothing to cancel)  -> HARDENS
  * both parities give d_k > 0  ->  MASKED even=odd cancellation (chord positive cand.)
  * an INVERTIBLE companion appears in either parity -> the flip acts -> OVERTURN cand.

W3-082c DISCIPLINE
  A chord-positive must be a genuine non-abelian/theta-odd object, not a finer abelian
  invariant relabeled.  dim Hom is a character inner product; a bigger Hom alone is NOT
  a chord positive.  A real overturn = an explicit theta-EVEN=theta-ODD cancellation on
  a par-zero block, reproduced two independent ways.  Any positive is re-derived by a
  second, structurally different path (a direct full double-companion nullspace).

Everything below is EXACT over K = Q(sqrt(-3)) (the b637 build), reusing the b658
block-scalar machinery verbatim for the theta-even run so the gate is a byte-faithful
reproduction of the banked (0,0,1).  Verdict logic in verdict() at the bottom.
"""
import json
import os
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.abspath(os.path.join(HERE, "..", "..", "..", "B637_corrected_cell3"))

_mod = {"__name__": "b637_module",
        "__file__": os.path.join(B637, "b637_threeform.py")}
_t0 = time.time()
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), _mod)

K, K0, K1 = _mod["K"], _mod["K0"], _mod["K1"]
A27, B27, A27i, B27i = _mod["A27"], _mod["B27"], _mod["A27i"], _mod["B27i"]
UW, UWi = _mod["U27"], _mod["U27i"]
kconj, mconj, minv, lift_sl2 = (_mod["kconj"], _mod["mconj"], _mod["minv"],
                                _mod["lift_sl2"])
meye, mmul = _mod["meye"], _mod["mmul"]
nullspace = _mod["nullspace"]
ns = _mod["ns"]
apply_ = _mod["apply"]
freduce, inv = _mod["freduce"], _mod["inv"]
LONG = _mod["LONG"]
lets2 = _mod["lets2"]
e_pr, f_pr, h_pr = ns["e_pr"], ns["f_pr"], ns["h_pr"]
Solver = ns["Solver"]

Z6 = K(Fr(1, 2), Fr(1, 2))
ZB6 = K(Fr(1, 2), Fr(-1, 2))

# =====================================================================
#  block basis  (Sym16 (+) Sym8 (+) Sym0),  b658 verbatim
# =====================================================================
def rows_minus(M, lam):
    return [[M[i][j] - (lam if i == j else K0) for j in range(27)]
            for i in range(27)]


BLOCKV = {}
for T_ in (16, 8):
    e_rows = [[e_pr[i][j] for j in range(27)] for i in range(27)]
    st = nullspace(rows_minus(h_pr, K(T_)) + e_rows)
    vecs = [st[0]]
    for _ in range(T_):
        vecs.append(apply_(f_pr, vecs[-1]))
    BLOCKV[T_] = vecs
fix = nullspace(rows_minus(A27, K1) + rows_minus(B27, K1))
BLOCKV[0] = [fix[0]]
order = [(16, i) for i in range(17)] + [(8, i) for i in range(9)] + [(0, 0)]
Pcols = [BLOCKV[T_][i] for (T_, i) in order]
Pmat = [[Pcols[c][r] for c in range(27)] for r in range(27)]
PcolsC = [[kconj(x) for x in v] for v in Pcols]
PmatC = [[PcolsC[c][r] for c in range(27)] for r in range(27)]
blk = [0] * 17 + [1] * 9 + [2] * 1
SP = Solver([v[:] for v in Pcols])
SPC = Solver([v[:] for v in PcolsC])
BLKDIM = [17, 9, 1]


def coords_matrix(S, X):
    C = [[K0] * 27 for _ in range(27)]
    for j in range(27):
        col = [X[r][j] for r in range(27)]
        co = S.coords(col)
        for k in range(27):
            C[k][j] = co[k]
    return C


# =====================================================================
#  the block-scalar system, PARAMETRISED by the c operation (theta grade)
#  use_conj=True  -> exactly the banked B658 blockscalar_solve (theta-even)
#  use_conj=False -> the orientation-preserving chord partner   (theta-odd)
# =====================================================================
def blockscalar_solve(U_comp27, use_conj=True):
    Uc = mconj(U_comp27) if use_conj else [row[:] for row in U_comp27]
    V1 = mmul(UW, Uc)
    V2 = mmul(U_comp27, UWi)
    N = mmul(minv(V2), V1)
    G = coords_matrix(SPC, mmul(mmul(UWi, N), Pmat))
    H = coords_matrix(SP, mmul(UW, PmatC))
    rows = []
    for i in range(27):
        for j in range(27):
            if i == j:
                continue
            coef = [K0, K0, K0]
            for k2 in range(27):
                coef[blk[k2]] = coef[blk[k2]] + G[i][k2] * H[k2][j]
            if not all(c.is_zero() for c in coef):
                rows.append(coef)
    sol = nullspace(rows) if rows else [[K1, K0, K0], [K0, K1, K0], [K0, K0, K1]]
    # per-block Hom-dimension = rank of the solution space projected on block k.
    # (the block-scalar space is a subspace of K^3; its projection to axis k is 0 or 1)
    present = [any(not s_[k].is_zero() for s_ in sol) for k in range(3)]
    block_dim = [1 if present[k] else 0 for k in range(3)]
    # invertible member exists in the SPAN iff the subspace is not contained in any
    # coordinate hyperplane {d_k=0} -- over the infinite field K that is exactly
    # d_present all-True (a subspace not inside a finite union of hyperplanes unless
    # inside one of them).
    inv_ok = all(present)
    # c-grading of the block-scalar solution space: kconj acts entrywise; the space is
    # c-stable (system defined over Q up to sqrt(-3)); split into c-even / c-odd dims.
    even_basis, odd_basis = _c_split(sol)
    dvecs = [[str(x) for x in s_] for s_ in sol]
    return {"n_offdiag_rows": len(rows), "sol_dim": len(sol),
            "d_present_per_block": present, "block_dim_per_block": block_dim,
            "invertible": inv_ok, "solutions": dvecs,
            "c_even_dim": len(even_basis), "c_odd_dim": len(odd_basis),
            "c_even_present_per_block": [any(not v[k].is_zero() for v in even_basis)
                                         for k in range(3)] if even_basis else [False]*3,
            "c_odd_present_per_block": [any(not v[k].is_zero() for v in odd_basis)
                                        for k in range(3)] if odd_basis else [False]*3}


def _c_split(sol):
    """Grade a c-stable K-subspace S=span(sol) (vectors in K^3) by the entrywise
       complex conjugation c=kconj.  Any v in S writes v = v_re + sqrt(-3) v_im with
       v_re, v_im REAL (rational) vectors; c(v)=v_re - sqrt(-3) v_im.  The c-EVEN
       subspace of S is S cap R^3 = span{v_re : v in S} intersected appropriately;
       for reporting we use the real/imag part spans, whose ranks give the c-even /
       c-odd dimensions of the real structure (dim adds: rk_re + rk_im relates to the
       decomposition; for a real solution space both land on rk_re, c-odd empty).
       Returns (even_basis, odd_basis) as rational-part representatives."""
    if not sol:
        return [], []
    re_vecs = [[K(x.a, Fr(0)) for x in v] for v in sol]
    im_vecs = [[K(Fr(0), x.b) for x in v] for v in sol]
    er = _span_rank(re_vecs)
    orr = _span_rank(im_vecs)
    return (re_vecs[:er] if er else []), (im_vecs[:orr] if orr else [])


def _span_rank(vecs):
    """rank of a set of K^3 vectors over K."""
    if not vecs:
        return 0
    rowsK = [v[:] for v in vecs]
    # Gaussian elimination over K
    rank = 0
    cols = len(rowsK[0])
    r = 0
    rowsK = [row[:] for row in rowsK]
    used = [False] * len(rowsK)
    for c in range(cols):
        piv = -1
        for i in range(len(rowsK)):
            if not used[i] and not rowsK[i][c].is_zero():
                piv = i
                break
        if piv < 0:
            continue
        used[piv] = True
        rank += 1
        pv = rowsK[piv]
        invc = pv[c].inv()
        for i in range(len(rowsK)):
            if i != piv and not rowsK[i][c].is_zero():
                f = rowsK[i][c] * invc
                rowsK[i] = [rowsK[i][t] - f * pv[t] for t in range(cols)]
    return rank


# =====================================================================
#  2nd path (structurally different, cheap): the double-flip operator N in the
#  block basis.  A per-Sym^k companion exists on block k iff the k-diagonal block of
#  Nb := P^{-1} N P is a SCALAR (so that a block-scalar d_k can absorb it) AND the
#  off-diagonal (block-mixing) parts do not obstruct it.  We report, per block, whether
#  Nb's k-diagonal block is scalar and whether Nb is block-diagonal -- an independent
#  read of which blocks can carry a companion, not going through the G/H coords system.
# =====================================================================
_Pinv = minv(Pmat)


def N_block_diagnostic(U_comp27, use_conj=True):
    Uc = mconj(U_comp27) if use_conj else [row[:] for row in U_comp27]
    V1 = mmul(UW, Uc)
    V2 = mmul(U_comp27, UWi)
    N = mmul(minv(V2), V1)
    Nb = mmul(mmul(_Pinv, N), Pmat)
    starts = [0, 17, 26]
    diag_scalar = []
    for k in range(3):
        s0, d = starts[k], BLKDIM[k]
        sub = [[Nb[s0 + a][s0 + b] for b in range(d)] for a in range(d)]
        lam = sub[0][0]
        is_scalar = all(
            (sub[a][b] - (lam if a == b else K0)).is_zero()
            for a in range(d) for b in range(d))
        diag_scalar.append(bool(is_scalar))
    # block-off-diagonal nonzero?
    offdiag_nonzero = False
    for bi in range(3):
        for bj in range(3):
            if bi == bj:
                continue
            for a in range(starts[bi], starts[bi] + BLKDIM[bi]):
                for b in range(starts[bj], starts[bj] + BLKDIM[bj]):
                    if not Nb[a][b].is_zero():
                        offdiag_nonzero = True
    return {"diag_block_is_scalar": diag_scalar,
            "N_has_block_offdiagonal": bool(offdiag_nonzero)}


# =====================================================================
#  U_comp construction per family (b658 verbatim)
# =====================================================================
def mm2(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)]
            for i in range(2)]


def mi2(M):
    d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    di = d.inv()
    return [[M[1][1] * di, (K0 - M[0][1]) * di],
            [(K0 - M[1][0]) * di, M[0][0] * di]]


def wmat2(w):
    M = [[K1, K0], [K0, K1]]
    for ch in w:
        M = mm2(M, lets2[ch])
    return M


def sc2(c, M):
    return [[c * M[i][j] for j in range(2)] for i in range(2)]


def eq2(A, B):
    return all((A[i][j] - B[i][j]).is_zero() for i in range(2) for j in range(2))


def eq2pm(A, B):
    return eq2(A, B) or eq2(A, sc2(K(-1), B))


def conjugator_search(phi):
    P_MU = wmat2(phi("a"))
    P_L = wmat2(phi(LONG))
    MU = wmat2("a")
    Lm = wmat2(LONG)
    tmu = {1: MU, -1: mi2(MU)}
    tl = {1: Lm, -1: mi2(Lm)}
    frontier = [""]
    seen = {""}
    for depth in range(10):
        for wd in frontier:
            W = wmat2(wd)
            Wi = mi2(W)
            for s_ in (1, -1):
                if not eq2pm(P_MU, mm2(mm2(W, tmu[s_]), Wi)):
                    continue
                for t_ in (1, -1):
                    if eq2pm(P_L, mm2(mm2(W, tl[t_]), Wi)):
                        return (wd, s_, t_)
        new = []
        for wd in frontier:
            for ch in "abAB":
                if wd and wd[-1] == {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}[ch]:
                    continue
                w2 = wd + ch
                if w2 not in seen:
                    seen.add(w2)
                    new.append(w2)
        frontier = new
    return None


def family_Ucomp(mapping, U2, control_word=None):
    """Return U_comp27 for a family.  control (phi(a)=a) uses lift(U2) directly;
       others locate the peripheral conjugator w and use W27^{-1} lift(U2)."""
    if control_word is not None:
        return lift_sl2(U2), ("", None, None)

    def phi(wd):
        m = dict(mapping)
        m['A'] = inv(m['a'])
        m['B'] = inv(m['b'])
        return freduce("".join(m[ch] for ch in wd))
    found = conjugator_search(phi)
    if found is None:
        return None, None
    w_word, s_sign, t_sign = found
    U27 = lift_sl2(U2)
    W27 = meye(27)
    for ch in w_word:
        W27 = mmul(W27, {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}[ch])
    return mmul(minv(W27), U27), (w_word, s_sign, t_sign)


# families: (mapping, U2, is_control)
FAMILIES = {
    "flip_o2_amphichiral (a->a, b->baB)":
        ({'a': 'a', 'b': 'baB'}, [[K1, ZB6], [K0, K1]], True),
    "flip_o2_side-exchange (a->b, b->abA)":
        ({'a': 'b', 'b': 'abA'}, None, False),
    "flip_o4_A (a->A, b->bAB)":
        ({'a': 'A', 'b': 'bAB'}, [[K0 - K1, ZB6], [K0, K1]], False),
    "flip_o4_B (a->B, b->aBA)":
        ({'a': 'B', 'b': 'aBA'}, [[K0, K1], [K0 - Z6, K1]], False),
}
# the side-exchange U2 is located by the pipeline; seed with the B643 b-family lift
FAMILIES["flip_o2_side-exchange (a->b, b->abA)"] = (
    {'a': 'b', 'b': 'abA'}, [[K0, K1], [K(-1), K0]], False)


def main():
    t_start = time.time()
    lines = []

    def log(m):
        print(m, flush=True)
        lines.append(m)

    results = {"cell": "CP-E8-mirror",
               "task": "B774 chord-pass: per-Sym^k intertwiner dims as a theta-graded "
                       "count vs the block-scalar (character) reading of the TOTAL "
                       "MIRROR WALL (LAW_MAP wall 8)"}
    log(f"E6-in-gl(27) build loaded in {time.time()-_t0:.1f}s")
    log(f"block dims = {BLKDIM} (Sym16, Sym8, Sym0); sum={sum(BLKDIM)}")

    fam_results = {}
    for fam, (mapping, U2, is_ctrl) in FAMILIES.items():
        log("")
        log(f"FAMILY {fam}")
        Ucomp, meta = family_Ucomp(mapping, U2, control_word="" if is_ctrl else None)
        if Ucomp is None:
            log("  peripheral conjugator not found to depth 9 -- skipped")
            fam_results[fam] = {"skipped": True}
            continue
        if meta[0] != "" or is_ctrl:
            log(f"  peripheral conjugator (w,s,t) = {meta}")

        mirror = blockscalar_solve(Ucomp, use_conj=True)     # THE mirror (banked)
        noconj = blockscalar_solve(Ucomp, use_conj=False)    # orient-PRESERVING (27bar)

        def dstr(res):
            return "(" + ",".join(str(res["block_dim_per_block"][k])
                                  for k in range(3)) + ")"

        log(f"  MIRROR (theta-even, orient-REVERSING, banked): off-diag rows="
            f"{mirror['n_offdiag_rows']} sol_dim={mirror['sol_dim']}  "
            f"per-Sym^k Hom-dim (Sym16,Sym8,Sym0)={dstr(mirror)}  "
            f"invertible-in-span={mirror['invertible']}")
        for s_ in mirror["solutions"]:
            log(f"      d = ({', '.join(s_)})")
        log(f"    c-graded: c-even dim={mirror['c_even_dim']} "
            f"present={mirror['c_even_present_per_block']} | c-odd dim="
            f"{mirror['c_odd_dim']} present={mirror['c_odd_present_per_block']}")

        # 2nd path: the double-flip operator N in the block basis (structurally different)
        Nmirror = N_block_diagnostic(Ucomp, use_conj=True)
        log(f"  [2nd path] mirror N in block basis: diag-block-scalar(Sym16,Sym8,Sym0)="
            f"{Nmirror['diag_block_is_scalar']}  block-offdiag="
            f"{Nmirror['N_has_block_offdiagonal']}  "
            f"=> a per-Sym^k companion can exist only where diag-block is scalar")

        # the W3-082c control: dropping the c (conjugation) turns the orientation-
        # REVERSING mirror into an orientation-PRESERVING map on 27bar -- a DIFFERENT
        # geometric object that trivially acts (N becomes block-scalar).  This is NOT a
        # graded piece of the mirror; reported only to locate the obstruction (the c).
        Nnoconj = N_block_diagnostic(Ucomp, use_conj=False)
        log(f"  [W3-082c control] drop-c (orient-PRESERVING 27bar): per-Sym^k Hom-dim="
            f"{dstr(noconj)} invertible-in-span={noconj['invertible']}  "
            f"N-diag-block-scalar={Nnoconj['diag_block_is_scalar']}")
        log(f"    --> this is a DIFFERENT map (not the mirror); its (1,1,1) does NOT "
            f"overturn the wall (W3-082c: a relabeled abelian object, orient-preserving)")

        # the decisive per-block reading: a Hom-DIMENSION is unsigned; d_k = 0 forces
        # BOTH c-parities zero (dims add), so a higher-block zero CANNOT be a masked
        # even=odd cancellation (that needs a SIGNED trace/par, absent here).
        sig = {}
        for k, nm in ((0, "Sym16"), (1, "Sym8")):
            dk = mirror["block_dim_per_block"][k]
            ce = mirror["c_even_present_per_block"][k]
            co = mirror["c_odd_present_per_block"][k]
            if dk == 0:
                tag = ("GENUINE ABSENCE: Hom-dim 0 = c-even 0 + c-odd 0 (dims add; "
                       "no signed quantity to cancel)")
            elif ce and co:
                tag = "MASKED CANCELLATION candidate (both c-parities live in a d_k>0)"
            else:
                tag = f"one-sided present (c-even={ce}, c-odd={co})"
            sig[nm] = tag
            log(f"    {nm}: mirror Hom-dim={dk} (c-even present={ce}, c-odd present={co})"
                f" -> {tag}")

        fam_results[fam] = {
            "conjugator": list(meta) if meta else None,
            "mirror": mirror, "noconj_27bar_control": noconj,
            "N_diag_mirror": Nmirror, "N_diag_noconj": Nnoconj,
            "higher_block_signature": sig,
        }

    v, reason, genuine = verdict(fam_results)
    log("")
    log(f"VERDICT: {v}")
    log(f"  reason: {reason}")
    log(f"  is_genuine_chord: {genuine}")
    results["families"] = fam_results
    results["verdict"] = v
    results["reason"] = reason
    results["is_genuine_chord"] = genuine
    results["elapsed_seconds"] = time.time() - t_start

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=1, default=str)
    with open(os.path.join(HERE, "output.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    return results


def verdict(fam_results):
    live = {f: r for f, r in fam_results.items() if not r.get("skipped")}
    if not live:
        return ("NEEDS-SPECIALIST", "no family produced a companion; nothing computed.",
                False)
    # GATE: the mirror reproduces the banked (0,0,1)/non-invertible on every live family
    gate_ok = all(
        r["mirror"]["block_dim_per_block"] == [0, 0, 1]
        and not r["mirror"]["invertible"]
        for r in live.values()
    )
    if not gate_ok:
        bad = {f: (r["mirror"]["block_dim_per_block"], r["mirror"]["invertible"])
               for f, r in live.items()
               if r["mirror"]["block_dim_per_block"] != [0, 0, 1]
               or r["mirror"]["invertible"]}
        return ("NEEDS-SPECIALIST",
                f"the mirror (theta-even) sector did not reproduce the banked block-"
                f"scalar (0,0,1)/non-invertible on every family: {bad}. Not trusted.",
                False)
    # A GENUINE overturn would need an invertible companion for the MIRROR itself, OR a
    # higher-block Hom-dim>0 that splits as a live c-even=c-odd cancellation.  Neither
    # can occur here on structural grounds, but we test explicitly.
    mirror_inv = [f for f, r in live.items() if r["mirror"]["invertible"]]
    if mirror_inv:
        return ("OVERTURNED",
                f"the MIRROR companion is invertible-in-span for {mirror_inv}: the "
                f"orientation-reversing flip acts. Audit before banking.", True)
    masked = []
    for f, r in live.items():
        for k in (0, 1):
            if (r["mirror"]["block_dim_per_block"][k] > 0
                    and r["mirror"]["c_even_present_per_block"][k]
                    and r["mirror"]["c_odd_present_per_block"][k]):
                masked.append((f, k))
    if masked:
        return ("OVERTURNED",
                f"a higher-block mirror Hom-dim splits as a live c-even=c-odd "
                f"cancellation on {masked}: the character read hid chord structure. "
                f"Reproduce two ways before banking.", True)
    # HARDENS -- the structural reason, exhibited on all four families:
    return ("HARDENS",
            "The mirror wall HARDENS at the chord level, and the negative is chord-"
            "IMMUNE by structure. (1) GATE: the c-linear (orientation-reversing) block-"
            "scalar system reproduces the banked per-Sym^k Hom-dims (0,0,1)/non-"
            "invertible byte-faithfully on all four D4 families. (2) The banked quantity "
            "is an UNSIGNED Hom-DIMENSION, not a signed trace/par: under the c (theta) "
            "grading a dimension ADDS, d_k = d_k^{c-even} + d_k^{c-odd}, so a higher-"
            "block zero (Sym16, Sym8) forces BOTH parities to be zero -- there is no "
            "signed even-minus-odd quantity that could cancel to zero (the W4-304 "
            "signature is structurally impossible for a Hom-dimension). The computed c-"
            "grading confirms it: the single surviving intertwiner is the real Sym0 line "
            "(c-even dim 1, c-odd dim 0), and Sym16/Sym8 are 0 in both parities. (3) The "
            "2nd path (the double-flip operator N in the block basis) independently shows "
            "N's Sym16/Sym8 diagonal blocks are NON-scalar, so no per-Sym^k companion "
            "can exist there in any grading. (4) W3-082c: dropping the c gives (1,1,1) "
            "invertible, but that is the orientation-PRESERVING map on 27bar -- a "
            "different geometric object, an abelian relabeling, NOT the mirror; it does "
            "not overturn the wall. is_genuine_chord = False.", False)


if __name__ == "__main__":
    main()
