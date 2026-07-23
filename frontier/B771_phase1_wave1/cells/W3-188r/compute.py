#!/usr/bin/env python3
"""
W3-188r (H114 kappa-naming: tiers) -- wave-2 carry, fixing a real wave-2 defect.

DEFECT BEING FIXED (read from cells/W2-188/):
  W2-188's compute.py EXPLICITLY comments (line ~282): "tier omitted here -- tier
  needs the interaction-form Galois-channel computation, out of scope for kappa_q
  re-derivation". Despite that, its "READING" narration (compute.py lines 318-319)
  and PATCH 6 (proposed_patches.md, the flagship-paper edit) then HAND-ASSERT
  specific tier labels that were never computed:
      "(2,6)=15dark vs (4,6)=15dark [same], (2,12)=15dark vs (4,12)=15qrs
       [DIFFERENT TIER, same value] ... They first diverge in tier at gy=12"
  This is precisely a hand-read value smuggled into a claim that reads as computed,
  and it was headed into the flagship paper's S4.1 patch. This cell:
    1. Locates the ACTUAL S4.3 tier definition and printed master table in
       papers/P4_markov_stage/DRAFT_v8.md (Theorem G(ii)) -- the real ground truth,
       not S4.1's 5x5 value sample that W2-188 conflated it with.
    2. COMPUTES every one of the 36 divisor-lattice tiers from the interaction-form
       definition itself (Galois-channel vanishing pattern of tr(Par.P_a.Q_b) in the
       basis {1,sqrt5,sqrt-3,sqrt-15}), via TWO independent code paths:
         (a) exact cyclotomic arithmetic (Fraction-exact, Q(zeta_60) as a 16-dim
             Q-vector space) -- the repo's banked B358/B367/B468 engine, invoked
             fresh here on the full 20x12 grid (not merely imported as a citation:
             every one of the 240 points is recomputed in this process);
         (b) an independent floating-point numpy reconstruction of the SAME
             W1,W2,Par matrices and the SAME Fourier/projector formula, used to
             numerically verify the exact coefficients reconstruct the traces
             (two independent implementations = the >=2-seed check).
    3. Diffs the from-scratch 36-cell (value,tier) table against the printed S4.3
       table (transcribed verbatim from the paper) -- checks the PAPER, not W2-188.
    4. Pulls out the gx=2 vs gx=4 row comparison across all 6 gy values EXACTLY
       (the object of the wave-2 hand-read) and reports, with citations to computed
       cells, exactly where the two rows agree/disagree in TIER -- adjudicating the
       "first diverge in tier at gy=12" claim.
    5. A vacuity self-test: corrupts the interaction-form data and shows the check
       stops passing (the check has discriminating power, is not a tautology).
"""
import sys
import os
import math
import cmath

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "frontier", "B358_seam_certification"))
sys.path.insert(0, os.path.join(ROOT, "frontier", "B367_value_map"))
sys.path.insert(0, os.path.join(ROOT, "frontier", "B465_monodromy_intake"))

import cyclo_engine as E                       # noqa: E402
import seam_certification as SC                 # noqa: E402
from step0_exact_matrices import build_theta_W, matrix_order, pair_smatrix  # noqa: E402
from exact_engine import build as build_fp, matmul as matmul_fp             # noqa: E402

LOG = []


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.append(s)


# ==============================================================================
# PART 0 -- locate the ground truth: transcribe S4.3's printed master table
# (papers/P4_markov_stage/DRAFT_v8.md, Theorem G(ii), lines 475-482) VERBATIM,
# character for character, before computing anything, so the diff below is
# against the actual paper text, not a memory of it.
# ==============================================================================
PAPER_PATH = os.path.join(ROOT, "papers", "P4_markov_stage", "DRAFT_v8.md")

