"""B1655 -- main audits its negatives (P-152): GENESIS v1.46 is the amendment of the received v1.45; the 24 verdict files
and 24 FINDINGS carry the audit; B1648's conditions are in four hypotheses; the public refresh blocks, the outside-review
page, THE_WEAVE, LAW_MAP and THEOREM_REGISTRY carry the scopes and their rows parse; the kill graph's printed text carries
the audit; B1604's lock no longer ends 'or True'; the three phrases are swept. The bite: the edits refuse to apply twice,
the amendment refuses another source, and the potential check shows minima between the cone and the real locus."""
import glob, json, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1655_main_audits_its_negatives"
TAG = "[Audited by main (P-152, B1655, 2026-10-15):"
AUDITED = ("B1602 B1603 B1604 B1606 B1615 B1616 B1617 B1618 B1620 B1628 B1633 B1635 B1641 B1642 B1643 B1644 B1645 "
           "B1646 B1648 B1649 B1651 B1652 B1653 B1654").split()
POINTED = ("B1602 B1603 B1604 B1606 B1615 B1616 B1617 B1618 B1620 B1628 B1629 B1630 B1632 B1633 B1635 B1637 B1641 "
           "B1642 B1643 B1644 B1646 B1651 B1652 B1653").split()


def _verdict(b):
    return json.load(open(glob.glob(str(ROOT / "frontier" / ("%s_*" % b) / "arc_verdict.json"))[0]))


def _cells(line):
    return len(re.split(r"(?<!\\)\|", line)) - 2


def test_genesis_v1_46_is_the_amendment():
    assert subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"]).returncode == 0
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    assert "**Version 1.46 · 2026-10-15 · canonical.**" in g and "- **v1.46 · 2026-10-15 · main B1655.**" in g
    for s in ("[v1.46] Withdrawn in part (main's audit of its negatives, P-152, B1655; B1604 §2b, B1605 R2)",
              "Six kinds on certified covers, not eight", "B1646's \"never between\" holds for a quartic potential",
              "Not forced for a point or density Higgs (B1651's premise P1, tested by no cell)",
              "have no cell: no spectrum near ω was computed"):
        assert s in g, s


def test_the_verdict_files_and_findings_carry_the_audit():
    for b in AUDITED:
        assert TAG in _verdict(b)["claim_one_line"], b
    for b in ("B1642", "B1644", "B1645", "B1646"):
        assert "B1648's conditions, applied by B1655" in json.dumps(_verdict(b)["scope"]["hypotheses"]), b
    for b in POINTED:
        f = glob.glob(str(ROOT / "frontier" / ("%s_*" % b) / "FINDINGS.md"))[0]
        assert "Audited 2026-10-15 by main (P-152, B1655)" in open(f, encoding="utf-8").read(), b
    v = json.load(open(A / "arc_verdict.json"))
    assert v["verdict"] == "PROVED" and not v["creates_law"] and "0 of 19." in v["claim_one_line"]


def test_the_pages_carry_the_scopes_and_their_tables_parse():
    for f in ("README.md", "ROADMAP.md", "docs/MASTERPLAN.md", "docs/OPEN_PROBLEMS.md", "docs/LEAD_REGISTER.md",
              "docs/PRICED_DOORS.md"):
        t = (ROOT / f).read_text(encoding="utf-8")
        assert "every weight (scoped by B1655: where the inner automorphisms act)" in t, f
        assert "by themselves (withdrawn, B1655)." in t, f
    ds = (ROOT / "docs" / "THE_DERIVED_STRUCTURE_FOR_REVIEW.md").read_text(encoding="utf-8")
    assert "this paragraph was computed where the inner automorphisms are symmetries" in ds
    w = (ROOT / "docs" / "THE_WEAVE.md").read_text(encoding="utf-8")
    assert w.count("*(Audited 2026-10-15, B1655:") == 13
    for f, n in (("docs/LAW_MAP.md", 3), ("docs/THEOREM_REGISTRY.md", 5)):
        rows = [l for l in (ROOT / f).read_text(encoding="utf-8").split("\n") if l.startswith("|") and "B1655" in l]
        assert rows and all(_cells(l) == n for l in rows), f
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8").split("\n")
    assert all(_cells(l) == 5 for l in reg if l.startswith("| T-FIBRE-LOOPS-PARITY") or l.startswith("| T-RESIDUE-ANTISYMMETRIC"))


def test_the_kill_graph_the_lock_and_the_sweep():
    g = json.load(open(ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json", encoding="utf-8"))
    marked = {r["id"] for r in g if "Audited, B1655" in r.get("kill_form", "")}
    assert marked == {"B1629", "B1632", "B1635", "B1642", "B1644"}
    lock = (ROOT / "tests" / "test_b1604_the_class_index_is_not_an_index.py").read_text(encoding="utf-8")
    assert not re.search(r"^\s*assert .* or True\s*$", lock, re.M) and "(1, 3, 16)" in lock
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    import retraction_sweep
    ph = retraction_sweep._phrases()
    for p in ("τ = ω gives degenerate masses at every weight", "explains W72's rank 3",  # retracted phrases, quoted to lock or bracket them
              "zero modes give no flavour structure by themselves. Their residue coupling"):  # retracted phrases, quoted to lock or bracket them
        assert p in ph, p


def test_bite_the_edits_refuse_to_apply_twice_and_the_amendment_another_source(tmp_path):
    r = subprocess.run([sys.executable, "-B", str(A / "verification" / "apply_audit.py"), str(ROOT), "--dry"],
                       capture_output=True, text=True)
    assert r.returncode == 1 and "PROBLEMS:" in r.stdout
    src = (A / "adoption" / "amend.py").read_text(encoding="utf-8")
    bad = tmp_path / "GENESIS_v1_45_main.md"; bad.write_text("not v1.45\n", encoding="utf-8")
    ns = {"__name__": "x", "__file__": str(A / "adoption" / "amend.py")}
    exec(compile(src, "amend", "exec"), ns); ns["SRC"] = str(bad)
    try:
        ns["build"](); raised = False
    except AssertionError:
        raised = True
    assert raised


def test_bite_the_potential_check_has_minima_between():
    run = (A / "verification" / "check_potential_run.txt").read_text(encoding="utf-8")
    assert "lam2=-0.05 kappa=0.5: defect |a.a|/|a|^2 in [0.447,0.447]" in run and "40/40" in run
    assert "lam2=-0.02 g=  0.1: defect in [0.912,0.912]  m in [0.323,0.323]  #minima with 1e-3<m<0.45: 40/40" in run
