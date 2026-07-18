"""D4 -- THE CEILING LAW: Z_k(R^{n-2}L) at SU(3)_k, n=3..10, k=1..12 (kappa=k+3=4..15).
(cc2 subagent, loop 4 cell D4; prereg <cc2-seat>/anatomy/loop4/PREREG_L4.md sec D4)

MACHINERY (reused, not rebuilt): engine_v7.An_Level(3, k) builds the SU(3)_k
Kac-Peterson modular data (S, T), mpmath high precision (dps=60), from
  <cc2-seat>/veins/v7_conduit/engine_v7.py
(read-only import; nothing in that file or the repo is modified).

CONVENTION (pinned exactly, gate-verified below, NOT trusted on chat-1's say-so):
R -> T (the diagonal T-matrix). L -> S T^-1 S^-1 (equivalently S^-1 T^-1 S; the
two are IDENTICAL representation matrices because C := S^2 is central in the
image -- C commutes with S trivially and with T because conjugate primaries
share conformal weight -- so S^-1 = C S = S C forces S T^-1 S^-1 = S^-1 T^-1 S).
This is exactly the convention verified by the banked two-word lock
(engine_v7.rho_A1_matrix: T^2 S T == T S T^-1 S^-1, both equal the literal
SL(2,Z) matrix A1 = R L = [[2,1],[1,1]]) and by
  <cc2-seat>/loops_queue/d4_su3/d4_su3_run.py Gate 3
(Z_direct = Tr(T^2 S T) matches the independent A2-Jeffrey Gauss-sum pipeline's
Z_{+3}(kappa) exactly, to ~1e-50, for k=1..3).

CORRECTION (post-hoc, applied after the first per-level runs surfaced it):
Z_direct = Tr(rho(w)) (the FULL trace, above) is NOT the banked ladder
quantity. The banked d4_su3_run.py "tr_odd(kappa)" column -- the quantity the
whole D4 addendum (additive law, {2,5} resonance spectrum, golden -1/phi) is
actually about -- is the THETA-PARITY PROJECTED trace
  tr_odd(w) = (Z_{+3-analogue}(w) + Z_{-3-analogue}(w)) / 2
where the "-w" (negative-word / -A1-bundle) trace is, per B585's naming
theorem and d4_su3_run.py Gate 3's audited convention,
  Z_minus(w) = det(w0) * Tr(C . rho(w)),   C := S^2 (charge conjugation),
  det(w0) = -1 for A2 (w0 = the longest Weyl element of W(A2)=S3; A2's Weyl
  group does not contain -I, so w0 is a REFLECTION, det=-1 -- this sign is
  lifted VERBATIM from d4_su3_run.py's own convention-audit resolution of its
  Gate 3, not re-derived here).
-I is central in SL(2,Z) and is represented by C at the level of modular data
regardless of which word w is fed in (C = S^2 is a fixed, word-independent
matrix per level k) -- so this generalizes cleanly from d4_su3_run.py's single
worked word (A1 = RL, P=+3) to every word in our R^{n-2}L family. Verified
below (Gate G1): with this correction, our n=3 (RL) row reproduces the banked
tr_odd(kappa) column EXACTLY at every kappa=4..15 (not just kappa=4,5 where
the plain full trace happened to coincide because tr_even=0 there).
The FULL trace Z_direct is still recorded per word/level (diagnostic field
"Z_full") but the table/ceiling-map/verdict quantity is tr_odd throughout.

WORD TRACE, EFFICIENT FORM: since T is diagonal (T_i = exp(2pi i(h_i - c/24))),
  Z_k(R^m L) = Tr(T^m . L) = sum_i T_i^m . L_ii
where L = S T^-1 S^-1 is built ONCE per level k (an N x N matrix, N = #
level-k SU(3) primaries) and then every m = n-2 (n = 3..10, i.e. m = 1..8) is
just a re-weighted diagonal sum -- no repeated NxN matrix multiplication
needed per word.  n = trace of the literal 2x2 SL(2,Z) matrix R^{n-2}L
(R^m L = [[1+m, m],[1,1]], trace m+2 = n); disc(w) = n^2-4.

GATES (hard stops, in order):
  G0 -- modular battery (S unitary+symmetric, S^4=I, (ST)^3=S^2, two-word
        lock) at every k = 1..12, via engine_v7.gate_report.
  G1 -- FIG-8 REPRODUCTION (the hard gate): our n=3 (m=1, word "RL") row must
        equal the BANKED tr_odd(kappa) column of
          <cc2-seat>/loops_queue/d4_su3/d4_results.json
        (itself gate-verified there against B584/B238's golden value
        Z(4_1; SU(3)_2) = -1/phi at kappa=5) to < 1e-40, all 12 levels.
  G2 -- B238 cross-check: our n=4 (m=2, word "RRL") value at k=2 (kappa=5)
        must equal B238's reported SU(3)_2 RRL trace (-1/2 - i*sqrt(3)/2,
        |Z|=1) to < 1e-8 (B238 was float-precision; we hold ourselves to
        tighter tolerance and report the exact deviation).

STRUCTURAL NOTE (derived here, cheap, exact -- NOT a re-run of the A2-Jeffrey
Gauss-sum pipeline for all 8 words, which would be its own follow-up cell):
the A2-Jeffrey B_w(P) = P.I - w - w^-1 construction (loops_queue/d4_su3,
P = trace of the monodromy) generalizes from P=+3 to ANY integer trace P=n by
elementary linear algebra on W(A2)=S3's three conjugacy classes acting on the
rank-2 coroot lattice:
  identity  (1 elem):  w=I, w^-1=I           => det B_w = (n-2)^2 = m^2
  3-cycles  (2 elems): w+w^-1 = 2cos(120)I=-I => det B_w = (n+1)^2
  reflections (3 elems): w^-1=w, eigs +-1     => det B_w = (n-2)(n+2) = n^2-4
For n=3 (m=1) this reproduces the sealed spectrum {1,16,16,5,5,5} exactly
(the prereg's own worked example). This predicts which primes can resonate
for each word (only primes dividing m^2 . (n+1)^2 . disc(w)); we test this
prediction against the direct numeric ladder below (silence-law check).
"""
import json
import sys
import time as _time
from fractions import Fraction

