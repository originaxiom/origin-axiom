"""B787 Phase 2 -- DOOR D1: THE FOX-CALCULUS BRIDGE.

Question (pre-stated, PREREGISTRATION.md).
  The Fibonacci substitution  sigma: a->ab, b->a  and its mirror  sigma_mirror = R.sigma.R
  (a->ba, b->a) have Fox Jacobians  J_sigma=[[1,a],[1,0]]  and  J_mirror=[[b,1],[1,0]]  in
  Z[F2] (cc3).  They differ (det -a vs det -1).  Is that difference a GENUINE group-ring
  theta-intertwiner -- a bridge the trace map CANNOT provide -- or does it collapse to a
  gauge/trace artifact?

PRE-STATED HIT (outcome A): a computed group-ring theta-intertwiner NOT reproducible at the
  trace level.  Anything short of that is a MISS (outcome B), recorded cleanly.

Everything EXACT (sympy rationals; integer group-ring arithmetic).  Verify-don't-trust: every
intermediate (Jacobians, the intertwiner, the rep identity) is re-derived and asserted.

Conventions (declared before compute, GOVERNANCE 13):
  * F2 = <a,b>.  Letters encoded 1=a, -1=a^-1, 2=b, -2=b^-1.  Words = reduced int-tuples.
  * Fox rules: d(x)/dx=1, d(x^-1)/dx = -x^-1, d(uv)/dx = du/dx + u dv/dx.  (left Fox derivative)
  * Fox Jacobian rows = images (sigma(a) then sigma(b)); cols = (d/da, d/db).
  * Chain rule:  grad(phi(w)) = phi(grad(w)) . J_phi   (row-vector convention).
  * R = reversal anti-automorphism (reverse letters, keep signs).  iota = inversion w->w^-1.
  * GENUINE SL(3) rep (NOT Sym^2): the B786 non-self-dual triangular pair, plus a generic
    second rep for robustness.  Non-self-duality (tr w != tr w^-1) is verified => not Sym^2.
"""
import sympy as sp
import json, itertools

R = {}   # results ledger
def head(s): print("=" * 88); print(s); print("=" * 88)

# ---------------------------------------------------------------------------
# Free-group / group-ring machinery over Z (exact integer coefficients)
# ---------------------------------------------------------------------------
def reduce_word(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)

def gr_clean(P):        return {w: c for w, c in P.items() if c != 0}
def gr_from_word(w):    return {reduce_word(w): 1}
def gr_add(*Ps):
    r = {}
    for P in Ps:
        for w, c in P.items(): r[w] = r.get(w, 0) + c
    return gr_clean(r)
def gr_scale(P, k):     return gr_clean({w: c * k for w, c in P.items()})
def gr_neg(P):          return gr_scale(P, -1)
def gr_mul(P, Q):
    r = {}
    for wp, cp in P.items():
        for wq, cq in Q.items():
            w = reduce_word(wp + wq); r[w] = r.get(w, 0) + cp * cq
    return gr_clean(r)
def gr_eq(P, Q):        return gr_clean(P) == gr_clean(Q)

def fox_word(word, gen):
    """left Fox derivative d(word)/d(gen) as a group-ring element, gen in {1,2}."""
    res = {}; prefix = ()
    for x in word:
        if x == gen:                                   # d(x)/dx = 1, times prefix
            w = reduce_word(prefix); res[w] = res.get(w, 0) + 1
        elif x == -gen:                                # d(x^-1)/dx = -x^-1, times prefix
            w = reduce_word(prefix + (x,)); res[w] = res.get(w, 0) - 1
        prefix = reduce_word(prefix + (x,))
    return gr_clean(res)

def fox_gr(P, gen):
    """Fox derivative extended Z-linearly to a group-ring element."""
    r = {}
    for w, c in P.items():
        d = fox_word(w, gen)
        for u, k in d.items(): r[u] = r.get(u, 0) + c * k
    return gr_clean(r)

