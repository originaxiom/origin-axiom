"""S1 -- the paper's bibliography must be functional, not decorative.

Found by the submission campaign: 12 of 13 bibitems were never cited. LaTeX prints an unused
bibitem WITHOUT warning, so the build was clean while no claim pointed at any source. These
tests make that state unreachable again.
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "checks" / "paper_citations.py"


def _run(*a):
    return subprocess.run([sys.executable, str(SCRIPT), *a],
                          capture_output=True, text=True, cwd=str(ROOT))


def test_no_citation_defects():
    r = _run()
    assert r.returncode == 0, r.stdout + r.stderr
    m = re.search(r"DEFECTS: (\d+)", r.stdout)
    assert m and m.group(1) == "0", r.stdout


def test_every_bibitem_is_cited():
    """A reference nothing points at is furniture, not a reference."""
    out = _run().stdout
    n = int(re.search(r"bibitems nothing cites \(furniture\): (\d+)", out).group(1))
    assert n == 0, out


def test_checker_can_fail():
    """MB12, both defect kinds planted."""
    r = _run("--selftest")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "PLANT uncited bibitem      reported: True" in r.stdout, r.stdout
    assert "PLANT citation-free appeal reported: True" in r.stdout, r.stdout


def test_terminology_is_not_demanded_a_citation():
    """The instrument must not train the author to add furniture: names used as standard
    terminology (Weyl data, Galois, Jordan) are deliberately outside the appeal list."""
    src = SCRIPT.read_text(encoding="utf-8")
    assert "Weyl" not in src.split("NAMED = [")[1].split("]")[0]
    assert "terminology" in src.lower()