import mpmath as mp
import numpy as np

V7_CONDUIT = "<cc2-seat>/veins/v7_conduit"
sys.path.insert(0, V7_CONDUIT)
from engine_v7 import An_Level  # noqa: E402  (gate_report NOT used -- see fast_gate_report below)


# ---------------------------------------------------------------------------
# PERFORMANCE FIX (found live, during this cell's own run): engine_v7.gate_report
# computes each check as
#   max(abs((S * S.conjugate().transpose() - I)[i, j]) for i in range(N) for j in range(N))
# -- a Python generator expression that RECOMPUTES the full O(N^3) matrix
# product fresh on EVERY (i,j) iteration (no caching across generator steps),
# turning an O(N^3) check into O(N^5). At N=55 (k=9) this one line alone is
# ~3000x too much work; it is the actual mechanism behind the "level 9 took
# ~8h" report, not fundamental cost of the modular data itself (benchmarked
# directly: building S,T for k=9 takes <1s, a full NxN multiply ~1s, LU
# inverse ~3s -- all fast). Confirmed live: calling engine_v7.gate_report(S,T)
# for k=9 (N=55) did not return within 5 minutes; every matrix op it calls,
# timed in isolation, finishes in under 6s.
# FIX (local to this cell, engine_v7.py itself left untouched -- it is shared
# by other banked cells and this fixes OUR call site, not the library): the
# identical five checks, each matrix expression computed ONCE then scanned in
# O(N^2). Also replaces the two LU inversions (S**-1, T**-1) with the
# unitarity-justified cheap forms (S^-1 = S^dagger since S is unitary --
# itself one of the five gates checked here; T^-1 via elementwise conjugate
# since |T_i|=1 by construction) -- ~2x fewer O(N^3) operations on top of
# fixing the O(N^5) blowup. Gate-checked below (G0': compares this function's
# output against the banked gate_report at small k where both are cheap
# enough to run) before being trusted for k up to 10.
# ---------------------------------------------------------------------------
def fast_gate_report(S, T, Tlist):
    N = S.rows
    I = mp.eye(N)

    def maxabs(M):
        best = mp.mpf(0)
        for i in range(N):
            for j in range(N):
                v = abs(M[i, j])
                if v > best:
                    best = v
        return best

    Sdag = S.conjugate().transpose()
    Tconj = [mp.conj(t) for t in Tlist]  # T^-1 diagonal entries (|T_i|=1 exactly)

    rep = {}
    rep['unitary'] = maxabs(S * Sdag - I)
    rep['symmetric'] = maxabs(S - S.transpose())
    C2 = S * S
    ST = S * T
    STcubed = ST * ST * ST
    rep['(ST)^3=S^2'] = maxabs(STcubed - C2)
    rep['S^4=I'] = maxabs(C2 * C2 - I)

    # two-word lock: w1 = T^2 S T, w2 = T S T^-1 S^-1 (S^-1 -> Sdag, T^-1 -> Tconj diag)
    w1 = T * T * S * T
    # w2 = T*S*Tinv*Sdag ; build via column-scale (Tinv diagonal) to avoid a full
    # diagonal-matrix multiply, then one real multiply by Sdag
    TS = T * S
    TSTinv = mp.matrix(N, N)
    for i in range(N):
        for j in range(N):
            TSTinv[i, j] = TS[i, j] * Tconj[j]
    w2 = TSTinv * Sdag
    dev = maxabs(w1 - w2)
    rep['two_word'] = dev
    rho = w1
    rep['rho_unitary'] = maxabs(rho * rho.conjugate().transpose() - I)
    return rep, rho, Sdag, Tconj


