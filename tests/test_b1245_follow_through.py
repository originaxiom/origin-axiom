"""B1245 — the follow-through: the three statements reach the CHAIN, not just the log."""
import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
LED = ROOT / "docs" / "THEOREM_LEDGER.md"

def _link(cid):
    t = LED.read_text(encoding="utf-8"); i = t.index(f"**{cid} [")
    nxt = t.find("\n**C", i + 5)
    return t[i:nxt if nxt > 0 else len(t)]

def test_C43_carries_its_group_independence_scope():
    seg = _link("C43")
    assert "group-independent" in seg.lower(), "C43 lost the scope (it lived only in the log once)"
    assert "no group parameter" in seg.lower() and "crossing.py" in seg
    assert "desert configuration" in seg, "the scope must say WHAT the kill is about"

def test_C44_carries_the_borromean_sharpening_and_REFUSES_the_heisenberg_identification():
    seg = _link("C44")
    assert "BORROMEAN" in seg.upper() and "not pairwise" in seg.lower()
    assert "uncertainty relation" in seg.lower(), "the distinction must be stated, not implied"
    assert "B1087" in seg, "the real comparison must be named"
    # and it must NOT assert the identification
    assert "is an uncertainty relation" not in seg.lower()

def test_E59_is_minted_with_the_owners_words():
    el = (ROOT / "docs" / "ERROR_LEDGER.md").read_text(encoding="utf-8")
    assert "E59" in el and "FOUND-BUT-NOT-REVERIFIED" in el
    assert "reverify it in the new light" in el, "the class must carry the words that named it"

def test_the_discriminating_fact_is_RUN_not_asserted():
    r = subprocess.run([sys.executable, "verification/b1245_no_group_parameter.py"],
                       capture_output=True, text=True,
                       cwd=str(ROOT / "frontier" / "B1245_follow_through"),
                       env={"OA_ROOT": str(ROOT), "PATH": "/usr/bin:/bin"})
    assert r.returncode == 0, r.stdout + r.stderr
    assert r.stdout.rstrip().endswith("REPRODUCES"), r.stdout[-400:]

def test_B915s_code_really_has_no_group_parameter():
    """asserted here too, so it fails even if the CLI is bypassed"""
    import ast, re
    src = (ROOT / "frontier" / "B915_the_crossing" / "crossing.py").read_text(encoding="utf-8")
    fn = next(n for n in ast.walk(ast.parse(src))
              if isinstance(n, ast.FunctionDef) and n.name == "curve_point")
    assert [a.arg for a in fn.args.args] == ["MU", "two_loop"]
