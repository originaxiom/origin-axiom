"""E2 -- THE SILVER SPLIT RESOLUTION (PREREG_L5.md, E2 clause). Compute agent:
loop 5 cell E2 (anatomy campaign).

QUESTION (PREREG_L5.md, section E2): D3 (loop4/d3_silvercup) proved the SILVER
vector-cup pairing [u_i cup_x u_j] in H^2(D_silver;27bar) FORM-MATCHES golden's
C1/D1 table exactly: one mute off-diagonal pair -- classes (0,1) in the
w2_silver basis -- plus the Koszul diagonal, rank 5 (d3_results.json:
zero_offdiag_pairs = ["01","10"], all other 18 off-diagonal pairs nonzero). At
GOLDEN, the mute pair [c_01] IS the boundary-born pair (w1_portal.py's
B637-sourced split; loop4/d1_pairing's block table: "[c_01] (boundary-boundary)
= ZERO"). At SILVER, the boundary/solo split of the 5 H^1 classes is UNRESOLVED
-- w2_silver/FINDINGS_CC2.md's own caveat: "silver's portal is exactly
UPPER-TRIANGULAR with no analogous zero block ... deciding requires a canonical
boundary-restriction decomposition on the silver double (priced, one cell)."
THIS CELL builds that decomposition and answers: IS THE SILVER MUTE PAIR THE
BOUNDARY PAIR?

===========================================================================
THE GOLDEN CONVENTION FOR "BOUNDARY-BORN" (read off B637_corrected_cell3's
FINDINGS.md and w1_portal.py's own restatement -- STATED EXPLICITLY, as
required):

  B637 built D = M cup_{T^2} Mbar via the amalgam presentation (cell3b_stage1.py,
  banked stage1_classes.pkl):
      pi_1(D) = <a,b,c | R1=REL(a,b), R2=REL(a,c), R3=LAM(a,c).LAM(a,b)^-1>
  where 'a' is the SHARED meridian generator (identical, unrenamed, in both
  copies' relators R1/R2 -- cell3b_stage1.py's own comment: "c = the mirror
  copy's b"), and R3 identifies the two copies' LONGITUDE words (LAM =
  'abABaaBAbA', CELL3A_PREREG's "true longitude", the SAME word used to build
  R3). So the double's PERIPHERAL SUBGROUP (pi_1 of the boundary torus T^2) is
  the abelian rank-2 subgroup <mu, lambda> with mu = the word 'a', lambda = the
  word 'abABaaBAbA'.

  w1_portal.py (STEP 7, "THE SPLIT") states the B637 naming VERBATIM: classes
  {0,1} = "boundary-born" ("the coker-delta^0 pair" -- the image of the
  Mayer-Vietoris connecting map H^0(T^2;V) -> H^1(D;V)); classes {2,3,4} =
  "solo-inherited" (classes that restrict nontrivially into H^1(M)/H^1(Mbar)
  individually). B637/w1_portal.py do NOT themselves compute this split via an
  explicit peripheral-RESTRICTION map on H^1(D) -- they read it off the
  Fox-calculus construction's own bookkeeping. THIS CELL BUILDS the missing
  restriction map from first principles and uses the ALREADY-BANKED golden
  split (0,1 boundary / 2,3,4 solo) purely as the CONTROL to calibrate it.

THE PRECISE RESTRICTION CRITERION (as the prereg specifies: "nonzero
restriction cocycle class on the torus = Z^1/B^1 of the restricted action, NOT
just nonzero cocycle values" -- naive nonzero-on-a-generator is not
coboundary-invariant / not gauge-independent):

  For a class represented by cocycle u in Z^1(D;V), restrict it to the
  peripheral subgroup <mu,lambda> by evaluating u on the two peripheral WORDS:
  u(mu), u(lambda) in V (via the standard bar-resolution cocycle recursion).
  The restricted pair is a genuine class in H^1(T^2;V) = Z^1(T^2;V)/B^1(T^2;V)
  (T^2 abelian, rank 2): it is a COBOUNDARY (i.e. the restriction of u to T^2 is
  ZERO in H^1(T^2;V)) iff there EXISTS a single v in V with
      u(mu)     = rho(mu).v     - v        AND
      u(lambda) = rho(lambda).v - v                     SIMULTANEOUSLY.
  This is checked exactly by stacking (rho(mu)-I) and (rho(lambda)-I) as a
  54-row/27-col augmented linear system (target = (u(mu), u(lambda))) and
  testing RREF consistency (no pivot in the augmented column) -- exact field
  arithmetic throughout, zero floats.

  We do NOT presuppose which direction ("restriction nonzero" vs "restriction
  IS a coboundary / zero") is the one B637 meant by "boundary-born": BOTH
  labelings are computed on the golden 5-class basis and compared against the
  ALREADY-BANKED split {0,1}=boundary, {2,3,4}=solo (w1_portal.py's
  BOUNDARY_BORN/SOLO_INHERITED constants). Whichever direction reproduces that
  split EXACTLY is the CONVENTION -- adopted UNCHANGED for silver. If NEITHER
  direction reproduces it exactly: STOP, report DEGENERATE (per the prereg's
  hard gate: "the golden control must reproduce the banked 2 boundary + 3 solo
  split exactly" before any silver work).

===========================================================================
THE SILVER PERIPHERAL WORDS (read off B649_silver_holonomy/FINDINGS.md and
PREREG_STAGE3A.md -- STATED explicitly, not invented here):

  Silver M's own (solo, pre-double) presentation: <a,b,c | aBAbcc, aaCbcB>
  (FINDINGS.md, "S1-G1 PASS ... Presentation <a,b,c|aBAbcc,aaCbcB>; peripheral
  (CCB, caCA)."). So silver's own (meridian, longitude) = (CCB, caCA), words in
  a,b,c.

  The silver DOUBLE's presentation (b649_stage3b_swap.py, same construction
  d3_silvercup.py execs): <a,b,c,d,e,f | R1=aBAbcc, R2=aaCbcB, R1'=dEDeff,
  R2'=ddFefE, Rmu=CCBeff, Rlambda=caCAfdFD> (PREREG_STAGE3A.md: "Rmu = CCBeff
  (mu1 mu2^-1), Rlambda = caCAfdFD (lambda1 lambda2)" -- "the fig-8 convention:
  mu2=mu1, lambda2=lambda1^-1"). The two gluing relators identify side-1's
  peripheral words CCB/caCA with side-2's (d,e,f) mirror words up to sign; we
  use SIDE-1's own words mu_S = 'CCB', lambda_S = 'caCA' as generators of the
  SAME (abelian, rank-2) peripheral subgroup living inside the silver double's
  6-generator presentation -- exactly analogous to golden's mu='a',
  lambda='abABaaBAbA'.

METHOD: identical machinery both sides -- cocycle_val/rho_word
(c1_vecmassey.py's small bar-resolution recursion pattern), the generic
joint-coboundary consistency solve described above. GOLDEN gate runs FIRST
(hard gate); silver only proceeds if golden's control passes exactly.

Repo (origin-axiom) READ-ONLY throughout; all writes confined to this cell's
directory. Exact field arithmetic: K = Q(sqrt(-3)) (Fraction pairs) for golden,
L = Q(s,i) (Fraction 4-tuples, s^4=8s^2+16) for silver. Zero floats anywhere.
"""
import os
import sys
import time
import json

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
W1_PORTAL = "<seat-workdir>/invariant_line/w1_portal/w1_portal.py"
SWAP = "<repo>/frontier/B649_silver_holonomy/b649_stage3b_swap.py"