# (kappa_q value, tier) exactly as printed at gx in {1,2,4,5,10,20} x gy in {1,2,3,4,6,12}
PRINTED_S43 = {
    (1, 1): (-1, "free"), (1, 2): (3, "free"), (1, 3): (-5, "qs"),
    (1, 4): (3, "free"), (1, 6): (15, "dark"), (1, 12): (15, "dark"),
    (2, 1): (3, "free"), (2, 2): (3, "free"), (2, 3): (15, "dark"),
    (2, 4): (3, "dark"), (2, 6): (15, "qrs"), (2, 12): (15, "dark"),
    (4, 1): (3, "free"), (4, 2): (3, "dark"), (4, 3): (15, "dark"),
    (4, 4): (3, "free"), (4, 6): (15, "dark"), (4, 12): (15, "qrs"),
    (5, 1): (-5, "free"), (5, 2): (15, "rs"), (5, 3): (-5, "qs"),
    (5, 4): (15, "rs"), (5, 6): (15, "dark"), (5, 12): (15, "dark"),
    (10, 1): (15, "rs"), (10, 2): (15, "rs"), (10, 3): (15, "dark"),
    (10, 4): (15, "dark"), (10, 6): (15, "qrs"), (10, 12): (15, "dark"),
    (20, 1): (15, "rs"), (20, 2): (15, "dark"), (20, 3): (15, "dark"),
    (20, 4): (15, "rs"), (20, 6): (15, "dark"), (20, 12): (15, "qrs"),
}


def part0_transcription_selfcheck():
    log("=" * 78)
    log("PART 0 -- transcription self-check of the printed S4.3 table")
    log("=" * 78)
    assert os.path.exists(PAPER_PATH), "paper file not found"
    with open(PAPER_PATH) as f:
        text = f.read()
    # sanity: the raw table rows must literally appear in the paper text (exact
    # substring match), so PRINTED_S43 cannot silently drift from the source.
    raw_rows = {
        1: "| **1** | −1 free | 3 free | −5 qs | 3 free | 15 dark | 15 dark |",
        2: "| **2** | 3 free | 3 free | 15 dark | 3 dark | 15 qrs | 15 dark |",
        4: "| **4** | 3 free | 3 dark | 15 dark | 3 free | 15 dark | 15 qrs |",
        5: "| **5** | −5 free | 15 rs | −5 qs | 15 rs | 15 dark | 15 dark |",
        10: "| **10** | 15 rs | 15 rs | 15 dark | 15 dark | 15 qrs | 15 dark |",
        20: "| **20** | 15 rs | 15 dark | 15 dark | 15 rs | 15 dark | 15 qrs |",
    }
    all_found = True
    for gx, row in raw_rows.items():
        found = row in text
        all_found &= found
        log(f"  row gx={gx:>2} literal match in DRAFT_v8.md: {found}")
    log("PART 0 verdict:", "PASS (PRINTED_S43 is a verbatim transcription)" if all_found
        else "FAIL -- transcription drift, STOP")
    assert all_found
    return all_found


# ==============================================================================
# PART 1 -- compute kappa_q(j,l) exactly on the full 20x12 grid (F_p engine,
# two primes; same method as W2-188, re-run fresh here since Part 3 needs the
# value half for the combined (value,tier) diff).
# ==============================================================================
def compute_kappa_grid(p):
    z, i4, W1, W2, Par = build_fp(p, c=1)

    def matinv(M, p=p):
        n = len(M)
        A = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(M)]
        for c in range(n):
            piv = next(i for i in range(c, n) if A[i][c] % p)
            A[c], A[piv] = A[piv], A[c]
            inv = pow(A[c][c], p - 2, p)
            A[c] = [(x * inv) % p for x in A[c]]
            for i in range(n):
                if i != c and A[i][c]:
                    f = A[i][c]
                    A[i] = [(a - f * b) % p for a, b in zip(A[i], A[c])]
        return [r[n:] for r in A]

    def matpow(M, k):
        n = len(M)
        R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        while k:
            if k & 1:
                R = matmul_fp(R, M, p)
            M = matmul_fp(M, M, p)
            k >>= 1
        return R

    table = {}
    for j in range(1, 21):
        A = matpow(W1, j)
        for l in range(1, 13):
            B = matpow(W2, l)
            C = matmul_fp(matmul_fp(A, B, p), matmul_fp(matinv(A), matinv(B), p), p)
            t = sum(C[i][i] for i in range(15)) % p
            table[(j, l)] = t if t <= p // 2 else t - p
    return table


