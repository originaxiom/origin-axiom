"""B1290 — the index formula applied; net chirality = -chi(d+M); I-26 reframed, NOT paid."""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1290_the_index_formula"
LEDGER = ROOT / "docs" / "IDENTIFICATION_LEDGER.md"


def _row(tag):
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        if re.match(rf"\|\s*{re.escape(tag)}\s*\|", line):
            return line
    raise AssertionError(f"{tag} missing from the identification ledger")


def test_the_arc_reproduces_by_RUNNING_its_script():
    r = subprocess.run([sys.executable, str(ARC / "verification" / "index_formula.py")],
                       capture_output=True, text=True, cwd=str(ARC / "verification"))
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    assert r.stdout.rstrip().endswith("SELFTEST: PASS"), r.stdout[-500:]


def test_the_arithmetic_is_computed_not_asserted():
    sys.path.insert(0, str(ARC / "verification"))
    try:
        import index_formula as m
    finally:
        sys.path.pop(0)
    # chi(M) comes from SnapPy's presentation of m004: 2 generators, 1 relator
    assert m.euler_presentation(2, 1) == 0
    assert m.SURFACES["torus T^2"] == 0
    # the law, and its IFF character
    assert m.net_chirality(0, m.SURFACES["annulus"]) == 0        # annular  -> ZERO
    assert m.net_chirality(0, m.SURFACES["disc"]) != 0           # discs    -> NONZERO
    assert m.net_chirality(0, m.SURFACES["pair of pants"]) != 0  # corners  -> NONZERO


def test_the_control_is_not_vacuous_in_either_direction():
    """MB12: the surface table must contain BOTH chi=0 and chi!=0 pieces."""
    sys.path.insert(0, str(ARC / "verification"))
    try:
        import index_formula as m
    finally:
        sys.path.pop(0)
    vals = set(m.SURFACES.values())
    assert 0 in vals and any(v != 0 for v in vals), m.SURFACES


def test_I26_is_REFRAMED_and_still_UNEARNED():
    """The reframing must not be mistaken for payment — this is the ratchet on B1290 itself."""
    row = _row("I-26")
    assert "**UNEARNED**" in row, "B1290 reframes I-26's price; it does NOT earn the row"
    # the new price must name the actual question, not the old one alone
    assert "chi(" in row or "χ(" in row, "I-26's price never mentions the Euler characteristic"
    assert "∂⁺M" in row or "d+M" in row, "I-26's price never names the boundary piece"


def test_the_cited_not_derived_fence_is_stated():
    txt = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "CITED" in txt and "not derived here" in txt.lower().replace("—", "-") or \
           "CITED, not derived here" in txt, "the formula's provenance fence is missing"
    # and the harvested R61 candidate must be fenced as harvest, not verification
    assert "NOT verified here" in txt or "not verified here" in txt


def test_the_fourth_route_names_all_four_and_does_not_double_count():
    txt = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for route in ("B1267", "R61", "SM seat"):
        assert route in txt, f"the convergence table omits {route}"
    assert "FOURTH" in txt.upper()


def test_B1290_respects_the_reserved_range():
    """B1278-B1289 are RESERVED-NEVER-ASSIGNED on main (CC_TO_ALL_SEATS 2026-09-06)."""
    n = int(re.match(r"B(\d+)", ARC.name).group(1))
    assert not (1278 <= n <= 1289), f"{ARC.name} lands inside the reserved range"
    assert n >= 1290


def test_the_verdict_declares_no_new_identifications():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "PROVED" and v["identifications"] == []
    assert "I-26" in v["claim_one_line"] and "UNEARNED" in v["claim_one_line"]


# --- B1290's follow-through: the supersession back-link gate -------------------------------

def _gates():
    sys.path.insert(0, str(ROOT / "scripts" / "gates"))
    try:
        import gates
        return gates
    finally:
        sys.path.pop(0)


def test_no_arc_is_silently_superseded():
    """43 arcs were claimed superseded and only ONE said so — E53's shape at the supersession
    level. A reader landing on B154 saw PROVED with no marker. The back-link is derivable."""
    ok, detail = _gates().gate_supersession_backlinks()
    assert ok, detail


def test_the_backlink_gate_CAN_fail(tmp_path, monkeypatch):
    """MB12 both directions: plant a forward claim with no back-link and require a red."""
    g = _gates()
    frontier = tmp_path / "frontier"
    (frontier / "Bx").mkdir(parents=True)
    (frontier / "By").mkdir(parents=True)
    (frontier / "Bx" / "arc_verdict.json").write_text(json.dumps(
        {"id": "B9001", "verdict": "PROVED", "supersedes": None, "superseded_by": None}))
    (frontier / "By" / "arc_verdict.json").write_text(json.dumps(
        {"id": "B9002", "verdict": "PROVED", "supersedes": "B9001", "superseded_by": None}))
    monkeypatch.setattr(g, "ROOT", str(tmp_path))
    ok, detail = g.gate_supersession_backlinks()
    assert not ok and "B9001" in str(detail), detail

    # and it goes green the moment the back-link is written -- so it is a real discriminator
    (frontier / "Bx" / "arc_verdict.json").write_text(json.dumps(
        {"id": "B9001", "verdict": "PROVED", "supersedes": None, "superseded_by": "B9002"}))
    ok2, _ = g.gate_supersession_backlinks()
    assert ok2