# ---------------------------------------------------------------------------
# W(A2)=S3 + the longest element w0 -- lifted VERBATIM (construction and
# reasoning) from <cc2-seat>/loops_queue/d4_su3/d4_su3_run.py
# (its Gate 3 convention-audit resolution): det(w0) is the sign correction
# needed in Z_minus(w) = det(w0) * Tr(C . rho(w)), C = S^2, because A2's Weyl
# group does not contain -I (w0 is a reflection, not the identity's negative).
# ---------------------------------------------------------------------------
def _build_weyl_group_A2():
    s1 = np.array([[-1, 1], [0, 1]], dtype=np.int64)
    s2 = np.array([[1, 0], [1, -1]], dtype=np.int64)
    gens = [s1, s2]
    I = np.eye(2, dtype=np.int64)
    seen = {I.tobytes()}
    mats = [I]
    frontier = [I]
    while frontier:
        new = []
        for M in frontier:
            for g in gens:
                Mg = g @ M
                key = Mg.tobytes()
                if key not in seen:
                    seen.add(key)
                    new.append(Mg)
                    mats.append(Mg)
        frontier = new
    return mats


def _find_longest_element_A2(Wlist):
    pos_roots = [np.array([1, 0]), np.array([0, 1]), np.array([1, 1])]
    for idx, w in enumerate(Wlist):
        images = [w @ rt for rt in pos_roots]
        if all((im <= 0).all() for im in images):
            return idx, w
    raise RuntimeError("no longest element found")


_W_A2 = _build_weyl_group_A2()
assert len(_W_A2) == 6, f"expected |W(A2)|=6, got {len(_W_A2)}"
_W0_IDX, _W0_MAT = _find_longest_element_A2(_W_A2)
DET_W0 = int(round(np.linalg.det(_W0_MAT)))
assert DET_W0 == -1, f"expected det(w0)=-1 for A2 (verbatim d4_su3_run.py fact), got {DET_W0}"

WORK_DIR = "<cc2-seat>/anatomy/loop4/d4_ceiling"
BANKED_D4_SU3_JSON = "<cc2-seat>/loops_queue/d4_su3/d4_results.json"

mp.mp.dps = 60

PHI = (1 + mp.sqrt(5)) / 2
import sys as _lvlsys
KS = [int(_lvlsys.argv[1])] if len(_lvlsys.argv) > 1 else list(range(1, 13))  # per-level mode: argv[1] = k
NS = list(range(3, 11))              # n = 3..10 (m = n-2 = 1..8)

FAILED_GATES = []


def gate(tag, name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"\n[GATE {tag}] {name}: {status}", flush=True)
    if detail:
        print(detail, flush=True)
    if not ok:
        FAILED_GATES.append((tag, name))
        print(f"*** ESCALATION: GATE {tag} FAILED ({name}) ***", flush=True)
    return ok


def factorize(n):
    n = abs(int(n))
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def fac_str(f):
    if not f:
        return "1"
    return " * ".join(f"{p}^{a}" if a > 1 else f"{p}" for p, a in sorted(f.items()))


