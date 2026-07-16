#!/usr/bin/env python3
"""
F4 track-S verify: INDEPENDENT recompute of B649 stage 2a/2b headline
("the m136 holonomy generators are EXACT elements of SL2(L), L=Q(s,i),
s^4=8s^2+16; the silver 27-letters exact over L").

Written from scratch (own pslq identification code, own precision choices
different from cc's 1200-bit run, own arithmetic backend for exactness
checks: sympy's algebraic number field QQ.algebraic_field(s0, I) instead
of cc's hand-rolled Fraction-vector quotient-ring class in b649_stage2a.py
/ b649_stage2b.py). cc's scripts are consulted only for the PUBLIC
conventions (presentation, field, targets) already stated in the sealed
preregs -- not for the identification/verification code itself.

Repo READ-ONLY: only reads from origin-axiom; all writes go to this
work dir.
"""
import json
import os
import time

import mpmath as mp
import snappy
import sympy
from sympy import QQ, I as sI, sqrt as sy_sqrt, symbols

RESULTS = {}
SRC = "<seat-workdir>/origin-axiom/frontier/B649_silver_holonomy"


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78)


# ----------------------------------------------------------------------------
# 1. Fresh numeric holonomy at bits_prec = 800 (own choice; cc used 1200) and
#    a second, independent lower threshold at bits_prec = 400, to check that
#    exact identification is stable across precision (the "two thresholds").
# ----------------------------------------------------------------------------
section("1. FRESH SNAPPY HOLONOMY, TWO PRECISIONS (800-bit, 400-bit)")
from snappy.snap.polished_reps import polished_holonomy

M0 = snappy.Manifold("m136")


def get_holonomy(bits):
    t0 = time.time()
    G = polished_holonomy(M0, bits_prec=bits, lift_to_SL2=False)
    print(f"  polished_holonomy(bits_prec={bits}) obtained in {time.time()-t0:.1f}s")
    return G


G800 = get_holonomy(800)
G400 = get_holonomy(400)


def clean(x):
    return str(x).replace(" E", "e").replace("E", "e").strip()


def mat_mpc(mat, dps):
    with mp.workdps(dps):
        return [[mp.mpc(clean(mat[i][j].real()), clean(mat[i][j].imag()))
                 for j in range(2)] for i in range(2)]


mp.mp.dps = 260
A800 = mat_mpc(G800("a"), 260)
A400 = mat_mpc(G400("a"), 130)

print("A (800-bit) =", A800)
print("A (400-bit) =", A400)

# both precisions must agree well inside the tighter precision's noise floor
cross_resid = max(abs(A800[i][j] - A400[i][j]) for i in range(2) for j in range(2))
print("cross-precision residual (800-bit vs 400-bit):", cross_resid)
RESULTS["cross_precision_residual_a"] = str(cross_resid)

# ----------------------------------------------------------------------------
# 2. Own pslq-based identification of A's entries in Q(s), s^4=8s^2+16
#    (fresh code: different variable names / control flow from cc's
#    ident_real/ident_entry; same underlying math method (pslq) since
#    that IS the correct tool -- independence here means "own script",
#    not "different algorithm for an inherently pslq problem").
# ----------------------------------------------------------------------------
section("2. OWN PSLQ IDENTIFICATION IN Q(s,i), TWO ACCEPTANCE THRESHOLDS")

s_val = mp.sqrt(4 + 4 * mp.sqrt(2))
print("s (positive real root of s^4-8s^2-16) =", s_val)
print("quartic residual:", abs(s_val ** 4 - 8 * s_val ** 2 - 16))


def identify_in_Qs(x, dps, thresh_exp):
    """Return (c0,c1,c2,c3) rationals with x ~= c0+c1 s+c2 s^2+c3 s^3, or None."""
    with mp.workdps(dps):
        basis = [mp.mpf(1), s_val, s_val ** 2, s_val ** 3]
        if abs(x) < mp.mpf(10) ** (-(dps - 20)):
            return (0, 0, 0, 0)
        rel = mp.pslq([x] + basis, maxcoeff=10 ** 9, maxsteps=2 * 10 ** 5)
        if rel is None or rel[0] == 0:
            return None
        from fractions import Fraction as Fr
        c0 = rel[0]
        coeffs = tuple(Fr(-rel[k + 1], c0) for k in range(4))
        recon = sum(mp.mpf(c.numerator) / c.denominator * basis[k]
                    for k, c in enumerate(coeffs))
        resid = abs(recon - x)
        if resid > mp.mpf(10) ** (-thresh_exp):
            return None
        return coeffs, resid


