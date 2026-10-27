"""B1756 -- JUNO's second release against P10 (a) and P10'.  B1628's sealed instrument is the one used (its hash); the
committed grade reproduces (TM1 2.28 sigma, TM2 5.82 sigma; P10' falsified, P10 (a) not); the register carries both."""
import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1756_junos_second_release_and_the_two_trimaximal_relations"


def test_the_grade_reproduces(tmp_path):
    g = json.loads((A / "verification" / "grade.json").read_text(encoding="utf-8"))
    j = g["JUNO_2026_second_release"]
    assert abs(j["TM1_pull_sigma"] - 2.282) < 1e-3 and abs(j["TM2_pull_sigma"] - 5.823) < 1e-3
    assert j["P10prime_falsified"] and not j["P10a_falsified"]
    assert g["JUNO_2025_first_result"]["P10prime_falsified"]          # disclosed: met already on the first result
    r = subprocess.run([sys.executable, "-B", "-c", "import importlib.util,pathlib,json;"
                        "s=importlib.util.spec_from_file_location('g',r'%s');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);"
                        "m.HERE=pathlib.Path(r'%s');print(m.SRC_SHA)" % (A / "verification" / "grade.py", tmp_path)], capture_output=True, text=True)
    assert r.returncode == 0 and r.stdout.strip() == "e638ccb7c634acc770b835a146dbfed0b21202ccf80bdd5b4e247f9433bcf0dd"


def test_the_register_carries_it():
    f = (ROOT / "docs" / "FALSIFIER_REGISTER.md").read_text(encoding="utf-8")
    assert "**FALSIFIED 2026-10-24 (B1756)**" in f and "2.28σ on JUNO's second release" in f
