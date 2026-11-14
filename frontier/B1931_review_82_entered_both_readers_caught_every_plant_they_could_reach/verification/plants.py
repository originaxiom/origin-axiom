"""Review 82's six planted faults (main, 2026-11-14). Applied only to the reading copy (branch review-82/read); this file is
kept in the audit room until the review's entry, and its sha256 is published at the opening. Usage: python3 plants.py DIR"""
import glob, pathlib, sys
PLANTS = [
 ("P1", "a number off its source", "frontier/B1927_*/FINDINGS.md",
  "| L_max, the maximal horoball | **1.99** (both angles) | 1.98 |", "| L_max, the maximal horoball | **1.79** (both angles) | 1.98 |"),
 ("P2", "a stronger label", "frontier/B1928_*/FINDINGS.md",
  "**Verdict: OPEN** (a proof sketch from standard ergodic theory, with three hypotheses to check;", "**Verdict: OPEN** (a proof from standard ergodic theory, every hypothesis checked;"),
 ("P3", "a check that cannot fail", "frontier/B1929_*/verification/test_b1929_twisted_eta.py",
  "    assert worst < 1e-10\n", "    assert worst < 1e10\n"),
 ("P4", "a session as an authority", "frontier/B1926_*/FINDINGS.md",
  "- **The web seat's W-F4** (harvest row 1773).", "- **The web seat's W-F4** (harvest row 1773), whose reading settles it."),
 ("P5", "a wider claim", "frontier/B1925_*/FINDINGS.md",
  "So the tick's structure picks **every odd metallic act**", "So the tick's structure picks **every metallic act**"),
 ("P6", "a number off its source", "frontier/B1924_*/FINDINGS.md",
  "has median ∣z∣ 0.74, 92 % within two errors.", "has median ∣z∣ 0.74, 98 % within two errors."),
]
if __name__ == "__main__":
    root = pathlib.Path(sys.argv[1])
    for pid, kind, g, old, new in PLANTS:
        f = pathlib.Path(glob.glob(str(root / g))[0]); t = f.read_text()
        assert t.count(old) == 1, pid
        f.write_text(t.replace(old, new))
    print("six plants applied")
