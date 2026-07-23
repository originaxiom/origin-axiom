"""
OI-148 -- B415 level-27 mu_infinity confirmation (B771 Phase-1 Wave-1).

CONTEXT (read from the sources, not asserted):
  - docs/LEAD_REGISTER.md:66 lists "B415 (level-27 mu_inf confirmation, #3)" as an
    open LOW-priority lead using the cyclotomic engine (#3).
  - frontier/B415_behavior_tracking/FINDINGS.md (T1, already banked) characterizes
    mu_inf as a "Gauss-sum-modulated Haar measure on Z_3 x Z/5" but explicitly flags:
    "the level-27 magnitude check needs the correct Frobenius orbit and is deferred
     -- not a lock; the characterization rests on the exact level-9 anchor."
  - frontier/B415_behavior_tracking/t1_continuum.py's level-27 check used an AD HOC,
    admittedly-uncertain orbit guess (orbit_m=[1,4,7], with the code comment itself
    unsure which Frobenius map it represents) and got a numeric near-miss (3.27
    against a naively-extrapolated target). Not a real computation.
  - The REAL level-27 object exists and is banked structurally in a different arc:
    frontier/B399_wall_scale/FINDINGS.md + triple_id.json. At the 1215 tower rung,
    besides the 12 frozen 1/12-cells, there is a genuine "Z/3 orbit at the zeta27
    level" -- three tower-support values (cells 121, 256, 391 mod 1215, each with
    multiplicity 4) that are the roots of the cubic
        t^3 - (1/48) t - e3,     e1 = 0 (EXACT, proven), e2 = -1/48 (EXACT),
    with e3 PENDING -- two independent CRT/LLL reconstruction passes (recon_e3.py,
    triple_cubic.json) both failed to pin it down (UNSTABLE / denominator-collision).
    A third attempt in the sibling cell OI-031 (this same B771 wave, a DIFFERENT
    cell targeting e3's closed form specifically) also failed to identify e3 in Q
    or Q(sqrt5) at the swept height (crashed on an internal LLL assertion after the
    Q/Q(sqrt5) hunts were already rejected on the stability/margin guard).

THIS CELL'S STRATEGY (avoids the e3 bottleneck entirely):
  B413's exact level-9 "flat/Gauss-sum" fact was: for the raw Galois-conjugate
  triple c_k = 2cos(2pi k/9) (k in {1,2,4}, roots of x^3-3x+1), the Z/3-Fourier
  "Lagrange resolvent" L = c_0 + omega*c_1 + omega^2*c_2 (omega = primitive cube
  root of unity) has |L|^2 = 9 EXACTLY, computed there as |12*L(chi_1)|^2 = 9 in
  Z[zeta_9] (the "12" clears the tower's (1+c)/12 normalization back to the raw
  algebraic-integer roots c_k).

  The key algebraic fact (elementary, symmetric-function identity, proved below
  with sympy AND checked against the level-9 numbers as a control): for ANY cubic
  with real roots r0,r1,r2 and elementary symmetric functions e1=Sum r_i,
  e2=Sum r_i r_j (i<j), the resolvent product
        L * conj(L) = (r0+w r1+w^2 r2)(r0+w^2 r1+w r2) = e1^2 - 3 e2
  ALWAYS holds -- independent of e3, independent of which cyclic order is chosen
  (e1, e2 are symmetric; the identity does not need to know "the correct Frobenius
  orbit" at all). Since e1=0 and e2=-1/48 are ALREADY EXACT AND BANKED (re-derived
  in-cell below from the raw F_p tower data, not cited), the level-27 resolvent
  norm is COMPUTABLE EXACTLY RIGHT NOW, without e3.

  To compare like-for-like with level 9's raw-algebraic-integer convention (where
  the tower value was v=(1+c)/12 and the norm was computed on 12v=c, i.e. the roots
  after "clearing the /12 normalization"), we apply the SAME clearing transform
  y = 12*v to the 1215-level triple (v = the raw tower cell value, root of
  t^3-(1/48)t-e3) and recompute the resolvent norm on y. This is forced, not a free
  choice: y=12v satisfies y^3 - 3y - 1728*e3 = 0 (verified below both symbolically
  and against the raw F_p data), i.e. the SAME "-3" linear coefficient as the
  level-9 minimal polynomial x^3-3x+1 -- a non-trivial internal match confirming the
  clearing transform is the right one to compare against level 9's exact convention.

  T1's registered numeric prediction (t1_continuum.py, gauss_norm_at_level(k) =
  3**k): if the flat/Gauss-sum property persists from level 9 (k=2, norm^2=9) to
  level 27 (k=3), the norm-squared should be 3^3 = 27. This cell computes the EXACT
  value and checks it against 27.

Everything below is exact rational/symbolic arithmetic (sympy Rational + Poly) plus
independent verification against the raw F_p tower data (20 primes, no numerics).
"""
import json
import math
import os
import sys
import time

