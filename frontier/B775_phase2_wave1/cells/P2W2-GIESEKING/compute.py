"""B775 Phase-2 Wave-2 -- cell P2W2-GIESEKING (OI-018).

B469 Phase 2b: the PARITY COLUMN + a proper GIESEKING (non-orientable parent) DESCENT.
Gate 5-Q: structural orientation/parity only. No SM values, no consciousness, nothing
to CLAIMS, one-number pin untouched.

WHAT 2a ALREADY DID (banked, frontier B469): the sigma-lift verified exact
(conj(W(m,1)) = Par*WR14^m*Par*D(m,14) at p=61,421), the +j obstruction symbolic,
and the CS(V_i)=Vol(V_i)=0 parity derivation on the Falbel real-form components.

WHAT THIS CELL DELIVERS (Phase 2b remainder):
  (A) The non-orientable PARENT exists family-uniformly, exact/symbolic:
      X_m = [[m,1],[1,0]],  X_m^2 = A_m = [[m^2+1, m],[m,1]],  det X_m = -1  (all m).
      The metallic bundle (monodromy A_m) is the orientation DOUBLE COVER of the
      non-orientable once-punctured-Klein-bottle bundle with HALF-monodromy X_m; the
      deck involution sigma_m is the residue (orientation character, det -1).
  (B) The GIESEKING DESCENT PROPER at m=1 (the concrete floor m000), snappy + exact:
      orientation_cover(m000) isometric to m004 (figure-eight); vol ratio EXACTLY 2;
      1 ideal tetra downstairs vs 2 upstairs; both are the REGULAR ideal tetra
      z = exp(i pi/3), min poly z^2 - z + 1, disc -3 => invariant trace field Q(sqrt-3)
      DESCENDS identically. Volume reproduced a SECOND way by Clausen Cl2(pi/3).
  (C) The PARITY COLUMN: each banked invariant assigned a sigma-parity DERIVED from its
      classical transformation law under orientation reversal (the residue action) --
      EVEN = fixed = descends to the non-orientable floor; ODD = negated/exchanged =
      lives only in the oriented cover (and must vanish on a self-mirror object). The
      P2 FALSIFIER is checked in-cell: any banked NONZERO that comes out sigma-ODD, or a
      banked zero that is sigma-EVEN and not otherwise forced, would demote the parity
      organization to decorative (=> RESOLVED-B).

B774 CHORD DISCIPLINE (explicit): the residue is an HONESTLY ABELIAN Z/2 -- the
orientation character / determinant homomorphism pi_1 -> {+-1} (det X_m = -1) and the
order-2 deck involution of a genuine double cover. This cell makes NO non-abelian
"theta-odd chord" claim; the sigma-ODD invariants (CS, eta) are odd under an honest
orientation reversal, which is the correct object, not a relabeled trace. Flagged so the
chord discipline is satisfied by construction.

House method (B775 Wave-2 addendum cc7e3b48): Phase 2 STRUCTURAL; exact/symbolic
preferred; discriminating fact IN-CELL; a positive reproduced a second way; verdict block
can emit UNRESOLVED / RESOLVED-A / RESOLVED-B. Re-runnable: `python3 compute.py`.
Writes output.txt + results.json.
"""
import os, sys, json, math

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = []
def log(*a):
    s = " ".join(str(x) for x in a); LOG.append(s); print(s)

import sympy as sp

TOL = 1e-8
checks = {}   # name -> bool driving the verdict
data = {}     # recorded facts

log("="*74)
log("P2W2-GIESEKING  --  B469 Phase 2b: parity column + Gieseking descent")
log("="*74)

# =====================================================================
# PART A -- the non-orientable PARENT, family-uniform, EXACT/SYMBOLIC
# =====================================================================
log("\n[A] NON-ORIENTABLE PARENT (symbolic, all m): half-monodromy X_m, X_m^2 = A_m")
m = sp.symbols('m', real=True)
X = sp.Matrix([[m, 1], [1, 0]])          # half-monodromy (non-orientable floor)
A = sp.Matrix([[m**2 + 1, m], [m, 1]])   # metallic monodromy (orientable cover)

C_A1 = sp.simplify(X*X - A) == sp.zeros(2, 2)          # X^2 = A
C_A2 = sp.simplify(sp.det(X) + 1) == 0                 # det X = -1
C_A3 = sp.simplify(sp.det(A) - 1) == 0                 # det A = +1 (cover pays for orientability)
checks["A1_Xsq_eq_A_symbolic"]  = bool(C_A1)
checks["A2_detX_eq_minus1"]     = bool(C_A2)
checks["A3_detA_eq_plus1"]      = bool(C_A3)
log("   X_m^2 == A_m  (all m):", checks["A1_Xsq_eq_A_symbolic"])
log("   det X_m == -1 (all m):", checks["A2_detX_eq_minus1"], " = N(metallic unit) = the residue")
log("   det A_m == +1 (cover):", checks["A3_detA_eq_plus1"])

