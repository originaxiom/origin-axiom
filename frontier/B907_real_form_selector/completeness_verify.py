#!/usr/bin/env python3
"""B907-completeness -- INDEPENDENT verification (fresh code path).

Verifies the load-bearing facts of completeness.py / DRAFT_COMPLETENESS.md
through a DIFFERENT exact route:

  - sympy DomainMatrix over QQ (completeness.py used numpy object-int
    matrices with manual denominator bookkeeping);
  - the two sign-locking kill certificates recomputed exactly over QQ and
    AGAIN modulo three FRESH primes (101, 2003, 9973 -- disjoint from
    stage 7's 1000003/999983/65537), rational entries mapped by modular
    inverse (no scaled-integer sharing with the original path);
  - the full low-degree moment census (total degree <= 4) redone over QQ:
    every odd-parity moment must vanish, the Gram must be diagonal with the
    recorded exact values;
  - the 128-representative rescan redone; the 8 C-compatible ones re-verified
    as automorphisms on ALL 78^2 basis bracket pairs USING THE FRAME'S OWN
    br() on full vectors (not the replicated coefficient bookkeeping of
    is_automorphism_full), as involutions, with patterns, fixed dims
    (DomainMatrix rank), and the omega-composite fixed dims (form naming);
  - structure ranks: rank A8 = rank A16 = 48 = rank of the stacked pair
    (=> ker ad x8 = ker ad x16 exactly, dim 30), four-stack rank 66
    (=> dim z(C) = 12);
  - the wall pair: fix(phi|a) via stacked-kernel ranks, the bookkeeping
    fix(phi) = 24 + fix(phi|a), and phi1*phi2 == the inner all-minus
    character as full matrices;
  - the pattern-level logic replayed: the two certificates kill exactly the
    12 non-(a,b,a,b) patterns; the 4 survivors are exactly the realized ones.

Every check is an assertion; the script writes completeness_verify_results.json
and exits 0 only if ALL pass.  Run from a scratch cwd.
"""
import io, os, sys, json, time, contextlib, itertools
from fractions import Fraction
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy import QQ

ARC = "/Users/dri/origin-axiom/frontier/B907_real_form_selector"
FRAME = "/Users/dri/origin-axiom/frontier/B854_centralizer_exact/e6_centralizer.py"
OUT = os.path.join(ARC, "completeness_verify_results.json")
R = {}
t0 = time.time()
def log(*a):
    print(f"[{time.time()-t0:6.1f}s]", *a, flush=True)

assert os.path.basename(os.getcwd()) != "B907_real_form_selector", \
    "run from a scratch cwd"
# redirect the frame's HERE (= dirname(__file__)) into the scratch cwd so the
# frame's results.json cannot touch any arc directory
__file__ = os.path.join(os.getcwd(), "frame_marker.py")
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(FRAME).read(), "b854", "exec"), globals())
assert ns == [8, 14, 16, 22] and DIM == 78
log("frame rebuilt; frame results.json redirected to", os.getcwd())

# ---------------- exact matrices over QQ (DomainMatrix path) ----------------
DM = {}
for n in ns:
    DM[n] = DomainMatrix.from_Matrix(ADS[n]).convert_to(QQ)
log("DomainMatrix conversions done")

ZDM = DomainMatrix.zeros((78, 78), QQ)
for a_, b_ in itertools.combinations(ns, 2):
    assert DM[a_] * DM[b_] == DM[b_] * DM[a_], f"x{a_},x{b_} do not commute"
log("VERIFIED: all 6 charge pairs commute (QQ)")
R["commutation"] = True

def dm_trace(M):
    L = M.to_list()
    s = QQ.zero
    for i in range(78):
        s += L[i][i]
    q = sp.Rational(str(s))
    return Fraction(q.p, q.q)

# ---------------- the two kill certificates, exact over QQ ------------------
P22 = [DomainMatrix.eye(78, QQ).to_dense(), DM[22]]
for k in range(2, 6):
    P22.append(P22[-1] * DM[22])
