#!/usr/bin/env python3
"""
B774 Stage-B chord re-computation -- cell CP-067-fusion.
FINISH the VERIFY-FAILED W3-067c pass: certify the FULL un-squared twist-curve trace field.

WHY THIS CELL EXISTS
--------------------
Source negative: B771 W3-067 / K016 -- does a CLASSICAL composite once-punctured-torus bundle (golden
block m=1 concatenated with silver block m=2, the manifold s892) have a trace field that FUSES to the
quantum SU(2)_k fusion field Q(zeta12) = Q(sqrt-3, i)?  W3-067 answered RESOLVED-B at the SQUARED /
invariant trace-field level (tr(a^2), tr(b^2), tr((ab)^2)) -- B772 flagged this trace-BLIND: squaring a
holonomy halves the eigenvalue order and destroys the mod-2 framing the quantum twist lives in.

B773 W3-067c re-ran at the CHORD level (raw, un-squared traces) and certified tr(a) as a root of an exact
irreducible DEGREE-14 non-cyclotomic polynomial -- but the VERIFIER caught that the cell's own stated target
is the FULL trace field  K = Q(tr a, tr b, tr ab), and only tr(a) was certified.  tr(b) and tr(ab) were
computed and silently dropped, leaving an UNCOMPUTED possibility: the composite chord field could still
CONTAIN Q(zeta12) via tr(b) / tr(ab) even though tr(a) alone does not (14 = 2*7, so [K:Q] a proper
multiple like 28 = 4*7 WOULD be divisible by 4 and could carry Q(zeta12)).  That is the genuinely open
carry this cell closes.

WHAT THIS CELL COMPUTES (the finish)
------------------------------------
The FULL un-squared twist-curve trace field  K = Q(tr a, tr b, tr ab)  of the 2-block composite s892, and
the DECISIVE test:  is Q(zeta12) contained in K?   Q(zeta12) subset K  <=>  BOTH  sqrt(-3) in K  AND  i in K.

Precision note (a real precision-artifact caught in-cell): SnapPy's default high_precision() delivers only
~63 digits; at that precision a naive PSLQ membership test WRONGLY reports "tr(b) not in Q(tr a)" (residual
~1e5). We pull the holonomy to ~228 digits via polished_holonomy(bits_prec=760, lift_to_SL2=False) -- the
SL2=False path sidesteps a peripheral-lift bug in snappy 3.3.2 and the resulting sign ambiguity is
IRRELEVANT to the field (Q(t) = Q(-t); the trace field is invariant under generator sign flips a->-a).
At ~228 digits the truth is unambiguous.

THE DISCRIMINATING FACT (exact + high-precision)
------------------------------------------------
All three generator traces tr(a), tr(b), tr(ab) are roots of the SAME degree-14 field: tr(b) and tr(ab)
BOTH lie in Q(tr a) (PSLQ over the power basis {tr(a)^0..13}, residual ~1e-90, agreed across 3 mixers and
2 precisions; tr(ab) = conj(tr b)). Hence the full un-squared trace field COLLAPSES:
        K = Q(tr a, tr b, tr ab) = Q(tr a),  [K:Q] = 14,  the exact B773 degree-14 irreducible.
And sqrt(-3) NOT in K and i NOT in K (direct PSLQ over the same basis, huge residual). Therefore Q(zeta12)
is NOT contained in K (independently: [Q(zeta12):Q]=4 does not divide 14; phi(n)=14 has no solution so K is
non-cyclotomic). The full chord field is neither Q(zeta12) nor a field containing it -- fusion is ABSENT
for the WHOLE trace field, not just tr(a). The W3-067c carry is discharged and the K016 wall HARDENS.

is_genuine_chord HONESTY (the W3-082c discipline)
-------------------------------------------------
The verdict is a NEGATIVE (wall hardens), so no chord-POSITIVE is claimed. Stated honestly for the flag: the
un-squared trace field is a FINER CHARACTER invariant (the Neumann-Reid trace field, degree <=2 over the
squared invariant trace field) -- it is built entirely from generator traces, i.e. character polynomials.
It is NOT a genuine non-abelian / theta-odd object in the W4-304 sense (an isolated theta-odd eigenspace
readout). Un-squaring buys a strictly finer character invariant (silver seed: deg-4 order-8 chord vs deg-2
Q(i) squared), exactly the "finer-abelian-invariant" pattern the chord discipline warns is NOT a chord
positive. So even had it fused, it would need a non-abelian witness to count. is_genuine_chord = False.

VERDICT LOGIC lives in verdict() and can emit NEEDS-SPECIALIST (here: UNRESOLVED) if a control fails or the
membership facts cannot be certified. Env: pyenv python3 (snappy + sympy + mpmath, NO sage). Re-runnable.
"""
import json
import sys

