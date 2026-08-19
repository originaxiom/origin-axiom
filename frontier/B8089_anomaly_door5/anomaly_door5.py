#!/usr/bin/env python3
"""B8089 -- the anomaly layer over the object's DERIVED content (L144, door 5).

Preregistered in PREREGISTRATION.md, sealed (SEAL.txt) before this file existed.

THE GAP. Every anomaly computation in the bank runs over the IMPORTED chiral 15 (B864, and its
B8070 sharpening). B876 DERIVES the object's matter as the 16 -- one generation WITH nu^c. The
anomaly layer over the derived content has never been computed. L144 asks whether that layer
yields a door-5 ratio: dimensionless, quantized, RG-invariant, with genuine gauge content.

QUANTIFIER (COMPUTE_THE_PROGRAM): the ALGEBRA su(3)+su(2)+u(1) with the derived 16 and the
global form Z6. Nothing about the manifold. NO VALUE IS COMPARED TO ANY MEASUREMENT -- this is
the ratio lane, and the scale lane (B413, B563) stays closed. Gate 5: nothing enters CLAIMS.md.
"""
from fractions import Fraction as F
import itertools, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
FAILED = []
def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAILED.append(label)

# ---------------------------------------------------------------------------
# ROUTE 1 -- the field content, typed.  (colour_dim, signed_triality, isospin_dim, Y, count)
# triality: +1 for 3, -1 for 3bar, 0 for singlet.  Weyl fermions, all written left-handed.
# ---------------------------------------------------------------------------
R1 = [
    ("Q",    3,  1, 2, F(1, 6)),
    ("u^c",  3, -1, 1, F(-2, 3)),
    ("d^c",  3, -1, 1, F(1, 3)),
    ("L",    1,  0, 2, F(-1, 2)),
    ("e^c",  1,  0, 1, F(1)),
    ("nu^c", 1,  0, 1, F(0)),
]

# ---------------------------------------------------------------------------
# ROUTE 2 -- derive the SAME hypercharges from su(5) alone, independently.
# The 5 carries Y = diag(-1/3,-1/3,-1/3, 1/2, 1/2) (traceless).  Then 16 = 10 + 5bar + 1 with
# 10 = Lambda^2(5), so Y(10)_{ij} = Y_i + Y_j.  Nothing about the SM is typed in here.
# ---------------------------------------------------------------------------
Y5 = [F(-1, 3)] * 3 + [F(1, 2)] * 2
assert sum(Y5) == 0, "the su(5) generator must be traceless"
R2 = []
for i, j in itertools.combinations(range(5), 2):          # 10 = Lambda^2(5)
    col = sum(1 for k in (i, j) if k < 3)
    R2.append(("10", Y5[i] + Y5[j], col))
for i in range(5):                                        # 5bar
    R2.append(("5bar", -Y5[i], 1 if i < 3 else 0))
R2.append(("1", F(0), 0))                                 # the singlet: nu^c

print("=" * 78)
print("CONTROLS")
print("=" * 78)
gate("route 1 has 16 Weyl states",
     sum(c * iso for _, c, _, iso, _ in R1) == 16,
     str(sum(c * iso for _, c, _, iso, _ in R1)))
gate("route 2 (su(5)) has 16 states", len(R2) == 16, str(len(R2)))

# the two routes must agree as multisets of hypercharge, with multiplicity
m1 = sorted([y for _, c, _, iso, y in R1 for _ in range(c * iso)])
m2 = sorted([y for _, y, _ in R2])
gate("ROUTE 2 REPRODUCES ROUTE 1's HYPERCHARGES EXACTLY (independent derivation)", m1 == m2,
     f"{len(m1)} charges")

# ---------------------------------------------------------------------------
# the anomaly functionals, over an arbitrary charge assignment
# ---------------------------------------------------------------------------
def anomalies(fields):
    """fields: list of (name, colour_dim, triality, isospin_dim, charge)"""
    A = {}
    A["U(1)^3"]      = sum(c * iso * y**3 for _, c, _, iso, y in fields)
    A["U(1)-grav"]   = sum(c * iso * y      for _, c, _, iso, y in fields)
    # index T = 1/2 for the fundamental of su(N), 0 for a singlet
    A["[SU(3)]^2U(1)"] = sum((F(1,2) if c == 3 else 0) * iso * y for _, c, _, iso, y in fields)
    A["[SU(2)]^2U(1)"] = sum((F(1,2) if iso == 2 else 0) * c * y for _, c, _, iso, y in fields)
    A["[SU(3)]^3"]     = sum(t * iso for _, c, t, iso, _ in fields)          # A(3)=+1, A(3bar)=-1
    A["SU(2)-Witten"]  = sum(c for _, c, _, iso, _ in fields if iso == 2) % 2  # doublet count mod 2
    return A

SIXTEEN = R1
FIFTEEN = [f for f in R1 if f[0] != "nu^c"]

print()
print("=" * 78)
print("1. THE GAUGE ANOMALY LAYER OVER THE DERIVED 16")
print("=" * 78)
a16 = anomalies(SIXTEEN)
for k, v in a16.items():
    print(f"    {k:<16} = {v}")
gate("every gauge anomaly vanishes over the 16 (INSTRUMENT CONTROL)",
     all(v == 0 for v in a16.values()))

print("\n  the 15, for comparison (nu^c dropped):")
a15 = anomalies(FIFTEEN)
for k, v in a15.items():
    print(f"    {k:<16} = {v}")
gate("the 15 is also gauge-anomaly-free (nu^c is a gauge singlet, so it MUST be)",
     all(v == 0 for v in a15.values()))