m1 = dm_trace(DM[14] * P22[5])                      # tr(A14 A22^5)
m2 = dm_trace(DM[8] * DM[16] * P22[4])              # tr(A8 A16 A22^4)
M1_CLAIM = Fraction(-13172147840218514352082453085409194803200000000000, 19**5)
M2_CLAIM = Fraction(4957259939867182820676192021390557184000000000, 13 * 19**4)
assert m1 == M1_CLAIM, f"certificate 1 mismatch: {m1}"
assert m2 == M2_CLAIM, f"certificate 2 mismatch: {m2}"
assert m1 != 0 and m2 != 0
log("VERIFIED: tr(A14 A22^5)   =", m1, "(exact, nonzero)")
log("VERIFIED: tr(A8 A16 A22^4)=", m2, "(exact, nonzero)")
R["certificates_exact"] = {
    "tr_A14_A22^5": str(m1), "tr_A8_A16_A22^4": str(m2),
    "match_claimed": True}

# ---------------- fresh-prime modular re-verification -----------------------
FRESH = [101, 2003, 9973]
def modmat(n, p):
    M = []
    for i in range(78):
        row = []
        for j in range(78):
            q = sp.Rational(ADS[n][i, j])
            row.append((q.p % p) * pow(q.q % p, p - 2, p) % p)
        M.append(row)
    return M

def modmul(A, B, p):
    n_ = 78
    Bt = list(zip(*B))
    return [[sum(A[i][k] * Bt[j][k] for k in range(n_)) % p
             for j in range(n_)] for i in range(n_)]

def modtrace_word(word, p):
    M = None
    for n in word:
        A = modmat(n, p)
        M = A if M is None else modmul(M, A, p)
    return sum(M[i][i] for i in range(78)) % p

modres = {}
for p in FRESH:
    r1 = modtrace_word([14] + [22] * 5, p)
    r2 = modtrace_word([8, 16] + [22] * 4, p)
    e1 = (m1.numerator % p) * pow(m1.denominator % p, p - 2, p) % p
    e2 = (m2.numerator % p) * pow(m2.denominator % p, p - 2, p) % p
    assert r1 == e1 and r2 == e2, f"mod-{p} mismatch"
    modres[str(p)] = {"cert1": r1, "cert2": r2, "agree_with_exact": True}
    log(f"VERIFIED mod {p}: cert1 residue {r1}, cert2 residue {r2} (both match)")
R["certificates_fresh_primes"] = modres

# ---------------- the full low-degree census over QQ ------------------------
POW = {}
for n in ns:
    POW[n] = [DomainMatrix.eye(78, QQ).to_dense(), DM[n]]
    for k in (2, 3):
        POW[n].append(POW[n][-1] * DM[n])
gram = {}
odd_nonzero, n_moments = [], 0
for a_ in range(4):
    for b_ in range(4):
        if a_ + b_ > 4:
            continue
        L = POW[8][a_] * POW[14][b_]
        for c_ in range(4):
            for d_ in range(4):
                tot = a_ + b_ + c_ + d_
                if c_ + d_ > 4 or tot == 0 or tot > 4:
                    continue
                n_moments += 1
                mv = dm_trace(L * POW[16][c_] * POW[22][d_])
                par = (a_ % 2, b_ % 2, c_ % 2, d_ % 2)
                if par != (0, 0, 0, 0) and mv != 0:
                    odd_nonzero.append(((a_, b_, c_, d_), str(mv)))
                if tot == 2 and max(a_, b_, c_, d_) <= 2:
                    gram[(a_, b_, c_, d_)] = mv
assert not odd_nonzero, f"odd-parity low-degree moment nonzero: {odd_nonzero}"
GRAM_CLAIM = {(2, 0, 0, 0): Fraction(241532928),
              (0, 2, 0, 0): Fraction(-317708697600),
              (0, 0, 2, 0): Fraction(988843239014400, 13),
              (0, 0, 0, 2): Fraction(-889958915112960000, 19),
              (1, 0, 1, 0): Fraction(0), (0, 1, 0, 1): Fraction(0),
              (1, 1, 0, 0): Fraction(0), (1, 0, 0, 1): Fraction(0),
              (0, 1, 1, 0): Fraction(0), (0, 0, 1, 1): Fraction(0)}
for k, v in GRAM_CLAIM.items():
    assert gram[k] == v, f"Gram mismatch at {k}: {gram[k]}"
log(f"VERIFIED: all {n_moments} moments of total degree <= 4: every odd-parity "
    "one vanishes; Gram diagonal with the recorded values")
