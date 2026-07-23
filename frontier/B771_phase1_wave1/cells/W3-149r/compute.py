#!/usr/bin/env python3
"""
W3-149r (B174 genus-2 sole-kappa): ACTUALLY RUN THE NEGATIVE CONTROL (wave-2 carry).

DEFECT BEING FIXED (FINDINGS_WAVE2.md row W2-149, "fabricated control"):
  W2-149/compute.py's "C3: necessity control" NEVER attempted a genus-2 construction with
  mismatched kappa at all. Its `try_witness()` has an internal guard
      if k1 != kN: return "SKIP"
  and C3 just counted how many draws hit that guard ("90/90 blocked") -- a TAUTOLOGY: the
  code is *written* to bail on mismatch, so of course every mismatched draw is "blocked".
  No matrix was ever built, no product was ever multiplied, no genuine failure was ever
  observed. The wave-2 summary further claims "12 genuine FAILUREs" for this control --
  that string/number appears NOWHERE in W2-149/compute.py or W2-149/output.txt. Fabricated.

THIS CELL: build the wrong-gluing (M1 vs M2, kappa1 != kappa2) construction FOR REAL --
remove the early trace-equality bailout, force the SAME diagonalize-and-glue machinery
through to an actual 2x2 matrix identity check, on genuinely mismatched (x1,y1,z1) vs
(x2,y2,z2), and report the ACTUAL count of constructed-and-checked attempts that fail.
Three independent negative-control channels + one symbolic proof + one paired vacuity
self-test, so the result cannot be an artifact of one code path or one lucky sample.

QUESTION (screening, carried from B174/W2-149, OPEN_LEADS H5-a):
  Is kappa = tr([A1,B1]) = tr([A2,B2]) the SOLE coupling between leaf-1 and leaf-2 on the
  glued genus-2 surface [A1,B1][A2,B2]=I? The positive half (kappa-matched => witness exists)
  was already constructively verified in W2-149/C2 (that part is a real construction, not the
  defect). The MISSING half is the negative control: kappa-MISMATCHED => NO witness, actually
  attempted and actually observed to fail (not asserted by a guard clause).

METHOD:
  S0. Exact symbolic proof (sympy, generic 2x2 entries as free symbols, no numeric substitution):
      tr(h M h^-1) = tr(M) identically, and tr(M^-1) = tr(M) when det M = 1. This is the exact
      algebraic reason mismatched kappa CANNOT glue under ANY conjugator -- established in-cell,
      not cited.
  S1. Numeric negative control, diagonalize-based "blind" construction: build M1=[A1,B1] (trace
      k1) and M2'=[A2,B2'] (trace k2, k1!=k2 verified by direct computation on genuinely
      independently-drawn triples). Diagonalize M1^-1 at ITS OWN eigenvalue t1 and M2' at ITS OWN
      eigenvalue t2 (no forcing t1=t2), build h_s = P1.diag(s,1/s).P2^-1 for the twist s exactly as
      the positive construction does, and ACTUALLY multiply [A1,B1]*(h M2' h^-1) and compare to I.
      Every non-degenerate attempt is counted; report the REAL failure count.
  S2. Positive-control sanity on the SAME code path (kappa-matched, same function, no special
      casing) -- must succeed, proving S1's failures are not a blanket "always False" bug.
  S3. Independent brute-force control: sample random invertible conjugators h directly from
      GL(2,GF(p)) (bypassing the diagonalize construction entirely) for mismatched-kappa pairs,
      and confirm zero successes over a large sample -- model-independent of S1's construction.
  S4. Paired vacuity self-test: for ONE fixed (x1,y1,z1,x2,y2) draw, solve z2 TWO ways -- kappa-
      matched (z2_match) and deliberately kappa-mismatched (z2_mismatch = z2_match + 1 mod p,
      re-checked to differ in kappa) -- run the IDENTICAL code on both and confirm the outcome
      flips (match succeeds, mismatch fails). This rules out kappa being a "free symbol" that
      the check doesn't actually depend on.

VERDICT RULE:
  S0 proof exact AND S1 shows >=1 genuine (non-skip) mismatched attempt with 100% failure AND
  S2 shows the same code succeeds on matched kappa (>0 successes) AND S3 shows 0/N successes on
  an independent random-h sample AND S4's paired flip holds
    => RESOLVED-A: the negative control is REAL and CONFIRMS kappa-mismatch is a genuine,
       actually-observed obstruction (upgrades W2-149's fabricated "90/90 blocked" claim to a
       real computed fact; the original sole-kappa screening verdict now rests on real evidence).
  Any mismatched-kappa trial actually SUCCEEDS (a real witness with kappa1 != kappa2)
    => RESOLVED-B: sole-kappa claim REFUTED (a hidden extra coupling exists / kappa is not
       necessary).
  Too few non-degenerate mismatched trials to say anything (all SKIP) => UNRESOLVED.

FIREWALL: character-variety / low-dim-topology mathematics (K010 boundary, emergent); no scale,
Lambda, mass, or physical constant; nothing to CLAIMS.md.
"""
import random
import sympy
from sympy import symbols, Matrix, simplify, expand, eye as sympy_eye
from sympy.ntheory.residue_ntheory import sqrt_mod

