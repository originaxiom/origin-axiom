"""R47-2 — the arc_verdict schema-validator lock (landed WITH the creates_law
field per the audit seat's sharpening: a declaration a gate reads beats a
standing rule nobody reads).

Every frontier/*/arc_verdict.json must:
  - parse as JSON with the five required fields;
  - carry a verdict from the closed enum;
  - carry instrument as a BOOLEAN (E45's species, locked);
  - carry creates_law as a BOOLEAN when present — and ALWAYS from B1103 on
    (legacy arcs may omit it; omission means false to the registry gate);
  - carry a scope tag (frame, object, reach, hypotheses) from B1516 on (GENESIS.md section 6);
  - carry a prior_work record (the repo leg with each swept head's sha, the literature leg, and a standing) from
    B1517 on (WORKING_RULES 2026-10-02, SEE THE REPO FIRST, THEN THE LITERATURE; the form is checked by
    scripts/checks/prior_work.py's validate()), and word any novelty only as far as that standing allows;
  - have an id matching its directory prefix.
"""
import importlib.util
import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
# The corpus's actual universal core (schema survey 2026-08-21: 906 of 995
# verdicts carry {authored_by, claim_one_line, depends_on, id, instrument,
# superseded_by, supersedes, verdict}; `title` exists only in a recent subset
# and is NOT required). E45's lesson, applied by survey not by one neighbor.
REQUIRED = {"id", "verdict", "claim_one_line", "instrument"}
VERDICTS = {"NEGATIVE", "OPEN", "PROVED", "RETRACTED"}
CREATES_LAW_REQUIRED_FROM = 1103
# B1231: identifications declared, same self-declaration pattern as creates_law. The programme's
# dominant error mode is gluing two structures whose labels match, in different places, without a
# map (B813; B1223's "direct is not semidirect"; and two of this bench's own in one session).
IDENTIFICATIONS_REQUIRED_FROM = 1231
# B1516 (GENESIS.md v1.0 section 6): every result carries a scope tag -- the frame it was computed in,
# the object, how far it reaches and what else it needs. A negative blocks only where its tag reaches.
SCOPE_REQUIRED_FROM = 1516
SCOPE_REACH = {"single", "class", "general"}
# B1517 (the owner, 2026-10-02: "make a rule to see the repo first and literature"): every arc records what it swept
# before it claims anything, in the repo (every head, with its sha) and in the literature (the sources read), and
# the standing of its main result. The form is checked here; the judgement stays with the seat.
PRIOR_WORK_REQUIRED_FROM = 1517
_spec = importlib.util.spec_from_file_location("prior_work", ROOT / "scripts" / "checks" / "prior_work.py")
prior_work = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(prior_work)
# Novelty wording in a FINDINGS body (quotations and block quotes excluded) needs a standing that allows it.
NOVELTY = re.compile(r"\b(novel|for the first time|not in the literature|no prior (?:work|art)|nobody has|"
                     r"not previously known|previously unknown|new result|the first to)\b", re.I)

FILES = sorted((ROOT / "frontier").glob("*/arc_verdict.json"))


def test_verdict_files_exist():
    assert len(FILES) > 900, "the corpus's verdict census went missing"


@pytest.mark.parametrize("path", FILES, ids=lambda p: p.parent.name)
def test_schema(path):
    d = json.load(open(path, encoding="utf-8"))
    missing = REQUIRED - set(d)
    assert not missing, f"{path.parent.name}: missing {missing}"
    assert d["verdict"] in VERDICTS, f"{path.parent.name}: verdict {d['verdict']!r}"
    assert isinstance(d["instrument"], bool), (
        f"{path.parent.name}: instrument must be boolean (E45)")
    m = re.match(r"(B\d+)", path.parent.name)
    assert m and d["id"] == m.group(1), (
        f"{path.parent.name}: id {d['id']!r} does not match directory")
    num = int(d["id"][1:])
    if "creates_law" in d:
        assert isinstance(d["creates_law"], bool), (
            f"{path.parent.name}: creates_law must be boolean")
    if "identifications" in d:
        assert isinstance(d["identifications"], list), (
            f"{path.parent.name}: identifications must be a list")
        for it in d["identifications"]:
            assert isinstance(it, dict) and "row" in it, (
                f"{path.parent.name}: each identification needs a 'row' naming its "
                f"docs/IDENTIFICATION_LEDGER.md entry (I-n)")
    if num >= IDENTIFICATIONS_REQUIRED_FROM:
        assert "identifications" in d, (
            f"{path.parent.name}: arcs from B{IDENTIFICATIONS_REQUIRED_FROM} on must declare "
            f"identifications (use [] if the arc makes none)")
    if num >= CREATES_LAW_REQUIRED_FROM:
        assert "creates_law" in d, (
            f"{path.parent.name}: creates_law is REQUIRED from "
            f"B{CREATES_LAW_REQUIRED_FROM} on (declare it, the gate reads it)")
    if "scope" in d or num >= SCOPE_REQUIRED_FROM:
        sc = d.get("scope")
        assert isinstance(sc, dict), (
            f"{path.parent.name}: arcs from B{SCOPE_REQUIRED_FROM} on carry a scope tag (GENESIS.md section 6)")
        assert isinstance(sc.get("frame"), str) and sc["frame"], f"{path.parent.name}: scope.frame"
        assert isinstance(sc.get("object"), str) and sc["object"], f"{path.parent.name}: scope.object"
        assert sc.get("reach") in SCOPE_REACH, f"{path.parent.name}: scope.reach must be one of {SCOPE_REACH}"
        assert isinstance(sc.get("hypotheses"), list), f"{path.parent.name}: scope.hypotheses must be a list"
    if "prior_work" in d or num >= PRIOR_WORK_REQUIRED_FROM:
        problems = prior_work.validate(d.get("prior_work"))
        assert not problems, (
            f"{path.parent.name}: arcs from B{PRIOR_WORK_REQUIRED_FROM} on record the repo leg and the literature "
            f"leg (WORKING_RULES 2026-10-02): {problems}")


def _unquoted(text):
    text = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith(">"))
    return re.sub(r'"[^"\n]*"|\u201c[^\u201d\n]*\u201d|`[^`\n]*`', " ", text)


LATE = [p for p in FILES if int(re.match(r"B(\d+)", p.parent.name).group(1)) >= PRIOR_WORK_REQUIRED_FROM]


@pytest.mark.parametrize("path", LATE or [None], ids=lambda p: p.parent.name if p else "none-yet")
def test_novelty_wording_rests_on_the_sweep(path):
    """A FINDINGS body that calls a result novel, first or absent from the literature needs a recorded sweep
    whose standing allows it (NEW-AS-SWEPT or EXTENDS) and the literature queries that were run."""
    if path is None:
        return
    f = path.parent / "FINDINGS.md"
    if not f.exists():
        return
    hits = sorted({m.group(0).lower() for m in NOVELTY.finditer(_unquoted(f.read_text(encoding="utf-8")))})
    if hits:
        pw = json.load(open(path, encoding="utf-8")).get("prior_work") or {}
        assert pw.get("standing") in ("NEW-AS-SWEPT", "EXTENDS") and (pw.get("literature") or {}).get("queries"), (
            f"{path.parent.name}: FINDINGS says {hits} but the recorded standing is {pw.get('standing')!r}")


def test_novelty_check_can_fail():
    """The wording check is live in both directions on planted text."""
    assert NOVELTY.search(_unquoted("This is a novel identity."))
    assert not NOVELTY.search(_unquoted('The rule forbids the word "novel" without a sweep.'))
    assert not NOVELTY.search(_unquoted("> the owner: nothing novel here"))
