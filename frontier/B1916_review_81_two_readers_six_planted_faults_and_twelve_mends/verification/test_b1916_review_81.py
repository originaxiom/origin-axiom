"""B1916's lock: the plants file is the one whose hash was published at the opening; each plant is in the reading commit
and not on main's window head; the recount is git's; the mends carry their markers. It writes nothing."""
import hashlib, pathlib, subprocess, sys, re
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))


def show(rev, path):
    r = subprocess.run(["git", "-C", str(ROOT), "show", f"{rev}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def test_the_plants_file_is_the_one_published_at_the_opening():
    h = hashlib.sha256((HERE / "plants.py").read_bytes()).hexdigest()
    assert h == "7ab2417be3674a113e95644aba4572ea89416246f20e2e2fdd475851b30967a3"
    assert "7ab2417b" in (show("a45e66fd1", "CHANGELOG.md") or "") + (show("a45e66fd1", "docs/POINT_REGISTER.md") or "")


def test_each_plant_is_in_the_reading_commit_and_not_in_the_window_head():
    import plants as P
    assert len(P.PLANTS) == 6
    for key, kind, path, old, new in P.PLANTS:
        read, head = show("7d7ab1dfa", path), show("0e637ea9e", path)
        if read is None or head is None:                  # a commit absent from a shallow clone: nothing to check here
            continue
        assert new in read and old in head and new not in head, key


def test_the_recount_is_gits():
    rec = (HERE / "recount_row18.txt").read_text()
    assert "e6298271a: test_b*.py at the top of tests/ 1407; test_*.py at the top 1522; test_*.py at any depth 1537" in rec


def test_the_mends_carry_their_markers():
    pages = [ROOT / "frontier" / d / f for d, f in (
        ("B1898_review_80_one_hundred_findings_and_what_main_checked", "FINDINGS.md"),
        ("B1898_review_80_one_hundred_findings_and_what_main_checked", "STATUS_OF_THE_57.md"),
        ("B1892_review_79_read_by_those_who_did_not_build_it", "FINDINGS.md"))]
    text = "".join(p.read_text(encoding="utf-8") for p in pages)
    assert len(re.findall(r"CORRECTED 2026-11-13 \(Review 81, ", text)) >= 9