ok_all = True
def chk(name, cond, x=""):
    global ok_all
    ok_all = ok_all and bool(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  {x}" if x else ""))

# ---------------------------------------------------------------- mod-p 2x2 matrix helpers
def mm(A, B, p):
    return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % p, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % p],
            [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % p, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % p]]

def tr(A, p):
    return (A[0][0] + A[1][1]) % p

def det(A, p):
    return (A[0][0]*A[1][1] - A[0][1]*A[1][0]) % p

def inv_sl2(A, p):
    return [[A[1][1] % p, (-A[0][1]) % p], [(-A[1][0]) % p, A[0][0] % p]]

def inv_gl2(A, p):
    d = det(A, p)
    if d == 0:
        return None
    dinv = pow(d, -1, p)
    return [[(A[1][1]*dinv) % p, (-A[0][1]*dinv) % p], [(-A[1][0]*dinv) % p, (A[0][0]*dinv) % p]]

def eye(p):
    return [[1, 0], [0, 1]]

def mat_eq(A, B, p):
    return all((A[i][j] - B[i][j]) % p == 0 for i in range(2) for j in range(2))

def kappa_of(x, y, z, p):
    return (x*x + y*y + z*z - x*y*z - 2) % p

def fricke_build(x, y, z, p):
    x, y, z = x % p, y % p, z % p
    disc = (z*z - 4) % p
    try:
        roots = sqrt_mod(disc, p, all_roots=True)
    except Exception:
        roots = None
    if not roots:
        return None
    r = roots[0]
    inv2 = pow(2, -1, p)
    mu = ((z + r) * inv2) % p
    if mu == 0:
        return None
    muinv = pow(mu, -1, p)
    A = [[x, (-1) % p], [1, 0]]
    B = [[0, mu], [(-muinv) % p, y]]
    return A, B, mu

def commutator(A, B, p):
    return mm(mm(A, B, p), mm(inv_sl2(A, p), inv_sl2(B, p), p), p)

def diagonalize(M, p, t):
    a, b = M[0][0] % p, M[0][1] % p
    c, d = M[1][0] % p, M[1][1] % p
    tinv = (tr(M, p) - t) % p
    def eigvec(lam):
        if b % p != 0:
            return (b % p, (lam - a) % p)
        if c % p != 0:
            return ((lam - d) % p, c % p)
        if (a - lam) % p == 0:
            return (1, 0)
        return None
    v1 = eigvec(t)
    v2 = eigvec(tinv)
    if v1 is None or v2 is None:
        return None
    P = [[v1[0] % p, v2[0] % p], [v1[1] % p, v2[1] % p]]
    if det(P, p) == 0:
        return None
    return P, t, tinv

def eigen_t(kappa, p):
    disc = (kappa*kappa - 4) % p
    try:
        roots = sqrt_mod(disc, p, all_roots=True)
    except Exception:
        roots = None
    if not roots:
        return None
    inv2 = pow(2, -1, p)
    return ((kappa + roots[0]) * inv2) % p

# ================================================================== S0: exact symbolic proof
print("== S0: exact symbolic proof -- conjugation preserves trace, det=1 => tr(M^-1)=tr(M) ==")
a, b, c, d, e, f, g, h_ = symbols('a b c d e f g h')
M_sym = Matrix([[a, b], [c, d]])
H_sym = Matrix([[e, f], [g, h_]])
detH = e*h_ - f*g
Hinv = Matrix([[h_, -f], [-g, e]]) / detH   # exact adjugate/det inverse, symbolic, no numeric sub
conj = H_sym * M_sym * Hinv
tr_conj_minus_trM = simplify(expand(conj[0, 0] + conj[1, 1]) - (a + d))
chk("tr(H M H^-1) - tr(M) simplifies to EXACTLY 0 (generic symbolic entries, det H != 0 assumed symbolically)",
    tr_conj_minus_trM == 0, x=f"residual: {tr_conj_minus_trM}")