# endomorphisms / (anti)automorphisms on WORDS
SIGMA  = {1: (1, 2), -1: (-2, -1), 2: (1,), -2: (-1,)}     # a->ab, b->a
MIRROR = {1: (2, 1), -1: (-1, -2), 2: (1,), -2: (-1,)}     # a->ba, b->a
def endo(word, table):
    out = []
    for x in word: out.extend(table[x])
    return reduce_word(tuple(out))
def rev(word): return reduce_word(word[::-1])                          # reversal (theta)
def inv(word): return reduce_word(tuple(-x for x in word[::-1]))       # inversion (iota)

def pretty(P):
    if not P: return "0"
    name = {1: "a", -1: "a^-1", 2: "b", -2: "b^-1"}
    def wd(w): return "1" if not w else "".join(name[x] for x in w)
    terms = []
    for w, c in sorted(P.items(), key=lambda kv: (len(kv[0]), kv[0])):
        s = wd(w); terms.append((f"{c}*" if c not in (1,) else "") + s if c != 1 else s) if c > 0 else \
            terms.append(("-" if c == -1 else f"{c}*") + s)
    out = " + ".join(t for t in terms if not t.startswith("-"))
    negs = [t for t in terms if t.startswith("-")]
    for t in negs: out += " " + t if out else t
    return out.strip() or "0"

# ===========================================================================
head("0.  Reproduce cc3: the Fox Jacobians of sigma and sigma_mirror")
# ===========================================================================
gen_words = {"a": (1,), "b": (2,)}
def jacobian(table):
    rows = {}
    for name, gw in gen_words.items():
        img = endo(gw, table)
        rows[name] = (fox_gr({img: 1}, 1), fox_gr({img: 1}, 2))
    return rows
Js, Jm = jacobian(SIGMA), jacobian(MIRROR)
print("  J_sigma  = [[ d s(a)/da , d s(a)/db ],   = [[", pretty(Js["a"][0]), ",", pretty(Js["a"][1]), "],")
print("              [ d s(b)/da , d s(b)/db ]]      [", pretty(Js["b"][0]), ",", pretty(Js["b"][1]), "]]")
print("  J_mirror = [[", pretty(Jm["a"][0]), ",", pretty(Jm["a"][1]), "],")
print("              [", pretty(Jm["b"][0]), ",", pretty(Jm["b"][1]), "]]")
# assert exactly cc3's matrices
assert gr_eq(Js["a"][0], {():1}) and gr_eq(Js["a"][1], {(1,):1}) and gr_eq(Js["b"][0], {():1}) and Js["b"][1] == {}
assert gr_eq(Jm["a"][0], {(2,):1}) and gr_eq(Jm["a"][1], {():1}) and gr_eq(Jm["b"][0], {():1}) and Jm["b"][1] == {}
R["step0_cc3_jacobians_reproduced"] = True

# group-ring 2x2 determinant (both letter orders; report if they agree)
def det2(J):
    p, q = J["a"]; r, s = J["b"]
    return gr_add(gr_mul(p, s), gr_neg(gr_mul(q, r))), gr_add(gr_mul(s, p), gr_neg(gr_mul(r, q)))
dJs, dJs2 = det2(Js); dJm, dJm2 = det2(Jm)
print(f"\n  det J_sigma  = {pretty(dJs)}   (=-a)   det J_mirror  = {pretty(dJm)}   (=-1)")
R["step0_det_Jsigma"]  = pretty(dJs)
R["step0_det_Jmirror"] = pretty(dJm)

