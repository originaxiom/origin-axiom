"""B666 CELL B' — the per-exponent torsion landscape.

Sealed scope (ADDENDUM_1, CELL B'): |tau_m(tr)| for all six exponents
m in {1,4,5,7,8,11}, tr = 3..15, from the banked B617 closed form
    tau_m = (-1)^m (tr^2-4)^m prod_{j=1}^m U_{j-1}(tr/2)^2 ;
the ratio table |tau_m|/|tau_1| per word; family-constant vs
word-dependent; the m=1-mode participation in the banked Y support
(lookup vs B637's tables + B662/cellH's class table). All labels
firewalled.

GATES (all exact, sympy/Integer):
  GATE A (bundle, t=3 column + neighbors): closed form == direct
    det'(I - Sym^{2m}A) product for tr = 3, 4, 5, all six m, via the
    radical route (lambda = (t+sqrt(t^2-4))/2), AND the banked B423
    (fig-8, tr 3) / B616 (m136, tr 4) spot values reproduced.
  GATE B (B581's exact t=3 torsions): the six banked EXTERIOR torsions
    of the tr-3 object (fig-8) reproduced from the committed
    six_torsions_results.json — monic-normalize the Wada quotient
    (B581 Review-17 units note), check integrality, Delta_m(1) = 0,
    Delta'_m(1) == the banked integers.  This anchors the identity of
    the landscape's t=3 column object.  (The bundle closed form and the
    exterior torsion are DIFFERENT invariants of the same object; the
    sealed landscape is the bundle one — B617's family theorem.)
  GATE C (integer cross-route): the direct integer route
    tau_m = prod_{j=1}^m (2 - L_{2j}(t))  (L = trace/Lucas sequence)
    equals the closed-form route (t^2-4)^m (prod F~_j)^2 with sign
    (-1)^m, for EVERY (m, tr) in the landscape (independent recursions).

Exact arithmetic throughout (sympy Integer / Rational; no floats in any
decisive step).
"""
import json
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
B581_JSON = os.path.join(REPO, "frontier", "B581_six_torsions",
                         "six_torsions_results.json")
B637_DIR = os.path.join(REPO, "frontier", "B637_corrected_cell3")

EXPS = (1, 4, 5, 7, 8, 11)
TRS = tuple(range(3, 16))

out_lines = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    out_lines.append(s)


# ----------------------------------------------------------------------
say("=" * 72)
say("GATE A — B617 closed form vs direct (radical route), tr = 3, 4, 5")
say("=" * 72)


def tau_direct_radical(m, lam, lam_inv):
    """prod_{k != m} (1 - lam^{2(m-k)}) with lam^{-1} given EXPLICITLY
    (lam * lam_inv = 1 for lam = (t+s)/2, lam_inv = (t-s)/2, s^2 = t^2-4)
    so no radical denominators ever appear; incremental expand keeps the
    quadratic-integer form a + b s throughout (exact)."""
    p = sp.Integer(1)
    for k in range(0, 2 * m + 1):
        if k == m:
            continue
        j = m - k
        f = (1 - lam ** (2 * j)) if j > 0 else (1 - lam_inv ** (-2 * j))
        p = sp.expand(p * sp.expand(f))
    return p


def tau_closed_radical(m, lam, lam_inv):
    p = sp.Integer(1)
    for j in range(1, m + 1):
        p = sp.expand(p * sp.expand((lam ** j - lam_inv ** j) ** 2))
    return sp.expand((-1) ** m * p)


BANKED_BUNDLE = {  # B617's committed spot checks (B423 / B616)
    3: {1: -5, 4: 158760000},
    4: {1: -12, 4: 234101145600},
}
for t_int in (3, 4, 5):
    s_rad = sp.sqrt(sp.Integer(t_int) ** 2 - 4)
    lam = (sp.Integer(t_int) + s_rad) / 2
    lam_inv = (sp.Integer(t_int) - s_rad) / 2
    assert sp.expand(lam * lam_inv - 1) == 0
    for m in EXPS:
        d = tau_direct_radical(m, lam, lam_inv)
        c = tau_closed_radical(m, lam, lam_inv)
        assert sp.expand(d - c) == 0, (t_int, m, "closed != direct")
        assert d.is_Rational, (t_int, m, "radical failed to cancel")
        assert (d > 0) == (m % 2 == 0), (t_int, m, "sign law")
        if t_int in BANKED_BUNDLE and m in BANKED_BUNDLE[t_int]:
            assert d == BANKED_BUNDLE[t_int][m], (t_int, m, "banked value")
    say(f"  tr={t_int}: closed==direct (radical), sign law (-1)^m, "
        f"banked spot values: PASS")