# tr(M^-1) = tr(M) when det M = 1 (SL2): adjugate inverse is [[d,-b],[-c,a]], trace = a+d, identical.
Minv_sym = Matrix([[d, -b], [-c, a]])   # adjugate = inverse since det M = ad-bc =: forced to 1 below
tr_Minv_minus_trM = simplify((Minv_sym[0, 0] + Minv_sym[1, 1]) - (a + d))
chk("tr(adj(M)) - tr(M) simplifies to EXACTLY 0 (so for det M=1, tr(M^-1)=tr(M) identically)",
    tr_Minv_minus_trM == 0, x=f"residual: {tr_Minv_minus_trM}")
print("  => EXACT CONSEQUENCE: [A2,B2] = h[A2',B2']h^-1 has trace k2 for ANY h (S0a); if")
print("     [A1,B1][A2,B2]=I then [A2,B2]=[A1,B1]^-1 which has trace k1 (S0b). So k1=k2 is")
print("     PROVED necessary for gluing under ANY conjugator, symbolically, not by a guard clause.")

# ============================================================ S1: REAL negative-control construction
print("\n== S1: REAL mismatched-kappa construction attempt (M1 vs M2 directly, no guard-clause bailout) ==")

def attempt_mismatched_glue(x1, y1, z1, x2, y2, z2, p, twist_s):
    """Force the SAME diagonalize-and-glue machinery through for a genuinely mismatched
    (kappa1 != kappa2) pair -- NO early return on kappa mismatch. Diagonalizes M1^-1 at its
    OWN eigenvalue and M2' at ITS OWN eigenvalue (independently), builds h, and ACTUALLY
    checks the closure identity [A1,B1][A2,B2]=I as a real 2x2 matrix comparison.
    Returns 'SKIP' (unrelated degeneracy: non-QR discriminant / parabolic-central / P singular),
    True (construction closed -- would be a genuine counterexample to necessity),
    or False (construction attempted, closure FAILS -- a REAL, OBSERVED failure)."""
    b1 = fricke_build(x1, y1, z1, p)
    b2 = fricke_build(x2, y2, z2, p)
    if b1 is None or b2 is None:
        return "SKIP"
    A1, B1, _ = b1
    A2p, B2p, _ = b2
    M1 = commutator(A1, B1, p)
    M2p = commutator(A2p, B2p, p)
    k1, k2 = tr(M1, p), tr(M2p, p)
    if k1 == k2:
        return "SKIP"  # this function is ONLY for the genuinely-mismatched case (see S2 for matched)
    if k1 in (2, (p - 2) % p) or k2 in (2, (p - 2) % p):
        return "SKIP"  # central/parabolic, unrelated degeneracy (also excluded in the positive control)
    Ntarget = inv_sl2(M1, p)                 # M1^-1, trace k1 (S0b)
    t1 = eigen_t(k1, p)                      # eigenvalue of Ntarget (== eigenvalue of M1)
    t2 = eigen_t(k2, p)                      # eigenvalue of M2p, its OWN trace (NOT forced to k1)
    if t1 is None or t2 is None or t1 == 0 or t2 == 0:
        return "SKIP"
    dg1 = diagonalize(Ntarget, p, t1)
    dg2 = diagonalize(M2p, p, t2)
    if dg1 is None or dg2 is None:
        return "SKIP"
    P1, _, _ = dg1
    P2, _, _ = dg2
    P1inv = inv_gl2(P1, p)
    P2inv = inv_gl2(P2, p)
    if P1inv is None or P2inv is None:
        return "SKIP"
    if twist_s % p == 0:
        return "SKIP"
    sinv = pow(twist_s, -1, p)
    Sdiag = [[twist_s % p, 0], [0, sinv]]
    h = mm(mm(P1, Sdiag, p), P2inv, p)
    hinv = inv_gl2(h, p)
    if hinv is None:
        return "SKIP"
    A2 = mm(mm(h, A2p, p), hinv, p)
    B2 = mm(mm(h, B2p, p), hinv, p)
    # this is the ACTUAL matrix multiplication and comparison -- the real closure check
    lhs = mm(commutator(A1, B1, p), commutator(A2, B2, p), p)
    return mat_eq(lhs, eye(p), p)

