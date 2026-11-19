"""B940 -- what produces the +- pairing (P-540, 2026-11-19): pairing_source.py run live equals its committed output, every
identity holds and every control fails (a check that can fail: the wrong matrix in U, the wrong translation, no
conjugation in the cocycle)."""
import pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B940_dirac_sealed"


def test_the_pairing_source_live():
    out = subprocess.run([sys.executable, "-B", str(A / "pairing_source.py")], capture_output=True, text=True, check=True).stdout
    assert out == (A / "pairing_source_run.txt").read_text(encoding="utf-8")
    assert out.strip().endswith("ALL HOLD: True")
    for k in ("'A_to_A': True", "'B_to_BAB': True", "'g_conj_g_is_A': True", "'minus_B_to_rho2_word': True",
              "'control_x_conj_fails': True", "'control_no_g_fails': True", "'U_D_plus_D_U_is_zero': True",
              "'control_identity_in_place_of_sigma2_fails': True", "'control_sigma1_fails': True", "'control_sigma3_fails': True",
              "'sigma2_k_sigma2inv_is_conj_k': True", "'s_of_reflection_is_conj_s': True", "'s_of_translate_is_g_s': True"):
        assert k in out, k
    assert "(P-540, checked by main; `pairing_source.py`" in (A / "FINDINGS.md").read_text(encoding="utf-8")
