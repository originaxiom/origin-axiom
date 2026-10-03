"""B1460 -- GENESIS v1.5: the owner's two decisions, and the audit lane's refinement of GAP3."""
import importlib.util, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1460_genesis_v1_5_the_owners_two_decisions")


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(A, rel)); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_amend_reproduces_the_page_at_v1_5():
    am = load("adoption/amend.py", "amend_b1460")
    t = am.build(); assert len(am.CHANGES) == 7
    cur = open(os.path.join(ROOT, "GENESIS.md")).read()
    if "**Version 1.5 ·" in cur: assert cur == t


def test_the_decisions_are_in_the_page_and_propagated():
    g = open(os.path.join(ROOT, "GENESIS.md")).read()
    assert "| FK1 | The principle's single wording (§1) | **[v1.5] CONFIRMED** (the owner, 2026-10-03) |" in g
    assert "**[v1.5] The register** (the owner's framing, decided 2026-10-03)" in g and "a word and its reverse are one manifold (B1456)" in g
    assert "Is the register that keeps the order part of the state, carried by the act, or an input from outside?" in g
    assert "that the act generates the register rather than receives it" in g
    assert "- **v1.5 · 2026-10-03 · main B1460.**" in g and "**Pending the owner:**" not in g and "owner to confirm" not in g
    assert "do\n  not prove that a one-ended state can get the third *only* from a relation" in g
    r = open(os.path.join(ROOT, "README.md")).read()
    import re
    assert "confirmed by the owner on 2026-10-03 (fork FK1, GENESIS v1.5)" in r and "awaits the owner" not in r
    v = re.search(r"`GENESIS.md` \(v1\.(\d+)\)", r); assert v and int(v.group(1)) >= 5      # the README names the current version, 1.5 or later
    p = open(os.path.join(ROOT, "docs", "THE_FOUNDATION_LOCK_PLAN.md")).read()
    assert "S43 (B1460). FK1 and FK12 decided by the owner" in p
