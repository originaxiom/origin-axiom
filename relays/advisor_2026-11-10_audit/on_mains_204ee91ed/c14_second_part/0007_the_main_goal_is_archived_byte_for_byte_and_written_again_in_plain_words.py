#!/usr/bin/env python3
"""C14, patch 7, as a script and not as a diff: the main goal's page is archived byte for byte beside it, and written
again in plain words.

A diff of this change would carry, in its added lines (the archive) and in its removed lines (the page), passages that
quote a person. So the archive is made here by copying the page's own bytes in the checkout, and no line of it is written
in this file.

    python3 <this file> <a clean checkout of the series before this patch>

It stages what it changes and prints the tree, and says whether it is the tree this seat built. It commits nothing: the
message is 0007_message.txt, beside this file.
"""
import subprocess, sys
EXPECTED = "6ce6816c54264c4cc240250fdb30c582044cfa7a"
root = sys.argv[1]
if subprocess.run(["git", "-C", root, "status", "--porcelain"], capture_output=True, text=True).stdout.strip():
    sys.exit("STOPPED, nothing written: the checkout is not clean")
sys.argv = [sys.argv[0], root]

import hashlib, os, re, subprocess, sys
wt = sys.argv[1]; os.chdir(wt)
PAGE, HIST = "docs/MAIN_GOAL.md", "docs/MAIN_GOAL_HISTORY.md"
old = open(PAGE, encoding="utf-8").read()
assert "Its state is **0 of 19**" in old
digest = hashlib.sha256(old.encode("utf-8")).hexdigest()

head = ("# The main goal's page as it stood until 2026-11-13, archived byte for byte\n\n"
        "*Archived on 2026-11-13, when the page was written again in plain words for a reader outside the project. Everything\n"
        "after the marker below is `docs/MAIN_GOAL.md` as it stood when it was archived (after the plain rewording of its\n"
        "opening lines, 2026-11-13), byte for byte: its dated paragraphs from 2026-09-06 on, its three joins as they were\n"
        "then written, and its rule. Its paths are written from the repository root. The sha-256 of the archived text:\n"
        "`%s`. The current page is `docs/MAIN_GOAL.md`.*\n\n"
        "<!-- ARCHIVE:BEGIN -->\n" % digest)
open(HIST, "w", encoding="utf-8").write(head + old)

new = """# The main goal

*What the programme works towards, in plain words; each line names where it comes from. The page as it was written from
2026-09-06 to 2026-11-13 (its dated paragraphs, its three joins in detail, the frame it settled and its rule as first
written) is archived byte for byte in [`MAIN_GOAL_HISTORY.md`](MAIN_GOAL_HISTORY.md), and each source below is a section
of it.*

## The goal

To derive the nineteen free parameters of the Standard Model from the object, and to keep the work on that until it is
done. It was set on 2026-09-06 (the archive, its opening lines).

Its state is **0 of 19**: no parameter has been derived (the archive, its note of 2026-10-30; the current state is in
`docs/CAMPAIGN_STATUS.md`, its newest entries, which belong to the working record).

## Three joins, in order

The goal is approached through three joins between the object and the Standard Model (the archive, "JOIN 1", "JOIN 2",
"JOIN 3"):

1. **The count of generations:** whether the object gives three generations of matter, read in a frame that can carry
   chirality. The frame was chosen on 2026-09-06 (the archive, "The frame").
2. **The values:** whether the numbers the frames read are fixed by the object.
3. **Dynamics:** how the interactions meet.

## The rule

The joins are worked in order. A join is left only when it is earned, refuted, or blocked by a computation that is named
and registered. A join that does not hold is worse than one not made: each must be shown to act, and before work builds
on a frame, what that frame provably cannot produce is checked against the target (the archive, "The rule of no drift"
and "The thesis, and the discipline it needs").

## Where it stands

The current state, the order of work and the open questions are kept in the working record: `docs/CAMPAIGN_STATUS.md`
and `docs/POINT_REGISTER.md`. The foundations are in `GENESIS.md`.
"""
open(PAGE, "w", encoding="utf-8").write(new)