random.seed(20260723)
PRIMES = [10007, 20011, 40009, 65521, 100003]
s1_attempts, s1_genuine_failures, s1_unexpected_successes, s1_skips = 0, 0, 0, 0
for p in PRIMES:
    for _ in range(200):
        x1, y1, z1 = random.randrange(2, p - 2), random.randrange(2, p - 2), random.randrange(2, p - 2)
        x2, y2, z2 = random.randrange(2, p - 2), random.randrange(2, p - 2), random.randrange(2, p - 2)
        k1c, k2c = kappa_of(x1, y1, z1, p), kappa_of(x2, y2, z2, p)
        if k1c == k2c:
            continue  # only genuinely mismatched draws feed the negative control
        for s in (random.randrange(2, p - 2), random.randrange(2, p - 2)):
            s1_attempts += 1
            res = attempt_mismatched_glue(x1, y1, z1, x2, y2, z2, p, s)
            if res == "SKIP":
                s1_skips += 1
            elif res is False:
                s1_genuine_failures += 1
            else:
                s1_unexpected_successes += 1

s1_nonskip = s1_attempts - s1_skips
chk("genuinely mismatched trials were actually CONSTRUCTED and CHECKED (not pre-filtered by a guard clause)",
    s1_nonskip >= 50, x=f"{s1_nonskip} non-skip attempts / {s1_attempts} total ({s1_skips} unrelated-degeneracy skips)")
chk("REAL failure count: every non-skip mismatched-kappa construction attempt actually FAILS the closure check",
    s1_unexpected_successes == 0 and s1_genuine_failures == s1_nonskip and s1_genuine_failures > 0,
    x=f"{s1_genuine_failures} genuine FAILUREs / {s1_nonskip} attempted, {s1_unexpected_successes} unexpected successes")

# ============================================================ S2: positive-control sanity (same code path)
print("\n== S2: positive-control sanity -- same machinery, kappa-MATCHED, must succeed (rules out 'always False') ==")

def attempt_matched_glue(x1, y1, z1, x2, y2, z2, p, twist_s):
    """Identical machinery to attempt_mismatched_glue, but for a kappa-MATCHED pair (k1==k2),
    diagonalizing at the SHARED eigenvalue -- this is the positive-construction sanity twin."""
    b1 = fricke_build(x1, y1, z1, p)
    b2 = fricke_build(x2, y2, z2, p)
    if b1 is None or b2 is None:
        return "SKIP"
    A1, B1, _ = b1
    A2p, B2p, _ = b2
    M1 = commutator(A1, B1, p)
    M2p = commutator(A2p, B2p, p)
    k1, k2 = tr(M1, p), tr(M2p, p)
    if k1 != k2:
        return "SKIP"  # this twin is ONLY for the matched case
    if k1 in (2, (p - 2) % p):
        return "SKIP"
    Ntarget = inv_sl2(M1, p)
    t = eigen_t(k1, p)
    if t is None or t == 0:
        return "SKIP"
    dg1 = diagonalize(Ntarget, p, t)
    dg2 = diagonalize(M2p, p, t)
    if dg1 is None or dg2 is None:
        return "SKIP"
    P1, _, _ = dg1
    P2, _, _ = dg2
    P1inv, P2inv = inv_gl2(P1, p), inv_gl2(P2, p)
    if P1inv is None or P2inv is None:
        return "SKIP"
    if twist_s % p == 0:
        return "SKIP"
    sinv = pow(twist_s, -1, p)
    Sdiag = [[twist_s % p, 0], [0, sinv]]
    h = mm(mm(P1, Sdiag, p), P2inv, p)
    hinv = inv_gl2(h, p)
    if hinv is None:
        return "SKIP"
    A2 = mm(mm(h, A2p, p), hinv, p)
    B2 = mm(mm(h, B2p, p), hinv, p)
    lhs = mm(commutator(A1, B1, p), commutator(A2, B2, p), p)
    return mat_eq(lhs, eye(p), p)

