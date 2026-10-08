"""B1619 -- THE CODEX LANES ROWED: every item and relay listed in rowed.json has its row in the ledgers."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1619_the_codex_lanes_rowed"


def test_every_listed_item_and_relay_has_a_row():
    r = json.load(open(ARC / "verification" / "rowed.json"))
    h = open(ROOT / "docs" / "HARVEST_LEDGER.md", encoding="utf-8").read()
    rl = open(ROOT / "docs" / "RELAY_LEDGER.md", encoding="utf-8").read()
    assert len(r["harvest_rows"]) == 87 and len(r["relay_rows"]) == 37
    for row in r["harvest_rows"]:
        assert f"| {row['n']} | " in h and f" | {row['item']} | " in h
    for f in r["relay_rows"]:
        assert f"`{f}`" in rl
