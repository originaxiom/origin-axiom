#!/usr/bin/env python3
"""T9 — THE L154 KIND-MAP SURVEY (corpus-wide boundary-character search).

The typed instrument GC-6 named and never ran, at corpus scale.

KIND-MAP (six-condition acceptance gate, per B1034/B1216/P3 'The wall';
implemented here as five machine conditions K1..K5 + the provenance clause):

  (K-i)   GENUINE q-SERIES: a formal power series on an exponent grid
          alpha + Z_{>=0} with rational leading exponent alpha (the
          q^{h-c/24} prefactor slot). Objects with no formal q-expansion
          (numbers, growth rates, continuum integrals, finite Laurent
          polynomials) are NOT-COMPARABLE.
  (K-ii)  NON-NEGATIVE INTEGERS: after stripping q^alpha, every
          coefficient must be a non-negative integer (a character IS a
          graded-dimension count). First violation reported exactly.
  (K-iii) c = 6 EXACTLY, under the candidate's own normalization.
          CONVENTION (stated): a candidate supplies c only if its banked
          record names a chiral algebra / module with a stated central
          charge, or banks (h, c) such that alpha = h - c/24. If no c
          datum is banked, the condition is UNTYPED-FAIL (the candidate
          does not present itself as a character of anything).
  (K-iv)  CARDY GROWTH, SIX UNITS: log a_n ~ 2*pi*sqrt(c_eff * n / 6)
          with c_eff ~ 6 (six cusp-boson units), NOT ~ 1 (the one unit
          the banked T[4_1] supplies). Implemented as the sqrt-growth
          constant test: least-squares fit of
              log a_n = A*sqrt(n) + B*log(n) + C
          on the upper half of the available range, c_eff = 6 A^2/(4 pi^2).
          PASS band: c_eff in [4.5, 7.5] with >= 200 usable terms.
          ONE-UNIT band: [0.5, 1.6]. Below 0.2: ZERO units.
  (K-v)   ANTI-NUMEROLOGY: the series must be the object's own datum
          (constructed from m004 / its family data), not imported.
          Classified per entry from the banked provenance, documented.

MB12: every condition is exercised in BOTH directions by controls run in
this script (see CONTROLS section): a planted valid (E6)_1 vacuum
character, built here from the E6 root lattice via the A2^3 glue
decomposition (independently verified against direct 6-dim enumeration
and the root count 72), must PASS (i)-(iv); a random bounded non-negative
series must FAIL the growth test while PASSING non-negativity; the
one-boson character 1/eta (the T[4_1] cusp boson) must land in the
ONE-UNIT band, showing the 6-vs-1 clause discriminates.

Exact integer/Fraction arithmetic in every decisive step; floats only in
the growth-fit diagnostics (whose verdicts are banded, not knife-edge).

Gate 5: every number here is an internal invariant (lattice norms,
series coefficients, central charges of named modules). No measured SM
value anywhere.
"""

import json
import math
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))

OUT = []


def say(s=""):
    print(s, flush=True)
    OUT.append(str(s))


# ====================================================================
# series engine (dense lists over Z / Fraction, index = exponent step)
# ====================================================================

def smul(a, b, N):
    """product of two dense series truncated at index N."""
    c = [0] * (N + 1)
    for i, ai in enumerate(a):
        if i > N or ai == 0:
            continue
        lim = N - i
        for j, bj in enumerate(b):
            if j > lim:
                break
            if bj:
                c[i + j] += ai * bj
    return c


def spow(a, k, N):
    r = [1] + [0] * N
    base = list(a[: N + 1]) + [0] * max(0, N + 1 - len(a))
    while k:
        if k & 1:
            r = smul(r, base, N)
        base = smul(base, base, N)
        k >>= 1
    return r


def sinv(a, N):
    """inverse of a series with a[0] = 1."""
    assert a[0] == 1
    inv = [1] + [0] * N
    for n in range(1, N + 1):
        s = 0
        for k in range(1, min(n, len(a) - 1) + 1):
            if a[k]:
                s += a[k] * inv[n - k]
        inv[n] = -s
    return inv