def part1_kappa_values():
    log("=" * 78)
    log("PART 1 -- kappa_q(j,l) recomputed exactly, two primes, full 240-point grid")
    log("=" * 78)
    grids = {}
    for p in (61, 421):
        grids[p] = compute_kappa_grid(p)
    diffs = [(j, l) for j in range(1, 21) for l in range(1, 13)
              if grids[61][(j, l)] != grids[421][(j, l)]]
    log(f"cross-prime (61 vs 421) agreement: {240-len(diffs)}/240",
        "-- PASS" if not diffs else f"-- FAIL {diffs[:5]}")
    assert not diffs
    kappa = grids[61]
    # reduce to the 36-cell divisor lattice and check single-valuedness
    cells_val = {}
    viol = []
    for (j, l), v in kappa.items():
        key = (math.gcd(j, 20), math.gcd(l, 12))
        if key in cells_val and cells_val[key] != v:
            viol.append((key, cells_val[key], v))
        cells_val[key] = v
    log(f"kappa_q single-valuedness on (gx,gy): {len(viol)} violations",
        "-- PASS" if not viol else f"-- FAIL {viol}")
    assert not viol
    return kappa, cells_val


# ==============================================================================
# PART 2 -- compute the TIER of every one of the 240 points from the actual
# interaction-form definition, exact cyclotomic arithmetic (route A).
# ==============================================================================
# channel order in solve_H's output vector: (1, sqrt5, sqrt-3, sqrt-15) -- index
# i in {0,1,2,3}; a channel VANISHES at (a,b) iff its coefficient is exactly 0.
TIER_FROM_PATTERN = {
    (0, 0, 0, 0): "free",   # none vanish
    (0, 0, 1, 1): "rs",     # sqrt-3, sqrt-15 vanish
    (0, 1, 0, 1): "qs",     # sqrt5, sqrt-15 vanish
    (0, 1, 1, 1): "qrs",    # sqrt5, sqrt-3, sqrt-15 vanish (only rational survives)
    (1, 1, 1, 1): "dark",   # all four vanish
}
CHANNEL_NAMES = ["rat", "sqrt5", "sqrt-3", "sqrt-15"]


def exact_tier_grid():
    """Route A: exact cyclotomic construction, full 20x12 grid.

    (a,b) are the SAME order-torus exponent labels as kappa_q(j,l) -- Theorem
    G(ii) states both maps live on the same divisor lattice. sm(a,b) =
    tr(Par.P_a.Q_b) (spectral projector traces) gives the exact (p,q,r,s)
    H-coordinates directly at each (a,b); its nonzero support, re-summed with
    weights zeta_20^{ax}.zeta_12^{by} (via the zeta_60 embedding 3*20=5*12=60),
    reconstructs each Galois channel's contribution AT THE SAME point (x,y)=(a,b)
    read as an order-torus point. A channel VANISHES there iff the full 16-dim
    Q(zeta_60) reconstruction is exactly the zero vector -- checked exactly, no
    plain-rational assumption of any kind (this fixes an over-strong assumption
    from an earlier draft of this cell, caught by the assertion it tripped)."""
    W1 = build_theta_W(1)
    W2 = build_theta_W(2)
    o1, pow1 = matrix_order(W1)
    o2, pow2 = matrix_order(W2)
    assert (o1, o2) == (20, 12), (o1, o2)
    sm = pair_smatrix(pow1, pow2)   # {(a,b): (p,q,r,s)} over nonzero total only
    # per-channel nonzero spectral support (this IS the "interaction form" data)
    chan = {i: {(a, b): v[i] for (a, b), v in sm.items() if v[i] != 0} for i in range(4)}
    patterns = {}      # (j,l) -> vanishing pattern tuple (bit i =1 means channel i is 0)
    for x in range(20):
        for y in range(12):
            pat = []
            for i in range(4):
                t = E.ZERO
                for (a, b), val in chan[i].items():
                    t = E.add(t, E.scal(SC.Fr(val), E.zeta((3 * a * x + 5 * b * y) % 60)))
                pat.append(1 if t == E.ZERO else 0)
            j = x if x != 0 else 20
            l = y if y != 0 else 12
            patterns[(j, l)] = tuple(pat)
    return sm, chan, patterns


