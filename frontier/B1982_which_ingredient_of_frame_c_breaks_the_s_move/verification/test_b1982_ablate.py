"""B1982's lock: the corrected runs show S covariance with the end law and no Fricke duality; the sealed ablation run holds the control, no passing variant, and the ranking the page reads from it (V1
nearest; V3 within 0.05 of V0; V2, V4, V5 above 0.6). Fails if a variant passes or the ranking moves."""
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent


def test_ablation_outcomes():
    t = (HERE / "ablate_run.txt").read_text()
    assert "SUMMARY E0: V0 reproduces B1980 (0.18 and 0.32 within 1e-2): True" in t
    assert "SUMMARY variants passing S (largest d < 1e-8 at both pairs): []" in t
    d = {}
    for v, x in re.findall(r"^(V\d) \{.*?\}: S move [\d.]+ against [\d.]+: largest d ([\d.e+-]+)", t, re.M):
        d[v] = max(d.get(v, 0), float(x))
    assert len(d) == 7 and min(d, key=d.get) == "V1" and d["V1"] < 0.2
    assert abs(d["V3"] - d["V0"]) < 0.05 and all(d[v] > 0.6 for v in ("V2", "V4", "V5"))


def test_s_with_the_end_law():
    t = (HERE / "s_endlaw_run.txt").read_text()
    assert "SUMMARY L1: frame C (V0) passes S with the record's end law: True" in t
    assert "SUMMARY L2: V1 (no norm) fails as before: True" in t and "SUMMARY V3 (a0 dropped) passes: True" in t
    d = [float(x) for x in re.findall(r"^V0, the end law .*largest d ([\d.e+-]+)", t, re.M)]
    assert len(d) == 3 and max(d) < 1e-12, d


def test_no_fricke_duality_with_the_end_law():
    t = (HERE / "fricke_endlaw_run.txt").read_text()
    assert "SUMMARY F-law: K != 1 passing with the end law: []" in t
    m = re.search(r"check: L_law\(0.4\) - L_law\(2.5\) = ([\d.]+), log 2.5 = ([\d.]+)", t)
    assert m and abs(float(m.group(1)) - float(m.group(2))) < 1e-10
