#!/usr/bin/env python3
"""G4 SUPPLEMENTARY CENSUS RUN — census-completeness verification of T9.

An INDEPENDENT sweep (different search patterns: Molien / Hilbert series /
Poincare series / 'character of' / eta( / numeric-signature greps over
verification data files) found series-like objects with computable
coefficients that CENSUS.md's 16 entries do not list. Per the verification
mandate, every such find is run through T9's own kind-map machinery here,
WITHOUT editing the committed script or its entries: this file exec's the
machinery head of kind_map_survey.py (series engine + c_eff_fit + kind_map
+ report), re-arms the three bite controls in-run, and adjudicates the
supplementary entries. Outputs: supplementary_output.txt,
supplementary_results.json (this cell dir only).

Also performs the mandated INDEPENDENT check of the planted (E6)_1
character's first coefficients (1, 78, 729, 4382, ...) against a direct
construction (fresh 6-dim lattice enumeration with saturation control,
written here, not copied from the committed cell).

Gate 5: every number is a lattice norm, series coefficient, group order,
or stated central charge of a named module. No measured SM values.
"""

import json
import math
import os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))

# ------------------------------------------------------------------
# load T9's machinery WITHOUT executing its survey (exec the head only,
# up to the SECTION 1 marker); nothing committed is modified.
# ------------------------------------------------------------------
_src = open(os.path.join(HERE, "kind_map_survey.py")).read()
_marker = "# SECTION 1"
_head = _src[: _src.index(_marker)]
_ns = {"__file__": os.path.join(HERE, "kind_map_survey.py"), "__name__": "t9head"}
exec(compile(_head, "kind_map_survey.py[head]", "exec"), _ns)

kind_map = _ns["kind_map"]
report = _ns["report"]
say = _ns["say"]
OUT = _ns["OUT"]
smul = _ns["smul"]
spow = _ns["spow"]
sinv = _ns["sinv"]
euler_qq = _ns["euler_qq"]
prod_one_minus = _ns["prod_one_minus"]
c_eff_fit = _ns["c_eff_fit"]

say("=" * 74)
say("G4 SUPPLEMENTARY CENSUS RUN — entries the independent sweep found")
say("=" * 74)

# ==================================================================
# PART A — independent (E6)_1 first-coefficient check
# ==================================================================
say("")
say("PART A: independent (E6)_1 planted-character check")
say("-" * 74)

import numpy as np

# My own E6 Cartan labeling (chain 1-2-3-4-5, branch node 6 on node 3);
# simply-laced, so Gram of the root lattice = Cartan matrix.
C6 = np.array([
    [2, -1, 0, 0, 0, 0],
    [-1, 2, -1, 0, 0, 0],
    [0, -1, 2, -1, 0, -1],
    [0, 0, -1, 2, -1, 0],
    [0, 0, 0, -1, 2, 0],
    [0, 0, -1, 0, 0, 2]], dtype=np.int64)
assert (C6 == C6.T).all()
for k in range(1, 7):
    assert np.linalg.det(C6[:k, :k].astype(float)) > 0.5

def theta_counts(box, max_norm):
    """norm counts of the E6 root lattice in root-basis box [-box, box]^6."""
    rng = np.arange(-box, box + 1, dtype=np.int64)
    sub = np.stack(np.meshgrid(*[rng] * 5, indexing="ij"), -1).reshape(-1, 5)
    tot = np.zeros(max_norm + 1, dtype=np.int64)
    for c0 in rng:
        v = np.column_stack([np.full(len(sub), c0, dtype=np.int64), sub])
        norms = np.einsum("ij,jk,ik->i", v, C6, v)
        assert (norms >= 0).all()
        tot += np.bincount(norms[norms <= max_norm], minlength=max_norm + 1)
    return tot

t5 = theta_counts(6, 12)
t6 = theta_counts(7, 12)
sat = -1
for m in range(13):
    if t5[m] != t6[m]:
        break
    sat = m
