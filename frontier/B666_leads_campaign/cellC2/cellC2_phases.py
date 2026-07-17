"""B666 CELL C' — the invariant being-end phase catalogue.

Sealed task (ADDENDUM_1, CELL C'): gauge-fixed quantities ONLY
(cross-ratios, sigma*-eigenvalues, dial deviations); the phase-lattice
question: is every invariant phase in (pi/6)Z (hexagonal / Eisenstein,
golden side) resp. (pi/4)Z (Q(i), silver side)?
Outcomes: lattice-closed (per object) / richer (name the first
non-lattice phase exactly).

Firewall note (binding): the raw 3-form phases and the 24 zeta6 ratio
are GAUGE (B647/B662-F) and appear below ONLY as boolean
parse-transcription locks, never as catalogued content.

THE DICHOTOMY LEMMA used for certification (proved inline, exact):
for z in an imaginary quadratic field K subset C,
    arg(z) in pi*Q  <=>  z/conj(z) is a root of unity in K
                    <=>  z/conj(z) in mu(K)
                    <=>  arg(z) in the lattice
        ((pi/6)Z for K = Q(sqrt(-3)), mu(K) = mu_6;
         (pi/4)Z for K = Q(i),        mu(K) = mu_4).
Proof: z/conj(z) = e^{2i arg z} lies in K and has modulus 1; if
arg z = (p/q) pi then (z/conj z)^q = 1, so z/conj z is a root of unity
of K, i.e. in mu(K) (mu(Q(sqrt(-3))) = mu_6, mu(Q(i)) = mu_4); then
2 arg z in (pi/3)Z resp. (pi/2)Z, i.e. arg z in (pi/6)Z resp (pi/4)Z.
Conversely lattice phases give z/conj(z) in mu(K).  QED
Consequence: every catalogued phase is EITHER exactly on the lattice
OR an irrational multiple of pi — no intermediate root-of-unity phases
can occur.  Each verdict below is certified by the exact rational test
z/conj(z) in mu(K), cross-validated against the exact ray case-split.
"""
import itertools as it
import json
import math
import os
import re
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
B637 = os.path.join(REPO, "frontier", "B637_corrected_cell3")
B649 = os.path.join(REPO, "frontier", "B649_silver_holonomy")
CELLC = os.path.join(REPO, "frontier", "B662_successor_campaign", "cellC")

CATALOGUE = []  # rows for the JSON artifact


# ---------------------------------------------------------------------------
# exact K-arithmetic: z = (x, y) means x + y*delta, delta^2 = D (D = -3, -1)
# ---------------------------------------------------------------------------
def kmul(u, v, D):
    (a, b), (c, d) = u, v
    return (a * c + D * b * d, a * d + b * c)


def kconj(u):
    return (u[0], -u[1])


def knorm(u, D):
    return u[0] * u[0] - D * u[1] * u[1]


def kdiv(u, v, D):
    n = knorm(v, D)
    w = kmul(u, kconj(v), D)
    return (w[0] / n, w[1] / n)


MU6 = [(Fr(1), Fr(0)), (Fr(1, 2), Fr(1, 2)), (Fr(-1, 2), Fr(1, 2)),
       (Fr(-1), Fr(0)), (Fr(-1, 2), Fr(-1, 2)), (Fr(1, 2), Fr(-1, 2))]
MU4 = [(Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(-1), Fr(0)), (Fr(0), Fr(-1))]


def lattice_k_sqrtm3(x, y):
    """arg(x + y sqrt(-3)) = k*pi/6 with k in (-6, 6]; None if off-ray."""
    if x == 0 and y == 0:
        raise ValueError("zero has no phase")
    if y == 0:
        return 0 if x > 0 else 6
    if x == 0:
        return 3 if y > 0 else -3
    if x == y:
        return 2 if x > 0 else -4
    if x == -y:
        return -2 if x > 0 else 4
    if x == 3 * y:
        return 1 if y > 0 else -5
    if x == -3 * y:
        return 5 if y > 0 else -1
    return None


def lattice_k_i(x, y):
    """arg(x + y i) = k*pi/4 with k in (-4, 4]; None if off-ray."""
    if x == 0 and y == 0:
        raise ValueError("zero has no phase")
    if y == 0:
        return 0 if x > 0 else 4
    if x == 0:
        return 2 if y > 0 else -2
    if x == y:
        return 1 if x > 0 else -3
    if x == -y:
        return -1 if x > 0 else 3
    return None


