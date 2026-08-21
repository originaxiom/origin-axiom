#!/usr/bin/env python3
"""P-INSTRUMENT -- the listener-map crossing cell, one-free-parameter form.

Standalone, self-contained: no imports from the repo, no machine paths in the logic. Every
number in PART A (the object-side construction) is computed from the SU(3)-level-2 modular
data (Kac-Peterson) alone -- Gate 5 clean, no SM number appears anywhere in Part A.

PART A -- rebuilds, independently and in mpmath 50-digit precision:
  - the SU(3)_2 modular S,T matrices (Kac-Peterson), gate-checked against the defining
    modular identities;
  - R = T, L = S^-1 T^-1 S, the conjugation weld C (theta), and the DERIVED listener pair
    u3, u6 (B1070/B1071's sealed pair -- taken as given, not re-derived here);
  - the welded coupling h(g,u) = u^dagger (C . g) u for g in the metallic word family;
  - the one-real-parameter listener u(theta) = cos(theta) u3 + sin(theta) u6, theta in
    [0, pi) -- the real great circle through u3, u6 (see NOTES.md/PRECOMMIT.md for why this
    curve and not another).

PART B -- given ONE measured SM number (passed as an explicit argument, never hardcoded in
Part A's logic), solves for theta and predicts the companion curve's value. This is the
only place a measured number may legally appear (Gate 5).

Run standalone: `python3 instrument.py` prints the Part-A structural facts (no SM data
touched). The calibration/prediction driver lives in run_prediction.py, which supplies the
actual PMNS/CKM numbers and writes results.json.
"""
import itertools
import mpmath as mp

mp.mp.dps = 50  # 50 decimal digits throughout


# ======================================================================================
# PART A -- pure object-side construction. NO SM NUMBER MAY EVER APPEAR BELOW THIS LINE
# UNTIL THE EXPLICIT "PART B" SECTION.
# ======================================================================================

def su3_level2_data():
    """Kac-Peterson modular (S,T) for SU(3) at level 2 (6 primaries). Independent
    reimplementation (own cyclotomic-free high-precision route); cross-checked against
    the banked construction (frontier/B238_su32_levelrank/su32_wrt.py) by exact numeric
    agreement on every downstream quantity (see NOTES.md V1)."""
    k, kap = 2, 5
    weights = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    n = len(weights)

    def Lvec(w):
        return (w[0] + w[1] + 2, w[1] + 1, 0)

    def ip(u, v):
        dot = sum(u[i] * v[i] for i in range(3))
        su, sv = sum(u), sum(v)
        return mp.mpf(dot) - mp.mpf(su) * mp.mpf(sv) / 3

    perms = list(itertools.permutations(range(3)))

    def sgn(p):
        s = 1
        for i in range(3):
            for j in range(i + 1, 3):
                if p[i] > p[j]:
                    s = -s
        return s

    S = mp.matrix(n, n)
    for i, wl in enumerate(weights):
        Ll = Lvec(wl)
        for j, wm in enumerate(weights):
            Lm = Lvec(wm)
            acc = mp.mpc(0)
            for p in perms:
                Llp = tuple(Ll[q] for q in p)
                acc += sgn(p) * mp.e ** (-2j * mp.pi * ip(Llp, Lm) / kap)
            S[i, j] = acc

    norm0 = mp.sqrt(mp.fsum(mp.fabs(S[i, 0]) ** 2 for i in range(n)))
    for i in range(n):
        for j in range(n):
            S[i, j] = S[i, j] / norm0

    c_central = mp.mpf(k * 8) / (k + 3)
    Tdiag = []
    for (a, b) in weights:
        hexp = (mp.mpf(2) / 3 * (a * a + a * b + b * b) + 2 * (a + b)) / (2 * kap) - c_central / 24
        Tdiag.append(mp.e ** (2j * mp.pi * hexp))
    T = mp.matrix(n, n)
    for i in range(n):
        T[i, i] = Tdiag[i]

    return weights, S, T, c_central


def dagger(M):
    n, m = M.rows, M.cols
    out = mp.matrix(m, n)
    for i in range(n):
        for j in range(m):
            out[j, i] = mp.conj(M[i, j])
    return out


def mat_close(A, B, tol=mp.mpf('1e-40')):
    worst = mp.mpf(0)
    for i in range(A.rows):
        for j in range(A.cols):
            worst = max(worst, mp.fabs(A[i, j] - B[i, j]))
    return worst < tol, worst


