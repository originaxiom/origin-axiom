"""B1634 -- the sealed instrument unchanged; at length 12 <L, R> meets the inner automorphisms only in conj(c^+-1), never conj(a),
conj(b); every lift of a word fixing tau is a scalar; the residual at i is a plane and a line, at omega three lines; the weave's
lifts (move products, H_1's convention) satisfy the Mp2(Z) relations unrescaled and equal rho_theta exactly; chi_{3/2} = 0 by
the formula and by the independent count.  Bite controls: the helper's sign on S~ breaks the relations; mpmath's nome-based
theta_2 fails the T law at a wrapped point where the direct series holds."""
import cmath, hashlib, json, math, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1634_w50_on_main"
P13 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=complex); P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
rS = cmath.exp(-23j * math.pi / 4) * P13
rT = cmath.exp(7j * math.pi / 4) * np.diag([1j, 1, 1]) @ P23


def test_sealed_unchanged_and_graded():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 478abc379")
    assert hashlib.sha256(open(ARC / "verification" / "w50_on_main.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(ARC / "verification" / "sealed_run" / "w50_on_main.json"))
    assert d["V1"]["classified"]["id"] == d["V1"]["words_with_H1_identity"] == 325
    assert d["V2"]["lifts_all_scalar"]
    assert d["V3_theta_law_checks"][0]["T_rel_err"] > 0.5 > 1e-12 > d["V3_theta_law_checks"][1]["T_rel_err"]
    assert d["V3"]["n_equivalences"] == 8 and all(e["theta3_to"] == [-1, -1] for e in d["V3"]["equivalences"])
    assert abs(d["V4"]["chi_3_2"]) < 1e-9 and d["V4"]["chi_23_2"] >= 1
    assert json.load(open(ARC / "arc_verdict.json"))["verdict"] == "PROVED"


def test_post_seal_facts():
    p = json.load(open(ARC / "verification" / "post_seal_w50.json"))
    assert p["P1"]["sealed_failures_are_exactly_the_wraps"] and p["P1"]["direct_max_error"] < 1e-12
    c = p["P2"]["classified"]["+I"]
    assert c == {"id": 1944, "conj(c)": 196, "conj(c^-1)": 196}
    assert p["P2"]["word_lift_nonscalar"] == {"+I": 0, "-I": 0} and p["P2"]["braid_relation_on_move_matrices_max_defect"] < 1e-12
    at_i, at_w = p["P3"]["i: Delta^-1 = R L^-1 R"], p["P3"]["omega: L R^-1 (order 6 in SL2Z)"]
    assert at_i["order_on_T"] == 8 and sorted(e["dim"] for e in at_i["eigenspaces"].values()) == [1, 2]
    assert at_w["order_on_T"] == 12 and all(e["dim"] == 1 for e in at_w["eigenspaces"].values())
    assert all(r["dim_M_k(rho_theta)"] == round(r["chi_k_formula"]) for r in p["P4"])
    assert [r["dim_M_k(rho_theta)"] for r in p["P4"]] == [0, 0, 1, 1, 2, 2, 3, 3]
    six = p["P6"]
    assert six["M_of_sign_vs_move_product"] == {"L": "+", "R": "+", "S~": "-"}
    assert six["relations_exact_unrescaled"] and six["S8_is_I"] and six["monomial"]
    assert six["intertwiner_to_rho_theta_smallest_singular_value"] < 1e-10 and six["theta3_to"] == [-1, -1]
    assert six["allowed_3_2"] and not six["dual_allowed_3_2"] and abs(six["chi_3_2"]) < 1e-9


def test_rho_theta_relations_and_the_sign_bite():
    assert np.allclose(rS @ rS, np.linalg.matrix_power(rS @ rT, 3)) and np.allclose(np.linalg.matrix_power(rS, 8), np.eye(3))
    assert not np.allclose((-rS) @ (-rS), np.linalg.matrix_power((-rS) @ rT, 3))       # the helper's sign breaks it


def test_theta_law_branch_bite():
    import mpmath as mp
    mp.mp.dps = 25
    t = mp.mpc(0.4, 1.1)
    def direct(t, N=30):
        e = lambda x: mp.exp(1j * mp.pi * t * x)
        th = (mp.fsum(e((n + mp.mpf(1) / 2) ** 2) for n in range(-N, N)), mp.fsum(e(n * n) for n in range(-N, N + 1)),
              mp.fsum((-1) ** abs(n) * e(n * n) for n in range(-N, N + 1)))
        eta = mp.exp(1j * mp.pi * t / 12) * mp.fprod(1 - mp.exp(2j * mp.pi * t * n) for n in range(1, 120))
        return np.array([complex(eta ** 21 * x ** 2) for x in th])
    def nome(t):
        q = mp.exp(1j * mp.pi * t); eta = mp.exp(1j * mp.pi * t / 12) * mp.qp(mp.exp(2j * mp.pi * t))
        return np.array([complex(eta ** 21 * mp.jtheta(n, 0, q) ** 2) for n in (2, 3, 4)])
    for F, ok in ((direct, True), (nome, False)):
        err = np.abs(F(t + 1) - rT @ F(t)).max() / np.abs(rT @ F(t)).max()
        assert (err < 1e-12) == ok