# ---------------------------------------------------------------------------
# BITE CONTROL -- a check that cannot detect an anomaly is not a check
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("2. BITE CONTROL")
print("=" * 78)
BROKEN = [f for f in R1 if f[0] != "e^c"]
ab = anomalies(BROKEN)
print("    dropping e^c:", {k: str(v) for k, v in ab.items()})
gate("the instrument DETECTS an anomaly when one is present", any(v != 0 for v in ab.values()),
     f"nonzero in {[k for k,v in ab.items() if v != 0]}")

# ---------------------------------------------------------------------------
# 3. B-L, the global symmetry -- the 't Hooft layer L144 hoped would constrain dynamics
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("3. B-L: THE 't HOOFT LAYER")
print("=" * 78)
BL = {"Q": F(1,3), "u^c": F(-1,3), "d^c": F(-1,3), "L": F(-1), "e^c": F(1), "nu^c": F(1)}
def bl_fields(fields):
    return [(n, c, t, iso, BL[n]) for n, c, t, iso, _ in fields]

bl16, bl15 = anomalies(bl_fields(SIXTEEN)), anomalies(bl_fields(FIFTEEN))
print(f"    (B-L)^3      over 16 = {bl16['U(1)^3']}      over 15 = {bl15['U(1)^3']}")
print(f"    (B-L)-grav   over 16 = {bl16['U(1)-grav']}      over 15 = {bl15['U(1)-grav']}")
gate("B-L is 't Hooft anomaly FREE over the derived 16",
     bl16["U(1)^3"] == 0 and bl16["U(1)-grav"] == 0)
gate("B-L is ANOMALOUS over the imported 15 -- nu^c is exactly what cancels it",
     bl15["U(1)^3"] != 0 and bl15["U(1)-grav"] != 0,
     f"cubic {bl15['U(1)^3']}, grav {bl15['U(1)-grav']}")

# nu^c isolation: 16 vs 15 may differ ONLY where nu^c can contribute
gauge_same = all(a16[k] == a15[k] for k in a16)
gate("16-vs-15 differ ONLY in B-L, not in any gauge channel (nu^c isolation)", gauge_same)

# ---------------------------------------------------------------------------
# 4. THE Z6 GLOBAL FORM -- is the derived matter consistent with the QUOTIENT?
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("4. THE Z6 GLOBAL FORM")
print("=" * 78)
# The Z6 generated by (omega I_3, -I_2, e^{i pi/3}) acts trivially on a field iff a congruence
# 6Y = a*t + b*d (mod 6) holds simultaneously for all fields, for some fixed (a,b).  Solve for
# (a,b) by exhaustion rather than quoting one.
def triality_unsigned(c, t):
    return (0 if c == 1 else (1 if t == 1 else 2))
sols = []
for a in range(6):
    for b in range(6):
        if all((6 * y - a * triality_unsigned(c, t) - b * (1 if iso == 2 else 0)) % 6 == 0
               for _, c, t, iso, y in R1):
            sols.append((a, b))
print(f"    (a,b) solving  6Y = a*triality + b*duality  (mod 6)  for ALL six fields: {sols}")
gate("the derived matter IS consistent with the Z6 quotient (a solution exists)", len(sols) > 0)
gate("and the solution is unique mod 6", len(sols) == 1, str(sols))

# ---------------------------------------------------------------------------
# 5. RATIOS -- door 5's actual ask
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("5. DOOR 5's ASK: a dimensionless quantized RATIO with gauge content")
print("=" * 78)
nonzero_gauge = {k: v for k, v in a16.items() if v != 0}
nonzero_bl    = {k: v for k, v in bl16.items() if v != 0}
print(f"    non-vanishing gauge invariants over the 16: {nonzero_gauge or '{} -- ALL ZERO'}")
print(f"    non-vanishing B-L  invariants over the 16: {nonzero_bl or '{} -- ALL ZERO'}")
n_ratios = len(nonzero_gauge) + len(nonzero_bl)
gate("the anomaly layer over the derived content is IDENTICALLY ZERO", n_ratios == 0,
     f"{n_ratios} non-vanishing invariants")

RES = {
 "route2_reproduces_route1": m1 == m2,
 "n_states": 16,
 "gauge_anomalies_16": {k: str(v) for k, v in a16.items()},
 "gauge_anomalies_15": {k: str(v) for k, v in a15.items()},
 "bite_control_nonzero": [k for k, v in ab.items() if v != 0],
 "BL_16": {k: str(v) for k, v in bl16.items()},
 "BL_15": {k: str(v) for k, v in bl15.items()},
 "BL_anomaly_free_over_16": bl16["U(1)^3"] == 0 and bl16["U(1)-grav"] == 0,
 "BL_anomalous_over_15": bl15["U(1)^3"] != 0,
 "z6_solutions": sols,
 "z6_consistent": len(sols) > 0,
 "n_nonvanishing_invariants": n_ratios,
 "anomaly_layer_identically_zero": n_ratios == 0,
 "outcome": "B" if n_ratios == 0 else "A",
 "verdict": ("OUTCOME B, as preregistered: the anomaly layer over the DERIVED 16 is identically "
             "zero, so it supplies no ratio at all -- door 5's ask is structurally unanswerable "
             "by this layer, not merely unanswered. B167 stands and receives its first citation."),
 "scope": ("su(3)+su(2)+u(1) with the derived 16 and global form Z6. NO value compared to any "
           "measurement; the ratio lane only, with the scale lane (B413/B563) untouched and "
           "closed. Says nothing about the manifold. Gate 5: nothing enters CLAIMS.md.")}
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True)
print("\n  results.json written")

print()
print("=" * 78)
if FAILED:
    raise SystemExit(f"CONTROLS FAILED: {FAILED}")
print(f"ALL CHECKS PASS -- OUTCOME {RES['outcome']}")
