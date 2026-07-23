#!/usr/bin/env python3
"""
W3-119r -- L80(b) NON-VACUOUS colored theater at E6 level 1 + (d) Meyerhoff carry.

CARRY / DEFECT BEING FIXED
--------------------------
Wave-2 cell W2-119 part (b) built the E6-level-1 pointed (abelian, Z_3) theater
and ran the Turaev enhanced-Yang-Baxter braid-closure pipeline with N=1,
mu=[[1]].  It reported J_a(4_1)=J_a(3_1)=J_a(unknot)=1.  That is a TAUTOLOGY:
for a single-colored knot the braid scalar is c(a,a)^{writhe} and the canonical
framing correction is theta_a^{-writhe} with theta_a = c(a,a); the two cancel
for ANY value of the braiding scalar.  Substituting a FREE symbol s for the
E6-derived twist c(a,a) STILL yields 1 -- the E6 datum never enters the answer.
Self-tested below in part (b3, SELF-TEST 0): free symbol -> 1 identically.

THE FIX (non-vacuous theater where the E6 twist genuinely enters)
-----------------------------------------------------------------
The vacuity is a *knot* phenomenon, not a machinery phenomenon: in ANY pointed
(all-invertible) braided category the framing-corrected invariant of a one-
component link is 1 by a theorem, because there are no distinct-color crossings.
The E6-level-1 twist enters as soon as there is more than one component, through
the MONODROMY (double-braiding) charge b(a,b)=c(a,b)c(b,a).  So we build the
colored-LINK theater:

  b3.NEW  A genuine colored braid-closure computation on LINKS in the E6 level-1
          pointed Z_3 category (colors 27=1, 27bar=2).  Strands carry component
          colors; sigma_i multiplies by the braiding scalar c(color_i,color_{i+1})
          and permutes the colors; the closure scalar is read off exactly.
          - Hopf(a,b) = closure(sigma_1^2): J = b(a,b) = omega^{ab}  (NOT 1).
          - (2,2k) torus links = closure(sigma_1^{2k}): J = b(a,b)^k.
          NON-VACUITY SELF-TEST 1: replace the braiding scalar by FREE symbols
          -> the Hopf answer is a non-constant function of them (d/ds != 0), so
          the E6 value genuinely determines the result (unlike the knot).
          VALIDATION against independently-built modular data: the normalized
          Hopf link value equals S_{ab}/S_{00} for the E6-level-1 S-matrix that
          we construct from the quadratic form and verify is unitary, symmetric,
          S^2 = charge conjugation, and (ST)^3 = e^{2 pi i c/8} S^2 (Vafa).
          THEN we report the E6 result honestly: the colored 4_1 KNOT value is 1
          (pointed-category theorem, vacuity BOUNDED to one component), while the
          E6 monodromy charges omega^{ab} are the non-trivial content the twist
          delivers on every multi-component diagram.

  b2 (kept)  Nonabelian control: the SAME generic pipeline reproduces the Jones
             polynomials of 3_1 and 4_1 via U_q(sl2) -- proving the machinery is
             not blind and can output non-trivial colored values.

Part (d) (kept from wave 2, was fine): 4_1(5,1) vs 4_1(-5,1) -- oriented mirror
pair via orientation-sensitive Chern-Simons + is_amphicheiral, two seeds.

Env: pyenv python3 (snappy + sympy). Re-runnable end-to-end.  Gate-5 structural
language only; no SM values; nothing to CLAIMS.
"""

import sympy as sp

LOG = []


def log(*args):
    s = " ".join(str(a) for a in args)
    LOG.append(s)
    print(s)


csimp = lambda e: sp.simplify(sp.expand_complex(e))


# =====================================================================
# Part b0 -- E6 level-1 theater data from first principles (exact)
# =====================================================================
log("=" * 72)
log("PART (b0): E6 level-1 modular data derived in-cell (sympy exact)")
log("=" * 72)

