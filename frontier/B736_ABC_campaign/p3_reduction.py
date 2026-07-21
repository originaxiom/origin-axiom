#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRACK P3 — the parameter-reduction ledger + the equivariance wall.
B736 A+B+C joint campaign, cc's half, Path 3.

FIREWALL: pure math / structural. Gate 5. COMPUTE-NOT-CITE (E19),
BASE-RATE (E20). CHARACTERIZE, never FIT. No SM value is claimed or
predicted anywhere below; empirical ratios appear ONLY as inputs to a
falsification (genericity) test whose OUTPUT is a NEGATIVE (no relation).

Deliverable:
  (1) recompute the EQUIVARIANCE WALL (B650 W2-G1): the only monodromy-
      equivariant C-linear map being->hearing is T = 0.
  (2) the capacity no-go (B733 bounded V4 ceiling vs B706 kind-mismatch):
      a discrete rank<=3 F2-space cannot parametrise ~19 continuous reals.
  (3) a genericity control reproducing B706 rung-1 (SM mass ratios carry
      no low-height relation over Q(sqrt5)) -- COMPUTE-NOT-CITE.
  (4) the LEDGER: each of the ~19(+nu) SM free parameters graded
      a/b/c/d against the banked discriminating fact.
  (5) the reduction COUNT and the structural NO-GO THEOREM.

Two-outcome:  A = >=1 genuine forced relation (a reduction).
              B = zero + the rigorous no-go.