say("GATE A: PASS")

# ----------------------------------------------------------------------
say("")
say("=" * 72)
say("GATE B — B581's six exact t=3 (fig-8) EXTERIOR torsions reproduced")
say("        from the committed data (monic normalization per Review 17)")
say("=" * 72)

TAU11 = -(sp.Integer(2) ** 21 * 3 ** 7 * 5 * 7 ** 6 * 11 ** 2 * 13 ** 2
          * 17 * 19 * 73 * 149 * 151 * 1471 * 160453)
BANKED_B581 = {
    1: sp.Integer(-3),
    4: sp.Integer(260736),               # 2^7 3 7 97
    5: sp.Integer(-165110400),           # -2^7 3^4 5^2 7^2 13
    7: sp.Integer(-3257341296168960),
    8: sp.Integer(100636318520821923840),
    11: TAU11,
}
# factorization self-checks of the banked table rows used above
assert sp.Integer(260736) == 2 ** 7 * 3 * 7 * 97
assert sp.Integer(165110400) == 2 ** 7 * 3 ** 4 * 5 ** 2 * 7 ** 2 * 13
assert sp.Integer(3257341296168960) == (2 ** 12 * 3 ** 4 * 5 * 7 ** 5
                                        * 11 * 13 * 19 * 43)
assert sp.Integer(100636318520821923840) == (2 ** 14 * 3 ** 3 * 5 * 7 ** 3
                                             * 11 * 13 * 31 * 607 * 49297)
assert abs(sp.Float(TAU11, 6) / sp.Float(10, 6) ** 36 + sp.Float("6.9081", 6)
           ) < sp.Float("0.001", 6)  # magnitude sanity vs the banked 6.9081e36

with open(B581_JSON) as fh:
    b581 = json.load(fh)

tvar = sp.Symbol("t")
for m in EXPS:
    rec = b581[str(m)]
    assert rec["exact"] is True
    coeffs = []
    for a, b in rec["quotient"]:
        assert sp.Integer(b) == 0, (m, "non-rational coefficient")
        coeffs.append(sp.Rational(a))
    # stored leading-first; the quotient is skew-palindromic so the
    # reading direction only flips the overall unit, which the monic
    # normalization (Review-17 units note) removes.
    if coeffs[0] < 0:
        coeffs = [-c for c in coeffs]
    assert coeffs[0] == 1, (m, "not monic after unit normalization")
    n = len(coeffs) - 1
    poly = sum(c * tvar ** (n - i) for i, c in enumerate(coeffs))
    assert all(sp.Integer(c) == c for c in coeffs), (m, "non-integer")
    # skew-palindromic check c_k = -c_{deg-k}
    assert all(coeffs[i] == -coeffs[n - i] for i in range(n + 1)), m
    at1 = poly.subs(tvar, 1)
    d1 = sp.diff(poly, tvar).subs(tvar, 1)
    assert at1 == 0, (m, "Delta(1) != 0")
    assert d1 == BANKED_B581[m], (m, "tau mismatch", d1)
    say(f"  m={m:>2}: integer, skew-palindromic, Delta(1)=0, "
        f"Delta'(1) = {d1}  == banked  PASS")
say("GATE B: PASS — the six banked B581 exterior torsions reproduced "
    "exactly")

# ----------------------------------------------------------------------
say("")
say("=" * 72)
say("THE LANDSCAPE — |tau_m(tr)| exact, m in {1,4,5,7,8,11}, tr = 3..15")
say("   two independent integer routes per entry (GATE C inline)")
say("=" * 72)


def seqs(t_int, top):
    """L_k (trace/Lucas: L0=2, L1=t) and F~_k (Chebyshev U_{k-1}(t/2):
    F0=0, F1=1), both integer recursions x_{k+1} = t x_k - x_{k-1}."""
    t = sp.Integer(t_int)
    L = [sp.Integer(2), t]
    F = [sp.Integer(0), sp.Integer(1)]
    while len(L) <= top:
        L.append(t * L[-1] - L[-2])
        F.append(t * F[-1] - F[-2])
    return L, F