gates = {}
result = {
    "prereg_note": "PREREG_L5.md (loop5), E2 clause -- THE SILVER SPLIT RESOLUTION",
}

# ===========================================================================
# GENERIC (field-agnostic) machinery -- works for any field-element type that
# supports .is_zero(), .inv(), + - * (both K = Q(sqrt(-3)) and L = Q(s,i)).
# ===========================================================================


def vadd(u, v):
    assert len(u) == len(v)
    return [u[i] + v[i] for i in range(len(u))]


def generic_rref(rows):
    """Exact Gaussian elimination (field-agnostic); returns (echelon rows,
    pivot column list). Same pattern as d3_silvercup.py's local rrefL /
    w1_portal.py's rref."""
    A = [r[:] for r in rows]
    m = len(A)
    ncols = len(A[0]) if m else 0
    r = 0
    pivs = []
    for c in range(ncols):
        piv = next((k for k in range(r, m) if not A[k][c].is_zero()), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv_inv = A[r][c].inv()
        A[r] = [x * pv_inv for x in A[r]]
        for k in range(m):
            if k != r and not A[k][c].is_zero():
                f = A[k][c]
                A[k] = [x - f * y for x, y in zip(A[k], A[r])]
        pivs.append(c)
        r += 1
        if r == m:
            break
    return A, pivs


def make_cocycle_fns(acts, apply_fn, mmul_fn, meye_fn, dim, ZERO):
    """c1_vecmassey.py's tiny lv/cocycle_val/rho_word pattern, parameterized
    over (acts, apply, mmul, meye, dim, ZERO) so the SAME code runs on golden
    (K, d=27, acts=a/b/c) and silver (L, d=27, acts=LETS a..f)."""

    def lv(zc, ch):
        low = ch.lower()
        if ch.islower():
            return zc[low]
        return [ZERO - x for x in apply_fn(acts[ch], zc[low])]

    def cocycle_val(zc, word):
        val = [ZERO] * dim
        P = meye_fn(dim)
        for ch in word:
            add = apply_fn(P, lv(zc, ch))
            val = vadd(val, add)
            P = mmul_fn(P, acts[ch])
        return val

    def rho_word(word):
        P = meye_fn(dim)
        for ch in word:
            P = mmul_fn(P, acts[ch])
        return P

    return cocycle_val, rho_word


def commute_check(A, B, mmul_fn, dim):
    AB = mmul_fn(A, B)
    BA = mmul_fn(B, A)
    return all((AB[i][j] - BA[i][j]).is_zero() for i in range(dim) for j in range(dim))


def coboundary_consistent(rho_mu, rho_lam, u_mu, u_lam, dim, ZERO, ONE):
    """True iff EXISTS v with u_mu = rho_mu.v - v AND u_lam = rho_lam.v - v
    SIMULTANEOUSLY -- i.e. the restriction of the cocycle to the (abelian)
    peripheral subgroup <mu,lambda> is a COBOUNDARY (zero in H^1(T^2;V))."""
    rows = []
    for i in range(dim):
        row = [(rho_mu[i][j] - (ONE if i == j else ZERO)) for j in range(dim)] + [u_mu[i]]
        rows.append(row)
    for i in range(dim):
        row = [(rho_lam[i][j] - (ONE if i == j else ZERO)) for j in range(dim)] + [u_lam[i]]
        rows.append(row)
    _, piv = generic_rref(rows)
    return dim not in piv


def fmtK(x):
    if x.is_zero():
        return "0"
    if x.b == 0:
        return str(x.a)
    return f"({x.a}{'+' if x.b > 0 else ''}{x.b}*sqrt(-3))"


def fmtL(x):
    if x.is_zero():
        return "0"

    def poly_str(coeffs, varname):
        terms = []
        for k, c in enumerate(coeffs):
            if c == 0:
                continue
            if k == 0:
                terms.append(f"{c}")
            elif k == 1:
                terms.append(f"{c}*{varname}")
            else:
                terms.append(f"{c}*{varname}^{k}")
        return "+".join(terms) if terms else "0"

    re_s = poly_str(x.re, "s")
    im_s = poly_str(x.im, "s")
    if im_s == "0":
        return re_s
    return f"({re_s}) + i*({im_s})"


# ===========================================================================
log("=== PART 1: GOLDEN CONTROL (hard gate -- must reproduce banked 2+3 split "
    "before any silver work) ===")
log("STEP G0: exec w1_portal.py verbatim through its own STEP 5 (same cut "
    "point c1_vecmassey.py used: 'log(\"STEP 6:') -- B575 prefix, pkl "
    "rehydration (cell3_double/stage1_classes.pkl), C27 via J, dual Fox "
    "machinery. Source READ only.")
src_g = open(W1_PORTAL).read()
cut_g = src_g.index('log("STEP 6:')
ns_g = {"__name__": "w1_prefix", "__file__": W1_PORTAL}
t0 = time.time()
exec(compile(src_g[:cut_g], W1_PORTAL, "exec"), ns_g)
log(f"  w1_portal STEP0-5 done ({time.time()-t0:.0f}s)")

K, K0, K1 = ns_g["K"], ns_g["K0"], ns_g["K1"]
GENS_g = ns_g["GENS"]
acts_g = ns_g["acts"]
apply_g = ns_g["apply"]
mmul_g, meye_g = ns_g["mmul"], ns_g["meye"]
classes_g = ns_g["classes"]
h1_bank = ns_g["h1_bank"]
d_g = 27

for k in ("C27_inverse_consistent", "relator_R1", "relator_R2", "relator_R3", "v0_dim1"):
    gates[f"golden_inherited_{k}"] = ns_g["gates"][k]
log(f"  inherited w1_portal gates: "
    f"{ {k: v for k, v in gates.items() if k.startswith('golden_inherited')} }")
assert all(gates[f"golden_inherited_{k}"] for k in
           ("C27_inverse_consistent", "relator_R1", "relator_R2", "relator_R3", "v0_dim1"))
gates["golden_h1_bank_eq_5"] = (h1_bank == 5)
assert gates["golden_h1_bank_eq_5"], f"golden h1_bank={h1_bank} != 5"
log(f"  golden: 5 H^1(D;27) classes rehydrated (banked h1={h1_bank}); "
    f"pi_1(D) = <a,b,c | R1,R2,R3> (a=shared meridian, cell3b_stage1.py)")

MU_G = "a"
LAM_G = "abABaaBAbA"
log(f"  golden peripheral words: mu = {MU_G!r}, lambda = {LAM_G!r} "
    f"(CELL3A_PREREG's 'true longitude'; SAME word cell3b_stage1.py's R3 uses)")

cocycle_val_g, rho_word_g = make_cocycle_fns(acts_g, apply_g, mmul_g, meye_g, d_g, K0)
rho_mu_g = rho_word_g(MU_G)
rho_lam_g = rho_word_g(LAM_G)

gates["golden_peripheral_commute"] = commute_check(rho_mu_g, rho_lam_g, mmul_g, d_g)
log(f"  CONTROL: rho(mu).rho(lambda) == rho(lambda).rho(mu) exactly "
    f"(peripheral subgroup is abelian, rep-level check): "
    f"{gates['golden_peripheral_commute']}")
assert gates["golden_peripheral_commute"], "golden mu,lambda do not commute at rep level -- STOP"

gates["golden_mu_nontrivial"] = not all(
    (rho_mu_g[i][j] - (K1 if i == j else K0)).is_zero() for i in range(d_g) for j in range(d_g))
log(f"  sanity: rho(mu) != identity: {gates['golden_mu_nontrivial']}")

golden_per_class = {}
for i in range(5):
    u_mu = cocycle_val_g(classes_g[i], MU_G)
    u_lam = cocycle_val_g(classes_g[i], LAM_G)
    consistent = coboundary_consistent(rho_mu_g, rho_lam_g, u_mu, u_lam, d_g, K0, K1)
    golden_per_class[i] = {
        "u_mu": [fmtK(x) for x in u_mu],
        "u_lambda": [fmtK(x) for x in u_lam],
        "restriction_is_coboundary": consistent,
    }
    log(f"  golden class {i}: restriction to T^2 IS a coboundary (trivial on "
        f"boundary): {consistent}")

BANKED_BOUNDARY = {0, 1}
BANKED_SOLO = {2, 3, 4}
log(f"  BANKED golden split (w1_portal.py's BOUNDARY_BORN/SOLO_INHERITED, "
    f"sourced from B637_corrected_cell3/FINDINGS.md): boundary-born = "
    f"{sorted(BANKED_BOUNDARY)}, solo-inherited = {sorted(BANKED_SOLO)}")

detected_if_inconsistent = {i for i in range(5) if not golden_per_class[i]["restriction_is_coboundary"]}
detected_if_consistent = {i for i in range(5) if golden_per_class[i]["restriction_is_coboundary"]}
log(f"  convention A ('boundary-detected' = restriction NONZERO / NOT a "
    f"coboundary): {sorted(detected_if_inconsistent)}")
log(f"  convention B ('boundary-detected' = restriction ZERO / IS a "
    f"coboundary): {sorted(detected_if_consistent)}")

conv_A_match = (detected_if_inconsistent == BANKED_BOUNDARY)
conv_B_match = (detected_if_consistent == BANKED_BOUNDARY)
gates["golden_control_gate"] = conv_A_match or conv_B_match
gates["golden_control_unambiguous"] = not (conv_A_match and conv_B_match)

if conv_A_match:
    CONVENTION = "A"
    CONVENTION_NOTE = ("boundary-DETECTED := the cocycle's restriction to the "
                        "peripheral subgroup <mu,lambda> is NONZERO in "
                        "H^1(T^2;V) (NOT a coboundary of the restricted action)")
elif conv_B_match:
    CONVENTION = "B"
    CONVENTION_NOTE = ("boundary-DETECTED := the cocycle's restriction to the "
                        "peripheral subgroup <mu,lambda> IS a coboundary "
                        "(ZERO in H^1(T^2;V)) of the restricted action")
else:
    CONVENTION = None
    CONVENTION_NOTE = "NEITHER direction reproduced the banked golden split"

log(f"  GOLDEN CONTROL GATE: {'PASS' if gates['golden_control_gate'] else 'FAIL -- STOP, no improvisation'}"
    f"  (convention adopted: {CONVENTION})")
if CONVENTION is not None:
    log(f"  CONVENTION: {CONVENTION_NOTE}")

result["golden_control"] = {
    "peripheral_words": {"mu": MU_G, "lambda": LAM_G},
    "presentation_note": "pi_1(D)=<a,b,c|R1=REL(a,b),R2=REL(a,c),R3=LAM(a,c)LAM(a,b)^-1>, a=shared meridian (cell3b_stage1.py)",
    "banked_split_source": "w1_portal.py STEP7 (B637_corrected_cell3/FINDINGS.md 'coker-delta^0 pair' naming)",
    "banked_boundary_born": sorted(BANKED_BOUNDARY),
    "banked_solo_inherited": sorted(BANKED_SOLO),
    "per_class": golden_per_class,
    "convention_A_detected_set": sorted(detected_if_inconsistent),
    "convention_B_detected_set": sorted(detected_if_consistent),
    "convention_A_matches_banked": conv_A_match,
    "convention_B_matches_banked": conv_B_match,
    "convention_adopted": CONVENTION,
    "convention_note": CONVENTION_NOTE,
    "gates": {k: v for k, v in gates.items() if k.startswith("golden_")},
}

if not gates["golden_control_gate"]:
    log("STOP: golden control gate FAILED -- the restriction criterion does "
        "not reproduce the banked split under EITHER direction. Per protocol, "
        "no improvisation: reporting DEGENERATE and exiting before any silver "
        "computation.")
    result["verdict"] = "DEGENERATE: golden control gate failed -- restriction " \
        "criterion (Z^1/B^1 of the peripheral-subgroup-restricted cocycle) " \
        "does not reproduce the banked B637 split {0,1}-boundary/{2,3,4}-solo " \
        "under either labeling direction; criterion inconclusive at the " \
        "control stage, silver NOT attempted."
    result["all_gates_pass"] = all(v for v in gates.values() if isinstance(v, bool))
    result["runtime_s"] = time.time() - T0
    with open(os.path.join(HERE, "e2_results.json"), "w") as f:
        json.dump(result, f, indent=2)
    log(f"saved {os.path.join(HERE, 'e2_results.json')}")
    sys.exit(1)

# ===========================================================================
log("=== PART 2: SILVER (the actual question -- runs only because the "
    "golden gate above PASSED) ===")
log("STEP S0: exec b649_stage3b_swap.py prefix (weld + silver DOUBLE "
    "Fox/Z1/cob/reps) -- SAME cut point d3_silvercup.py/w2a_silver.py used "
    "('# ---- sigma* ---'). Source READ only.")
src_s = open(SWAP).read()
cut_s = src_s.index("# ---- sigma* ---")
ns_s = {"__name__": "b649_double_prefix", "__file__": SWAP}
t0 = time.time()
exec(compile(src_s[:cut_s], SWAP, "exec"), ns_s)
log(f"  b649_stage3b_swap prefix done ({time.time()-t0:.0f}s)")

L, Lc, L0, L1 = ns_s["L"], ns_s["Lc"], ns_s["L0"], ns_s["L1"]
meye_s, mmul_s = ns_s["meye"], ns_s["mmul"]
LETS = ns_s["LETS"]
RELATORS_D, GENS_D = ns_s["RELATORS"], ns_s["GENS"]
Z1_D, cob_D, nc_D, reps = ns_s["Z1"], ns_s["cob"], ns_s["nc"], ns_s["reps"]
d_s = 27
log(f"  double presentation: GENS={GENS_D!r}  RELATORS={RELATORS_D}")

h0_D = d_s - nc_D
h1_D = len(Z1_D) - nc_D
gates["silver_double_h0_eq_1"] = (h0_D == 1)
gates["silver_double_h1_eq_5"] = (h1_D == 5)
log(f"  double: h0(D)={h0_D} h1(D)={h1_D}  GATE(h0=1,h1=5): "
    f"{'PASS' if (gates['silver_double_h0_eq_1'] and gates['silver_double_h1_eq_5']) else 'FAIL'}")
assert gates["silver_double_h0_eq_1"] and gates["silver_double_h1_eq_5"]


def matvec_s(M, v):
    n = len(v)
    return [sum((M[i][k] * v[k] for k in range(n) if not v[k].is_zero()), L0)
            for i in range(len(M))]


def slice_rep(u162):
    return {g: u162[27 * i:27 * (i + 1)] for i, g in enumerate(GENS_D)}


classes_s = [slice_rep(r) for r in reps]
assert len(classes_s) == 5
log(f"  {len(classes_s)} silver H^1(D_silver;27) classes sliced from reps "
    f"(same basis/order as loop4/d3_silvercup.py and w2a_silver.py)")

MU_S = "CCB"
LAM_S = "caCA"
log(f"  silver peripheral words: mu = {MU_S!r}, lambda = {LAM_S!r} "
    f"(B649_silver_holonomy/FINDINGS.md: 'peripheral (CCB, caCA)'; "
    f"PREREG_STAGE3A.md: 'Rmu=CCBeff (mu1 mu2^-1), Rlambda=caCAfdFD "
    f"(lambda1 lambda2)')")

cocycle_val_s, rho_word_s = make_cocycle_fns(LETS, matvec_s, mmul_s, meye_s, d_s, L0)
rho_mu_s = rho_word_s(MU_S)
rho_lam_s = rho_word_s(LAM_S)

gates["silver_peripheral_commute"] = commute_check(rho_mu_s, rho_lam_s, mmul_s, d_s)
log(f"  CONTROL: rho(mu).rho(lambda) == rho(lambda).rho(mu) exactly "
    f"(peripheral subgroup abelian, rep-level check): "
    f"{gates['silver_peripheral_commute']}")
assert gates["silver_peripheral_commute"], "silver mu,lambda do not commute at rep level -- STOP"

gates["silver_mu_nontrivial"] = not all(
    (rho_mu_s[i][j] - (L1 if i == j else L0)).is_zero() for i in range(d_s) for j in range(d_s))
log(f"  sanity: rho(mu) != identity: {gates['silver_mu_nontrivial']}")

silver_per_class = {}
for i in range(5):
    u_mu = cocycle_val_s(classes_s[i], MU_S)
    u_lam = cocycle_val_s(classes_s[i], LAM_S)
    consistent = coboundary_consistent(rho_mu_s, rho_lam_s, u_mu, u_lam, d_s, L0, L1)
    silver_per_class[i] = {
        "u_mu": [fmtL(x) for x in u_mu],
        "u_lambda": [fmtL(x) for x in u_lam],
        "restriction_is_coboundary": consistent,
    }
    log(f"  silver class {i}: restriction to T^2 IS a coboundary (trivial on "
        f"boundary): {consistent}")

if CONVENTION == "A":
    silver_boundary_detected = {i for i in range(5) if not silver_per_class[i]["restriction_is_coboundary"]}
else:  # CONVENTION == "B"
    silver_boundary_detected = {i for i in range(5) if silver_per_class[i]["restriction_is_coboundary"]}

log(f"  SILVER boundary-DETECTED classes (convention {CONVENTION} applied "
    f"identically to golden): {sorted(silver_boundary_detected)}")

# ---- cross-check against the ALREADY-BANKED D3 mute pair -------------------
D3_RESULTS = "<seat-workdir>/anatomy/loop4/d3_silvercup/d3_results.json"
d3 = json.load(open(D3_RESULTS))
SILVER_MUTE_PAIR = {0, 1}   # d3_results.json: zero_offdiag_pairs == ["01","10"]
gates["silver_mute_pair_matches_d3_banked"] = (
    set(d3["zero_offdiag_pairs"]) == {"01", "10"})
log(f"  cross-check: d3_results.json zero_offdiag_pairs = "
    f"{d3['zero_offdiag_pairs']} (expected ['01','10']): "
    f"{gates['silver_mute_pair_matches_d3_banked']}")
assert gates["silver_mute_pair_matches_d3_banked"]

SILVER_NONMUTE = {2, 3, 4}
if silver_boundary_detected == SILVER_MUTE_PAIR:
    verdict = ("MUTE-PAIR-IS-BOUNDARY: the silver mute vector-cup pair "
                "{0,1} is EXACTLY the boundary-detected set under the "
                "golden-calibrated restriction criterion (convention "
                f"{CONVENTION}). The golden form-match becomes exact in "
                "MEANING: the boundary pair is mute at BOTH golden and "
                "silver.")
elif len(silver_boundary_detected) == 0 or len(silver_boundary_detected) == 5:
    verdict = (f"DEGENERATE: the restriction criterion collapses on silver "
               f"(boundary-detected = {sorted(silver_boundary_detected)}, "
               f"either none or all 5 classes) -- does not cleanly identify "
               f"any boundary/solo split, so it cannot be compared to the "
               f"mute pair {{0,1}} either way.")
else:
    verdict = (f"MUTE-PAIR-NOT-BOUNDARY: the restriction criterion (convention "
               f"{CONVENTION}, golden-gated) detects boundary classes "
               f"{sorted(silver_boundary_detected)} on silver, NOT the mute "
               f"pair {{0,1}} -- the silver mute pair is a DIFFERENT structure "
               f"from the boundary split.")

log(f"*** VERDICT: {verdict} ***")

# ===========================================================================
gates["control_exactness"] = True
log("  exactness: golden in K=Q(sqrt(-3)), silver in L=Q(s,i) (s^4=8s^2+16), "
    "Fraction arithmetic throughout; zero floats anywhere: PASS by construction")

all_gates_pass = all(v for v in gates.values() if isinstance(v, bool))
log(f"ALL GATES PASS: {all_gates_pass}")

result.update({
    "silver": {
        "double_presentation": {"gens": GENS_D, "relators": RELATORS_D},
        "peripheral_words": {"mu": MU_S, "lambda": LAM_S},
        "peripheral_source": "B649_silver_holonomy/FINDINGS.md ('peripheral (CCB, caCA)') + PREREG_STAGE3A.md (Rmu/Rlambda gluing relators)",
        "double_dims": {"h0": h0_D, "h1": h1_D},
        "per_class": silver_per_class,
        "convention_applied": CONVENTION,
        "boundary_detected_set": sorted(silver_boundary_detected),
        "d3_banked_mute_pair": sorted(SILVER_MUTE_PAIR),
        "d3_banked_nonzero_pairs": d3["nonvanishing_pairs"],
        "d3_zero_offdiag_pairs": d3["zero_offdiag_pairs"],
    },
    "gates": gates,
    "verdict": verdict,
    "all_gates_pass": all_gates_pass,
    "runtime_s": time.time() - T0,
})

with open(os.path.join(HERE, "e2_results.json"), "w") as f:
    json.dump(result, f, indent=2)
log(f"saved {os.path.join(HERE, 'e2_results.json')}")
log("DONE.")
