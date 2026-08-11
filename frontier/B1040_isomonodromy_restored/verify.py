"""B1040 — the isomonodromy cluster restored (B164 + B169 + B150).

Restoration 4 of B1037's seven, under campaign step 5. Three debt rows, one law.

Unlike arithmeticity / the collective / the open arrow, this cluster IS fully re-verifiable here:
the core is polynomial identities, and the one numerical result (the Schlesinger flow) is
numpy-only AND ships with a non-vacuity control, which is what makes it evidence at all.

Re-verifying sharpened three things, in the B1039 pattern:

  (1) B164's "dim = 6g-6+2n = 2 only at (1,1) and (0,4)" is an inline parenthetical carried by
      CITATION (Cantat-Loray, Iwasaki, Boalch) with NO backing check anywhere in the repo -- a
      repo-wide search for "6g-6" returns two hits, neither a computation. It is a two-line
      exhaustive integer argument. PROVED here: the restoration UPGRADES a citation to a proof.
  (2) B169's P1 is tagged [exact], but what its script computes is an EIGENVALUE TAUTOLOGY. No
      Picard lattice and no homological action is computed anywhere in the arc. The NUMBER
      re-verifies (and generalises -- symbolically in m, where the arc did m = 1,2,3); the
      identification of that number as the DYNAMICAL DEGREE is citation-carried. Said so.
  (3) B169's P3 checks are `chk(..., True)` LITERALS -- they assert, they do not compute. Its one
      formalisable sub-claim (scale-freeness) is checked here, and P3 still restores as POSTULATED,
      because a verified homogeneity does not make a structural verdict a theorem.

And one supersession the restoration must respect: B164's C4 was CORRECTED by B169's P1 (the
point-orbit-norm proxy tracked the naive degree, not the dynamical one). The restored row carries
B169's form.
"""
import json
import pathlib
import re
import subprocess
import sys

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


x, y, z = sp.symbols("x y z")
t1, t2, t3, t4 = sp.symbols("t1 t2 t3 t4")
lam, m, u = sp.symbols("lam m u")

# =================================================== C1 -- the Jimbo-Fricke cubic and its dynamics
px, py, pz = t1*t2 + t3*t4, t1*t4 + t2*t3, t1*t3 + t2*t4
p0 = 4 - (t1**2 + t2**2 + t3**2 + t4**2) - t1*t2*t3*t4
PHI = x**2 + y**2 + z**2 + x*y*z - px*x - py*y - pz*z - p0

VIETA = {
    "s_x": lambda v: (px - v[1]*v[2] - v[0], v[1], v[2]),
    "s_y": lambda v: (v[0], py - v[0]*v[2] - v[1], v[2]),
    "s_z": lambda v: (v[0], v[1], pz - v[0]*v[1] - v[2]),
}
inv_ok, pres_ok = {}, {}
for nm, s in VIETA.items():
    im = s((x, y, z))
    inv_ok[nm] = sp.expand(sp.Matrix(s(im)) - sp.Matrix([x, y, z])) == sp.zeros(3, 1)
    pres_ok[nm] = sp.expand(PHI.subs({x: im[0], y: im[1], z: im[2]}, simultaneous=True) - PHI) == 0
chk("C1_the_three_Vieta_maps_are_involutions", all(inv_ok.values()), per_map=inv_ok)
chk("C1b_and_each_PRESERVES_the_Jimbo_Fricke_cubic", all(pres_ok.values()), per_map=pres_ok,
    note="symbolic in ALL SEVEN variables -- the four boundary traces stay free, so this is the "
         "cubic as a family, not one fibre")

# the composite is NOT an involution -- otherwise 'they generate a dynamics' would be vacuous
sxy = VIETA["s_y"](VIETA["s_x"]((x, y, z)))
sxy2 = VIETA["s_y"](VIETA["s_x"](sxy))
chk("C1c_but_the_COMPOSITE_is_not_one_so_the_group_is_infinite",
    sp.expand(sp.Matrix(sxy2) - sp.Matrix([x, y, z])) != sp.zeros(3, 1),
    note="MB-style non-vacuity: three involutions generating only involutions would be a finite "
         "group and there would be no Painleve-VI dynamics to speak of")

# =================================================== C2 -- the bridge to the OPT cubic at kappa = 2
PHI0 = sp.expand(PHI.subs({t1: 0, t2: 0, t3: 0, t4: 0}))
KAPPA = x**2 + y**2 + z**2 - x*y*z - 2
chk("C2_at_zero_boundary_traces_the_cubic_becomes_the_OPT_kappa_equals_2_fibre",
    sp.expand(PHI0 - (x**2 + y**2 + z**2 + x*y*z - 4)) == 0
    and sp.expand(PHI0.subs(z, -z) - (KAPPA - 2)) == 0,
    note="z -> -z carries it onto kappa = 2, the void / cancellation fibre (B161). So the (0,4) "
         "void fibre IS the OPT kappa = 2 fibre -- a concrete link at ONE special fibre, which is "
         "all B164 claims; the general OPT <-> (0,4) dictionary is explicitly deferred")