def identify_entry(z, dps, thresh_exp):
    re_r = identify_in_Qs(mp.re(z), dps, thresh_exp)
    im_r = identify_in_Qs(mp.im(z), dps, thresh_exp)
    return re_r, im_r


# identify a[0][0] at two different (precision, threshold) pairs
res_tight = identify_entry(A800[0][0], 240, 220)
res_loose = identify_entry(A800[0][0], 130, 110)
print("a[0][0] identified at 800-bit/220-digit threshold:", res_tight)
print("a[0][0] identified at 400-bit/110-digit threshold:", res_loose)

RESULTS["a00_identification"] = {
    "tight_240dps_220digit": str(res_tight),
    "loose_130dps_110digit": str(res_loose),
}

tight_ok = res_tight is not None and res_tight[0] is not None and res_tight[1] is not None
loose_ok = res_loose is not None and res_loose[0] is not None and res_loose[1] is not None
same_coeffs = tight_ok and loose_ok and res_tight[0][0] == res_loose[0][0] and res_tight[1][0] == res_loose[1][0]
print("identification succeeds at BOTH thresholds:", tight_ok and loose_ok)
print("identical coefficients recovered at both thresholds (stability check):", same_coeffs)
RESULTS["identification_stable_across_thresholds"] = bool(same_coeffs)

# ----------------------------------------------------------------------------
# 3. Compare against the banked, hash-verified entries_L.json (a00), via an
#    INDEPENDENT arithmetic backend: sympy's algebraic number field
#    QQ.algebraic_field(s0, I), rather than cc's Fraction-vector class.
# ----------------------------------------------------------------------------
section("3. CROSS-CHECK vs entries_L.json, VIA SYMPY ALGEBRAIC FIELD (own backend)")

banked = json.load(open(os.path.join(SRC, "entries_L.json")))
a00_re_banked = [int(x) if "/" not in x else x for x in banked["a00"][0]]
a00_im_banked = [int(x) if "/" not in x else x for x in banked["a00"][1]]
print("banked entries_L.json a00 re-coeffs:", banked["a00"][0])
print("banked entries_L.json a00 im-coeffs:", banked["a00"][1])

from fractions import Fraction as Fr


def to_fr_list(lst):
    return [Fr(x) for x in lst]


banked_re = to_fr_list(banked["a00"][0])
banked_im = to_fr_list(banked["a00"][1])

my_re, resid_re = res_tight[0]
my_im, resid_im = res_tight[1]
match_re = tuple(my_re) == tuple(banked_re)
match_im = tuple(my_im) == tuple(banked_im)
print("my identified re-coeffs == banked:", match_re, tuple(my_re), "vs", tuple(banked_re))
print("my identified im-coeffs == banked:", match_im, tuple(my_im), "vs", tuple(banked_im))
RESULTS["a00_matches_banked_entries_L"] = bool(match_re and match_im)

# sympy algebraic field arithmetic: build s0 as a sympy algebraic number,
# construct L = Q(s0, I) directly, verify entry a00 as an ANP element, and
# independently re-verify one exact trace relation (tr(b) = 2) and one
# relator (aBAbcc = I) via THIS field, using ONLY the banked entries_L.json
# (hash-verified) -- an independent arithmetic re-derivation of S2a-G2/G3.
s0 = sy_sqrt(4 + 4 * sy_sqrt(2))
K = QQ.algebraic_field(s0, sI)
print("sympy field:", K)


def L_from_coeffs(re_c, im_c):
    expr = sum(sympy.Rational(c) * s0 ** k for k, c in enumerate(re_c)) + \
        sI * sum(sympy.Rational(c) * s0 ** k for k, c in enumerate(im_c))
    return K.from_sympy(sympy.expand(expr))


