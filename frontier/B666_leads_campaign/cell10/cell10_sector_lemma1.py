"""B666 CELL 10 — L97-RESCOPE: the remainder run.

The two genuine remainders of the ladder proof queue (per the sealed campaign
prereg, cell 10):

  (1) THE SECTOR DECOMPOSITION — the theta-even/odd sector split of the E6
      Z-ladder with the mirror channel (B656/G3, B651/P4 convention eps = +1):
        tr_odd(r)  = (Z_{+3}(r) - Z_{-3}(r)) / 2
        tr_even(r) = (Z_{+3}(r) + Z_{-3}(r)) / 2
      State and verify the exact decomposition identity on 20 rungs (r = 13..32),
      including the exact class-level sector split (Q3-L2, both channels) and the
      sector-carry clause, against the banked P4 sector ladder (13 rows).

  (2) THE LEMMA-1 DEPENDENCY — B651/F1's proof consumes Wall's even-type LOCAL
      MAGNITUDE lemma, not Lemma 1; Lemma 1 (the Milgram/Wall multiplier twist,
      G(rq) = (r|p)^m G(q), m = # odd-exponent p-elementary divisors) is consumed
      by the generic-rung theorem (Q3-L2), A2's voice closed form, and the sector
      decomposition. Here its instances are verified EXHAUSTIVELY for the object:
      for every one of the 25+25 classes (both channels), for EVERY unit
      multiplier residue mod the class period, the exact cyclotomic identity
        G_w(r) = (r|5)^{m_w(5)} * G_w(1)
      is decided by integer-polynomial reduction mod Phi_m (zero floats).
      Since G_w(r) depends only on r mod P_class (all phase orders divide
      P_class), passing every unit residue PROVES the twist law for ALL generic
      multipliers — the object-level Lemma-1 dependency is thereby discharged
      (the abstract lemma stays cited-standard for the general statement).

GATES (two-outcome; all must pass for "queue closed clean"):
  G0   both channels build 25 classes; the direct (size, sign, |det|) table ==
       banked jeffrey_terms.json; the mirror det multiset == banked P4 list.
  G1   Lemma-1 instances: exhaustive per-class twist law, 0 failures, both
       channels; odd-exponent primes across all SNF divisors = {5} only;
       m_w(5) odd <=> squarefree part s_w = 5; 10 chi5 classes per channel.
  G2   gamma_w(1) in {+1, -1} identified EXACTLY (cyclotomic reduction) for all
       50 classes; direct-channel gamma_w(13) = gamma_w(1)*(13|5)^{m_w(5)}
       matches banked p1_certificates.json 25/25.
  G3   exact sector sums (pure Fraction arithmetic from exact gammas):
       direct (S_triv, S_chi5) = (+1/2, -1/2); mirror = (-1/2, +1/2)
       => the exact generic laws Z_+ = (1-(r|5))/2, Z_- = ((r|5)-1)/2 and
       tr_even == 0 on every doubly-generic rung (a THEOREM, exact).
  G4   the decomposition on the ladder: r = 13..25 reproduces the banked P4
       sector ladder 13/13 (values quantized in (1/2)Z[sqrt5] at 1e-30, dps 50 —
       the banked cell-G decision pattern); direct totals Z(13)=1, Z(16)=0,
       Z(19)=2 reproduced; numeric cross-gate vs banked p4_results < 1e-6.
  G5   sector-carry: tr_even(r) != 0 => r NOT doubly generic, on all 20 rungs;
       the mirror-spectrum-coprime witnesses (the r = 19 sharpening) recorded.

Provenance of replicated machinery (verbatim, banked):
  weyl_group()/C6 — frontier/B600_level_ladder engine via
  frontier/B662_successor_campaign/cellG/l100_period.py (banked);
  q_multiset()/hnf_column() — same cell G source;
  bucket construction — the B646 n1 pipeline convention (P_WORD rebuilt at -3
  for the mirror, the B651/P4 + B656/G3 convention).
House pattern: exact Fractions/integers in every decisive step; mpmath dps 50 +
1e-30 quantization only at value-gate evaluation.
"""
import hashlib
import itertools
import json
import math
import os
_REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
import sys
import time
from collections import Counter
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

