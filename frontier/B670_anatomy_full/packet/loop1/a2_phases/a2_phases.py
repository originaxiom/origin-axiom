"""A2 — THE RESONANT-PHASE LAW (cc2, loop1, per sealed PREREG_L1.md sha 247ace23).

Extends the P1 Milgram identification (promotion_queue/p1_milgram/p1_milgram.py:
gauss_exact, cyc_reduce, the sqrt|A|*zeta_8^j*[sqrt5] candidate pattern) to
RESONANT rungs r = p*u for each of the 25 Weyl classes and each resonant prime
p | det B_w, p in {2,3,5,7,11,19}.

Machinery reused verbatim (read, not re-executed as a side-effecting import):
  - bucket construction (25 classes) via next_queue/n1_counting/n1_jeffrey_terms
    (weyl_group/hnf_column/C6/P_WORD) -- identical to p1_milgram.py / f1_certificates.py
    so bucket indices line up with the banked findings (b0 sz6480 divs[7,35] ...).
  - gauss_exact/cyc_reduce/embed/poly_of/mul_dicts -- verbatim from p1_milgram.py.
  - elem_divisors(B) (SNF) and predicted_g2 (the banked UNIFORM JUMP LAW,
    finisher_queue/f1_jump/JUMP_LAW_THEOREM.md + f1_certificates.py):
        |G_w(r)|^2 = prod over elementary divisors d=p1^a1*p2^a2*... of
                     prod_p p^(a_p + min(v_p(r), a_p))
    -- this IS the "banked jump law" cited in the A2 clause; used here as the
    per-cell MAGNITUDE GATE (verified independently via conjugate-multiply, not
    just asserted).

NEW in this script: the PHASE at resonant r. For each (bucket, prime) cell,
sqrt(predicted_g2) = m * sqrt(radical), radical = product of primes with odd
exponent in predicted_g2's factorization. The radical is represented exactly in
the cyclotomic field via the classical quadratic Gauss sum
    gauss_dict(p, Np) = sum_{t=1}^{p-1} (t|p) zeta_p^t   (odd p; = eps_p*sqrt(p))
and, for p=2 (no odd-prime formula), the standard identity
    sqrt2_dict(Np) = zeta_8 + zeta_8^{-1} = sqrt(2).
gamma_w(pu) := G_w(pu) / (m * sqrt(radical)) is then searched over zeta_8^j,
j=0..7 (the SAME 8-candidate search p1_milgram.py already uses at generic
rungs) and VERIFIED exactly (embed candidate, compare polys mod Phi_Np) -- the
p1 pattern, extended.

SEALED HYPOTHESIS under test: gamma_w(pu) = c_w(p) * (u|p)^{m_w(p)}, m_w(p) in
{0,1}, c_w(p) a class constant. For p=2, "(u|p)" is replaced by the u mod 8
class per the prereg's explicit dyadic carve-out.
"""
import itertools
import json
import sys
import time
from fractions import Fraction

sys.path.insert(0, '<seat-workdir>/next_queue/n1_counting')
import mpmath as mp
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
try:
    from sympy.functions.combinatorial.numbers import legendre_symbol
except ImportError:
    from sympy.ntheory.residue_ntheory import legendre_symbol

import n1_jeffrey_terms as J

OUTDIR = '<seat-workdir>/anatomy/loop1/a2_phases'
PRIMES = (2, 3, 5, 7, 11, 19)
x = sp.symbols('x')

# =============================================================================
# bucket construction -- identical to p1_milgram.py / f1_certificates.py
# =============================================================================
W, eps = J.weyl_group()
buckets = {}
for idx in range(len(W)):
    w = W[idx]
    winv = np.rint(np.linalg.inv(w)).astype(np.int64)
    B = J.P_WORD * np.eye(6, dtype=np.int64) - w - winv
    cp = tuple(np.rint(np.poly(w.astype(float))).astype(np.int64))
    spec = tuple(sorted(np.linalg.eigvals(B.astype(float)).real.round(6)))
    buckets.setdefault((cp, spec), []).append((idx, B, int(eps[idx])))