def modular_gates(S, T):
    """The Kac-Peterson correctness gates: S unitary & symmetric, S^2 a permutation
    (charge conjugation), (ST)^3 proportional to S^2. All must PASS or the instrument is
    not the object's modular data at all."""
    n = S.rows
    uni_ok, uni_err = mat_close(S * dagger(S), mp.eye(n))
    sym_ok, sym_err = mat_close(S, S.T)
    S2 = S * S
    perm_ok = all(mp.fabs(S2[i, j]) < mp.mpf('1e-30') or mp.fabs(mp.fabs(S2[i, j]) - 1) < mp.mpf('1e-30')
                  for i in range(n) for j in range(n))
    ST3 = (S * T) ** 3
    idx = next((i, j) for i in range(n) for j in range(n) if mp.fabs(S2[i, j]) > mp.mpf('0.5'))
    ratio = ST3[idx] / S2[idx]
    prop_ok, prop_err = mat_close(ST3, mp.matrix([[ratio * S2[i, j] for j in range(n)] for i in range(n)]))
    return dict(unitary=uni_ok, symmetric=sym_ok, S2_is_permutation=perm_ok, ST3_prop_S2=prop_ok,
                errors=dict(unitary=float(uni_err), symmetric=float(sym_err), prop=float(prop_err)))


def build_instrument():
    """Everything field-side: S,T,R,L,C(theta),u3,u6. No SM number. Returns a dict."""
    weights, S, T, c = su3_level2_data()
    n = S.rows
    R = T
    L = (S ** -1) * (T ** -1) * S

    okR, _ = mat_close(R * dagger(R), mp.eye(n))
    okL, _ = mat_close(L * dagger(L), mp.eye(n))
    assert okR and okL, "R or L not unitary -- construction error"

    idx = {w: i for i, w in enumerate(weights)}
    C = mp.matrix(n, n)  # theta: the conjugation weld, permutation (a,b) <-> (b,a)
    for i, (a, b) in enumerate(weights):
        C[idx[(b, a)], i] = 1

    # u3, u6: THE DERIVED LISTENER PAIR (B1070/B1071, sealed+proved) -- taken as given.
    # The antisymmetric combinations of the two theta-odd conjugate weight pairs.
    pairs = [((1, 0), (0, 1)), ((2, 0), (0, 2))]
    U = []
    for (wa, wb) in pairs:
        a, b = idx[wa], idx[wb]
        u = mp.matrix(n, 1)
        u[a, 0], u[b, 0] = 1 / mp.sqrt(2), -1 / mp.sqrt(2)
        U.append(u)
    u3, u6 = U

    def inner(u, v):
        return (dagger(u) * v)[0, 0]

    assert mp.fabs(inner(u3, u3) - 1) < mp.mpf('1e-40')
    assert mp.fabs(inner(u6, u6) - 1) < mp.mpf('1e-40')
    assert mp.fabs(inner(u3, u6)) < mp.mpf('1e-40'), "u3, u6 not orthogonal -- construction error"

    return dict(weights=weights, S=S, T=T, c=c, R=R, L=L, C=C, u3=u3, u6=u6, n=n)


def weld_word(inst, word):
    """weld(word) = C . rho(word), word a string over {'R','L'}."""
    R, L, C, n = inst['R'], inst['L'], inst['C'], inst['n']
    P = mp.eye(n)
    for ch in word:
        P = P * (R if ch == 'R' else L)
    return C * P


SX = mp.matrix([[0, 1], [1, 0]])
SY = mp.matrix([[0, -1j], [1j, 0]])
SZ = mp.matrix([[1, 0], [0, -1]])
I2 = mp.eye(2)


def M_odd_2x2(inst, word):
    """The 2x2 compression of weld(word) onto the {u3,u6} orthonormal basis -- 'M_odd(g)'
    in the corpus's notation."""
    u3, u6 = inst['u3'], inst['u6']
    W = weld_word(inst, word)
    basis = [u3, u6]
    M = mp.matrix(2, 2)
    for i in range(2):
        for j in range(2):
            M[i, j] = (dagger(basis[i]) * W * basis[j])[0, 0]
    return M


def trace2(M):
    return M[0, 0] + M[1, 1]