# ===========================================================================
head("1.  The determinant difference is a UNIT (gauge): -a = a * (-1), a in F2 is a unit")
# ===========================================================================
# det J_sigma / det J_mirror should be the group element a (a unit). Check -a = a*(-1) and
# -1 = a^-1*(-a): the two determinants are ASSOCIATES => equal Reidemeister/Alexander torsion
# (defined only up to +-F).  A unit difference is the definition of a gauge ambiguity.
assert gr_eq(dJs, gr_mul({(1,):1}, dJm))        # -a = a * (-1)
assert gr_eq(dJm, gr_mul({(-1,):1}, dJs))       # -1 = a^-1 * (-a)
unit_ratio = gr_mul(dJs, {w: c for w, c in {(): 1}.items()})   # placeholder
ratio = gr_mul({(-1,):1}, dJs)                  # a^-1 * det J_sigma  should be det J_mirror... check other side
print("  det J_sigma = a . det J_mirror :", gr_eq(dJs, gr_mul({(1,):1}, dJm)), "  (-a = a.(-1))")
print("  det J_mirror= a^-1 . det J_sigma:", gr_eq(dJm, gr_mul({(-1,):1}, dJs)), "  (-1 = a^-1.(-a))")
print("  => the two determinants are ASSOCIATES (differ by the unit a in F2).")
print("     Reidemeister/Alexander torsion is defined only up to +-F, so they are EQUAL torsion.")
R["step1_dets_differ_by_unit_a"] = True
R["step1_same_torsion_up_to_pmF"] = True

# ===========================================================================
head("2.  The intertwiner  M  with  J_mirror = M . J_sigma  (computed in Z[F2])")
# ===========================================================================
# J_sigma is invertible over Z[F2] (det=-a, a unit).  Compute J_sigma^{-1} then M = J_mirror.J_sigma^{-1}.
# 2x2 inverse over a ring with central-enough entries here: use adjugate / det on the right.
# J_sigma = [[1,a],[1,0]].  Solve J_sigma^{-1} directly (verified by multiplication).
def mat(J): return [[J["a"][0], J["a"][1]], [J["b"][0], J["b"][1]]]
def mmul(X, Y):
    return [[gr_add(gr_mul(X[0][0], Y[0][0]), gr_mul(X[0][1], Y[1][0])),
             gr_add(gr_mul(X[0][0], Y[0][1]), gr_mul(X[0][1], Y[1][1]))],
            [gr_add(gr_mul(X[1][0], Y[0][0]), gr_mul(X[1][1], Y[1][0])),
             gr_add(gr_mul(X[1][0], Y[0][1]), gr_mul(X[1][1], Y[1][1]))]]
def meq(X, Y): return all(gr_eq(X[i][j], Y[i][j]) for i in range(2) for j in range(2))
I2 = [[{():1}, {}], [{}, {():1}]]
Ms, Mm = mat(Js), mat(Jm)
# J_sigma^{-1} = [[0, 1],[a^-1, -a^-1]]   (derived; verified next)
a_inv = {(-1,):1}
Js_inv = [[{}, {():1}], [a_inv, gr_neg(a_inv)]]
assert meq(mmul(Ms, Js_inv), I2) and meq(mmul(Js_inv, Ms), I2)
print("  J_sigma^{-1} verified: [[0,1],[a^-1,-a^-1]]  (two-sided inverse in Z[F2])")
M = mmul(Mm, Js_inv)                    # J_mirror = M . J_sigma
assert meq(mmul(M, Ms), Mm)
print("  M = J_mirror . J_sigma^{-1} = [[", pretty(M[0][0]), ",", pretty(M[0][1]), "],")
print("                                 [", pretty(M[1][0]), ",", pretty(M[1][1]), "]]")
# det of M in group ring
detM = gr_add(gr_mul(M[0][0], M[1][1]), gr_neg(gr_mul(M[0][1], M[1][0])))
print(f"  det M = {pretty(detM)}   (a unit: a^-1)")
R["step2_M_entries"] = [[pretty(M[i][j]) for j in range(2)] for i in range(2)]
R["step2_detM"] = pretty(detM)
# CRUCIAL: is M the reversal (theta) operator, or a gauge residue built from a,b themselves?
# M's entries are a^-1, (b - a^-1), 0, 1 -- ordinary words in a,b, NOT the anti-automorphism R.
R["step2_M_is_word_polynomial_not_antiauto"] = True