# =================================================== the (g,n) uniqueness -- CITATION -> PROOF
gn = [(g, n) for g in range(0, 41) for n in range(0, 81)
      if 6*g - 6 + 2*n == 2 and 2*g - 2 + n > 0]
chk("THE_UPGRADE_dim_2_Fricke_cubics_are_EXACTLY_(1,1)_and_(0,4)",
    sorted(gn) == [(0, 4), (1, 1)],
    solutions=[list(p) for p in sorted(gn)], swept="g <= 40, n <= 80",
    note="6g-6+2n = 2 <=> 3g+n = 4; with hyperbolicity 2g-2+n > 0 the cases are g=0 -> n=4 and "
         "g=1 -> n=1, and g >= 2 forces n = 4-3g < 0. B164 states this as an inline parenthetical "
         "carried by citation; a repo-wide search for '6g-6' returns exactly TWO hits, NEITHER a "
         "computation. NOT A DISCOVERY -- the fact is classical (Fricke; Cantat-Loray), and "
         "docs/OPEN_LEADS.md:209 says so in as many words: 'the exactly two cubic surfaces "
         "dim-count is classical-known ... not a discovery'. What changes is only that the corpus "
         "now CHECKS what it had only cited. A verification, not a result")

# =================================================== B150 -- the convention match, exactly
fricke_lhs = sp.expand((-x)**2 + (-y)**2 + (-z)**2 + (-x)*(-y)*(-z))
chk("B150_the_Fricke_cubic_and_kappa_are_the_same_equation",
    sp.expand(fricke_lhs - (KAPPA + 2)) == 0,
    note="Allegretti-Shan write a^2+b^2+c^2+abc = 2+lam+1/lam with (a,b,c) = (-tr A, -tr B, "
         "-tr AB). Substituting gives kappa = tr[A,B] = lam + 1/lam exactly, so the class-S "
         "Coulomb-branch cubic and the B148 kappa level sets COINCIDE -- the convention match "
         "that makes the whole comparison a comparison of one object rather than two")
chk("B150b_and_the_Markov_fibre_is_kappa_equals_minus_2",
    sp.solve(sp.Eq(lam + 1/lam, -2), lam) == [-1],
    note="kappa = -2 <=> lam = -1")

# =================================================== C3 / P1 -- the metallic degrees, IN m
lam_m = (m + sp.sqrt(m**2 + 4)) / 2
chk("C3_the_metallic_eigenvalue_and_its_square_SYMBOLICALLY_IN_m",
    sp.simplify(lam_m**2 - m*lam_m - 1) == 0
    and sp.simplify(sp.expand((lam_m**2)**2 - (m**2 + 2)*lam_m**2 + 1)) == 0,
    minpoly_of_lambda="t^2 - m t - 1", minpoly_of_lambda_squared="u^2 - (m^2+2) u + 1",
    note="B164 and B169 verify m = 1,2,3; this holds for every m, which is the statement the law "
         "actually needs")
vals = {mm: str(sp.nsimplify(sp.radsimp(lam_m.subs(m, mm)**2))) for mm in (1, 2, 3)}
chk("C3b_and_it_reproduces_the_three_banked_values",
    sp.simplify(sp.radsimp(lam_m.subs(m, 1)**2) - (3 + sp.sqrt(5))/2) == 0
    and sp.simplify(sp.radsimp(lam_m.subs(m, 2)**2) - (3 + 2*sp.sqrt(2))) == 0
    and sp.simplify(sp.radsimp(lam_m.subs(m, 3)**2) - (11 + 3*sp.sqrt(13))/2) == 0,
    values=vals, trace_fields={mm: "Q(sqrt(%d))" % (mm*mm + 4) for mm in (1, 2, 3)})

# =================================================== P2 -- the flow, re-run WITH ITS CONTROL
out = subprocess.run([sys.executable, str(ROOT / "frontier/B169_isomonodromy_flow/isomonodromy.py")],
                     capture_output=True, text=True, timeout=1800)
drift = re.search(r"max invariant drift over s:2->3 = ([0-9.e+-]+)", out.stdout)
ctrl = re.search(r"wrong-ODE invariant drift = ([0-9.e+-]+)", out.stdout)
d_val = float(drift.group(1)) if drift else None
c_val = float(ctrl.group(1)) if ctrl else None
chk("P2_the_Schlesinger_flow_preserves_every_local_conjugacy_class",
    out.returncode == 0 and d_val is not None and d_val < 1e-8,
    drift=drift.group(1) if drift else None,
    note="re-run here via B169's own reproducer (the B1033 pattern), not quoted")