def euler_qq(N):
    """(q;q)_inf = sum_k (-1)^k q^{k(3k-1)/2} (pentagonal), to q^N."""
    e = [0] * (N + 1)
    k = 0
    while True:
        done = True
        for kk in (k, -k) if k else (0,):
            ex = kk * (3 * kk - 1) // 2
            if ex <= N:
                e[ex] += (-1) ** abs(kk)
                done = False
        if k and done:
            break
        k += 1
    return e


def prod_one_minus(exponents_with_mult, N):
    """prod (1 - q^e)^m as dense series (m positive int)."""
    r = [1] + [0] * N
    for e, m in exponents_with_mult:
        for _ in range(m):
            # multiply by (1 - q^e)
            for i in range(N, e - 1, -1):
                r[i] -= r[i - e]
    return r


# ====================================================================
# the growth instrument (K-iv): sqrt-growth constant -> c_eff
# ====================================================================

def c_eff_fit(coeffs, label=""):
    """Fit log a_n = A sqrt(n) + B log n + C on the upper half of the
    positive-coefficient support; return (c_eff, n_used, A)."""
    pts = [(n, c) for n, c in enumerate(coeffs) if n >= 2 and c > 0]
    if len(pts) < 12:
        return None, len(pts), None
    n_hi = pts[-1][0]
    window = [(n, c) for n, c in pts if n >= n_hi // 2]
    if len(window) < 8:
        return None, len(window), None
    import numpy as np
    xs = np.array([float(n) for n, _ in window])
    ys = np.array([math.log(c) for _, c in window])
    M = np.column_stack([np.sqrt(xs), np.log(xs), np.ones_like(xs)])
    sol, *_ = np.linalg.lstsq(M, ys, rcond=None)
    A = float(sol[0])
    c_eff = 6.0 * A * A / (4.0 * math.pi ** 2) if A > 0 else 0.0
    return c_eff, len(pts), A


# ====================================================================
# the kind-map
# ====================================================================

SIX_LO, SIX_HI = 4.5, 7.5
ONE_LO, ONE_HI = 0.5, 1.6
MIN_TERMS_FOR_GROWTH_PASS = 200


def kind_map(entry):
    """entry: dict with keys
        name, location, coeffs (list of ints/Fractions, stripped),
        alpha (Fraction or None), stated_c (Fraction or None or 'named:<x>'),
        provenance ('object'|'imported'|'control'), notes.
    Returns verdict dict."""
    v = {"name": entry["name"], "conditions": {}}
    coeffs = entry["coeffs"]

    # K-i: genuine series with rational prefactor slot
    if coeffs is None:
        v["conditions"]["K-i"] = "FAIL (NOT-COMPARABLE: no formal q-expansion exists)"
        v["verdict"] = "NOT-COMPARABLE"
        return v
    ok_i = entry["alpha"] is not None and len(coeffs) >= 5
    v["conditions"]["K-i"] = (
        f"PASS (series on q^({entry['alpha']}) + Z_>=0 grid, {len(coeffs)} terms)"
        if ok_i else
        "FAIL (no rational prefactor exponent banked / too few computable terms)"
    )

    # K-ii: non-negative integers after stripping
    ok_ii = True
    first_bad = None
    for n, c in enumerate(coeffs):
        if isinstance(c, Fr) and c.denominator != 1:
            ok_ii, first_bad = False, (n, c, "non-integer")
            break
        if c < 0:
            ok_ii, first_bad = False, (n, c, "negative")
            break
    v["conditions"]["K-ii"] = (
        f"PASS (all {len(coeffs)} stripped coefficients non-negative integers)"
        if ok_ii else
        f"FAIL at n={first_bad[0]}: coefficient {first_bad[1]} ({first_bad[2]})"
    )

    # K-iii: c = 6 exactly under the candidate's own normalization
    c_datum = entry["stated_c"]
    if c_datum is None:
        v["conditions"]["K-iii"] = ("UNTYPED-FAIL (no central-charge datum banked "
                                    "with the candidate: it does not present itself "
                                    "as a character of any chiral algebra)")
        ok_iii = False
    else:
        ok_iii = (c_datum == 6)
        v["conditions"]["K-iii"] = (f"PASS (banked c = {c_datum} = 6 exactly)" if ok_iii
                                    else f"FAIL (banked c = {c_datum} != 6)")

    # K-iv: Cardy growth, six units
    if not ok_ii:
        c_eff, n_used, A = c_eff_fit([abs(int(c)) if not isinstance(c, Fr) else 0
                                      for c in coeffs])
        tag = (f" [diagnostic on |a_n|: c_eff ~= {c_eff:.3f} from {n_used} terms]"
               if c_eff is not None else "")
        v["conditions"]["K-iv"] = "MOOT (K-ii already fails; growth of a signed series is not a character growth)" + tag
        ok_iv = False
    else:
        c_eff, n_used, A = c_eff_fit(coeffs)
        if c_eff is None:
            v["conditions"]["K-iv"] = (f"FAIL (UNDERPOWERED: only {n_used} usable terms; "
                                       "cannot exhibit six-unit Cardy growth)")
            ok_iv = False
        elif n_used < MIN_TERMS_FOR_GROWTH_PASS:
            band = "SIX-UNIT" if SIX_LO <= c_eff <= SIX_HI else "not six-unit"
            v["conditions"]["K-iv"] = (f"FAIL (UNDERPOWERED: {n_used} terms < "
                                       f"{MIN_TERMS_FOR_GROWTH_PASS}; c_eff ~= {c_eff:.3f}, {band})")
            ok_iv = False
        else:
            if SIX_LO <= c_eff <= SIX_HI:
                v["conditions"]["K-iv"] = (f"PASS (c_eff ~= {c_eff:.3f} in six-unit band "
                                           f"[{SIX_LO},{SIX_HI}]; {n_used} terms; sqrt-const A={A:.4f} "
                                           f"vs 2*pi={2*math.pi:.4f})")
                ok_iv = True
            elif ONE_LO <= c_eff <= ONE_HI:
                v["conditions"]["K-iv"] = (f"FAIL (c_eff ~= {c_eff:.3f}: ONE cusp-boson unit, "
                                           "the T[4_1] value — the Cardy 6-vs-1 clause bites)")
                ok_iv = False
            else:
                v["conditions"]["K-iv"] = (f"FAIL (c_eff ~= {c_eff:.3f}: neither six units nor one)")
                ok_iv = False

    # K-v: anti-numerology / provenance
    prov = entry["provenance"]
    if prov == "object":
        v["conditions"]["K-v"] = "PASS (object-side: constructed from m004/its family data)"
        ok_v = True
    elif prov == "control":
        v["conditions"]["K-v"] = "N/A (planted control; clause stipulated for machinery test)"
        ok_v = True
    else:
        v["conditions"]["K-v"] = ("FAIL (IMPORTED: constructed from external data — "
                                  "a model whose central charge happens to fit is the "
                                  "anti-numerology clause's exact target)")
        ok_v = False

    v["verdict"] = "PASS" if (ok_i and ok_ii and ok_iii and ok_iv and ok_v) else "FAIL"
    v["first_failed"] = None if v["verdict"] == "PASS" else next(
        k for k, s in v["conditions"].items()
        if s.startswith(("FAIL", "UNTYPED", "MOOT")))
    return v


def report(v, entry):
    say(f"--- {entry['name']}")
    say(f"    location: {entry['location']}")
    if entry.get("notes"):
        say(f"    notes: {entry['notes']}")
    for k, s in v["conditions"].items():
        say(f"    {k}: {s}")
    say(f"    VERDICT: {v['verdict']}"
        + (f" (first failed: {v['first_failed']})" if v.get("first_failed") else ""))
    say("")


# ====================================================================
# SECTION 1 — construct the census entries with computable coefficients
# ====================================================================

say("=" * 74)
say("T9 KIND-MAP SURVEY — construction of computable census entries")
say("=" * 74)

N672 = 400  # terms for the B672 reconstruction

# ---- Rogers-Ramanujan G, H via the product identities (exact) --------
def rr_products(N):
    # G = 1/((q;q^5)(q^4;q^5)),  H = 1/((q^2;q^5)(q^3;q^5))
    gden = prod_one_minus([(e, 1) for e in range(1, N + 1) if e % 5 in (1, 4)], N)
    hden = prod_one_minus([(e, 1) for e in range(1, N + 1) if e % 5 in (2, 3)], N)
    return sinv(gden, N), sinv(hden, N)

G, H = rr_products(N672)
assert G[:8] == [1, 1, 1, 1, 2, 2, 3, 3], "RR G sanity failed"
assert H[:8] == [1, 0, 1, 1, 1, 1, 2, 2], "RR H sanity failed"
say("[build] Rogers-Ramanujan G, H built from product identities "
    f"({N672 + 1} terms; leading terms verified: G={G[:6]}, H={H[:6]})")

QQ = euler_qq(N672)
comp1_2hat = smul(G, spow(QQ, 10, N672), N672)   # (q;q)G * (q;q)^9 = G*(q;q)^10
comp2_2hat = smul(H, spow(QQ, 10, N672), N672)

# cross-check against the banked B666/cellW33 machine-readable streams
w33_path = os.path.join(REPO, "frontier", "B666_leads_campaign", "cellW33",
                        "cellW33_doublet_streams.json")
with open(w33_path) as f:
    W33 = json.load(f)
banked_2hat_c1 = [int(x) for x in W33["doublet_streams_integer"]["2hat.comp1"]]
banked_2hat_c2 = [int(x) for x in W33["doublet_streams_integer"]["2hat.comp2"]]
m1 = comp1_2hat[: len(banked_2hat_c1)] == banked_2hat_c1
m2 = comp2_2hat[: len(banked_2hat_c2)] == banked_2hat_c2
say(f"[gate] fresh reconstruction vs banked B666/cellW33 integer streams: "
    f"comp1 {len(banked_2hat_c1)}/{len(banked_2hat_c1)} match = {m1}; "
    f"comp2 {len(banked_2hat_c2)}/{len(banked_2hat_c2)} match = {m2}")
assert m1 and m2, "reconstruction does not match the banked doublet streams"

banked_2hatp_c1 = [int(x) for x in W33["doublet_streams_integer"]["2hat'.comp1"]]
banked_2hatp_c2 = [int(x) for x in W33["doublet_streams_integer"]["2hat'.comp2"]]
sextet = {k: [int(x) for x in v] for k, v in W33["sextet_rows"].items()}
F1_stream = [Fr(x) for x in W33["F1_stream"]]
F2_stream = [Fr(x) for x in W33["F2_stream"]]

# ---- B724 GGM rotated 3D-index of 4_1 (banked coefficients) ----------
idx3d = [1, -8, -9, 18, 46, 90]   # FINDINGS.md row 'Path 1 GGM', arXiv:2007.10190 eq (80)

# ---- B364/B365 theta families of the fiber torus ---------------------
def partial_theta(residues, Efun, modulus, nmax, denom):
    """sum over n = -nmax..nmax with n mod modulus in residues of q^{E(n)};
    returns dense coefficient list on the q^{1/denom} grid + alpha (Fraction)."""
    from collections import defaultdict
    acc = defaultdict(int)
    for n in range(-nmax, nmax + 1):
        if n % modulus in residues:
            e = Efun(n)          # Fraction
            acc[e] += 1
    exps = sorted(acc)
    alpha = exps[0]
    top = max(exps)
    steps = int((top - alpha) * denom)
    dense = [0] * (steps + 1)
    for e, c in acc.items():
        dense[int((e - alpha) * denom)] += c
    return dense, alpha

E_tri = lambda n: Fr(n * (n - 1), 30)      # B364 triangular family
E_sq = lambda n: Fr(n * n, 15)             # B364 square family
theta_tri_j1, a_tri = partial_theta({1}, E_tri, 15, 160, 30)
theta_sq_j1, a_sq = partial_theta({1}, E_sq, 15, 120, 15)
say(f"[build] B364 theta slices built: triangular j=1 ({len(theta_tri_j1)} grid terms, "
    f"alpha={a_tri}), square j=1 ({len(theta_sq_j1)} grid terms, alpha={a_sq})")

# ====================================================================
# SECTION 2 — the planted controls
# ====================================================================
say("")
say("=" * 74)
say("CONTROLS (MB12: the gate must be failable both ways, and is)")
say("=" * 74)

NE6 = 600

# ---- (E6)_1 vacuum character, built HERE from the E6 root lattice ----
# Step (a): E6 root count from the Cartan matrix (simply-laced: Gram = Cartan).
import numpy as np

# E6 Dynkin diagram: chain 1-2-3-4-5 with node 6 attached to node 3
# (arm lengths 2,2,1 from the branch node = T(3,3,2) = E6).
CARTAN_E6 = np.array([
    [2, -1, 0, 0, 0, 0],
    [-1, 2, -1, 0, 0, 0],
    [0, -1, 2, -1, 0, -1],
    [0, 0, -1, 2, -1, 0],
    [0, 0, 0, -1, 2, 0],
    [0, 0, -1, 0, 0, 2],
], dtype=np.int64)
assert (CARTAN_E6 == CARTAN_E6.T).all()
assert all(np.linalg.det(CARTAN_E6[:k, :k].astype(float)) > 0
           for k in range(1, 7)), "Cartan matrix not positive definite"

# direct enumeration with a SATURATION check: counts for norm m are
# trusted only where boxes +-5 and +-6 agree (no vector of that norm has
# a root-basis coefficient beyond the smaller box).
def norm_counts(box, max_norm):
    rng = list(range(-box, box + 1))
    sub = np.array(np.meshgrid(*[rng] * 5, indexing="ij")).reshape(5, -1).T
    total = np.zeros(max_norm + 1, dtype=np.int64)
    for c0 in rng:   # chunk over the first coordinate (memory-safe at box 6)
        grid = np.column_stack([np.full(len(sub), c0, dtype=np.int64), sub])
        norms = np.einsum("ij,jk,ik->i", grid, CARTAN_E6, grid)
        assert (norms >= 0).all()
        total += np.bincount(norms[norms <= max_norm], minlength=max_norm + 1)
    assert total[0] == 1 and total[1] == 0
    return total

cnt6 = norm_counts(6, 16)
cnt7 = norm_counts(7, 16)
sat = 0
while sat + 2 <= 16 and (cnt6[: sat + 3] == cnt7[: sat + 3]).all():
    sat += 2
say(f"[E6 direct] saturation: boxes +-6 and +-7 agree on norms 0..{sat} "
    "(the inverse-Cartan diagonal reaches 6, so small boxes clip long vectors; "
    "only saturated norms are trusted)")
count_roots = int(cnt7[2])
count_norm4 = int(cnt7[4])
say(f"[E6 direct] norm-2 vectors = {count_roots} (E6 root count, expect 72); "
    f"norm-4 vectors = {count_norm4} (expect 270)")
assert count_roots == 72
q_trust = sat // 2
theta_direct = np.array([cnt7[2 * n] for n in range(q_trust + 1)])
say(f"[E6 direct] theta to q^{q_trust} (saturated): {theta_direct.tolist()}")

# Step (b): A2^3 + glue construction (glue code {(000),(111),(222)})
def a2_class_thetas(N3):
    """theta of A2* classes k=0,1,2; exponents (a^2+ab+b^2)/3 as dense lists
    on the q^{1/3} grid up to exponent N3 (in units of 1/3): index = 3*exponent."""
    R = int(math.isqrt(3 * N3)) + 3
    th = [[0] * (N3 + 1) for _ in range(3)]
    for a in range(-R, R + 1):
        for b in range(-R, R + 1):
            m = a * a + a * b + b * b     # = 3*exponent
            if m <= N3:
                th[(a - b) % 3][m] += 1
    return th

N3 = 3 * NE6
th0, th1, th2 = a2_class_thetas(N3)
assert th1 == th2, "class 1 and 2 thetas must agree (negation symmetry)"

def cube_on_grid(t, N3):
    t2 = smul(t, t, N3)
    return smul(t2, t, N3)

theta_E6_grid = [x + 2 * y for x, y in zip(cube_on_grid(th0, N3), cube_on_grid(th1, N3))]
# integrality of the grid: nonzero only at multiples of 3 (integer exponents)
assert all(c == 0 for i, c in enumerate(theta_E6_grid) if i % 3 != 0), \
    "E6 glue construction produced non-integer exponents"
theta_E6 = [theta_E6_grid[3 * n] for n in range(NE6 + 1)]
say(f"[E6 glue] A2^3 + glue {{(0,0,0),(1,1,1),(2,2,2)}}: theta to q^{q_trust} = "
    f"{theta_E6[:q_trust + 1]}")
assert theta_E6[: q_trust + 1] == theta_direct.tolist(), \
    "glue construction disagrees with direct enumeration"
say(f"[gate] E6 theta: glue construction == direct enumeration on q^0..q^{q_trust}; "
    f"extended exactly to q^{NE6}")

# chi_vac = q^{-1/4} * Theta_E6(q) / (q;q)^6   (h=0, c=6 -> alpha = -1/4)
qq6_inv = sinv(spow(euler_qq(NE6), 6, NE6), NE6)
chi_e6_vac = smul(theta_E6, qq6_inv, NE6)
say(f"[build] (E6)_1 vacuum character stripped series, first 8 terms: {chi_e6_vac[:8]}")
assert chi_e6_vac[0] == 1 and chi_e6_vac[1] == 78, "level-1 vacuum q^1 grade must be dim E6 = 78"
say("[gate] chi q^1 coefficient = 78 = dim E6 (level-1 vacuum grade-1 space is the adjoint): PASS")
assert all(c >= 0 for c in chi_e6_vac)

# ---- one-boson comparator: 1/(q;q) (the T[4_1] single cusp boson) ----
one_boson = sinv(euler_qq(NE6), NE6)     # p(n)

# ---- random bounded non-negative series (seeded) ---------------------
import random
random.seed(20260901)
rand_series = [1] + [random.randint(0, 9) for _ in range(NE6)]

controls = [
    dict(name="CONTROL PLANT-VALID: (E6)_1 vacuum character  chi_0 = q^{-1/4} Theta_E6/(q;q)^6",
         location="constructed in this script from the E6 root lattice "
                  "(A2^3 glue; verified vs direct enumeration + root count 72)",
         coeffs=chi_e6_vac, alpha=Fr(-1, 4), stated_c=Fr(6),
         provenance="control",
         notes="the unique named target of B1228 (K1): (E6)_1 vacuum module, c=6; "
               "must PASS (i)-(iv) or the gate is broken"),
    dict(name="CONTROL 6-vs-1: single cusp boson  1/(q;q) (T[4_1]'s one unit)",
         location="constructed in this script (Euler product inverse)",
         coeffs=one_boson, alpha=Fr(-1, 24), stated_c=Fr(6),
         provenance="control",
         notes="c stipulated 6 to isolate the GROWTH clause: must FAIL K-iv "
               "in the ONE-UNIT band, proving the 6-vs-1 clause discriminates"),
    dict(name="CONTROL PLANT-INVALID: random bounded non-negative integer series",
         location="constructed in this script (seed 20260901, coefficients 0..9)",
         coeffs=rand_series, alpha=Fr(0), stated_c=Fr(6),
         provenance="control",
         notes="passes K-ii by construction; must FAIL the growth test K-iv"),
]

control_verdicts = []
for e in controls:
    v = kind_map(e)
    control_verdicts.append(v)
    report(v, e)

pv, p1, pr = control_verdicts
bite_ok = (
    pv["verdict"] == "PASS"
    and p1["verdict"] == "FAIL" and "ONE cusp-boson unit" in p1["conditions"]["K-iv"]
    and pr["verdict"] == "FAIL" and pr["first_failed"] == "K-iv"
    and pr["conditions"]["K-ii"].startswith("PASS")
)
say(f"[BITE] plant-valid PASSES: {pv['verdict'] == 'PASS'}; "
    f"one-boson fails in ONE-UNIT band: {'ONE cusp-boson unit' in p1['conditions']['K-iv']}; "
    f"random series passes K-ii but fails K-iv: "
    f"{pr['conditions']['K-ii'].startswith('PASS') and pr['first_failed'] == 'K-iv'}")
say(f"[BITE] ALL CONTROLS BITE: {bite_ok}")
if not bite_ok:
    say("!! CONTROL FAILURE — the instrument is not armed; survey verdicts void")

# ====================================================================
# SECTION 3 — the census, run through the kind-map
# ====================================================================
say("")
say("=" * 74)
say("THE CENSUS, RUN (series with computable coefficients)")
say("=" * 74)

census = [
    dict(name="B672/B666 Y^(5)_2hat.comp1 = q^{2/5} (q;q)G(q) (q;q)^9",
         location="frontier/B672_grading_hunt/FINDINGS.md; banked streams "
                  "frontier/B666_leads_campaign/cellW33/cellW33_doublet_streams.json",
         coeffs=comp1_2hat, alpha=Fr(2, 5), stated_c=None,
         provenance="object",
         notes="reconstructed here from the RR product identities, 60/60 match "
               "to the banked stream, extended to 400 terms; no c datum banked "
               "(the Lee-Yang reading in GC-12 matches only the leading exponent)"),
    dict(name="B672/B666 Y^(5)_2hat.comp2 = q^{3/5} (q;q)H(q) (q;q)^9",
         location="frontier/B672_grading_hunt/FINDINGS.md; B666 cellW33 JSON",
         coeffs=comp2_2hat, alpha=Fr(3, 5), stated_c=None,
         provenance="object", notes="same construction, second component"),
    dict(name="B672/B666 Y^(5)_2hat'.comp1 (eta^{24/5} quintic in F1,F2)",
         location="frontier/B666_leads_campaign/cellW33/cellW33_doublet_streams.json "
                  "(doublet_streams_integer, 60 banked terms)",
         coeffs=banked_2hatp_c1, alpha=Fr(1, 5), stated_c=None,
         provenance="object", notes="banked integer stream used as-is"),
    dict(name="B672/B666 Y^(5)_2hat'.comp2 (eta^{24/5} quintic in F1,F2)",
         location="same JSON (60 banked terms)",
         coeffs=banked_2hatp_c2, alpha=Fr(4, 5), stated_c=None,
         provenance="object", notes="banked integer stream used as-is"),
    dict(name="B666 F1 stream (rational modular-flavor stream)",
         location="same JSON (F1_stream, 42 banked terms)",
         coeffs=F1_stream, alpha=Fr(0), stated_c=None,
         provenance="object", notes="denominators are pure 5-powers (banked note)"),
    dict(name="B666 F2 stream (rational modular-flavor stream)",
         location="same JSON (F2_stream, 42 banked terms)",
         coeffs=F2_stream, alpha=Fr(0), stated_c=None,
         provenance="object", notes="same"),
    dict(name="B724 GGM rotated 3D-index of 4_1: 1 - 8q - 9q^2 + 18q^3 + 46q^4 + 90q^5",
         location="frontier/B724_seeing_readjudication/FINDINGS.md (Path 1 GGM row; "
                  "recomputed there from arXiv:2007.10190 eq (80))",
         coeffs=idx3d, alpha=Fr(0), stated_c=None,
         provenance="object",
         notes="a GENUINE object-side q-series GC-12's keyword sweep missed "
               "(token '3D-index'); the 3D index is defined from m004's own "
               "ideal triangulation"),
    dict(name="B364 triangular theta family f_1(0,tau), E(n)=n(n-1)/30, n=1 mod 15",
         location="frontier/B364_theta_polarization/FINDINGS.md (the seam-bearing "
                  "theta class); coefficients computed here on the q^{1/30} grid",
         coeffs=theta_tri_j1, alpha=a_tri, stated_c=None,
         provenance="object",
         notes="fiber-torus theta: object-side, unit coefficients (a second "
               "series class the GC-12 sweep missed)"),
    dict(name="B364 square theta family, E'(n)=n^2/15, n=1 mod 15",
         location="frontier/B364_theta_polarization/FINDINGS.md (the canonical-lift "
                  "class); coefficients computed here on the q^{1/15} grid",
         coeffs=theta_sq_j1, alpha=a_sq, stated_c=None,
         provenance="object", notes="same family, integral polarization"),
    dict(name="B1190 (E6)_1 characters as corpus artifacts (Theta_E6/eta^6, vacuum)",
         location="frontier/B1190_close_loop_batch2/verification/gc6_l154_bridge.py "
                  "(computed there from the E6 root lattice; committed corpus artifact)",
         coeffs=chi_e6_vac, alpha=Fr(-1, 4), stated_c=Fr(6),
         provenance="imported",
         notes="the STAGE-side character: passes (i)-(iv) but it is built from the "
               "E6 root lattice, not from m004 data — B1228's open identification "
               "(nominated type vs geometric connection) is exactly whether this "
               "importation can ever be discharged; until then K-v fails"),
]

# sextet rows (banked 20-term streams; normalization/prefactor untyped)
for k, row in sextet.items():
    census.append(dict(
        name=f"B666 sextet {k}",
        location="frontier/B666_leads_campaign/cellW33/cellW33_doublet_streams.json "
                 "(sextet_rows, 20 banked terms)",
        coeffs=row, alpha=Fr(0), stated_c=None,
        provenance="object",
        notes="weight-1 stream; prefactor normalization untyped in the bank"))

results = []
for e in census:
    v = kind_map(e)
    results.append(v)
    report(v, e)

# NOT-COMPARABLE classes (no formal q-expansion exists): recorded for the
# census; kind_map returns NOT-COMPARABLE via coeffs=None.
not_comparable = [
    ("B441 WRT invariants tau_r(4_1(5,1))",
     "frontier/B441_child_wrt/FINDINGS.md",
     "per-r algebraic numbers in Q(zeta_4r); no formal q-variable"),
    ("B384/B1116/B246 Kashaev <4_1>_N / J_N tower",
     "frontier/B384_kashaev_bridge/, B1116_asymptotic_channel/",
     "N-indexed algebraic numbers at roots of unity + a growth rate (-> Vol); "
     "the Habiro sum does not converge as a formal power series"),
    ("B685/B800/B839 Habiro/GSWZ element Phi(h)Phi(-h)",
     "frontier/B800_habiro_integrality/FINDINGS.md",
     "perturbative hbar-expansion around the hyperbolic saddle; content is "
     "3-adic valuation of denominators; no graded character structure"),
    ("B1090 Andersen-Kashaev state integral",
     "frontier/B1090_partition_bridge/FINDINGS.md",
     "continuum Faddeev quantum-dilogarithm integral over b; no q-expansion"),
    ("B240 golden colored-Jones values [N] J_N(4_1; e^{2pi i/5})",
     "frontier/B240_golden_jones_integrality/FINDINGS.md",
     "a 4-number evaluation table at one root of unity"),
    ("B205 generic-q skein tower (quantum trace map, R_q^m L_q^m)",
     "frontier/B205_metallic_quantum_trace_map/FINDINGS.md",
     "finite Laurent polynomials in q per word; no infinite graded expansion "
     "(B672 candidate C1, dead there with exact first mismatches)"),
    ("B737/B754 zeta-quotient spectral identities",
     "frontier/B737_candidate_zero/, B754_p2_spectral/",
     "Selberg-type zeta data; no q-series"),
    ("B492 Verlinde fusion / boundary entropy",
     "frontier/B492_verlinde_boundary_lens/FINDINGS.md",
     "fusion integers and quantum dimensions; no graded expansion"),
    ("B646/B1212 finite character tables (rho(A1) sectors; lepton character ledger)",
     "frontier/B646_wave2_integration/.../n1_character.py; "
     "frontier/B1212_two_replies/verification/",
     "finite-group / finite-module character values; not q-graded"),
    ("B762 self-naming Hecke palette {1,2,8}; B854/B866 E6 centralizer cubics",
     "frontier/B762*/, B854*/, B866*/",
     "discrete invariant tuples and Lie-bracket computations; no q-series "
     "(GC-12 already corrected this false lead)"),
]

say("")
say("NOT-COMPARABLE census entries (no formal q-expansion; kind-map K-i fails):")
for name, loc, why in not_comparable:
    say(f"  - {name}")
    say(f"      at {loc}")
    say(f"      why: {why}")

# ====================================================================
# SECTION 4 — the tally
# ====================================================================
say("")
say("=" * 74)
say("TALLY")
say("=" * 74)
n_pass = sum(1 for v in results if v["verdict"] == "PASS")
say(f"census entries with computable coefficients: {len(results)}")
say(f"NOT-COMPARABLE classes: {len(not_comparable)}")
say(f"kind-map PASSES among census entries: {n_pass}")
for v in results:
    say(f"  {v['verdict']:>4}  {v['name'][:80]}"
        + (f"  [{v['first_failed']}]" if v.get('first_failed') else ""))
say("")
say(f"controls armed and biting: {bite_ok}")
say(f"CANDIDATE-FOUND: {'YES' if n_pass > 0 else 'NO'}")

# persist
out = {
    "controls": control_verdicts,
    "census": results,
    "not_comparable": [dict(name=n, location=l, reason=w) for n, l, w in not_comparable],
    "bite_ok": bite_ok,
    "n_pass": n_pass,
}
def jsonable(x):
    if isinstance(x, Fr):
        return str(x)
    if isinstance(x, dict):
        return {k: jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    return x

with open(os.path.join(HERE, "survey_results.json"), "w") as f:
    json.dump(jsonable(out), f, indent=1)
with open(os.path.join(HERE, "survey_output.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
say("\n[saved] survey_results.json, survey_output.txt")
