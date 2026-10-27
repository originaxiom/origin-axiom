"""B1757 -- step 2's free doublets at the strip, the vectors committed.  The committed run reproduces step 2's eight
chi2_nine values; every vector is normalised with its largest component real and positive; both doublets sit near the
null line (0, 1, i)/sqrt2."""
import json, math, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1757_step_twos_free_doublets_at_the_strip" / "verification"
STEP2 = [19.08, 45.85, 4.05, 37.97, 29.17, 45.47, 2.75, 29.37]


def test_the_committed_fits():
    d = json.loads((A / "free_doublets.json").read_text(encoding="utf-8"))
    assert [round(r["chi2_nine"], 2) for r in d] == STEP2
    for r in d:
        for key in ("H_u", "H_d"):
            v = [complex(a, b) for a, b in r[key]]
            assert abs(sum(abs(z) ** 2 for z in v) - 1) < 1e-9
            k = max(range(3), key=lambda i: abs(v[i])); assert abs(v[k].imag) < 1e-12 and v[k].real > 0
            assert abs(v[0]) < 0.2 and min(abs(v[1]), abs(v[2])) > 0.68          # near (0, 1, i)/sqrt2 up to phase