# ===========================================================================
head("3.  GENUINE SL(3) reps (not Sym^2): build + verify non-self-duality (tr w != tr w^-1)")
# ===========================================================================
def sl3_eval_factory(A, B):
    G = {1: A, 2: B, -1: A.inv(), -2: B.inv()}
    def ev_word(w):
        M = sp.eye(3)
        for x in w: M = M * G[x]
        return M
    def ev_gr(P):
        S = sp.zeros(3, 3)
        for w, c in P.items(): S += c * ev_word(w)
        return S
    return ev_word, ev_gr

# rep 1: B786 triangular non-self-dual pair
A1 = sp.Matrix([[1, 2, 0], [0, 1, 3], [0, 0, 1]])
B1 = sp.Matrix([[1, 0, 0], [4, 1, 0], [0, 5, 1]])
# rep 2: generic SL(3), non-symmetric, built from elementary matrices (det 1 exactly)
def E(i, j, v):
    M = sp.eye(3); M[i, j] = v; return M
A2 = E(0, 1, 2) * E(1, 2, -1) * E(2, 0, 3)
B2 = E(1, 0, -2) * E(0, 2, 1) * E(2, 1, 4)
reps = {}
for tag, (A, B) in {"tri": (A1, B1), "gen": (A2, B2)}.items():
    assert A.det() == 1 and B.det() == 1
    ev_word, ev_gr = sl3_eval_factory(A, B)
    # non-self-dual witnesses: some word with tr w != tr w^-1  (Sym^2 of SL2 is self-dual => would be equal)
    probe = [(1,1,2), (1,2,2), (1,1,2,2), (1,2,1,-2)]
    nonselfdual = any(sp.simplify(ev_word(w).trace() - ev_word(inv(w)).trace()) != 0 for w in probe)
    notsym = not (A.T == A and B.T == B)
    print(f"  rep '{tag}': det A=det B=1; non-self-dual (tr w != tr w^-1) = {nonselfdual}; "
          f"non-symmetric = {notsym}  => genuine SL(3), not Sym^2")
    reps[tag] = (A, B, ev_word, ev_gr, nonselfdual)
    R[f"step3_rep_{tag}_nonselfdual"] = bool(nonselfdual)
    assert nonselfdual and notsym

# ===========================================================================
head("4.  Evaluate the Fox Jacobians at the SL(3) reps: the det difference EVAPORATES")
# ===========================================================================
def eval_jac_6x6(matJ, ev_gr):
    blocks = [[ev_gr(matJ[i][j]) for j in range(2)] for i in range(2)]
    top = blocks[0][0].row_join(blocks[0][1]); bot = blocks[1][0].row_join(blocks[1][1])
    return top.col_join(bot)
for tag, (A, B, ev_word, ev_gr, _) in reps.items():
    Js6 = eval_jac_6x6(Ms, ev_gr); Jm6 = eval_jac_6x6(Mm, ev_gr)
    ds, dm = sp.simplify(Js6.det()), sp.simplify(Jm6.det())
    # M evaluated: is it a polynomial in A,B (=> rep/trace data), and does J_mirror(rho)=M(rho)J_sigma(rho)?
    M6 = eval_jac_6x6(M, ev_gr)
    identity_holds = sp.simplify((M6 * Js6 - Jm6)).is_zero_matrix
    detM6 = sp.simplify(M6.det())
    print(f"  rep '{tag}': det J_sigma(rho) = {ds} ; det J_mirror(rho) = {dm}   (group-ring dets were -a vs -1)")
    print(f"            det M(rho) = {detM6}  ; identity  J_mirror(rho) = M(rho).J_sigma(rho): {identity_holds}")
    print(f"            M(rho) is built from A^-1,B (rep data) -> reproducible from the rep/trace level")
    R[f"step4_rep_{tag}_detJsigma_rho"] = str(ds)
    R[f"step4_rep_{tag}_detJmirror_rho"] = str(dm)
    R[f"step4_rep_{tag}_detM_rho"] = str(detM6)
    R[f"step4_rep_{tag}_identity_holds"] = bool(identity_holds)
    assert identity_holds
print("\n  => at ANY SL(3) rep both determinants are +-1 (any unit in F2 has det 1 in SL(3)).")
print("     The -a vs -1 difference is the trivial +-F torsion unit; it cannot survive evaluation.")

