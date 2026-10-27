"""B1784 -- the agy lane audited.  The four auditors' reports are carried; the findings keep 0 of 19 and name the one
re-banked arc; no vendor name and no absolute path in the arc."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1784_the_agy_lane_audited"


def test_the_audit_is_carried():
    for f in ("A_B1758.md", "B_B1759_B1761.md", "C_B1762_B1764.md", "D_B1765_B1782.md", "FINDINGS.md"):
        assert (A / f).exists()
    t = (A / "FINDINGS.md").read_text(encoding="utf-8")
    assert "0 OF 19 STANDS" in t and "re-banked as main's B1758" in t and "**0 of 19.**" in t


def test_no_vendor_name_or_absolute_path():
    bad = re.compile(r"/Us" + r"ers/|/pri" + r"vate/|\bgo" + r"ogle\b|anti" + r"gravity", re.I)   # assembled from fragments, as B1426's survey does
    for f in A.glob("*.md"):
        assert not bad.search(f.read_text(encoding="utf-8")), f.name
