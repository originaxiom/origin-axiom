"""B1487 -- THE ENDS: the stored cells, the amendment, the registry."""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1487_the_ends"


def test_the_floor_holds_on_every_reading_on_main():
    d = json.load(open(HERE / "verification" / "floor_check.json"))
    assert d["summary"]["rows"] == 390 and d["summary"]["violations"] == 0 and d["summary"]["tight"] == 2
    assert all(r["ok"] for r in d["rows"]) and all(abs(r["I"]) <= r["mA"] + r["b0"] for r in d["rows"] if r["src"] != "N45")


def test_the_odd_modules_are_acyclic_and_the_four_has_no_interior_class_on_all_304_lifts():
    d = json.load(open(HERE / "verification" / "odd_modules_acyclic.json"))
    assert len(d) == 68 and sum(len(r["lifts"]) for r in d) == 304
    assert all(r["odd_modules_acyclic_on_every_lift"] for r in d)
    for r in d:
        for l in r["lifts"]:
            assert l["Sym1"]["a1"] == 0 and l["Sym3"]["a1"] == 0 and l["four"]["a1"] == 1 and l["four"]["n"] == 0
        tm, tl = complex(r["tr_mu"].replace(" ", "").strip("()")), complex(r["tr_lam"].replace(" ", "").strip("()"))
        assert abs(tm + 2) < 1e-6 or abs(tl + 2) < 1e-6          # the fibre's boundary has trace -2 on every state
    # the failing path: an odd module with a class somewhere would be a different world
    assert not any(l["Sym3"]["a1"] > 0 for r in d for l in r["lifts"])


def test_genesis_carries_v1_15_and_the_amendment_reproduces_it():
    root = HERE.parents[1]
    g = (root / "GENESIS.md").read_text()
    assert "- **v1.15 · 2026-10-07 · main B1487.**" in g and "| FK14" in g and "**Six gaps**" in g and "mirror-even for" in g
    import importlib.util
    spec = importlib.util.spec_from_file_location("amend_b1487", HERE / "adoption" / "amend.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    out = m.build(); assert "**Version 1.15 " in out and "| FK14" in out       # the amendment still builds from its received v1.14
    r = subprocess.run([sys.executable, str(HERE / "adoption" / "amend.py"), "--check"], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