def pauli_decompose(M):
    """M = w0*I2 + i*(wx*SX + wy*SY + wz*SZ); returns (w0,wx,wy,wz), all real for M in
    (a phase times) SU(2)."""
    w0 = trace2(M) / 2
    wx = trace2(SX * M) / (2j)
    wy = trace2(SY * M) / (2j)
    wz = trace2(SZ * M) / (2j)
    return w0, wx, wy, wz


def curve_axis(inst, word):
    """Returns (tone, wx, wz) -- the real great-circle-visible part of word's Bloch axis.
    (wy is invisible to the real-coefficient family u(theta); see NOTES.md.)"""
    M = M_odd_2x2(inst, word)
    unit_ok, uerr = mat_close(M * dagger(M), I2)
    det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    w0, wx, wy, wz = pauli_decompose(M)
    return dict(word=word, tone=mp.re(w0), wx=mp.re(wx), wy=mp.re(wy), wz=mp.re(wz),
                unitary=unit_ok, unitary_err=float(uerr), det=complex(det))


def h_theta(axis, theta):
    """h(g, u(theta)) = tone + i*(wx*sin(2 theta) + wz*cos(2 theta)) -- exact closed form,
    valid because Re h is proven u-independent (B1070 A2/B641) and the real great-circle
    Bloch vector is (sin 2theta, 0, cos 2theta)."""
    tone, wx, wz = axis['tone'], axis['wx'], axis['wz']
    im = wx * mp.sin(2 * theta) + wz * mp.cos(2 * theta)
    return mp.mpc(tone, im)


def abs_h_theta(axis, theta):
    return mp.fabs(h_theta(axis, theta))


def h_theta_bruteforce(inst, word, theta):
    """Direct evaluation u(theta)^dagger weld(word) u(theta) -- cross-check of the closed
    form above, no shortcuts."""
    u3, u6 = inst['u3'], inst['u6']
    u = mp.cos(theta) * u3 + mp.sin(theta) * u6
    W = weld_word(inst, word)
    return (dagger(u) * W * u)[0, 0]


def achievable_range(axis, samples=4000):
    """min/max of |h(theta)| over theta in [0,pi) by dense scan + closed-form refinement
    (the function is a single cosine in 2 theta, so the scan is exact up to sampling; the
    true extrema are |tone| and sqrt(tone^2+A^2) in closed form, cross-checked below)."""
    tone, wx, wz = axis['tone'], axis['wx'], axis['wz']
    A = mp.sqrt(wx ** 2 + wz ** 2)
    lo_closed = mp.fabs(tone)
    hi_closed = mp.sqrt(tone ** 2 + A ** 2)
    vals = [float(abs_h_theta(axis, mp.pi * i / samples)) for i in range(samples)]
    return dict(lo=float(lo_closed), hi=float(hi_closed),
                scan_lo=min(vals), scan_hi=max(vals), amplitude=float(A))


def solve_calibration(axis, target, samples=20000):
    """All theta in [0,pi) solving |h(axis,theta)| = target, found by dense scan + bisection
    refinement. Returns sorted list of theta roots (possibly empty if target is out of
    range)."""
    f = lambda t: float(abs_h_theta(axis, mp.mpf(t))) - float(target)
    ts = [mp.pi * i / samples for i in range(samples + 1)]
    fs = [f(t) for t in ts]
    roots = []
    for i in range(samples):
        if fs[i] == 0:
            roots.append(ts[i])
        elif fs[i] * fs[i + 1] < 0:
            lo, hi = ts[i], ts[i + 1]
            flo = fs[i]
            for _ in range(200):
                mid = (lo + hi) / 2
                fm = f(mid)
                if fm == 0:
                    lo = hi = mid
                    break
                if (fm > 0) == (flo > 0):
                    lo, flo = mid, fm
                else:
                    hi = mid
            roots.append((lo + hi) / 2)
    return roots


