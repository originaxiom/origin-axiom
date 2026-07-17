#!/usr/bin/env python3
# B666 CELL 7 (R21-5): THE 13-DIAL MECHANISM HUNT
#
# Sealed task (CAMPAIGN_PREREGISTRATION.md, wave 2, cell 7):
#   (a) v13 of every entry in the exact cup table (cell2_cup_values.json)
#       and the natural-operator matrices -- does 13 localize in a
#       specific H^2 direction or class?
#   (b) the norm route: 13 = N(1+2*sqrt(-3)) (1 + 3*4 = 13); do the
#       13-carrying values factor through the ideal (1+2*sqrt(-3))
#       systematically?  Exact ideal-valuation arithmetic in O_K.
#   (c) the 211 side on the silver values (B649 silver_Y_L.json; 211
#       inert in Q(i)); the general-law hunt: "dial prime = smallest
#       prime with object-specific splitting behavior X" -- state X or
#       bank the constraint set.
#
# Exact arithmetic only (integers + Fractions); no floats anywhere in a
# decisive step.  New files only; nothing tracked is modified.
#
# Inputs (banked):
#   frontier/B666_leads_campaign/cell2/cell2_cup_values.json  (cell 2)
#   frontier/B649_silver_holonomy/silver_Y_L.json             (B649 G2)
# Cross-checked against banked normal forms: B645 (golden dial law),
# cellC2 (phase catalogue), b649_g3_analysis.txt (silver deviations).

import json, os, sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
CAMP = os.path.dirname(HERE)
CELL2 = os.path.join(CAMP, "cell2", "cell2_cup_values.json")
SILVER = os.path.join(CAMP, "..", "B649_silver_holonomy", "silver_Y_L.json")

OUT = {}          # persisted JSON
def out(*a):
    print(*a, flush=True)

# ===========================================================================
# STEP 0 -- exact ideal-valuation machinery, with self-tests
# ===========================================================================
# K = Q(sqrt(-3)), O_K = Z[omega].  13 = pi * pibar with
#   pi    = 1 + 2*sqrt(-3)   (mod pi:    sqrt(-3) == 6  in F_13, 6^2=36==-3)
#   pibar = 1 - 2*sqrt(-3)   (mod pibar: sqrt(-3) == 7  in F_13, 7^2=49==-3)
# N(1+2*sqrt(-3)) = 1 + 3*4 = 13.
#
# For x = A + B*sqrt(-3), A,B in Z:
#   x == 0 mod pi     <=>  A + 6B == 0 (mod 13)
#   x / pi    = ((A+6B) + (B-2A)*sqrt(-3)) / 13      (exact when divisible)
#   x == 0 mod pibar  <=>  A - 6B == 0 (mod 13)
#   x / pibar = ((A-6B) + (B+2A)*sqrt(-3)) / 13      (exact when divisible)

def vp_rat(n, p):
    """p-adic valuation of a nonzero integer."""
    n = abs(int(n)); v = 0
    while n % p == 0:
        n //= p; v += 1
    return v

def v13_rat(q):
    """13-adic valuation of a nonzero Fraction."""
    return vp_rat(q.numerator, 13) - vp_rat(q.denominator, 13)

def val_split(a, b, p, r, div):
    """Valuation of x = a + b*delta (a,b Fractions) at the split prime of p
    where delta == r (mod that prime); div(A,B) returns the exact division
    of A + B*delta by the prime element (integer pair), valid when
    A + r*B == 0 mod p.  Returns None for x = 0."""
    if a == 0 and b == 0:
        return None
    d = (a.denominator * b.denominator) // __import__("math").gcd(
        a.denominator, b.denominator)
    A = int(a * d); B = int(b * d)
    vd = vp_rat(d, p)
    v = 0
    while (A + r * B) % p == 0:
        A, B = div(A, B)
        v += 1
    return v - vd

