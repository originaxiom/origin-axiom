"""B646 locks — the cc2 wave-2 integration."""
import hashlib
import os
import subprocess

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
B646 = os.path.join(HERE, "..", "frontier", "B646_wave2_integration")
PK = os.path.join(B646, "cc2_packets")

# the two disclosed privacy patches (archive differs from as-received manifest)
PATCHED = {
    "next_queue/next_queue/n4_receipt/FINDINGS_CC2.md",
    "next_queue/next_queue/n3_fine_grid/FINDINGS_CC2.md",
}

SEALS = {
    "residuals/level_ladder_campaign/PREREG_L7.md": "0c4df92d",
    "residuals/level_ladder_campaign/scripts/level7_run.py": "70a41662",
    "residuals/residuals_loop/r2_injectivity/H_R2_SEALED.md": "0982d8e0",
    "next_queue/next_queue/n1_counting/PREREG_N1.md": "aa47092d",
    "next_queue/next_queue/n2_clock_law/PREREG_N2.md": "8393e404",
    "next_queue/next_queue/n2_clock_law/ADDENDUM_N2.md": "09fc3565",
    "next_queue/next_queue/n3_fine_grid/PREREG_N3.md": "09246f08",
    "proof_queue/proof_queue/q3_proofs/ERRATUM_N1.md": "cbb83a82",
    "proof_queue/proof_queue/q1_level8/PREREG_Q1.md": "f3b19098",
    "proof_queue/proof_queue/q1_level8/level8_run.py": "a415f881",
    "proof_queue/proof_queue/q2_conductor/PREREG_Q2.md": "287bfe86",
}


def _sha8(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:8]


def test_eleven_seals_live():
    for rel, h8 in SEALS.items():
        assert _sha8(os.path.join(PK, rel)) == h8, rel


def test_archive_matches_manifest_except_disclosed():
    man = {}
    for ln in open(os.path.join(PK, "ORIGINALS_MANIFEST.txt")):
        if ln.startswith("#") or not ln.strip():
            continue
        h, rel = ln.split(None, 1)
        man[rel.strip()] = h
    mismatches = []
    for rel, h in man.items():
        p = os.path.join(PK, rel)
        if not os.path.exists(p):
            mismatches.append(("MISSING", rel))
            continue
        got = hashlib.sha256(open(p, "rb").read()).hexdigest()
        if got != h and rel not in PATCHED:
            mismatches.append(("HASH", rel))
    # A HASH mismatch is the integrity failure this lock exists to catch and is always
    # fatal.  A MISSING file is a different thing: .gitignore's LaTeX rule `*.log` also
    # matches every cc2 packet log, so those originals were never committed and no clone
    # has them.  That is an incomplete archive, not a corrupted one -- say so precisely
    # instead of reporting it as a hash failure.  (A negation for this path is in
    # .gitignore so a bench that still holds the logs can commit them; then this passes
    # outright everywhere.)
    hashes = [m for m in mismatches if m[0] == "HASH"]
    assert hashes == [], hashes
    missing = [rel for kind, rel in mismatches if kind == "MISSING"]
    if missing:
        untracked = [rel for rel in missing
                     if subprocess.run(["git", "ls-files", "--error-unmatch",
                                        os.path.join(PK, rel)],
                                       capture_output=True, cwd=B646).returncode != 0]
        assert set(untracked) == set(missing), (
            "manifest names files that ARE tracked but are absent from the working "
            f"tree: {sorted(set(missing) - set(untracked))}")
        pytest.skip(f"{len(missing)} manifest originals were never committed "
                    f"(gitignored *.log); every file present matches its hash: "
                    f"{sorted(missing)[:3]} ...")
    # the two patched files must actually differ (the patch is real)
    for rel in PATCHED:
        got = hashlib.sha256(
            open(os.path.join(PK, rel), "rb").read()).hexdigest()
        assert got != man[rel], rel


def test_findings_carries_the_erratum_and_ladder():
    fnd = open(os.path.join(B646, "FINDINGS.md")).read()
    assert "Z(κ) = (1 − (κ|5))/2" in fnd
    assert "{+1, +1, +1, 0, +1, +1, 2}" in fnd
    assert "NO COLLISION" in fnd
    assert "NEEDS-SPECIALIST" in fnd