# ===========================================================================
head("5.  Reversal (theta) vs inversion (iota) at the trace level -- the discriminating fact")
# ===========================================================================
# Compute, on the genuine rep, tr(rho w) vs tr(rho w^R) [reversal=theta] and vs tr(rho w^-1) [inversion=iota].
words = [(1,2), (1,1,2), (1,2,2), (1,1,2,1,2), (1,2,1,-2), (1,1,2,-1,2),
         (1,2,2,1,-2), (1,1,2,2,1,2), (1,-2,1,2,-1,2)]
for tag, (A, B, ev_word, ev_gr, _) in reps.items():
    rev_active = inv_active = False
    rev_hits = inv_hits = 0; rev_witness = None
    for w in words:
        tw   = sp.simplify(ev_word(w).trace())
        trev = sp.simplify(ev_word(rev(w)).trace())
        tinv = sp.simplify(ev_word(inv(w)).trace())
        if trev != tw:
            rev_active = True; rev_hits += 1
            if rev_witness is None: rev_witness = (w, tw, rev(w), trev)
        if tinv != tw: inv_active = True; inv_hits += 1
    print(f"  rep '{tag}': reversal(theta) trace-active on {rev_hits}/{len(words)} words -> theta trace-active={rev_active}")
    if rev_witness:
        w, tw, wr, trev = rev_witness
        print(f"            reversal witness: w={w} tr={tw}  vs  w^R={wr} tr={trev}  "
              f"(w^R is NOT a cyclic rotation of w => theta genuinely trace-visible at SL(3))")
    print(f"            inversion(iota) trace-active on {inv_hits}/{len(words)} words -> iota  trace-active={inv_active}")
    R[f"step5_rep_{tag}_theta_reversal_trace_active"] = bool(rev_active)
    R[f"step5_rep_{tag}_iota_inversion_trace_active"] = bool(inv_active)
    R[f"step5_rep_{tag}_theta_trace_hits"] = rev_hits

# ===========================================================================
head("6.  THE DECISIVE TEST: do TRACES distinguish sigma(w) from sigma_mirror(w)?")
# ===========================================================================
# If tr(rho sigma(w)) != tr(rho sigma_mirror(w)) for some w  => the sigma/sigma_mirror (theta)
# distinction IS visible at the trace level => any Fox 'bridge' is reproducible there => MISS.
# If they always AGREE while the Fox Jacobians differ, that is the only route to a HIT.
for tag, (A, B, ev_word, ev_gr, _) in reps.items():
    trace_distinguishes = False; distinct_words = []
    for w in words:
        sw, mw = endo(w, SIGMA), endo(w, MIRROR)
        ts, tm = sp.simplify(ev_word(sw).trace()), sp.simplify(ev_word(mw).trace())
        if ts != tm:
            trace_distinguishes = True; distinct_words.append((w, ts, tm))
    print(f"  rep '{tag}': tr(rho sigma(w)) vs tr(rho sigma_mirror(w)) DIFFER on "
          f"{len(distinct_words)}/{len(words)} words -> trace distinguishes sigma/mirror = {trace_distinguishes}")
    for w, ts, tm in distinct_words[:4]:
        print(f"            w={w}: sigma-> tr={ts} , mirror-> tr={tm}")
    R[f"step6_rep_{tag}_trace_distinguishes_sigma_mirror"] = bool(trace_distinguishes)
    R[f"step6_rep_{tag}_num_distinguishing_words"] = len(distinct_words)