A = sp.Matrix([
    [2, 0, -1, 0, 0, 0],
    [0, 2, 0, -1, 0, 0],
    [-1, 0, 2, -1, 0, 0],
    [0, -1, -1, 2, -1, 0],
    [0, 0, 0, -1, 2, -1],
    [0, 0, 0, 0, -1, 2],
])
assert A == A.T
rank = 6
simple = [tuple(1 if j == i else 0 for j in range(rank)) for i in range(rank)]


def inner(a, b):
    return sum(A[i, j] * a[i] * b[j] for i in range(rank) for j in range(rank))


roots = set(simple)
frontier_set = set(simple)
while frontier_set:
    new = set()
    for r in frontier_set:
        for i, al in enumerate(simple):
            n = inner(r, al)
            cand = tuple(r[j] + al[j] for j in range(rank))
            p = 0
            cur = r
            while True:
                cur2 = tuple(cur[j] - al[j] for j in range(rank))
                if cur2 in roots or cur2 == tuple(0 for _ in range(rank)):
                    if cur2 == tuple(0 for _ in range(rank)):
                        break
                    cur = cur2
                    p += 1
                else:
                    break
            if p - n > 0 and cand not in roots:
                new.add(cand)
    roots |= new
    frontier_set = new

pos_roots = sorted(roots, key=lambda r: (sum(r), r))
n_pos = len(pos_roots)
dim_g = 2 * n_pos + rank
log(f"positive roots: {n_pos}   dim g = {dim_g}")
assert n_pos == 36 and dim_g == 78, "E6 root count failed"

highest = max(pos_roots, key=lambda r: sum(r))
h_vee = sum(highest) + 1
log(f"h^vee(E6) = {h_vee}")
assert h_vee == 12

comarks = list(highest)
level1_nodes = [i + 1 for i, c in enumerate(comarks) if c == 1]
n_primaries_level1 = 1 + len(level1_nodes)
log(f"comark-1 nodes -> primaries omega_{level1_nodes}; # level-1 primaries = {n_primaries_level1}")
assert n_primaries_level1 == 3, "E6 level 1 should have 3 primaries (Z3)"

F = A.inv()
k = 1
denom = 2 * (k + h_vee)  # 26
rho = sp.ones(rank, 1)


def conf_weight(lam_omega_coords):
    lam = sp.Matrix(lam_omega_coords)
    return sp.nsimplify((lam.T * F * (lam + 2 * rho))[0, 0] / denom)


h27 = conf_weight([1, 0, 0, 0, 0, 0])
h27b = conf_weight([0, 0, 0, 0, 0, 1])
log(f"h(27) = {h27}   h(27bar) = {h27b}")
assert h27 == sp.Rational(2, 3) and h27b == sp.Rational(2, 3)

c_central = sp.Rational(k * dim_g, k + h_vee)
log(f"central charge c = {c_central}")
assert c_central == 6

# Pointed MTC on Z3 from the quadratic form q(g) = e^{2 pi i (2/3) g^2}.
w = sp.exp(2 * sp.pi * sp.I / 3)  # omega
theta = {g: sp.exp(2 * sp.pi * sp.I * sp.Rational(2, 3) * g * g) for g in range(3)}
for g in range(3):
    log(f"twist theta_{g} = {csimp(theta[g])}")
assert csimp(theta[1] - w**2) == 0 and csimp(theta[2] - w**2) == 0

gauss = csimp(sum(theta.values()) / sp.sqrt(3))
target = sp.exp(2 * sp.pi * sp.I * c_central / 8)
log(f"Gauss sum (1/sqrt3) sum theta_g = {gauss};  e^(2 pi i c/8) = {csimp(target)}")
assert csimp(gauss - target) == 0, "Gauss-sum / central-charge check failed"
log("[PASS] Gauss sum = e^{2 pi i c/8} = -i  -> pointed Z3 model IS the E6 lvl-1 MTC data.")


# -- braiding scalar and monodromy (the E6-derived key quantities) --
def cbraid(a, b):
    """braiding scalar c_{a,b} of the pointed Z3 category; c(a,a)=theta_a."""
    return w ** ((2 * a * b) % 3)