# the lock of B1294 reads the dated sentence in the archive
p = "tests/test_b1294_the_chirality_bit.py"; s = open(p, encoding="utf-8").read()
o = '''    mg = (ROOT / "docs" / "MAIN_GOAL.md").read_text(encoding="utf-8")
'''
n = '''    # 2026-11-13 (C14, patch 7): the main goal's dated paragraphs are archived byte for byte in docs/MAIN_GOAL_HISTORY.md
    mg = (ROOT / "docs" / "MAIN_GOAL_HISTORY.md").read_text(encoding="utf-8")
'''
assert s.count(o) == 1
open(p, "w", encoding="utf-8").write(s.replace(o, n))

# the outside bench's certificates quote two sentences of the dated page
for p in ("outside_bench/certificates/require_and_test_cell10.py",):
    s = open(p, encoding="utf-8").read()
    k = s.count('("docs/MAIN_GOAL.md", ')
    if k:
        s = s.replace('("docs/MAIN_GOAL.md", ', '("docs/MAIN_GOAL_HISTORY.md", ')   # 2026-11-13 (C14, patch 7): archived byte for byte
        open(p, "w", encoding="utf-8").write(s)
    print(p, k)

# the arrival gate leaves the archive unread, as it leaves the README's
p = "scripts/gates/gates.py"; s = open(p, encoding="utf-8").read()
o = '"docs/README_HISTORY.md", '
assert s.count(o) == 1
s = s.replace(o, '"docs/README_HISTORY.md", "docs/MAIN_GOAL_HISTORY.md", ', 1)
held = re.search(r"^    'docs/MAIN_GOAL\.md': \{[^\n]*\},\n", s, re.M)
assert held
s = s[:held.start()] + "    # docs/MAIN_GOAL.md: at zero since C14's seventh patch (2026-11-13)\n" + s[held.end():]
open(p, "w", encoding="utf-8").write(s)
print("patch 7 written; archived", digest[:12])

p = "outside_bench/certificates/require_and_test_cell10.py"; s = open(p, encoding="utf-8").read()
o = "# quotations the addenda attribute to OTHER files -- must be present there\n"
assert s.count(o) == 1
s = s.replace(o, o + "# 2026-11-13 (C14, patch 7): the main goal's dated paragraphs are archived byte for byte in docs/MAIN_GOAL_HISTORY.md\n")
open(p, "w", encoding="utf-8").write(s)

p = "tests/test_public_face.py"; s = open(p, encoding="utf-8").read()
open(p, "w", encoding="utf-8").write(s + '\n\ndef _archive(text):\n    head, body = text.split("<!-- ARCHIVE:BEGIN -->\\n", 1)\n    import hashlib, re\n    said = re.search(r"The sha-256 of the archived text:\\s*`([0-9a-f]{64})`", head).group(1)\n    return said, hashlib.sha256(body.encode("utf-8")).hexdigest(), body\n\n\ndef test_the_main_goal_is_archived_byte_for_byte_and_its_page_is_plain():\n    """C14, patch 7 (main\'s M25, answer 1): the main goal\'s page as it stood is archived byte for byte beside it, held by\n    the hash its head gives; the living page uses no inner word, links the archive, and keeps the line the generator and\n    the programme\'s page read. Planted: one character of the archive changed."""\n    g = _gates()\n    hist = (ROOT / "docs" / "MAIN_GOAL_HISTORY.md").read_text(encoding="utf-8")\n    said, got, body = _archive(hist)\n    assert said == got\n    assert body.startswith("# THE MAIN GOAL") and "counts 2" in body\n    page = (ROOT / "docs" / "MAIN_GOAL.md").read_text(encoding="utf-8")\n    assert dict(g.public_face_words(page)) == {}\n    assert "(MAIN_GOAL_HISTORY.md)" in page and "Its state is **0 of 19**" in page\n    assert "docs/MAIN_GOAL.md" not in g.PUBLIC_FACE_HELD\n    planted = hist.replace("counts 2", "counts 3", 1)\n    s2, g2, _ = _archive(planted)\n    assert s2 != g2\n')

subprocess.run(["git", "-C", root, "add", "-A"], check=True)
tree = subprocess.run(["git", "-C", root, "write-tree"], capture_output=True, text=True).stdout.strip()
print("the tree: %s" % tree)
print("it is the tree the builder made" if tree == EXPECTED else "it is NOT the tree the builder made (%s): the base differs, or something else is staged" % EXPECTED)