# ======================================================================================
# PART A self-verification -- no SM data anywhere in this function.
# ======================================================================================
def part_a_selfcheck():
    inst = build_instrument()
    gates = modular_gates(inst['S'], inst['T'])
    print("=== Kac-Peterson modular gates ===")
    for k_, v in gates.items():
        print(" ", k_, v)
    assert all(gates[k_] for k_ in ('unitary', 'symmetric', 'S2_is_permutation', 'ST3_prop_S2'))

    phi = (1 + mp.sqrt(5)) / 2
    target = 1 / (2 * phi) + 1j * mp.sin(2 * mp.pi / 5) / mp.sqrt(5)
    h1 = (dagger(inst['u3']) * weld_word(inst, 'RL') * inst['u3'])[0, 0]
    print("\n=== B593 reproduction ===")
    print("  h(RL,u3)   =", h1)
    print("  B593 value =", target)
    print("  |diff|     =", mp.fabs(h1 - target))
    assert mp.fabs(h1 - target) < mp.mpf('1e-40')
    print("  EXACT to 50 digits.")

    print("\n=== the two independent curves (A = RL, B = R^2L^2) ===")
    axisA = curve_axis(inst, 'RL')
    axisB = curve_axis(inst, 'RRLL')
    for ax in (axisA, axisB):
        print(f"  {ax['word']:>6}: tone={float(ax['tone']):+.9f}  wx={float(ax['wx']):+.9f}  "
              f"wy={float(ax['wy']):+.9f}  wz={float(ax['wz']):+.9f}  unitary={ax['unitary']}  det={ax['det']}")
    rA, rB = achievable_range(axisA), achievable_range(axisB)
    print(f"  Curve A |h| range: [{rA['lo']:.6f}, {rA['hi']:.6f}]  (scan: [{rA['scan_lo']:.6f}, {rA['scan_hi']:.6f}])")
    print(f"  Curve B |h| range: [{rB['lo']:.6f}, {rB['hi']:.6f}]  (scan: [{rB['scan_lo']:.6f}, {rB['scan_hi']:.6f}])")

    print("\n=== closed-form vs brute-force cross-check (5 random theta) ===")
    import random
    random.seed(20260821)
    for _ in range(5):
        th = mp.mpf(random.random()) * mp.pi
        cf = h_theta(axisA, th)
        bf = h_theta_bruteforce(inst, 'RL', th)
        print(f"  theta={float(th):.6f}  closed={complex(cf)}  brute={complex(bf)}  |diff|={float(mp.fabs(cf-bf)):.2e}")
        assert mp.fabs(cf - bf) < mp.mpf('1e-35')
    print("\nPART A: all self-checks PASS. No SM number appeared above this line.")
    return inst, axisA, axisB


# ======================================================================================
# PART B/C -- calibration + prediction + comparison. THIS IS THE ONLY SECTION OF THIS
# FILE IN WHICH A MEASURED SM NUMBER MAY APPEAR (Gate 5 boundary). Run exactly per
# PRECOMMIT.md, plus the mid-run degeneracy discovery documented in NOTES.md Sec.3: all 4
# calibration-branch roots gave identical predictions because h(R^2L^2,theta) =
# -phi*h(RL,theta) EXACTLY on this curve -- a zero-parameter forced relation, not a
# genuine use of theta as a free coordinate. Both the originally pre-committed branch
# framing and the sharpened direct-ratio framing are run and reported; neither target nor
# method changed after seeing any comparison value.
# ======================================================================================

# PMNS: NuFIT 6.1 via arXiv:2604.04585 Table 1, reused VERBATIM from the already-sealed,
# already-vetted frontier/B1075_moduli_crossing/b1075_execution.json (not re-fetched, for
# full reproducibility from a single already-cited source).
PMNS = {
    "NO": {"Ue1": (0.8092, 0.8345), "Ue2": (0.531, 0.5676), "Ue3": (0.1437, 0.1555)},
    "IO": {"Ue1": (0.8091, 0.8343), "Ue2": (0.531, 0.5676), "Ue3": (0.1447, 0.1562)},
}
# CKM: PDG global-fit standard magnitudes (long-stable across editions). Sourcing caveat,
# disclosed: this session's live web-search budget was exhausted before a fresh citation
# could be pulled -- carried from training knowledge, not freshly fetched. BONUS ONLY, not
# part of the primary verdict (see PRECOMMIT.md / NOTES.md).
CKM_E_ROW = {"Vud": 0.97435, "Vus": 0.22500, "Vub": 0.00369}


def box_mid(lo, hi):
    return (lo + hi) / 2


def in_box(val, lo, hi):
    return lo <= val <= hi


def excess_halfwidths(val, lo, hi):
    mid, half = (lo + hi) / 2, (hi - lo) / 2
    d = abs(val - mid)
    return 0.0 if d <= half else (d - half) / half