def bmono(a, b):
    """double-braiding / monodromy charge b(a,b) = c(a,b) c(b,a) = q(a+b)/q(a)q(b)."""
    return csimp(cbraid(a, b) * cbraid(b, a))


# ribbon + quadratic-form consistency, exact
for g in range(3):
    assert csimp(cbraid(g, g) - theta[g]) == 0
    for h in range(3):
        assert csimp(bmono(g, h) - csimp(theta[(g + h) % 3] / (theta[g] * theta[h]))) == 0
log("[PASS] c(a,a)=theta_a and b(a,b)=q(a+b)/q(a)q(b) hold exactly on Z3.")

# -- E6 level-1 modular S and T, verified (independent reference data) --
S = sp.Matrix(3, 3, lambda a, b: w ** ((-a * b) % 3) / sp.sqrt(3))
Tmat = sp.diag(*[csimp(theta[g] * sp.exp(-2 * sp.pi * sp.I * c_central / 24)) for g in range(3)])
C = sp.Matrix(3, 3, lambda a, b: 1 if (a + b) % 3 == 0 else 0)  # charge conjugation
assert csimp(sp.Matrix(S - S.T)) == sp.zeros(3, 3), "S not symmetric"
assert csimp(sp.Matrix(S * S.conjugate().T - sp.eye(3))) == sp.zeros(3, 3), "S not unitary"
assert csimp(sp.Matrix(S * S - C)) == sp.zeros(3, 3), "S^2 != charge conjugation"
# With T carrying the e^{-2 pi i c/24} phase, T is the genuine SL(2,Z) rep and
# (ST)^3 = S^2 exactly; the e^{2 pi i c/8} anomaly is the Gauss sum (checked b0).
ST3 = csimp(sp.Matrix((S * Tmat) ** 3))
assert csimp(sp.Matrix(ST3 - S * S)) == sp.zeros(3, 3), "(ST)^3 != S^2 for normalized T"
Ttilde = sp.diag(*[theta[g] for g in range(3)])
anom = csimp(((S * Ttilde) ** 3)[0, 0] / (S * S)[0, 0])
assert csimp(anom - sp.exp(2 * sp.pi * sp.I * c_central / 8)) == 0, "un-normalized anomaly wrong"
log("[PASS] modular data: S symmetric+unitary, S^2 = charge-conj, (ST)^3 = S^2 (normalized T);")
log(f"       un-normalized (S Ttilde)^3 anomaly = {anom} = e^(2 pi i c/8) (Vafa).")
log(f"       S_{{a,b}} = omega^{{-ab}}/sqrt3 ; normalized Hopf reference S_ab/S_00 = omega^{{-ab}}.")


# =====================================================================
# Part b1 -- generic braid-closure pipeline (Turaev enhanced YB, matrix form)
# =====================================================================
log("")
log("=" * 72)
log("PART (b1): generic matrix braid-closure pipeline (used by the b2 control)")
log("=" * 72)


def kron(*mats):
    out = mats[0]
    for m in mats[1:]:
        out = sp.Matrix(sp.kronecker_product(out, m))
    return out


def braid_rep(R, Rinv, N, n_strands, word):
    dim = N ** n_strands
    out = sp.eye(dim)
    for s in word:
        i = abs(s)
        Rm = R if s > 0 else Rinv
        M = kron(sp.eye(N ** (i - 1)), Rm, sp.eye(N ** (n_strands - i - 1)))
        out = M * out
    return out


def partial_trace_last(M, N, n_strands):
    d = N ** (n_strands - 1)
    out = sp.zeros(d, d)
    for a in range(d):
        for b in range(d):
            out[a, b] = sum(M[a * N + s, b * N + s] for s in range(N))
    return out


def closure_invariant(R, Rinv, mu, a_mark, N, n_strands, word, simplifier=sp.simplify):
    wri = sum(1 if s > 0 else -1 for s in word)
    rho = braid_rep(R, Rinv, N, n_strands, word)
    mun = kron(*([mu] * n_strands)) if n_strands > 1 else mu
    tr = (mun * rho).trace()
    return simplifier(a_mark ** (-wri) * tr / mu.trace())


