"""Two cases main wrote AFTER reading the second series' patches line by line (2026-11-12).  They are not unseen cases: they
were found by reading patches 3 and 5.  The question: a ceiling that FALLS and then RISES BACK to the value it had at the
rule's anchor.  Is the rise seen?

Each case is made in a small repository of its own with the helpers of the series' own lock, and each has a control: the same
rise with no fall before it, which the series catches.

    python3 a_ceiling_that_falls_and_rises_back.py <a checkout that has the series applied>
"""
import importlib.util, json, pathlib, sys, tempfile
W = pathlib.Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("lock", W / "tests" / "test_nothing_leaves_a_ledger.py")
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
out = {}
# ---- A: the identification baseline
with tempfile.TemporaryDirectory() as d:
    repo, anchor = L._scratch(pathlib.Path(d), L._REGISTER)                       # I-1 EARNED, I-2 UNEARNED; baseline 1
    out["A0 at the anchor"] = L._gate(repo, "identification-register", anchor)
    earned = L._IDENT.replace("| I-2 | two | A | B | x | y | **UNEARNED**", "| I-2 | two | A | B | x | y | **EARNED**")
    L._commit(repo, "the unearned row is earned and the baseline lowered to 0", {"docs/IDENTIFICATION_LEDGER.md": earned, "docs/IDENTIFICATION_BASELINE.json": L._baseline(0)})
    out["A1 after the fall"] = L._gate(repo, "identification-register", anchor)
    L._commit(repo, "a new unearned row, and the baseline moved back up to fit it, with no record",
              {"docs/IDENTIFICATION_LEDGER.md": earned + (L._UNEARNED % 3), "docs/IDENTIFICATION_BASELINE.json": L._baseline(1)})
    out["A2 after the rise back to the anchor's value (the plant)"] = L._gate(repo, "identification-register", anchor)
    # the control: the same plant without the fall first is caught (the lock's own case)
with tempfile.TemporaryDirectory() as d:
    repo, anchor = L._scratch(pathlib.Path(d), L._REGISTER)
    L._commit(repo, "a new unearned row and the baseline raised 1 -> 2, no record",
              {"docs/IDENTIFICATION_LEDGER.md": L._IDENT + (L._UNEARNED % 3), "docs/IDENTIFICATION_BASELINE.json": L._baseline(2)})
    out["A-control: the same rise with no fall before it"] = L._gate(repo, "identification-register", anchor)
# ---- B: the attribution baseline's table of ceilings
g = L._gates()
with tempfile.TemporaryDirectory() as d:
    repo = pathlib.Path(d) / "small"; repo.mkdir(); L._git(repo, "init", "-q")
    frozen = lambda counts: json.dumps({"_note": "a ratchet", "frozen": counts}) + "\n"
    anchor = L._commit(repo, "the anchor", {"docs/ATTRIBUTION_BASELINE.json": frozen({"a.md": 4})})
    L._commit(repo, "lowered", {"docs/ATTRIBUTION_BASELINE.json": frozen({"a.md": 2})})
    L._commit(repo, "raised back", {"docs/ATTRIBUTION_BASELINE.json": frozen({"a.md": 4})})
    real = g._load_attr_baseline
    g._load_attr_baseline = lambda: json.loads((repo / "docs" / "ATTRIBUTION_BASELINE.json").read_text())["frozen"]
    try:
        out["B after a fall 4 -> 2 and a rise back 2 -> 4 (the plant)"] = g.attribution_baseline_rise(anchor, repo)
        (repo / "docs" / "ATTRIBUTION_BASELINE.json").write_text(frozen({"a.md": 5}))
        out["B-control: a rise above the anchor's value"] = g.attribution_baseline_rise(anchor, repo)
    finally:
        g._load_attr_baseline = real
for k, v in out.items():
    print("%-66s %s" % (k, str(v)[:200]))
