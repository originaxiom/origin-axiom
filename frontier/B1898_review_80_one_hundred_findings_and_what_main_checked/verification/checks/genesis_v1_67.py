#!/usr/bin/env python3
"""The foundation at version 1.67 (prepared 2026-11-12; applied at Review 80's landing): the quotations of the owner in
its body are put in plain words (his ruling of 2026-11-11 on his messages, register rows P-796 and P-825; the web
seat's finding 7 of Review 80).  No item is added and no status cell changes.  The dated list of versions keeps what
it wrote.

    python3 genesis_v1_67.py PATH_TO_GENESIS [--write]     # without --write it only checks that every passage is there once
"""
import pathlib, sys
EDITS = [
    ('The owner\'s hypothesis of 2026-10-02, "choice might be golden", was tested in these two sealed forms',
     'The owner\'s hypothesis of 2026-10-02, that the choice might be golden, was tested in these two sealed forms'),
    ('Which set "the family as object" names (the owner\'s rule of 2026-10-04)',
     'Which set the family, taken as the object, names (the owner\'s rule of 2026-10-04)'),
    ('(main B1480; the owner, 2026-10-07: "it\'s not up to me, it should be up to math, to the principle of emergence")',
     '(main B1480; the owner, 2026-10-07: it is not his to decide; the mathematics decides it, by the principle of emergence)'),
    ('(the owner, 2026-10-14: "how can a field be forced into existence … same as from philosophy to the seed")',
     '(the owner\'s question of 2026-10-14: how a field can be forced into existence, by a passage like the one from philosophy to the seed)'),
    ('the owner\'s "choice might be golden" in their two sealed forms',
     'the owner\'s hypothesis that the choice might be golden, in its two sealed forms'),
    ('the owner\'s hypothesis "choice might be golden" is on the record in two sealed forms',
     'the owner\'s hypothesis that the choice might be golden is on the record in two sealed forms'),
    ('**The owner\'s rule (2026-10-04): "existence emerges from the family as object; we shouldn\'t tie ourselves to m004."**',
     '**The owner\'s rule (2026-10-04): existence emerges from the family taken as the object, and the programme is not to be tied to m004.**'),
]
LOG_ANCHOR = "- **v1.66 · 2026-11-12 · main B1891.**"
LOG_ENTRY = ("- **v1.67 · 2026-11-12 · main B[[N]].** Wording only, from Review 80 (the web seat's finding 7) and the owner's word of "
             "2026-11-12 (register row P-825): the owner's sentences that stood in quotation marks in the body are given in plain words, "
             "seven passages in FK9, FK13, FK15, § 7 and § 8. A governing page quotes nothing he said (his ruling of 2026-11-11, P-796); "
             "this list of versions is a dated record and keeps what it wrote. No item is added and no status cell changes.\n")
if __name__ == "__main__":
    p = pathlib.Path(sys.argv[1]); t = p.read_text(encoding="utf-8")
    for old, new in EDITS:
        n = t.count(old)
        print("%d  %s" % (n, old[:90]))
        assert n == 1, old
        t = t.replace(old, new)
    assert t.count(LOG_ANCHOR) == 1
    t = t.replace(LOG_ANCHOR, LOG_ENTRY + LOG_ANCHOR)
    if "--write" in sys.argv:
        p.write_text(t, encoding="utf-8"); print("written")
    else:
        print("every passage stands once; nothing written")
