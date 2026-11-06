"""B1850 -- R76-1's second half: every checker quote is verbatim at its path; the confirmed leads are closed and the rest
carry their notes; the backlog rows carry their new dispositions; the counter reads the current disposition; L206's
check reproduces."""
import pathlib, re, subprocess, sys, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def _load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + ".py")); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m


def test_every_quote_is_verbatim_at_its_path():
    n, bad = _load("quote_check").check()
    assert n >= 312 and bad == []


def test_the_leads_carry_their_dispositions():
    ap = _load("apply_open_leads")
    text = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8").split("\n")
    first = {}
    for i, ln in enumerate(text):
        m = re.match(r"#{2,3} (L\d+)\b", ln)
        if m and m.group(1) not in first:
            first[m.group(1)] = i
    for L in ap.CLOSE:
        assert "— CLOSED 2026-11-06 (R76-1, B1850:" in text[first[L]], L
    for L in ap.KEEP:
        assert not re.search(r"(?:\*\*|— |- |L\d+[a-z]? )(?:CLOSED|DISCHARGED|WITHDRAWN)\b", text[first[L]]), L
        assert text[first[L] + 2].startswith("> *2026-11-06 (R76-1, B1850):"), L


def test_the_backlog_rows_and_the_counter():
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    import harvest_debt as h
    rows = {r["n"]: r for r in h.read_rows((ROOT / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8"))}
    ab = _load("apply_backlog")
    for row, (host, _) in ab.REPOINT.items():
        assert rows[row]["disp"].startswith("**CARRIED by %s**" % host) and not h.is_scheduled(rows[row]["disp"]), row
    for row in (351, 358, 494, 523, 202):
        assert rows[row]["disp"].startswith("**CLOSED-") and not h.is_scheduled(rows[row]["disp"]), row
    for row in (125, 189, 374, 448):
        assert h.is_scheduled(rows[row]["disp"]) and "R76-1, B1850" in rows[row]["disp"], row
    assert sum(1 for r in rows.values() if h.is_scheduled(r["disp"])) <= h.SCHEDULED_BASELINE == 46


def test_the_generating_pair_check_reproduces():
    out = subprocess.run([sys.executable, "-B", str(HERE / "l206_generating_pair.py")], capture_output=True, text=True,
                         check=True, timeout=300).stdout
    assert out == (HERE / "l206_generating_pair_run.txt").read_text(encoding="utf-8")
    assert "generates pi_1(m003)" in out
