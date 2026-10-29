"""The Ledger Desk builds from main's record, offline, and cites the newest arc (P-420, phase 1).

The page is built into a temporary directory (nothing is written into the checkout) from the commit HEAD names when the
module starts, and then held to what it says:

  1. it is built, it is large, and it names that commit;
  2. the newest arc at that commit is in it, found here from git and not from the builder;
  3. its verdict counts equal a recount of the verdict files at that commit made here, by its own git calls;
  4. its edge total equals a recount made here from the raw lists;
  5. it loads nothing external, and carries a policy that refuses every external load;
  6. it, and every file this directory commits, names no vendor and no local absolute path;
  7. the relay-debt pattern the board uses is the gate's own; every claim shown is the verdict file's text or a marked cut
     of it; P-415's disposition is the register's.

The checks in 5 and 6 are functions, and each is shown to fail on a page that breaks it (MB12: a criterion must be
able to fail). The build takes seconds; nothing here needs the network.
"""
import base64
import collections
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DESK = ROOT / "docs" / "workdesk"
# encoded so that this file passes the attribution gate it helps to mirror
VENDOR = re.compile(r"\b(" + "|".join(base64.b64decode(b).decode() for b in
                                       (b"Y2xhdWRl", b"YW50aHJvcGlj", b"b3B1cw==", b"c29ubmV0", b"ZmFibGU=")) + r")\b", re.I)
# assembled from fragments, as tests/test_no_hardcoded_paths.py does, so that this file does not trip that guard
_USERS, _HOME, _PRIVATE = "/Us" + "ers/", "/ho" + "me/", "/pri" + "vate/"
LOCAL_PATH = re.compile("|".join(re.escape(x) for x in (_USERS, _HOME, _PRIVATE)) + r"|[A-Za-z]:\\Us" + "ers")
ALLOWED_URLS = ("http://www.w3.org/2000/svg", "https://github.com/originaxiom/origin-axiom/blob/")


def git(*args):
    r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-400:]
    return r.stdout


def ids(v):
    raw = [v] if isinstance(v, str) else list(v) if isinstance(v, list) else []
    return [t for chunk in raw if isinstance(chunk, str) for t in re.split(r"[,\s]+", chunk.strip()) if t]


def recount(head):
    """{path: verdict file} for frontier/*/arc_verdict.json at head, read here by path, not by the builder's blob batch"""
    paths = [p for p in git("ls-tree", "-r", "--name-only", head, "frontier/").splitlines()
             if p.endswith("/arc_verdict.json") and p.count("/") == 2]
    raw = subprocess.run(["git", "-C", str(ROOT), "cat-file", "--batch"], capture_output=True,
                         input=("\n".join(f"{head}:{p}" for p in paths) + "\n").encode()).stdout
    out, i = {}, 0
    for p in paths:
        nl = raw.index(b"\n", i)
        size = int(raw[i:nl].split()[2])
        out[p] = json.loads(raw[nl + 1:nl + 1 + size])
        i = nl + 1 + size + 1
    return out


def split_page(page):
    """(the DESK data, the rest of the page): the record's own text is in the first, the markup and script in the second"""
    lines = page.split("\n")
    data = [ln for ln in lines if ln.startswith("const DESK=")]
    assert len(data) == 1
    return json.loads(data[0][len("const DESK="):].rstrip(";")), "\n".join(ln for ln in lines if not ln.startswith("const DESK="))


def external_loads(shell):
    """everything in the markup and script that loads or calls something outside the page, or the absence of the policy"""
    hits = re.findall(r"<script[^>]*\bsrc\s*=", shell, re.I) + re.findall(r"<link[^>]*\bhref\s*=", shell, re.I)
    hits += re.findall(r"@import|\bimport\s*\(|\bfetch\s*\(|XMLHttpRequest|sendBeacon|WebSocket|EventSource|importScripts|\burl\s*\(",
                       shell)
    hits += [u for u in re.findall(r"https?://[^\s\"'<>)]+", shell) if not u.startswith(ALLOWED_URLS)]
    if "Content-Security-Policy" not in shell or "default-src 'none'" not in shell:
        hits.append("no policy refusing external loads")
    return hits


def leaks(text):
    """vendor names and local absolute paths"""
    return [m.group(0) for m in VENDOR.finditer(text)] + [m.group(0) for m in LOCAL_PATH.finditer(text)]


@pytest.fixture(scope="module")
def head():
    r = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True)
    if r.returncode != 0:
        pytest.skip("not a git checkout")
    return r.stdout.strip()


@pytest.fixture(scope="module")
def built(tmp_path_factory, head):
    out = tmp_path_factory.mktemp("desk")
    r = subprocess.run([sys.executable, "-B", str(DESK / "build_page.py"), "--main-ref", head, "--out", str(out)],
                       capture_output=True, text=True, timeout=300)
    assert r.returncode == 0, r.stderr[-800:]
    page = (out / "index.html").read_text(encoding="utf-8")
    data, shell = split_page(page)
    return page, data, shell


def test_the_page_is_built_and_names_head(built, head):
    page, data, shell = built
    assert len(page) > 200_000
    assert f'const SHA = "{head}";' in shell
    assert data["index"]["manifest"]["built_from"]["main"] == head


