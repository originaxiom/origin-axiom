"""The seal gates read a ledger row by its cells from the right (B1456; found by the SM seat's lane): a "|" inside a
row's description no longer hides the row from both gates."""
import importlib.util, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("gates", os.path.join(ROOT, "scripts", "gates", "gates.py"))
gates = importlib.util.module_from_spec(spec); spec.loader.exec_module(gates)
H = "a" * 64


def test_a_pipe_in_the_description_does_not_hide_the_row():
    row = "| 2026-09-01 | a seal with a | pipe in its description | `frontier/x/PREREG.md` | `%s` |" % H
    assert gates._seal_ledger_rows(row) == [("2026-09-01", "frontier/x/PREREG.md", H)]
    old = re.match(r"\|\s*\d{4}-\d{2}-\d{2}\s*\|[^|]*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`", row)
    assert old is None, "the old pattern skipped this row: the control"


def test_plain_rows_branch_rows_and_rows_without_a_digest():
    t = "\n".join(["| 2026-08-21 | a seal | `docs/A.md` | `%s` |" % H,
                   "| 2026-08-05 | a branch seal | cc3 branch cell9 | `da516046` |",
                   "| 2026-08-06 | a seal without a digest | `docs/B.md` | pending |",
                   "| sealed document | sha8 | banked in |"])
    assert gates._seal_ledger_rows(t) == [("2026-08-21", "docs/A.md", H), ("2026-08-06", "docs/B.md", None)]


def test_the_ledger_is_read_and_both_gates_pass():
    rows = gates._seal_ledger_rows(open(os.path.join(ROOT, "docs", "SEAL_LEDGER.md")).read())
    assert len(rows) >= 19 and all(os.sep not in r[1] or "/" in r[1] for r in rows)
    assert gates.gate_seal_provenance()[0] is True and gates.gate_seal_digests()[0] is True
