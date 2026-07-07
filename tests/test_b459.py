"""Lock for B459 — the Klein-four/subfield-lattice verification (exact)."""
import os
import subprocess
import sys

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B459_klein_four_verification")


def test_patterns_verify():
    out = subprocess.run([sys.executable, "verify_patterns.py"], cwd=HERE,
                         capture_output=True, text=True, timeout=600).stdout
    assert "total patterns occurring: 5 of 16" in out
    assert "Law 1 (no single vanishing): PASS" in out
    assert "Law 2 (s=sqrt-15 dies in every nontrivial pattern): PASS" in out
    assert "patterns == the subfield lattice of Q(sqrt5,sqrt-3): True" in out
    assert "the Q(sqrt-15)-valued pattern (q,r dead, s alive) occurs: False" in out
    assert "counts match the addendum (120/20/20/10/70): True" in out