def verify_eyb(R, Rinv, mu, N, tag, simplifier=sp.simplify):
    I_N = sp.eye(N)
    assert simplifier(R * Rinv - sp.eye(N * N)) == sp.zeros(N * N, N * N)
    R12 = kron(R, I_N)
    R23 = kron(I_N, R)
    assert simplifier(R12 * R23 * R12 - R23 * R12 * R23) == sp.zeros(N ** 3, N ** 3), f"YBE fails [{tag}]"
    mumu = kron(mu, mu)
    assert simplifier(R * mumu - mumu * R) == sp.zeros(N * N, N * N), f"[R,mu x mu] != 0 [{tag}]"
    Mp = partial_trace_last(kron(I_N, mu) * R, N, 2)
    Mm = partial_trace_last(kron(I_N, mu) * Rinv, N, 2)
    a_val = simplifier(Mp[0, 0])
    assert simplifier(Mp - a_val * I_N) == sp.zeros(N, N), f"Markov(+) fails [{tag}]"
    assert simplifier(Mm - I_N / a_val) == sp.zeros(N, N), f"Markov(-) fails [{tag}]"
    log(f"[PASS] ({tag}) YBE + invertibility + [R,mu x mu]=0 + Markov(+/-) exact; a = {a_val}")
    return a_val


WORD_UNKNOT_B2 = [1]
WORD_TREFOIL = [1, 1, 1]
WORD_FIG8 = [1, -2, 1, -2]


# =====================================================================
# Part b2 -- NONABELIAN CONTROL: Jones via U_q(sl2) (pipeline is not blind)
# =====================================================================
log("")
log("=" * 72)
log("PART (b2): nonabelian control -- pipeline reproduces Jones(3_1), Jones(4_1)")
log("=" * 72)

q = sp.symbols('q', positive=True)
Rh = sp.Matrix([[q, 0, 0, 0], [0, q - 1 / q, 1, 0], [0, 1, 0, 0], [0, 0, 0, q]])
Rh_inv = Rh.inv()
x, y, av = sp.symbols('x y a_mark')
mu_gen = sp.diag(x, y)
Mp = partial_trace_last(kron(sp.eye(2), mu_gen) * Rh, 2, 2)
Mm = partial_trace_last(kron(sp.eye(2), mu_gen) * Rh_inv, 2, 2)
eqs = [sp.Eq(Mp[0, 0], av), sp.Eq(Mp[1, 1], av), sp.Eq(Mp[0, 1], 0), sp.Eq(Mp[1, 0], 0),
       sp.Eq(Mm[0, 0], 1 / av), sp.Eq(Mm[1, 1], 1 / av), sp.Eq(x + y, q + 1 / q)]
sols = sp.solve(eqs, [x, y, av], dict=True)
assert sols, "no enhancement mu exists"
sol = sols[0]
mu2 = sp.diag(sol[x], sol[y])
a2 = sol[av]
verify_eyb(Rh, Rh_inv, mu2, 2, "U_q(sl2) fund", simplifier=lambda e: sp.simplify(sp.expand(e)))
simp = lambda e: sp.simplify(sp.expand(sp.cancel(e)))
J_unknot = closure_invariant(Rh, Rh_inv, mu2, a2, 2, 2, WORD_UNKNOT_B2, simp)
J_tref = closure_invariant(Rh, Rh_inv, mu2, a2, 2, 2, WORD_TREFOIL, simp)
J_fig8 = closure_invariant(Rh, Rh_inv, mu2, a2, 2, 3, WORD_FIG8, simp)
log(f"J(unknot)  = {J_unknot}")
log(f"J(trefoil) = {sp.expand(J_tref)}")
log(f"J(4_1)     = {sp.expand(J_fig8)}")
t = sp.symbols('t')
V_tref_L = -t**-4 + t**-3 + t**-1
V_tref_R = V_tref_L.subs(t, 1 / t)
V_fig8 = t**-2 - t**-1 + 1 - t + t**2
assert simp(J_unknot - 1) == 0
match_tref = any(
    simp(J_tref - Vv.subs(t, sub)) == 0
    for Vv in (V_tref_L, V_tref_R) for sub in (q**2, q**-2))
