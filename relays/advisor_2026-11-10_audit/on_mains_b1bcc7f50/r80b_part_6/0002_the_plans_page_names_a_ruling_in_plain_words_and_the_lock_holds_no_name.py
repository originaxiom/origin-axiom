#!/usr/bin/env python3
"""R80b, part 6, patch 2, as a script and not as a diff: the plan's page names a ruling in plain words, and the lock holds no name.

A diff of this change would carry, in its removed lines, words that are treated as the owner's.  So the change is given
as the blocks that come in: each block that goes is named by its file, the line it starts at and the sha256 of its text,
and no line of it is written here.

    python3 <this file> <a clean checkout>

It stops and writes nothing if a block that goes is not, byte for byte, the block this seat replaced.  It stages what
it changes and prints the tree, and says whether it is the tree this seat built.  It commits nothing: the message is the file beside this one.
"""
import hashlib, json, pathlib, subprocess, sys

root = pathlib.Path(sys.argv[1]).resolve()
EXPECTED = 'aae874bde43e526ede495d87fac77e78d0d5ba86'
AFTER = 'python3 -B frontier/B1861_the_closure_programme/verification/build_programme.py --write'
OPS = json.loads(r'''[
[
"frontier/B1861_the_closure_programme/PROGRAMME.json",
747,
1,
"1178e5c9f66c36d8f948bf52a3edac6c286d639652011799dc3df7372428954e",
[
"   \"the owner's ruling of 2026-11-11, to main, with B1879's computation in hand: every tick is in the ledger; that only even ticks are observed is no longer a ruling but a condition the weight must deliver. So this input has a named condition downstream that it must satisfy, and none is built: it is not derived and is not counted as derived. [Was PRESSED: the ledger: the principle does not force it and may speak against it. The non-orientable sibling is the alternative. Verified on main (B1871): if the tick, the owner's founding rule, is an act, both sheets exist and this is no choice; it supplies no hand. Asked of the owner (P-771). RULED BY THE OWNER on 2026-11-11, to main: the tick is an act. The owner's ruling of 2026-10-08 that only even ticks are observed also stands; how the two stand together waits on a computation, at the owner's word (P-769). So this entry keeps its kind: nothing yet says that the orientation has stopped being a choice.]\""
]
],
[
"frontier/B1861_the_closure_programme/PROGRAMME.json",
2498,
1,
"4c259a87b8f5138870f2c748114e0d8495d93d8af32b3f9d31725f3bb783a509",
[
"  \"the tick is an act\": \"admit it: it is the founding rule's single step, nothing forbids it, and it makes the root's mirror symmetry a consequence. It supplies no hand. Build nothing on the added histories before the three debts are computed (P-769). MAIN'S OPINION AS FIRST GIVEN ALSO SAID that it removes the orientation as a choice; that was said without the owner's standing ruling of 2026-10-08 that only even ticks are observed beside it, and is withdrawn until the two are related\","
]
],
[
"frontier/B1861_the_closure_programme/PROGRAMME.md",
127,
1,
"e94cbaac0e3f0113ca1cb846dcb0cecdaf1bc510326425a4980e28a73a38d6f8",
[
"| the orientation | bit | BACK-EDGE NAMED | the owner's ruling of 2026-11-11, to main, with B1879's computation in hand: every tick is in the ledger; that only even ticks are observed is no longer a ruling but a condition the weight must deliver. So this input has a named condition downstream that it must satisfy, and none is built: it is not derived and is not counted as derived. [Was PRESSED: the ledger: the principle does not force it and may speak against it. The non-orientable sibling is the alternative. Verified on main (B1871): if the tick, the owner's founding rule, is an act, both sheets exist and this is no choice; it supplies no hand. Asked of the owner (P-771). RULED BY THE OWNER on 2026-11-11, to main: the tick is an act. The owner's ruling of 2026-10-08 that only even ticks are observed also stands; how the two stand together waits on a computation, at the owner's word (P-769). So this entry keeps its kind: nothing yet says that the orientation has stopped being a choice.] |"
]
],
[
"frontier/B1861_the_closure_programme/PROGRAMME.md",
1006,
1,
"63ebaf2a62892451a9e6cec3b2f219b3072553ac0f8e9a8d7e5fb13a6beafb71",
[
"| the tick is an act | \"The tick is an act, and both kinds of history are in the ledger\" | CONFIRMED 2026-11-11: asked \"Is the tick an act?\", the owner chose main's option: Yes, admit it (Recommended) | WP-1.4 | admit it: it is the founding rule's single step, nothing forbids it, and it makes the root's mirror symmetry a consequence. It supplies no hand. Build nothing on the added histories before the three debts are computed (P-769). MAIN'S OPINION AS FIRST GIVEN ALSO SAID that it removes the orientation as a choice; that was said without the owner's standing ruling of 2026-10-08 that only even ticks are observed beside it, and is withdrawn until the two are related |"
]
],
[
"frontier/B1861_the_closure_programme/verification/programme_source.py",
829,
0,
"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
[
"# REWORDED 2026-11-12 (Review 80; main's word in its third folder for the builder, section 8, row 2).  Main's opinion on \"the tick",
"# is an act\", below, named the ruling of 2026-10-08 by three words in single marks.  Main cannot show that the three words are",
"# its own label and not the owner's, so they are treated as his, and are not kept in this note.  The opinion now says, in",
"# plain words: the ruling of 2026-10-08 that only even ticks are observed.  The exit \"the orientation\", further down, named",
"# the ruling the same way and is reworded the same way.  The table of rulings given to main directly keeps the names of two",
"# rulings and main's questions as they were asked: whether those are reworded as well is main's to say."
]
],
[
"frontier/B1861_the_closure_programme/verification/programme_source.py",
830,
1,
"ad30a9d9f722915b2a7f9712253fb66be2cf02a6b1c7e78cd149ecb2f9d51202",
[
"    \"the tick is an act\": \"admit it: it is the founding rule's single step, nothing forbids it, and it makes the root's mirror symmetry a consequence. It supplies no hand. Build nothing on the added histories before the three debts are computed (P-769). MAIN'S OPINION AS FIRST GIVEN ALSO SAID that it removes the orientation as a choice; that was said without the owner's standing ruling of 2026-10-08 that only even ticks are observed beside it, and is withdrawn until the two are related\","
]
],
[
"frontier/B1861_the_closure_programme/verification/programme_source.py",
995,
1,
"4a157904504ef0a7ca2fcc875f5263857cd7efffbd8292a1b6b76add349e441b",
[
"    \"the orientation\": (\"BACK-EDGE NAMED\", \"the owner's ruling of 2026-11-11, to main, with B1879's computation in hand: every tick is in the ledger; that only even ticks are observed is no longer a ruling but a condition the weight must deliver. So this input has a named condition downstream that it must satisfy, and none is built: it is not derived and is not counted as derived. [Was PRESSED: the ledger: the principle does not force it and may speak against it. The non-orientable sibling is the alternative. Verified on main (B1871): if the tick, the owner's founding rule, is an act, both sheets exist and this is no choice; it supplies no hand. Asked of the owner (P-771). RULED BY THE OWNER on 2026-11-11, to main: the tick is an act. The owner's ruling of 2026-10-08 that only even ticks are observed also stands; how the two stand together waits on a computation, at the owner's word (P-769). So this entry keeps its kind: nothing yet says that the orientation has stopped being a choice.]\"),"
]
],
[
"frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py",
227,
1,
"42c5707a466e6878986f13f51dc8a70f8da6be9e2704e2f0bfe7b2d0c5820cd5",
[
"    # the ground is the act; 'close' means the whole agrees (P-774); and how the tick's ruling stands with the ruling of 2026-10-08 that only even ticks are observed: after the computation"
]
],
[
"frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py",
766,
0,
"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
[
"_CLOSES = \"\\\"”’»'\""
]
],
[
"frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py",
774,
1,
"46407cb962f9421f97a3bd1a5211a07a09d64a31382028acb22c21f722aa087e",
[
"# EMPTIED 2026-11-12 (main's word, its third folder for the builder, section 8, row 2): the name is treated as the owner's, both",
"# places are reworded in plain words, and the table holds no name.  It held one, twice.  The reader of the first part also",
"# found that the exemption asked only that the text after the opening mark BEGINS with the name, so any words could follow it",
"# inside the same marks; with the table empty nothing is exempt.  The name itself is not kept here.",
"HELD_BY_NAME = {}"
]
],
[
"frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py",
801,
1,
"0999e645a3c537c52e4fd633ee085200abc241db506090b888696ab62a23baac",
[
"                # until 2026-11-12: `cell[m.end():].startswith(k)`, so words that followed a held name inside the same marks were",
"                # excused with it (found by the reader of the first part).  A held name is the whole of what stands in the marks.",
"                rest = cell[m.end():]",
"                name = next((k for k in left if rest.startswith(k) and rest[len(k):len(k) + 1] in tuple(_CLOSES)), None)"
]
],
[
"frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py",
821,
3,
"818ba604931bab138c1010f68208e0c08e2a88f443d003dda8b369a6e2d7c082",
[
"    # CHANGED 2026-11-12 (main's word, its third folder for the builder, section 8, row 2).  Three lines stood here: with the",
"    # table of names held empty the page's two places were reported, and a third place with the same name in marks was",
"    # reported.  The two places are reworded and the table is empty, so the page reports nothing with nothing held; and a",
"    # ruling named in marks after a word for the owner is reported, whatever follows its first words inside the marks.",
"    assert HELD_BY_NAME == {} and what_the_plans_page_quotes(page, held={}) == []",
"    assert page.count(\"ruling of 2026-10-08 that only even ticks are observed\") == 2",
"    for planted_name in (\"The owner's ruling ('a name of three words') once more.\", \"The owner's ruling ('a name of three words, and words after it') once more.\"):",
"        assert len(what_the_plans_page_quotes(page + \"\\n\" + planted_name + \"\\n\")) == 1, planted_name",
"    # the exemption as it stood excused words that follow a held name inside the same marks.  Shown on a table of one name: the",
"    # name alone in its marks is held, and the name with words after it is reported",
"    assert what_the_plans_page_quotes(\"The owner's ruling ('a name').\", held={\"a name\": 1}) == []",
"    assert len(what_the_plans_page_quotes(\"The owner's ruling ('a name and anything he said after it').\", held={\"a name\": 1})) == 1"
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