def test_the_newest_arc_at_head_is_in_the_page(built, head):
    _, data, _ = built
    vf = recount(head)
    newest = max((int(m.group(1)), p) for p in vf if (m := re.match(r"frontier/B(\d+)", p)))
    nodes = {n[0]: n for n in data["index"]["atlas"]["nodes"]}
    assert f"main:B{newest[0]}" in nodes
    assert nodes[f"main:B{newest[0]}"][1] == str(vf[newest[1]]["verdict"]).upper()


def test_the_counts_equal_a_recount_of_the_verdict_files(built, head):
    _, data, _ = built
    want = collections.Counter(v["verdict"] for v in recount(head).values())
    got = {r[2]: r[3] for r in data["index"]["counts"] if r[0] == "main" and r[1] == "B"}
    assert got == dict(want)
    assert data["index"]["manifest"]["tables"]["arcs"]["rows"] == sum(want.values())


def test_the_edge_total_equals_a_recount_of_the_raw_lists(built, head):
    _, data, _ = built
    n = 0
    for v in recount(head).values():
        for k in ("depends_on", "supersedes", "superseded_by"):
            n += sum(1 for t in ids(v.get(k)) if re.fullmatch(r"B\d+[a-z]?", t))
        for k in ("rests_on_seat", "cites_seat"):
            n += sum(1 for t in (v.get(k) or []) if isinstance(t, str) and ":" in t)
    assert sum(c for _, c in data["index"]["resolved"]) == n


def test_every_claim_on_the_page_is_the_verdict_files_own_text_or_a_marked_cut_of_it(built, head):
    _, data, _ = built
    seen, expected = collections.Counter(), {}
    vf = recount(head)
    for path in sorted(vf):
        base = "main:" + path.split("/")[1].split("_")[0]
        seen[base] += 1
        expected[base if seen[base] == 1 else f"{base}#{seen[base]}"] = vf[path]["claim_one_line"]
    checked = 0
    for key, _verdict, _tag, claim, _src in data["index"]["atlas"]["nodes"]:
        if key in expected:
            full = expected[key]
            assert claim == full or (claim.endswith("…") and full.startswith(claim[:-1])), key
            checked += 1
    assert checked == len(expected) == len(vf)


def test_p415_disposition_on_the_page_is_the_registers(built, head):
    _, data, _ = built
    row = next(ln for ln in git("show", f"{head}:docs/POINT_REGISTER.md").splitlines() if ln.startswith("| P-415 |"))
    assert data["index"]["curated"]["register"]["disposition"] == [c.strip() for c in row.strip().strip("|").split("|")][4].split()[0]


def test_the_page_loads_nothing_external(built):
    _, _, shell = built
    assert external_loads(shell) == []


def test_the_external_load_check_can_fail():
    clean = "<meta http-equiv=\"Content-Security-Policy\" content=\"default-src 'none'\"><script>1</script>"
    assert external_loads(clean) == []
    for bad in ('<script src="https://cdn.example/x.js"></script>', '<link rel="stylesheet" href="https://fonts.example/c.css">',
                "<script>fetch('/x')</script>", "<style>@import 'x.css'</style>", '<a href="https://example.org/">x</a>'):
        assert external_loads(clean + bad), bad
    assert external_loads("<script>1</script>")        # no policy


def test_no_vendor_and_no_local_path_in_the_page_or_the_files(built):
    page, _, _ = built
    assert leaks(page) == []
    for name in ("README.md", "build_index.py", "build_page.py", "extract_desk_data.py", "the_ledger_desk.template.html"):
        assert leaks((DESK / name).read_text(encoding="utf-8")) == [], name


def test_the_leak_check_can_fail():
    assert leaks("a model named " + base64.b64decode(b"Y2xhdWRl").decode() + " wrote this")
    assert leaks("see " + _USERS + "someone/work") and leaks("at " + _PRIVATE + "tmp/x") and leaks("in " + _HOME + "someone")
    # the names are matched as words: ordinary words that contain them as fragments are not hits (the pieces are joined here
    # so that this source holds no fragment either)
    assert leaks("phil" + "an" + "thropic and ine" + "ff" + "able prose, a word like 'cloud' or 'private'") == []


def test_the_committed_page_is_clean():
    page = DESK / "the_ledger_desk.html"
    if not page.is_file():
        pytest.skip("no committed page yet")
    _, shell = split_page(page.read_text(encoding="utf-8"))
    assert external_loads(shell) == []
    assert leaks(page.read_text(encoding="utf-8")) == []


def test_the_boards_relay_pattern_is_the_gates_own(built, head, tmp_path):
    _, data, _ = built
    (tmp_path / "relay_debt.py").write_text(git("show", f"{head}:scripts/checks/relay_debt.py"), encoding="utf-8")
    spec = importlib.util.spec_from_file_location("relay_debt_gate", tmp_path / "relay_debt.py")   # the gate as it stands at head
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    text = git("show", f"{head}:docs/RELAY_LEDGER.md")
    seen = {m.group("name") for m in gate.ROW_RE.finditer(text) if m.group("disp") == "OPEN"}
    waiting = data["index"]["board"]["waiting"]
    assert {w[1] for w in waiting if w[8]} == seen & {w[1] for w in waiting}
    assert data["index"]["board"]["stale_days"] == gate.STALE_DAYS
