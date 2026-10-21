"""B1693 -- B1692's bound against the measured masses (P-241), sealed aa36d2667. Live: the comparison re-run from the
pinned data (its hash checked) reproduces the stored grades; the bite: with a bound of 16 instead of 4 T1 is no longer
excluded. Stored: the seal's hashes."""
import hashlib, importlib.util, io, contextlib, json, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1693_the_bound_against_the_masses"


def _m():
    spec = importlib.util.spec_from_file_location("b1693_compare", A / "verification" / "compare.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


def test_the_comparison_live_with_the_bite():
    m = _m(); stored = json.loads((A / "verification" / "comparison.json").read_text(encoding="utf-8"))
    assert m.out["T1_one_Higgs"]["grade"] == stored["T1_one_Higgs"]["grade"] == "EXCLUDED"
    assert m.out["T2_down_lepton"]["grade"] == stored["T2_down_lepton"]["grade"] == "ALLOWED"
    assert abs(m.out["T1_one_Higgs"]["S"] - 15.977) < 1e-2 and abs(m.out["T2_down_lepton"]["S"] - 3.144) < 1e-2
    assert m.out["T1_one_Higgs"]["lower_3sigma"] < 16                                  # the bite: a bound of 16 would allow it


def test_the_seal():
    h = hashlib.sha256((A / "verification" / "compare.py").read_bytes()).hexdigest()
    assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert hashlib.sha256((A / "PREREGISTRATION.md").read_bytes()).hexdigest().startswith("ffe0a6e1")