def test_the_backlinks_did_NOT_change_any_verdict():
    """Superseding is not retracting. The 12 RETRACTED arcs are a separate, deliberate act."""
    import glob, collections
    c = collections.Counter()
    for f in glob.glob(str(ROOT / "frontier" / "*" / "arc_verdict.json")):
        try: c[json.load(open(f, encoding="utf-8")).get("verdict")] += 1
        except Exception: pass
    # PIN THE INVARIANT, NOT THE SNAPSHOT. An earlier version pinned PROVED/NEGATIVE/OPEN
    # literally; that went red at B1291 for the legitimate reason that a new NEGATIVE arc was
    # banked. Banking arcs must not red this test -- the claim it defends is narrower and
    # permanent: SUPERSEDING IS NOT RETRACTING, so writing 36 superseded_by back-links moved
    # no arc into or out of RETRACTED. (Same lesson as test_b1242's ratchet comment.)
    assert c["RETRACTED"] == 12, f"retraction count moved: {c['RETRACTED']}"
    import json as _json, glob as _glob
    backlinked = [f for f in _glob.glob(str(ROOT / "frontier" / "*" / "arc_verdict.json"))
                  if (_json.load(open(f, encoding="utf-8")) or {}).get("superseded_by")]
    assert len(backlinked) >= 36, f"back-links lost: {len(backlinked)}"
    for f in backlinked:
        d = _json.load(open(f, encoding="utf-8"))
        assert d["verdict"] in {"PROVED", "NEGATIVE", "OPEN", "RETRACTED"}, d
        # a superseded arc keeps whatever verdict it earned; supersession never implies retraction
    assert sum(c.values()) == len(_glob.glob(str(ROOT / "frontier" / "*" / "arc_verdict.json")))


# --- B1290's second follow-through: the relay gate now enforces its own stated rule --------

def test_the_relay_gate_matches_its_own_docstring():
    """The rule said 'cross-seat relay files'; the regex enforced only CC2/CC3, so CC_TO_FC,
    CC_TO_CLOUD, CC_TO_CODEX and CC_TO_ALL_SEATS were invisible — B1226's shape. Both
    violations it had already cost were committed by this bench on the day it was found."""
    g = _gates()
    ok, detail = g.gate_tracked_forbidden()
    assert ok, detail
    src = (ROOT / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
    # the widened matcher must key on a seat AND the relay convention's date stamp
    assert "_RELAY_RE" in src and r"\d{4}-\d{2}-\d{2}" in src


def test_the_relay_gate_CAN_fail_and_spares_the_sanctioned_location(monkeypatch):
    """MB12 both directions: a NEW loose relay reds; the same relay inside an arc dir does not."""
    g = _gates()
    NEW = "CC_TO_CLOUD_2026-09-07_A_NEW_LOOSE_RELAY.md"
    ARCHIVED = "frontier/B1290_the_index_formula/" + NEW
    MASTERPLAN = "docs/STRUCTURE_TO_NATURE_MASTERPLAN.md"

    def fake(*a):
        return 0, "\n".join(["README.md", MASTERPLAN, ARCHIVED, NEW])
    monkeypatch.setattr(g, "_git", fake)
    ok, bad = g.gate_tracked_forbidden()
    assert not ok and NEW in bad, bad
    # the sanctioned location and the false-positive-shaped masterplan are BOTH spared
    assert ARCHIVED not in bad and MASTERPLAN not in bad, bad

    def fake_clean(*a):
        return 0, "\n".join(["README.md", MASTERPLAN, ARCHIVED])
    monkeypatch.setattr(g, "_git", fake_clean)
    ok2, _ = g.gate_tracked_forbidden()
    assert ok2


def test_the_grandfathered_relays_are_named_and_bounded():
    """GOVERNANCE §12 forbids moving banked paths, so these three stay — but the set must not
    grow silently; a fourth entry means someone committed a loose relay instead of archiving it."""
    src = (ROOT / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
    block = src.split("GRANDFATHERED_RELAYS = {", 1)[1].split("}", 1)[0]
    names = [x for x in re.findall(r'"([^"]+\.md)"', block)]
    assert len(names) == 3, names
    assert "CC3_TO_CC_2026-07-22_p3_complete.md" in names