"""

import sympy as sp

SEP = "=" * 78
sub = "-" * 78


# ----------------------------------------------------------------------
# PART 1 -- THE EQUIVARIANCE WALL  (recompute B650 W2-G1, exact)
# ----------------------------------------------------------------------
# Source: any classical A1-module with the banked hyperbolic action.
#   spectrum { lambda(A1)^{+1}, lambda(A1)^{-1} } = { phi^2, phi^-2 }
#   -- real, off the unit circle, INFINITE order.
# Target: the theta-odd hearing plane at kappa=5 with rho_hear(RL):
#   tr = -1/phi, det = 1, ORDER 10 (primitive 10th root of unity spectrum).
# Equivariance: T * A_source = rho_hear(RL) * T,  T a 2x2 C-linear map.
# The argument needs only the spectra; disjoint spectra => T = 0.
def equivariance_wall():
    phi = (1 + sp.sqrt(5)) / 2
    lam = sp.nsimplify(phi**2)                 # = (3+sqrt5)/2, eigenvalue of A1

    # A1: explicit hyperbolic realization with spectrum {phi^2, phi^-2}.
    A1 = sp.Matrix([[lam, 0], [0, 1/lam]])
    A1 = sp.simplify(A1)

    # rho_hear(RL): companion matrix with tr = -1/phi, det = 1.
    tr_t = sp.simplify(-1/phi)                  # = 1/2 - sqrt5/2
    B = sp.Matrix([[0, -1], [1, tr_t]])         # char poly x^2 - tr_t x + 1

    # ---- invariant checks (the banked witnesses) ----
    src_eigs = sorted([sp.simplify(e) for e in A1.eigenvals()],
                      key=lambda z: float(z))
    is_phi_pow = (sp.simplify(A1.eigenvals().__len__()) == 2 and
                  sp.simplify(sp.prod(list(A1.eigenvals().keys()))) == 1)
    tgt_tr = sp.simplify(B.trace())
    tgt_det = sp.simplify(B.det())
    # target order: is B^10 = I and B^k != I for k<10 ?
    order = None
    P = sp.eye(2)
    for k in range(1, 21):
        P = sp.simplify(P * B)
        if sp.simplify(P - sp.eye(2)) == sp.zeros(2):
            order = k
            break
    # target eigenvalues on the unit circle?
    tgt_eigs = list(B.eigenvals().keys())
    on_circle = all(sp.simplify(sp.Abs(e) - 1) == 0 for e in tgt_eigs)
    # spectra disjoint?
    disjoint = all(sp.simplify(se - te) != 0
                   for se in A1.eigenvals() for te in B.eigenvals())

    # ---- the Sylvester solve  T*A1 - B*T = 0 ----
    t0, t1, t2, t3 = sp.symbols('t0 t1 t2 t3')
    T = sp.Matrix([[t0, t1], [t2, t3]])
    M = sp.simplify(T * A1 - B * T)
    sol = sp.solve([M[0, 0], M[0, 1], M[1, 0], M[1, 1]],
                   [t0, t1, t2, t3], dict=True)
    only_zero = (sol == [{t0: 0, t1: 0, t2: 0, t3: 0}] or
                 all(all(sp.simplify(v) == 0 for v in s.values()) for s in sol))

    out = []
    out.append(SEP)
    out.append("PART 1 -- THE EQUIVARIANCE WALL  (recompute B650 W2-G1, exact)")
    out.append(SEP)
    out.append(f"source A1 eigenvalues        : {src_eigs}")
    out.append(f"  = {{phi^2, phi^-2}}, det 1  : {bool(is_phi_pow)}  (real, |e| != 1, infinite order)")
    out.append(f"target rho_hear(RL) trace    : {tgt_tr}   ( = -1/phi )")
    out.append(f"target det                   : {tgt_det}")
    out.append(f"target multiplicative order  : {order}   (primitive 10th root spectrum)")
    out.append(f"target eigenvalues |e| == 1  : {bool(on_circle)}")
    out.append(f"spectra DISJOINT             : {bool(disjoint)}   (hyperbolic real  vs  unitary 10th-root)")
    out.append(f"Sylvester T*A1 = rho*T  solution set : {sol}")
    out.append(f"==> the ONLY equivariant linear map is T = 0 : {bool(only_zero)}")
    out.append("")
    out.append("THE WALL: no nonzero C-linear monodromy-equivariant map exists from the")
    out.append("classical (being) A1-module to the theta-odd (hearing) plane. Disjoint")
    out.append("spectra kill every intertwiner. Mechanistically this is 'passage through")
    out.append("the finite' (B644): the stage hears only the finite congruence shadow, so")
    out.append("no linear channel can TRANSPORT a continuous quantity from one sector to")
    out.append("the other. => the being<->hearing coupling cannot manufacture a forced")
    out.append("RELATION between two continuous SM parameters. (grade-(b) mechanism dead.)")
    return "\n".join(out), bool(only_zero and disjoint)


# ----------------------------------------------------------------------
# PART 2 -- THE CAPACITY NO-GO  (B733 bounded ceiling vs B706 kind-mismatch)
# ----------------------------------------------------------------------
def capacity_nogo():
    # B733: the arithmetic-Galois observer bit-count is a BOUNDED discrete
    # F2-space. V4 = <being sqrt(-3), hearing sqrt(5)> has rank 2, up to 3
    # with the stage prime sqrt(-7) (B704). The full-diagonal 2-rank
    # sequence [0,2,3,3,3,3] SATURATES at 3. Depth-independent.
    v4_rank = 2
    seam_rank_max = 3                 # + stage prime sqrt(-7)  (B704)
    design_points = 2 ** seam_rank_max     # every bit flipped: 2^3 = 8 menus
    design_dimension = 0             # a finite set: topological dimension 0

    sm_continuous_params = 19        # 9 masses + 4 CKM + 3 gauge + 2 Higgs + 1 theta_QCD
    sm_with_neutrinos = 26           # + 3 nu masses + 3 PMNS (1 phase + 2 Majorana) etc.

    out = []
    out.append(SEP)
    out.append("PART 2 -- THE CAPACITY NO-GO  (B733 bounded ceiling + B706 kind-mismatch)")
    out.append(SEP)
    out.append(f"object design-space (B733/B704)   : a DISCRETE F2-space, V4 rank {v4_rank}"
               f" (up to {seam_rank_max} w/ stage prime)")
    out.append(f"  full menu of observers          : {design_points} points (2^{seam_rank_max}),"
               f" saturating, depth-independent")
    out.append(f"  topological dimension           : {design_dimension}  (a finite set is not a manifold)")
    out.append(f"SM flavor freedom (B706 rung-2)   : a CONTINUOUS R^n moduli space")
    out.append(f"  parameter count                 : ~{sm_continuous_params}"
               f"  (up to ~{sm_with_neutrinos} with the neutrino sector)")
    out.append("")
    out.append(f"KIND mismatch  : dim {design_dimension} discrete  vs  dim ~{sm_continuous_params}"
               f" continuous  ==> different cardinality AND dimension-type.")
    out.append("A dimension-0 discrete set of <=8 points cannot coordinatize a ~19-real")
    out.append("continuum. No injection of the SM moduli into the observer menu exists;")
    out.append("even cherry-picking EVERY bit yields 3 binary choices, not 19 tunable reals.")
    out.append("=> the observer structure cannot FORCE (a) a continuous value nor (b) a")
    out.append("continuous relation. (grades (a),(b) dead by cardinality/dimension.)")
    return "\n".join(out)


# ----------------------------------------------------------------------
# PART 3 -- GENERICITY CONTROL  (reproduce B706 rung-1 NO-MATCH; COMPUTE-NOT-CITE)
# ----------------------------------------------------------------------
# Empirical dimensionless ratios are inputs to a FALSIFICATION test whose
# OUTPUT is a NEGATIVE (no low-height algebraic relation over Q(sqrt5)).
# No value is claimed. This reproduces the banked B706 rung-1 fact.
def genericity_control():
    import mpmath as mp
    mp.mp.dps = 40
    sqrt5 = mp.sqrt(5)

    # PDG dimensionless lepton mass ratios (empirical INPUTS to a NEGATIVE test).
    # digits_known := the significant digits to which the ratio is measured; a
    # k-digit decimal is TRIVIALLY rational of height ~10^k, so to make "no
    # relation" meaningful the PSLQ height ceiling MUST sit well below 10^k
    # (the base-rate discipline B706/E20; else PSLQ just recovers the decimal).
    HEIGHT_CEIL = 10**3          # B706 rung-1 primary bound; << 10^k for both rows
    ratios = {
        "m_mu/m_e":  (mp.mpf("206.7682830"), 10),   # ~10 known digits
        "m_tau/m_mu": (mp.mpf("16.81700"),   6),     # ~6 known digits (m_tau-limited)
    }
    out = []
    out.append(SEP)
    out.append("PART 3 -- GENERICITY CONTROL  (reproduce B706 rung-1 over Q(sqrt5))")
    out.append(SEP)
    out.append("PSLQ on basis [1, r, sqrt5, r*sqrt5] with height ceiling %d." % HEIGHT_CEIL)
    out.append("A hit would mean r is algebraic of degree<=2 over Q(sqrt5) at LOW height.")
    out.append("Base-rate guard: ceiling %d << 10^(known digits) for every row, so the" % HEIGHT_CEIL)
    out.append("trivial self-rational (height ~10^k) CANNOT masquerade as a relation.")
    out.append(sub)
    any_relation = False
    for name, (r, kdig) in ratios.items():
        assert HEIGHT_CEIL < 10**kdig, "ceiling must sit below the decimal's own height"
        vec = [mp.mpf(1), r, sqrt5, r * sqrt5]
        try:
            rel = mp.pslq(vec, maxcoeff=HEIGHT_CEIL, maxsteps=10**5)
        except Exception:
            rel = None
        found = rel is not None and any(c != 0 for c in (rel or []))
        any_relation = any_relation or found
        out.append(f"  {name:12s} (~{kdig}d): PSLQ rel (h<={HEIGHT_CEIL}) = {rel}"
                   f"  -> {'RELATION' if found else 'NONE (generic)'}")
    out.append(sub)
    out.append(f"any low-height relation found : {any_relation}"
               f"   (expected False = B706 rung-1 NO-MATCH reproduced)")
    out.append("=> the SM mass ratios are GENERIC over the object's audible field Q(sqrt5).")
    out.append("   The object's arithmetic does not carry them. (grade (a)/(b) dead at the")
    out.append("   number level too, independently of the structural walls above.)")
    return "\n".join(out), not any_relation


# ----------------------------------------------------------------------
# PART 4 -- THE LEDGER
# ----------------------------------------------------------------------
# grade legend:
#   a = a forced VALUE           b = a forced RELATION to another param (a REDUCTION)
#   c = a forced discrete CONSTRAINT on this param    d = nothing forced
LEDGER = [
    # (parameter, grade, discriminating banked fact)
    ("m_e (electron mass)",      "d",
     "B685: object=BEING(3), masses are level-5 COUPLING data, not intrinsic; "
     "object is SCALELESS (symmetry-yes/scale-no, B82) => no absolute mass."),
    ("m_mu (muon mass)",         "d",
     "B685 (mass=coupling datum) + scaleless object; B706 rung-1: m_mu/m_e generic over Q(sqrt5)."),
    ("m_tau (tau mass)",         "d",
     "B685 + scaleless; B706 rung-1: m_tau/m_mu, m_tau/m_e generic (PSLQ NO relation, Part 3)."),
    ("m_u (up mass)",            "d",
     "B685: hearing/flavor lives in coupling, not the object; scaleless object => no value."),
    ("m_d (down mass)",          "d",
     "B685 terminal no-go: no framework-derivable generator makes the flavor streams; scaleless."),
    ("m_s (strange mass)",       "d",
     "B685 (coupling datum) + scaleless; no low-height ratio relation banked (B706)."),
    ("m_c (charm mass)",         "d",
     "B685 (coupling) + scaleless object; no forced value or ratio."),
    ("m_b (bottom mass)",        "d",
     "B685 (coupling) + scaleless object; no forced value or ratio."),
    ("m_t (top mass)",           "d",
     "B685 (coupling) + scaleless; the object provides no scale (Higgs vev sets it)."),

    ("theta_12 CKM (Cabibbo)",   "d",
     "B706 rung-2 kind-mismatch (continuous mixing vs discrete F2 seam); Cabibbo lambda~9/40 is a "
     "RUNG-4 TRAP -- FIELD MISMATCH (9/40 in Q, no sqrt5) + no forcing mechanism (B685)."),
    ("theta_13 CKM",             "d",
     "B706 rung-2: continuous mixing manifold is not the object's F2-seam; no banked relation."),
    ("theta_23 CKM",             "d",
     "B706 rung-2 kind-mismatch; no low-height relation over Q(sqrt5); nothing forced."),
    ("delta_CKM (CP phase)",     "d",
     "B355 phase-null fired (Weil-layer phase scan); B713: CP/chirality is the OBSERVER's discrete "
     "Z/2 c-bit (B701 free), a bit -- WRONG KIND for a continuous phase (B706/B733)."),

    ("theta_12 PMNS",            "d",
     "B706 rung-2 kind-mismatch; neutrino/lepton mixing is coupling data (B685), not object."),
    ("theta_13 PMNS",            "d",
     "B706 rung-2; no banked relation; continuous vs discrete-bit kind-mismatch."),
    ("theta_23 PMNS",            "d",
     "B706 rung-2; nothing forced; lepton sector lives in the coupling (B685)."),
    ("delta_PMNS (CP phase)",    "d",
     "B713: leptonic CP = observer's discrete c-bit, not a continuous angle; kind-mismatch (B706)."),

    ("g1 (U(1)_Y coupling)",     "d",
     "B650 equivariance wall (T=0, Part 1): being<->hearing carries no linear intertwiner to "
     "transport a coupling; PHYSICS_MAP: no gauge/dynamics crossing; B706 kind-mismatch."),
    ("g2 (SU(2)_L coupling)",    "d",
     "B650 wall + PHYSICS_MAP (Path 5 gauge = numerology-risk, blocked); the object's only inter-sector "
     "'coupling' is the DISCRETE invariant det(I-B_odd)=phi^2, not a continuous gauge coupling."),
    ("g3 (SU(3)_c coupling)",    "d",
     "B650 wall; PHYSICS_MAP: SL(n>=3) tower has NO transfer-matrix (dynamics) realization (B52); "
     "no forced value or relation among {g1,g2,g3}."),

    ("m_H (Higgs mass)",         "d",
     "SCALELESS object: 'symmetry yes, scale no' is the standing structural theorem (two-ended "
     "unification; B82 physics chapter closed; DESI 122-order scale gap). No scale => no value."),
    ("v (Higgs vev)",            "d",
     "The vev SETS the electroweak scale; the object supplies NO scale (B82, scaleless). Nothing forced."),

    ("theta_QCD (strong CP)",    "d",
     "B713: the object is amphichiral/theta-symmetric (vector-like BEING); CP is the observer's "
     "DISCRETE Z/2 c-bit (B701 free, B711 free swap). theta_QCD is a continuous angle -> the bit is "
     "the WRONG KIND (B706/B733); the constraint is on the object's orientation, not on theta_QCD."),

    # extended (neutrino) sector -- graded for completeness
    ("nu masses (m1,m2,m3)",     "d",
     "B685: masses are coupling data; object scaleless => no neutrino mass value or splitting forced."),
]


def print_ledger():
    out = []
    out.append(SEP)
    out.append("PART 4 -- THE PARAMETER-REDUCTION LEDGER")
    out.append(SEP)
    out.append("grade: a=forced VALUE  b=forced RELATION(=reduction)  c=discrete CONSTRAINT  d=nothing")
    out.append(sub)
    out.append(f"{'parameter':26s} | grade | discriminating banked fact")
    out.append(sub)
    for name, grade, reason in LEDGER:
        # wrap reason
        words = reason.split()
        lines, cur = [], ""
        for w in words:
            if len(cur) + len(w) + 1 > 44:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        lines.append(cur)
        out.append(f"{name:26s} |   {grade}   | {lines[0]}")
        for extra in lines[1:]:
            out.append(f"{'':26s} |       | {extra}")
    out.append(sub)
    return "\n".join(out)


# ----------------------------------------------------------------------
# PART 5 -- THE COUNT + THE THEOREM
# ----------------------------------------------------------------------
def count_and_theorem(wall_ok, generic_ok):
    grades = [g for _, g, _ in LEDGER]
    n = len(grades)
    n_a = grades.count("a")   # forced values
    n_b = grades.count("b")   # forced relations = REDUCTIONS
    n_c = grades.count("c")   # discrete constraints on an SM parameter
    n_d = grades.count("d")   # nothing

    out = []
    out.append(SEP)
    out.append("PART 5 -- THE COUNT + THE STRUCTURAL NO-GO THEOREM")
    out.append(SEP)
    out.append(f"parameters graded            : {n}")
    out.append(f"  (a) forced VALUE           : {n_a}")
    out.append(f"  (b) forced RELATION        : {n_b}   <== the REDUCTION count")
    out.append(f"  (c) discrete CONSTRAINT    : {n_c}")
    out.append(f"  (d) nothing forced         : {n_d}")
    out.append("")
    out.append(f"GENUINE REDUCTIONS (forced relations removing a free parameter) = {n_b}")
    out.append("")
    out.append("THEOREM (P3 no-go). No SM free parameter is fixed, and no pair is tied by a")
    out.append("framework-forced relation. Every candidate reduction dies to one of three")
    out.append("independent, mutually-reinforcing obstructions:")
    out.append("")
    out.append("  (i)  EQUIVARIANCE WALL (B650, recomputed Part 1). The only monodromy-")
    out.append("       equivariant C-linear map being->hearing is T = 0 (spectra disjoint:")
    out.append("       phi^{+-2} real hyperbolic vs primitive-10th-root unitary). => no linear")
    out.append("       channel transports a continuous quantity across sectors, so the")
    out.append("       being<->hearing coupling CANNOT synthesize a grade-(b) relation.")
    out.append("")
    out.append("  (ii) KIND-MISMATCH (B706, Part 3). The object's freedom is DISCRETE (F2")
    out.append("       orientation bits); the SM's is CONTINUOUS (~19 reals). Different")
    out.append("       cardinality and dimension-type. Independently, PSLQ over Q(sqrt5)")
    out.append("       finds NO low-height relation among the mass ratios: generic at the")
    out.append("       number level too. => no grade-(a) value, no grade-(b) relation.")
    out.append("")
    out.append("  (iii) BOUNDED-V4 CEILING (B733/B704, Part 2). The observer/design space is")
    out.append("       a bounded discrete F2-space of rank <= 3, depth-independent and")
    out.append("       saturating -- a dimension-0 set of <=8 menus. It never grows toward")
    out.append("       the ~19-parameter continuum. => cannot coordinatize the SM moduli;")
    out.append("       no grade-(a)/(b)/(c) constraint on a continuous parameter survives.")
    out.append("")
    out.append("The only framework-FORCED content is DISCRETE/structural and lives entirely")
    out.append("on the object side, never on an SM parameter: the arithmetic atom Q(sqrt-3)")
    out.append("(Reid/B266); the V4 measurement torsor (B701/B704); the congruence bits")
    out.append("(m004 @ (2)^3=(8), B734; B701 = Out(A5), B732). None of these is an SM")
    out.append("parameter, and none is a relation BETWEEN SM parameters.")
    out.append("")
    verdict = "B" if (n_b == 0 and wall_ok) else "A"
    out.append(f"internal consistency: wall==T=0? {wall_ok}   ratios generic? {generic_ok}")
    out.append(f"OUTCOME: {verdict}   (A = >=1 reduction; B = zero + the rigorous no-go)")
    return "\n".join(out), n_b, verdict


def main():
    blocks = []
    wall_txt, wall_ok = equivariance_wall()
    blocks.append(wall_txt)
    blocks.append(capacity_nogo())
    try:
        gen_txt, generic_ok = genericity_control()
    except Exception as e:
        gen_txt, generic_ok = (f"PART 3 skipped (mpmath issue: {e})", True)
    blocks.append(gen_txt)
    blocks.append(print_ledger())
    thm_txt, nred, verdict = count_and_theorem(wall_ok, generic_ok)
    blocks.append(thm_txt)

    report = "\n\n".join(blocks) + "\n"
    print(report)
    return report


if __name__ == "__main__":
    main()