ordered = sorted(buckets.items(), key=lambda kv: -len(kv[1]))
assert len(ordered) == 25, f"expected 25 classes, got {len(ordered)}"
BUCKET_B0 = {}
BUCKET_SIZE = {}
BUCKET_SIGN = {}
for bi, (key, members) in enumerate(ordered):
    idx0, B0, sgn = members[0]
    BUCKET_B0[bi] = B0
    BUCKET_SIZE[bi] = len(members)
    BUCKET_SIGN[bi] = sgn


def elem_divisors(B):
    M = sp.Matrix(B.tolist())
    snf = smith_normal_form(M)
    return [abs(int(snf[i, i])) for i in range(6) if abs(int(snf[i, i])) != 1]


BUCKET_DIVS = {bi: elem_divisors(BUCKET_B0[bi]) for bi in range(25)}


def vp(n, p):
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def resonant_primes(divs):
    det = 1
    for d in divs:
        det *= d
    return [p for p in PRIMES if det % p == 0]


BUCKET_RESONANT_PRIMES = {bi: resonant_primes(BUCKET_DIVS[bi]) for bi in range(25)}


# =============================================================================
# gauss_exact / cyc_reduce / embed / poly_of / mul_dicts -- verbatim p1_milgram.py
# =============================================================================
def cyc_reduce(vec_dict, N):
    coeffs = [0] * N
    for e, c in vec_dict.items():
        coeffs[e % N] += c
    p = sp.Poly(list(reversed(coeffs)), x, domain='QQ')
    rem = p.rem(sp.Poly(sp.cyclotomic_poly(N, x), x))
    return rem


