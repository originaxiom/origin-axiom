"""B1833 lock -- the brainstorms re-read (P-628): every item main confirmed FORGOTTEN now has a register carrier, the
corrections it made are on the record, and the owner's two calls are in the register as OWNER rows.

The before-rows sweep is the evidence that the items had no register row; the after-rows sweep is re-run here, so a row
that later loses its wording fails this lock.
"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REG = (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8")
# carried elsewhere in other words (read by main): the golden converse by P-030-P-032 (Q6), the near-fixed-point
# hierarchy by the Q4 slot's rows, the Dirac-Laplace coincidences by P-649 ('near-coincidences')
CARRIED_ELSEWHERE = {"goldconv", "nearfixed", "DiracLap"}


def _row(pid):
    rows = [l for l in REG.split("\n") if l.startswith("| %s |" % pid)]
    assert len(rows) == 1, pid
    return [c.strip() for c in rows[0].strip().strip("|").split(" | ")]


def test_the_items_without_a_row_before_now_have_one(tmp_path):
    import os
    before = json.loads((HERE / "verify_forgotten_before_rows.json").read_text(encoding="utf-8"))
    out = tmp_path / "after.json"   # re-run into a temporary file: the committed after-rows file is the landing's record
    subprocess.run([sys.executable, str(HERE / "verify_forgotten.py")], cwd=ROOT, capture_output=True, check=True, timeout=600,
                   env=dict(os.environ, VERIFY_FORGOTTEN_OUT=str(out)))
    after = json.loads(out.read_text(encoding="utf-8"))
    unrowed = [k for k, v in before.items() if not v["register"]]
    assert len(unrowed) >= 40, "the evidence no longer shows the gap it records"
    still = {k for k in unrowed if not after[k]["register"]}
    assert still <= CARRIED_ELSEWHERE, "items with no register carrier: %s" % sorted(still - CARRIED_ELSEWHERE)


def test_the_new_rows_run_without_gaps_and_are_typed():
    for n in range(629, 661):
        c = _row("P-%03d" % n)
        assert c[4] in {"QUEUED", "OWNER", "DONE"}, (n, c[4])
        if c[4] == "QUEUED":
            assert len(re.findall(r"\[(DEBT|LEAD|PROCESS)\]", c[5])) == 1, n
    assert _row("P-628")[4] == "DONE" and "B1833" in _row("P-628")[5]
    for pid in ("P-652", "P-659", "P-660", "P-625"):
        assert _row(pid)[4] == "OWNER", pid


def test_the_corrections_are_on_the_record():
    ol = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    assert "this note mislabels item (b)" in ol and "(g) and (h) fell out of the carry" in ol
    sp = (ROOT / "speculations" / "S_THE_FIELDS_GENESIS.md").read_text(encoding="utf-8")
    assert "describe a plan, not work done" in sp
    for pid in ("P-303", "P-335"):
        assert "omitted from main's 2026-10-24 list" in _row(pid)[5], pid


def test_the_findings_keep_the_web_era_private():
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    for word in ("chatA", "chatB", "chat A", "chat B", "chatB_full", "HARVEST_CANDIDATES"):
        assert word not in f, word