def phase_report(tag, name, z, field, note=""):
    """field: 'sqrt-3' (lattice pi/6, mu6) or 'i' (lattice pi/4, mu4).
    Certifies via BOTH the ray case-split and the mu(K) dichotomy test;
    asserts they agree. Returns True iff lattice."""
    x, y = z
    if field == "sqrt-3":
        D, mu, latfn, denom = -3, MU6, lattice_k_sqrtm3, 6
        zf = float(x) + float(y) * math.sqrt(3) * 1j
        rep = f"{x} + ({y})*sqrt(-3)"
    else:
        D, mu, latfn, denom = -1, MU4, lattice_k_i, 4
        zf = float(x) + float(y) * 1j
        rep = f"{x} + ({y})*i"
    if x == 0 and y == 0:
        print(f"  [{tag}] {name} = 0 (no phase; excluded)")
        return None
    k = latfn(x, y)
    unit = kdiv(z, kconj(z), D)      # z/conj(z), exact in K
    in_mu = unit in mu
    assert (k is not None) == in_mu, (tag, name, k, unit)
    argf = math.atan2(zf.imag, zf.real)
    if k is not None:
        verdict = f"LATTICE  arg = {k}*pi/{denom}"
        ok = True
    else:
        verdict = (f"NON-LATTICE  (z/conj(z) = {unit[0]} + ({unit[1]})*delta"
                   f" is NOT a root of unity => arg is an IRRATIONAL"
                   f" multiple of pi)")
        ok = False
    print(f"  [{tag}] {name}")
    print(f"        value = {rep}")
    print(f"        arg (float, display only) = {argf:+.12f} rad"
          f" = {math.degrees(argf):+.9f} deg")
    print(f"        {verdict}{('  ' + note) if note else ''}")
    CATALOGUE.append({
        "tag": tag, "object": name, "field": field,
        "x": str(x), "y": str(y),
        "lattice": ok, "k": k,
        "lattice_denominator": denom,
        "z_over_conj_z": [str(unit[0]), str(unit[1])],
        "note": note})
    return ok


# ---------------------------------------------------------------------------
# PART 1 — GOLDEN: the nine doubles' normalization-free invariants (B645)
# ---------------------------------------------------------------------------
print("=" * 78)
print("PART 1 — GOLDEN (fig-8) cross-ratio invariants over Q(sqrt(-3))")
print("=" * 78)

VAL = re.compile(r"Y\[\((\d), (\d), (\d)\)\] = (.+)$")


def parse_val(s):
    s = s.strip()
    if s == "0":
        return (Fr(0), Fr(0))
    m = re.match(r"\((-?\d+(?:/\d+)?)\+(-?\d+(?:/\d+)?)r\)", s)
    assert m, s
    return (Fr(m.group(1)), Fr(m.group(2)))


def parse_tables(path, headers):
    txt = open(path).read().splitlines()
    tabs, cur = {}, None
    for ln in txt:
        for h, name in headers:
            if h in ln:
                cur = name
                tabs[cur] = {}
        m = VAL.search(ln)
        if m and cur is not None:
            tabs[cur][(int(m.group(1)), int(m.group(2)),
                       int(m.group(3)))] = parse_val(m.group(4))
    return tabs


T = {}
T.update(parse_tables(
    os.path.join(B637, "stage3_output.txt"),
    [("phi(a)=a:", "Dphi_a"), ("phi(a)=A:", "Dphi_Ainv"),
     ("phi(a)=b:", "Dphi_b"), ("phi(a)=B:", "Dphi_Binv"),
     ("unbent weld table", "weld_none")]))
T.update(parse_tables(
    os.path.join(B637, "part2b_stage2_fixed_output.txt"),
    [("D_bent(M; m=1):", "bent_m1"), ("D_bent(M; m=5):", "bent_m5"),
     ("D_bent(M; m=7):", "bent_m7"), ("D_bent(M; m=11):", "bent_m11")]))
print(f"parsed doubles: {sorted(T)} (expect 9)")
assert len(T) == 9
for k_, tab in T.items():
    assert len(tab) == 10, (k_, len(tab))