assert match_tref, "trefoil does not match Jones"
ok8 = any(simp(J_fig8 - V_fig8.subs(t, sub)) == 0 for sub in (q**2, q**-2))
assert ok8, "4_1 does not match Jones(4_1)"
diff_at_unknot = simp(J_fig8 - 1)
assert diff_at_unknot != 0
log(f"[PASS] pipeline = Jones for 3_1 and 4_1; J(4_1)-1 = {sp.factor(diff_at_unknot)} != 0 (not blind).")


# =====================================================================
# Part b3 -- NON-VACUOUS colored theater at E6 level 1 (LINKS)
# =====================================================================
log("")
log("=" * 72)
log("PART (b3): the NON-VACUOUS E6-level-1 colored theater (colored LINKS)")
log("=" * 72)


def colored_closure_scalar(word, comp_colors, strand_of, cfun):
    """Exact braid-closure scalar for a colored braid whose closure is a link.
    word: signed generators (+i = sigma_i, -i = sigma_i^{-1}), 1-indexed.
    comp_colors: {component -> color}.  strand_of: list, strand position -> component
                 (the coloring of the initial strands, top of the braid).
    cfun(a,b): braiding scalar for over-color a, under-color b.
    Returns (scalar, self_writhe_per_component, inter_crossing_signed_sum)."""
    colors = [comp_colors[strand_of[i]] for i in range(len(strand_of))]
    comps = [strand_of[i] for i in range(len(strand_of))]
    scalar = sp.Integer(1)
    self_w = {cpt: 0 for cpt in comp_colors}
    inter = 0
    for gen in word:
        i = abs(gen) - 1  # positions i, i+1
        a, b = colors[i], colors[i + 1]
        ca, cb = comps[i], comps[i + 1]
        if gen > 0:
            scalar *= cfun(a, b)
            if ca == cb:
                self_w[ca] += 1
            else:
                inter += 1
        else:
            scalar *= 1 / cfun(colors[i + 1], colors[i])
            if ca == cb:
                self_w[ca] -= 1
            else:
                inter -= 1
        colors[i], colors[i + 1] = colors[i + 1], colors[i]
        comps[i], comps[i + 1] = comps[i + 1], comps[i]
    # closure must restore the strand coloring (well-defined colored link)
    final = [comp_colors[comps[i]] for i in range(len(comps))]
    assert final == [comp_colors[strand_of[i]] for i in range(len(strand_of))], \
        "closure does not restore colors -- ill-posed colored diagram"
    return scalar, self_w, inter


def framing_corrected(word, comp_colors, strand_of, cfun, thetafun):
    """ambient-isotopy invariant = raw closure scalar / prod theta_g^{self-writhe_g}."""
    raw, self_w, inter = colored_closure_scalar(word, comp_colors, strand_of, cfun)
    corr = sp.Integer(1)
    for cpt, wself in self_w.items():
        corr *= thetafun(comp_colors[cpt]) ** wself
    return csimp(raw / corr), self_w, inter


thetafun = lambda a: theta[a]

# ---- SELF-TEST 0: reproduce the DEFECT (knot => vacuous) ----
log("")
log("-- SELF-TEST 0: the wave-2 defect reproduced (KNOT => free symbol gives 1) --")
s = sp.symbols('s')                      # free stand-in for the braiding scalar c(a,a)
free_knot_cfun = lambda a, b: s          # a totally free key quantity
free_theta = lambda a: s                 # ribbon/framing tied to that same free scalar
for word, kn in [(WORD_TREFOIL, "3_1"), (WORD_FIG8, "4_1")]:
    val, _, _ = framing_corrected(word, {0: 1}, [0] * (max(abs(g) for g in word) + 1),
                                  free_knot_cfun, free_theta)
    log(f"   free-symbol J({kn}) = {sp.simplify(val)}   (independent of s: VACUOUS -- this is the defect)")
    assert sp.simplify(val - 1) == 0, "expected the knot to be identically 1 (the vacuity)"