import sympy as sp

T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, "..", "..", "..", "B399_wall_scale"))
assert os.path.isdir(SRC), f"source arc missing: {SRC}"

FILES = [
    "singles_1215.json",
    "singles_1215_p3.json",
    "singles_1215_p456.json",
    "singles_1215_p7_10.json",
    "singles_1215_p11_20.json",
    "singles_1215_p14_20.json",
]
CELLS = (121, 256, 391)

# ---------------------------------------------------------------------------
# STEP 0: load the raw F_p tower data (the 20-prime CRT record from B399), and
# recompute e1, e2, e3 mod p myself -- IN-CELL, not cited from FINDINGS.md.
# ---------------------------------------------------------------------------
DATA = {}
for f in FILES:
    path = os.path.join(SRC, f)
    assert os.path.isfile(path), f"missing source file: {path}"
    DATA.update(json.load(open(path)))

primes = sorted(int(p) for p in DATA)
log(f"loaded {len(primes)} primes from B399_wall_scale/*.json: {primes}")
assert len(primes) >= 15, "need a healthy prime batch to trust the CRT reconstruction"

e1_mod = {}
e2_mod = {}
e3_mod = {}
for p in primes:
    d = DATA[str(p)]
    vals = [int(d[str(c)]) % p for c in CELLS]
    v0, v1, v2 = vals
    e1_mod[p] = (v0 + v1 + v2) % p
    e2_mod[p] = (v0 * v1 + v1 * v2 + v2 * v0) % p
    e3_mod[p] = (v0 * v1 * v2) % p

# gate: e1 == 0 mod every prime (the sum rule / trace-zero innovation law)
assert all(e1_mod[p] == 0 for p in primes), "e1 != 0 mod some prime -- STOP"
log("gate: e1 == 0 mod all 20 primes (trace-zero innovation, re-derived in-cell)")

# gate: e2 == -1/48 mod every prime
inv48 = {p: pow(48, p - 2, p) for p in primes}
target_e2 = {p: (-inv48[p]) % p for p in primes}
assert all(e2_mod[p] == target_e2[p] for p in primes), "e2 != -1/48 mod some prime -- STOP"
log("gate: e2 == -1/48 mod all 20 primes (re-derived in-cell, matches B399's banked value)")

# ---------------------------------------------------------------------------
# STEP 1: is e3 pinned down by 20 primes as a SMALL rational (a much simpler
# ansatz than the Q(sqrt5) hunt that already failed in OI-031 and in recon_e3.py)?
# Direct test: does 1728*e3 reduce to the SAME small integer mod every prime?
# (Motivated by the y=12v clearing transform derived below: y^3-3y-1728e3=0,
#  echoing x^3-3x+1 at level 9, where the constant term was the small integer 1.)
# ---------------------------------------------------------------------------
cand_hit = None
for k in range(-5000, 5001):
    if all((1728 * e3_mod[p] - k) % p == 0 for p in primes):
        cand_hit = k
        break
log(f"small-integer scan on 1728*e3 in [-5000,5000] against all 20 primes: {cand_hit}")

# Also attempt a genuine rational reconstruction of e3 from the full 20-prime CRT
# (Q ansatz only -- the simplest possible one; Q(sqrt5) and beyond are OI-031's
# territory and already failed there / in recon_e3.py; not re-litigated here).
M = 1
for p in primes:
    M *= p
r = 0
for p in primes:
    Mi = M // p
    r = (r + e3_mod[p] * Mi * pow(Mi, -1, p)) % M