# parse-transcription lock (GAUGE machinery only — the ratio itself is
# gauge per B647/B662-F and is NOT catalogued): Y[023] = 24 zeta6 Y[123].
z6 = (Fr(1, 2), Fr(1, 2))  # zeta6 = (1 + sqrt(-3))/2
lock_ok = all(
    T[k_][(0, 2, 3)] == kmul((Fr(24), Fr(0)),
                             kmul(z6, T[k_][(1, 2, 3)], -3), -3)
    for k_ in T)
print(f"parse lock (gauge machinery only, not catalogued): "
      f"core-law transcription holds on 9/9: {lock_ok}")
assert lock_ok

# the two named invariant exponent vectors (B645's banked generators):
#   inv1 = (Y023 * Y124)/(Y024 * Y123)   [the 124-type]
#   inv2 = (Y023 * Y134)/(Y034 * Y123)   [the 134-type, the unit law's]
INV1 = {(0, 2, 3): 1, (1, 2, 4): 1, (0, 2, 4): -1, (1, 2, 3): -1}
INV2 = {(0, 2, 3): 1, (1, 3, 4): 1, (0, 3, 4): -1, (1, 2, 3): -1}


def eval_inv(tab, expvec, D=-3):
    num, den = (Fr(1), Fr(0)), (Fr(1), Fr(0))
    for slot, e in expvec.items():
        v = tab[slot]
        assert v != (Fr(0), Fr(0)), (slot, "zero slot in invariant")
        if e > 0:
            for _ in range(e):
                num = kmul(num, v, D)
        else:
            for _ in range(-e):
                den = kmul(den, v, D)
    return kdiv(num, den, D)


def incidence_rank_check(tab, expected_rank, gens):
    nz = [s for s in sorted(tab) if tab[s] != (Fr(0), Fr(0))]
    M = sp.Matrix([[1 if i in s else 0 for s in nz] for i in range(5)])
    null = M.nullspace()
    assert len(null) == expected_rank, (expected_rank, len(null))
    # certify each named generator IS an invariant: exponent vector
    # lies in ker(incidence)
    for g in gens:
        v = sp.Matrix([g.get(s, 0) for s in nz])
        assert (M * v).is_zero_matrix, ("generator not invariant", g)
    return nz


SILENT = ["Dphi_Binv", "Dphi_b", "bent_m11", "bent_m5", "bent_m7",
          "weld_none"]
LIT = ["Dphi_a", "Dphi_Ainv", "bent_m1"]

print("\n-- the 024-silent class (6 doubles): the unit cross-ratio law --")
for name in SILENT:
    nz = incidence_rank_check(T[name], 1, [INV2])
    v = eval_inv(T[name], INV2)
    assert v == (Fr(1), Fr(0)), (name, v)
    phase_report("G-SIL", f"{name}: inv2 = (Y023*Y134)/(Y034*Y123)", v,
                 "sqrt-3", note="(the unit cross-ratio law, exact = 1)")

print("\n-- the 024-lit class (3 doubles): invariant VALUES --")
lit_vals = {}
for name in LIT:
    incidence_rank_check(T[name], 2, [INV1, INV2])
    v1 = eval_inv(T[name], INV1)
    v2 = eval_inv(T[name], INV2)
    lit_vals[name] = (v1, v2)
    phase_report("G-LIT", f"{name}: inv1 = (Y023*Y124)/(Y024*Y123)", v1,
                 "sqrt-3")
    phase_report("G-LIT", f"{name}: inv2 = (Y023*Y134)/(Y034*Y123)", v2,
                 "sqrt-3")

# locks against the banked B645 normal forms
assert lit_vals["Dphi_a"] == lit_vals["Dphi_Ainv"]
assert lit_vals["Dphi_a"][0] == (Fr(7379, 7392), Fr(13, 7392))
assert lit_vals["Dphi_a"][1] == (Fr(6561, 6574), Fr(13, 6574))
assert lit_vals["bent_m1"][0] == (Fr(3709, 3696), Fr(0))
assert lit_vals["bent_m1"][1] == (Fr(21952107, 21866138),
                                  Fr(169, 21866138))
print("locks vs the banked B645 normal forms (incl. 3^8+13sqrt(-3) over"
      " 3^8+13): ALL PASS")

print("\n-- the 024-lit class: DEVIATIONS from 1 (the 13-dial objects) --")
one = (Fr(1), Fr(0))
for name in LIT:
    for label, v in zip(("inv1", "inv2"), lit_vals[name]):
        dev = (v[0] - 1, v[1])
        phase_report("G-DEV", f"{name}: {label} - 1", dev, "sqrt-3")
        # 13-divisibility lock (numerators of both components, lowest terms)
        for c in dev:
            if c != 0:
                assert c.numerator % 13 == 0, (name, label, c)
                assert c.denominator % 13 != 0, (name, label, c)
