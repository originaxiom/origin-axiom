"""Assemble REPORT.json from the referee's result files (numbers read from them, not retyped where possible)."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
J = lambda f: json.loads((HERE / f).read_text())

vac = J("t_vacua.json"); sym = J("t_sympoints.json"); rs = J("t_runaway_stable.json"); dj = J("t_dec_jacobian.json")
nj = J("t_norm_jacobian.json"); cv = J("t_conventions.json"); a0 = J("t_a0.json"); ct = J("t_cross_terms.json")
sn = J("t_supnorm.json"); n2 = J("t_n2_cross.json"); sa = J("t_controls_S_action.json")

iso = [r for r in vac["rows"] if r["draft_class"]["isolated"]]
gaps = sorted(((r["H_eigs"][1] - r["S_rayleigh"]) / max(abs(x) for x in r["H_eigs"]), r["menu"], r["tnorm"], r["n"], r["mu2"], r["lv"]) for r in iso)
undercut = [r for r in rs["rows"] if r["undercut_confirmed_in_mpmath"] and r["tnorm"] == "cusp"]
undercut_txt = "; ".join("%s/%s n=%d (mu2 %.1f, lv %.1f): reported %.4g, found %.4g at Im tau %.2f" % (
    r["menu"], r["tnorm"], r["n"], r["mu2"], r["lv"], r["V_reported"], r["arbiter_mpmath_V_at_best"], r["arbiter_best_tau"][1]) for r in undercut)
not_undercut_primary = [r for r in rs["rows"] if r["tnorm"] == "N" and not r["undercut_confirmed_in_mpmath"]]

dec_txt = "; ".join("%s n=%d %s: rank(mu alone) 1, rank(mu + 3n normalisations) %d, svals %s" % (
    r["menu"], r["n"], "on a mirror line" if r["on_mirror_line"] else "OFF the mirror lines", r["rank_all"],
    ", ".join("%.2g" % v for v in r["svals_all"])) for r in dj["rows"])
nj_off = [r for r in nj["rows"] if r["mirror"] is None and r["n"] >= 3]
nj_txt = "; ".join("%s n=%d mu2=%.1f lv=%.1f: rank(draft's 3) %d, rank(+normalisations) %d" % (
    r["menu"], r["n"], r["mu2"], r["lv"], r["rank_draft_params"], r["rank_all"]) for r in nj_off)
hess_min = min(min(r["hess_eigs"]) for r in nj["rows"])

conv_rows = [r for r in cv["rows"] if "singlets" in r]
conv_txt = "; ".join("%s n=%d singlets %s/triplets %s: tau0* %.4f%+.4fi, c_min %+.4f%s" % (
    r["menu"], r["n"], r["singlets"], r["triplets"], r["tau0"][0], r["tau0"][1], min(r["c_coefs"]),
    "" if r["all_copies_heavy"] else " (LIGHT copy)") for r in conv_rows if r["triplets"] == "N")
cmp_rows = [r for r in cv["rows"] if "compare" in r and "(sup, N)" not in r["compare"].split(" vs ")[0]]
cmp_txt = "; ".join("%s n=%d %s: d_hyp(tau) %.3f, d_FS(S) %.3f" % (r["menu"], r["n"], r["compare"].split(" vs ")[0],
                                                                    r["tau_hyperbolic_distance"], r["direction_FS_distance"]) for r in cmp_rows)

sup_vals = {k: v["referee"] for k, v in sn.items()}
num = a0["numeric"]

report = {
 "verdict": "FAIL",
 "verdict_reading": (
  "FAIL for the claim as stated ('Yes: ... from two heavy copies on, as an isolated minimum, with one leading free number'). "
  "The mathematics underneath is sound and reproduces: gauge invariance of the H_d-type coupling, modular invariance with "
  "exponent = weight, the removal of S's phase, the Coleman-Weinberg structure, the decoupling-limit eigenvector, n = 2's "
  "Y1 x Y2 (and menu H's R), the symmetric configurations as saddles, and the a0 identity. What fails is the headline: it "
  "contradicts the plan's sealed reading at n = 2 and n = 3 (B1), its compression is a property of a post-hoc, continuous "
  "normalisation convention and of couplings set to zero that the exhibited symmetry allows (B2), and the field content is "
  "anomalous in the supersymmetric reading the potential needs, so 'the Higgs direction' is H_d's only (B3). A corrected "
  "claim (B1-B3 applied; mostly rewording plus one rerun with a stable F) could land as PASS."),
 "blocking": [
  {"item": "B1. The headline contradicts the plan's sealed reading; 'in the heavy regime' is a post-hoc restriction, and the n = 3 tally counts a configuration whose global minimum is not the isolated interior point.",
   "evidence": (
    "PLAN.md section 3 (sha256 4e2181fd..., hashed before the main runs): '\"tied ratios fix the direction\" means that the global "
    "minimum is isolated (section 3.4) for the n in question, at EVERY primary parameter point.' The draft's own section D on the "
    "primary grid: n = 2 has 3 of 20 points FLAT(1) (menu Z, mu^2 = 0.3, all three lambda v) -> n = 2 does not pass; n = 3 has "
    "H at (0.3, 1.0) unconverged (grad 1e-3) and Z at (0.3, 1.0) flagged by the draft itself as RUNAWAY, yet DESIGN counts the latter "
    "in 'isolated in 19/20' and in 'all 119 certified'. The referee confirms that runaway with a cancellation-free F and an mpmath "
    "arbiter at 30 digits: V = -0.0057202 at Im tau 10.38 below the interior point's -0.0043525 (t_runaway_stable.json). Under the "
    "sealed reading the first n that passes on the whole primary grid is n = 4 (sup/N convention): the referee's wider re-search "
    "(72 starts to Im tau 16, stable F, mpmath arbiter) undercuts none of the %d other primary configurations it re-ran (every n >= 3 point at (0.3, 1.0) "
    "whose interior V lay above the cusp's asymptotic bound, and the (0.5, 0.3) points for n = 1-8, both menus). DESIGN's headline instead says 'from two heavy copies on ... This holds in the heavy regime' -- a restriction "
    "absent from the plan, chosen after the results." % len(not_undercut_primary)),
   "fix": "Lead with the sealed verdict: n = 1 no (flat), n = 2 no (17/20; the three are light-copy valleys), n = 3 no (18/20 isolated global minima, one runaway, one unconverged), n = 4-8 yes in the sup/N convention. Present 'the heavy regime' as a post-hoc refinement, labelled so. Remove the runaway from every 'isolated' tally (19/20 -> 18/20; 119 -> 118 of 120)."},
  {"item": "B2. 'One leading free number (mu/M)' is a property of a post-hoc, CONTINUOUS normalisation convention plus couplings set to zero that the exhibited symmetry allows; in the source's convention and in a Petersson-type one the small-n result disappears, and the cusp-convention 'isolated n >= 4-5' is refuted.",
   "evidence": (
    "(a) The convention was set by a prototype scale table (PLAN.md's own disclosure). The singlets' sup norms span %.4g (eta^24) to %.4g "
    "(eta^8 E4^3) (t_supnorm.json, reproduced to 1e-14), so sup versus cusp normalisation changes relative masses^2 by up to ~1e9. "
    "(b) The decoupling-limit vacuum at mu^2 = 0.5, m0^2 = 0.005 under three canonical singlet conventions (t_conventions.json): %s. "
    "In the cusp convention (leading coefficient 1, the normalisation under which arXiv:2402.02071 ties its pairs) and in the "
    "Petersson-type L2 one (int_F (2y)^w |Y|^2 dmu = 1), every n computed (2-5, both menus) sits in the light-copy regime (c_i < 0), "
    "where DESIGN's own section 4.1 gives a flat valley at n = 2, not an isolated point. The cusp n = 3 point stops at the search's "
    "Im tau bound of 6, so it runs further into the cusp. Distances to the draft's vacuum: %s. The triplet convention alone (N -> cusp, same tau0*) rotates the n >= 3 direction by "
    "0.12-1.45 rad (Z n = 5: 1.45, nearly orthogonal) and the n = 2 direction by 0: the cross product is convention-free, as the draft says. "
    "(c) The draft's own cusp-convention section D: n = 1, 2 unconverged/unresolved at Im tau 4.12, n = 3 runaway, and the 'isolated' "
    "interior points at n >= 4 have V = +4.8 to +6.6, positive, far from every copy's level. The referee's stable re-search, with an "
    "mpmath arbiter, finds lower points IN THE SAME CONVENTION for: %s. So section 4.2's 'n >= 4-5: isolated' is false at least for Z n=4 and H n=5 "
    "(both labelled ISOLATED); n = 6-8 were not undercut within Im tau <= 16 (unresolved). "
    "(d) The convention is continuous: 3n - 2 hidden ratios (2n - 1 singlet ratios after M, n - 1 triplet ratios after lambda). The "
    "Jacobian of the decoupling-limit vacuum with respect to log mu^2 and the 3n log normalisation constants (t_dec_jacobian.json, "
    "central differences, each perturbed vacuum re-solved): %s. At finite lambda v (t_norm_jacobian.json, implicit-function theorem at "
    "the draft's vacua, Hessians positive in an independent exponential chart, smallest eigenvalue %.2g): %s. Per e-fold of a single "
    "constant the decoupling-limit vacuum moves up to 2.8 (hyperbolic and Fubini-Study combined), against mu^2's 0.02-1.2. "
    "(e) Under the draft's OWN exhibited weight/character assignment (checks_extra section 2: every copy k_L = 0, c_L = 0) the cross-copy "
    "terms carry exactly the weight and character of copy j's own terms: L_i Lbar_j (form Y_L,j) and H L_i Ebar_j (triplet Y3,j) are "
    "modular- and gauge-invariant for every i != j (t_cross_terms.json: n = 8: %s (Z), %s (H)); 'one block per copy' sets ~3n(n-1) "
    "invariant couplings to zero by choice. (f) The one-loop log divergence, STr M^4 proportional to m0^2 sum_i (2a_i^2 + d_i^2 + b_i^2), "
    "requires counterterms of exactly the singlet-mass and Q forms (m0^2 (2y)^w |Y|^2 and m0^2 lambda^2 (2y)^(3/2) |S^T Y3,i|^2), each "
    "separately invariant: 'one mu' is their universal finite part, a renormalisation condition (CHOSEN); non-universal parts shift the "
    "c_i of Q, i.e. act like (d)'s triplet ratios. The 'Kahler ambiguity' of section 6 is therefore not optional." % (
     min(sup_vals.values()), max(sup_vals.values()), conv_txt, cmp_txt, undercut_txt,
     dec_txt, hess_min, nj_txt,
     ", ".join("%s %d/%d" % (k, v["count"], v["off_diagonal_pairs"]) for k, v in ct["menu_Z"]["n8"].items()),
     ", ".join("%s %d/%d" % (k, v["count"], v["off_diagonal_pairs"]) for k, v in ct["menu_H"]["n8"].items()))),
   "fix": "Put the convention in the headline ('in the CHOSEN sup/N convention, with the cross-copy couplings and the non-universal counterterm parts set to zero'). Report the convention-free count (n = 2: 1 on a mirror line, 2 off; n >= 3: 3 on a mirror line, 6 off -- no compression). State that in the source's (cusp) and a Petersson-type convention every n computed (2-5) is light-copy at the decoupling point (no isolated vacuum at n = 2) and that the cusp-convention n >= 4 points are not global (Z n=4, H n=5 undercut). Either exhibit an assignment from the affine family that forbids the cross terms, or count them (CHOSEN = 0). Replace 'one leading number plus a discrete menu' by 'one leading number given a continuous CHOSEN convention'."},
  {"item": "B3. The field content is not consistent as the supersymmetric theory the potential presupposes; 'the Higgs direction fixed' is H_d's only.",
   "evidence": (
    "F(u) is the softly broken supersymmetric supertrace (two complex scalars at u + m0^2 per Dirac fermion at u; overall 1/16pi^2) and "
    "H is written in a superpotential (card: 'superpotential of copy i'). With only the Y = -1/2 triplet H (three doublet superfields), "
    "the Higgsinos give Tr Y^3 = 3 x 2 x (-1/2)^3 = -3/4, Tr(Y T^2) = -3/4 and Tr Y = -3, all non-zero, and an odd number of SU(2) "
    "doublets (SM 12 + vector-like 2n + 3): Witten's global anomaly. A Y = +1/2 triplet H_u is required. It brings its own CP^2 "
    "direction, tan beta and a relative phase. None is fixed here: H_u has no coupling in the construction; H_u Lbar E is "
    "gauge-invariant and its modular status is not examined. FR-FIB's single Higgs serves its up and down sectors (B1656; B1703), so "
    "using this vacuum for the frame needs H_u's direction identified with H_d's: an UNEARNED identification. In a non-SUSY reading "
    "instead, F's form needs scalar quartics tuned to the Yukawa (not RG-stable), and tree-level quartics invariant under the "
    "signed-permutation image of rho_R (e.g. sum_alpha (H_alpha^dag H_alpha)^2) depend on S at tree level and would dominate the "
    "one-loop selection unless CHOSEN zero. DESIGN section 5 nevertheless writes 'A consistent construction exists (P-518's four "
    "demands)' and section 6 treats the two-Higgs completion as optional."),
   "fix": "Declare the reading. If SUSY: add H_u, count its coordinates (4 + tan beta + a phase) as unfixed, or give it heavy couplings (more menu); label the up/down identification UNEARNED; replace 'a consistent construction exists' by 'gauge- and modular-invariant couplings for the H_d sector; the completion is required and not computed'. If non-SUSY: list the tuned quartics and the zeroed tree-level invariants as CHOSEN, and justify F."}
 ],
 "non_blocking": [
  {"item": "N1. The vacuum search is restricted to charge-preserving (aligned) vevs; the referee's charge-breaking test passes at every isolated vacuum, but the flat valleys extend into charge-breaking vevs.",
   "evidence": ("Three doublets' vev is a 3x2 matrix Phi; only K = Phi Phi^dag (rank <= 2, trace v^2) enters, beta_i = W_i^T K conj(W_i), so at fixed "
                "|v| the space is 7-dimensional, not CP^2 (4). Moving weight eps onto t (t perp S) changes V at first order by "
                "eps (t^dag H t - S^dag H S), H = sum_i Phi_i'(beta_i) conj(W_i) W_i^T. At all %d points the draft classifies as isolated (both conventions), S* is H's lowest "
                "eigenvector (smallest relative gap %.1e, %s), so they are stable to charge breaking (t_vacua.json). At the 24 degenerate "
                "points (all n = 1, and Z n = 2 at mu^2 = 0.3) H has a two-dimensional null space: the n = 1 vacuum is a 3-ball of density "
                "matrices (CP^1 its boundary), not a CP^1, and the light-copy n = 2 valley extends likewise." % (len(iso), gaps[0][0], gaps[0][1:])),
   "fix": "State the restriction and add the test (it passes); correct the n = 1 and light-copy valley dimensions."},
  {"item": "N2. The draft's double-precision F(u) is numerically wrong for large u: it returns exactly 0 for u >~ 1e14 and is 3-20% off at 1e12-1e13 (m0^2 = 0.003, mu^2 = 0.3).",
   "evidence": ("(u + m0^2) rounds to u, so the two terms cancel exactly: numpy F(1e14) = 0 against the exact 1.95e13; F(1e12) = 1.72e11 against "
                "1.67e11. Near the cusp the growing triplets give b^2 ~ 1e17 (t_probe_cusp.py: two copies at b^2 = 2.0e17 counted as F = 0), "
                "creating spurious low points. The referee's first wide re-search 'undercut' Z n=5 and n=7 (0.3, 1.0) this way; with the "
                "stable form F = (2u m0^2 + m0^4)(log(u/mu^2) - 3/2) + (u + m0^2)^2 log1p(m0^2/u) both disappeared. The draft's own runaway "
                "flags survive the stable F and the mpmath arbiter. Its 24 starts stop at Im tau 3.5, and runaway detection rests on the numpy "
                "search."),
   "fix": "Use the stable form, add starts deep in the cusp, and re-derive the runaway flags (the referee's t_runaway_stable.py does both)."},
  {"item": "N3. 'Never at i or omega: stationary for every parameter but never minima' was computed at one parameter point; the referee extends it to the grid.",
   "evidence": ("DESIGN section 4.3 used mu^2 = 0.5, lambda v = 0.3 only. The referee computed all nine primary (mu^2, lambda v) points and the cusp convention, menus Z and H, "
                "n = 1-8, at the four symmetric configurations (%d Hessians): every one has a negative direction (least negative smallest "
                "eigenvalue -0.31; t_sympoints.json). Separately, the cusp convention's n >= 6 interior points sit within 5e-3 of omega "
                "(0.4953 + 0.8687i), where E4 = 0 removes the E4-carrying singlets." % sym["total"]),
   "fix": "Scope the sentence to the grid computed."},
  {"item": "N4. The invariance test's resolution is ~1e-16, not 1e-33, and it cannot see characters; one of the four controls is doubly wrong.",
   "evidence": ("S is renormalised in double precision inside MPModel.recenter. Where unit(L^-1 S) differs from L^-1 unit(S) by 1 ulp, the deviation is ~1e-17 "
                "(referee's control run: 9.7e-18 at one of three points; 1e-33 at the other two). The quoted 2.5e-33 is real but partly the "
                "luck of rounding. Only moduli (|eta|) enter, so the test is blind to multipliers and characters; those rest on checks_extra "
                "section 2's arithmetic alone. Control (i), theta3^4 with exponent 4, is both a non-singlet and has the wrong exponent, so it "
                "shows the test can fail without isolating either property. Added control: the right couplings with the wrong action on S "
                "fail as they must (L instead of L^-1: %.2f (Z), %.2f (H); S left unchanged under T: %.2f / %.2f; under S: %.2f / %.2f)." % (
                    sa["menu_Z"]["T with L"], sa["menu_H"]["T with L"], sa["menu_Z"]["T with S unchanged"], sa["menu_H"]["T with S unchanged"],
                    sa["menu_Z"]["S-move with S unchanged"], sa["menu_H"]["S-move with S unchanged"])),
   "fix": "Quote the resolution; add the S-action control; replace control (i) by the correct singlet with a wrong exponent."},
  {"item": "N5. Overstated wording elsewhere.",
   "evidence": ("'the interaction's one-loop vacuum' (the heavy sector is CHOSEN, added by hand: P-415); 'six coordinates are fixed by one leading number plus a discrete "
                "menu' (the convention is continuous, B2); 'isolated in all 119 certified' (B1); 'n >= 4-5: isolated' in the cusp convention (B2c); "
                "'Q's lowest eigenvalue is simple ... gap ratio 0.008-0.44 in menu H': at 0.008 (H, n = 3) a perturbation of ~1% of Q's spread "
                "(two-loop, a counterterm, a Kahler term) rotates the direction by O(1); the decoupling-limit Jacobian gives up to 2.8 (combined "
                "hyperbolic/Fubini-Study) per e-fold of a singlet constant there."),
   "fix": "Reword as indicated; flag the small-gap cases as fragile."},
  {"item": "N6. Not listed among 'does not establish' (to add).",
   "evidence": ("(i) The light fields' own loops (the frame's Yukawa sector) also give S-dependent terms, of order y^4 v^4 log against the heavy "
                "sector's (lambda v)^2 m0^2 log; the direction is the heavy sector's only if m0 >> y v. Section 6 lists light loops for tau only. "
                "(ii) The two non-vacuum Higgs combinations are physical extra doublets, with masses^2 set by Q's other eigenvalues "
                "(~ lambda^2 m0^2 x 0.01-1 / 16pi^2). (iii) No relation is derived between M, the scale at which FR-FIB's frame is read, and v "
                "(|v| fixed by hand; v << M assumed). (iv) Menu H's n = 2 vacuum lies exactly on R, an isotropic direction with m1 = 0 identically "
                "(B1809): as a Higgs for the frame it gives a massless first generation. That is an outcome, not an aside."),
   "fix": "Add these to section 6."},
  {"item": "N7. Why the sup convention makes the small-n heavy regime generic, and two process notes.",
   "evidence": ("The sup convention caps every singlet's canonical mass at M. With mu^2 in [0.3, 0.8] M^2, every singlet therefore reaches its level "
                "u* ~ mu^2 somewhere in the fundamental domain, so c_i > 0 at small n is a property of the convention (B2), not of the forms. "
                "Process: (a) 'Seen first' records no literature search on the bench, yet the draft calls directions 'new' and cites the Kahler "
                "ambiguity from memory (WORKING_RULES, 2026-10-02: the literature leg is required before 'new'). (b) The plan's flat/isolated "
                "criterion was replaced after the runs (disclosed); summary.txt prints both readings, and they differ at several points."),
   "fix": "Say it in section 6; add the literature line (e.g. the Kahler-ambiguity papers of modular flavour symmetry) or drop 'new'."},
 {"item": "N8. What survives (reproduced by the referee).",
   "evidence": ("Gauge invariance of lambda (H^T Y3) L Ebar with Y_H = -1/2 (H_d-type; with the SM-normalised Y = +1/2 Higgs, the holomorphic invariant would be H Lbar E). "
                "Exponent = weight for every form; invariance rerun from a copy. The charged matrix [[a, b], [0, d]] (rows L^-, E; columns "
                "Lbar^+, Ebar) and the neutral a; singular values depend on |a|, |b|, |d| only; copies share no fields, and with cross-copy H L_i "
                "Ebar_j terms the phase is still a gauge rotation. V over the 3n heavy states, neutral included; supertrace signs right. "
                "V = V0 + (lambda v)^2 S^dag Q S + O((lambda v)^4) with c_i = (G(a^2) - G(d^2))/(a^2 - d^2), re-derived. n = 2: S* = Y1 x Y2 at "
                "all 17 isolated vacua (FS <= 1e-16, independent forms), and menu H's S* proportional to R(tau*) (R.R, R.DR <= 1e-30). Hessians "
                "positive definite in an independent chart at 35 vacua. n = 2's direction is a covariant section of tau*, so its cost is tau* "
                "alone: rank 1 on a mirror line even with every normalisation free -- the one robust compression in the draft."),
   "fix": "Keep these as the arc's computed core."}
 ],
 "reruns": (
  "All 23 draft artefacts match ARTIFACT_HASHES.txt's final block (sha256). Copied model.py, search.py, step_a_v2.py, checks_extra.py and "
  "the rest to referee/rerun/ and ran python3 -I under nice 10, OMP_NUM_THREADS=1 (Python 3.12.1, numpy 2.4.0, scipy 1.16.3, mpmath 1.3.0), "
  "at most four cores. Section B's JSON is identical; checks_extra.json is identical. Section A: controls identical (0.809, 0.642, 0.339, "
  "2.785; positive 9.1e-34), worst 2.55e-33 (Z) and 2.34e-33 (H) against the draft's 2.55e-33 and 2.38e-33. "
  "The referee also wrote an independent implementation (ref_model.py: theta series in tau; E2, E4, E6 by Lambert series; Dedekind eta by "
  "the product; DR by numerical differentiation; the charged spectrum by an SVD). Its forms agree with model.py to <= 6e-29 (E6) and "
  "<= 2e-30 otherwise; its sup norms to 1e-14; V at all 176 reported vacua to <= %.1e relative. New computations: the charge-breaking "
  "test at 176 vacua; Hessians in an exponential chart (35); normalisation Jacobians at finite lambda v (35) and in the decoupling "
  "limit (14); a convention comparison (sup / cusp / L2 x N / cusp, n = 2-5, both menus); a global-minimum re-search with a "
  "cancellation-free F (40 configurations, 24 draft-seeded plus 48 wide starts each, an mpmath arbiter); the symmetric configurations "
  "on the whole grid (640); the cross-term enumeration; the a0 identity (exact q-series in B1691's machinery, numerics, a hand proof); "
  "and the S-action controls. Scripts and outputs are in referee/ (t_*.py -> t_*.json, *_run.txt)." % vac["max_V_rel_dev"]),
 "free_numbers_honest_count": (
  "Within the draft's CHOSEN inputs (sup/N/24DR convention; cross-copy couplings zero; universal counterterm finite parts; minimal Kahler; "
  "H_d only; charge-preserving vevs): ONE leading number (mu/M) in the decoupling limit; m0^2/mu^2 sub-leading (~1%); lambda v as (lambda v)^2. "
  "At finite lambda v, n >= 3: rank 3 (mu, m0, lambda v), as the draft says. "
  "Counting the convention as the continuous data it is (3n - 2 ratios), the leading-order vacuum's rank is: n = 2: 1 on a mirror line "
  "(robust: the direction is the section Y1 x Y2 of tau*) and 2 off one; n >= 3: 3 on a mirror line, 6 off one, i.e. no compression "
  "(computed: n = 5, both menus; finite lambda v n = 5, 6, 8 off-line, both menus). Set to zero by choice on top: ~3n(n-1) invariant "
  "cross-copy couplings, 3n - 1 non-universal counterterm parts, and the H_u sector (at least 4 + 2 real coordinates, unfixed). In the "
  "source's (cusp) convention n = 2 and 3 have no isolated vacuum, and the interior points at n = 4 (both menus) and H n = 5 are not global minima. Honest summary: '1, given a CHOSEN continuous convention and zeroed invariant "
  "couplings; 1-2 for n = 2 without it; 3-6 for n >= 3 without it; plus the unfixed H_u direction'."),
 "a0_identity": (
  "CORRECT, as an identity with the Dedekind eta: a0 := D^2 R - E4 R/48 (B1697; Serre derivative D_k = q d/dq - (k/12) E2, q = e^{2 pi i tau}; "
  "R = (-th2^2, -th4^2, i th3^2)/(th2 th3 th4)) equals (1/48)(th2 th3^3 th4^3, th2^3 th3^3 th4, i th2^3 th3 th4^3) = (1/48)(th2 th3 th4)^3 (th2^-2, th4^-2, i th3^-2) "
  "= (eta^9/6)(th2^-2, th4^-2, i th3^-2) = eta^4 F_-2/6, with F_-2 = eta^5 (th2^-2, th4^-2, i th3^-2) (B1730, eps = +1) and eta^3 = th2 th3 th4/2. "
  "Componentwise, a0_k = (1/48) x (-th3^4 th4^4 R_1, -th2^4 th3^4 R_2, th2^4 th4^4 R_3)_k. "
  "Exact check in B1691's own q-series machinery (copied): all three components agree to x^200 = q^25 (leading terms q^(1/8)/24, q^(3/8)/6, i q^(3/8)/6). "
  "Numerical check: the ratio a0/(eta^4 F_-2) = 1/6 to <= 1e-30 at five tau, including Re tau = 1.7 and -2.3 (t_a0.json). "
  "Proof (the referee's, elementary): with D log th2 = (E2 + th3^4 + th4^4)/24, D log th3 = (E2 + th2^4 - th4^4)/24 and "
  "D log th4 = (E2 - th2^4 - th3^4)/24 (verified to 1e-32), write A = th2^4, B = th3^4, C = th4^4 (B = A + C). Then D R_1 = R_1 (B + C)/12 and "
  "D^2 R_1 - E4 R_1/48 = R_1 [2(B + C)^2 + 4(AB - AC - 2BC) - 3(A^2 + B^2 + C^2)]/288 = -R_1 BC/48. Likewise -R_2 AB/48 and +R_3 AC/48. "
  "Only t = -1/48 collapses the bracket to a monomial. "
  "The draft's proof sketch is right in outline but omits its crux: 'bounded at the cusps' holds because -1/48 cancels the q^(-1/8) term of "
  "components 2 and 3 (B1697's unit), and the constant 1/6 follows from the leading terms (q^(1/8)/24 against q^(1/8)/4). Equivalently, "
  "B1697's uniqueness (the weight-7/2 rho_R section without end data is one line) contains eta^4 F_-2. "
  "Main's mismatch is a convention for F_-2, not a failure. If 'F_-2' was B1810's direction function (th2^-2, th4^-2, i th3^-2), which has no eta^5, "
  "the scalar is eta^9/6 = (th2 th3 th4)^3/48. Its ratio to eta^4/6 is eta^5: 0.195+0.044i at tau = 0.17+1.23i. If F_-2 was built with model.py's "
  "|eta|^5, the scalar is eta^9/(6|eta|^5) = (|eta|^4/6) e^{9i arg eta}: ratio 0.922+0.387i there. With one eta used consistently in F_-2 and in "
  "the comparison (any cube-root branch), the ratio is exactly eta^4/6. "
  "Consequence confirmed: a0 and F_-2 are one direction at every tau, so B1810's thirteen declared directions are twelve distinct ones. At "
  "tau = i B1810 already has further coincidences (there a0's outputs equal F_6's through B1810's kappa -> 2/kappa symmetry)."),
 "files": "referee/: ref_model.py, ref_helpers.py, qseries_B1691_copy.py, t_forms.py, t_supnorm.py, t_vacua.py, t_cusp_bound.py, t_runaway.py (superseded by t_runaway_stable.py: its 'undercuts' of Z n=5, 7 were the F-cancellation artefact), t_runaway_stable.py, t_probe_cusp.py, t_norm_jacobian.py, t_dec_jacobian.py, t_conventions.py, t_sympoints.py, t_cross_terms.py, t_n2_cross.py, t_controls_S_action.py, t_a0.py; outputs t_*.json and *_run.txt; rerun/ holds the copied draft code and its rerun outputs."
}
(HERE / "REPORT.json").write_text(json.dumps(report, indent=1, ensure_ascii=False))
print("written REPORT.json;", len(report["blocking"]), "blocking,", len(report["non_blocking"]), "non-blocking")