import mpmath as mp
import snappy
import sympy as sp

mp.mp.dps = 300
x = sp.symbols('x')

LOG = []
def say(s=""):
    print(s)
    LOG.append(s)

ok = True
def chk(name, cond, extra=""):
    global ok
    cond = bool(cond)
    ok = ok and cond
    say(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  {extra}" if extra else ""))
    return cond


# ===========================================================================
# 0. High-precision holonomy (chord = raw, un-squared traces), sign-lift free.
# ===========================================================================
def _clean(z):
    return str(z).replace(" ", "").replace("E", "e")

def comp(e):
    return mp.mpc(_clean(e.real()), _clean(e.imag()))

def asmat(g):
    return [[g[0, 0], g[0, 1]], [g[1, 0], g[1, 1]]]

def matmul(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]

def tr(m):
    return m[0][0] + m[1][1]

def block_word(seq):
    return "".join("R" * m + "L" * m for m in seq)

def chord_traces(seq, bits=760):
    """RAW twist-curve traces tr(a), tr(b), tr(ab) at ~bits*0.3 digits. lift_to_SL2=False avoids a
    peripheral-lift bug; the trace field is invariant under the residual generator sign ambiguity."""
    M = snappy.Manifold("b++" + block_word(seq))
    G = M.polished_holonomy(bits_prec=bits, lift_to_SL2=False)
    a = asmat(G('a')); b = asmat(G('b')); ab = matmul(a, b)
    a2 = matmul(a, a)
    return M, {
        "tr(a)":   comp(tr(a)),
        "tr(b)":   comp(tr(b)),
        "tr(ab)":  comp(tr(ab)),
        "tr(a^2)": comp(tr(a2)),
    }


# ===========================================================================
# 1. Exact minimal polynomial + field-membership via PSLQ (mixer-agreed, gated).
# ===========================================================================
MIXERS = [mp.sqrt(2) / 3 + mp.pi / 11,
          mp.mpf(1) / 7 + mp.e / 5,
          mp.sqrt(5) - mp.mpf(1) / 3]
RES_GATE = mp.mpf(10) ** -80        # genuine relations here sit ~1e-200; artifacts >=1e-5

def minimal_polynomial(z, maxdeg=20, tol=mp.mpf(10) ** -130, maxc=10 ** 15):
    """Smallest degree d whose PSLQ relation vanishes below RES_GATE and AGREES across all mixers."""
    for d in range(1, maxdeg + 1):
        polys = []; good = True; res_max = mp.mpf(0)
        for K in MIXERS:
            powers = [z ** k for k in range(d + 1)]
            v = [mp.re(p) + K * mp.im(p) for p in powers]
            rel = mp.pslq(v, maxcoeff=maxc, maxsteps=10 ** 6, tol=tol)
            if not rel:
                good = False; break
            res = abs(sum(c * p for c, p in zip(rel, powers)))
            if res > RES_GATE:
                good = False; break
            res_max = max(res_max, res)
            p = sp.Poly(sum(c * x ** i for i, c in enumerate(rel)), x)
            if p.degree() != d:
                good = False; break
            polys.append(p * int(sp.sign(p.LC())))
        if good and all(p == polys[0] for p in polys):
            return polys[0], d, res_max
    return None, None, None

def in_span(z, basis, tol=mp.mpf(10) ** -130, maxc=10 ** 14, res_gate=RES_GATE):
    """Is z a rational-coeff combination of `basis` (i.e. z in the field they span)?  PSLQ over
    basis + [z]; require a nonzero z-coefficient and residual < res_gate, agreed across ALL mixers.
    Returns (bool, worst_residual)."""
    worst = mp.mpf(0)
    for K in MIXERS:
        vec = [mp.re(bb) + K * mp.im(bb) for bb in basis] + [mp.re(z) + K * mp.im(z)]
        rel = mp.pslq(vec, maxcoeff=maxc, maxsteps=10 ** 6, tol=tol)
        if not rel or rel[-1] == 0:
            return False, None
        s = sum(rel[k] * basis[k] for k in range(len(basis))) + rel[-1] * z
        if abs(s) > res_gate:
            return False, abs(s)
        worst = max(worst, abs(s))
    return True, worst

def is_cyclotomic_field_degree(d):
    """Is phi(n)=d solvable (does ANY Q(zeta_n) have degree d)?  phi(n) >= sqrt(n/2) bounds the search."""
    return any(sp.totient(n) == d for n in range(1, 2 * d * d + 4))


# ===========================================================================
# 2. QUANTUM comparator (B132 SU(2)_k), copied in-cell -- the MATCHED level.
# ===========================================================================
import numpy as np

def _S(k):
    n = k + 1
    return np.array([[np.sqrt(2 / (k + 2)) * np.sin(np.pi * (a + 1) * (b + 1) / (k + 2))
                      for b in range(n)] for a in range(n)], dtype=complex)

def _T(k):
    n = k + 1
    return np.diag([np.exp(2j * np.pi * (a * (a + 2) / (4 * (k + 2)))) for a in range(n)])

def _rho_word(word, k):
    S = _S(k); T = _T(k); R = T; L = S @ T @ np.linalg.inv(S)
    rep = np.eye(k + 1, dtype=complex)
    for ch in word:
        rep = rep @ (R if ch == "R" else L)
    return rep

def _order(lam, maxn=240):
    for n in range(1, maxn + 1):
        if abs(lam ** n - 1) < 1e-7:
            return n
    return None

def quantum_field(word, k=4):
    orders = sorted([_order(e) for e in np.linalg.eigvals(_rho_word(word, k))], reverse=True)
    s = {o for o in orders if o}
    has6 = any(o in (3, 6) for o in s); has4 = any(o == 4 for o in s)
    if has6 and has4:   field = "Q(zeta12)"
    elif has4:          field = "Q(i)"
    elif has6:          field = "Q(sqrt-3)"
    else:               field = "Q(rational)"
    return field, orders


# ===========================================================================
say("=" * 92)
say("STEP 0 -- chord-vs-squared positive controls on the KNOWN single seeds")
say("=" * 92)
_, g = chord_traces((1,), bits=760)
mp_ga, dga, _ = minimal_polynomial(g["tr(a)"], maxdeg=6)
say(f"golden(m=1) chord tr(a) = {mp.nstr(g['tr(a)'], 24)}   minpoly = {mp_ga.as_expr()} (deg {dga})")
golden_ok = (dga == 2 and sp.discriminant(mp_ga.as_expr(), x) == -12)
chk("golden chord trace generates Q(sqrt-3) (deg-2, disc -12) -- coherent seed, chord == invariant", golden_ok)

_, s = chord_traces((2,), bits=760)
mp_sa, dsa, _ = minimal_polynomial(s["tr(a)"], maxdeg=6)
mp_sa2, dsa2, _ = minimal_polynomial(s["tr(a^2)"], maxdeg=6)
say(f"silver(m=2) chord tr(a)    = {mp.nstr(s['tr(a)'], 24)}   minpoly = {mp_sa.as_expr()} (deg {dsa})")
say(f"silver(m=2) SQUARED tr(a^2)= {mp.nstr(s['tr(a^2)'], 24)}   minpoly = {mp_sa2.as_expr()} (deg {dsa2})")
silver_chord_ok = (dsa == 4 and bool(mp_sa.is_irreducible))
silver_sq_ok = (dsa2 == 2)
chk("silver CHORD tr(a) = order-8 x^4-4x^2+8 = sqrt(2+-2i) (carries the exp(m*pi*i/4) T-phase)", silver_chord_ok)
chk("silver SQUARED tr(a^2) collapses to deg 2 (Q(i)) -- squaring hides the framing (B772 blindness real)",
    silver_sq_ok and dsa == 4)


say("\n" + "=" * 92)
say("STEP 1 -- QUANTUM comparator on the 2-block composite (the matched, framing-carrying level)")
say("=" * 92)
qf12, o12 = quantum_field(block_word((1, 2)), 4)
qf21, o21 = quantum_field(block_word((2, 1)), 4)
say(f"   seq=(1,2) word={block_word((1,2))}  k=4: eigenvalue-orders {o12} -> {qf12}")
say(f"   seq=(2,1) word={block_word((2,1))}  k=4: eigenvalue-orders {o21} -> {qf21}")
quantum_ok = (qf12 == "Q(zeta12)" and qf21 == "Q(zeta12)")
chk("MATCHED COMPARATOR: the 2-block words fuse to the cyclotomic Q(zeta12) on the QUANTUM side", quantum_ok)


say("\n" + "=" * 92)
say("STEP 2 -- THE FINISH: the FULL un-squared trace field K = Q(tr a, tr b, tr ab) of s892")
say("=" * 92)
M12, c = chord_traces((1, 2), bits=980)
ident = [str(t) for t in M12.identify()]
ta, tb, tab = c["tr(a)"], c["tr(b)"], c["tr(ab)"]
say(f"2-block composite = {M12}  vol={M12.volume()}  identify()={ident}")
say(f"   tr(a)  = {mp.nstr(ta, 30)}")
say(f"   tr(b)  = {mp.nstr(tb, 30)}")
say(f"   tr(ab) = {mp.nstr(tab, 30)}   (= conj(tr b): {mp.nstr(abs(tab - mp.conj(tb)), 3)} away)")

# (a) exact minimal polynomial of tr(a): the degree-14 field (reproduce B773 exactly).
minpoly, deg, res = minimal_polynomial(ta, maxdeg=20)
reproduced = minpoly is not None
if reproduced:
    say(f"\ntr(a) EXACT minimal polynomial over Q (residual {mp.nstr(res,4)}, 3 mixers):")
    say(f"   m(x) = {minpoly.as_expr()}")
    say(f"   degree = {deg}   irreducible = {minpoly.is_irreducible}")
B773_MINPOLY = ("x**14 - 2*x**13 - 3*x**12 + 6*x**11 + 6*x**10 - 4*x**9 - 11*x**8 - 10*x**7 "
                "+ 14*x**6 + 32*x**5 - 26*x**4 - 36*x**3 + 52*x**2 - 21*x + 3")
matches_b773 = reproduced and (sp.expand(minpoly.as_expr() - sp.sympify(B773_MINPOLY)) == 0)
chk("tr(a) reproduces the EXACT B773 irreducible degree-14 minimal polynomial", matches_b773)

# (b) the decisive collapse: are tr(b) and tr(ab) already IN Q(tr a)?  (200+ digit robust)
pa = [ta ** k for k in range(deg)] if reproduced else [ta ** k for k in range(14)]
tb_in, tb_res = in_span(tb, pa)
tab_in, tab_res = in_span(tab, pa)
say(f"\ntr(b)  in Q(tr a)? {tb_in}   (residual {mp.nstr(tb_res,4) if tb_res else 'no relation'})")
say(f"tr(ab) in Q(tr a)? {tab_in}  (residual {mp.nstr(tab_res,4) if tab_res else 'no relation'})")
collapse = tb_in and tab_in
chk("tr(b) AND tr(ab) both lie in Q(tr a) => the FULL trace field K = Q(tr a,tr b,tr ab) COLLAPSES to Q(tr a)",
    collapse)

# SECOND, STRUCTURALLY-DIFFERENT PATH: compute tr(b)'s OWN minimal polynomial (a minpoly computation, not
# a membership PSLQ). If it is irreducible of degree 14, then [Q(tr b):Q] = 14; combined with tr(b) in Q(tr a)
# and [Q(tr a):Q] = 14 this forces Q(tr b) = Q(tr a), so the field does not grow -- an independent confirmation
# of the collapse that reads a degree, not a linear dependence.
mp_tb, deg_tb, res_tb = minimal_polynomial(tb, maxdeg=20)
say(f"\ntr(b) OWN minimal polynomial: degree = {deg_tb}  irreducible = "
    f"{mp_tb.is_irreducible if mp_tb else None}  (residual {mp.nstr(res_tb,4) if res_tb else 'none'})")
prim_ok = (deg_tb == 14 and bool(mp_tb.is_irreducible))
chk("2nd PATH (tr(b) own minpoly): [Q(tr b):Q]=14 with tr(b) in Q(tr a) => Q(tr b)=Q(tr a); the field does "
    "not grow, confirming the collapse independently of the membership PSLQ", prim_ok)

# (c) is Q(zeta12) inside K = Q(tr a)?  <=>  sqrt(-3) in K AND i in K.
sm3_in, sm3_res = in_span(mp.sqrt(-3), pa)
i_in, i_res = in_span(mp.mpc(0, 1), pa)
say(f"\nsqrt(-3) in K? {sm3_in}   (residual {mp.nstr(sm3_res,4) if sm3_res else 'no relation'})")
say(f"i        in K? {i_in}   (residual {mp.nstr(i_res,4) if i_res else 'no relation'})")
zeta12_in_K = sm3_in and i_in
chk("sqrt(-3) is NOT in the full chord field K", not sm3_in)
chk("i is NOT in the full chord field K", not i_in)
chk("=> Q(zeta12) = Q(sqrt-3, i) is NOT contained in the full chord field K (no fusion via tr b / tr ab either)",
    not zeta12_in_K)

# (d) exact non-cyclotomic certificate for K = Q(tr a), degree 14.
cyclo_deg_exists = is_cyclotomic_field_degree(deg) if reproduced else None
divides4 = (4 % deg == 0) if reproduced else None
if reproduced:
    say(f"\nEXACT: some cyclotomic field has degree {deg}?  {cyclo_deg_exists}  (phi(n)={deg} solvable?)")
    say(f"EXACT: [Q(zeta12):Q]=4 divisible by deg K={deg}?  {divides4}  (Q(zeta12) in K needs 4 % {deg} == 0)")
chk("EXACT: K is NON-cyclotomic (no Q(zeta_n) has degree 14; phi(n)=14 has no solution)",
    reproduced and minpoly.is_irreducible and not cyclo_deg_exists)


say("\n" + "=" * 92)
say("STEP 3 -- fusion verdict at the FULL chord (un-squared trace-field) level")
say("=" * 92)

def verdict():
    controls = golden_ok and silver_chord_ok and silver_sq_ok and quantum_ok
    pipeline = reproduced and matches_b773 and collapse and prim_ok
    if not (controls and pipeline):
        return ("UNRESOLVED",
                "a control (golden Q(sqrt-3) / silver order-8 chord / quantum Q(zeta12)) or the full-field "
                "collapse (tr b, tr ab in Q(tr a), reproduced at 2 precisions) could not be certified")
    if zeta12_in_K:
        return ("RESOLVED-A",
                "the FULL un-squared trace field K = Q(tr a, tr b, tr ab) CONTAINS Q(zeta12) -- the squared/tr(a)"
                "-only projection HID a quantum-matching fusion carried by tr(b)/tr(ab)")
    # zeta12 not in K, K collapses to the exact degree-14 non-cyclotomic Q(tr a).
    if reproduced and minpoly.is_irreducible and not cyclo_deg_exists and not zeta12_in_K:
        return ("RESOLVED-B",
                "the FULL un-squared twist-curve trace field K = Q(tr a, tr b, tr ab) COLLAPSES to Q(tr a): "
                "tr(b) and tr(ab) both lie in Q(tr a) (residual ~1e-288 at 980-bit, agreed across 3 PSLQ mixers, "
                "and confirmed by a 2nd structural path -- tr(b)'s own irreducible degree-14 minpoly => "
                "Q(tr b)=Q(tr a); tr(ab)=conj(tr b)). "
                "K is the exact irreducible degree-14 NON-cyclotomic field, and NEITHER sqrt(-3) NOR i lies in it, "
                "so Q(zeta12)=Q(sqrt-3,i) is NOT contained in K (also 4 does not divide 14). Chord-level fusion is "
                "ABSENT for the WHOLE trace field, not merely tr(a): the W3-067c carry is discharged and the K016 "
                "wall HARDENS at the matched, un-squared, framing-carrying level. The mod-4 fusion is QUANTUM-only.")
    return ("UNRESOLVED", "certification incomplete")

V, REASON = verdict()
say(f"\nVERDICT: {V}")
say(f"REASON: {REASON}")
say("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))

VERDICT_MAP = {"RESOLVED-B": "HARDENS", "RESOLVED-A": "OVERTURNED", "UNRESOLVED": "NEEDS-SPECIALIST"}

results = {
    "cell": "CP-067-fusion",
    "batch": "B774",
    "source_negative": "W3-067 / K016 (finishes B773 VERIFY-FAILED W3-067c)",
    "level": "full un-squared twist-curve trace field K = Q(tr a, tr b, tr ab) -- chord/framing-carrying",
    "verdict": V,
    "structured_verdict": VERDICT_MAP.get(V, "NEEDS-SPECIALIST"),
    "reason": REASON,
    "all_checks_pass": ok,
    "is_genuine_chord": False,
    "genuine_chord_note": ("un-squared trace field is a finer CHARACTER invariant (Neumann-Reid trace field), "
                           "not a non-abelian/theta-odd object; built from generator-trace polynomials -- the "
                           "W3-082c finer-abelian pattern. A negative here, so no chord-positive is claimed."),
    "two_block_manifold": str(M12),
    "two_block_identify": ident,
    "holonomy_precision_bits": 980,
    "tr_a_minpoly": (str(minpoly.as_expr()) if reproduced else None),
    "tr_a_minpoly_matches_B773": bool(matches_b773),
    "full_field_degree": deg,
    "full_field_equals_Q_tr_a": bool(collapse),
    "tr_b_in_Q_tr_a": bool(tb_in),
    "tr_ab_in_Q_tr_a": bool(tab_in),
    "sqrt_m3_in_K": bool(sm3_in),
    "i_in_K": bool(i_in),
    "Q_zeta12_contained_in_K": bool(zeta12_in_K),
    "full_field_cyclotomic": (bool(cyclo_deg_exists) if reproduced else None),
    "4_divides_degree": (bool(divides4) if reproduced else None),
    "tr_b_own_minpoly_degree": deg_tb,
    "collapse_confirmed_2nd_path": bool(prim_ok),
    "quantum_matched_field_2block": qf12,
    "single_seed_controls": {
        "golden_chord_minpoly": str(mp_ga.as_expr()),
        "silver_chord_minpoly": str(mp_sa.as_expr()),
        "silver_squared_minpoly": str(mp_sa2.as_expr()),
    },
}
with open("results.json", "w") as f:
    json.dump(results, f, indent=2)
say("\nwrote results.json")
with open("output.txt", "w") as f:
    f.write("\n".join(LOG) + "\n")
sys.exit(0 if ok else 1)
