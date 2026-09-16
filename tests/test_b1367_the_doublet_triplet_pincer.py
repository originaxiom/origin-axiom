"""B1367 lock (seconds): the E6 cubic in trinification form pairs N with (H_u, H_d) and (D, Dbar) and nu^c with (L, H_u) and (D, d^c)
with equal magnitudes; over n = 3, 4, 6 copies, fifteen coupling patterns and every VEV support, light up-Higgs doublets equal light
exotic triplets and every vacuum with a Higgs has a light D."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1367_the_doublet_triplet_pincer" / "verification"


def test_light_higgs_doublets_equal_light_exotic_triplets_for_every_e6_symmetric_vacuum():
    out = subprocess.run([sys.executable, str(VER / "pincer.py")], capture_output=True, text=True, timeout=900).stdout
    assert "N H_u^1 H_d^2 = +0.167+0.000j, N H_u^2 H_d^1 = -0.167+0.000j, N H_u^1 L^2 = +0.000+0.000j" in out
    assert "N D_1 Dbar_1 = +0.167+0.000j, N D_1 d^c_1 = +0.000+0.000j" in out
    assert "nu^c L^1 H_u^2 = +0.167+0.000j, nu^c H_d^1 H_u^2 = +0.000+0.000j" in out
    assert "nu^c D_1 d^c_1 = +0.167+0.000j, nu^c D_1 Dbar_1 = +0.000+0.000j" in out
    assert "n = 3: configurations 960; light H_u != light D: 0; configurations with a light H_u: 193, minimum light D among them: 1; configurations with a light H_u, no light D and >= 4 light Y = -1/2 doublets: 0" in out
    assert "n = 4: configurations 3840; light H_u != light D: 0" in out
    assert "n = 6: configurations 4500; light H_u != light D: 0" in out
    assert "every vacuum with a Higgs has a light D: True" in out