log("   => confirmed: for ONE component the theater is vacuous for ANY braiding scalar.")

# ---- the E6 colored LINK invariants (twist genuinely enters) ----
log("")
log("-- E6 level-1 colored LINK invariants (colors 27=1, 27bar=2) --")
# Hopf link = closure(sigma_1^2) in B2: 2 components, inter-crossings only.
HOPF_R = [1, 1]      # right-handed
HOPF_L = [-1, -1]    # left-handed
TORUS4 = [1, 1, 1, 1]  # (2,4) torus link, lk=2
link_results = {}
color_pairs = [(1, 1), (1, 2), (2, 2)]
for (a, b) in color_pairs:
    cc = {0: a, 1: b}
    strand = [0, 1]
    JR, sw, inter = framing_corrected(HOPF_R, cc, strand, cbraid, thetafun)
    JL, _, _ = framing_corrected(HOPF_L, cc, strand, cbraid, thetafun)
    lk = inter // 2
    # reference from modular data: normalized Hopf(a,b) = S_ab/S_00 = omega^{-ab}
    ref = csimp(S[a, b] / S[0, 0])
    assert all(v == 0 for v in sw.values()), "unexpected self-framing on the Hopf link"
    assert lk == 1
    # right/left Hopf are complex conjugates; one of them equals the S-matrix ref
    match = (csimp(JR - ref) == 0) or (csimp(JL - ref) == 0)
    assert csimp(JR - bmono(a, b)) == 0, "right Hopf != monodromy b(a,b)"
    assert csimp(JL - csimp(1 / bmono(a, b))) == 0, "left Hopf != b(a,b)^{-1}"
    assert match, f"neither Hopf chirality matches S_ab/S_00 for ({a},{b})"
    log(f"   Hopf(27^{a},27^{b}): J_right = {JR} = b({a},{b}) ; J_left = {JL} ; "
        f"S_{a}{b}/S_00 = {ref}  [match={match}]")
    link_results[(a, b)] = (JR, JL, ref)

# a torus (2,4) link to show the twist enters with the right power b(a,b)^{lk}
Jt4, sw4, inter4 = framing_corrected(TORUS4, {0: 1, 1: 2}, [0, 1], cbraid, thetafun)
assert all(v == 0 for v in sw4.values()) and inter4 // 2 == 2
assert csimp(Jt4 - bmono(1, 2) ** 2) == 0
log(f"   (2,4)-torus link (27,27bar): J = {Jt4} = b(1,2)^2  (lk=2 -> monodromy squared)")

# at least one colored link value is NOT 1 -> the theater speaks
nontrivial = [k for k, (JR, JL, ref) in link_results.items() if csimp(JR - 1) != 0]
assert nontrivial, "all colored link values are 1 -- still vacuous!"
log(f"   NON-TRIVIAL colored link values at color pairs {nontrivial} (J != 1).")

# ---- SELF-TEST 1: LINK non-vacuity (free symbol => answer MOVES) ----
log("")
log("-- SELF-TEST 1: the SAME machinery on the Hopf link is NON-VACUOUS --")
s12, s21 = sp.symbols('s12 s21')
free_link_cfun = lambda a, b: {(1, 2): s12, (2, 1): s21}.get((a, b), sp.Integer(1))
# no self-crossings on the Hopf link, so framing correction is trivial here
Jfree, _, _ = framing_corrected(HOPF_R, {0: 1, 1: 2}, [0, 1], free_link_cfun,
                                lambda a: sp.Integer(1))
log(f"   free-symbol Hopf(27,27bar) = {Jfree}  (= s12*s21, the raw braiding product)")
# NON-CONSTANCY, proven by three distinct braiding-scalar inputs -> three distinct
# outputs (a constant/vacuous invariant would give the same output for all inputs):
probes = {"E6 twist": (cbraid(1, 2), cbraid(2, 1)),
          "trivial braiding": (sp.Integer(1), sp.Integer(1)),
          "arbitrary (2,3)": (sp.Integer(2), sp.Integer(3))}
