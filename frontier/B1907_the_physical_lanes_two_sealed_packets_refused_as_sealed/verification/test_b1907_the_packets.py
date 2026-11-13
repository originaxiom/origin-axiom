"""B1907's lock. It recomputes the custody of both packets from the lane's sealed commits (the branch must be fetched),
holds the page and the verdict line to the computed counts and to the kept quotation checks, and plants a changed hash
that the custody check must see. It writes nothing."""
import sys, json, re, pathlib, subprocess, pytest
HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
sys.path.insert(0, str(HERE))
import custody_on_main as C
PAGE = re.sub(r"\s+", " ", (ARC / "FINDINGS.md").read_text(encoding="utf-8"))
LINE = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]

def _have(rev):
    return subprocess.run(["git", "cat-file", "-e", rev + "^{commit}"], capture_output=True).returncode == 0

needs_lane = pytest.mark.skipif(not all(_have(r) for r in ("bda89f04a94d09217551cef96056f375b21c260b", "d1a33e921d5cb16e4606b196fa970b91a2abfb6d", C.HEAD)),
                                reason="the physical lane's branch is not fetched in this clone")

@needs_lane
def test_custody_holds_and_is_what_the_page_says():
    out = C.custody(quiet=True)
    kept = json.loads((HERE / "custody_on_main.json").read_text(encoding="utf-8"))
    for name in ("packet 1", "packet 2"):
        o = out[name]
        assert o["pins"] == o["equal at the sealed commit"] == o["equal at the lane's head"] == kept[name]["pins"]
        assert o["not equal at the seal"] == []
    assert (out["packet 1"]["pins"], out["packet 2"]["pins"]) == (63, 41)
    assert "63 of 63 and 41 of 41" in LINE and "| 63 of 63, and 63 of 63;" in PAGE and "| 41 of 41, and 41 of 41 |" in PAGE

@needs_lane
def test_a_changed_hash_is_seen():
    """plant: one artifact of packet 2 hashes to something else at its sealed commit; custody must count it as not equal"""
    real = C.blob
    seen = []
    def planted(rev, path):
        if rev.startswith("d1a33e921") and not path.endswith("SPECIFICATION.json") and (not seen or seen[0] == path):
            seen[:] = [path]
            return "0" * 64
        return real(rev, path)
    C.blob = planted
    try:
        out = C.custody(quiet=True)
    finally:
        C.blob = real
    assert out["packet 2"]["equal at the sealed commit"] == out["packet 2"]["pins"] - 1 and out["packet 2"]["not equal at the seal"] == seen
    assert out["packet 1"]["equal at the sealed commit"] == out["packet 1"]["pins"]

def test_the_quotation_checks_are_what_the_page_says():
    p1 = json.loads((HERE / "quote_check_readers_packet1.json").read_text(encoding="utf-8"))
    p2 = json.loads((HERE / "quote_check_readers_packet2.json").read_text(encoding="utf-8"))
    reg = json.loads((HERE / "quote_check_packet1_math_registry.json").read_text(encoding="utf-8"))
    assert p1["code"]["quotations"] == p1["code"]["found on one line"] == 94 and p2["code"]["quotations"] == p2["code"]["found on one line"] == 47
    assert reg["quotations in the registry"] == reg["found at the line named"] == 63 and reg["controls found"] == 0
    assert (p2["math"]["found in a pinned file"], p2["math"]["quotations"]) == (84, 91)
    assert (p1["math"]["found in a pinned file"], p1["math"]["quotations"]) == (22, 35)
    assert "code 94 of 94; mathematics 63 of 63 at the line named" in PAGE
    assert "code 47 of 47; mathematics 84 of 91 exact" in PAGE
    assert "35 passages in double quotation marks" in PAGE and "22 of them are found in a pinned file and 13 are not" in PAGE

def test_the_decision_and_what_a_reseal_needs():
    assert "**Neither packet is accepted for execution as sealed.**" in PAGE
    assert "ARE NOT ACCEPTED FOR EXECUTION AS SEALED" in LINE
    section = PAGE.split("## 4. What a reseal needs", 1)[1].split("## 5.", 1)[0]
    assert re.findall(r" (\d)\. ", " " + section) == ["1", "2", "3", "4", "5", "6", "7"]
    for f in ("verification/readers/packet1_REVIEW_CODE.txt", "verification/readers/packet1_REVIEW_MATHEMATICS.txt",
              "verification/readers/packet2_REVIEW_CODE.txt", "verification/readers/packet2_REVIEW_MATHEMATICS.txt"):
        assert (ARC / f).is_file(), f