s2_attempts, s2_successes, s2_failures, s2_skips = 0, 0, 0, 0
for p in PRIMES:
    for _ in range(150):
        x1, y1 = random.randrange(2, p - 2), random.randrange(2, p - 2)
        z1 = random.randrange(2, p - 2)
        k1 = kappa_of(x1, y1, z1, p)
        x2, y2 = random.randrange(2, p - 2), random.randrange(2, p - 2)
        A2c, B2c = 1, (-x2 * y2) % p
        C2c = (-(k1 - x2*x2 - y2*y2 + 2)) % p
        disc = (B2c*B2c - 4*A2c*C2c) % p
        try:
            roots = sqrt_mod(disc, p, all_roots=True)
        except Exception:
            roots = None
        if not roots:
            continue
        inv2 = pow(2, -1, p)
        z2 = ((-B2c + roots[0]) * inv2) % p
        if kappa_of(x2, y2, z2, p) != k1:
            continue
        s = random.randrange(2, p - 2)
        s2_attempts += 1
        res = attempt_matched_glue(x1, y1, z1, x2, y2, z2, p, s)
        if res == "SKIP":
            s2_skips += 1
        elif res is True:
            s2_successes += 1
        else:
            s2_failures += 1

chk("same code path, kappa-MATCHED: genuine successes occur (rules out an 'always returns False' bug)",
    s2_successes >= 50 and s2_failures == 0, x=f"{s2_successes} successes, {s2_failures} failures / "
    f"{s2_attempts - s2_skips} non-skip attempts ({s2_skips} skips)")

# ============================================================ S3: independent brute random-h control
print("\n== S3: independent brute-force control -- random h in GL(2,GF(p)) directly, mismatched kappa ==")
s3_p = 100003
s3_samples, s3_successes = 0, 0
for _ in range(40):
    x1, y1, z1 = random.randrange(2, s3_p - 2), random.randrange(2, s3_p - 2), random.randrange(2, s3_p - 2)
    x2, y2, z2 = random.randrange(2, s3_p - 2), random.randrange(2, s3_p - 2), random.randrange(2, s3_p - 2)
    if kappa_of(x1, y1, z1, s3_p) == kappa_of(x2, y2, z2, s3_p):
        continue
    b1 = fricke_build(x1, y1, z1, s3_p)
    b2 = fricke_build(x2, y2, z2, s3_p)
    if b1 is None or b2 is None:
        continue
    A1, B1, _ = b1
    A2p, B2p, _ = b2
    for _ in range(25):   # 25 independently-drawn random conjugators per (leaf1,leaf2) pair
        he = [[random.randrange(0, s3_p), random.randrange(0, s3_p)],
              [random.randrange(0, s3_p), random.randrange(0, s3_p)]]
        hinv = inv_gl2(he, s3_p)
        if hinv is None:
            continue
        s3_samples += 1
        A2 = mm(mm(he, A2p, s3_p), hinv, s3_p)
        B2 = mm(mm(he, B2p, s3_p), hinv, s3_p)
        lhs = mm(commutator(A1, B1, s3_p), commutator(A2, B2, s3_p), s3_p)
        if mat_eq(lhs, eye(s3_p), s3_p):
            s3_successes += 1

chk("brute random-h search (model-independent of the diagonalize construction) over mismatched-kappa "
    "pairs: zero successes over a large sample",
    s3_samples >= 200 and s3_successes == 0, x=f"{s3_successes} successes / {s3_samples} random-h attempts")

# ============================================================ S4: paired vacuity self-test
print("\n== S4: paired vacuity self-test -- SAME leaf-1/leaf-2 draw, only kappa2 flipped match<->mismatch ==")
p4 = 100003
paired_ok = False
paired_report = None
random.seed(7)
for _trial in range(400):
    x1_4 = random.randrange(2, p4 - 2)
    y1_4 = random.randrange(2, p4 - 2)
    z1_4 = random.randrange(2, p4 - 2)
    x2_4 = random.randrange(2, p4 - 2)
    y2_4 = random.randrange(2, p4 - 2)
    k1_4 = kappa_of(x1_4, y1_4, z1_4, p4)
    A2c4, B2c4 = 1, (-x2_4 * y2_4) % p4
    C2c4 = (-(k1_4 - x2_4*x2_4 - y2_4*y2_4 + 2)) % p4
    disc4 = (B2c4*B2c4 - 4*A2c4*C2c4) % p4
    try:
        roots4 = sqrt_mod(disc4, p4, all_roots=True)
    except Exception:
        roots4 = None
    if not roots4:
        continue
    inv2_4 = pow(2, -1, p4)
    z2_match = ((-B2c4 + roots4[0]) * inv2_4) % p4
    k2_match = kappa_of(x2_4, y2_4, z2_match, p4)
    z2_mismatch = (z2_match + 1) % p4
    k2_mismatch = kappa_of(x2_4, y2_4, z2_mismatch, p4)
    if k2_match != k1_4 or k2_mismatch == k1_4:
        continue
    res_match = attempt_matched_glue(x1_4, y1_4, z1_4, x2_4, y2_4, z2_match, p4, 12345)
    res_mismatch = attempt_mismatched_glue(x1_4, y1_4, z1_4, x2_4, y2_4, z2_mismatch, p4, 12345)
    if res_match == "SKIP" or res_mismatch == "SKIP":
        continue  # unrelated degeneracy at this seed -- try another draw, don't count as a result
    paired_report = (x1_4, y1_4, z1_4, x2_4, y2_4, z2_match, k2_match, res_match,
                      z2_mismatch, k2_mismatch, res_mismatch)
    paired_ok = (res_match is True) and (res_mismatch is False)
    break
