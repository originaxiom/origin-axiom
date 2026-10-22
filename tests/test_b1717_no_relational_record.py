"""B1717 -- no relational record on the private modules (P-278). Stored: the commutants and Homs; live: the computation
re-run from B1675's module, with its positive control (the commutant of V_3 + V_3 is M_2(C))."""
import json, pathlib, subprocess, sys
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1717_no_relational_record" / "verification"


def test_stored():
    d = json.loads((A / "no_relational_record.json").read_text(encoding="utf-8"))
    for g in ("<L, R>", "<L, R, P, I>"):
        v = d[g]
        assert (v["dim_V2"], v["dim_V3"], v["End_V2"], v["End_V3"], v["Hom_V2_V3"], v["Hom_V3_V2"]) == (4, 2, 1, 1, 0, 0)
        assert set(v["Hom_rhoQ_Vk_max_over_signs"].values()) == {0} and set(v["Hom_Vk_rhoQ_max_over_signs"].values()) == {0}
    assert d["control_End_V3_plus_V3"] == 4 and d["control_End_V2_plus_V3"] == 2


def test_live():
    src = A / "no_relational_record.py"
    r = subprocess.run([sys.executable, "-B", str(src), "--check"], capture_output=True, text=True, cwd=str(A), timeout=600)
    assert r.returncode == 0, r.stderr[-500:]
    assert "End(V_3 + V_3) = 4" in r.stdout and "End_G(V_2): 1 | End_G(V_3): 1 | Hom_G(V_2, V_3): 0" in r.stdout