def part2_exact_tiers():
    log("=" * 78)
    log("PART 2 -- exact tier computation (route A: cyclotomic Q(zeta_60) engine)")
    log("=" * 78)
    sm, chan, patterns = exact_tier_grid()
    log(f"points computed: {len(patterns)} (expect 240) -- ",
        "PASS" if len(patterns) == 240 else "FAIL")
    assert len(patterns) == 240
    bad_patterns = [pt for pt, pat in patterns.items() if pat not in TIER_FROM_PATTERN]
    log(f"every pattern is one of the 5 legal tiers: {len(bad_patterns)} exceptions",
        "-- PASS" if not bad_patterns else f"-- FAIL {bad_patterns[:5]}")
    assert not bad_patterns
    tiers = {pt: TIER_FROM_PATTERN[pat] for pt, pat in patterns.items()}
    from collections import Counter
    counts = Counter(tiers.values())
    log("global tier point-counts (all 240 points, no gcd-reduction yet):",
        dict(counts))
    log("paper's stated counts (Theorem G(ii) prose): free=120 qs=20 rs=20 qrs=10 dark=70")
    expect = {"free": 120, "qs": 20, "rs": 20, "qrs": 10, "dark": 70}
    ok = all(counts.get(k, 0) == v for k, v in expect.items())
    log("counts match paper prose:", "PASS" if ok else "FAIL", dict(counts))
    assert ok
    return sm, chan, patterns, tiers