R["low_degree_census"] = {"n_moments": n_moments,
                          "odd_parity_all_zero": True,
                          "gram_matches_claimed": True}

# ---------------- rebuild the 128 representatives ---------------------------
FLIP = {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}
def flip_root(r):
    return tuple(r[FLIP[i]] for i in range(6))
assert all(C[FLIP[i]][FLIP[j]] == C[i][j] for i in range(6) for j in range(6))

ridx = {r: i for i, r in enumerate(ROOTS)}
rows, rhs = [], []
for a_ in ROOTS:
    for b_ in ROOTS:
        s_ = tuple(a_[i] + b_[i] for i in range(6))
        if s_ in ridx:
            row = [0] * 72
            row[ridx[a_]] ^= 1; row[ridx[b_]] ^= 1; row[ridx[s_]] ^= 1
            cc = eps(a_, b_) * eps(flip_root(a_), flip_root(b_))
            rows.append(row); rhs.append(0 if cc == 1 else 1)
Aug = [row + [r_] for row, r_ in zip(rows, rhs)]
rank2 = 0
for c_ in range(72):
    piv = next((i for i in range(rank2, len(Aug)) if Aug[i][c_]), None)
    if piv is None:
        continue
    Aug[rank2], Aug[piv] = Aug[piv], Aug[rank2]
    for i in range(len(Aug)):
        if i != rank2 and Aug[i][c_]:
            Aug[i] = [x ^ y for x, y in zip(Aug[i], Aug[rank2])]
    rank2 += 1
assert not any(sum(row[:72]) == 0 and row[72] for row in Aug), "cocycle inconsistent"
sol = [0] * 72
for i in range(rank2):
    c_ = next(cc for cc in range(72) if Aug[i][cc])
    sol[c_] = Aug[i][72]
dcoc = {ROOTS[i]: (-1) ** sol[i] for i in range(72)}
log("tau cocycle re-solved: F2 rank", rank2)

def chi_of(signs):
    def ch(r):
        v = 1
        for i in range(6):
            if r[i] % 2:
                v *= signs[i]
        return v
    return ch

def mono_inner(signs):
    """monomial map as dict col -> (row, coef)."""
    ch = chi_of(signs)
    m = {j: (j, 1) for j in range(6)}
    for r in ROOTS:
        m[6 + IDX[r]] = (6 + IDX[r], ch(r))
    return m

def mono_outer(signs):
    ch = chi_of(signs)
    m = {j: (FLIP[j], 1) for j in range(6)}
    for r in ROOTS:
        fr = flip_root(r)
        m[6 + IDX[r]] = (6 + IDX[fr], dcoc[r] * ch(fr))
    return m

def mono_omega():
    m = {j: (j, -1) for j in range(6)}
    for r in ROOTS:
        m[6 + IDX[r]] = (6 + IDX[tuple(-x for x in r)], 1)
    return m

def mono_compose(m2, m1):          # apply m1 then m2
    out = {}
    for j, (i, c) in m1.items():
        i2, c2 = m2[i]
        out[j] = (i2, c2 * c)
    return out

def mono_apply(m, vec):
    out = [Fraction(0)] * 78
    for j in range(78):
        if vec[j]:
            i, c = m[j]
            out[i] += c * vec[j]
    return out

def mono_is_identity(m):
    return all(m[j] == (j, 1) for j in range(78))

def mono_pattern(m):
    out = []
    for n in ns:
        vec = [Fraction(c) for c in INV[n]]
        img = mono_apply(m, vec)
        for s_ in (1, -1):
            if all(img[k] == s_ * vec[k] for k in range(78)):
                out.append(s_); break
        else:
            return None
    return tuple(out)

def mono_fix_dim(m):
    """dim ker(M - I) exactly: cycles of the signed permutation."""
    seen, fix = [False] * 78, 0
    for j in range(78):
        if seen[j]:
            continue
        cyc, sgn, cur = [], 1, j
        while not seen[cur]:
            seen[cur] = True
            cyc.append(cur)
            cur, c = m[cur]
            sgn *= c
        # cycle of length L with sign product s: eigenvalue 1 iff s == +1
        if sgn == 1:
            fix += 1
    return fix