say(f"[A] direct enumeration: boxes +-6/+-7 agree on norms 0..{sat} (saturation)")
assert sat >= 8, "need norms through 8 for chi to q^4"
theta_direct = [int(t6[2 * n]) for n in range(sat // 2 + 1)]
say(f"[A] Theta_E6 direct (independent code): {theta_direct}")
assert theta_direct[:5] == [1, 72, 270, 720, 936], "theta head mismatch"

# character chi = Theta/(q;q)^6, computed with MY OWN convolution (not the
# committed cell's): chi_n = sum_k theta_k * p6(n-k), p6 = 1/(q;q)^6.
Ncheck = sat // 2
p6 = sinv(spow(euler_qq(Ncheck), 6, Ncheck), Ncheck)
chi_head = [sum(theta_direct[k] * p6[n - k] for k in range(n + 1))
            for n in range(Ncheck + 1)]
say(f"[A] chi head from direct theta: {chi_head}")
assert chi_head[:5] == [1, 78, 729, 4382, 19917], \
    "planted (E6)_1 first coefficients FAIL the direct-construction check"
say("[A] PASS: planted character head (1, 78, 729, 4382, 19917) confirmed "
    "against a fresh direct lattice construction")
# independent rep-theoretic anchors: 78 = dim E6; 729 = 3^6 is the banked
# grade-2 count and matches 270 + 72*6 + 27 (theta*1/(q;q)^6 by hand).
assert chi_head[2] == 270 + 72 * 6 + 27 == 729

# extension for the control plant: A2^3 + glue {000,111,222}, written fresh
NE6 = 600
N3 = 3 * NE6
R = int(math.isqrt(3 * N3)) + 3
th = [[0] * (N3 + 1) for _ in range(3)]
for a in range(-R, R + 1):
    for b in range(-R, R + 1):
        m = a * a + a * b + b * b
        if m <= N3:
            th[(a - b) % 3][m] += 1
assert th[1] == th[2]
c0 = smul(smul(th[0], th[0], N3), th[0], N3)
c1 = smul(smul(th[1], th[1], N3), th[1], N3)
grid = [x + 2 * y for x, y in zip(c0, c1)]
assert all(v == 0 for i, v in enumerate(grid) if i % 3)
theta_E6 = [grid[3 * n] for n in range(NE6 + 1)]
assert theta_E6[: len(theta_direct)] == theta_direct, "glue != direct enumeration"
p6_full = sinv(spow(euler_qq(NE6), 6, NE6), NE6)
chi_e6 = smul(theta_E6, p6_full, NE6)
assert chi_e6[: Ncheck + 1] == chi_head

# ==================================================================
# PART B — re-arm the bite controls IN THIS RUN (MB12)
# ==================================================================
say("")
say("PART B: bite controls re-armed in this supplementary run")
say("-" * 74)
one_boson = sinv(euler_qq(NE6), NE6)
import random
random.seed(20260901)
rand_series = [1] + [random.randint(0, 9) for _ in range(NE6)]

controls = [
    dict(name="CTRL plant-valid: (E6)_1 vacuum character (independent build)",
         location="constructed in this script (fresh enumeration + fresh glue)",
         coeffs=chi_e6, alpha=Fr(-1, 4), stated_c=Fr(6), provenance="control",
         notes="must PASS K-i..K-iv or this run's verdicts are void"),
    dict(name="CTRL 6-vs-1: one cusp boson 1/(q;q)",
         location="constructed in this script", coeffs=one_boson,
         alpha=Fr(-1, 24), stated_c=Fr(6), provenance="control",
         notes="must FAIL K-iv in the ONE-UNIT band"),
    dict(name="CTRL plant-invalid: seeded random non-negative series",
         location="constructed in this script (seed 20260901)",
         coeffs=rand_series, alpha=Fr(0), stated_c=Fr(6), provenance="control",
         notes="must PASS K-ii and FAIL K-iv"),
]
cv = []
for e in controls:
    v = kind_map(e)
    cv.append(v)
    report(v, e)
bite_ok = (cv[0]["verdict"] == "PASS"
           and cv[1]["verdict"] == "FAIL"
           and "ONE cusp-boson unit" in cv[1]["conditions"]["K-iv"]
           and cv[2]["verdict"] == "FAIL" and cv[2]["first_failed"] == "K-iv"
           and cv[2]["conditions"]["K-ii"].startswith("PASS"))
say(f"[BITE] controls bite in this run: {bite_ok}")
assert bite_ok

# ==================================================================
# PART C — the supplementary census entries (the sweep's finds)
# ==================================================================
say("")
say("PART C: supplementary entries (missed by CENSUS.md), adjudicated")
say("-" * 74)

NSER = 360

# ---- C1/C2: Lee-Yang/(2,5) minimal-model characters (B677 g1_tube) ----
# chi_1 = q^{...} G(q), chi_tau = q^{...} H(q); banked with stated c
# (YL convention c=-22/5; FIB convention c=14/5) in g1_run_log.txt.
gden = prod_one_minus([(e, 1) for e in range(1, NSER + 1) if e % 5 in (1, 4)], NSER)
hden = prod_one_minus([(e, 1) for e in range(1, NSER + 1) if e % 5 in (2, 3)], NSER)
G = sinv(gden, NSER)
H = sinv(hden, NSER)
assert G[:8] == [1, 1, 1, 1, 2, 2, 3, 3] and H[:8] == [1, 0, 1, 1, 1, 1, 2, 2]

# ---- C3/C4: B674 w2_step3 Molien doublet avatars (banked JSON) --------
w2 = json.load(open(os.path.join(
    REPO, "frontier", "B674_generation_leg", "w2_step3",
    "coefficients_both_conjugates.json")))
M = [(Fr(a), Fr(b)) for a, b in w2["M_coefficients"]]        # a + b*sqrt5
Mc = [(Fr(a), Fr(b)) for a, b in w2["Mconj_coefficients"]]
# sanity: conjugation flips the sqrt5 part
assert all(x[0] == y[0] and x[1] == -y[1] for x, y in zip(M, Mc))
M_sum = [x[0] + y[0] for x, y in zip(M, Mc)]                  # M + M' in Q
M_odd = [x[1] - y[1] for x, y in zip(M, Mc)]                  # (M - M')/sqrt5
assert all(c.denominator == 1 for c in M_sum), "M+M' not in Z"
assert all(c.denominator == 1 for c in M_odd), "(M-M')/sqrt5 not in Z"
say(f"[C] B674 Molien doublet loaded: 120 exact Q(sqrt5) coefficients; "
    f"M itself has coefficient {w2['M_coefficients'][0][0]} + "
    f"{w2['M_coefficients'][0][1]}*sqrt5 at n=0 — NOT a rational integer "
    "(irrational, in Z[phi]): the raw doublet fails K-ii at n=0 by "
    "inspection; its two rational avatars M+M' and (M-M')/sqrt5 are run "
    "through the kind-map below")

# ---- C5/C6: B774 A5 Molien series, recomputed exactly in Q(sqrt5) -----
# Field elements as (a, b) = a + b*sqrt5 with Fraction parts.
def fmul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

def series_inv_field(p, N):
    """inverse of a Q(sqrt5)[t] polynomial with constant term 1, to t^N."""
    p = list(p) + [(Fr(0), Fr(0))] * (N + 1 - len(p))
    inv = [(Fr(1), Fr(0))] + [(Fr(0), Fr(0))] * N
    for n in range(1, N + 1):
        s = (Fr(0), Fr(0))
        for k in range(1, n + 1):
            if p[k] != (Fr(0), Fr(0)):
                t = fmul(p[k], inv[n - k])
                s = (s[0] + t[0], s[1] + t[1])
        inv[n] = (-s[0], -s[1])
    return inv

half = Fr(1, 2)
phi = (half, half)               # (1+sqrt5)/2
phim1 = (-half, half)            # phi - 1
one = (Fr(1), Fr(0))
zero = (Fr(0), Fr(0))

def polymul(p, q):
    r = [zero] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            t = fmul(a, b)
            r[i + j] = (r[i + j][0] + t[0], r[i + j][1] + t[1])
    return r

lin = [one, (Fr(-1), Fr(0))]                        # 1 - t
D1 = polymul(lin, polymul(lin, lin))                # (1-t)^3
D2 = polymul(lin, polymul([one, one], [one, one]))  # (1-t)(1+t)^2
D3 = polymul(lin, [one, one, one])                  # (1-t)(1+t+t^2)
D5a = polymul(lin, [one, (-phim1[0], -phim1[1]), one])
D5b = polymul(lin, [one, phi, one])

inv1 = series_inv_field(D1, NSER)
inv2 = series_inv_field(D2, NSER)
inv3 = series_inv_field(D3, NSER)
inv5a = series_inv_field(D5a, NSER)
inv5b = series_inv_field(D5b, NSER)

# untwisted Molien (Hilbert series of A5-invariants):
# (1/60)[1*inv1 + 15*inv2 + 20*inv3 + 12*inv5a + 12*inv5b]
hilb_A5 = []
for n in range(NSER + 1):
    a = inv1[n][0] + 15 * inv2[n][0] + 20 * inv3[n][0] \
        + 12 * inv5a[n][0] + 12 * inv5b[n][0]
    b = inv1[n][1] + 15 * inv2[n][1] + 20 * inv3[n][1] \
        + 12 * inv5a[n][1] + 12 * inv5b[n][1]
    assert b == 0, "A5 Hilbert series must be rational"
    c = a / 60
    assert c.denominator == 1 and c >= 0
    hilb_A5.append(int(c))
assert hilb_A5[:16] == [1, 0, 1, 0, 1, 0, 2, 0, 2, 0, 3, 0, 4, 0, 4, 1], \
    "A5 Hilbert head does not match the banked CP-A5-molien output"
say(f"[C] A5 invariant Hilbert series recomputed exactly, head matches "
    f"banked cell: {hilb_A5[:16]}")

# theta-odd twisted Molien: M_odd(t) = (sqrt5/5)(inv5a - inv5b)*(12/60)*sqrt5?
# Banked closed form: M_odd = (12/60)*sqrt5*(inv5a - inv5b) = (sqrt5/5)(...)
# Each (inv5a - inv5b)_n is Galois-odd = pure sqrt5 * rational = (0, r_n);
# so M_odd_n = (1/5)*sqrt5*sqrt5*r_n = r_n.
modd_A5 = []
for n in range(NSER + 1):
    da = (inv5a[n][0] - inv5b[n][0], inv5a[n][1] - inv5b[n][1])
    assert da[0] == 0, "difference must be Galois-odd (pure sqrt5 part)"
    c = da[1]  # (sqrt5/5) * sqrt5 * r = r
    assert c.denominator == 1
    modd_A5.append(int(c))
assert modd_A5[:16] == [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0], \
    "theta-odd twisted Molien head does not match banked output"
say(f"[C] A5 theta-odd twisted Molien recomputed exactly, head matches "
    f"banked cell: {modd_A5[:16]}")

# ---- C7/C8: 2T Molien series (B267/B1068) and B1068's 1/(1-t^3) -------
num_2t = [1] + [0] * 11 + [1]                     # 1 + t^12
den_2t = prod_one_minus([(6, 1), (8, 1)], NSER)   # (1-t^6)(1-t^8)
mol_2t_full = smul(num_2t, sinv(den_2t, NSER), NSER)
mol_2t = mol_2t_full[: NSER + 1]
assert all(c >= 0 for c in mol_2t)
hilb_z3 = sinv(prod_one_minus([(3, 1)], NSER), NSER)

# ---- C9: B683 divided-power series (q;q)^{-3/5} ----------------------
# recurrence n f_n = r * sum_m (-sigma1(m)) f_{n-m}, r = -3/5
N683 = 60
sig1 = [0] * (N683 + 1)
for d in range(1, N683 + 1):
    for m in range(d, N683 + 1, d):
        sig1[m] += d
f683 = [Fr(1)] + [Fr(0)] * N683
r = Fr(-3, 5)
for n in range(1, N683 + 1):
    s = Fr(0)
    for m in range(1, n + 1):
        s += Fr(-sig1[m]) * f683[n - m]
    f683[n] = r * s / n
assert f683[1] == Fr(3, 5)
# spot the divided-power law v5(den c_n) = n + v5(n!) at n = 1, 5, 10
def v5(x):
    v = 0
    while x % 5 == 0:
        x //= 5
        v += 1
    return v
for n in (1, 5, 10):
    vn = v5(f683[n].denominator)
    vfact = sum(n // 5 ** k for k in range(1, 8))
    assert vn == n + vfact, f"divided-power law fails at n={n}"
say("[C] B683 (q;q)^{-3/5} recomputed exactly; divided-power law "
    "v5(den c_n) = n + v5(n!) spot-verified at n = 1, 5, 10")

# ---- C10: B739 Q(sqrt-3) ideal-count series --------------------------
# a_n = #ideals of norm n = sum_{d|n} chi_{-3}(d); series 1 + sum a_n q^n
N739 = 400
chi3 = {0: 0, 1: 1, 2: -1}
a739 = [1] + [0] * N739
for n in range(1, N739 + 1):
    s = 0
    for d in range(1, n + 1):
        if n % d == 0:
            s += chi3[d % 3]
    a739[n] = s
assert a739[1:8] == [1, 0, 1, 1, 0, 0, 2]   # ideal counts for n=1..7
# anchors: n=3 ramified (one ideal), n=4 inert 2 squared, n=7 split (two)
assert all(c >= 0 for c in a739)

supplementary = [
    dict(name="SUPP-1 Lee-Yang chi_1 = q^{11/60} G(q) (YL convention, banked c=-22/5)",
         location="frontier/B677_morning_packet/generation_leg/g1_tube/g1_run_log.txt "
                  "(candidate T2; conventions banked with c and h)",
         coeffs=G, alpha=Fr(11, 60), stated_c=Fr(-22, 5), provenance="imported",
         notes="(2,5) minimal-model character as committed corpus artifact; "
               "stage-side (Lee-Yang CFT data), like census class A4"),
    dict(name="SUPP-2 Lee-Yang chi_tau = q^{-1/60} H(q) (YL convention, banked c=-22/5)",
         location="same g1_tube artifact",
         coeffs=H, alpha=Fr(-1, 60), stated_c=Fr(-22, 5), provenance="imported",
         notes="second (2,5) character"),
    dict(name="SUPP-3 Fibonacci chi_1 = q^{-7/60} G(q) (FIB convention, banked c=14/5)",
         location="same g1_tube artifact (second banked convention)",
         coeffs=G, alpha=Fr(-7, 60), stated_c=Fr(14, 5), provenance="imported",
         notes="same series, other banked (c, h) reading"),
    dict(name="SUPP-4 B674 Molien avatar M+M' (trace sum, 120 banked terms)",
         location="frontier/B674_generation_leg/w2_step3/coefficients_both_conjugates.json",
         coeffs=M_sum, alpha=Fr(0), stated_c=None, provenance="object",
         notes="raw M has irrational coefficient 3/2 + sqrt5/2 at n=0 (fails "
               "K-ii by inspection); this rational avatar carries the sign "
               "structure"),
    dict(name="SUPP-5 B674 Molien avatar (M-M')/sqrt5 (theta-odd, 120 banked terms)",
         location="same JSON",
         coeffs=M_odd, alpha=Fr(0), stated_c=None, provenance="object",
         notes="the STEP3_VERDICT diagnostic stream"),
    dict(name="SUPP-6 B774 A5 invariant Hilbert/Molien series (untwisted)",
         location="frontier/B774_chord_pass/cells/CP-A5-molien/{compute.py,output.txt} "
                  "(recomputed exactly here, head 16/16 match)",
         coeffs=hilb_A5, alpha=Fr(0), stated_c=None, provenance="imported",
         notes="icosahedral invariant ring; A5 is stage apparatus, not m004 data"),
    dict(name="SUPP-7 B774 A5 theta-odd twisted Molien M_odd(t)",
         location="same cell (closed form banked; recomputed exactly here)",
         coeffs=modd_A5, alpha=Fr(0), stated_c=None, provenance="imported",
         notes="the chord-pass 5-adic test object"),
    dict(name="SUPP-8 2T Molien series (1+t^12)/((1-t^6)(1-t^8)) (B267/B1068)",
         location="frontier/B267_e6_coherence/FINDINGS.md; "
                  "frontier/B1068_descent_inventory/w2_full_results.json "
                  "('the ONE genuine q-series that 2T supplies')",
         coeffs=mol_2t, alpha=Fr(0), stated_c=None, provenance="object",
         notes="E6 Kleinian singularity C^2/2T coordinate ring; 2T is the "
               "arc's arithmetic-route group — provenance read generously as "
               "object-side so the kill lands on a computed clause"),
    dict(name="SUPP-9 B1068 Hilbert series 1/(1-t^3) (order-3 character rep)",
         location="frontier/B1068_descent_inventory/w2_full_results.json",
         coeffs=hilb_z3, alpha=Fr(0), stated_c=None, provenance="object",
         notes="the parity-falsifier control series banked in B1068"),
    dict(name="SUPP-10 B683 divided-power series (q;q)_inf^{-3/5}",
         location="frontier/B683_arithmetic_ledger/verify_divided_power.py "
                  "(theorem cell; coefficients recomputed exactly here)",
         coeffs=f683, alpha=Fr(0), stated_c=None, provenance="object",
         notes="the F-stream denominators' engine; genuinely object-side"),
    dict(name="SUPP-11 B739 Q(sqrt-3) ideal-count series 1 + sum #ideals(n) q^n",
         location="frontier/B739_character_rigidity/b739_probe_out.txt "
                  "(a_n = sum_(d|n) chi_-3(d), verified there to n=1500; "
                  "recomputed here to n=400)",
         coeffs=a739, alpha=Fr(0), stated_c=None, provenance="object",
         notes="Q(sqrt-3) is the object's (invariant) trace field: read "
               "object-side; weight-1 theta-type growth (divisor-bounded)"),
]

results = []
for e in supplementary:
    v = kind_map(e)
    results.append(v)
    report(v, e)

n_pass = sum(1 for v in results if v["verdict"] == "PASS")
say("=" * 74)
say(f"SUPPLEMENTARY TALLY: {len(results)} entries, {n_pass} kind-map passes")
for v in results:
    say(f"  {v['verdict']:>4}  {v['name'][:78]}"
        + (f"  [{v['first_failed']}]" if v.get("first_failed") else ""))
say(f"controls bite in this run: {bite_ok}")
say(f"CANDIDATE-FOUND among supplementary entries: {'YES' if n_pass else 'NO'}")

def jsonable(x):
    if isinstance(x, Fr):
        return str(x)
    if isinstance(x, dict):
        return {k: jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    return x

with open(os.path.join(HERE, "supplementary_results.json"), "w") as f:
    json.dump(jsonable({
        "e6_first_coefficients_check": chi_head,
        "controls": cv, "bite_ok": bite_ok,
        "supplementary": results, "n_pass": n_pass}), f, indent=1)
with open(os.path.join(HERE, "supplementary_output.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
say("[saved] supplementary_results.json, supplementary_output.txt")