def gauss_exact(B, r):
    Bs = sp.Matrix(B.tolist())
    ad = abs(int(Bs.det()))
    M = sp.Matrix(J.C6.tolist()) * Bs.inv()
    H = J.hnf_column(B)
    diag = [int(H[i, i]) for i in range(6)]
    Mf = [[Fraction(M[i, j]) for j in range(6)] for i in range(6)]
    terms = {}
    dens = set()
    raw = []
    for xx in itertools.product(*[range(d) for d in diag]):
        q = Fraction(0)
        for i in range(6):
            if xx[i]:
                for jj in range(6):
                    if xx[jj]:
                        q += xx[i] * Mf[i][jj] * xx[jj]
        e = (r * q) % 2
        raw.append(e)
        dens.add(e.denominator)
    N = 2 * np.lcm.reduce([int(d) for d in dens]) if dens else 2
    N = int(N)
    for e in raw:
        expo = int(-(e * N // 2)) % N
        terms[expo] = terms.get(expo, 0) + 1
    return cyc_reduce(terms, N), N, ad


def embed(polyrem, N, Np):
    k = Np // N
    out = {}
    cs = list(reversed(polyrem.all_coeffs()))
    for e, c in enumerate(cs):
        if c:
            out[(e * k) % Np] = out.get((e * k) % Np, 0) + c
    return out


def poly_of(dic, Np):
    coeffs = [0] * Np
    for e, c in dic.items():
        coeffs[e % Np] += c
    p = sp.Poly(list(reversed(coeffs)), x, domain='QQ')
    return p.rem(sp.Poly(sp.cyclotomic_poly(Np, x), x))


def mul_dicts(d1, d2, Np):
    out = {}
    for e1, c1 in d1.items():
        for e2, c2 in d2.items():
            out[(e1 + e2) % Np] = out.get((e1 + e2) % Np, 0) + c1 * c2
    return out


# =============================================================================
# |G|^2 exact (conjugate-multiply, verbatim f1_certificates.py) -- the per-cell
# MAGNITUDE GATE, checked against the banked jump-law formula predicted_g2.
# =============================================================================
def conjugate_mod(Gp, N):
    d = {}
    for (e,), c in Gp.as_dict().items():
        ne = (N - e) % N
        d[ne] = d.get(ne, 0) + c
    return cyc_reduce(d, N)


def abs_sq_exact(Gp, N):
    Gconj = conjugate_mod(Gp, N)
    prod = Gp * Gconj
    PhiN = sp.Poly(sp.cyclotomic_poly(N, x), x)
    rem = prod.rem(PhiN)
    if rem.is_zero:
        return 0
    assert rem.degree() == 0, f"|G|^2 not a rational constant (N={N}): {rem.as_expr()}"
    c = rem.all_coeffs()[0]
    cr = sp.nsimplify(c)
    assert cr.is_Integer or (cr.is_Rational and cr.q == 1), f"|G|^2 not integer: {c}"
    val = int(cr)
    assert val >= 0, f"|G|^2 negative: {val}"
    return val


def predicted_g2(divs, r):
    """THE BANKED UNIFORM JUMP LAW (F1, JUMP_LAW_THEOREM.md): certified integer."""
    pred = 1
    for d in divs:
        for p in PRIMES:
            a = vp(d, p)
            if a:
                v = vp(r, p)
                pred *= p ** (a + min(v, a))
    return pred


# =============================================================================
# radical representation: classical Gauss sum (odd p) / sqrt2 identity (p=2)
# =============================================================================
def gauss_dict(p, Np):
    """sum_{t=1}^{p-1} (t|p) zeta_p^t embedded in Q(zeta_Np); p odd, p | Np.
    Equals eps_p*sqrt(p) by Gauss's theorem (eps_p = 1 if p=1 mod4, i if p=3
    mod4) -- generalizes p1_milgram.py's sqrt5_dict to any odd resonant p."""
    k = Np // p
    d = {}
    for t in range(1, p):
        leg = legendre_symbol(t, p)
        d[(t * k) % Np] = d.get((t * k) % Np, 0) + leg
    return d


def sqrt2_dict(Np):
    """zeta_8 + zeta_8^{-1} = sqrt(2) exactly; 8 | Np."""
    k = Np // 8
    return {(1 * k) % Np: 1, (7 * k) % Np: 1}


def radical_dict(p, Np):
    return sqrt2_dict(Np) if p == 2 else gauss_dict(p, Np)


# =============================================================================
# per-cell identification: G_w(r) = m * sqrt(radical) * zeta_8^j  (search+verify)
# =============================================================================
def identify_cell(bi, p, u):
    B0 = BUCKET_B0[bi]
    divs = BUCKET_DIVS[bi]
    r = p * u
    Gp, N, ad = gauss_exact(B0, r)
    g2_obs = abs_sq_exact(Gp, N)
    g2_pred = predicted_g2(divs, r)
    mag_gate = (g2_obs == g2_pred)

    m = 1
    R = []
    for q in PRIMES:
        v = vp(g2_pred, q)
        m *= q ** (v // 2)
        if v % 2:
            R.append(q)

    Np = N
    for f in (8, *R):
        Np = int(np.lcm(Np, f))
    Gd = embed(Gp, N, Np)
    Gcan = poly_of(Gd, Np)

    magdict = {0: m}
    for q in R:
        magdict = mul_dicts(magdict, radical_dict(q, Np), Np)

    ident = None
    for j in range(8):
        base = {(j * (Np // 8)) % Np: 1}
        cand = mul_dicts(base, magdict, Np)
        if poly_of(cand, Np) == Gcan:
            ident = j
            break

    fallback = None
    if ident is None:
        # numeric snap (dps 40) then exact re-verify over a wider ring, per
        # the prereg's prescribed fallback (24th/40th roots as needed).
        mp.mp.dps = 40
        zNp = mp.e ** (2j * mp.pi / Np)
        Gval = sum(c * zNp ** e for e, c in Gd.items())
        magval_real = mp.sqrt(g2_pred)
        phase = Gval / magval_real
        for Kc in (8, 24, 40, 4 * p if p != 2 else 8, Np):
            Kc = int(Kc)
            if Np % Kc != 0 and Kc != Np:
                continue
            found = False
            for jj in range(Kc):
                cand_phase = mp.e ** (2j * mp.pi * jj / Kc)
                if abs(phase - cand_phase) < mp.mpf('1e-20'):
                    # exact re-verify at this Kc
                    Npp = int(np.lcm(Np, Kc))
                    Gdd = embed(Gp, N, Npp)
                    Gcc = poly_of(Gdd, Npp)
                    md2 = {0: m}
                    for q in R:
                        md2 = mul_dicts(md2, radical_dict(q, Npp), Npp)
                    base2 = {(jj * (Npp // Kc)) % Npp: 1}
                    cand2 = mul_dicts(base2, md2, Npp)
                    if poly_of(cand2, Npp) == Gcc:
                        fallback = {"Kc": Kc, "j": jj}
                        found = True
                        break
            if found:
                break

    return {
        "bucket": bi, "p": p, "u": u, "r": r,
        "legendre_u_p": (None if p == 2 else int(legendre_symbol(u, p))),
        "legendre_u_5": (int(legendre_symbol(u, 5)) if u % 5 != 0 else None),
        "u_mod_8": (u % 8 if p == 2 else None),
        "N": N, "Np": Np, "absdet": ad,
        "g2_obs": g2_obs, "g2_pred": g2_pred, "magnitude_gate": mag_gate,
        "m": m, "radical": R,
        "j8": ident, "fallback": fallback,
        "identified": (ident is not None) or (fallback is not None),
    }


# =============================================================================
# TEST PLAN -- scope control per prereg: ALL p=5 classes (10 chi5 + 6 more with
# 5|det); b1/p=19; b2,b3/p=11; b0/p=7; 3 dyadic classes/p=2 (mod-8 character);
# one deep-3 class. r=p*u chosen with u prime (or, for p=2,3, small units)
# coprime to every OTHER resonant prime of that bucket -- stated explicitly.
# =============================================================================
P5_BUCKETS = [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 19, 22, 23]
P5_UNITS = (13, 17, 29, 41)          # (13|5)=-1 (17|5)=-1 (29|5)=+1 (41|5)=+1
P19_UNITS = (13, 17, 23, 29)          # bucket1 (not chi5: no confound)
P11_UNITS_B2 = (13, 23, 31, 41)       # bucket2 (not chi5, radical=[]: plain (u|11) test)
# bucket3 IS chi5 (radical=[5] when p=11 resonant) -- its generic-level twist
# character depends on (r|5); a first pass with primes correlated (u|11) with
# (u|5) by accident and produced an apparent within-symbol inconsistency. Redesigned
# to independently span all 4 combinations of ((u|11),(u|5)) so the two candidate
# drivers can be told apart: u=1((+,+)), 23((+,-)), 101((-,+)), 17((-,-)).
P11_UNITS_B3 = (1, 23, 101, 17)
# bucket0 IS chi5 (radical=[5] when p=7 resonant) -- same redesign, spanning all
# 4 combinations of ((u|7),(u|5)): 71((+,+)), 127((+,-)), 31((-,+)), 17((-,-)).
P7_UNITS = (71, 127, 31, 17)
P2_UNITS = (1, 3, 5, 7, 9)            # buckets 14,20,21 -- u mod 8 in {1,3,5,7,1}
P3_UNITS = (1, 2, 4, 5, 7, 8)          # bucket16 (deep-3) -- full unit set mod 9

PLAN = []
for b in P5_BUCKETS:
    for u in P5_UNITS:
        PLAN.append((b, 5, u))
for u in P19_UNITS:
    PLAN.append((1, 19, u))
for u in P11_UNITS_B2:
    PLAN.append((2, 11, u))
for u in P11_UNITS_B3:
    PLAN.append((3, 11, u))
for u in P7_UNITS:
    PLAN.append((0, 7, u))
for b in (14, 20, 21):
    for u in P2_UNITS:
        PLAN.append((b, 2, u))
for u in P3_UNITS:
    PLAN.append((16, 3, u))

# sanity: every planned r must be coprime to every OTHER resonant prime of its bucket
for (bi, p, u) in PLAN:
    r = p * u
    others = [q for q in BUCKET_RESONANT_PRIMES[bi] if q != p]
    for q in others:
        assert r % q != 0, f"bucket {bi} p={p} u={u}: r={r} divisible by other resonant prime {q}"


def main():
    t0 = time.time()
    print(f"25 classes built. {len(PLAN)} (bucket,prime,unit) cells planned.", flush=True)
    print(f"resonant primes per bucket: "
          f"{ {bi: BUCKET_RESONANT_PRIMES[bi] for bi in range(25)} }", flush=True)

    rows = []
    mag_gate_total = 0
    mag_gate_pass = 0
    ident_total = 0
    ident_pass = 0
    fallback_count = 0

    by_bp = {}
    for (bi, p, u) in PLAN:
        t_c = time.time()
        cell = identify_cell(bi, p, u)
        rows.append(cell)
        mag_gate_total += 1
        mag_gate_pass += int(cell["magnitude_gate"])
        ident_total += 1
        ident_pass += int(cell["identified"])
        if cell["fallback"] is not None:
            fallback_count += 1
        by_bp.setdefault((bi, p), []).append(cell)
        sym = (cell["legendre_u_p"] if p != 2 else f"u%8={cell['u_mod_8']}")
        print(f"b{bi:2d} p={p:2d} u={u:3d} r={cell['r']:4d}  sym={sym}  "
              f"|G|^2 obs={cell['g2_obs']:6d} pred={cell['g2_pred']:6d} "
              f"gate={'OK' if cell['magnitude_gate'] else 'FAIL'}  "
              f"m={cell['m']:4d} rad={cell['radical']}  j8={cell['j8']}"
              f"{'  [fallback ' + str(cell['fallback']) + ']' if cell['fallback'] else ''}"
              f"  ({time.time() - t_c:.2f}s)", flush=True)

    # ---- per-(bucket,prime) phase-law analysis ----
    print("\n=== PER-CLASS-PRIME PHASE LAW: c_w(p), m_w(p) ===", flush=True)
    law_table = {}
    law_holds_all = True
    witnesses = []
    for (bi, p), cells in sorted(by_bp.items()):
        if p == 2:
            # dyadic: report j as function of u mod 8 (no Legendre symbol)
            by_res = {}
            for c in cells:
                by_res.setdefault(c["u_mod_8"], []).append(c["j8"])
            consistent = all(len(set(v)) == 1 for v in by_res.values() if all(x is not None for x in v))
            all_j = set(c["j8"] for c in cells)
            const_across_res = len(all_j) == 1
            entry = {"kind": "dyadic-mod8", "by_u_mod8": {str(k): v for k, v in by_res.items()},
                     "within_class_consistent": consistent,
                     "constant_across_mod8_classes": const_across_res,
                     "c_w": (list(all_j)[0] if const_across_res else None)}
            law_table[f"b{bi}_p{p}"] = entry
            if not consistent:
                law_holds_all = False
                witnesses.append((bi, p, "within-mod8-class j not constant", by_res))
        else:
            has_confound = any(5 in c["radical"] for c in cells) and p != 5
            plus = [c["j8"] for c in cells if c["legendre_u_p"] == 1]
            minus = [c["j8"] for c in cells if c["legendre_u_p"] == -1]
            plus_ok = len(set(plus)) <= 1
            minus_ok = len(set(minus)) <= 1
            j_plus = plus[0] if plus else None
            j_minus = minus[0] if minus else None
            if plus_ok and minus_ok and j_plus is not None and j_minus is not None:
                if j_plus == j_minus:
                    m_w = 0
                    c_w = j_plus
                elif (j_minus - j_plus) % 8 == 4:
                    m_w = 1
                    c_w = j_plus
                else:
                    m_w = None
                    c_w = None
            else:
                m_w = None
                c_w = None
            consistent = plus_ok and minus_ok and (m_w is not None)
            entry = {"kind": "odd-legendre", "j_at_plus1": j_plus, "j_at_minus1": j_minus,
                     "m_w": m_w, "c_w_zeta8_exp": c_w, "consistent": consistent}

            if has_confound:
                # class carries an intrinsic chi5 (radical=[5]) character even
                # though the resonant prime under test is p != 5; the class's
                # PRE-EXISTING generic-level twist (P1's "gamma(29)/gamma(13)=-1
                # on chi5 classes") depends on (r|5), and r=p*u's own residue
                # mod 5 varies with u even when 5 is not the resonant prime.
                # Units were chosen (P7_UNITS/P11_UNITS_B3) to independently span
                # all 4 combinations of ((u|p),(u|5)) so the two candidate
                # drivers can be told apart exactly.
                by_sym_p = {}
                by_sym_5 = {}
                by_prod = {}
                detail = []
                for c in cells:
                    sp_, s5 = c["legendre_u_p"], c["legendre_u_5"]
                    by_sym_p.setdefault(sp_, set()).add(c["j8"])
                    by_sym_5.setdefault(s5, set()).add(c["j8"])
                    by_prod.setdefault(sp_ * s5, set()).add(c["j8"])
                    detail.append({"u": c["u"], "sym_p": sp_, "sym_5": s5, "j8": c["j8"]})
                fits_p = all(len(v) == 1 for v in by_sym_p.values())
                fits_5 = all(len(v) == 1 for v in by_sym_5.values())
                fits_prod = all(len(v) == 1 for v in by_prod.values())
                driver = ("(u|p)" if fits_p else None) or ("(u|5)" if fits_5 else None) \
                    or ("(u|p)*(u|5)" if fits_prod else None) or "NONE (falsified)"
                entry["confound_check"] = {
                    "detail": detail, "fits_symbol_p": fits_p, "fits_symbol_5": fits_5,
                    "fits_product": fits_prod, "true_driver": driver}
                # override the naive (u|p)-only verdict with the disentangled one
                entry["consistent"] = fits_p or fits_5 or fits_prod
                entry["m_w"] = (1 if fits_p else 0) if fits_p or (not fits_5 and not fits_prod) else None
                consistent = entry["consistent"]
                if not (fits_p or fits_5 or fits_prod):
                    law_holds_all = False
                    witnesses.append((bi, p, "no quadratic-symbol driver fits (p, 5, or product)", detail))
                elif not fits_p:
                    # sealed hypothesis as literally stated (driver = (u|p)) is
                    # falsified for this cell; the broader "depends only on SOME
                    # quadratic symbol" reading survives via (u|5) or the product.
                    witnesses.append((bi, p,
                                       f"driver is {driver}, not (u|{p}) -- literal "
                                       f"sealed hypothesis falsified, broader symbol "
                                       f"reading survives", detail))
            law_table[f"b{bi}_p{p}"] = entry
            if not has_confound and not consistent:
                law_holds_all = False
                witnesses.append((bi, p, "symbol pattern broken", {"plus": plus, "minus": minus}))
        print(f"b{bi:2d} p={p:2d}: {law_table[f'b{bi}_p{p}']}", flush=True)

    dt = time.time() - t0
    print(f"\n=== TOTALS ===", flush=True)
    print(f"magnitude gate: {mag_gate_pass}/{mag_gate_total}", flush=True)
    print(f"phase identification: {ident_pass}/{ident_total} (fallback used: {fallback_count})", flush=True)
    print(f"LAW consistent on ALL tested (bucket,prime) cells: {law_holds_all}", flush=True)
    if witnesses:
        print(f"WITNESSES (falsifier hits): {witnesses}", flush=True)
    print(f"total wall time: {dt:.2f}s", flush=True)

    out = {
        "plan_size": len(PLAN),
        "bucket_divs": BUCKET_DIVS,
        "bucket_resonant_primes": BUCKET_RESONANT_PRIMES,
        "cells": rows,
        "law_table": law_table,
        "law_holds_all": law_holds_all,
        "witnesses": witnesses,
        "gates": {
            "magnitude_gate": {"pass": mag_gate_pass, "total": mag_gate_total},
            "identification": {"pass": ident_pass, "total": ident_total,
                                "fallback_used": fallback_count},
        },
        "total_wall_time_s": dt,
    }
    with open(f"{OUTDIR}/a2_table.json", "w") as f:
        json.dump(out, f, indent=1)
    print("DONE -- a2_table.json", flush=True)
    return 0 if (mag_gate_pass == mag_gate_total and ident_pass == ident_total) else 1


if __name__ == '__main__':
    sys.exit(main())