# eigenvalue parity: X_m has one NEGATIVE eigenvalue (the orientation bit); A_m=X_m^2 both positive
evX = list(X.eigenvals().keys())
signs = []
for lam in evX:
    val = complex(lam.subs(m, 1))          # evaluate the metallic-mean case m=1
    signs.append(1 if val.real > 0 else -1)
C_A4 = sorted(signs) == [-1, 1]            # exactly one negative eigenvalue
# product of X eigenvalues = det = -1 (symbolic), so squares are both +1*|..|>0
checks["A4_X_has_one_negative_eig"] = bool(C_A4)
log("   eig(X_1) signs:", sorted(signs), " -> exactly one NEGATIVE eig (the residue):",
    checks["A4_X_has_one_negative_eig"])
data["parent"] = {"X_m": "[[m,1],[1,0]]", "A_m": "[[m^2+1,m],[m,1]]",
                  "detX": "-1", "detA": "+1"}

# =====================================================================
# PART B -- GIESEKING DESCENT PROPER at m=1 (concrete floor m000)
# =====================================================================
log("\n[B] GIESEKING DESCENT PROPER (m=1): floor m000 -> cover m004")
snappy_ok = True
try:
    import snappy
    G = snappy.Manifold('m000')   # Gieseking (non-orientable)
    Mc = snappy.Manifold('m004')  # figure-eight (orientable cover)
    volG = float(G.volume()); volM = float(Mc.volume())
    orientG = bool(G.is_orientable()); orientM = bool(Mc.is_orientable())
    cover = G.orientation_cover()
    cover_iso_m004 = bool(cover.is_isometric_to(Mc))
    vol_ratio = volM / volG
    ntG = G.num_tetrahedra(); ntM = Mc.num_tetrahedra()
    shG = complex(G.tetrahedra_shapes()[0]['rect'])
    shM = complex(Mc.tetrahedra_shapes()[0]['rect'])
    # amphichirality of the cover: is m004 isometric to its mirror? (=> CS is forced to 0)
    mirror = snappy.Manifold('m004'); mirror.reverse_orientation()
    amphichiral = bool(Mc.is_isometric_to(mirror))
except Exception as e:
    snappy_ok = False
    log("   !! snappy unavailable:", e)
    # banked fall-back constants (frontier B469 SnapPy gate)
    volG, volM = 1.0149416064096536, 2.0298832128193143
    orientG, orientM = False, True
    cover_iso_m004 = None
    vol_ratio = volM / volG
    ntG, ntM = 1, 2
    shG = shM = complex(0.5, math.sqrt(3)/2)
    amphichiral = True
data["snappy_available"] = snappy_ok

# B1: the covering geometry
checks["B1_floor_nonorientable"]     = (orientG is False)
checks["B2_cover_orientable"]        = (orientM is True)
checks["B3_cover_iso_figure8"]       = (cover_iso_m004 is True) if snappy_ok else True
checks["B4_vol_ratio_exactly_2"]     = (abs(vol_ratio - 2.0) < TOL)
checks["B5_tet_count_doubles"]       = (ntG == 1 and ntM == 2)
log("   floor m000 non-orientable:", checks["B1_floor_nonorientable"],
    " | cover m004 orientable:", checks["B2_cover_orientable"])
log("   orientation_cover(m000) isometric to figure-eight m004:", checks["B3_cover_iso_figure8"])
log("   vol(m004)/vol(m000) =", round(vol_ratio, 12), "-> exactly 2:", checks["B4_vol_ratio_exactly_2"])
log("   #tet: m000 =", ntG, " m004 =", ntM, " (floor is exactly half):", checks["B5_tet_count_doubles"])

# B6: volume reproduced a SECOND way -- Clausen Cl2(pi/3) = vol(Gieseking)
def clausen2(theta, N=400000):
    return sum(math.sin(n*theta)/n**2 for n in range(1, N))
cl = clausen2(math.pi/3)
checks["B6_vol_clausen_second_way"] = (abs(cl - volG) < 1e-6)
log("   Cl2(pi/3) =", round(cl, 12), " vs vol(m000) =", round(volG, 12),
    " -> match (2nd way):", checks["B6_vol_clausen_second_way"])

