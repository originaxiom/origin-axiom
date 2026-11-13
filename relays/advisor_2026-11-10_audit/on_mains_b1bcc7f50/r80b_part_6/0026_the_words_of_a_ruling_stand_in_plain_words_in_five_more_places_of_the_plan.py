#!/usr/bin/env python3
"""R80b, part 6, patch 26 (main's M21): the words of the ruling of 2026-10-08 stand in plain words in five more places of the plan's source, and the lock holds no form of them in marks

A diff of this change would carry, in its removed lines, words that are treated as the owner's.  So the change is given
as the blocks that come in: each block that goes is named by its file, the line it starts at and the sha256 of its text,
and no line of it is written here.

    python3 <this file> <a clean checkout>

It stops and writes nothing if a block that goes is not, byte for byte, the block this seat replaced.  It stages what
it changes and prints the tree, and says whether it is the tree this seat built.  It commits nothing: the message is the file beside this one.
"""
import hashlib, json, pathlib, subprocess, sys

root = pathlib.Path(sys.argv[1]).resolve()
EXPECTED = '3c70e7078e6859262a23828d472937fcba2e6070'
AFTER = 'python3 -B frontier/B1861_the_closure_programme/verification/build_programme.py --write'
OPS = json.loads(r'''[
[
"frontier/B1861_the_closure_programme/PROGRAMME.json",
604,
2,
"bc6f1f292fcc75af4970961284d73c402d16c505f23459450173a6cf71c951dc",
[
"   \"how 'the tick is an act' stands with the ruling of 2026-10-08\",",
"   \"On 2026-10-08 you ruled that only even ticks are observed ... Today you ruled that the tick is an act and both kinds of history are in the ledger. I did not remind you of the first ruling when I asked. How do the two stand together?\","
]
],
[
"frontier/B1861_the_closure_programme/PROGRAMME.json",
614,
2,
"8fc296f0d9da8a57d0eb3d042dc6cf69cac0bc9eb9ae5923d720632c7b2077ff",
[
"   \"the ruling of 2026-10-08, after the computation\",",
"   \"With the computation in hand: your ruling of 2026-10-08 says that only even ticks are observed ... Today you ruled the tick an act. The computation shows the only thing at stake between them is the hand ... How should they stand together?\","
]
],
[
"frontier/B1861_the_closure_programme/PROGRAMME.json",
622,
1,
"a4d47bd640a754338ee406ebac92538349ab14d2eb8071accb20314cc2c86ec7",
[
"   \"every tick is in the ledger; that only even ticks are observed is no longer a ruling but a condition the weight must deliver; the chiral three stays exactly as conditional as it was; the budget's orientation bit is a named condition to derive, not a declared choice, and is not counted as derived (B1879)\""
]
],
[
"frontier/B1861_the_closure_programme/PROGRAMME.md",
1016,
2,
"8fabf1d141cd8c833825f1d0b22106898948653b17baaf271d29d5df7376e057",
[
"| how 'the tick is an act' stands with the ruling of 2026-10-08 | \"On 2026-10-08 you ruled that only even ticks are observed ... Today you ruled that the tick is an act and both kinds of history are in the ledger. I did not remind you of the first ruling when I asked. How do the two stand together?\" | After the computation | 2026-11-11 | WP-1.4 | both rulings stand side by side and the foundation records both; their relation is decided after main has computed the weave's theorems for the group with the exchange (P-769). Until then nothing says that the orientation has stopped being a choice, or that the mark is both twins |",
"| the ruling of 2026-10-08, after the computation | \"With the computation in hand: your ruling of 2026-10-08 says that only even ticks are observed ... Today you ruled the tick an act. The computation shows the only thing at stake between them is the hand ... How should they stand together?\" | A condition to derive (Recommended) | 2026-11-11 | WP-1.4, WP-1.6 | every tick is in the ledger; that only even ticks are observed is no longer a ruling but a condition the weight must deliver; the chiral three stays exactly as conditional as it was; the budget's orientation bit is a named condition to derive, not a declared choice, and is not counted as derived (B1879) |"
]
],
[
"frontier/B1861_the_closure_programme/verification/programme_source.py",
841,
0,
"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
[
"# 2026-11-13 (R80b, part 6, patch 26; main's M21): the words of the ruling of 2026-10-08 stood in marks in five places of",
"# this table, in the names of two rulings, in main's two questions as they were asked, and in one account of what a",
"# ruling means.  Main cannot show that they were its own label and not the owner's, so they are treated as his (register",
"# row P-796), and all five are in plain words now.  What stood is not kept here."
]
],
[
"frontier/B1861_the_closure_programme/verification/programme_source.py",
847,
2,
"75ee9ccb986946bbb786e56c1314da0607eb60187e2d016c94e3fe278ade7023",
[
"    (\"how 'the tick is an act' stands with the ruling of 2026-10-08\",",
"     \"On 2026-10-08 you ruled that only even ticks are observed ... Today you ruled that the tick is an act and both kinds of history are in the ledger. I did not remind you of the first ruling when I asked. How do the two stand together?\","
]
],
[
"frontier/B1861_the_closure_programme/verification/programme_source.py",
852,
2,
"45ba4bdc629c857375209987eeb9c001b9889683beadafa00500790e026eb6bb",
[
"    (\"the ruling of 2026-10-08, after the computation\",",
"     \"With the computation in hand: your ruling of 2026-10-08 says that only even ticks are observed ... Today you ruled the tick an act. The computation shows the only thing at stake between them is the hand ... How should they stand together?\","
]
],
[
"frontier/B1861_the_closure_programme/verification/programme_source.py",
855,
1,
"32954c0063985e15adf10ac50e5f4ca8a0f9e2d1218a573ebbca11e78d60c935",
[
"     \"every tick is in the ledger; that only even ticks are observed is no longer a ruling but a condition the weight must deliver; the chiral three stays exactly as conditional as it was; the budget's orientation bit is a named condition to derive, not a declared choice, and is not counted as derived (B1879)\"),"
]
],
[
"frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py",
1027,
0,
"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
[
"",
"# 2026-11-13 (R80b, part 6, patch 26; main's M21).  The words of the ruling of 2026-10-08 are held nowhere in marks: not in the",
"# source, not on the page, not in the data.  The plain words (\"the ruling of 2026-10-08 that only even ticks are observed\",",
"# or shorter) stand where they are needed.  A form in marks is found by a mark of quotation that stands right before the",
"# words (and not after a letter, as an apostrophe of possession does) and one that closes within thirty characters after",
"# them, so that no spelling of the ruling's words is needed here.",
"_IN_MARKS = re.compile(r\"(?<![A-Za-z])[\\'\\\"\\u2018\\u201c\\u00ab]\\s*(?:only\\s+)?even\\s+ticks\\b[^\\'\\\"\\u2019\\u201d\\u00bb\\n]{0,30}[\\'\\\"\\u2019\\u201d\\u00bb](?![A-Za-z])\")",
"",
"",
"def _the_rulings_words_in_marks(text):",
"    return [m.group(0) for m in _IN_MARKS.finditer(text)]",
"",
"",
"def test_the_words_of_the_ruling_of_2026_10_08_stand_in_marks_nowhere_in_the_source_the_page_or_the_data():",
"    arc = pathlib.Path(__file__).resolve().parents[1]",
"    for rel in (\"verification/programme_source.py\", \"PROGRAMME.md\", \"PROGRAMME.json\"):",
"        text = (arc / rel).read_text(encoding=\"utf-8\")",
"        assert _the_rulings_words_in_marks(text) == [], rel",
"        assert \"only even ticks are observed\" in text, rel                       # the plain words stand",
"    # planted: the plain words put in marks, in each of the shapes a mark takes; and their twin, the same words without marks",
"    plain = \"the ruling of 2026-10-08 that only even ticks are observed\"",
"    for a, b in ((\"'\", \"'\"), ('\"', '\"'), (\"\\u2018\", \"\\u2019\"), (\"\\u201c\", \"\\u201d\"), (\"\\u00ab\", \"\\u00bb\")):",
"        assert _the_rulings_words_in_marks(\"you ruled %sonly even ticks are observed%s on that day\" % (a, b)), a",
"        assert _the_rulings_words_in_marks(\"%seven  ticks%s\" % (a, b)), a",
"    assert _the_rulings_words_in_marks(plain) == [] and _the_rulings_words_in_marks(\"how 'the tick is an act' stands with \" + plain) == []",
"    # the source with one of the five places as it stood is refused: the name of the fourth ruling put back in marks",
"    src = (arc / \"verification\" / \"programme_source.py\").read_text(encoding=\"utf-8\")",
"    old = '(\"the ruling of 2026-10-08, after the computation\"'",
"    assert src.count(old) == 1",
"    assert _the_rulings_words_in_marks(src.replace(old, '(\"\\'only even ticks\\', after the computation\"')) != []",
"",
""
]
],
[
"frontier/B1877_review_78_the_decadal_review/verification/test_b1877_review_78.py",
91,
0,
"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
[
"    # [CHANGED 2026-11-13 (R80b, part 6, patch 26; main's M21).  The third and fourth names held here stood in the words of",
"    #  the ruling of 2026-10-08, in marks; main has them in plain words in the programme, as words treated as the owner's",
"    #  (P-796), and this lock holds the names as they now stand.  What stood is not kept.]"
]
],
[
"frontier/B1877_review_78_the_decadal_review/verification/test_b1877_review_78.py",
92,
1,
"1370d1e921d7d796082b1b7fbd4a1714d7c076b490df4c2cdace314b6edf212f",
[
"                                                           \"how 'the tick is an act' stands with the ruling of 2026-10-08\"]"
]
],
[
"frontier/B1877_review_78_the_decadal_review/verification/test_b1877_review_78.py",
94,
1,
"498aaeef882b3258428e5ddeec9999233446ab1f3fc09f13d0e083bd3c3a7bb9",
[
"    assert [r[0] for r in prog[\"direct_rulings\"]][3:] == [\"the ruling of 2026-10-08, after the computation\"]"
]
]
]''')