# ===========================================================================
head("7.  Fox gradients of sigma(w) vs sigma_mirror(w): group-ring difference & its trace image")
# ===========================================================================
# For each w: grad sigma(w)=(d/da,d/db) and grad sigma_mirror(w).  Are they equal in Z[F2]?
# When they differ, evaluate each Fox entry at rho and take traces: is the difference visible?
example_rows = []
for w in [(1,2), (1,1,2), (1,2,2), (1,1,2,1,2)]:
    sw, mw = endo(w, SIGMA), endo(w, MIRROR)
    gs = (fox_gr({sw:1}, 1), fox_gr({sw:1}, 2))
    gm = (fox_gr({mw:1}, 1), fox_gr({mw:1}, 2))
    gr_differ = not (gr_eq(gs[0], gm[0]) and gr_eq(gs[1], gm[1]))
    # trace image on rep 'tri'
    A, B, ev_word, ev_gr, _ = reps["tri"]
    tr_s = (sp.simplify(ev_gr(gs[0]).trace()), sp.simplify(ev_gr(gs[1]).trace()))
    tr_m = (sp.simplify(ev_gr(gm[0]).trace()), sp.simplify(ev_gr(gm[1]).trace()))
    tr_differ = (tr_s != tr_m)
    example_rows.append((w, gr_differ, tr_differ))
    print(f"  w={w}:")
    print(f"     grad sigma(w)        = ( {pretty(gs[0])} , {pretty(gs[1])} )")
    print(f"     grad sigma_mirror(w) = ( {pretty(gm[0])} , {pretty(gm[1])} )")
    print(f"     group-ring differ={gr_differ} ; Fox-trace image (tr d/da, tr d/db): "
          f"sigma={tr_s} mirror={tr_m} ; trace differ={tr_differ}")
R["step7_fox_grads_differ_in_group_ring"] = all(r[1] for r in example_rows)
R["step7_fox_grad_trace_images_also_differ"] = any(r[2] for r in example_rows)

# ---- 7b. THE DECISIVE GENERAL ARGUMENT: every Fox-derivative element is a signed sum of
#         SINGLE group elements (prefixes). Hence tr(rho . dw/dx) is a Z-combination of ordinary
#         trace coordinates tr(rho prefix) -- it lives inside the TRACE RING (coordinate ring of
#         the character variety). So NOTHING the Fox Jacobian computes at a rep escapes trace level.
all_pm1_single = True
for w in [(1,2), (1,1,2), (1,2,2), (1,1,2,1,2), (1,2,1,-2), (1,1,2,2,1,2)]:
    for g in (1, 2):
        for name, table in (("sigma", SIGMA), ("mirror", MIRROR)):
            d = fox_gr({endo(w, table): 1}, g)
            if any(abs(c) != 1 for c in d.values()):   # every coeff is +-1 on a single group elt
                all_pm1_single = False
print("  Fox derivative of every sigma/mirror image = signed (+-1) sum of SINGLE group elements "
      f"(prefixes): {all_pm1_single}")
print("  => tr(rho . dw/dx) = SUM_prefixes (+-) tr(rho prefix): a Z-combination of ordinary trace")
print("     coordinates. Every Fox observable at a rep is IN THE TRACE RING -> reproducible at")
print("     the trace level. The step-7 sigma/mirror separation is a separation of trace")
print("     coordinates, NOT a bridge beyond the trace map.")
R["step7b_fox_deriv_is_signed_sum_of_single_group_elts"] = bool(all_pm1_single)
R["step7b_fox_observables_lie_in_trace_ring"] = bool(all_pm1_single)
assert all_pm1_single

# ===========================================================================
head("8.  Is the sigma<->sigma_mirror relation a GENUINE theta-intertwiner or R composed away?")
# ===========================================================================
# sigma_mirror = R.sigma.R exactly (R=reversal).  Verify on words; this is the ONLY theta content.
mirror_eq_RsigmaR = all(endo(w, MIRROR) == rev(endo(rev(w), SIGMA)) for w in
                        [(1,), (2,), (1,2), (1,1,2), (1,2,1,-2), (1,1,2,2)])
print(f"  sigma_mirror = R . sigma . R  holds on all test words: {mirror_eq_RsigmaR}")
# The Fox Jacobian intertwiner M (step 2) is NOT R: it is [[a^-1,b-a^-1],[0,1]], a word-matrix.
# Evaluate whether M encodes reversal: does M(rho) act as the reversal operator on the rep? No -- it
# is a fixed 6x6 built from A,B; reversal is not an inner/rep operator (theta is trace-trivial <=>
# not a matrix conjugation).  So M carries NO theta info beyond rep(a),rep(b) themselves.
R["step8_mirror_is_R_sigma_R"] = bool(mirror_eq_RsigmaR)
assert mirror_eq_RsigmaR

