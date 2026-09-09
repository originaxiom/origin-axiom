"""B1243 — the point-of-use gate, the chain's coverage, and the two no-gos.

Three locks: (1) the instrument's own controls bite in both directions; (2) the chain carries
every result pinned in docs/CHAIN_COVERAGE.json — the lock that exists because the genesis
theorem sat uncited by the chain for three months; (3) C25 carries its scope and C44/C45 exist.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE = ROOT / "scripts" / "checks" / "citation_status.py"
LEDGER = ROOT / "docs" / "THEOREM_LEDGER.md"
COVERAGE = ROOT / "docs" / "CHAIN_COVERAGE.json"


def _run(*args):
    return subprocess.run([sys.executable, str(GATE), *args], capture_output=True, text=True,
                          cwd=str(ROOT), env={"OA_ROOT": str(ROOT), "PATH": "/usr/bin:/bin"})


def test_the_instrument_selftests_in_both_directions():
    r = _run("--selftest")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "controls pass" in r.stdout, r.stdout


def test_the_gate_runs_green_on_the_live_chain():
    """It must actually RUN the tool, not read a string (the E57 lesson)."""
    r = _run("--chain")
    assert r.returncode == 0, f"the chain has a citation or coverage violation:\n{r.stdout}"


def test_every_pinned_result_is_carried_by_the_chain():
    """The coverage direction, asserted here too so it fails even if the CLI is bypassed."""
    rows = json.loads(COVERAGE.read_text(encoding="utf-8"))["must_appear_in_chain"]
    text = LEDGER.read_text(encoding="utf-8")
    missing = [r["token"] for r in rows if r["token"] not in text]
    assert not missing, f"the chain dropped pinned result(s): {missing}"
    assert {"UNIQUENESS_THEOREM", "A1–A7"} <= {r["token"] for r in rows}, (
        "the genesis theorem must stay pinned — it went uncited for three months")


def test_the_genesis_theorem_is_real_and_locked():
    """The pin is only worth something if the thing it pins is green."""
    assert (ROOT / "docs" / "UNIQUENESS_THEOREM.md").exists()
    assert (ROOT / "tests" / "test_uniqueness_theorem.py").exists()
    body = (ROOT / "docs" / "UNIQUENESS_THEOREM.md").read_text(encoding="utf-8")
    assert "A = LR" in body and "[[2,1],[1,1]]" in body
    # its own honest limit must survive: it does NOT derive the axioms from anything weaker
    assert "Derive A1–A7 from anything weaker" in body or "derive A1–A7" in body.lower()


def test_C25_carries_the_fourteen_versus_twelve_scope():
    """The sentence that propagated to two downstream seats. Facts, not a word count."""
    t = LEDGER.read_text(encoding="utf-8")
    i = t.index("**C25 [")
    seg = t[i:t.index("**C26 [")]
    assert "14-dimensional" in seg and "**12**" in seg, "C25 lost its dimension scope"
    assert "B992" in seg and "B1096" in seg, "C25 must name both extra u(1)s' fates"
    assert "centralizer" in seg, "C25 must say the 14 is a centralizer, not the gauge algebra"


def test_the_two_new_no_gos_are_present_and_labelled():
    t = LEDGER.read_text(encoding="utf-8")
    assert "**C44 [NO-GO" in t and "**C45 [NO-GO" in t
    i44 = t.index("**C44 [NO-GO")
    seg = t[i44:t.index("**C45 [NO-GO")]
    assert "never three" in seg and "B1138" in seg, "C44 must state the fork and its arc"
    seg45 = t[t.index("**C45 [NO-GO"):]
    assert "B1096" in seg45 and "vanishes identically" in seg45


def test_the_census_still_passes_with_the_two_new_links():
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "checks" / "forcedness_census.py")],
                       capture_output=True, text=True, cwd=str(ROOT))
    assert r.returncode == 0, r.stdout + r.stderr
    # growth-safe: assert what B1243 did (two NO-GOs added, axioms untouched), not a snapshot
    import re as _re
    m = _re.search(r"FORCED \(non-axiom\): (\d+) of (\d+)", r.stdout)
    assert m, r.stdout
    forced, links = int(m.group(1)), int(m.group(2))
    assert links >= 45 and links - forced == 4, r.stdout
    assert _re.search(r"NO-GO\s+(\d+)", r.stdout), r.stdout
    assert int(_re.search(r"NO-GO\s+(\d+)", r.stdout).group(1)) >= 7, "C44/C45 must stay NO-GO"