CELL = _REPO + '/frontier/B666_leads_campaign/cell10'
BANKED_TERMS = (_REPO + '/frontier/B646_wave2_integration/cc2_packets/'
                'next_queue/next_queue/n1_counting/jeffrey_terms.json')
BANKED_P1 = (_REPO + '/frontier/B651_wave3_integration/cc2_packets/'
             'promotion_queue/promotion_queue/p1_milgram/p1_certificates.json')
BANKED_P4 = (_REPO + '/frontier/B651_wave3_integration/cc2_packets/'
             'promotion_queue/promotion_queue/p4_sectors/p4_results.json')

C6 = np.array([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
               [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]],
              dtype=np.int64)
WN = 51840
RUNGS = list(range(13, 33))                      # 20 rungs
DIRECT_SPECTRUM = 2 * 3 * 5 * 7 * 11 * 19        # primes of the +3 channel dets
MIRROR_SPECTRUM = 2 * 3 * 5 * 7 * 17             # primes of the -3 channel dets
GATES = {}

_x = sp.Symbol('x')
_fh = open(f'{CELL}/cell10_output.txt', 'w')


def log(msg=""):
    print(msg, flush=True)
    _fh.write(msg + "\n")
    _fh.flush()


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


# ---------------------------------------------------------------- banked machinery
def weyl_group():
    """Verbatim from the banked engine (B600 packet / cell G)."""
    gens = []
    for j in range(6):
        M = np.eye(6, dtype=np.int64)
        M[j, :] -= C6[:, j]
        gens.append(M)
    I = np.eye(6, dtype=np.int64)
    seen = {I.tobytes()}
    mats, signs = [I], [1]
    frontier = [(I, 1)]
    while frontier:
        new = []
        for M, s in frontier:
            for g in gens:
                Mg = g @ M
                key = Mg.tobytes()
                if key not in seen:
                    seen.add(key)
                    new.append((Mg, -s))
                    mats.append(Mg)
                    signs.append(-s)
        frontier = new
    return np.array(mats), np.array(signs, dtype=np.int64)


def hnf_column(B):
    M = sp.Matrix(B.tolist())
    H = hermite_normal_form(M)
    return np.array(H.tolist(), dtype=np.int64)


def q_multiset(B):
    """EXACT multiset {q(mu) mod 2} as Counter{Fraction: int} (cell G, verbatim)."""
    Bs = sp.Matrix(B.tolist())
    det = int(Bs.det())
    ad = abs(det)
    M = sp.Matrix(C6.tolist()) * Bs.inv()
    H = hnf_column(B)
    diag = [int(H[i, i]) for i in range(6)]
    assert np.prod(diag) == ad, (diag, ad)
    Mf = [[Fraction(M[i, j].p, M[i, j].q) for j in range(6)] for i in range(6)]
    D = 1
    for row in Mf:
        for v in row:
            D = D * v.denominator // math.gcd(D, v.denominator)
    Mi = [[int(v * D) for v in row] for row in Mf]
    twoD = 2 * D
    cnt = Counter()
    for xt in itertools.product(*[range(d) for d in diag]):
        n = 0
        for i in range(6):
            xi = xt[i]
            if xi:
                Mrow = Mi[i]
                for j in range(6):
                    if xt[j]:
                        n += xi * Mrow[j] * xt[j]
        cnt[Fraction(n % twoD, D)] += 1
    return cnt, ad