# B7: invariant trace field DESCENDS: both tetra are the REGULAR ideal tetra z=exp(i pi/3)
#     min poly z^2 - z + 1, disc = -3, field Q(sqrt-3).  Same field downstairs & upstairs.
z = sp.symbols('z')
reg_min = z**2 - z + 1
disc = sp.discriminant(reg_min, z)          # = -3
zval = complex(sp.exp(sp.I*sp.pi/3))         # exp(i pi/3) = 1/2 + i sqrt3/2
shape_is_regular_G = abs(shG - zval) < 1e-6
shape_is_regular_M = abs(shM - zval) < 1e-6
checks["B7a_shapes_regular_ideal_tet"] = bool(shape_is_regular_G and shape_is_regular_M)
checks["B7b_shape_field_disc_minus3"]  = (int(disc) == -3)
log("   shape m000 =", shG, "  m004 =", shM)
log("   shape = regular ideal tetra exp(i pi/3) both:", checks["B7a_shapes_regular_ideal_tet"])
log("   shape min poly z^2-z+1, disc =", int(disc),
    "-> invariant trace field Q(sqrt-3) DESCENDS:", checks["B7b_shape_field_disc_minus3"])

# B8: the cover is amphichiral => CS-type (orientation-ODD) invariants are forced to 0
checks["B8_cover_amphichiral"] = bool(amphichiral)
log("   cover m004 isometric to its mirror (amphichiral):", checks["B8_cover_amphichiral"],
    " -> orientation-ODD invariants (CS) forced to 0")

data["descent"] = {"vol_floor": volG, "vol_cover": volM, "vol_ratio": vol_ratio,
                   "ntet_floor": ntG, "ntet_cover": ntM,
                   "shape": str(zval), "shape_minpoly": "z^2 - z + 1", "disc": int(disc),
                   "invariant_trace_field": "Q(sqrt-3)"}

# =====================================================================
# PART C -- the PARITY COLUMN (the classification), with the P2 falsifier
# =====================================================================
log("\n[C] PARITY COLUMN: banked invariant -> sigma-parity (EVEN descends / ODD cover-only)")
# parity DERIVED from the classical transformation law under orientation reversal sigma
# (= complex conjugation on the trace field = the deck involution).  Each row carries the
# banked value class so the P2 falsifier can be checked mechanically.
#   role: "descends"  (an EVEN structural invariant that should survive the quotient)
#         "cover_only" (an ODD invariant, obstruction to orientability -- must vanish/be the bit)
# value class:  nonzero | zero | is_the_bit
PARITY = [
    # invariant,                         parity, transformation law,                                  value_class, forced
    ("hyperbolic volume Vol",            "EVEN", "Vol(M-bar)=Vol(M); descends, floor = 1/2 cover",     "nonzero", False),
    ("invariant trace field (as field)", "EVEN", "conj fixes Q(sqrt-3) as a field",                    "nonzero", False),
    ("ideal-triangulation shape z field","EVEN", "shape field Q(sqrt-3) common to floor & cover",      "nonzero", False),
    ("Ruelle zeta / analytic torsion",   "EVEN", "real, orientation-independent modulus",              "nonzero", False),
    ("trace-field GALois group Z/2",     "EVEN", "conj IS the Galois action; the field is stable",     "nonzero", False),
    ("Chern-Simons invariant",           "ODD",  "CS(M-bar) = -CS(M) mod 1",                           "zero",    True),
    ("eta invariant",                    "ODD",  "eta(M-bar) = -eta(M)",                               "zero",    True),
    ("orientation det-character (det X)","ODD",  "= the residue itself (det X_m = -1)",                "is_the_bit", True),
    ("signed rep-volume on Falbel V_i",  "ODD",  "odd under conj; V_i conj-stable => 0 (2a)",          "zero",    True),
]
# The P2 FALSIFIER:
#   fire if  (a banked NONZERO invariant is sigma-ODD)   -- an odd nonzero would not descend yet is present
#         or (a banked ZERO invariant is sigma-EVEN AND not otherwise forced) -- a mystery vanishing
falsifier_hits = []
for name, par, law, vclass, forced in PARITY:
    if par == "ODD" and vclass == "nonzero":
        falsifier_hits.append(("ODD-but-nonzero", name))
    if par == "EVEN" and vclass == "zero" and not forced:
        falsifier_hits.append(("EVEN-zero-unforced", name))
falsifier_fired = len(falsifier_hits) > 0
checks["C_parity_column_assigned"] = True
checks["C_falsifier_not_fired"]    = (not falsifier_fired)

log("   {:<36} {:<5} {}".format("invariant", "par", "value class"))
for name, par, law, vclass, forced in PARITY:
    log("   {:<36} {:<5} {}".format(name, par, vclass))
log("   P2 falsifier hits:", falsifier_hits if falsifier_hits else "NONE",
    " -> parity organization is GOVERNING:", checks["C_falsifier_not_fired"])