landscape = {}   # landscape[t][m] = tau_m(t)  (exact Integer)
for t_int in TRS:
    L, F = seqs(t_int, 2 * max(EXPS) + 1)
    base = sp.Integer(t_int) ** 2 - 4
    landscape[t_int] = {}
    for m in EXPS:
        # route 1: closed form
        prodF = sp.Integer(1)
        for j in range(1, m + 1):
            prodF *= F[j]
        tau_closed = sp.Integer(-1) ** m * base ** m * prodF ** 2
        # route 2: direct product prod_{j=1..m} (2 - L_{2j})
        tau_direct = sp.Integer(1)
        for j in range(1, m + 1):
            tau_direct *= (2 - L[2 * j])
        assert tau_closed == tau_direct, (t_int, m, "GATE C")
        assert (tau_closed > 0) == (m % 2 == 0), (t_int, m, "sign law")
        landscape[t_int][m] = tau_closed
say("GATE C: PASS — closed form == direct integer product at all "
    f"{len(TRS) * len(EXPS)} landscape entries; sign law (-1)^m at all")

say("")
say("|tau_m(tr)| (digit counts in brackets for entries > 10^24):")
hdr = "  tr | " + " | ".join(f"m={m}" for m in EXPS)
say(hdr)
for t_int in TRS:
    cells = []
    for m in EXPS:
        v = abs(landscape[t_int][m])
        s = str(v)
        cells.append(s if len(s) <= 24 else f"[{len(s)}d]{s[:10]}...")
    say(f"  {t_int:>2} | " + " | ".join(cells))

# ----------------------------------------------------------------------
say("")
say("=" * 72)
say("THE RATIO TABLE — R_m(tr) = |tau_m(tr)| / |tau_1(tr)| per word")
say("=" * 72)

ratios = {}
for t_int in TRS:
    ratios[t_int] = {}
    tau1 = abs(landscape[t_int][1])
    for m in EXPS:
        R = sp.Rational(abs(landscape[t_int][m]), tau1)
        assert R == sp.Integer(R), (t_int, m, "tau_1 does not divide tau_m")
        ratios[t_int][m] = sp.Integer(R)
say("divisibility: tau_1 | tau_m exactly (integer R_m) at all "
    f"{len(TRS) * len(EXPS)} entries")
say("")
say("R_m(tr) (digit counts for entries > 10^24):")
say(hdr)
for t_int in TRS:
    cells = []
    for m in EXPS:
        s = str(ratios[t_int][m])
        cells.append(s if len(s) <= 24 else f"[{len(s)}d]{s[:10]}...")
    say(f"  {t_int:>2} | " + " | ".join(cells))

# ----------------------------------------------------------------------
say("")
say("=" * 72)
say("THE DECISION — is the ratio vector constant across the family?")
say("=" * 72)

MODES = tuple(m for m in EXPS if m != 1)
v3 = tuple(ratios[3][m] for m in MODES)
constant = all(tuple(ratios[t][m] for m in MODES) == v3 for t in TRS)
say(f"  exact vector equality across tr = 3..15: {constant}")
if not constant:
    say(f"  witness: R_4(3) = {ratios[3][4]}  vs  R_4(4) = {ratios[4][4]}")

# secondary (stronger falsifier): projective constancy — is v(tr)
# parallel to v(3), i.e. equal up to one overall word scalar?
proj = True
witness = None
for t_int in TRS:
    for i in range(len(MODES)):
        for j in range(i + 1, len(MODES)):
            lhs = ratios[t_int][MODES[i]] * ratios[3][MODES[j]]
            rhs = ratios[t_int][MODES[j]] * ratios[3][MODES[i]]
            if lhs != rhs:
                proj = False
                if witness is None:
                    witness = (t_int, MODES[i], MODES[j])
if proj:
    say("  projective constancy (up to one word scalar): TRUE")
else:
    t_w, mi, mj = witness
    say(f"  projective constancy: FALSE — witness tr={t_w}: "
        f"R_{mi}/R_{mj} differs from tr=3:")
    say(f"    R_{mi}({t_w})/R_{mj}({t_w}) = "
        f"{sp.Rational(ratios[t_w][mi], ratios[t_w][mj])}")
    say(f"    R_{mi}(3)/R_{mj}(3)   = "
        f"{sp.Rational(ratios[3][mi], ratios[3][mj])}")

say("")
say("  what IS family-constant (B617's theorem, re-verified on the")
say("  whole landscape): sign(tau_m) = (-1)^m at all 78 entries, and")
say("  the exponent structure tau_m = (-1)^m (tr^2-4)^m * (integer)^2 —")
say("  |tau_m| / |tau_1|^m = (prod_{j=1}^m U_{j-1}(tr/2))^2, a perfect")
sq_ok = all(sp.sqrt(abs(landscape[t][m]) / abs(landscape[t][1]) ** m
                    ).is_Integer for t in TRS for m in EXPS)