texts = {}
for path, start, count, digest, new in OPS:
    lines = texts.setdefault(path, (root / path).read_text(encoding="utf-8").split("\n"))
by_file = {}
for op in OPS:
    by_file.setdefault(op[0], []).append(op)
for path, ops in by_file.items():
    lines = texts[path]
    for _p, start, count, digest, new in ops:
        if hashlib.sha256("\n".join(lines[start:start + count]).encode("utf-8")).hexdigest() != digest:
            sys.exit("STOPPED, nothing written: in %s the %d line(s) from line %d are not the ones this change replaces" % (path, count, start + 1))
    for _p, start, count, digest, new in sorted(ops, key=lambda o: -o[1]):
        lines[start:start + count] = new
for path, lines in texts.items():
    (root / path).write_text("\n".join(lines), encoding="utf-8")
if AFTER:
    r = subprocess.run(AFTER, cwd=str(root), shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("the files are edited and THE STEP AFTER THEM FAILED (%s):\n" % AFTER + (r.stdout + r.stderr)[-1500:])
subprocess.run(["git", "add", "-A"], cwd=str(root), check=True)
tree = subprocess.run(["git", "write-tree"], cwd=str(root), capture_output=True, text=True).stdout.strip()
changed = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=str(root), capture_output=True, text=True).stdout.split()
print("staged: %d files" % len(changed)); print("\n".join("  " + c for c in changed))
print("the tree: %s" % tree)
if EXPECTED:
    print("it is the tree the builder made" if tree == EXPECTED else "it is NOT the tree the builder made (%s): the base differs, or something else is staged" % EXPECTED)