outs = {name: csimp(Jfree.subs({s12: v12, s21: v21})) for name, (v12, v21) in probes.items()}
for name, val in outs.items():
    log(f"     input {name:18s} -> {val}")
distinct = len({sp.nsimplify(v, [sp.sqrt(3)]) for v in outs.values()}) == len(outs)
assert distinct, "free-symbol Hopf gives the SAME output for distinct inputs -- vacuous"
val_at_E6 = outs["E6 twist"]
val_at_one = outs["trivial braiding"]
assert csimp(val_at_E6 - bmono(1, 2)) == 0, "E6 substitution must recover monodromy b(1,2)"
assert csimp(val_at_E6 - val_at_one) != 0, "E6 twist does not change the answer -- vacuous"
d12 = d21 = 1  # sentinel: non-constancy established by the distinct-outputs test above
log(f"   three distinct inputs -> three distinct outputs (NON-CONSTANT in the key quantity);")
log(f"   substitute E6 twist -> {val_at_E6} ;  substitute trivial braiding -> {val_at_one} ;  DISTINCT")
log("   => the E6-level-1 twist GENUINELY ENTERS the colored link answer (NON-VACUOUS).")

# ---- honest report of the E6 knot result, with the vacuity BOUNDED ----
log("")
log("-- the colored 4_1 KNOT value, with vacuity honestly bounded --")
J41_E6, _, _ = framing_corrected(WORD_FIG8, {0: 1}, [0, 0, 0], cbraid, thetafun)
J41_E6b, _, _ = framing_corrected(WORD_FIG8, {0: 2}, [0, 0, 0], cbraid, thetafun)
assert J41_E6 == 1 and J41_E6b == 1
log(f"   J_27(4_1) = {J41_E6},  J_27bar(4_1) = {J41_E6b}  (= 1, the pointed-category theorem)")
log("[COMPUTED FACT -- part (b)] In the E6 level-1 pointed Z3 theater the colored")
log("  4_1 KNOT invariant is 1 -- but this is now a BOUNDED statement: it is the")
log("  one-component pointed-category theorem, NOT machinery blindness. The SAME")
log("  colored theater is NON-VACUOUS -- the E6 twist enters through the monodromy")
log("  charges b(a,b)=omega^{ab}, giving J(Hopf; 27,27)=omega, J(Hopf; 27,27bar)=")
log("  omega^2, J((2,4)-torus;27,27bar)=omega, all reproducing the E6-level-1")
log("  modular S-matrix (S_ab/S_00) that we built and verified independently, and")
log("  all MOVING under a free-symbol substitution (self-test 1). B580 Q1's cited")
log("  colored-blindness is thus computed AND correctly located: it lives on knots,")
log("  the object's twist speaks on every multi-component diagram.")


# =====================================================================
# Part d -- the +-5 Meyerhoff filling (kept: was fine in wave 2)
# =====================================================================
log("")
log("=" * 72)
log("PART (d): 4_1(5,1) vs 4_1(-5,1)  (SnapPy, orientation-sensitive)")
log("=" * 72)

import snappy

M1 = snappy.Manifold("m004")
cs_cusped = M1.chern_simons()
M1.dehn_fill((5, 1))
M2 = snappy.Manifold("m004")
M2.chern_simons()
M2.dehn_fill((-5, 1))
log(f"m004 cusped CS = {cs_cusped} (~0)")
log(f"M1 = m004(5,1):  {M1.solution_type()}, vol = {M1.volume()}")
log(f"M2 = m004(-5,1): {M2.solution_type()}, vol = {M2.volume()}")
log(f"identify(M1) = {M1.identify()};  identify(M2) = {M2.identify()}")
cs1 = M1.chern_simons()
cs2 = M2.chern_simons()
log(f"CS(M1) = {cs1};  CS(M2) = {cs2}")
iso_unoriented = M1.is_isometric_to(M2)
log(f"is_isometric_to(M1,M2) [orientation-insensitive] = {iso_unoriented}")
sg1 = M1.symmetry_group()
sg2 = M2.symmetry_group()
log(f"symmetry_group(M1) = {sg1}, is_amphicheiral = {sg1.is_amphicheiral()}")
log(f"symmetry_group(M2) = {sg2}, is_amphicheiral = {sg2.is_amphicheiral()}")