say(f"  square at all entries: {sq_ok}")
assert sq_ok

VERDICT = ("FAMILY-CONSTANT" if constant else "WORD-DEPENDENT")
say("")
say(f"VERDICT: {VERDICT} — the ratio vector is not constant (not even "
    f"projectively): the per-exponent landscape carries genuine word "
    f"(object) information beyond the family parity."
    if not constant else f"VERDICT: {VERDICT}")

# ----------------------------------------------------------------------
say("")
say("=" * 72)
say("THE m=1-MODE PARTICIPATION IN THE BANKED Y SUPPORT (lookup,")
say("  parsed from B637's banked tables; values re-read exactly)")
say("=" * 72)

r = sp.sqrt(-3)


def parse_val(s):
    s = s.strip()
    if s == "0":
        return sp.Integer(0)
    mm = re.fullmatch(r"\((-?[0-9/]+)\+(-?[0-9/]+)r\)", s)
    assert mm, s
    return sp.Rational(mm.group(1)) + sp.Rational(mm.group(2)) * r


def parse_tables(path, headers):
    """headers: dict name -> the header line prefix that starts its table."""
    with open(path) as fh:
        lines = [ln.rstrip("\n") for ln in fh]
    tables = {}
    for name, head in headers.items():
        idx = next(i for i, ln in enumerate(lines) if head in ln)
        tab = {}
        j = idx
        while len(tab) < 10:
            j += 1
            mm = re.match(r"\s*Y\[\((\d), (\d), (\d)\)\] = (.*)$", lines[j])
            if mm:
                key = (int(mm.group(1)), int(mm.group(2)), int(mm.group(3)))
                tab[key] = parse_val(mm.group(4))
        tables[name] = tab
    return tables


unbent = parse_tables(
    os.path.join(B637_DIR, "unbent_table.txt"),
    {"unbent": "the unbent weld table"})["unbent"]
bends = parse_tables(
    os.path.join(B637_DIR, "part2b_stage2_fixed_output.txt"),
    {f"m={m}": f"D_bent(M; m={m}):" for m in (1, 5, 7, 11)})
dphi = parse_tables(
    os.path.join(B637_DIR, "stage3_output.txt"),
    {"phi(a)=a": "phi(a)=a: gates", "phi(a)=A": "phi(a)=A: gates",
     "phi(a)=b": "phi(a)=b: gates", "phi(a)=B": "phi(a)=B: gates"})

TRIPLES = sorted(unbent.keys())
support = {"unbent": {k for k, v in unbent.items() if v != 0}}
for name, tab in list(bends.items()) + list(dphi.items()):
    support[name] = {k for k, v in tab.items() if v != 0}

say("  support sizes: " + ", ".join(
    f"{name}: {len(sup)}/10" for name, sup in support.items()))
assert len(support["unbent"]) == 6
assert support["m=5"] == support["m=7"] == support["m=11"] == \
    support["unbent"]
assert support["m=1"] == support["unbent"] | {(0, 2, 4)}
assert support["phi(a)=a"] == support["phi(a)=A"] == \
    support["unbent"] | {(0, 2, 4)}
assert support["phi(a)=b"] == support["phi(a)=B"] == support["unbent"]
say("")
say("  1. SUPPORT: the m=1 bend is the ONLY bend in {1,5,7,11} that")
say("     changes the Y support: 6/10 -> 7/10; the switched-on")
say(f"     component is Y[(0,2,4)] = {bends['m=1'][(0, 2, 4)]}")
say("     (banked). The same channel Y[024] is on for the involution")
say("     doubles phi(a)=a and phi(a)=A (7/10) and off for phi(a)=b,")
say("     phi(a)=B (6/10) — the Y[024]-channel activations of the")
say("     banked zero law are exactly {m=1, phi(a)=a, phi(a)=A}.")

changed = sorted(k for k in TRIPLES if bends["m=1"][k] != unbent[k])
unchanged = sorted(k for k in TRIPLES
                   if bends["m=1"][k] == unbent[k] and unbent[k] != 0)
zeros = sorted(k for k in TRIPLES if unbent[k] == 0
               and bends["m=1"][k] == 0)
say("")
say("  2. VALUES: components the m=1 mode touches (value differs from")
say("     the unbent golden table): " + ", ".join(str(k) for k in changed))
say("     untouched nonzero (the bend-independent core): "
    + ", ".join(str(k) for k in unchanged))