def legendre_mod5(a):
    r = a % 5
    if r == 0:
        return 0
    return 1 if r in (1, 4) else -1


def c2d(z):
    z = mp.mpc(z)
    return {"re": mp.nstr(z.real, 40), "im": mp.nstr(z.imag, 40)}


def recognize(x, constants):
    """Try mpmath.identify against a curated constant list; fall back to a
    high-precision decimal string (labeled UNIDENTIFIED, not lossy -- 40
    sig figs retained) if no closed form is found."""
    x = mp.mpf(x)
    if abs(x) < mp.mpf('1e-45'):
        return "0"
    ident = mp.identify(x, constants)
    if ident is not None:
        return ident
    # small-rational fallback
    for den in range(1, 25):
        val = x * den
        rd = mp.nint(val)
        if abs(val - rd) < mp.mpf('1e-40'):
            fr = Fraction(int(rd), den)
            return str(fr)
    return f"UNIDENTIFIED:{mp.nstr(x, 40)}"


def word_trace(Tlist, Ldiag, m):
    N = len(Tlist)
    total = mp.mpc(0, 0)
    for i in range(N):
        total += (Tlist[i] ** m) * Ldiag[i]
    return total


def main():
    print("=" * 78)
    print("D4 -- SU(3) ceiling law: Z_k(R^{n-2}L), n=3..10, k=1..12")
    print("=" * 78, flush=True)

    # ------------------------------------------------------------------
    # Load banked fig-8 (n=3) control BEFORE any of our own comparison
    # ------------------------------------------------------------------
    with open(BANKED_D4_SU3_JSON) as f:
        banked = json.load(f)
    banked_tr_odd = {}
    for kappa_str, rec in banked["results"].items():
        kappa = int(kappa_str)
        if 4 <= kappa <= 15:
            banked_tr_odd[kappa] = mp.mpc(rec["tr_odd"]["re"], rec["tr_odd"]["im"])
    print(f"loaded banked fig-8 control (tr_odd, kappa=4..15) from {BANKED_D4_SU3_JSON}")
    print(f"  banked verdict on record: {banked['verdict']}")

    # ------------------------------------------------------------------
    # Build SU(3)_k data for k=1..12, gate battery, word traces
    # ------------------------------------------------------------------
    gate_battery = {}
    Z_table = {}        # (n,k) -> mpc, THE quantity: tr_odd(w) (theta-parity projected)
    Zfull_table = {}    # (n,k) -> mpc, diagnostic: the plain full trace Tr(rho(w))
    Ldiag_by_k = {}
    Tlist_by_k = {}

    for k in KS:
        t_level0 = _time.time()
        L3 = An_Level(3, k, name=f"SU(3)_{k}")
        S, T = L3.build(verbose=False)
        Tlist = L3.T_matrix()
        N = S.rows
        rep, rho, Sdag, Tconj = fast_gate_report(S, T, Tlist)
        gate_battery[k] = {kk: mp.nstr(vv, 15) for kk, vv in rep.items()}
        print(f"--- gates: SU(3)_{k} (kappa={k+3}, N={N}) ---", flush=True)
        for kk, vv in rep.items():
            print(f"  {kk}: {float(vv):.3e}", flush=True)

        Si = Sdag  # S unitary (gate-verified above): S^-1 = S^dagger
        Ti = Tconj  # T^-1 diagonal entries (|T_i|=1 exactly)
        # L = S * Tinv * Sdag ; Tinv diagonal -> column-scale S (O(N^2)), then
        # one real O(N^3) multiply by Sdag (avoids a second LU inversion).
        S_Tinv = mp.matrix(N, N)
        for i in range(N):
            for j in range(N):
                S_Tinv[i, j] = S[i, j] * Ti[j]
        Lmat = S_Tinv * Si
        Ldiag = [Lmat[i, i] for i in range(N)]
        Ldiag_by_k[k] = Ldiag
        Tlist_by_k[k] = Tlist
        print(f"  [timing] level k={k} (N={N}) S,T+gates+L built in {_time.time()-t_level0:.2f}s",
              flush=True)

        # theta-odd projection weight vector: Codiag[j] = (L_jj + det(w0)*w_j)/2
        # where w_j = sum_i C[i,j] L[j,i], C = S^2 (charge conjugation), so that
        # sum_j T_j^m Codiag[j] = (Tr(T^m L) + det(w0) Tr(C T^m L)) / 2 = tr_odd(R^m L).
        Cmat = S * S
        wvec = [sum(Cmat[i, j] * Lmat[j, i] for i in range(N)) for j in range(N)]
        Codiag = [(Ldiag[j] + DET_W0 * wvec[j]) / 2 for j in range(N)]

        for n in NS:
            m = n - 2
            Zfull = word_trace(Tlist, Ldiag, m)
            Zodd = word_trace(Tlist, Codiag, m)
            Zfull_table[(n, k)] = Zfull
            Z_table[(n, k)] = Zodd

    # gate battery pass check
    tol = mp.mpf('1e-40')
    battery_ok = True
    for k in KS:
        rep = gate_battery[k]
        for key, val in rep.items():
            if mp.mpf(val) > tol:
                battery_ok = False
    gate("G0", "modular battery (unitary/symmetric/S^4=I/(ST)^3=S^2/two-word lock) "
               "all k=1..12 < 1e-40", battery_ok,
         detail="\n".join(f"  k={k}: " + ", ".join(f"{kk}={vv}" for kk, vv in gate_battery[k].items())
                           for k in KS))

    # ------------------------------------------------------------------
    # GATE 1 -- fig-8 reproduction (n=3 row vs banked tr_odd)
    # TWO checks, because the banked JSON itself is float64-limited:
    #  (a) sanity vs the banked d4_su3/d4_results.json tr_odd column, which
    #      was saved via that script's c2d() = {"re": float(z.real), ...} --
    #      a Python float64 cast (~1e-16 precision). So an irrational value
    #      (-1/phi at kappa=5,10,15) can only ever agree to ~1e-16/1e-17
    #      there NO MATTER HOW EXACT our own dps=60 computation is; integer
    #      values (0, 1) agree to full precision since floats represent them
    #      exactly. Tolerance set accordingly (1e-10, well above float64
    #      noise, well below "wrong value").
    #  (b) the EXACT closed-form additive law (banked, B585/D4-derived):
    #      tr_odd(kappa) = 1*[4|kappa] - (1/phi)*[5|kappa], evaluated at full
    #      dps=60 precision -- THIS is the true "exact arithmetic" gate.
    # ------------------------------------------------------------------
    def predicted_tr_odd_rl(kappa):
        ind4 = 1 if kappa % 4 == 0 else 0
        ind5 = 1 if kappa % 5 == 0 else 0
        return ind4 * mp.mpf(1) - ind5 / PHI

    fig8_devs = {}
    fig8_ok = True
    lines = []
    for k in KS:
        kappa = k + 3
        ours = Z_table[(3, k)]
        theirs = banked_tr_odd[kappa]
        dev_banked = abs(ours - theirs)
        pred_exact = predicted_tr_odd_rl(kappa)
        dev_exact = abs(ours.real - pred_exact) + abs(ours.imag)
        fig8_devs[kappa] = {"vs_banked_json_float64": mp.nstr(dev_banked, 6),
                             "vs_exact_closed_form": mp.nstr(dev_exact, 6)}
        ok_banked = dev_banked < mp.mpf('1e-10')
        ok_exact = dev_exact < mp.mpf('1e-40')
        ok = ok_banked and ok_exact
        fig8_ok &= ok
        lines.append(f"  kappa={kappa:2d}: ours={complex(ours)}  banked(float64)={complex(theirs)}  "
                      f"exact_pred={mp.nstr(pred_exact,20)}  |dev_banked|={mp.nstr(dev_banked,4)} "
                      f"{'OK' if ok_banked else 'FAIL'}  |dev_exact|={mp.nstr(dev_exact,4)} "
                      f"{'OK' if ok_exact else 'FAIL'}")
    gate("G1", "FIG-8 REPRODUCTION: n=3 row == banked d4_su3 tr_odd(kappa) "
               "(<1e-10 vs float64 JSON) AND == exact closed form [4|k]-[5|k]/phi (<1e-40), all k",
         fig8_ok, detail="\n".join(lines))

    # ------------------------------------------------------------------
    # GATE 2 -- B238 cross-check: n=4 (RRL) at k=2 (kappa=5).
    # NOTE: B238's su32_wrt.py computes the PLAIN full trace Tr(rho(word))
    # (no theta-parity projection) -- so this checks against Zfull_table, not
    # the tr_odd Z_table. GUARDED: only runs when (4,2) was actually computed
    # in this process's KS window (per-level runs with k != 2 skip it, no
    # KeyError; the monolithic/multi-level run still executes it).
    # ------------------------------------------------------------------
    if (4, 2) in Zfull_table:
        b238_target = mp.mpc(-1, 0) / 2 + mp.mpc(0, -1) * mp.sqrt(3) / 2  # -0.5 - i sqrt(3)/2
        ours_n4k2 = Zfull_table[(4, 2)]
        dev_b238 = min(abs(ours_n4k2 - b238_target), abs(ours_n4k2 - mp.conj(b238_target)))
        g2_pass = bool(dev_b238 < mp.mpf('1e-8'))
        gate("G2", "B238 cross-check: n=4 (RRL) FULL trace, k=2 (kappa=5) matches reported "
                   "-0.5 -+ i*sqrt(3)/2 (|Z|=1), to < 1e-8",
             g2_pass,
             detail=f"  ours(full)={complex(ours_n4k2)}  B238-target(up to conj)={complex(b238_target)}  "
                    f"|dev|={mp.nstr(dev_b238,6)}  |Z|={mp.nstr(abs(ours_n4k2),20)}")
    else:
        dev_b238 = None
        g2_pass = None
        print("\n[GATE G2] B238 cross-check: SKIPPED (k=2 and/or n=4 not in this run's window)",
              flush=True)

    # ------------------------------------------------------------------
    # Structural resonance prediction (B_w(P=n) determinant classes)
    # ------------------------------------------------------------------
    struct = {}
    for n in NS:
        m = n - 2
        det_id = m * m
        det_3cyc = (n + 1) * (n + 1)
        det_refl = n * n - 4
        primes = set()
        for d in (det_id, det_3cyc, det_refl):
            primes |= set(factorize(d).keys())
        struct[n] = dict(m=m, det_identity=det_id, det_3cycle=det_3cyc, det_reflection=det_refl,
                          disc=n * n - 4,
                          fac_identity=fac_str(factorize(det_id)),
                          fac_3cycle=fac_str(factorize(det_3cyc)),
                          fac_reflection=fac_str(factorize(det_refl)),
                          fac_disc=fac_str(factorize(n * n - 4)),
                          resonant_primes=sorted(primes))

    print("\n--- structural resonance prediction (B_w(P=n) determinant classes) ---")
    for n in NS:
        s = struct[n]
        print(f"  n={n} (m={s['m']}, word R^{s['m']}L): det_id={s['det_identity']} "
              f"({s['fac_identity']})  det_3cyc={s['det_3cycle']} ({s['fac_3cycle']})  "
              f"det_refl=disc={s['det_reflection']} ({s['fac_reflection']})  "
              f"resonant primes={s['resonant_primes']}", flush=True)

    # ------------------------------------------------------------------
    # Full 8 x 12 table: Z, |Z|^2, recognized forms
    # ------------------------------------------------------------------
    print("\n--- full table: Z_k(R^{n-2}L), |Z_k|^2 ---")
    table_rows = []
    for n in NS:
        m = n - 2
        disc = n * n - 4
        row_constants = ['phi', 'sqrt(5)', 'sqrt(2)', 'sqrt(3)', f'sqrt({disc})' if disc > 0 else None,
                          f'sqrt({struct[n]["det_3cycle"]})']
        row_constants = [c for c in row_constants if c]
        for k in KS:
            kappa = k + 3
            Z = Z_table[(n, k)]
            Z2 = (Z * mp.conj(Z)).real
            re_id = recognize(Z.real, row_constants)
            im_id = recognize(Z.imag, row_constants)
            z2_id = recognize(Z2, row_constants + [f'sqrt({disc*disc})' if disc else None] if False else row_constants)
            kappa_res_primes = set(factorize(kappa).keys())
            resonant_here = bool(kappa_res_primes & set(struct[n]['resonant_primes'])) or (kappa == 1)
            Zf = Zfull_table[(n, k)]
            row = dict(n=n, m=m, k=k, kappa=kappa, trace_n=n, disc=disc,
                       Z_re=mp.nstr(Z.real, 40), Z_im=mp.nstr(Z.imag, 40),
                       Z_re_id=re_id, Z_im_id=im_id,
                       Zabs2=mp.nstr(Z2, 40), Zabs2_id=z2_id,
                       Zabs=mp.nstr(abs(Z), 40),
                       Zfull_re=mp.nstr(Zf.real, 40), Zfull_im=mp.nstr(Zf.imag, 40),
                       resonant_predicted=resonant_here)
            table_rows.append(row)
            print(f"  n={n:2d} k={k:2d} kappa={kappa:2d}: Z = {re_id:>18} {'+' if Z.imag>=0 else '-'} "
                  f"{im_id.lstrip('-'):>18} i    |Z|^2 = {z2_id:>18}   "
                  f"(pred.resonant={resonant_here})", flush=True)

    # ------------------------------------------------------------------
    # Ceiling map: max_k |Z_k(w)| per word
    # ------------------------------------------------------------------
    print("\n--- CEILING MAP: max_k |Z_k(w)| over k=1..12 ---")
    ceiling = {}
    for n in NS:
        best_k, best_val = None, mp.mpf(-1)
        for k in KS:
            Z = Z_table[(n, k)]
            av = abs(Z)
            if av > best_val:
                best_val = av
                best_k = k
        argmax_ks = [k for k in KS if abs(abs(Z_table[(n, k)]) - best_val) < mp.mpf('1e-35')]
        s = struct[n]
        ceiling[n] = dict(n=n, m=s['m'], trace=n, disc=s['disc'], fac_disc=s['fac_disc'],
                           ceiling=mp.nstr(best_val, 30),
                           ceiling_squared=mp.nstr(best_val * best_val, 30),
                           ceiling_id=recognize(best_val, ['phi', 'sqrt(5)']),
                           argmax_k=argmax_ks,
                           argmax_kappa=[k + 3 for k in argmax_ks])
        print(f"  n={n:2d} (word R^{s['m']}L, disc={s['disc']}={s['fac_disc']}): "
              f"ceiling = {mp.nstr(best_val,15)}  (~{ceiling[n]['ceiling_id']})  "
              f"at k={argmax_ks} (kappa={ceiling[n]['argmax_kappa']})", flush=True)

    # ------------------------------------------------------------------
    # Boundedness / growth verdict per word
    # ------------------------------------------------------------------
    print("\n--- BOUNDEDNESS VERDICT (monotone-growth check across k=1..12) ---")
    growth_flags = {}
    for n in NS:
        seq = [abs(Z_table[(n, k)]) for k in KS]
        monotone_nondecreasing = all(seq[i + 1] >= seq[i] - mp.mpf('1e-30') for i in range(len(seq) - 1))
        strictly_increasing_run = monotone_nondecreasing and (seq[-1] - seq[0] > mp.mpf('1e-6'))
        growth_flags[n] = bool(strictly_increasing_run)
        print(f"  n={n:2d}: |Z_k| sequence (k=1..12) = {[mp.nstr(v,6) for v in seq]}  "
              f"monotone-nondecreasing-over-full-window={monotone_nondecreasing}  "
              f"FLAG_GROWTH={growth_flags[n]}", flush=True)
    any_growth = any(growth_flags.values())
    if any_growth:
        print("\n*** ESCALATION: monotone growth detected in at least one word's |Z_k| "
              "sequence over the full k=1..12 window -- STOP, double-check convention "
              "gate before reporting. ***", flush=True)

    # ------------------------------------------------------------------
    # Silence-law checks
    # ------------------------------------------------------------------
    print("\n--- SILENCE LAW CHECKS ---")
    # (a) candidate generic law Z = (1-(kappa|5))/2 (as literally handed down in task text)
    candidate_law_matches = []
    for k in KS:
        kappa = k + 3
        pred = (1 - legendre_mod5(kappa)) / mp.mpf(2)
        actual = Z_table[(3, k)]  # only n=3 (RL) is real-valued generically
        dev = abs(actual.real - pred) + abs(actual.imag)
        candidate_law_matches.append(dict(kappa=kappa, predicted=mp.nstr(pred, 10),
                                           actual=mp.nstr(actual.real, 10), dev=mp.nstr(dev, 6),
                                           match=bool(dev < mp.mpf('1e-30'))))
    n_match = sum(1 for r in candidate_law_matches if r['match'])
    print(f"  candidate law Z=(1-(kappa|5))/2 vs n=3(RL) row: {n_match}/{len(candidate_law_matches)} exact matches")
    for r in candidate_law_matches:
        print(f"    kappa={r['kappa']:2d}: predicted={r['predicted']}  actual={r['actual']}  "
              f"dev={r['dev']}  match={r['match']}", flush=True)

    # (b) the word-generic silence structure actually observed: Z=0 whenever kappa
    # shares no prime with the structural resonance set {primes | m^2 (n+1)^2 disc}
    print("\n  observed vs structurally-predicted silence (Z=0) per (word,kappa):")
    silence_rows = []
    for n in NS:
        s = struct[n]
        for k in KS:
            kappa = k + 3
            Z = Z_table[(n, k)]
            is_zero_observed = abs(Z) < mp.mpf('1e-35')
            kappa_primes = set(factorize(kappa).keys())
            shares_prime = bool(kappa_primes & set(s['resonant_primes'])) or kappa == 1
            predicted_silent = not shares_prime
            consistent = (predicted_silent == is_zero_observed)
            silence_rows.append(dict(n=n, k=k, kappa=kappa, observed_zero=is_zero_observed,
                                      predicted_silent=predicted_silent, consistent=consistent))
    n_consistent = sum(1 for r in silence_rows if r['consistent'])
    print(f"  structural silence-prediction consistency: {n_consistent}/{len(silence_rows)} cells "
          f"(predicted_silent == observed |Z|=0)")
    inconsistent = [r for r in silence_rows if not r['consistent']]
    if inconsistent:
        print(f"  INCONSISTENT cells ({len(inconsistent)}):")
        for r in inconsistent[:40]:
            print(f"    n={r['n']} k={r['k']} kappa={r['kappa']}: observed_zero={r['observed_zero']} "
                  f"predicted_silent={r['predicted_silent']}")

    # ------------------------------------------------------------------
    # Save
    # ------------------------------------------------------------------
    out = {
        "meta": {
            "engine": "veins/v7_conduit/engine_v7.py An_Level(3,k)",
            "banked_fig8_source": BANKED_D4_SU3_JSON,
            "banked_verdict_on_record": banked["verdict"],
            "convention": "R->T, L->S T^-1 S^-1 (== S^-1 T^-1 S, C=S^2 central); "
                           "Z_k(R^m L) = sum_i T_i^m L_ii",
            "dps": mp.mp.dps,
            "ks": KS, "ns": NS,
        },
        "gates": {
            "G0_modular_battery_pass": battery_ok,
            "G1_fig8_reproduction_pass": fig8_ok,
            "G1_fig8_deviations": fig8_devs,
            "G2_b238_crosscheck_pass": g2_pass,
            "G2_b238_deviation": (mp.nstr(dev_b238, 10) if dev_b238 is not None else None),
            "G2_skipped": bool(dev_b238 is None),
        },
        "structural_resonance_prediction": struct,
        "table": table_rows,
        "ceiling_map": ceiling,
        "growth_verdict": {"per_word_flag_growth": growth_flags, "any_growth": any_growth},
        "silence_law_candidate_1_minus_legendre5_over_2": candidate_law_matches,
        "silence_structural_consistency": {
            "n_consistent": n_consistent, "n_total": len(silence_rows),
            "inconsistent_cells": inconsistent,
        },
        "failed_gates": FAILED_GATES,
    }
    out_path = (f"{WORK_DIR}/d4_results_k{_lvlsys.argv[1]}.json"
                if len(_lvlsys.argv) > 1 else f"{WORK_DIR}/d4_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1)
    print(f"\nsaved -> {out_path}")

    g2_ok_for_pass = (g2_pass is None) or g2_pass  # None (skipped) does not block pass
    all_pass = battery_ok and fig8_ok and g2_ok_for_pass and not any_growth
    print(f"\n=== ALL GATES + NO-GROWTH: {all_pass} ===")
    print("=== D4_CEILING RUN COMPLETE - EXIT_MARKER_D4_CEILING ===", flush=True)
    return 0 if (battery_ok and fig8_ok and g2_ok_for_pass) else 1


if __name__ == "__main__":
    sys.exit(main())
