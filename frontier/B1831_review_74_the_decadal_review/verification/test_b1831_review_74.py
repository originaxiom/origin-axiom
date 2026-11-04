"""B1831 -- Review 74's block is on the page with its core lines and its carries' lineage; the relay-closure pass is on the
ledger; the register carries the review's rows; the instruments it committed are in place."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent


def test_review_74_block_core_lines_and_carries():
    t = ROOT.joinpath("docs", "progress", "REVIEWS.md").read_text(encoding="utf-8")
    blk = t[t.index("# Review 74 (2026-11-04)"):]
    assert "sample seed: 99d90d515" in blk and "gate controls: 47 registered" in blk and "fresh-clone: PASS @" in blk
    acts = blk.split("### Action items (Review 74)")[1]
    assert all(("R74-%d:" % n) in acts for n in range(1, 11))
    for key in ("R73-4", "R73-5", "R73-8", "R73-9", "R73-10"):
        assert key in acts, key
    r73 = t[t.index("# Review 73 (2026-10-30)"):t.index("# Review 74 (2026-11-04)")]
    assert not re.search(r"^- \[ \]", r73.split("### Action items (Review 73)")[1], re.M)


def test_the_relay_pass_is_on_the_ledger():
    tab = json.loads((HERE / "apply" / "relay_table.json").read_text(encoding="utf-8"))
    led = ROOT.joinpath("docs", "RELAY_LEDGER.md").read_text(encoding="utf-8")
    assert len(tab) == 84
    closed = [l for l in led.splitlines() if "B1831's relay-closure pass" in l]
    assert len(closed) == 79 and all(("| BANKED |" in l or "| DECLINED |" in l) for l in closed)


def test_the_register_rows_and_the_instruments():
    reg = ROOT.joinpath("docs", "POINT_REGISTER.md").read_text(encoding="utf-8")
    for n in range(594, 621):
        assert re.search(r"^\| P-%d \| 2026-11-04 \| R74 \|" % n, reg, re.M), n
    v = ROOT / "frontier" / "B1826_the_agy_lanes_november_audit_verified_on_main" / "verification" / "review74"
    for f in ("sigma_b_order8.py", "sigma_b_order8_out.txt", "ll_pair_norms.py", "ll_pair_norms_out.txt"):
        assert (v / f).is_file(), f
    s = (v / "sigma_b_order8_out.txt").read_text()
    assert "-1.021e-01" in s and "1.906e-04" in s