say("     zero on both (the boundary-born zero law Y[01k] = 0): "
    + ", ".join(str(k) for k in zeros))
assert changed == [(0, 2, 4), (0, 3, 4), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
assert unchanged == [(0, 2, 3), (1, 2, 3)]
assert zeros == [(0, 1, 2), (0, 1, 3), (0, 1, 4)]

# the core law re-verified on the parsed tables (sanity, banked B637):
zeta6 = (1 + r) / 2
for name, tab in [("unbent", unbent)] + list(bends.items()) \
        + list(dphi.items()):
    assert sp.simplify(tab[(0, 2, 3)] - 24 * zeta6 * tab[(1, 2, 3)]) == 0
say("")
say("  3. sanity: Y[023] = 24 zeta_6 Y[123] re-verified exactly on all")
say("     9 parsed tables (the banked law of the chord's core).")

say("")
say("  4. CLASS-TABLE cross-reference (B662/cellH, banked): classes")
say("     {0,1} = the boundary-born (coker-delta^0) pair; {2,3,4} = the")
say("     solo/generation triple; only class 4 sees the invariant line")
say("     (kappa = (1,1,1,1) on generators iff i=4). So the m=1-mode")
say("     signature component Y[024] couples boundary-born class 0 to")
say("     solo classes {2,4} — every m=1-touched component contains")
say("     slot 4 or is the dial slot Y[234]; the m=1-invariant core")
say("     pair {023, 123} avoids class 4 entirely.")
touched_with_4 = [k for k in changed if 4 in k]
say(f"     (check: {len(touched_with_4)}/{len(changed)} m=1-touched "
    f"components contain class 4: "
    + ", ".join(str(k) for k in touched_with_4) + ")")
assert all(4 in k for k in changed)
assert all(4 not in k for k in unchanged)

# ----------------------------------------------------------------------
say("")
say("=" * 72)
say("SUMMARY")
say("=" * 72)
say(f"  GATE A (B617 closed form vs direct + banked spot values): PASS")
say(f"  GATE B (B581's six exact t=3 exterior torsions): PASS")
say(f"  GATE C (two integer routes agree at all 78 entries): PASS")
say(f"  VERDICT: {VERDICT} (ratio vector varies with tr; not even")
say(f"    projectively constant). Family-constant content = the parity")
say(f"    sign (-1)^m and the square structure |tau_m| = ")
say(f"    (tr^2-4)^m * (prod U)^2 — exactly B617's theorem, nothing more.")
say(f"  m=1-mode in the Y support: Y[024] switch-on (unique among the")
say(f"    bends), value shifts exactly on the slot-4 components,")
say(f"    the core pair {{023, 123}} m=1-invariant.")

# ---------------------------------------------------------------------- data
data = {
    "cell": "B666 CELL B-prime — the per-exponent torsion landscape",
    "closed_form": "tau_m = (-1)^m (tr^2-4)^m prod_{j=1}^m U_{j-1}(tr/2)^2"
                   " (B617, banked)",
    "exponents": list(EXPS),
    "traces": list(TRS),
    "gates": {"A_bundle_banked": "PASS", "B_B581_exterior_t3": "PASS",
              "C_two_integer_routes_78_entries": "PASS"},
    "tau": {str(t): {str(m): str(landscape[t][m]) for m in EXPS}
            for t in TRS},
    "abs_ratio_over_tau1": {str(t): {str(m): str(ratios[t][m])
                                     for m in EXPS} for t in TRS},
    "verdict": VERDICT,
    "projective_constancy": proj,
    "family_constant_content": ["sign(tau_m) = (-1)^m (all 78 entries)",
                                "|tau_m|/|tau_1|^m is a perfect square "
                                "(all 78 entries)"],
    "m1_mode_Y_lookup": {
        "support_switch_on": "(0,2,4)",
        "Y024_at_m1": str(bends["m=1"][(0, 2, 4)]),
        "value_touched": [str(k) for k in changed],
        "invariant_core": [str(k) for k in unchanged],
        "always_zero": [str(k) for k in zeros],
        "Y024_channel_activations": ["m=1", "phi(a)=a", "phi(a)=A"],
        "class_note": "every m=1-touched component contains class 4; "
                      "the invariant core pair avoids class 4",
    },
}
with open(os.path.join(HERE, "landscape_table.json"), "w") as fh:
    json.dump(data, fh, indent=1)
say("")
say("data written: landscape_table.json")
say("B666 CELL B' DONE")