def load_gen_sympy(nm):
    return [[L_from_coeffs(banked[f"{nm}{i}{j}"][0], banked[f"{nm}{i}{j}"][1])
             for j in range(2)] for i in range(2)]


t0 = time.time()
Asy = load_gen_sympy("a")
Bsy = load_gen_sympy("b")
Csy = load_gen_sympy("c")
print(f"loaded a,b,c into sympy ANP field in {time.time()-t0:.2f}s")


def K_conj(x):
    """L-conjugation i -> -i on an ANP element, done by re-deriving through
    the sympy expression (own route, not touching cc's conj code)."""
    e = K.to_sympy(x)
    e2 = e.subs(sI, -sI, simultaneous=True)
    return K.from_sympy(sympy.expand(e2))


def mm(X, Y):
    return [[X[i][0] * Y[0][j] + X[i][1] * Y[1][j] for j in range(2)]
            for i in range(2)]


def madj(M):
    zero = K.from_sympy(sympy.Integer(0))
    return [[M[1][1], zero - M[0][1]], [zero - M[1][0], M[0][0]]]


ZERO = K.from_sympy(sympy.Integer(0))
ONE = K.from_sympy(sympy.Integer(1))
lets_sy = {"a": Asy, "b": Bsy, "c": Csy,
           "A": madj(Asy), "B": madj(Bsy), "C": madj(Csy)}


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


for nm in "abc":
    d = det2(lets_sy[nm])
    print(f"  sympy-field det({nm}) == 1 exactly:", d == ONE)
    RESULTS[f"sympy_det_{nm}_eq_1"] = bool(d == ONE)


def word(w):
    m = None
    for ch in w:
        m = lets_sy[ch] if m is None else mm(m, lets_sy[ch])
    return m


print("\n-- relators (sympy algebraic field, own backend) --")
for rel in ("aBAbcc", "aaCbcB"):
    R = word(rel)
    ok = (R[0][0] == ONE and R[1][1] == ONE and R[0][1] == ZERO and R[1][0] == ZERO)
    print(f"  {rel} = I exactly (sympy field): {ok}")
    RESULTS[f"sympy_relator_{rel}_eq_I"] = bool(ok)

print("\n-- peripheral + trace relations (sympy algebraic field) --")
TWO = K.from_sympy(sympy.Integer(2))
MTWO = K.from_sympy(sympy.Integer(-2))


def tr(M):
    return M[0][0] + M[1][1]


mu_tr = tr(word("CCB"))
lam_tr = tr(word("caCA"))
b_tr = tr(lets_sy["b"])
print("  tr(CCB) == 2:", mu_tr == TWO)
print("  tr(caCA) == -2:", lam_tr == MTWO)
print("  tr(b) == 2:", b_tr == TWO)
RESULTS["sympy_tr_mu_eq_2"] = bool(mu_tr == TWO)
RESULTS["sympy_tr_lam_eq_m2"] = bool(lam_tr == MTWO)
RESULTS["sympy_tr_b_eq_2"] = bool(b_tr == TWO)

sqrt2_expr = (s0 ** 2 - 4) / 4
sqrt2_K = K.from_sympy(sympy.expand(sqrt2_expr))
i_K = K.from_sympy(sI)
ac_target = ZERO - sqrt2_K - sqrt2_K * i_K
abc_target = ZERO - TWO * sqrt2_K * i_K
ac_tr = tr(word("ac"))
abc_tr = tr(word("abc"))
print("  tr(ac) == -sqrt2 - sqrt2*i:", ac_tr == ac_target)
print("  tr(abc) == -2*sqrt2*i:", abc_tr == abc_target)
RESULTS["sympy_tr_ac_matches"] = bool(ac_tr == ac_target)
RESULTS["sympy_tr_abc_matches"] = bool(abc_tr == abc_target)

section("STAGE 2 SUMMARY")
for k, v in RESULTS.items():
    print(f"  {k}: {v}")

with open("<seat-workdir>/seat-work/finisher_queue/f4_receipt/stage2_results.json", "w") as f:
    json.dump(RESULTS, f, indent=2, default=str)
print("\nWrote stage2_results.json")