print("13-dial lock: every deviation component numerator divisible by 13,"
      " every denominator 13-free: PASS")

# the unique off-lattice deviation, in named exact form
dev4 = (lit_vals["bent_m1"][1][0] - 1, lit_vals["bent_m1"][1][1])
assert dev4 == (Fr(85969, 21866138), Fr(169, 21866138))
assert 85969 == 13 * 6613 and 169 == 13 * 13
print("bent_m1 inv2 - 1 = (13/21866138)*(6613 + 13*sqrt(-3)) exactly:"
      " the two-unit mix 6613*[1] + 13*[sqrt(-3)]")

print("\n-- the 13-dial deviation unit alphabet {1, zeta3, sqrt(-3)} --")
phase_report("G-UNIT", "dial unit 1", (Fr(1), Fr(0)), "sqrt-3")
phase_report("G-UNIT", "dial unit zeta3 = (-1+sqrt(-3))/2",
             (Fr(-1, 2), Fr(1, 2)), "sqrt-3")
phase_report("G-UNIT", "dial unit sqrt(-3)", (Fr(0), Fr(1)), "sqrt-3")

# ---------------------------------------------------------------------------
# PART 2 — GOLDEN sigma*-matrix (persisted; B638 swap eigenvalues)
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("PART 2 — GOLDEN sigma* (sigma_matrix_golden.json; B638 G2 spectrum)")
print("=" * 78)

GJ = json.load(open(os.path.join(CELLC, "sigma_matrix_golden.json")))
GM = [[(Fr(e[0]), Fr(e[1])) for e in row] for row in GJ["matrix"]]


