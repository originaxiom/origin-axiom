"""B770 -- THE CLOSURE CENSUS: compute-grade locks on the census artifact.

The invariants locked here are the sealed prereg's binding rules (7682759b):
the no-unearned-closure invariant, full classification, and the exact counts.
All locks read census.json (the artifact of record), never the digest.
"""
import json
import pathlib

CENSUS = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B770_closure_census" / "census.json"


def _load():
    return json.loads(CENSUS.read_text())


def test_counts_exact():
    d = _load()
    assert d["raw_count"] == 431
    assert d["unique_count"] == 352
    assert d["counts"] == {
        "LIVE": 225, "EXTERNAL": 50, "CLOSED": 39,
        "STALE": 27, "CONSTITUTIVELY-OPEN": 6, "WALLED": 5,
    }
    assert sum(d["counts"].values()) == 352


def test_every_item_classified_once():
    d = _load()
    item_ids = {it["id"] for it in d["items"]}
    row_ids = [r["id"] for r in d["rows"]]
    assert len(row_ids) == len(set(row_ids)), "duplicate classification rows"
    assert set(row_ids) == item_ids, "items and rows must correspond 1:1"


def test_no_unearned_closure():
    # prereg rules 1-3: every CLOSED/WALLED/STALE row must carry a VERIFIED citation
    d = _load()
    for r in d["rows"]:
        if r["state"] in ("CLOSED", "WALLED", "STALE"):
            assert r.get("citation_verified") is True, f"{r['id']}: unverified closure"
            assert r.get("citation") and r["citation"] != "n/a", f"{r['id']}: missing citation"


def test_adversarial_pass_ran_on_all_closures():
    # every surviving closure was adversarially UPHELD; every refuted one reverted to LIVE
    d = _load()
    for r in d["rows"]:
        if r["state"] in ("CLOSED", "WALLED", "STALE"):
            assert r["adversarial"].startswith("UPHELD"), f"{r['id']}: closure without upheld verdict"
        if r["adversarial"].startswith("REFUTED"):
            assert r["state"] == "LIVE", f"{r['id']}: refuted closure must revert to LIVE"
    reverted = sum(1 for r in d["rows"] if r["adversarial"].startswith("REFUTED"))
    assert reverted == 16


def test_live_rows_carry_phases():
    d = _load()
    live = [r for r in d["rows"] if r["state"] == "LIVE"]
    assert len(live) == 225
    phases = {r.get("phase") or 0 for r in live}
    assert phases <= {0, 1, 2, 3, 4, 5}
    # the phase-1 mechanical list is non-empty (the quartet + B500 live there)
    assert sum(1 for r in live if r.get("phase") == 1) == 56


def test_states_are_the_sealed_six():
    d = _load()
    allowed = {"CLOSED", "WALLED", "CONSTITUTIVELY-OPEN", "EXTERNAL", "LIVE", "STALE"}
    assert {r["state"] for r in d["rows"]} <= allowed
