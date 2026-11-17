"""B1952's lock: the stored output of wa2_on_main.py, and its exact parts recomputed live."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
D = json.loads((HERE / "wa2_on_main.json").read_text())


def test_only_five_has_one_fixed_line_and_the_lines_are_the_weyl_operators():
    assert D["A_primes_with_one_fixed_line"] == [5] and D["A_rule_holds_below_2000"] is True
    b = D["B"]
    assert b["linear"] is True and b["equals_record"] is True and b["offdiag_HS"] < 1e-12
    assert b["M_T"] == [[1, 4], [0, 1]] and b["M_S"] == [[0, 1], [4, 0]]


def test_the_zero_modes_carry_the_module_and_split_three_plus_two():
    c = D["C"]
    assert max(c["Z"], c["X_common_factor"], c["parity"]) < 1e-20 and c["rank"] == 5 and c["split"] == [3, 2]


def test_families_and_colour_are_at_coprime_levels():
    d = D["D"]
    assert [round(8 * x) for x in d["higgs_T_phases"]] == [1, 3, 7] and max(abs(8 * x - round(8 * x)) for x in d["higgs_T_phases"]) < 1e-5
    assert d["weil_T_phases"] == ["0", "2/5", "3/5"] and d["anticommute"] < 1e-12 and d["units_square_to_minus_one"] < 1e-12
    f = D["F"]
    assert f["a_permutation_up_to_phases"] is True and f["null_singular_value"] < 1e-10 < 1e-3 < f["next_singular_value"]
    assert f["other_transport_null"] > 1e-3 and f["unitary_defect"] < 1e-9
    assert [round(4 * g) for g in f["eigenphase_gaps"]] == [1, 1, 2] and max(abs(4 * g - round(4 * g)) for g in f["eigenphase_gaps"]) < 1e-4


def test_the_rivals_anomalies_recomputed_live():
    from fractions import Fraction as Fr
    from math import comb

    def an(p):
        m, n = (p + 1) // 2, (p - 1) // 2; ym, yn = Fr(p - 1, 2), -Fr(p + 1, 2); s1 = s3 = am = Fr(0)
        for k1 in range(m + 1):
            for k2 in range(n + 1):
                if (k1 + k2) % 2 == 0:
                    y = k1 * ym + k2 * yn; dd = comb(m, k1) * comb(n, k2); s1 += dd * y; s3 += dd * y ** 3
                    if 1 <= k1 <= m - 1: am += y * Fr(comb(m - 2, k1 - 1), 2) * comb(n, k2)
        return s1, s3, am
    assert an(3) == (0, 6, Fr(-1, 2)) and an(5) == (0, 0, 0) and an(7) == (0, 0, 0) and an(13) == (0, 0, 0)
    assert [D["E"][p][6] for p in ("3", "5", "7", "11", "13")] == [0, 1, 0, 2, 0]
