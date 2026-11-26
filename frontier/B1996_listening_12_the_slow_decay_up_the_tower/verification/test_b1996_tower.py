"""B1996's lock: the committed runs hold the settled rate on the 3-tower and the rising one on the 5-tower (the runs take seconds to minutes; they are not rerun here)."""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent


def test_settled_and_rising():
    t = (HERE / "tower_decay_run.txt").read_text()
    # Review 87: the mod-125 value, the control and the gaps are now held too.
    rows = {l.split("(")[0].strip(): l for l in t.splitlines() if l.startswith("mod")}
    assert "slowest decay ratio 0.7071" in rows["mod   27"] and "gap below it 0.3542" in rows["mod   27"]
    assert "slowest decay ratio 0.8389" in rows["mod  125"] and "gap below it 0.1301" in rows["mod  125"]
    assert "gap below it 0.0405" in rows["mod   81"] and "gap below it 0.0405" in rows["mod  243"] and "gap below it 0.0053" in rows["mod  625"]
    assert t.count("slowest decay ratio 0.9576") == 2 and "mod  625 (p = 5, k = 4)" in t and "slowest decay ratio 0.9947" in t
    s = (HERE / "settle_posthoc_run.txt").read_text()
    assert "(c) mod 729:" in s and "largest orbit 52488" in s and "slowest decay ratio 0.9576" in s
    assert "(1.915298+0j), (1.915298+0j), (-1.915298+0j), (-1.915298+0j)" in s