if paired_report:
    (x1_4, y1_4, z1_4, x2_4, y2_4, z2_match, k2_match, res_match,
     z2_mismatch, k2_mismatch, res_mismatch) = paired_report
    print(f"  same (x1,y1,z1,x2,y2)=({x1_4},{y1_4},{z1_4},{x2_4},{y2_4}); z2_match={z2_match} (k2={k2_match}) "
          f"=> {res_match};  z2_mismatch={z2_mismatch} (k2={k2_mismatch}) => {res_mismatch}")
else:
    print("  no non-degenerate paired seed found in 400 tries")
chk("flipping ONLY kappa2 (via z2) on an otherwise IDENTICAL draw flips the outcome success<->failure "
    "(kappa is the actual controlling variable, not a free/unused symbol)",
    paired_ok)

# ================================================================== verdict
print("\n" + "="*78)
print("VERDICT")
print("="*78)
if ok_all:
    print(f"""RESOLVED-A: the wrong-gluing negative control is REAL and CONFIRMS necessity.

S0 (exact, symbolic): tr(H M H^-1) = tr(M) identically and tr(M^-1) = tr(M) for det M = 1 --
proved with free symbolic matrix entries, not asserted. Consequence: [A2,B2] always has trace
k2 regardless of the conjugator h, and closure [A1,B1][A2,B2]=I forces trace k1; so k1=k2 is
an exact algebraic necessity, established in-cell.

S1 (the actual carry fix): {s1_genuine_failures} genuine, ACTUALLY-CONSTRUCTED failures out of
{s1_nonskip} non-skip mismatched-kappa attempts across {len(PRIMES)} primes -- every one of them built
real Fricke matrices, diagonalized, formed h, conjugated, multiplied the commutators, and
compared to I, and every one of them FAILED the closure check (0 unexpected successes). This
replaces W2-149's fabricated "90/90 blocked" guard-clause count (and its nowhere-appearing "12
genuine FAILUREs" claim) with a real, non-vacuous, non-tautological negative control.

S2: the identical code path SUCCEEDS on kappa-matched input ({s2_successes} successes, 0 failures)
-- S1's failures are not an "always False" artifact.

S3: an independent brute-force search over random conjugators in GL(2,GF(p)) (bypassing the
diagonalize construction entirely) found 0/{s3_samples} successes on mismatched-kappa pairs --
model-independent confirmation.

S4: flipping ONLY kappa2 (via a +1 shift in z2) on an otherwise identical draw flips the outcome
match(True) <-> mismatch(False) -- kappa genuinely controls the result (not a free/unused symbol).

CONCLUSION: the B174/W2-149 sole-kappa screening verdict (kappa = tr([A1,B1]) = tr([A2,B2]) is
the sole leaf1<->leaf2 coupling on the glued genus-2 surface) now rests on a REAL negative
control, not a fabricated one. The positive half (W2-149/C2, kappa-matched => witness exists,
with a genuine free twist) was already a real construction and stands unchanged.""")
else:
    print("SOME CHECKS FAILED -- see FAIL lines above. Either the negative control found a genuine "
          "mismatched-kappa witness (RESOLVED-B, the sole-kappa claim is refuted) or the control could "
          "not be run to a real non-vacuous conclusion (UNRESOLVED).")

print("\n" + ("ALL CHECKS PASS" if ok_all else "SOME CHECKS FAILED"))
import sys
sys.exit(0 if ok_all else 1)