def rational_reconstruct(r, M, bound=None):
    if bound is None:
        bound = math.isqrt(M // 2)
    a0, a1 = M, r
    b0, b1 = 0, 1
    while a1 > bound:
        q = a0 // a1
        a0, a1 = a1, a0 - q * a1
        b0, b1 = b1, b0 - q * b1
    if b1 == 0 or sp.gcd(abs(b1), M) != 1:
        return None
    return sp.Rational(a1, b1) if b1 > 0 else sp.Rational(-a1, -b1)


e3_Q = rational_reconstruct(r, M)
log(f"pure-Q rational reconstruction of e3 from all 20 primes (full-height bound "
    f"~sqrt(M/2), M ~10^{len(str(M))}): {e3_Q}")
if e3_Q is not None:
    ok_all = all((int(e3_Q.p) * pow(int(e3_Q.q), p - 2, p) - e3_mod[p]) % p == 0 for p in primes)
    log(f"  candidate verified mod all 20 primes: {ok_all}  (height num~10^{len(str(e3_Q.p))}, "
        f"den~10^{len(str(e3_Q.q))})")
    log("  CAVEAT (not a positive result): with a reconstruction bound this large "
        "(~10^75), the extended-Euclidean algorithm ALWAYS returns SOME fraction "
        "under the bound for essentially any residue -- this is not evidence e3 IS "
        "this fraction, only that no genuine collapse to a small-height rational "
        "occurred. The informative test is the small-integer scan above (None found "
        "in [-5000,5000]) -- e3 is NOT small/simple in Q. Consistent with recon_e3.py "
        "(Q(sqrt5) ansatz, UNSTABLE) and OI-031 (Q and Q(sqrt5) both rejected on the "
        "stability/margin guard). e3's exact closed form remains UNRESOLVED -- that is "
        "OI-031's question, not this cell's; this cell's verdict does not depend on it.")
else:
    log("  no pure-Q candidate within the CRT modulus's reconstruction bound "
        "(modulus has ~150 digits; a real small rational would have been found "
        "trivially -- e3 is NOT a small/moderate rational)")

# ---------------------------------------------------------------------------
# STEP 2: THE DISCRIMINATING FACT -- the resolvent-norm identity, which needs
# e1, e2 ONLY (not e3). Prove it symbolically first (general cubic, sympy),
# then apply it to (a) the level-9 control (must reproduce the banked 9 exactly)
# and (b) the level-27/1215 triple, both raw (v) and 12-cleared (y).
# ---------------------------------------------------------------------------
r0, r1, r2, w = sp.symbols('r0 r1 r2 w')
E1 = r0 + r1 + r2
E2 = r0 * r1 + r1 * r2 + r2 * r0
L = r0 + w * r1 + w**2 * r2
Lbar = r0 + w**2 * r1 + w * r2  # = conj(L) when w -> 1/w and roots real
prod = sp.expand(L * Lbar)
# reduce using w^2 = -1-w (minimal poly of primitive cube root of unity)
prod_reduced = sp.expand(sp.rem(sp.Poly(prod, w), sp.Poly(w**2 + w + 1, w)).as_expr())
identity_check = sp.simplify(prod_reduced - (E1**2 - 3 * E2))
assert identity_check == 0, f"resolvent-norm identity FAILED symbolically: {identity_check}"
log("SYMBOLIC PROOF: (r0+w r1+w^2 r2)(r0+w^2 r1+w r2) = e1^2 - 3 e2 exactly "
    "(w^2+w+1=0 used; identity holds for ALL cyclic orderings since e1,e2 symmetric)")

# control: level-9 raw roots c_k = 2cos(2pi k/9), k in {1,2,4}, root of x^3-3x+1
x = sp.symbols('x')
level9_poly = sp.Poly(x**3 - 3 * x + 1, x)
e1_9, e2_9, e3_9 = (sp.Rational(0), sp.Rational(-3), sp.Rational(-1))  # x^3 - e1x^2+e2x-e3
norm9 = e1_9**2 - 3 * e2_9
log(f"CONTROL (level 9, x^3-3x+1): resolvent norm e1^2-3e2 = {norm9}  "
    f"(must equal the banked |12 L(chi_1)|^2 = 9 from B413) -> {'MATCH' if norm9 == 9 else 'MISMATCH -- STOP'}")
assert norm9 == 9, "control failed: level-9 identity does not reproduce the banked exact fact"

# level-27/1215 triple, RAW value v (root of t^3 - (1/48) t - e3): e1=0, e2=-1/48
e1_v, e2_v = sp.Rational(0), sp.Rational(-1, 48)
norm_v = e1_v**2 - 3 * e2_v
log(f"level-27/1215 triple, RAW tower value v: e1={e1_v}, e2={e2_v}  "
    f"=> resolvent norm |L(v)|^2 = e1^2-3e2 = {norm_v}")

# apply the SAME clearing transform as level 9: y = 12*v (forced -- verified next
# both symbolically and against the raw F_p data, not assumed)
t, y = sp.symbols('t y')
p_coef, q_coef = sp.Rational(-1, 48), sp.symbols('q')  # q_coef = -e3, kept symbolic
v_poly = t**3 + p_coef * t - q_coef  # t^3 - (1/48) t - e3   (q_coef stands for e3)
y_poly = sp.expand(sp.Poly(v_poly.subs(t, y / 12) * 12**3, y).as_expr())
log(f"clearing transform y=12v: 12^3*(t^3-(1/48)t-e3)|_{{t=y/12}} = {y_poly}")
# extract the coefficient of y (should be exactly -3, independent of e3)
y_poly_expanded = sp.Poly(y_poly, y)
coeff_y1 = y_poly_expanded.coeff_monomial(y)
coeff_y0 = y_poly_expanded.coeff_monomial(1)
log(f"  coefficient of y^1: {coeff_y1}  (compare level 9's x^3 -3x +1 coefficient -3)")
assert coeff_y1 == -3, "the clearing transform does NOT reproduce the level-9 '-3' -- STOP"
log(f"  coefficient of y^0 (constant term): {coeff_y0}  = -1728*e3 (e3 still unknown, unused below)")

e1_y, e2_y = sp.Rational(0), sp.Rational(-3)  # forced, e3-independent
norm_y = e1_y**2 - 3 * e2_y
log(f"level-27/1215 triple, 12-CLEARED value y=12v: e1={e1_y}, e2={e2_y}  "
    f"=> resolvent norm |L(y)|^2 = e1^2-3e2 = {norm_y}   "
    f"(this is the number directly comparable to level 9's exact 9 -- BOTH e3-independent)")

# ---------------------------------------------------------------------------
# STEP 2b: verify the y-cubic identity directly against the raw F_p data (not
# just symbolically) -- confirm y=12v really satisfies y^3-3y-(const) = 0 with
# the SAME constant across all 20 primes (this only re-checks internal
# consistency of e2(y)=-3; it does not require knowing e3 itself).
# ---------------------------------------------------------------------------
consts = set()
for p in primes:
    d = DATA[str(p)]
    for c in CELLS:
        v = int(d[str(c)]) % p
        y_ = (12 * v) % p
        const = (y_ ** 3 - 3 * y_) % p  # should equal 1728*e3 mod p, same for all 3 roots & all primes...
        # NOTE: 1728*e3 is the SAME constant for all three roots (it's -e3(y), a
        # symmetric function) -- check that y_i^3-3y_i is identical across the 3
        # roots at fixed p (that's the real per-prime check of e2(y)=-3 exactly).
        consts.add((p, const))
# group by prime, check the 3 roots agree
by_p = {}
for p, c in consts:
    by_p.setdefault(p, set()).add(c)
all_consistent = all(len(v) == 1 for v in by_p.values())
log(f"per-prime check: y_i^3 - 3y_i identical across the 3 roots (i.e. e2(y)=-3 exactly, "
    f"e3-independent) for all 20 primes: {all_consistent}")
assert all_consistent, "e2(y)=-3 check failed against raw data -- STOP"

# ---------------------------------------------------------------------------
# STEP 3: THE VERDICT -- compare against T1's registered prediction.
# ---------------------------------------------------------------------------
predicted = 3 ** 3  # t1_continuum.py: gauss_norm_at_level(3) = 3**3 = 27
computed = norm_y  # the like-for-like (12-cleared) exact resolvent norm
log("")
log("=== THE COMPARISON (T1's registered prediction vs the exact in-cell computation) ===")
log(f"  T1 registered prediction (t1_continuum.py gauss_norm_at_level(3)): |L|^2 = {predicted}")
log(f"  exact in-cell computation (12-cleared resolvent norm, e3-independent): |L|^2 = {computed}")
log(f"  level-9 anchor (recomputed as a control, same identity): |L|^2 = {norm9}")
verdict_confirmed = (computed == predicted)
log(f"  MATCH: {verdict_confirmed}")
if not verdict_confirmed:
    log(f"  DISCREPANCY: computed {computed} != predicted {predicted} "
        f"(computed EQUALS the level-9 value {norm9} instead -- the norm is FROZEN "
        f"at 9, not growing to 3^3=27; the '3^k growth' hypothesis in T1's script "
        f"is REFUTED by an exact rational computation, not a numeric near-miss)")

out = dict(
    primes_used=primes,
    e1_v="0", e2_v="-1/48",
    e1_y="0", e2_y="-3",
    resolvent_norm_raw_v=str(norm_v),
    resolvent_norm_cleared_y=str(norm_y),
    level9_control_norm=str(norm9),
    predicted_level27_norm=predicted,
    e3_small_integer_scan_hit=cand_hit,
    e3_pure_Q_reconstruction=str(e3_Q) if e3_Q is not None else None,
    verdict="RESOLVED-B (refuted)" if not verdict_confirmed else "RESOLVED-A (confirmed)",
    discriminating_fact=(
        f"exact resolvent norm |L|^2 = {computed} (e1={{0}}, e2={{-3}} on the "
        f"12-cleared level-27 triple, both e3-independent, symbolically proved "
        f"identity e1^2-3e2) vs the registered prediction 3^3={predicted}; the "
        f"computed value instead equals the level-9 anchor value {norm9} exactly "
        f"-- the norm freezes rather than growing as 3^k."
    ),
)
with open(os.path.join(HERE, "output.json"), "w") as fh:
    json.dump(out, fh, indent=1)
log("")
log("DONE. wrote output.json")
