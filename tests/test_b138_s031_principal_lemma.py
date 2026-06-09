"""Locks for B138 -- the principal-image direction of S031 (Sym^{n-1} seals in K_m, all n)."""
import importlib.util, pathlib
_ROOT = pathlib.Path(__file__).resolve().parents[1]
def _load():
    spec = importlib.util.spec_from_file_location("b138_probe", _ROOT / "frontier/B138_s031_principal_lemma/probe.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
B138 = _load()
def test_principal_image_seals_m1():
    r = B138.principal_image_seals(1)
    assert r["field"] == "Q(sqrt-3)" and r["sealed_all_n"]
    assert all(rr["det_A_is_1"] for rr in r["rows"].values())
def test_principal_image_seals_m2():
    r = B138.principal_image_seals(2)
    assert r["field"] == "Q(i)" and r["sealed_all_n"]