def sqfree_split(n):
    s, f = 1, 1
    for p, e in sp.factorint(n).items():
        f *= p ** (e // 2)
        if e % 2:
            s *= p
    return s, f


def ord_of_q(q):
    a, b = q.numerator, q.denominator
    if a == 0:
        return 1
    return 2 * b if a % 2 else b


# ---------------------------------------------------------------- channel builder
def build_channel(W, eps, p_word):
    buckets = {}
    for idx in range(len(W)):
        w = W[idx]
        winv = np.rint(np.linalg.inv(w)).astype(np.int64)
        assert (w @ winv == np.eye(6, dtype=np.int64)).all()
        B = p_word * np.eye(6, dtype=np.int64) - w - winv
        cp = tuple(np.rint(np.poly(w.astype(float))).astype(np.int64))
        spec = tuple(sorted(np.linalg.eigvals(B.astype(float)).real.round(6)))
        buckets.setdefault((cp, spec), []).append((idx, B, int(eps[idx])))
    sorted_buckets = sorted(buckets.items(), key=lambda kv: -len(kv[1]))
    assert len(sorted_buckets) == 25, f"expected 25 classes, got {len(sorted_buckets)}"
    assert sum(len(m) for _, m in sorted_buckets) == WN
    classes = []
    for bi, (key, members) in enumerate(sorted_buckets):
        idx0, B0, s0 = members[0]
        assert all(s == s0 for _, _, s in members)
        mult, ad = q_multiset(B0)
        if len(members) > 1:                      # exact 2-representative class gate
            mult2, ad2 = q_multiset(members[1][1])
            assert mult == mult2 and ad == ad2, f"class function failure at bucket {bi}"
        snf = smith_normal_form(sp.Matrix(B0.tolist()))
        divisors = [abs(int(snf[i, i])) for i in range(6) if abs(int(snf[i, i])) != 1]
        s, f = sqfree_split(ad)
        per = 1
        for q in mult:
            o = ord_of_q(q)
            per = per * o // math.gcd(per, o)
        # odd-exponent elementary-divisor counts per prime (the Lemma-1 m_w(p))
        modd = {}
        for d in divisors:
            for p, e in sp.factorint(d).items():
                if e % 2:
                    modd[p] = modd.get(p, 0) + 1
        modd = {p: c for p, c in modd.items() if c % 2}   # keep odd-count primes
        classes.append(dict(bucket=bi, size=len(members), sign=s0, det=ad, s=s, f=f,
                            divisors=divisors, mult=mult, period=per, modd=modd))
    return classes


# ------------------------------------------------- exact cyclotomic instance engine
_cyclo_cache = {}


def cyclo(m):
    if m not in _cyclo_cache:
        _cyclo_cache[m] = sp.Poly(sp.cyclotomic_poly(m, _x), _x)
    return _cyclo_cache[m]


def phase_vec(cls, r, m):
    """Integer coefficient vector of G_w(r) in powers of zeta_m = e^{-2 pi i / m}."""
    vec = [0] * m
    for q, c in cls['mult'].items():
        t = Fraction(r) * q * m / 2
        assert t.denominator == 1, (r, q, m)
        vec[int(t) % m] += c
    return vec


def is_zero_cyclo(vec, m):
    """Exact: does the integer vector represent 0 in Q(zeta_m)?"""
    if all(v == 0 for v in vec):
        return True
    p = sp.Poly.from_list(list(reversed(vec)), _x)
    return p.rem(cyclo(m)).is_zero


def sqrt5_vec(m, f=1):
    """Integer vector of f*sqrt(5) in zeta_m (requires 5 | m):
    sqrt5 = sum_{a=1..4} (a|5) e^{2 pi i a / 5}; e^{2 pi i a/5} = zeta_m^{-a m/5}."""
    assert m % 5 == 0
    vec = [0] * m
    for a in range(1, 5):
        vec[(-a * (m // 5)) % m] += legendre(a, 5) * f
    return vec


def identify_gamma(cls):
    """EXACT gamma_w(1) in {+1,-1} with G_w(1) = gamma * f * sqrt(s); None if not."""
    m = cls['period']
    v1 = phase_vec(cls, 1, m)
    if cls['s'] == 1:
        tgt = [0] * m
        tgt[0] = cls['f']
    else:
        assert cls['s'] == 5, cls['s']
        mm = m if m % 5 == 0 else None
        assert mm, f"5-part missing from period of bucket {cls['bucket']}"
        tgt = sqrt5_vec(m, cls['f'])
    for g in (1, -1):
        diff = [a - g * b for a, b in zip(v1, tgt)]
        if is_zero_cyclo(diff, m):
            return g
    return None


def lemma1_exhaustive(cls):
    """Exhaustively verify G_w(r) = (r|5)^{m_w(5)} G_w(1) over ALL unit residues
    r mod P_class (unit: gcd(r, det) = 1; r odd if det even). Exact. Returns
    (n_instances, n_failures)."""
    m = cls['period']
    det = cls['det']
    m5 = cls['modd'].get(5, 0)
    v1 = phase_vec(cls, 1, m)
    n_inst = n_fail = 0
    for r in range(m):
        if math.gcd(r if r else det, det) != 1:
            continue
        if det % 2 == 0 and r % 2 == 0:
            continue
        chi = legendre(r, 5) if (m5 % 2 and det % 5 == 0) else 1
        # (r|5) defined for gcd(r,5)=1; unit condition guarantees it when 5 | det
        vr = phase_vec(cls, r, m)
        diff = [a - chi * b for a, b in zip(vr, v1)]
        n_inst += 1
        if not is_zero_cyclo(diff, m):
            n_fail += 1
    return n_inst, n_fail


# ---------------------------------------------------------------- value evaluation
def class_eval_mp(cls, r):
    tot = mp.mpc(0)
    for q, c in cls['mult'].items():
        e = (r * q) % 2
        tot += c * mp.e ** (-1j * mp.pi * mp.mpf(e.numerator) / e.denominator)
    return tot


def Z_mp(classes, r):
    tot = mp.mpc(0)
    for cls in classes:
        tot += cls['size'] * cls['sign'] * class_eval_mp(cls, r) / mp.sqrt(cls['det'])
    return tot / WN


def quantize_half_zsqrt5(z):
    """Exact identification of z as a/2 + (b/2) sqrt5 (a, b integers, |b|<=48),
    at 1e-30; rigorous: distinct candidates are separated by >> 1e-30."""
    tol = mp.mpf('1e-30')
    if abs(z.imag) > tol:
        return None
    s5 = mp.sqrt(5)
    for b in range(-48, 49):
        a = 2 * z.real - b * s5
        an = mp.nint(a)
        if abs(a - an) < tol:
            return (Fraction(int(an), 2), Fraction(b, 2))
    return None


def fmt_val(v):
    a, b = v
    if b == 0:
        return str(a) if a.denominator > 1 else str(a.numerator)
    return f"({a}) + ({b})*sqrt5"


def main():
    t0 = time.time()
    src = open(f'{CELL}/cell10_sector_lemma1.py', 'rb').read()
    log(f"=== B666 CELL 10 — L97 remainder: the sector decomposition + the Lemma-1 "
        f"dependency — {time.strftime('%Y-%m-%d %H:%M:%S')} ===")
    log(f"script sha256 = {hashlib.sha256(src).hexdigest()}")

    # ---------------- PHASE 0: the two channels
    log("\n=== PHASE 0 — build W(E6) and BOTH channels (P_WORD = +3 and -3) ===")
    W, eps = weyl_group()
    log(f"|W| = {len(W)}")
    assert len(W) == WN
    chans = {}
    for pw in (3, -3):
        t1 = time.time()
        chans[pw] = build_channel(W, eps, pw)
        log(f"channel P_WORD = {pw:+d}: 25 classes, 2-rep class gates exact "
            f"({time.time()-t1:.1f}s)")

    banked = json.load(open(BANKED_TERMS))
    banked_keys = sorted((row['size'], row['sign'], row['absdetB']) for row in banked['rows'])
    mine_keys = sorted((c['size'], c['sign'], c['det']) for c in chans[3])
    GATES['G0_direct_table'] = (mine_keys == banked_keys)
    p4 = json.load(open(BANKED_P4))
    GATES['G0_mirror_dets'] = (sorted(c['det'] for c in chans[-3])
                               == p4['det_multiset_Pminus3_sorted'])
    log(f"GATE G0 direct table == banked jeffrey_terms: {GATES['G0_direct_table']}")
    log(f"GATE G0 mirror det multiset == banked P4:     {GATES['G0_mirror_dets']}")

    for pw in (3, -3):
        log(f"\n-- channel {pw:+d} class table --")
        for c in chans[pw]:
            log(f"   class {c['bucket']:>2}: size {c['size']:>5} sign {c['sign']:+d} "
                f"|det| {c['det']:>6} = {c['s']}*{c['f']}^2  eldiv {c['divisors']!s:<20} "
                f"P_class {c['period']:>3}  m_odd {c['modd']}")

    # ---------------- PHASE 1: Lemma-1 bookkeeping + exhaustive instance proof
    log("\n=== PHASE 1 — THE LEMMA-1 INSTANCES (exact, exhaustive per class) ===")
    all_odd_primes = set()
    sq_iff_m5 = True
    chi5_counts = {}
    inst_tot = fail_tot = 0
    for pw in (3, -3):
        n5 = 0
        for c in chans[pw]:
            all_odd_primes |= set(c['modd'])
            m5odd = (c['modd'].get(5, 0) % 2 == 1)
            sq_iff_m5 &= (m5odd == (c['s'] == 5))
            n5 += m5odd
            # structural sanity for exhaustiveness: primes(det) subset primes(period)*2
            pd = set(sp.factorint(c['det']))
            ppd = set(sp.factorint(c['period'])) | {2}
            assert pd <= ppd, (pw, c['bucket'], pd, ppd)
        chi5_counts[pw] = n5
        t1 = time.time()
        for c in chans[pw]:
            ni, nf = lemma1_exhaustive(c)
            inst_tot += ni
            fail_tot += nf
            if nf:
                log(f"   FAIL channel {pw:+d} class {c['bucket']}: {nf}/{ni}")
        log(f"channel {pw:+d}: exhaustive twist instances verified "
            f"({time.time()-t1:.1f}s)")
    GATES['G1_lemma1_instances'] = (fail_tot == 0)
    GATES['G1_odd_primes_only5'] = (all_odd_primes == {5})
    GATES['G1_sq_iff_m5'] = sq_iff_m5
    GATES['G1_chi5_counts'] = (chi5_counts == {3: 10, -3: 10})
    log(f"total instances {inst_tot}, failures {fail_tot}")
    log(f"GATE G1 instances (0 failures):            {GATES['G1_lemma1_instances']}")
    log(f"GATE G1 odd-exponent primes == {{5}}:        {GATES['G1_odd_primes_only5']} "
        f"({sorted(all_odd_primes)})")
    log(f"GATE G1 m_w(5) odd <=> s_w = 5:            {GATES['G1_sq_iff_m5']}")
    log(f"GATE G1 chi5-sector sizes (10 + 10):       {GATES['G1_chi5_counts']} "
        f"{chi5_counts}")

    # ---------------- PHASE 2: exact gammas + p1 cross-check
    log("\n=== PHASE 2 — EXACT gamma_w(1) (cyclotomic reduction) + banked cross-check ===")
    g2_ok = True
    for pw in (3, -3):
        for c in chans[pw]:
            g = identify_gamma(c)
            c['gamma1'] = g
            if g is None:
                g2_ok = False
                log(f"   channel {pw:+d} class {c['bucket']}: gamma NOT in {{+1,-1}}")
    GATES['G2_gamma_exact'] = g2_ok
    log(f"GATE G2 all 50 gammas in {{+1,-1}} exactly:  {GATES['G2_gamma_exact']}")
    p1 = json.load(open(BANKED_P1))
    p1_map = {(e['size'], e['sign'], e['absdet']): e['j_13'] for e in p1}
    match = 0
    for c in chans[3]:
        m5 = c['modd'].get(5, 0) % 2
        gamma13 = c['gamma1'] * (legendre(13, 5) if m5 else 1)
        want = 1 if p1_map[(c['size'], c['sign'], c['det'])] == 0 else -1
        match += (gamma13 == want)
    GATES['G2_p1_crosscheck'] = (match == 25)
    log(f"GATE G2 direct gamma(13) vs banked p1:     {GATES['G2_p1_crosscheck']} "
        f"({match}/25)")

    # ---------------- PHASE 3: exact sector sums => THE DECOMPOSITION THEOREM
    log("\n=== PHASE 3 — EXACT SECTOR SUMS and the decomposition theorem ===")
    sums = {}
    for pw in (3, -3):
        st = so = Fraction(0)
        for c in chans[pw]:
            contrib = Fraction(c['size'] * c['sign'] * c['gamma1'], WN)
            if c['modd'].get(5, 0) % 2:
                so += contrib
            else:
                st += contrib
        sums[pw] = (st, so)
        log(f"channel {pw:+d}: S_triv = {st}, S_chi5 = {so}   (exact Fractions)")
    GATES['G3_sector_sums'] = (sums[3] == (Fraction(1, 2), Fraction(-1, 2))
                               and sums[-3] == (Fraction(-1, 2), Fraction(1, 2)))
    log(f"GATE G3 (+1/2,-1/2) direct, (-1/2,+1/2) mirror: {GATES['G3_sector_sums']}")
    log("\nTHE SECTOR-DECOMPOSITION IDENTITY (now exact, object-level):")
    log("  Z_+(r) = tr_odd(r) + tr_even(r),  tr_odd = (Z_+ - Z_-)/2, "
        "tr_even = (Z_+ + Z_-)/2  [eps = +1]")
    log("  generic laws (PROVEN here by the exhaustive twist + exact gammas + sums):")
    log("    Z_+(r) = 1/2 - (r|5)/2   for gcd(r, 2*3*5*7*11*19) = 1")
    log("    Z_-(r) = -1/2 + (r|5)/2  for gcd(r, 2*3*5*7*17)   = 1")
    log("  => tr_even(r) = 0 and tr_odd(r) = (1-(r|5))/2 on every doubly-generic rung"
        " (EXACT).")

    # ---------------- PHASE 4: the 20-rung ladder + banked sector-ladder gate
    log("\n=== PHASE 4 — the decomposition on the ladder (r = 13..32, dps 50, "
        "quantized 1e-30) ===")
    mp.mp.dps = 50
    banked_ladder = {row['r']: tuple(row['rounded'])
                     for row in p4['ladder_k1_13'].values()}
    p4res = p4['results']
    rows = []
    lad_ok = xnum_ok = carry_ok = True
    totals_ok = True
    for r in RUNGS:
        zp = Z_mp(chans[3], r)
        zm = Z_mp(chans[-3], r)
        qp, qm = quantize_half_zsqrt5(zp), quantize_half_zsqrt5(zm)
        assert qp is not None and qm is not None, f"quantization failed at r={r}"
        tr_odd = ((qp[0] - qm[0]) / 2, (qp[1] - qm[1]) / 2)
        tr_even = ((qp[0] + qm[0]) / 2, (qp[1] + qm[1]) / 2)
        dg = math.gcd(r, 2 * 3 * 5 * 7 * 11 * 17 * 19) == 1
        mg = math.gcd(r, MIRROR_SPECTRUM) == 1
        even_zero = (tr_even == (Fraction(0), Fraction(0)))
        if r in banked_ladder:
            want = banked_ladder[r]
            ok = (tr_odd[1] == 0 and tr_even[1] == 0
                  and tr_odd[0] == want[0] and tr_even[0] == want[1])
            lad_ok &= ok
            bk = p4res[str(r)]
            xnum_ok &= (abs(complex(zp) - complex(bk['Zp'][0], bk['Zp'][1])) < 1e-6
                        and abs(complex(zm) - complex(bk['Zm'][0], bk['Zm'][1])) < 1e-6)
        else:
            ok = None
        if not even_zero:
            carry_ok &= (not dg)          # tr_even != 0 => not doubly generic
        if r == 13:
            totals_ok &= (qp == (Fraction(1), Fraction(0)))
        if r == 16:
            totals_ok &= (qp == (Fraction(0), Fraction(0)))
        if r == 19:
            totals_ok &= (qp == (Fraction(2), Fraction(0)))
        rows.append(dict(r=r, Zp=fmt_val(qp), Zm=fmt_val(qm),
                         tr_odd=fmt_val(tr_odd), tr_even=fmt_val(tr_even),
                         doubly_generic=dg, mirror_generic=mg,
                         banked_match=ok))
        log(f"  r={r:>2}: Z+ = {fmt_val(qp):>18}  Z- = {fmt_val(qm):>18}  "
            f"(odd, even) = ({fmt_val(tr_odd)}, {fmt_val(tr_even)})"
            f"{'  [banked ' + ('OK' if ok else 'MISMATCH') + ']' if ok is not None else '  [new row]'}"
            f"{'  DG' if dg else ''}{'  mirror-generic' if mg else ''}")
    GATES['G4_banked_ladder_13'] = lad_ok
    GATES['G4_numeric_crossgate'] = xnum_ok
    GATES['G4_direct_totals'] = totals_ok
    GATES['G5_sector_carry'] = carry_ok
    log(f"GATE G4 banked sector ladder 13/13:        {GATES['G4_banked_ladder_13']}")
    log(f"GATE G4 numeric cross-gate vs p4 (<1e-6):  {GATES['G4_numeric_crossgate']}")
    log(f"GATE G4 direct totals Z(13),Z(16),Z(19):   {GATES['G4_direct_totals']}")
    log(f"GATE G5 tr_even != 0 => not doubly generic: {GATES['G5_sector_carry']}")

    sharpen = [row['r'] for row in rows
               if row['tr_even'] != '0' and row['mirror_generic']]
    log(f"\nTHE SHARPENING (mirror-spectrum-coprime rungs that still carry the even "
        f"sector): {sharpen}")
    log("  => B656/G3's parenthetical 'even carries a unit iff kappa shares a prime "
        "with the mirror spectrum {2,3,5,7,17}' is NOT necessary: either channel's "
        "resonance can carry the even sector (r = 19: mirror-generic, direct "
        "Phi_9-saturated, tr_even = 1). The correct exact statement is the "
        "doubly-generic vanishing clause above.")

    # ---------------- verdict + persist
    verdict = all(GATES.values())
    log("\n=== GATE SUMMARY ===")
    for k, v in GATES.items():
        log(f"  {k}: {'PASS' if v else 'FAIL'}")
    out = dict(
        script_sha256=hashlib.sha256(src).hexdigest(),
        gates={k: bool(v) for k, v in GATES.items()},
        lemma1=dict(instances=inst_tot, failures=fail_tot,
                    odd_exponent_primes=sorted(all_odd_primes),
                    chi5_sector_sizes={str(k): v for k, v in chi5_counts.items()}),
        sector_sums={str(pw): [str(sums[pw][0]), str(sums[pw][1])] for pw in sums},
        ladder=rows,
        sharpening_witnesses=sharpen,
        classes={str(pw): [dict(bucket=cls['bucket'], size=cls['size'],
                                sign=cls['sign'], det=cls['det'], s=cls['s'],
                                f=cls['f'], divisors=cls['divisors'],
                                period=cls['period'], gamma1=cls['gamma1'],
                                modd={str(p): c for p, c in cls['modd'].items()},
                                mult={str(q): c for q, c in sorted(cls['mult'].items())})
                           for cls in chans[pw]] for pw in chans},
    )
    with open(f'{CELL}/cell10_results.json', 'w') as fj:
        json.dump(out, fj, indent=1, default=str)
    log(f"\nresults -> {CELL}/cell10_results.json")
    log(f"total wall time: {time.time()-t0:.1f}s")
    if verdict:
        log("\nVERDICT: THE QUEUE CLOSES CLEAN — the sector decomposition is stated "
            "and verified exactly (20 rungs, banked ladder 13/13, exact sector "
            "sums), and the Lemma-1 dependency is stated with its object-level "
            "instances exhaustively PROVEN (0 failures).")
    else:
        log("\nVERDICT: gates incomplete — the honest residue is the failed gate(s) "
            "above.")


if __name__ == '__main__':
    main()
