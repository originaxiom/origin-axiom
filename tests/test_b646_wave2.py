"""B646 locks — the cc2 wave-2 integration."""
import hashlib
import os

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


def _git_ignores(path):
    """True iff git itself refuses to track this path (B1041). Asking git rather than matching
    extensions keeps the exemption honest: it covers exactly what could never be committed."""
    import subprocess
    r = subprocess.run(["git", "check-ignore", "-q", os.path.abspath(path)],
                       cwd=os.path.join(HERE, ".."), capture_output=True)
    return r.returncode == 0


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
            # B1041: a manifest entry can be UNVERSIONABLE -- `.gitignore:20` is `*.log`, so git
            # refused those paths and no clone has ever had them (60 of 366 entries across the
            # nine manifest-bearing harvest arcs). That is a disclosed, single-caused gap, NOT
            # rot. It is exempted ONLY when git itself confirms the path is ignored, so a
            # genuinely lost file still fails this lock.
            if _git_ignores(p):
                continue
            mismatches.append(("MISSING", rel))
            continue
        got = hashlib.sha256(open(p, "rb").read()).hexdigest()
        if got != h and rel not in PATCHED:
            mismatches.append(("HASH", rel))
    assert mismatches == [], mismatches
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


def test_the_manifest_gap_is_real_and_bounded__B1041():
    """The exemption above must not become a blanket. Locks the SHAPE of the gap: every missing
    entry is git-ignored, and the count is bounded -- so if a tracked packet file ever vanishes,
    or the ignore rule widens, this fails."""
    man = {}
    for ln in open(os.path.join(PK, "ORIGINALS_MANIFEST.txt")):
        if ln.startswith("#") or not ln.strip():
            continue
        h, rel = ln.split(None, 1)
        man[rel.strip()] = h
    absent = [r for r in man if not os.path.exists(os.path.join(PK, r))]
    assert absent, "if nothing is absent the gap closed -- update B1041"
    assert all(_git_ignores(os.path.join(PK, r)) for r in absent), \
        [r for r in absent if not _git_ignores(os.path.join(PK, r))]
    assert len(absent) <= 15, len(absent)
    assert all(r.endswith((".log", ".pyc")) for r in absent), absent