def mono_to_dm(m):
    rowsL = [[QQ.zero] * 78 for _ in range(78)]
    for j, (i, c) in m.items():
        rowsL[i][j] = QQ(c)
    return DomainMatrix(rowsL, (78, 78), QQ)

def is_auto_via_br(m):
    """[M b_p, M b_q] == M [b_p, b_q] for ALL 78^2 pairs, via the frame's br()."""
    def basis_vec(k):
        v = [Fraction(0)] * 78
        v[k] = Fraction(1)
        return v
    imgs = [mono_apply(m, basis_vec(p)) for p in range(78)]
    for p in range(78):
        for q in range(78):
            lhs = br(imgs[p], imgs[q])
            rhs = mono_apply(m, [Fraction(c) for c in BB[p][q]])
            if lhs != rhs:
                return False
    return True

OMEGA = mono_omega()
assert is_auto_via_br(OMEGA) and mono_is_identity(mono_compose(OMEGA, OMEGA))
log("VERIFIED: omega is an automorphism (all 78^2 pairs, br path) and omega^2 = id")

scan = []
for kind, builder in (("inner", mono_inner), ("outer", mono_outer)):
    for signs in itertools.product((1, -1), repeat=6):
        m = builder(signs)
        pat = mono_pattern(m)
        if pat is not None:
            scan.append((kind, signs, m, pat))
assert len(scan) == 8, f"C-compatible count {len(scan)} != 8"
log("VERIFIED: the 128-rescan finds exactly 8 C-compatible representatives")

CLAIMED = {
    ("inner", (1, 1, 1, 1, 1, 1)):        ((1, 1, 1, 1), 78, 36),
    ("inner", (1, -1, -1, 1, -1, 1)):     ((1, -1, 1, -1), 38, 36),
    ("inner", (-1, 1, 1, -1, 1, -1)):     ((1, -1, 1, -1), 38, 36),
    ("inner", (-1, -1, -1, -1, -1, -1)):  ((1, 1, 1, 1), 38, 36),
    ("outer", (1, 1, -1, -1, -1, 1)):     ((-1, -1, -1, -1), 36, 38),
    ("outer", (1, -1, 1, -1, 1, 1)):      ((-1, 1, -1, 1), 36, 38),
    ("outer", (-1, 1, -1, 1, -1, -1)):    ((-1, 1, -1, 1), 52, 38),
    ("outer", (-1, -1, 1, 1, 1, -1)):     ((-1, -1, -1, -1), 36, 38)}
reps_out, MONO = [], {}
for kind, signs, m, pat in scan:
    key = (kind, signs)
    assert key in CLAIMED, f"unexpected representative {key}"
    cpat, cfix, ccomp = CLAIMED[key]
    assert pat == cpat, f"{key}: pattern {pat} != {cpat}"
    assert is_auto_via_br(m), f"{key}: not an automorphism"
    assert mono_is_identity(mono_compose(m, m)), f"{key}: not an involution"
    fix = mono_fix_dim(m)
    fix_dm = 78 - mono_to_dm(m).add(DomainMatrix.eye(78, QQ).to_dense() * QQ(-1)).rank()
    assert fix == fix_dm == cfix, f"{key}: fix {fix}/{fix_dm} != {cfix}"
    comp = mono_compose(m, OMEGA)
    assert mono_is_identity(mono_compose(comp, comp)), f"{key}: (phi.omega)^2 != id"
    cfixd = mono_fix_dim(comp)
    assert cfixd == ccomp, f"{key}: composite fix {cfixd} != {ccomp}"
    MONO[key] = m
    reps_out.append({"kind": kind, "signs": list(signs), "pattern": list(pat),
                     "auto_br_all_pairs": True, "involution": True,
                     "fixed_dim": fix, "composite_omega_fixed_dim": cfixd})
    log(f"VERIFIED {kind} {signs}: pattern {pat}, fix {fix}, "
        f"phi.omega fix {cfixd}, involution, automorphism")
R["representatives"] = reps_out
R["rescan_count_C_compatible"] = 8

# ---------------- structure ranks -------------------------------------------
def stack(mats):
    tot = sum(M.shape[0] for M in mats)
    rowsL = []
    for M in mats:
        rowsL += M.to_list()
    return DomainMatrix(rowsL, (tot, 78), QQ)

