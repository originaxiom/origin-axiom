"""B1387 lock -- THE INDEX COMPUTED: the L^2 harmonic representative of cube~3.24's cuspidal, isometry-invariant class v+ (B1386), by
a Hejhal-type solve on SnapPy's developed fundamental polyhedron.  A K_n = 6 solve (seconds): full rank, v+ vanishing on every
parabolic, the member's symmetries reproduced without being imposed (the rotation's equal magnitudes and the swap's equal
chart-invariant coefficient at cusps 0 and 3; the killed first shells at cusps 1 and 2; the real triple phase of the -I at cusp 2),
the partitions (chi = -1 at both Eisenstein cusps, annular at the other two) and the index N(v+) = +-2.  The run record carries
K_n up to 14 and the chart, height and seed variations."""
import importlib.util
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1387_the_index_computed" / "verification"


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, VER / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_index_computed():
    HF = _load("b1387_harmonic_cusp_form", "harmonic_cusp_form.py")
    M = HF.member()
    S, x, st = HF.solve(M, 6, 0.10)
    assert st["full rank"] and st["fit residual rms"] < 1e-2 and st["v on the parabolics (max)"] < 1e-12
    assert st["lowest pulled-back height"] > 0.10
    rows, N = HF.analyse(S, x)
    assert abs(N) == 2
    chis = [rows[c]["chi(d+)"] for c in range(4)]
    assert chis[0] == chis[3] and abs(chis[0]) == 1 and chis[1] == 0 and chis[2] == 0
    for c in (0, 3):                                      # the rotation (equal magnitudes) and the swap (equal chart invariants)
        mags = rows[c]["|c| sqrt(covol)"]
        assert rows[c]["vectors"] == 6 and max(mags) - min(mags) < 0.01 and abs(sum(mags) / 3 - 1.007) < 0.01
        assert abs(rows[c]["cos of the triple phase"] - 0.370) < 0.01
    for c in (1, 2):                                      # the first shell killed by R's translation, found ~0 without being told
        assert len(rows[c]["killed shells before the leading one (max |c| s)"]) == 1
        assert rows[c]["killed shells before the leading one (max |c| s)"][0] < 5e-3
    assert rows[1]["vectors"] == 2 and abs(rows[1]["|c| sqrt(covol)"][0] - 1.789) < 0.02
    mags2 = sorted(rows[2]["|c| sqrt(covol)"])
    assert rows[2]["vectors"] == 6 and abs(mags2[2] - 2.209) < 0.02 and mags2[1] < 0.35 and abs(rows[2]["cos of the triple phase"] - 1) < 1e-3