chk("P2b_AND_the_control_fires__which_is_what_makes_it_evidence",
    c_val is not None and c_val > 1.0 and d_val is not None and c_val / d_val > 1e8,
    control=ctrl.group(1) if ctrl else None,
    ratio="%.2e" % (c_val / d_val) if (c_val and d_val) else None,
    note="RK4 at h = 0.01 has O(h^4) truncation, so the ABSOLUTE smallness of 4e-10 is not the "
         "evidence -- the CONTRAST with a non-Schlesinger ODE at 1.6e+01 is. Restoring the drift "
         "without the control would restore a number that proves nothing")

# =================================================== P3 -- the one computable part of a POSTULATE
s_, c_, ti_ = sp.symbols("s c t_i")
rhs = 1/(s_ - ti_)
chk("P3_the_flow_is_SCALE_FREE_the_check_the_arc_never_runs",
    sp.simplify(rhs.subs({s_: c_*s_, ti_: c_*ti_}) - rhs/c_) == 0,
    note="under s -> c s, t -> c t with the residues fixed, dA/ds = [A_3,A_i]/(s-t_i) is "
         "homogeneous: the RHS scales by 1/c and ds by c. No dimensionful parameter appears. "
         "B169 asserts this in prose and its two P3 checks pass `True` LITERALLY")
chk("P3b_but_the_verdict_is_still_POSTULATED_and_stays_so", True,
    note="a verified homogeneity does not make 'the firewall RELOCATES rather than crosses' a "
         "theorem -- that is a structural reading, tiered POSTULATED by B169 itself, and the "
         "restored row carries that tier unchanged")

# =================================================== the supersession the row must respect
b164 = (ROOT / "frontier/B164_isomonodromy_04cubic/FINDINGS.md").read_text(encoding="utf-8")
b169 = (ROOT / "frontier/B169_isomonodromy_flow/FINDINGS.md").read_text(encoding="utf-8")
chk("B164s_C4_is_SUPERSEDED_by_B169s_P1_and_both_arcs_say_so",
    "This corrects B164's C4" in b169 and "the numerics **refuted** it" in b164,
    note="B164's C4 used a point-orbit-norm proxy that tracks the NAIVE (cancellation-free) "
         "degree, not the dynamical one. The restored row carries B169's corrected form; "
         "restoring B164's would restore a superseded reading")

# =================================================== the restoration landed, WITH its scope
LAWMAP = (ROOT / "docs/LAW_MAP.md").read_text(encoding="utf-8")
chk("the_law_is_now_on_a_curated_surface",
    "THE PAINLEVÉ-VI PARTNER IS FORCED BY A DIMENSION COUNT" in LAWMAP
    and all(b in LAWMAP for b in ("B164", "B169", "B150")))
chk("and_it_carries_the_THREE_scope_corrections_that_must_travel",
    "not a discovery" in LAWMAP and "no Picard lattice" in LAWMAP
    and "superseded by B169" in LAWMAP and "POSTULATED" in LAWMAP,
    note="the classical-not-discovered status of the (g,n) count, the missing homological "
         "computation behind an [exact] tag, and B164's C4 supersession. A restoration that drops "
         "any one of them restores an overclaim")
chk("and_the_control_is_named_beside_the_number_it_licenses",
    "non-Schlesinger control" in LAWMAP and "4.25×10⁻¹⁰" in LAWMAP,
    note="the drift is meaningless without the control; the row states both or neither")

R["carried_by_citation"] = {
    "the dynamical-degree IDENTIFICATION": "that lambda_m^2 IS the dynamical degree on the cubic "
        "is Cantat-Loray's theorem (the Picard-lattice / homological degree). NO Picard lattice "
        "is computed in B164, B169 or here -- the arcs compute an eigenvalue. B169 tags P1 "
        "[exact]; the exactness is the ALGEBRA's, not the identification's.",
    "the class-S dictionary (B150)": "that the SL(2,Z) MCG action on the character variety IS the "
        "N=2* S-duality action is read from Allegretti-Shan and GMN. B150 is a tagged "
        "literature comparison (FORCED / PERMITTED / RHYME), not a sandbox computation, and the "
        "tau-modularity face is tagged RHYME -- a HOMONYM, same group, different space.",
    "Painleve-VI itself": "that the (0,4) Vieta dynamics IS the Painleve-VI monodromy action is "
        "Jimbo-Miwa / Boalch. The cubic and its involutions are built here; the Painleve "
        "identification is cited.",
    "the Hitchin/Higgs side": "the hyperkahler metric and spectral curve, where the external "
        "scale would live explicitly, are NEEDS-SPECIALIST in B169's own words and are not "
        "attempted.",
}

R["all_pass"] = all(v["pass"] for v in R["checks"].values())
if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False, default=str))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"], " checks:", len(R["checks"]))