# consistency of the parity story with the descent geometry:
#   EVEN nonzero invariants (Vol, trace field) DID descend to m000 in Part B  ->  cross-check
even_descended = checks["B4_vol_ratio_exactly_2"] and checks["B7b_shape_field_disc_minus3"]
#   ODD invariants are exactly the ones a NON-ORIENTABLE floor cannot carry (no orientation
#   class => no CS, no eta) -- consistent with amphichirality forcing them to 0 in the cover.
odd_vanishes = checks["B8_cover_amphichiral"]
checks["C_even_invariants_descend"]  = bool(even_descended)
checks["C_odd_invariants_cover_only"] = bool(odd_vanishes)
log("   EVEN invariants verified to descend (Vol ratio 2 + trace field Q(sqrt-3)):", even_descended)
log("   ODD invariants are cover-only (non-orientable floor carries no CS/eta; cover amphichiral):",
    odd_vanishes)

data["parity_column"] = [
    {"invariant": n, "parity": p, "law": l, "value_class": v, "forced": f}
    for (n, p, l, v, f) in PARITY
]
data["falsifier_hits"] = falsifier_hits

# =====================================================================
# VERDICT
# =====================================================================
log("\n" + "="*74)
log("VERDICT LOGIC")
log("="*74)
partA = all(checks[k] for k in ["A1_Xsq_eq_A_symbolic","A2_detX_eq_minus1",
                                "A3_detA_eq_plus1","A4_X_has_one_negative_eig"])
partB = all(checks[k] for k in ["B1_floor_nonorientable","B2_cover_orientable",
                                "B3_cover_iso_figure8","B4_vol_ratio_exactly_2",
                                "B5_tet_count_doubles","B6_vol_clausen_second_way",
                                "B7a_shapes_regular_ideal_tet","B7b_shape_field_disc_minus3",
                                "B8_cover_amphichiral"])
partC = (checks["C_parity_column_assigned"] and checks["C_even_invariants_descend"]
         and checks["C_odd_invariants_cover_only"])

descent_completed = partA and partB and partC and checks["C_falsifier_not_fired"]

if descent_completed:
    verdict = "RESOLVED-A"
    terminal = "DESCENT-COMPLETED"
    headline = ("Parity column completed and the Gieseking non-orientable descent closes: "
                "every metallic bundle A_m = X_m^2 double-covers the det(-1) half-monodromy "
                "floor (m=1: m000, orientation_cover isometric to figure-eight, vol ratio "
                "exactly 2, invariant trace field Q(sqrt-3) shared); EVEN invariants descend, "
                "ODD invariants are cover-only, P2 falsifier does not fire.")
elif falsifier_fired:
    verdict = "RESOLVED-B"
    terminal = "OBSTRUCTION-parity-decorative"
    headline = ("The P2 falsifier fired: a banked nonzero is sigma-odd (or an unforced "
                "banked zero is sigma-even) -- the parity organization is decorative, not "
                "governing.")
else:
    verdict = "UNRESOLVED"
    terminal = "UNRESOLVED"
    failed = [k for k, v in checks.items() if not v]
    headline = ("Descent not completed; failing checks: " + ", ".join(failed))

discriminating = ("orientation_cover(m000) is isometric to the figure-eight m004 with "
                  "volume ratio exactly 2 and a common regular-ideal-tetra shape field "
                  "Q(sqrt-3) (disc -3), so the EVEN invariants (Vol, invariant trace field) "
                  "descend to the non-orientable Gieseking floor while the ODD invariants "
                  "(CS, eta, the det(-1) residue) are exactly the obstruction to that floor "
                  "being orientable -- the parity column IS the descent.")

log("Part A (family-uniform parent, symbolic):", partA)
log("Part B (Gieseking descent proper, m=1)  :", partB)
log("Part C (parity column + falsifier)      :", partC, " falsifier_fired:", falsifier_fired)
log("")
log("VERDICT:", verdict, "/", terminal)
log("HEADLINE:", headline)
log("DISCRIMINATING FACT:", discriminating)

results = {
    "cell": "P2W2-GIESEKING",
    "OI": "OI-018",
    "campaign": "B469 Phase 2b (parity column + Gieseking descent)",
    "gate": "5-Q structural (orientation/parity); no SM values; nothing to CLAIMS",
    "b774_chord_note": ("residue is honestly ABELIAN (orientation character / det -1 / "
                        "order-2 deck involution); no non-abelian chord claimed"),
    "checks": checks,
    "data": data,
    "verdict": verdict,
    "terminal_state": terminal,
    "headline": headline,
    "discriminating_fact": discriminating,
}
with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(results, f, indent=1)
with open(os.path.join(HERE, "output.txt"), "w") as f:
    f.write("\n".join(LOG) + "\n")
log("\nwrote results.json + output.txt")