def mat_mul(Amat, Bmat, D):
    n = len(Amat)
    out = [[(Fr(0), Fr(0))] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            acc = (Fr(0), Fr(0))
            for k2 in range(n):
                p = kmul(Amat[i][k2], Bmat[k2][j], D)
                acc = (acc[0] + p[0], acc[1] + p[1])
            out[i][j] = acc
    return out


def mat_conj(Amat):
    return [[kconj(e) for e in row] for row in Amat]


def is_identity(Amat):
    n = len(Amat)
    return all(Amat[i][j] == ((Fr(1), Fr(0)) if i == j else (Fr(0), Fr(0)))
               for i in range(n) for j in range(n))


# law verification (antilinear involution, row convention):
# sigma*^2 = conj(M).M  (and the json also claims M.conj(M) = I)
assert is_identity(mat_mul(mat_conj(GM), GM, -3))
assert is_identity(mat_mul(GM, mat_conj(GM), -3))
tri = all(GM[i][j] == (Fr(0), Fr(0))
          for i in range(5) for j in range(i + 1, 5))
print(f"conj(M).M = I exact: True;  M.conj(M) = I exact: True;"
      f"  lower-triangular: {tri}")
assert tri

gdiag = [GM[i][i] for i in range(5)]
expect = [(Fr(1, 2), Fr(1, 2)), (Fr(1, 2), Fr(-1, 2)),
          (Fr(-1, 2), Fr(-1, 2)), (Fr(-1, 2), Fr(1, 2)), (Fr(1), Fr(0))]
assert gdiag == expect
print("diagonal = (zeta6, conj zeta6, -zeta6, -conj zeta6, 1) exact"
      " (B638 G2 lock)")
names6 = ["zeta6", "conj(zeta6)", "-zeta6", "-conj(zeta6)", "1"]
for nm, d in zip(names6, gdiag):
    phase_report("G-SIG", f"sigma* diagonal (as persisted) {nm}", d,
                 "sqrt-3",
                 note="[GAUGE-SLACK per Hilbert 90 — see below]")

# Hilbert-90 gauge status (the banked B649 sharpening, verified here):
# each |d| = 1 diagonal entry of an ANTILINEAR involution rescales as
# d -> d*conj(lam)/lam under rep_i -> lam*rep_i; lam = 1 + conj(d)
# (or lam = i if d = -1) gauges d to 1.  So the diagonal phases are
# BASIS-GAUGE, not invariant content.
for nm, d in zip(names6, gdiag):
    assert knorm(d, -3) == 1
    lam = (1 + d[0], -d[1]) if d != (Fr(-1), Fr(0)) else (Fr(0), Fr(1))
    assert kdiv(kconj(lam), lam, -3) == d, (nm, d)
print("Hilbert-90 gauge exhibited for EVERY diagonal entry"
      " (lam with conj(lam)/lam = d, so d gauges to 1): the sigma*"
      " diagonal phases are GAUGE, not invariant content (B649 note,"
      " verified).")

# the basis-INVARIANT residue of sigma*: the R-linear spectrum.
# T(v) = M^T conj(v); on R^10 (v = p + i q, entries a + b*sqrt(3)*i):
s3 = sp.sqrt(3)
A_ = sp.Matrix(5, 5, lambda i, j: sp.Rational(str(GM[j][i][0])))
B_ = sp.Matrix(5, 5, lambda i, j: sp.Rational(str(GM[j][i][1])) * s3)
Rr = sp.Matrix(sp.BlockMatrix([[A_, B_], [B_, -A_]]))
assert (Rr * Rr - sp.eye(10)).is_zero_matrix
rp = (Rr - sp.eye(10)).rank()
rm = (Rr + sp.eye(10)).rank()
print(f"R-linear involution T(v) = M^T conj(v): T^2 = I exact;"
      f" eigenvalue multiplicities: +1 x {10 - rp}, -1 x {10 - rm}")
assert (10 - rp, 10 - rm) == (5, 5)
phase_report("G-SIG-INV", "sigma* R-spectrum eigenvalue +1 (mult 5)",
             (Fr(1), Fr(0)), "sqrt-3", note="[basis-invariant]")
phase_report("G-SIG-INV", "sigma* R-spectrum eigenvalue -1 (mult 5)",
             (Fr(-1), Fr(0)), "sqrt-3", note="[basis-invariant]")
print("swap scalar u*conj(u) = +1 (B638 G1, J^2 = +1): phase 0"
      " [basis-invariant]")
phase_report("G-SIG-INV", "J^2 scalar +1", (Fr(1), Fr(0)), "sqrt-3",
             note="[basis-invariant]")

# ---------------------------------------------------------------------------
# PART 3 — SILVER sigma*-matrix (sigma_matrix_L.json, Q(i))
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("PART 3 — SILVER sigma* (sigma_matrix_L.json) over Q(i)")
print("=" * 78)

SJ = json.load(open(os.path.join(B649, "sigma_matrix_L.json")))
# entry = 8-vector over basis (1, s, s^2, s^3, i, i s, i s^2, i s^3)
SM = []
for row in SJ:
    r_ = []
    for e in row:
        assert all(Fr(e[t]) == 0 for t in (1, 2, 3, 5, 6, 7)), e
        r_.append((Fr(e[0]), Fr(e[4])))
    SM.append(r_)
print("s-freeness of every entry: PASS (the matrix is defined over Q(i),"
      " the silver's imaginary quadratic subfield — B649 3b-i lock)")

assert is_identity(mat_mul(mat_conj(SM), SM, -1))
assert is_identity(mat_mul(SM, mat_conj(SM), -1))
tri = all(SM[i][j] == (Fr(0), Fr(0))
          for i in range(5) for j in range(i + 1, 5))
print(f"conj(C).C = I exact: True;  C.conj(C) = I exact: True;"
      f"  lower-triangular: {tri}")
assert tri

sdiag = [SM[i][i] for i in range(5)]
d0, d1 = sdiag[0], sdiag[1]
assert sdiag[2:] == [(Fr(1), Fr(0)), (Fr(-1), Fr(0)), (Fr(1), Fr(0))]
assert knorm(d0, -1) == 1 and knorm(d1, -1) == 1
print(f"diagonal = (d0, d1, 1, -1, 1) with |d0| = |d1| = 1 exact:")
print(f"  d0 = {d0[0]} + ({d0[1]})*i")
print(f"  d1 = {d1[0]} + ({d1[1]})*i")
silver_names = ["d0", "d1", "1", "-1", "1"]
for nm, d in zip(silver_names, sdiag):
    phase_report("S-SIG", f"sigma* diagonal (as persisted) {nm}", d, "i",
                 note="[GAUGE-SLACK per Hilbert 90 — see below]")
for nm, d in zip(silver_names, sdiag):
    lam = (1 + d[0], -d[1]) if d != (Fr(-1), Fr(0)) else (Fr(0), Fr(1))
    assert kdiv(kconj(lam), lam, -1) == d, (nm, d)
print("Hilbert-90 gauge exhibited for EVERY diagonal entry (incl. the"
      " off-lattice d0, d1): all gauge to 1 — the silver diagonal phases"
      " are GAUGE, not invariant content (B649's banked sharpening,"
      " re-verified).")

A_ = sp.Matrix(5, 5, lambda i, j: sp.Rational(str(SM[j][i][0])))
B_ = sp.Matrix(5, 5, lambda i, j: sp.Rational(str(SM[j][i][1])))
Rr = sp.Matrix(sp.BlockMatrix([[A_, B_], [B_, -A_]]))
assert (Rr * Rr - sp.eye(10)).is_zero_matrix
rp = (Rr - sp.eye(10)).rank()
rm = (Rr + sp.eye(10)).rank()
print(f"R-linear involution: T^2 = I exact; eigenvalue multiplicities:"
      f" +1 x {10 - rp}, -1 x {10 - rm}")
assert (10 - rp, 10 - rm) == (5, 5)
phase_report("S-SIG-INV", "sigma* R-spectrum eigenvalue +1 (mult 5)",
             (Fr(1), Fr(0)), "i", note="[basis-invariant]")
phase_report("S-SIG-INV", "sigma* R-spectrum eigenvalue -1 (mult 5)",
             (Fr(-1), Fr(0)), "i", note="[basis-invariant]")

# ---------------------------------------------------------------------------
# PART 4 — SILVER Y invariants (silver_Y_L.json, cross-ratio level)
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("PART 4 — SILVER Y cross-ratio invariants over Q(i)")
print("=" * 78)

YJ = json.load(open(os.path.join(B649, "silver_Y_L.json")))
Ys = {}
for key, vec in YJ.items():
    assert all(Fr(vec[t]) == 0 for t in (1, 2, 3, 5, 6, 7)), (key, vec)
    slot = tuple(int(c) for c in key)
    Ys[slot] = (Fr(vec[0]), Fr(vec[4]))
print("s-freeness of every Y value: PASS (the silver chord lives in Q(i))")

zero_slots = [s for s in sorted(Ys) if Ys[s] == (Fr(0), Fr(0))]
assert zero_slots == [(0, 1, 2), (0, 1, 3), (0, 1, 4)]
print(f"zero law: Y[01k] = 0 exactly, 3/3 (nonzero slots: 7)")

nz = incidence_rank_check(Ys, 2, [INV1, INV2])
print(f"incidence rank over the 7 nonzero slots: invariant rank 2;"
      f" inv1/inv2 exponent vectors certified in ker(incidence)")

sv1 = eval_inv(Ys, INV1, D=-1)
sv2 = eval_inv(Ys, INV2, D=-1)
# locks vs the banked b649_g3_analysis.txt values (independent transcription)
G3_CR2 = (Fr(1775661509660642434903313, 1775664925937025369121636),
          Fr(9285580552058180539, 1775664925937025369121636))
G3_CR1 = (Fr(16271648481252971729, 16271671961969963216),
          Fr(-369110590776791, 178988391581669595376))
assert sv2 == G3_CR2, sv2
assert sv1 == G3_CR1, sv1
print("locks vs the banked B649 G3 analysis values: BOTH PASS")

print("\n-- the silver unbent-weld double (LIT class): invariant VALUES --")
phase_report("S-CR", "silver inv1 = (Y023*Y124)/(Y024*Y123)", sv1, "i")
phase_report("S-CR", "silver inv2 = (Y023*Y134)/(Y034*Y123)", sv2, "i")

print("\n-- silver deviations from 1 (the 211-dial objects) --")
sdev1 = (sv1[0] - 1, sv1[1])
sdev2 = (sv2[0] - 1, sv2[1])
phase_report("S-DEV", "silver inv1 - 1", sdev1, "i")
phase_report("S-DEV", "silver inv2 - 1", sdev2, "i")
# the banked adic locks: every deviation numerator divisible by 211;
# inv2's two components also by 13; denominators 13- and 211-free.
for c in sdev2:
    assert c.numerator % (13 * 211) == 0 and c.denominator % 13 != 0 \
        and c.denominator % 211 != 0, c
for c in sdev1:
    assert c.numerator % 211 == 0 and c.denominator % 211 != 0, c
assert sdev2[0].numerator == -13 * 211 * 647 * 1924965322963
assert sdev2[1].numerator == 13 * 211 * 15441731 * 219223583
print("211/13-dial locks (banked factorizations re-multiplied exactly):"
      " ALL PASS")

# ---------------------------------------------------------------------------
# PART 5 — the catalogue summary + verdicts
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("PART 5 — THE PHASE CATALOGUE SUMMARY")
print("=" * 78)
inv_rows = [r for r in CATALOGUE if "GAUGE-SLACK" not in r["note"]]
gauge_rows = [r for r in CATALOGUE if "GAUGE-SLACK" in r["note"]]
gold = [r for r in inv_rows if r["field"] == "sqrt-3"]
silv = [r for r in inv_rows if r["field"] == "i"]
gold_off = [r for r in gold if not r["lattice"]]
silv_off = [r for r in silv if not r["lattice"]]
print(f"invariant-content rows: golden {len(gold)} ({len(gold_off)}"
      f" off-lattice), silver {len(silv)} ({len(silv_off)} off-lattice);"
      f" gauge-slack rows (catalogued, firewalled): {len(gauge_rows)}")
print("\nGOLDEN off-lattice invariant phases:")
for r in gold_off:
    print(f"  {r['object']}: {r['x']} + ({r['y']})*sqrt(-3)")
print("\nSILVER off-lattice invariant phases:")
for r in silv_off:
    print(f"  {r['object']}: {r['x']} + ({r['y']})*i")

print("""
VERDICT (two-outcome, per object):
  GOLDEN: RICHER — the invariant phase catalogue is NOT contained in
    (pi/6)Z.  First non-lattice phase, named exactly: the lit-class
    cross-ratio inv1 on D_phi(a)=a,
        arg( 7379/7392 + (13/7392) sqrt(-3) ) = arctan(13 sqrt(3)/7379),
    and the seal's exemplar inv2 = (3^8 + 13 sqrt(-3))/(3^8 + 13) with
        arg = arctan(13 sqrt(3) / 3^8)  —
    both certified irrational multiples of pi (z/conj z not a root of
    unity in Q(sqrt(-3))).
  SILVER: RICHER — first non-lattice phase, named exactly: the silver
    unbent-weld cross-ratio inv1 = (Y023*Y124)/(Y024*Y123), arg an
    irrational multiple of pi (certified); inv2 likewise.
STRUCTURE INSIDE THE VERDICT:
  - the silent-class invariants (6/6 golden) sit at phase 0 exactly;
  - the golden deviation ledger is lattice on 3 of 4 rows
    (13/3696 -> 0; 13 zeta3/3696 and 13 zeta3/3287 -> 2pi/3); the
    UNIQUE off-lattice golden deviation is bent_m1 inv2 - 1 =
    (13/21866138)(6613 + 13 sqrt(-3)) — the first two-unit mix
    (6613*[1] + 13*[sqrt(-3)]) of the lattice alphabet {1, zeta3,
    sqrt(-3)};
  - the silver deviations are off-lattice already at both rows (the
    211-dial mixes);
  - the sigma* diagonals ((zeta6,...,1) golden; (d0, d1, 1, -1, 1)
    silver) are GAUGE per Hilbert 90 (gauge exhibited entrywise): the
    golden's lattice look and the silver's off-lattice look are both
    basis-chosen; the basis-invariant sigma* content is the real
    structure J^2 = +1 with R-spectrum {+1 x5, -1 x5} (phases {0, pi},
    lattice-trivial) and the field of definition;
  - THE DICHOTOMY (proved): every invariant phase over the object's
    imaginary quadratic field is EITHER on the object's lattice
    ((pi/6)Z golden, (pi/4)Z silver) OR an irrational multiple of pi —
    no finer root-of-unity phases can occur.  "Richer" here means
    irrational-angle, not a finer lattice.
""")

json.dump({"cell": "B666-C'",
           "question": "is every invariant phase in (pi/6)Z (golden)"
                       " / (pi/4)Z (silver)?",
           "verdict": {"golden": "RICHER", "silver": "RICHER"},
           "dichotomy": "lattice-or-irrational-multiple-of-pi"
                        " (mu(K) lemma, certified per row)",
           "rows": CATALOGUE},
          open(os.path.join(HERE, "phase_catalogue.json"), "w"), indent=1)
print("phase_catalogue.json written")
print("CELL C' DONE")