# golden split primes over 13 in Q(sqrt(-3))
div_pi    = lambda A, B: ((A + 6 * B) // 13, (B - 2 * A) // 13)
div_pibar = lambda A, B: ((A - 6 * B) // 13, (B + 2 * A) // 13)
v_pi    = lambda a, b: val_split(a, b, 13, 6, div_pi)
v_pibar = lambda a, b: val_split(a, b, 13, -6, div_pibar)

# silver split primes over 13 in Q(i): 13 = (3+2i)(3-2i)
#   mod (3+2i): i == 5 (5^2 = 25 == -1); mod (3-2i): i == -5 == 8
#   x/(3+2i) = ((3A+2B) + (3B-2A)i)/13 ; x/(3-2i) = ((3A-2B) + (3B+2A)i)/13
div_p1 = lambda A, B: ((3 * A + 2 * B) // 13, (3 * B - 2 * A) // 13)
div_p2 = lambda A, B: ((3 * A - 2 * B) // 13, (3 * B + 2 * A) // 13)
v_p1 = lambda a, b: val_split(a, b, 13, 5, div_p1)   # v at (3+2i)
v_p2 = lambda a, b: val_split(a, b, 13, -5, div_p2)  # v at (3-2i)

def v_inert(a, b, p):
    """Valuation at an inert rational prime p of a + b*i (Fractions)."""
    if a == 0 and b == 0:
        return None
    vs = []
    for q in (a, b):
        if q != 0:
            vs.append(v13_rat(q) if False else
                      vp_rat(q.numerator, p) - vp_rat(q.denominator, p))
    return min(vs)

out("=" * 78)
out("STEP 0 -- machinery self-tests (exact)")
out("=" * 78)
# N(1+2 sqrt(-3)) = 13, N(3+2i) = 13, 211 inert in Q(i) (211 % 4 == 3), prime
assert 1 + 3 * 4 == 13
assert 3 * 3 + 2 * 2 == 13
assert 211 % 4 == 3
assert all(211 % k for k in range(2, 15))
assert (6 * 6 + 3) % 13 == 0 and (7 * 7 + 3) % 13 == 0
assert (5 * 5 + 1) % 13 == 0
# valuation self-tests, golden side
assert (v_pi(Fr(1), Fr(2)), v_pibar(Fr(1), Fr(2))) == (1, 0)      # pi itself
assert (v_pi(Fr(1), Fr(-2)), v_pibar(Fr(1), Fr(-2))) == (0, 1)    # pibar
assert (v_pi(Fr(13), Fr(0)), v_pibar(Fr(13), Fr(0))) == (1, 1)    # 13 = pi*pibar
assert (v_pi(Fr(1, 13), Fr(0)), v_pibar(Fr(1, 13), Fr(0))) == (-1, -1)
assert (v_pi(Fr(-1, 2), Fr(1, 2)), v_pibar(Fr(-1, 2), Fr(1, 2))) == (0, 0)  # zeta3
assert (v_pi(Fr(169), Fr(0)), v_pibar(Fr(169), Fr(0))) == (2, 2)
# (1+2r)^2 = 1 - 12 + 4r = -11 + 4r
assert (v_pi(Fr(-11), Fr(4)), v_pibar(Fr(-11), Fr(4))) == (2, 0)
# valuation self-tests, silver side
assert (v_p1(Fr(3), Fr(2)), v_p2(Fr(3), Fr(2))) == (1, 0)
assert (v_p1(Fr(3), Fr(-2)), v_p2(Fr(3), Fr(-2))) == (0, 1)
assert (v_p1(Fr(13), Fr(0)), v_p2(Fr(13), Fr(0))) == (1, 1)
assert v_inert(Fr(211), Fr(422), 211) == 1
assert v_inert(Fr(1, 211), Fr(3), 211) == -1
out("all valuation self-tests PASS  (pi = 1+2 sqrt(-3), pibar = conj;")
out("  silver split pair (3+2i),(3-2i); inert valuation = min of components)")

# ===========================================================================
# STEP 1 -- (a) v13 across the exact cup table + the operator matrices
# ===========================================================================
out()
out("=" * 78)
out("STEP 1 -- (a) the golden 13-localization table (banked cell-2 basis)")
out("=" * 78)
J = json.load(open(CELL2))
h2_basis = [tuple(x) for x in J["h2_basis"]]
assert h2_basis == [(0, 2), (0, 3), (1, 2), (2, 3), (2, 4)]

def parse_pair(v):
    return (Fr(v[0]), Fr(v[1]))

def vpair(x):
    return (v_pi(*x), v_pibar(*x))

asym_rows = []      # entries with v_pi != v_pibar
loc_pairs = {}      # (i,j) -> list of (m, vpi, vpibar) nonzero-13 coords
den13 = []          # entries with negative 13-valuation

def scan_matrix(name, M, rowlab, collab):
    """M: list of rows of [a,b] pairs. Returns list of findings."""
    findings = []
    for i, row in enumerate(M):
        for j, ent in enumerate(row):
            x = parse_pair(ent)
            if x == (Fr(0), Fr(0)):
                continue
            vp, vq = vpair(x)
            if vp != 0 or vq != 0:
                findings.append((rowlab(i), collab(j), vp, vq))
            if vp != vq:
                asym_rows.append((name, rowlab(i), collab(j), vp, vq, x))
            if min(vp, vq) < 0:
                den13.append((name, rowlab(i), collab(j), vp, vq))
    return findings

# --- the cup table itself
cup = J["cup_class_coords"]
out("\n-- cup table [u_i cup u_j] coordinates on b_m (13-carrying entries) --")
cup13 = []
for key in sorted(cup):
    i, j = (int(t) for t in key.split(","))
    for m, ent in enumerate(cup[key]):
        x = parse_pair(ent)
        if x == (Fr(0), Fr(0)):
            continue
        vp, vq = vpair(x)
        if vp != 0 or vq != 0:
            cup13.append((i, j, m, vp, vq))
            out(f"   [u_{i} cup u_{j}] coord b_{m}={h2_basis[m]}: "
                f"(v_pi, v_pibar) = ({vp}, {vq})   value = {x[0]} + {x[1]}*r")
        if vp != vq:
            asym_rows.append(("cup", f"({i},{j})", f"b_{m}", vp, vq, x))
        if min(vp, vq) < 0:
            den13.append(("cup", f"({i},{j})", f"b_{m}", vp, vq))

# localization verdicts on the cup table
pairs13 = sorted(set((i, j) for (i, j, m, vp, vq) in cup13))
pos13 = [(i, j, m, vp, vq) for (i, j, m, vp, vq) in cup13 if min(vp, vq) > 0]
pos_pairs = sorted(set((i, j) for (i, j, m, vp, vq) in pos13))
class4_only = all(4 in (i, j) for (i, j) in pos_pairs)
all_class4_lit = sorted(set((i, j) for (i, j) in pos_pairs))
dirs13 = sorted(set(m for (i, j, m, vp, vq) in pos13))
out(f"\n   pairs with ANY 13-content: {pairs13}")
out(f"   pairs with POSITIVE symmetric-or-not 13-content: {pos_pairs}")
out(f"   VERDICT A1: every v13>0 cup entry lies on a class-4 pair: "
    f"{class4_only}")
out(f"   H^2 directions (b_m) carrying v13>0 cup content: "
    f"{[f'b_{m}={h2_basis[m]}' for m in dirs13]}")
OUT["A1_pos13_pairs"] = pos_pairs
OUT["A1_class4_only"] = class4_only
OUT["A1_pos13_h2_dirs"] = dirs13

# --- the operator matrices
mats = {
    "P (Y-pairing)":       J["P_matrix_Y_pairing"],
    "MV0 (theta 2-form)":  J["MV0"],
    "sigma2 (S on H^2)":   J["sigma2_matrix_cup_basis"],
    "OH (natural op)":     J["natural_operator_OH"],
    "Theta (theta_*)":     J["Theta"],
    "Psi (thetabar_*)":    J["Psi"],
}
out("\n-- operator matrices: 13-carrying entries --")
mat13 = {}
for name, M in mats.items():
    f = scan_matrix(name, M, lambda i: f"row{i}", lambda j: f"col{j}")
    mat13[name] = f
    if f:
        out(f"   {name}:")
        for (r, c, vp, vq) in f:
            out(f"      {r},{c}: (v_pi, v_pibar) = ({vp}, {vq})")
    else:
        out(f"   {name}: 13-CLEAN (every nonzero entry has v_pi = v_pibar = 0)")
OUT["mat13"] = {k: v for k, v in mat13.items()}

out("\n-- entries with 13 in the DENOMINATOR (v13 < 0) --")
for t in den13:
    out(f"   {t[0]} {t[1]},{t[2]}: ({t[3]}, {t[4]})")
out(f"   count = {len(den13)}")

out("\n-- NORM-SYMMETRY on the banked-basis tables --")
out(f"   entries with v_pi != v_pibar (directional 13): {len(asym_rows)}")
for t in asym_rows:
    out(f"      {t[0]} {t[1]},{t[2]}: (v_pi, v_pibar) = ({t[3]}, {t[4]}) "
        f" value = {t[5][0]} + {t[5][1]}*r")
out("   [caveat: banked-basis entries are normalization-contaminated;")
out("    directional content at THIS layer is basis data, not invariant --")
out("    the invariant layer is STEP 2]")
OUT["basis_directional_entries"] = [
    [t[0], t[1], t[2], t[3], t[4]] for t in asym_rows]

# ===========================================================================
# STEP 2 -- (b) the norm route on the INVARIANT layer (golden)
# ===========================================================================
out()
out("=" * 78)
out("STEP 2 -- (b) the norm route: the normalization-free golden invariants")
out("=" * 78)
# Banked lit-class invariant values (B645 normal forms / cellC2 catalogue),
# re-entered and re-verified against their normal forms exactly:
r3 = "sqrt(-3)"
golden_invs = {
    "Dphi_a  inv1": (Fr(7379, 7392), Fr(13, 7392)),
    "Dphi_a  inv2": (Fr(6561, 6574), Fr(13, 6574)),
    "Dphi_Ainv inv1": (Fr(7379, 7392), Fr(13, 7392)),
    "Dphi_Ainv inv2": (Fr(6561, 6574), Fr(13, 6574)),
    "bent_m1 inv1": (Fr(3709, 3696), Fr(0)),
    "bent_m1 inv2": (Fr(21952107, 21866138), Fr(169, 21866138)),
}
# normal-form locks (exact):
#   inv2 = (3^8 + 13 r)/(3^8 + 13):  (a+b r)*(6574) == 6561 + 13 r
assert golden_invs["Dphi_a  inv2"][0] * 6574 == 3 ** 8
assert golden_invs["Dphi_a  inv2"][1] * 6574 == 13
#   inv1 - 1 = 13*zeta3/3696 = 13*(-1+r)/7392
assert golden_invs["Dphi_a  inv1"][0] - 1 == Fr(-13, 7392)
assert golden_invs["Dphi_a  inv1"][1] == Fr(13, 7392)
#   bent_m1 inv1 - 1 = 13/3696
assert golden_invs["bent_m1 inv1"][0] - 1 == Fr(13, 3696)
#   bent_m1 inv2 - 1 = 13*(6613 + 13 r)/21866138
assert golden_invs["bent_m1 inv2"][0] - 1 == Fr(13 * 6613, 21866138)
assert golden_invs["bent_m1 inv2"][1] == Fr(13 * 13, 21866138)
out("banked normal-form locks (B645): ALL PASS (exact re-verification)")

out("\n-- ideal valuations of the lit invariants and their deviations --")
norm_sym_all = True
inv_table = {}
for name, (a, b) in golden_invs.items():
    da, db = a - 1, b
    vv = vpair((a, b)); vd = vpair((da, db))
    inv_table[name] = {"value": [str(a), str(b)], "v_value": vv,
                       "v_dev": vd}
    sym = (vd[0] == vd[1])
    norm_sym_all = norm_sym_all and sym
    out(f"   {name}: v(inv) = {vv}; v(inv - 1) = (v_pi, v_pibar) = {vd}"
        f"   norm-symmetric: {sym}")
out(f"\n   VERDICT B (the norm route, golden): every normalization-free")
out(f"   deviation has v_pi = v_pibar = 1 EXACTLY: {norm_sym_all}")
out(f"   => the 13-content of every invariant deviation is the RATIONAL")
out(f"      ideal (13) = (pi)(pibar) = the NORM ideal of (1+2 sqrt(-3));")
out(f"      no invariant sees a single split factor directionally.")
OUT["B_invariant_norm_symmetric"] = norm_sym_all
OUT["B_invariant_table"] = inv_table

# cross-contamination: does 211 appear anywhere on the golden side?
g211 = []
for name, (a, b) in golden_invs.items():
    for q in (a - 1, b):
        if q != 0 and (q.numerator % 211 == 0 or q.denominator % 211 == 0):
            g211.append(name)
for key in sorted(cup):
    for ent in cup[key]:
        x = parse_pair(ent)
        for q in x:
            if q != 0 and (q.numerator % 211 == 0 or q.denominator % 211 == 0):
                g211.append(f"cup {key}")
out(f"\n   211 on the golden side (invariants + cup table): "
    f"{'NONE' if not g211 else g211}")
OUT["golden_211_hits"] = g211

# ===========================================================================
# STEP 3 -- (c) the silver side: 211 (inert) and 13 (split) in Z[i]
# ===========================================================================
out()
out("=" * 78)
out("STEP 3 -- (c) the silver valuations (Q(i); 211 inert, 13 = (3+2i)(3-2i))")
out("=" * 78)
YJ = json.load(open(SILVER))
Ys = {}
for key, vec in YJ.items():
    assert all(Fr(vec[t]) == 0 for t in (1, 2, 3, 5, 6, 7)), key
    Ys[tuple(int(c) for c in key)] = (Fr(vec[0]), Fr(vec[4]))
assert [s for s in sorted(Ys) if Ys[s] == (Fr(0), Fr(0))] == \
    [(0, 1, 2), (0, 1, 3), (0, 1, 4)]
out("silver_Y_L.json parsed: 10 slots, zero law Y[01k]=0 3/3, values in Q(i)")

def cdiv(x, y):
    a, b = x; c, d = y
    n = c * c + d * d
    return ((a * c + b * d) / n, (b * c - a * d) / n)

def cmul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c)

inv1 = cdiv(cmul(Ys[(0, 2, 3)], Ys[(1, 2, 4)]),
            cmul(Ys[(0, 2, 4)], Ys[(1, 2, 3)]))
inv2 = cdiv(cmul(Ys[(0, 2, 3)], Ys[(1, 3, 4)]),
            cmul(Ys[(0, 3, 4)], Ys[(1, 2, 3)]))
# locks vs the banked G3 analysis values
assert inv2 == (Fr(1775661509660642434903313, 1775664925937025369121636),
                Fr(9285580552058180539, 1775664925937025369121636))
assert inv1 == (Fr(16271648481252971729, 16271671961969963216),
                Fr(-369110590776791, 178988391581669595376))
out("cross-ratio recompute locks vs banked b649_g3_analysis values: BOTH PASS")

out("\n-- the silver lit deviations: v211 (inert) and v13 split pair --")
sil = {}
for name, z in (("silver inv1 - 1", (inv1[0] - 1, inv1[1])),
                ("silver inv2 - 1", (inv2[0] - 1, inv2[1]))):
    v211 = v_inert(*z, 211)
    v1, v2 = v_p1(*z), v_p2(*z)
    sil[name] = {"v211": v211, "v_3+2i": v1, "v_3-2i": v2}
    out(f"   {name}: v211 = {v211}; (v_(3+2i), v_(3-2i)) = ({v1}, {v2})"
        f"   13-norm-symmetric: {v1 == v2}")
OUT["C_silver_deviations"] = sil

out("\n-- the silver Y values and spectator ratios (basis-contaminated,")
out("   labeled; the pairwise ratio DIFFERENCES are normalization-free) --")
ratios = {}
for jk in ((2, 3), (2, 4), (3, 4)):
    r = cdiv(Ys[(0,) + jk], Ys[(1,) + jk])
    v211 = v_inert(*r, 211)
    v1, v2 = v_p1(*r), v_p2(*r)
    ratios[jk] = (v1, v2, v211)
    out(f"   Y[0{jk[0]}{jk[1]}]/Y[1{jk[0]}{jk[1]}]: "
        f"(v_(3+2i), v_(3-2i), v211) = ({v1}, {v2}, {v211})")
d1 = (ratios[(2, 3)][0] - ratios[(2, 4)][0],
      ratios[(2, 3)][1] - ratios[(2, 4)][1])
d2 = (ratios[(2, 3)][0] - ratios[(3, 4)][0],
      ratios[(2, 3)][1] - ratios[(3, 4)][1])
out(f"   normalization-free ratio differences (r23 - r24): {d1}; "
    f"(r23 - r34): {d2}")
OUT["C_silver_ratio_valuations"] = {str(k): v for k, v in ratios.items()}

out("\n-- v211 / v13 of the raw silver Y slots (basis-contaminated, listed) --")
raw = {}
for s in sorted(Ys):
    if Ys[s] == (Fr(0), Fr(0)):
        continue
    v211 = v_inert(*Ys[s], 211)
    v1, v2 = v_p1(*Ys[s]), v_p2(*Ys[s])
    raw["".join(map(str, s))] = (v1, v2, v211)
    out(f"   Y[{s[0]}{s[1]}{s[2]}]: (v_(3+2i), v_(3-2i), v211) = "
        f"({v1}, {v2}, {v211})")
OUT["C_silver_raw_valuations"] = raw

# ===========================================================================
# STEP 4 -- the general-law hunt: candidate X's, tested exactly
# ===========================================================================
out()
out("=" * 78)
out("STEP 4 -- the general law 'dial prime = smallest prime with behavior X'")
out("=" * 78)

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    t = pow(a, (p - 1) // 2, p)
    return 1 if t == 1 else -1

def kronecker2(d):
    """(d|2) for odd d: +1 if d == +-1 mod 8, -1 if d == +-3 mod 8."""
    return 1 if d % 8 in (1, 7) else -1

def split_sym(d, p):
    """splitting symbol of odd prime p in Q(sqrt(d)) via (disc|p)."""
    if p == 2:
        return kronecker2(d)
    return legendre(d, p)

def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = b"\x00" * len(sieve[i * i::i])
    return [i for i in range(n + 1) if sieve[i]]

PRIMES = primes_upto(5000)

out("\n-- the splitting signature battery (exact Legendre symbols) --")
fields = [-3, 5, -15, -1, 2, -2, 3, 6, -5, 10]
sig = {}
for p in (13, 211):
    sig[p] = {d: split_sym(d, p) for d in fields}
    out(f"   p = {p}: " + "  ".join(
        f"({d}|p)={sig[p][d]:+d}" for d in fields))
    out(f"        p mod 3,4,5,8,12,24,120 = "
        f"{p%3},{p%4},{p%5},{p%8},{p%12},{p%24},{p%120}")
OUT["X_signatures"] = {str(p): {str(d): s for d, s in sig[p].items()}
                       for p in (13, 211)}

def smallest_with(pred):
    for q in PRIMES:
        if pred(q):
            return q
    return None

out("\n-- candidate laws (smallest-prime tests; PASS = selects the dial) --")
laws = []
def law(tag, obj, dial, pred, note=""):
    s = smallest_with(pred)
    ok = (s == dial)
    laws.append((tag, obj, dial, s, ok, note))
    out(f"   [{'PASS' if ok else 'FAIL'}] {tag} ({obj}): smallest = {s}, "
        f"dial = {dial}  {note}")

# golden candidates
law("split in Q(sqrt(-3))", "golden", 13,
    lambda q: q != 3 and split_sym(-3, q) == 1)
law("split in Q(sqrt(-3)) & inert in Q(sqrt(5))", "golden", 13,
    lambda q: q != 3 and q != 5 and split_sym(-3, q) == 1
    and split_sym(5, q) == -1)
law("p == 1 mod 12 (splits in Q(zeta12))", "golden", 13,
    lambda q: q % 12 == 1)
law("p = 1 + 3 b^2 (norm of 1 + b sqrt(-3))", "golden", 13,
    lambda q: any(q == 1 + 3 * b * b for b in range(1, 60)))
law("inert in Q(sqrt(5)) alone", "golden", 13,
    lambda q: q != 5 and split_sym(5, q) == -1)
law("p == 13 mod 15 (golden-own modulus 3*5)", "golden", 13,
    lambda q: q % 15 == 13 % 15)
law("p == 13 mod 60", "golden", 13, lambda q: q % 60 == 13 % 60)

# silver candidates -- the same shapes transported
law("inert in Q(i) (p == 3 mod 4)", "silver", 211,
    lambda q: q % 4 == 3)
law("inert in Q(i) & inert in Q(sqrt(2))", "silver", 211,
    lambda q: q % 8 == 3)  # == 3 mod 8 <=> both inert with split sqrt(-2)
law("p = 1 + 2 b^2 (norm of 1 + b sqrt(-2))", "silver", 211,
    lambda q: any(q == 1 + 2 * b * b for b in range(1, 60)))
law("p = a^2 + b^2, a = 1 (norm of 1 + bi)", "silver", 211,
    lambda q: any(q == 1 + b * b for b in range(1, 60)))
law("silver-own 2-power moduli: p == 211 mod M", "silver", 211,
    lambda q: q % 8 == 211 % 8, "(M = 8; see sweep below)")

# the silver-own congruence sweep (non-vacuous only: M < 211)
out("\n-- silver-own / near-own congruence sweep (non-vacuous: M < 211) --")
sweep = {}
for M, label in ((4, "own: conductor field"), (8, "own: conductor"),
                 (16, "own: 2-power"), (32, "own: disc"),
                 (64, "own: 2-power"), (128, "own: 2-power"),
                 (3, "+chord prime 3"), (12, "2^2*3"), (24, "2^3*3"),
                 (48, "2^4*3"), (96, "2^5*3"), (120, "CROSS-OBJECT 8*3*5"),
                 (168, "2^3*3*7")):
    r = 211 % M
    s = smallest_with(lambda q, M=M, r=r: q % M == r)
    sweep[M] = s
    out(f"   M = {M:>3} ({label}): 211 == {r} mod M; smallest prime in "
        f"class = {s}  {'<-- SELECTS 211' if s == 211 else ''}")
OUT["X_silver_congruence_sweep"] = {str(k): v for k, v in sweep.items()}

# golden mirror of the cross-object modulus
s120g = smallest_with(lambda q: q % 120 == 13)
out(f"   golden mirror, M = 120: smallest prime == 13 mod 120 = {s120g}"
    f"  {'<-- SELECTS 13' if s120g == 13 else ''}")

# recurrence-membership candidates (exact integer recurrences)
out("\n-- recurrence-membership and unit-order facts (exact) --")
fib = [0, 1]
while fib[-1] < 10 ** 6:
    fib.append(fib[-1] + fib[-2])
pell = [0, 1]
while pell[-1] < 10 ** 6:
    pell.append(2 * pell[-1] + pell[-2])
comp = [2, 2]
while comp[-1] < 10 ** 6:
    comp.append(2 * comp[-1] + comp[-2])
out(f"   13 is a Fibonacci number (13 = F_7): {13 in fib}")
out(f"   211 is a Pell number: {211 in pell}; "
    f"a companion-Pell/half-companion: {211 in comp or 422 in comp}")
# rank of apparition (computed mod p, exact)
def rank_apparition(p, c1, c0):
    """least n >= 1 with U_n == 0 mod p for U_{n+1} = c1 U_n + c0 U_{n-1}."""
    a, b = 0, 1   # U_0, U_1
    n = 1
    while b % p != 0:
        a, b = b, (c1 * b + c0 * a) % p
        n += 1
        assert n < p * p
    return n
alpha_f = rank_apparition(13, 1, 1)
alpha_p = rank_apparition(211, 2, 1)
assert fib[alpha_f] % 13 == 0
out(f"   rank of apparition: alpha_Fib(13) = {alpha_f} (F_7 = 13: the dial")
out(f"   prime IS the Fibonacci number at its own rank of apparition);")
out(f"   alpha_Pell(211) = {alpha_p}  (212 = 2^2*53; alpha | p+1: "
    f"{(211 + 1) % alpha_p == 0}; P_alpha is NOT 211-related)")
OUT["X_rank_apparition"] = {"alpha_Fib_13": alpha_f,
                            "alpha_Pell_211": alpha_p}
law("p divides F_alpha with F_alpha = p (p IS a Fibonacci prime)",
    "golden", 13, lambda q: q in fib)
law("p IS a Pell-sequence term", "silver", 211, lambda q: q in pell)

def unit_order(p, d, u):
    """order of u = (a + b sqrt(d)) in (F_p[x]/(x^2-d))^* -- exact."""
    a, b = u
    x, y = a % p, b % p
    e = 1
    cx, cy = x, y
    while (cx, cy) != (1, 0):
        cx, cy = (cx * x + cy * y * d) % p, (cx * y + cy * x) % p
        e += 1
        assert e < p * p
    return e
og = unit_order(13, 5, (7, 7))  # phi = (1+sqrt5)/2 = 7 + 7 sqrt5 mod 13
# check: 2*(7,7) = (14,14) == (1,1) mod 13 -> phi transcribed correctly
assert (2 * 7 % 13, 2 * 7 % 13) == (1, 1)
os_ = unit_order(211, 2, (1, 1))
out(f"   ord(phi) in F_13[sqrt5]* = {og}  (2(p+1) = 28: maximal = "
    f"{og == 2 * (13 + 1)})")
out(f"   ord(1+sqrt2) in F_211[sqrt2]* = {os_}  (2(p+1) = 424: maximal = "
    f"{os_ == 2 * (211 + 1)})")
# maximal-order selectivity (recompute the unit mod q per prime)
def phi_mod(q):
    inv2q = pow(2, -1, q)
    return (inv2q % q, inv2q % q)
def max_ord_selector(d, umod, dial):
    for q in PRIMES:
        if q in (2,) or legendre(d, q) != -1:
            continue
        if unit_order(q, d, umod(q)) == 2 * (q + 1):
            return q
    return None
sg = max_ord_selector(5, phi_mod, 13)
ss = max_ord_selector(2, lambda q: (1, 1), 211)
out(f"   smallest inert prime with MAXIMAL unit order: golden {sg} "
    f"(dial 13: {'PASS' if sg == 13 else 'FAIL'}), silver {ss} "
    f"(dial 211: {'PASS' if ss == 211 else 'FAIL'})")
laws.append(("maximal unit order", "golden", 13, sg, sg == 13, ""))
laws.append(("maximal unit order", "silver", 211, ss, ss == 211, ""))
OUT["X_laws"] = [[t, o, d, s, ok, n] for (t, o, d, s, ok, n) in laws]

# ===========================================================================
# STEP 5 -- verdict assembly
# ===========================================================================
out()
out("=" * 78)
out("STEP 5 -- VERDICT ASSEMBLY")
out("=" * 78)
passes = [l for l in laws if l[4]]
fails = [l for l in laws if not l[4]]
out(f"   candidate smallest-prime laws: {len(passes)} PASS / "
    f"{len(fails)} FAIL")
for l in passes:
    out(f"      PASS: {l[0]} ({l[1]})")
silver_own_all_fail = all(sweep[M] != 211 for M in sweep if M < 211
                          and M != 120)
out(f"   every silver-OWN congruence law (2-power and 2^a*3 moduli < 211) "
    f"FAILS: {silver_own_all_fail}")
out(f"   the unique congruence selecting 211 found: mod 120 = 8*3*5 "
    f"(CROSS-OBJECT modulus -- uses the golden conductor 5; HINT, not law)")

# MB12 vacuity/selection analysis of the mod-120 coincidence:
#  - golden PASS is VACUOUS-GRADE: any prime < M is minimal in its class.
#  - silver PASS is non-vacuous (211 > 120) -- quantify its a-priori rarity:
red = [r for r in range(1, 120) if __import__("math").gcd(r, 120) == 1]
no_small = [r for r in red if all(q % 120 != r for q in PRIMES if q < 120)]
first_hit = {r: smallest_with(lambda q, r=r: q % 120 == r) for r in no_small}
out(f"   MB12 guard on mod 120: reduced classes = {len(red)}; classes with")
out(f"   NO prime below 120 = {no_small} ({len(no_small)}/{len(red)});")
out(f"   211 lies in class 91 -- one of only {len(no_small)} classes where")
out(f"   the smallest-prime test is even nontrivial; first primes there: "
    f"{first_hit}")
out(f"   => the mod-120 selection has a-priori weight ~{len(no_small)}/"
    f"{len(red)} x (first-candidate-prime); recorded as HINT, not law.")
OUT["X_mod120_guard"] = {"no_small_classes": no_small,
                         "first_primes": {str(k): v
                                          for k, v in first_hit.items()}}

json.dump(OUT, open(os.path.join(HERE, "cell7_dial_valuations.json"), "w"),
          indent=1)
out("\ncell7_dial_valuations.json written")
out("CELL 7 COMPUTATION COMPLETE")