H1 = snappy.ManifoldHP("m004")
H1.chern_simons()
H1.dehn_fill((5, 1))
H2 = snappy.ManifoldHP("m004")
H2.chern_simons()
H2.dehn_fill((-5, 1))
cs1_hp = H1.chern_simons()
cs2_hp = H2.chern_simons()
log(f"[seed 2 HP] CS(M1) = {cs1_hp}")
log(f"[seed 2 HP] CS(M2) = {cs2_hp}")

amphi_votes = []
for trial in range(2):
    Mr = snappy.Manifold("m004")
    Mr.dehn_fill((5, 1))
    Mr.randomize()
    sgr = Mr.symmetry_group()
    amphi_votes.append(sgr.is_amphicheiral())
    log(f"[seed 2 rand #{trial}] symmetry_group = {sgr}, is_amphicheiral = {sgr.is_amphicheiral()}")

cs_diff_seeds = abs(float(cs1) - float(cs1_hp))
log(f"CS(M1) double-vs-HP |diff| = {cs_diff_seeds:.3e}")
assert cs_diff_seeds < 1e-10, "seed disagreement in CS"
sum_cs = float(cs1_hp) + float(cs2_hp)
log(f"CS(M1) + CS(M2) = {sum_cs:.3e}")


def dist_mod(x, m):
    r = x % m
    return min(r, m - r)


d_half = dist_mod(float(cs1_hp) - float(cs2_hp), 0.5)
log(f"|CS(M1)-CS(M2)| mod 1/2 = {d_half:.12f}  (need 0 for orientation-preserving isometry)")

chiral = (d_half > 1e-9) and (not sg1.is_amphicheiral()) and (not sg2.is_amphicheiral()) \
         and (not any(amphi_votes))
consistent_unoriented = bool(iso_unoriented)
if chiral and consistent_unoriented and abs(sum_cs) < 1e-9:
    VERDICT_D = "ORIENTED-MIRROR-PAIR"
    log("[COMPUTED FACT -- part (d)] ORIENTED MIRROR PAIR: CS(M1) = -CS(M2), distinct")
    log("  mod 1/2, is_amphicheiral False (both fillings, original + randomized), and")
    log("  is_isometric_to True -- same unoriented manifold, opposite orientations.")
elif (not chiral):
    VERDICT_D = "UNRESOLVED"
    log("[UNRESOLVED -- part (d)] orientation-sensitive checks disagree.")
else:
    VERDICT_D = "AMPHICHIRAL" if sg1.is_amphicheiral() else "UNRESOLVED"
    log(f"[part (d)] verdict: {VERDICT_D}")


# =====================================================================
# Cell verdict logic (must be able to emit UNRESOLVED)
# =====================================================================
log("")
log("=" * 72)
b_nonvacuous = (len(nontrivial) > 0) and distinct and \
    (csimp(val_at_E6 - val_at_one) != 0)
d_ok = (VERDICT_D == "ORIENTED-MIRROR-PAIR")
log("CELL VERDICT INPUTS:")
log(f"  (b) non-vacuous colored theater : {b_nonvacuous}  "
    f"(link J!=1, free-symbol MOVES, E6 twist enters)")
log(f"  (d) Meyerhoff oriented mirror   : {d_ok}  ({VERDICT_D})")
if b_nonvacuous and d_ok:
    CELL = "RESOLVED-A"
elif b_nonvacuous or d_ok:
    CELL = "RESOLVED-B"
else:
    CELL = "UNRESOLVED"
log(f"CELL VERDICT: {CELL}")
log("=" * 72)

with open(__file__.replace("compute.py", "output.txt"), "w") as f:
    f.write("\n".join(LOG) + "\n")