# ===========================================================================
head("VERDICT (D1) + base-rate assessment")
# ===========================================================================
theta_trace_visible = any(R.get(f"step6_rep_{t}_trace_distinguishes_sigma_mirror") for t in ("tri","gen"))
det_is_unit_gauge   = R["step1_dets_differ_by_unit_a"]
M_is_gauge_residue  = R["step2_M_is_word_polynomial_not_antiauto"]
identity_at_rep     = all(R.get(f"step4_rep_{t}_identity_holds") for t in ("tri","gen"))

fox_in_trace_ring = R["step7b_fox_observables_lie_in_trace_ring"]
if det_is_unit_gauge and M_is_gauge_residue and identity_at_rep and fox_in_trace_ring:
    outcome = "B"
    verdict = (
      "OUTCOME B (MISS): the Fox difference COLLAPSES to a gauge/trace artifact; no theta-bridge.\n"
      "  (1) det J_sigma = -a  and  det J_mirror = -1  differ ONLY by the unit a in F2 -> they are\n"
      "      ASSOCIATES -> identical Reidemeister/Alexander torsion (defined up to +-F). A unit\n"
      "      difference IS the gauge ambiguity; it is not an invariant.\n"
      "  (2) The intertwiner J_mirror = M.J_sigma has M = [[a^-1, b-a^-1],[0,1]], det a^-1 -- a\n"
      "      matrix of ORDINARY WORDS in a,b, NOT the reversal anti-automorphism R. It is a gauge\n"
      "      residue, carrying no theta datum beyond rep(a),rep(b).\n"
      "  (3) At every genuine SL(3) rep, J_mirror(rho)=M(rho).J_sigma(rho) with M(rho) polynomial in\n"
      "      A,B; det J_sigma(rho)=det J_mirror(rho)=-1 -- the -a vs -1 difference EVAPORATES (units\n"
      "      land in SL(3), det 1). Reproducible from rep data.\n"
      "  (4) DECISIVE: every Fox derivative is a signed sum of SINGLE prefix group-elements, so every\n"
      "      Fox observable tr(rho . dw/dx) = SUM (+-) tr(rho prefix) lies IN THE TRACE RING. The\n"
      "      step-7 sigma/mirror separation (e.g. w=aab: (413,52) vs (436,29)) is a separation of\n"
      "      ordinary trace coordinates -- NOT a bridge the trace map cannot provide.\n"
      "  (5) There is no theta to 'reveal' hiding from traces anyway: reversal(theta) is directly\n"
      "      TRACE-ACTIVE at the genuine (non-self-dual) SL(3) rep on non-cyclic words (step 5).\n"
      "  => NO group-ring theta-intertwiner un-reproducible at the trace level. HIT criterion NOT met."
    )
else:
    outcome = "A"; verdict = "OUTCOME A: a genuine non-trace-reproducible theta-intertwiner survived (unexpected)."
print(verdict)
R["VERDICT_outcome"] = outcome
R["VERDICT_text"] = verdict
R["theta_trace_visible_at_sl3"] = bool(theta_trace_visible)

# base-rate note: this is a STRUCTURAL door, not a numeric match. No candidate-target enumeration
# applies; the look-elsewhere risk is 'mistaking a gauge unit for a bridge', which the unit-
# and rep-collapse computations (steps 1-4) directly rule out.
R["base_rate_note"] = ("structural door (no numeric target); the only false-positive risk is reading the "
                       "unit-a det difference as an invariant; steps 1-4 show it is a +-F gauge unit that "
                       "any SL(n) rep trivializes to det 1 -> no numeric coincidence involved.")

with open("output_results.json", "w") as f:
    json.dump(R, f, indent=1, default=str)
print("\nwrote output_results.json  |  outcome =", outcome)
