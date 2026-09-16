"""B1366 lock (seconds): every A2 of E6 is Weyl-conjugate (120, one orbit), every commuting (A2, A1) pair too (720, one orbit), exactly
three hypercharges realise a Standard-Model generation on the 27 and the residual su(3)_R permutes them; for each, the 27's two SM
singlets are an SU(2)_beta doublet with equal U(1)' charge and the 78's SM singlets are U(1)'-neutral."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1366_the_sign_is_e6s" / "verification"


def test_the_standard_model_embeds_in_e6_once_and_the_sign_theorem_is_universal():
    out = subprocess.run([sys.executable, str(VER / "sm_in_e6.py")], capture_output=True, text=True, timeout=900).stdout
    assert "(1) A2 root subsystems of E6: 120; Weyl orbits: 1 (sizes [120])" in out
    assert "centraliser of su(3)_c: 12 roots forming 2 A2's" in out
    assert "those with 27 -> 6 x 2 + 15 x 1 (a root su(2)_L): 6 (all of them: True)" in out
    assert "pairs (A2, A1 commuting): 720; Weyl orbits: 1" in out
    assert "with the Standard Model's multiset on the 27: 3 (one per choice of e^c among the three colour-weak singlets)" in out
    assert "permute the 3 hypercharges among themselves: True -> one embedding up to conjugacy" in out
    assert "the U(1)' D-term has one sign on all E6-charged SM singlets of 27s and 78s: True" in out