def run_branch(name, cal_axis, cal_target_lo, cal_target_hi, pred_axis, pred_name, orderings):
    out = {"branch": name}
    cal_mid = box_mid(cal_target_lo, cal_target_hi)
    rng = achievable_range(cal_axis)
    out["calibration_axis"] = cal_axis["word"]
    out["calibration_target_box"] = [cal_target_lo, cal_target_hi]
    out["calibration_target_mid"] = cal_mid
    out["calibration_axis_range"] = [rng["lo"], rng["hi"]]
    out["calibration_in_range"] = rng["lo"] <= cal_mid <= rng["hi"]

    roots = solve_calibration(cal_axis, cal_mid)
    roots_sorted = sorted(float(r) for r in roots)
    out["all_calibration_roots_theta"] = roots_sorted
    out["n_roots"] = len(roots_sorted)
    if not roots_sorted:
        out["outcome"] = "NEEDS-STRUCTURE (calibration target out of achievable range)"
        return out

    primary_theta = roots_sorted[0]  # PRE-COMMITTED RULE: smallest non-negative root
    out["primary_theta"] = primary_theta
    pred_rng = achievable_range(pred_axis)
    out["prediction_axis"] = pred_axis["word"]
    out["prediction_axis_range"] = [pred_rng["lo"], pred_rng["hi"]]
    primary_pred = float(abs_h_theta(pred_axis, mp.mpf(primary_theta)))
    out["primary_prediction_value"] = primary_pred
    all_preds = [float(abs_h_theta(pred_axis, mp.mpf(r))) for r in roots_sorted]
    out["all_branch_predictions"] = all_preds
    out["all_branch_predictions_identical"] = (max(all_preds) - min(all_preds)) < 1e-8
    out["orderings"] = {}
    for ordering in orderings:
        lo, hi = PMNS[ordering][pred_name]
        out["orderings"][ordering] = {
            "target_box": [lo, hi], "target_mid": box_mid(lo, hi),
            "primary_hit": in_box(primary_pred, lo, hi),
            "primary_excess_halfwidths": excess_halfwidths(primary_pred, lo, hi),
        }
    return out


def relation_check(inst):
    """The discovered exact relation: h(RRLL,theta) = -phi*h(RL,theta) on the real great
    circle; explicitly NOT a full-matrix identity."""
    phi = (1 + mp.sqrt(5)) / 2
    axisA, axisB = curve_axis(inst, 'RL'), curve_axis(inst, 'RRLL')
    worst = mp.mpf(0)
    import random
    random.seed(20260821)
    for _ in range(12):
        th = mp.mpf(random.random()) * mp.pi
        hA, hB = h_theta(axisA, th), h_theta(axisB, th)
        worst = max(worst, mp.fabs(hB - (-phi * hA)))
    MA, MB = M_odd_2x2(inst, 'RL'), M_odd_2x2(inst, 'RRLL')
    target = mp.matrix([[-phi * MA[i, j] for j in range(2)] for i in range(2)])
    full_matrix_ok, full_matrix_err = mat_close(MB, target, tol=mp.mpf('1e-20'))
    return dict(
        relation="h(RRLL,theta) = -phi * h(RL,theta), for ALL theta on the real great circle",
        verified_on_curve_worst_residual=float(worst),
        holds_on_curve=bool(worst < mp.mpf('1e-40')),
        holds_as_full_2x2_matrix_identity=full_matrix_ok,
        note="Full-matrix identity is FALSE (off-diagonal antisymmetric/wy part does not "
             "scale by -phi) -- the relation is specific to the real-linear-combination "
             "family, not a generic fact about the two words at every listener.",
    )


def direct_ratio_test(orderings):
    """THE SHARPENED TEST (post-discovery, same pre-committed targets, zero new SM number
    chosen): does the MEASURED ratio |Ue1|/|Ue2| equal phi -- a zero-parameter, forced,
    anchor-free relation, Type-Law clause (i)."""
    phi = float((1 + mp.sqrt(5)) / 2)
    out = {"predicted_ratio": phi, "orderings": {}}
    for ordering in orderings:
        e1lo, e1hi = PMNS[ordering]["Ue1"]
        e2lo, e2hi = PMNS[ordering]["Ue2"]
        ratio_lo, ratio_hi = e1lo / e2hi, e1hi / e2lo
        mid_ratio = (e1lo + e1hi) / 2 / ((e2lo + e2hi) / 2)
        out["orderings"][ordering] = {
            "Ue1_box": [e1lo, e1hi], "Ue2_box": [e2lo, e2hi],
            "measured_ratio_box": [ratio_lo, ratio_hi],
            "measured_ratio_midpoint": mid_ratio,
            "phi_inside_ratio_box": ratio_lo <= phi <= ratio_hi,
            "excess_halfwidths": excess_halfwidths(phi, ratio_lo, ratio_hi),
        }
    return out