# ==============================================================================
# PART 3 -- Route B: an INDEPENDENT floating-point cross-check (cmath, no
# cyclo_engine, no Fraction arithmetic, no shared code with Part 2 beyond the
# bare mathematical definition of W1/W2/Par), in two stages, matching the
# house method's >=2-seed / two-independent-implementations rule:
#
#   3a. Rebuild W1, W2, Par as floating complex matrices from the SAME level-15
#       definition (Hannay-Berry Weil rep), independently of build_theta_W;
#       forward-DFT the 240 physical traces C[j,l]=tr(Par.W1^j.W2^l) into
#       spectral values t_num(a,b); compare against the EXACT (p,q,r,s) from
#       `sm` (Part 2's spectral data) converted to a complex float. This
#       validates the SPECTRAL data sm independently of cyclo_engine.
#   3b. Using sm's exact rational support (already cross-checked in 3a),
#       redo the (a,b)->(x,y) physical-point reconstruction that Part 2 does
#       in exact arithmetic, but in floats with a numeric threshold, and
#       compare the resulting ZERO/NONZERO pattern against Part 2's exact
#       pattern at all 240*4 = 960 channel entries. This validates the
#       RECONSTRUCTION step independently of cyclo_engine's exact-zero test.
# ==============================================================================
def numeric_route_B(sm, patterns_exact):
    log("=" * 78)
    log("PART 3 -- route B: independent floating-point cross-check (cmath, no")
    log("cyclo_engine, no shared code with Part 2's exact arithmetic)")
    log("=" * 78)
    N = 15

    def matmul_c(A, B):
        n = len(A)
        return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

    def matpow_c(M, k):
        n = len(M)
        R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        while k:
            if k & 1:
                R = matmul_c(R, M)
            M = matmul_c(M, M)
            k >>= 1
        return R

    def build_Cjl(root60):
        """The full construction (Dn, F, Wr, W1, W2, Par, all traces C[j,l]) built
        from a SPECIFIC primitive 60th root of unity `root60` (not necessarily
        exp(2pi i/60)) -- i.e. the level-15 Weil rep evaluated at an arbitrary
        embedding. Feeding root60 = exp(2pi i c/60) for c coprime to 60 realizes
        the Galois automorphism sigma_c numerically (this is the ONLY correct way
        to numerically apply a cyclotomic Galois automorphism to an algebraic
        construction: re-evaluate the whole polynomial expression at the
        conjugate root, not manipulate a bare complex number after the fact)."""
        zc = root60 ** 4   # zeta_15 under this embedding (zeta_15 = zeta_60^4)
        Dn = [[zc ** ((j * (j - 1) // 2) % N) if i == j else 0 for j in range(N)] for i in range(N)]
        F = [[zc ** ((i * j) % N) for j in range(N)] for i in range(N)]
        Fh = [[F[j][i].conjugate() for j in range(N)] for i in range(N)]  # F^*
        F = [[x / math.sqrt(N) for x in row] for row in F]
        Fh = [[x / math.sqrt(N) for x in row] for row in Fh]
        WR_pre = matmul_c(matmul_c(F, Dn), Fh)
        Wr = [[WR_pre[j][i].conjugate() for j in range(N)] for i in range(N)]  # (F D F*)*
        Wl = Dn
        W1 = matmul_c(Wr, Wl)
        W2 = matmul_c(matmul_c(Wr, Wr), matmul_c(Wl, Wl))
        Par = [[1 if i == (-j) % N else 0 for j in range(N)] for i in range(N)]
        W1p = [matpow_c(W1, j) for j in range(20)]
        W2p = [matpow_c(W2, l) for l in range(12)]

        def trace_par(A, B):
            C = matmul_c(A, B)
            t = 0
            for x in range(N):
                row = [Par[y][x] for y in range(N)]
                src = row.index(1)
                t += C[src][x]
            return t

        return {(j, l): trace_par(W1p[j], W2p[l]) for j in range(20) for l in range(12)}

    # --- 3a: the SAME 4-fold Galois-averaging the exact route performs
    # (GAL_H = [1,19,31,49] = Gal(Q(zeta_60)/H), banked in
    # frontier/B358_seam_certification/seam_certification.py), reproduced
    # numerically at each of 4 independent embeddings, then averaged, and
    # compared against the exact sm (p,q,r,s) -- this is the genuine 2-seed
    # cross-check: NOT skipping the averaging step (an earlier draft of this
    # cell mistakenly compared the un-averaged raw trace and failed hard --
    # max error 0.19 -- catching that this step is load-bearing, not optional).
    GAL_H = [1, 19, 31, 49]
    Cjl_by_c = {}
    for c in GAL_H:
        root = cmath.exp(2j * math.pi * c / 60)
        Cjl_by_c[c] = build_Cjl(root)

    sqrt5 = math.sqrt(5)
    sqrt3 = math.sqrt(3)
    sqrt15 = math.sqrt(15)
    max_err_spectral = 0.0
    worst_spectral = None
    t_avg_all = {}
    for a in range(20):
        for b in range(12):
            acc = 0j
            for c in GAL_H:
                root = cmath.exp(2j * math.pi * c / 60)
                Cjl = Cjl_by_c[c]
                tnum = 0j
                for j in range(20):
                    for l in range(12):
                        tnum += root ** (-3 * j * a) * root ** (-5 * l * b) * Cjl[(j, l)]
                tnum /= 240
                acc += tnum
            t_avg = acc / 4
            t_avg_all[(a, b)] = t_avg
            p, q, r, s = (float(c) for c in sm.get((a, b), (0, 0, 0, 0)))
            predicted = complex(p + q * sqrt5, r * sqrt3 + s * sqrt15)
            err = abs(t_avg - predicted)
            if err > max_err_spectral:
                max_err_spectral = err
                worst_spectral = (a, b, t_avg, predicted)
    log("3a. spectral cross-check: 4-fold Galois-averaged float forward-DFT vs exact sm,")
    log("    240 points:")
    log(f"    max error = {max_err_spectral:.3e}, worst point = {worst_spectral}")
    tol = 10 ** -9
    ok_a = max_err_spectral < tol
    log("    tolerance 1e-9 (>=9 significant digits):", "PASS" if ok_a else "FAIL")
    assert ok_a

    # --- 3b: float physical-point reconstruction, compare zero-pattern ---
    chan_f = {i: {(a, b): float(v[i]) for (a, b), v in sm.items() if v[i] != 0}
              for i in range(4)}
    mismatches = []
    min_nonzero_abs = None
    for x in range(20):
        for y in range(12):
            pat = []
            for i in range(4):
                t = 0j
                for (a, b), val in chan_f[i].items():
                    t += val * cmath.exp(2j * math.pi * (3 * a * x + 5 * b * y) / 60)
                is_zero = abs(t) < 1e-8
                pat.append(1 if is_zero else 0)
                if not is_zero and (min_nonzero_abs is None or abs(t) < min_nonzero_abs):
                    min_nonzero_abs = abs(t)
            j = x if x != 0 else 20
            l = y if y != 0 else 12
            if tuple(pat) != patterns_exact[(j, l)]:
                mismatches.append(((j, l), tuple(pat), patterns_exact[(j, l)]))
    log(f"3b. physical-point float reconstruction vs exact pattern, 240*4=960 entries:")
    log(f"    mismatches: {len(mismatches)}", "-- PASS" if not mismatches else f"-- FAIL {mismatches[:5]}")
    log(f"    smallest float magnitude among entries the exact route calls NONZERO: "
        f"{min_nonzero_abs:.3e} (threshold 1e-8 -- comfortable separation from 0 "
        f"confirms no near-degenerate/ambiguous point)")
    assert not mismatches
    return ok_a and not mismatches


# ==============================================================================
# PART 4 -- reduce the exact 240-point tier grid to the 36-cell divisor lattice,
# check single-valuedness, and diff against the PRINTED S4.3 table.
# ==============================================================================
def part4_lattice_and_diff(kappa, tiers):
    log("=" * 78)
    log("PART 4 -- 36-cell divisor-lattice reduction + diff vs printed S4.3")
    log("=" * 78)
    cells = {}
    viol = []
    for (j, l), tname in tiers.items():
        key = (math.gcd(j, 20), math.gcd(l, 12))
        v = kappa[(j, l)]
        if key in cells and cells[key] != (v, tname):
            viol.append((key, cells[key], (v, tname)))
        cells[key] = (v, tname)
    log(f"tier+value single-valuedness on (gx,gy): {len(viol)} violations",
        "-- PASS (factors through gcd exactly)" if not viol else f"-- FAIL {viol}")
    assert not viol
    log(f"lattice cells populated: {len(cells)} (expect 36)")
    assert len(cells) == 36

    log("")
    log("Full 36-cell computed table (ours) vs printed S4.3, every cell:")
    disagreements = []
    for gx in sorted({k[0] for k in cells}):
        for gy in sorted({k[1] for k in cells if k[0] == gx}):
            ours = cells[(gx, gy)]
            theirs = PRINTED_S43.get((gx, gy))
            mark = "OK" if ours == theirs else "MISMATCH"
            if ours != theirs:
                disagreements.append(((gx, gy), ours, theirs))
            log(f"  (gx={gx:>2},gy={gy:>2}): ours={ours}  printed={theirs}  [{mark}]")
    log("")
    log(f"TOTAL disagreements (value+tier) vs printed S4.3 table: {len(disagreements)}",
        "-- PAPER CONFIRMED" if not disagreements else f"-- DISCREPANCIES: {disagreements}")
    return cells, disagreements


# ==============================================================================
# PART 5 -- the actual object of this cell: adjudicate the wave-2 hand-read.
# Pull the gx=2 and gx=4 rows and diff them column by column (all 6 gy), in
# BOTH value and tier, and check the specific W2-188 claims:
#   (a) "(2,6)=dark, (4,6)=dark [same]"
#   (b) "(2,12)=dark, (4,12)=qrs [DIFFERENT TIER, same value]"
#   (c) "gx=4 first diverges from gx=2 ... at gy=6 or gy=12"
#        i.e. the IMPLICIT claim that gy=1,2,3,4 all AGREE in tier between
#        gx=2 and gx=4 (since the divergence is asserted to first appear at 6/12).
# ==============================================================================
def part5_adjudicate_wave2(cells):
    log("=" * 78)
    log("PART 5 -- adjudicating the W2-188 gx=2-vs-gx=4 tier claims")
    log("=" * 78)
    gys = [1, 2, 3, 4, 6, 12]
    row2 = {gy: cells[(2, gy)] for gy in gys}
    row4 = {gy: cells[(4, gy)] for gy in gys}
    log(f"{'gy':>3} | {'gx=2 (val,tier)':>18} | {'gx=4 (val,tier)':>18} | value-same tier-same")
    first_tier_divergence = None
    tier_matches = []
    for gy in gys:
        v2, t2 = row2[gy]
        v4, t4 = row4[gy]
        vsame = (v2 == v4)
        tsame = (t2 == t4)
        tier_matches.append(tsame)
        if not tsame and first_tier_divergence is None:
            first_tier_divergence = gy
        log(f"{gy:>3} | {str(row2[gy]):>18} | {str(row4[gy]):>18} | "
            f"{vsame!s:>5} {tsame!s:>5}")
    n_tier_same = sum(tier_matches)
    n_tier_diff = len(gys) - n_tier_same
    log("")
    log(f"Of the {len(gys)} gy values, TIER matches gx=2 vs gx=4 at {n_tier_same}, "
        f"DIFFERS at {n_tier_diff}.")
    log(f"Computed first tier-divergence gy: {first_tier_divergence}")

    log("")
    log("Checking the three specific W2-188 claims (proposed_patches.md Patch 6 / ")
    log("compute.py 'READING' text) against the computed table:")

    # claim (a): (2,6)=dark, (4,6)=dark [same]
    claim_a_2_6 = (cells[(2, 6)][1] == "dark")
    claim_a_4_6 = (cells[(4, 6)][1] == "dark")
    log(f"  claim (a) (2,6)=dark: computed tier = {cells[(2,6)][1]!r} -- ",
        "MATCHES CLAIM" if claim_a_2_6 else "CONTRADICTS CLAIM (W2-188 WRONG)")
    log(f"  claim (a) (4,6)=dark: computed tier = {cells[(4,6)][1]!r} -- ",
        "MATCHES CLAIM" if claim_a_4_6 else "CONTRADICTS CLAIM (W2-188 WRONG)")

    # claim (b): (2,12)=dark, (4,12)=qrs [different tier, same value]
    claim_b_2_12 = (cells[(2, 12)][1] == "dark")
    claim_b_4_12 = (cells[(4, 12)][1] == "qrs")
    claim_b_sameval = (cells[(2, 12)][0] == cells[(4, 12)][0])
    log(f"  claim (b) (2,12)=dark: computed tier = {cells[(2,12)][1]!r} -- ",
        "MATCHES CLAIM" if claim_b_2_12 else "CONTRADICTS CLAIM (W2-188 WRONG)")
    log(f"  claim (b) (4,12)=qrs: computed tier = {cells[(4,12)][1]!r} -- ",
        "MATCHES CLAIM" if claim_b_4_12 else "CONTRADICTS CLAIM (W2-188 WRONG)")
    log(f"  claim (b) same VALUE at gy=12: {claim_b_sameval} -- ",
        "MATCHES CLAIM" if claim_b_sameval else "CONTRADICTS CLAIM (W2-188 WRONG)")

    # claim (c): first tier-divergence is at gy=6 or gy=12 (i.e. gy in {1,2,3,4}
    # all tier-agree)
    claim_c = first_tier_divergence in (6, 12)
    log(f"  claim (c) 'first diverge in tier at gy=6 or 12' "
        f"(i.e. gy=1,2,3,4 all tier-agree): computed first divergence = "
        f"gy={first_tier_divergence} -- ",
        "MATCHES CLAIM" if claim_c else "CONTRADICTS CLAIM (W2-188 WRONG)")
    if not claim_c:
        wrong_gys = [gy for gy in (1, 2, 3, 4) if row2[gy][1] != row4[gy][1]]
        log(f"    -- specifically, gx=2 and gx=4 ALREADY DIFFER IN TIER at gy in "
            f"{wrong_gys} (before gy=6 at all)")

    verdict_wrong_claims = []
    if not claim_a_2_6:
        verdict_wrong_claims.append("(2,6)=dark")
    if not claim_a_4_6:
        verdict_wrong_claims.append("(4,6)=dark")
    if not claim_b_2_12:
        verdict_wrong_claims.append("(2,12)=dark")
    if not claim_b_4_12:
        verdict_wrong_claims.append("(4,12)=qrs")
    if not claim_c:
        verdict_wrong_claims.append("first-divergence-at-6-or-12")

    log("")
    log(f"SUMMARY: of 5 explicit/implicit W2-188 tier assertions checked, "
        f"{len(verdict_wrong_claims)} are WRONG: {verdict_wrong_claims}")
    log(f"Of the {len(gys)} gy columns compared tier-wise between gx=2 and gx=4, "
        f"the TRUE computed pattern is: agree at gy in "
        f"{[gy for gy in gys if row2[gy][1]==row4[gy][1]]}, "
        f"differ at gy in {[gy for gy in gys if row2[gy][1]!=row4[gy][1]]} "
        f"-- i.e. {n_tier_diff} of {len(gys)} gy-columns show a tier difference, "
        f"not the 1-of-6 (gy=12 only) that W2-188's narration implied.")
    return {
        "row2": row2, "row4": row4,
        "first_tier_divergence": first_tier_divergence,
        "n_tier_same": n_tier_same, "n_tier_diff": n_tier_diff,
        "wrong_claims": verdict_wrong_claims,
    }


# ==============================================================================
# PART 6 -- vacuity self-test: corrupt the interaction-form spectral data and
# show the diff-vs-paper check STOPS PASSING (i.e. the check has power; it is
# not a tautology that would "pass" no matter what we fed it).
# ==============================================================================
def part6_vacuity_selftest():
    log("=" * 78)
    log("PART 6 -- vacuity self-test (corrupt the construction, expect FAILURE)")
    log("=" * 78)
    W1 = build_theta_W(1)
    W2 = build_theta_W(2)
    o1, pow1 = matrix_order(W1)
    o2, pow2 = matrix_order(W2)
    sm = pair_smatrix(pow1, pow2)
    # corruption: swap the sqrt5 and sqrt-3 channels for every support point
    # (a free symbol substituted for the real quantity -- if our check were
    # vacuous/tautological this swap would still "pass" against the paper).
    sm_corrupt = {k: (v[0], v[2], v[1], v[3]) for k, v in sm.items()}
    chan = {i: {(a, b): v[i] for (a, b), v in sm_corrupt.items() if v[i] != 0} for i in range(4)}
    mismatches = 0
    total = 0
    for x in range(20):
        for y in range(12):
            pattern = []
            for i in range(4):
                t = E.ZERO
                for (a, b), val in chan[i].items():
                    t = E.add(t, E.scal(SC.Fr(val), E.zeta((3 * a * x + 5 * b * y) % 60)))
                pattern.append(1 if t == E.ZERO else 0)
            pattern = tuple(pattern)
            tname = TIER_FROM_PATTERN.get(pattern, "ILLEGAL")
            j = x if x != 0 else 20
            l = y if y != 0 else 12
            gx, gy = math.gcd(j, 20), math.gcd(l, 12)
            printed = PRINTED_S43.get((gx, gy))
            total += 1
            if printed is None:
                continue
            if tname != printed[1]:
                mismatches += 1
    log(f"with the sqrt5<->sqrt-3 channels SWAPPED, tier vs printed S4.3 mismatches: "
        f"{mismatches}/{total} points")
    ok = mismatches > 0
    log("vacuity self-test:",
        "PASS (corruption breaks agreement -- the real check is non-tautological)"
        if ok else "FAIL (corruption did not break agreement -- SELF-TEST FAILED, "
        "the diff check would be vacuous)")
    assert ok, "VACUITY SELF-TEST FAILED -- the tier check does not discriminate"
    return mismatches


def main():
    all_ok = True
    part0_transcription_selfcheck()
    kappa, cells_val_only = part1_kappa_values()
    sm, chan, patterns, tiers = part2_exact_tiers()
    numeric_route_B(sm, patterns)
    cells, disagreements = part4_lattice_and_diff(kappa, tiers)
    all_ok &= not disagreements
    adjud = part5_adjudicate_wave2(cells)
    part6_vacuity_selftest()

    log("=" * 78)
    log("SUMMARY")
    log("=" * 78)
    log("PART 0 (printed-table transcription self-check): PASS")
    log("PART 1 (kappa_q grid, 2 primes, single-valued): PASS")
    log("PART 2 (exact tier grid, route A, cyclotomic exact arithmetic): PASS")
    log("PART 3 (route B, independent float cross-check, tol 1e-9): PASS")
    log(f"PART 4 (36-cell table vs printed S4.3): "
        f"{'CONFIRMED, 0 disagreements' if not disagreements else f'{len(disagreements)} DISAGREEMENTS'}")
    log(f"PART 5 (W2-188 gx=2-vs-gx=4 tier claims): "
        f"{len(adjud['wrong_claims'])} of the checked W2-188 assertions are WRONG "
        f"-- {adjud['wrong_claims']}")
    log("PART 6 (vacuity self-test): PASS (check is discriminating)")
    log("")
    if disagreements:
        log("OVERALL: the PAPER's S4.3 table itself has a computed defect -- see PART 4.")
        all_ok = False
    else:
        log("OVERALL: the paper's S4.3 table is exactly correct; the defect was "
            "entirely in W2-188's hand-read narration/patch text (now identified "
            "and itemized in PART 5), not in the paper.")
    log(f"kappa/tier computation phase: {'ALL CHECKS PASS' if all_ok else 'FAILURES ABOVE'}")
    return all_ok, cells, adjud


if __name__ == "__main__":
    ok, cells, adjud = main()
    sys.exit(0 if ok else 1)
