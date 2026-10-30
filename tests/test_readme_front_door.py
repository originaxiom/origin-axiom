"""P-513 (the owner, 2026-10-30: the README rewritten from blank). The front door's state block is generated from tracked
files and agrees with a recount; every link it gives resolves; its old text is archived byte for byte. A planted control
shows the link check can fail. (That the block equals the generator's output byte for byte is the views gate's check.)"""
import hashlib, json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
HIST = ROOT / "docs" / "README_HISTORY.md"


def _block(text):
    m = re.search(r"<!-- STATE:BEGIN[^\n]*-->\n(.*?)<!-- STATE:END -->", text, re.S)
    assert m, "the README has no generated state block"
    return m.group(1)


def _links(text):
    return [t for t in re.findall(r"\]\(([^)#\s]+)\)", text) if not re.match(r"[a-z]+:", t)]


def test_the_state_block_agrees_with_a_recount():
    b = _block(README.read_text(encoding="utf-8"))
    n = sum(1 for l in (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8").splitlines() if l.startswith("| P-"))
    assert "| points in the register | %d: " % n in b
    v = re.search(r"\*\*Version (\d+\.\d+) ·", (ROOT / "GENESIS.md").read_text(encoding="utf-8")).group(1)
    assert "`GENESIS.md` (v%s)" % v in b
    verdicts = [json.loads(p.read_text(encoding="utf-8")).get("verdict") for p in (ROOT / "frontier").glob("B*/arc_verdict.json")]
    assert re.search(r"\| arcs with a verdict \| \d+: %d PROVED, %d NEGATIVE," % (verdicts.count("PROVED"), verdicts.count("NEGATIVE")), b), b
    last = re.findall(r"(?m)^# Review (\d+) \(", (ROOT / "docs" / "progress" / "REVIEWS.md").read_text(encoding="utf-8"))[-1]
    assert "| the last review | Review %s (" % last in b


def test_every_link_resolves():
    bad = [t for t in _links(README.read_text(encoding="utf-8")) if not (ROOT / t).exists()]
    assert bad == [], bad


def test_the_link_check_can_fail():
    assert _links("see [x](docs/NO_SUCH_FILE.md) and [y](https://example.org/a)") == ["docs/NO_SUCH_FILE.md"]
    assert not (ROOT / "docs" / "NO_SUCH_FILE.md").exists()


def test_the_old_text_is_archived_byte_for_byte():
    head, body = HIST.read_text(encoding="utf-8").split("<!-- ARCHIVE:BEGIN -->\n", 1)
    sha = re.search(r"sha-256\s+of the archived text: `([0-9a-f]{64})`", head).group(1)
    assert hashlib.sha256(body.encode("utf-8")).hexdigest() == sha
    assert "## The state of the programme (as of B1458, 2026-10-03)" in body


def test_the_front_door_keeps_its_living_requirements():
    t = " ".join(README.read_text(encoding="utf-8").split())
    assert "All verification in this repository is INTERNAL" in t and "Nothing here is externally verified or peer-reviewed" in t
    assert "docs/README_HISTORY.md" in t and "GENESIS.md" in t
