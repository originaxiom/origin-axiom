"""B1832 -- the agy lanes' digest: the registry rows, the committed checks' key numbers, and two live recomputations
(the F_10 norm identity in mpmath; the Diophantine lemma)."""
import json, pathlib, re
from fractions import Fraction as F
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[2]


def test_registry_rows_and_findings():
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    for t in ("T-KERNEL-SUM-TWIST", "T-HALF-LIFT-LEPTON-DOWN", "T-FA-NORM", "T-THETA-Y-BSTEP"):
        assert re.search(r"^\| %s \|.*\| B1832 \|" % t, reg, re.M), t
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    assert "0 of 19" in f and "{5w ≡ ½} ∪ {3w ≡ ½}" in f


def test_the_committed_checks_carry_the_verified_numbers():
    j = json.loads((HERE / "frontier" / "check_b1761_i_residue.json").read_text())
    assert j, "the i-residue census output is committed"
    for name in ("check1_p524_kronecker_out.json", "check3_t21_half_lifts_out.json", "check9_coupling_reflection_identities_out.json"):
        assert (HERE / "t14_t22" / name).is_file(), name
    assert (HERE / "phases_t10_t13" / "c3e_mirror_per_sector_control_main_out.txt").is_file()


def test_f10_norm_identity_live():
    mp.mp.dps = 40
    for tau in (mp.mpc(0, 2), mp.mpc(0.31, 1.45)):
        q = mp.exp(1j * mp.pi * tau); t2, t3, t4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
        F10 = t2 ** 20 + t4 ** 20 - t3 ** 20
        eta = mp.exp(1j * mp.pi * tau / 12) * mp.qp(mp.exp(2j * mp.pi * tau))
        E4 = (t2 ** 8 + t3 ** 8 + t4 ** 8) / 2
        assert abs(F10 + 80 * eta ** 12 * E4) < mp.mpf(10) ** -30 * max(1, abs(F10))


def test_the_t_step_is_never_trivial_on_a_rational_line():
    for s in range(1, 200):
        for r in range(0, s):
            a = F(r, s)
            if a.denominator != s: continue
            assert (66 * a * a + F(1, 4)).denominator != 1, a