r8, r16 = DM[8].rank(), DM[16].rank()
rpair = stack([DM[8], DM[16]]).rank()
rall = stack([DM[n] for n in ns]).rank()
assert r8 == r16 == rpair == 48, (r8, r16, rpair)
assert rall == 66
log("VERIFIED: rank A8 = rank A16 = rank[A8;A16] = 48  =>  "
    "ker ad x8 = ker ad x16 exactly (dim 30 = dim a)")
log("VERIFIED: rank of the 4-stack = 66  =>  dim z(C) = 12")
# no nilpotency at the zero weight: rank(A^2) = rank(A) certifies that the
# generalized 0-eigenspace equals the literal kernel -- the exact fact the
# pairing formula fix(phi') = 24 + fix(phi'|_a) rests on.
sq = {n: (DM[n] * DM[n]).rank() for n in ns}
assert sq[8] == 48 and sq[16] == 48 and sq[14] == 66 and sq[22] == 66, sq
log("VERIFIED: rank(A^2) = rank(A) for all four charges  =>  "
    "generalized kernel = kernel (no Jordan blocks at 0)")
R["structure"] = {"rank_A8": 48, "rank_A16": 48, "rank_pair_stack": 48,
                  "ker_equality": True, "dim_a": 30, "rank_4stack": 66,
                  "dim_zC": 12,
                  "rank_squares": {str(n): sq[n] for n in ns},
                  "generalized_kernel_equals_kernel": True}

# ---------------- the wall pair ---------------------------------------------
W1 = ("outer", (1, -1, 1, -1, 1, 1))
W2 = ("outer", (-1, 1, -1, 1, -1, -1))
IEYE = DomainMatrix.eye(78, QQ).to_dense()
fixes = {}
for key in (W1, W2):
    Mdm = mono_to_dm(MONO[key])
    inter = 78 - stack([Mdm.add(IEYE * QQ(-1)), DM[8], DM[16]]).rank()
    fixes[key] = inter
assert fixes[W1] == 12 and fixes[W2] == 28, fixes
assert 24 + fixes[W1] == 36 and 24 + fixes[W2] == 52
log("VERIFIED: fix(phi|a) = 12 / 28; bookkeeping fix(phi) = 24 + fix(phi|a) "
    "= 36 / 52")
prod = mono_compose(MONO[W1], MONO[W2])
allminus = mono_inner((-1,) * 6)
assert all(prod[j] == allminus[j] for j in range(78))
log("VERIFIED: phi1 . phi2 == the inner all-minus character (exact)")
R["wall_pair"] = {"fix_on_a": {"phi1": 12, "phi2": 28},
                  "bookkeeping_24_plus": True,
                  "product_is_inner_allminus": True}

# ---------------- the pattern-level logic, replayed -------------------------
survivors, killed = [], []
for pat in itertools.product((1, -1), repeat=4):
    e8, e14, e16, e22 = pat
    k1 = (e14 * e22 == -1)      # killed by tr(A14 A22^5) != 0, parity (0,1,0,1)
    k2 = (e8 * e16 == -1)       # killed by tr(A8 A16 A22^4) != 0, parity (1,0,1,0)
    (killed if (k1 or k2) else survivors).append(pat)
assert len(killed) == 12 and len(survivors) == 4
realized = sorted({tuple(r["pattern"]) for r in reps_out})
assert sorted(survivors) == realized, (survivors, realized)
wall_ok = [p for p in survivors if p[1] == 1 and p[2] == -1]
assert wall_ok == [(-1, 1, -1, 1)]
log("VERIFIED: the two certificates kill exactly the 12 non-(a,b,a,b) "
    "patterns; the 4 survivors are exactly the realized ones; the unique "
    "wall-compatible survivor is (-1,+1,-1,+1)")
R["pattern_logic"] = {
    "killed": [list(p) for p in sorted(killed)],
    "survivors": [list(p) for p in sorted(survivors)],
    "survivors_equal_realized": True,
    "unique_wall_pattern": [-1, 1, -1, 1]}

R["ALL_CHECKS_PASSED"] = True
json.dump(R, open(OUT, "w"), indent=1)
log("ALL CHECKS PASSED ->", OUT)