def part_bc_prediction(inst, axisA, axisB):
    import json
    results = {
        "instrument": "u(theta) = cos(theta) u3 + sin(theta) u6, theta in [0,pi)",
        "modular_gates_pass": True,
        "b593_reproduction_exact": True,
        "curveA": {"word": "RL", "tone": float(axisA["tone"])},
        "curveB": {"word": "RRLL", "tone": float(axisB["tone"])},
        "range_screening": {
            "Ue3_excluded_both_curves_any_theta": True,
            "note": "Ue3 in [0.1437,0.1562] is below curve A min 0.309 and curve B min 0.500 -- structural, zero look-elsewhere",
        },
    }

    print("\n" + "=" * 78)
    print("PART B/C -- SM comparison begins here (the only SM numbers in this file)")
    print("=" * 78)

    print("\n=== Branch 1 (PRIMARY, as pre-committed): calibrate A=RL on Ue2, predict B=RRLL vs Ue1 ===")
    b1 = run_branch("1_A-calibrates_B-predicts", axisA, *PMNS["NO"]["Ue2"], axisB, "Ue1", ["NO", "IO"])
    print(json.dumps(b1, indent=2))
    results["branch_1_primary"] = b1

    print("\n=== Branch 2 (CROSS-CHECK, as pre-committed): calibrate B=RRLL on Ue1, predict A=RL vs Ue2 ===")
    b2 = run_branch("2_B-calibrates_A-predicts", axisB, *PMNS["NO"]["Ue1"], axisA, "Ue2", ["NO", "IO"])
    print(json.dumps(b2, indent=2))
    results["branch_2_crosscheck"] = b2

    print("\n=== MID-RUN DISCOVERY: why all 4 branch predictions were identical (see NOTES.md Sec.3) ===")
    rel = relation_check(inst)
    print(json.dumps(rel, indent=2))
    results["degeneracy_diagnosis"] = rel

    print("\n=== THE SHARPENED TEST: direct ratio |Ue1|/|Ue2| =? phi (zero-parameter, forced) ===")
    ratio_test = direct_ratio_test(["NO", "IO"])
    print(json.dumps(ratio_test, indent=2))
    results["direct_ratio_test"] = ratio_test

    print("\n=== CKM bonus (exploratory only, not part of primary verdict) ===")
    ckm = {}
    thA_star = b1["primary_theta"]
    predB = float(abs_h_theta(axisB, mp.mpf(thA_star)))
    for k, target in CKM_E_ROW.items():
        ckm[k] = {"target": target, "predicted_B_value": predB, "rel_diff": abs(predB - target) / target}
    print(json.dumps(ckm, indent=2))
    results["ckm_bonus"] = ckm

    ratio_hits = [ratio_test["orderings"][o]["phi_inside_ratio_box"] for o in ("NO", "IO")]
    branch_hits = [b1["orderings"][o]["primary_hit"] for o in ("NO", "IO")] + \
                  [b2["orderings"][o]["primary_hit"] for o in ("NO", "IO")]
    if any(ratio_hits) or any(branch_hits):
        verdict = "INSTRUMENT-PREDICTS -- FLAG FOR cc3 THIRD OPINION"
    else:
        verdict = "INSTRUMENT-NULL"
    results["verdict"] = verdict
    results["verdict_basis"] = ("the direct ratio test (|Ue1|/|Ue2| vs phi) is the honest "
                                 "primary basis after the mid-run degeneracy discovery; the "
                                 "originally pre-committed branch grading is reported "
                                 "alongside for the record and agrees with it (same relation, "
                                 "same MISS)")
    print("\n" + "=" * 78)
    print("VERDICT:", verdict)
    print("=" * 78)
    return results


if __name__ == "__main__":
    inst, axisA, axisB = part_a_selfcheck()
    results = part_bc_prediction(inst, axisA, axisB)
    import json
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2, sort_keys=False)
    print("\nWrote results.json")
