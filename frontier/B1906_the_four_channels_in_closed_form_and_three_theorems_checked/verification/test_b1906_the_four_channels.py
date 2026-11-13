"""B1906's lock. It recomputes, with the arc's own functions (imported, not copied), the identity at fresh points, the
residues, the zero law of the residues, P-268's pairing exactly, two lines of the census on Re tau = 0, Theorem C whole
and Theorem A's level-1 statement in its lighter form; each with a planted wrong form that must fail. It then holds the
page and the verdict line to the numbers the kept outputs give. It writes nothing."""
import sys, json, re, random, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
sys.path.insert(0, str(HERE))
_argv = sys.argv; sys.argv = ["x"]
import the_duplication_identity as E
import the_zero_law_on_every_line as Z
import theorem_c_on_main as C
import level_one_on_main as L
sys.argv = _argv
import mpmath as mp

PAGE = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
VERDICT = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
def flat(s): return re.sub(r"\s+", " ", s)

def test_the_identity_holds_at_fresh_points_and_three_wrong_forms_fail():
    mp.mp.dps = 25
    rnd = random.Random(1906)
    pts = [E.random_point(rnd) for _ in range(5)]
    assert max(E.max_rel(E.P_main(*p), E.P_formula(*p)) for p in pts) < mp.mpf(10) ** -18
    for plant in ("no_half_b", "e_of_y", "no_half_in_a_minus"):
        assert max(E.max_rel(E.P_main(*p), E.P_formula(*p, plant=plant)) for p in pts) > mp.mpf(10) ** -3, plant

def test_the_residues_are_the_products_of_two_theta_constants():
    mp.mp.dps = 25
    rnd = random.Random(19061)
    for _ in range(2):
        x, y, u, t = E.random_point(rnd)
        Rf, Rc = E.R_formula(x, y, t), E.R_contour(x, y, t)
        sc = max(abs(v) for v in Rf.values())
        assert max(abs(Rf[s] - Rc[s]) for s in Rf) / sc < mp.mpf(10) ** -15
        assert abs(sum(v ** 2 for v in Rf.values())) / sc ** 2 < mp.mpf(10) ** -15          # Z2: the rank-one residue

def test_the_zero_law_of_every_residue_on_the_lines_of_order_up_to_six():
    mp.mp.dps = 25
    agree, disagree, zmax, nzmin = E.zero_law_census(mp.mpc("0.41", "1.37"), max_order=6)
    assert disagree == 0 and agree > 0 and zmax < mp.mpf(10) ** -18 and nzmin > mp.mpf(10) ** -6
    # a planted wrong law (the minus twist left out) disagrees somewhere
    saved = E.predicted_zero
    try:
        E.predicted_zero = lambda a, b, ql, qr, s: E.mod1((Fr(ql + qr) * a, Fr(ql + qr) * b)) == E.HS[s]
        assert E.zero_law_census(mp.mpc("0.41", "1.37"), max_order=6)[1] > 0
    finally:
        E.predicted_zero = saved

def test_b1703_and_b1701_follow():
    assert all(E.predicted_zero(a, b, E.B.SIXY[l], E.B.SIXY[r], "1") for (a, b) in E.lines(3) for (l, r) in E.SECT.values())
    tied = [(Fr(j, 6), Fr(k, 6)) for j in range(6) for k in range(6) if E.tied(Fr(j, 6), Fr(k, 6))]
    assert len(tied) == 27
    assert all(E.predicted_zero(a, b, E.B.SIXY[l], E.B.SIXY[r], E.tied(a, b)) for (a, b) in tied for (l, r) in E.SECT.values())

def test_p268s_pairing_is_plus_or_minus_i_exactly_on_every_line_it_applies_to():
    law, ok, bad, both_zero = E.pairing_law()
    assert bad == 0 and ok == 2 * law and law > 0
    planted = dict(E.KAPPA); planted["k"] = (Fr(0), False)             # channel k's constant turned by a quarter
    assert E.pairing_law(kappa=planted)[2] > 0

def test_two_lines_of_the_census_on_re_tau_zero():
    zero = Z.on_line(Fr(1, 12), Fr(1, 12), "up", complex(0, 1.3), True)      # 12 alpha and 12 beta odd: a zero
    other = Z.on_line(Fr(1, 12), Fr(2, 12), "up", complex(0, 1.3), True)     # 12 beta even: not a zero
    assert zero[0] is True and zero[1] < 1e-10 and zero[3]
    assert other[0] is False and other[1] > 1e-4 and other[3]

def test_theorem_c():
    OUT, _ = C.run()
    assert OUT["C1_commutant_V"] == 1 and OUT["C1_commutant_V_plus_V_plus_V"] == 9 and OUT["C1_commutant_chi_plus_chibar_times_3"] == 18
    assert OUT["C2_orbit_size"] == 3 and OUT["C2_image_order"] == 6
    assert OUT["C3_group_order"] == 24 and OUT["C3_degrees_of_the_rest_all_solutions"] == [[2, 2, 2, 3]]

def test_theorem_a_level_one():
    OUT, _ = L.run(lock=True)
    assert OUT["A1_sigma_one"] == ["A6", "D6", "E6"] and OUT["A2_sigma_one_and_three_primaries"] == ["E6"]
    assert OUT["A3_SL2_Z4_involutions"] > 1 and OUT["A3_2O_elements_whose_square_is_1_other_than_1"] == 1

def test_the_page_and_the_verdict_line_hold_the_kept_outputs():
    e = json.loads((HERE / "the_duplication_identity.json").read_text(encoding="utf-8"))
    z = json.loads((HERE / "the_zero_law_on_every_line.json").read_text(encoding="utf-8"))
    agree = e["E2_residue_zero_law_agree_disagree"][0]
    pairs = e["E4_pairs_with_ratio_plus_minus_i"]
    page, line = flat(PAGE), VERDICT["claim_one_line"]
    assert e["E2_residue_zero_law_agree_disagree"][1] == 0 and e["E4_pairs_not"] == 0
    assert "{:,} of {:,}".format(agree, agree) in page and "{:,} of {:,}".format(agree, agree) in line
    assert "{0} of {0}".format(pairs) in line and "{0} pairs".format(pairs) in page
    counts = [v["agree"] for v in z["census"].values()]
    assert len(set(counts)) == 1 and all(v["disagree"] == 0 for v in z["census"].values())
    assert "{0} of {0}".format(counts[0]) in page and "{0} of {0}".format(counts[0]) in line
    split = z["P292_split_lines_and_zeros"]
    assert all(v["12b_odd"][0] == v["12b_odd"][1] == 16 and v["12b_even"][1] == 0 for v in split.values())
    assert "16 order-12 lines with 12α odd and 12β odd" in page and "16 order-12 lines with 12 alpha and 12 beta odd" in line
