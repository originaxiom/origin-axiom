#!/usr/bin/env python3
"""C14, patch 9 (main's M25, answer 4): the working indices mark the record's words as quotations, and what their generators write themselves uses no inner word, held by the gate

A diff of this change would carry, in its removed lines, words that are treated as the owner's.  So the change is given
as the blocks that come in: each block that goes is named by its file, the line it starts at and the sha256 of its text,
and no line of it is written here.

    python3 <this file> <a clean checkout>

It stops and writes nothing if a block that goes is not, byte for byte, the block this seat replaced.  It stages what
it changes and prints the tree, and says whether it is the tree this seat built.  It commits nothing: the message is the file beside this one.
"""
import hashlib, json, pathlib, subprocess, sys

root = pathlib.Path(sys.argv[1]).resolve()
EXPECTED = '4b3e43d406037d8e8613ca953e2a13dc7c582bba'
AFTER = "bash -c 'python3 -B scripts/views/generate.py >/dev/null && python3 -B scripts/views/spine.py >/dev/null'"
OPS = json.loads(r'''[
[
"scripts/gates/gates.py",
3195,
0,
"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
[
"",
"def working_index_own_words():",
"    \"\"\"C14, patch 9 (main's M25, answer 4): the inner words each working index's generator writes itself. Each view is",
"    built again with every quotation of the record emptied (the generators' `quoted`), and what is left is counted.\"\"\"",
"    import importlib.util as _u",
"    out = {}",
"    sys.dont_write_bytecode, was = True, sys.dont_write_bytecode",
"    try:",
"        spec = _u.spec_from_file_location(\"views_generate_for_the_public_face\", os.path.join(ROOT, \"scripts\", \"views\", \"generate.py\"))",
"        gen = _u.module_from_spec(spec); spec.loader.exec_module(gen)",
"        gen.quoted = lambda s: \"\\u201c\\u201d\"",
"        arcs, kills = gen.collect()",
"        out[\"docs/views/VERDICT_LEDGER.md\"] = gen.view_claims(arcs)",
"        out[\"docs/views/CLOSED_DOORS.md\"] = gen.view_closed_doors(arcs, kills)",
"        out[\"docs/views/REVIEWER.md\"] = gen.view_reviewer(arcs, kills)",
"        out[\"docs/views/CONTEXT_RECOVERY.md\"] = gen.view_context_recovery(arcs, kills)",
"        spec = _u.spec_from_file_location(\"views_spine_for_the_public_face\", os.path.join(ROOT, \"scripts\", \"views\", \"spine.py\"))",
"        sp = _u.module_from_spec(spec); spec.loader.exec_module(sp)",
"        sp.quoted = lambda s: \"\\u201c\\u201d\"",
"        out[\"docs/views/THE_SPINE.md\"] = sp.main(write=False)",
"    finally:",
"        sys.dont_write_bytecode = was",
"    return {p: dict(public_face_words(t)) for p, t in out.items()}",
"",
""
]
],
[
"scripts/gates/gates.py",
3221,
2,
"b6a7b9f4c388927dd71b719c085c4ffdb80583073f8ea0e2194e4649ab7592b4",
[
"def gate_public_face(reader=None, own_words=None):",
"    \"\"\"main's card C14: the public face uses none of the record's inner words.  Held by page and word as found; may only fall.",
"    2026-11-13 (C14, patch 9; main's M25, answer 4): a working index may quote the record's own words, marked as",
"    quotations, but what its generator writes itself uses none of them (working_index_own_words).\"\"\""
]
],
[
"scripts/gates/gates.py",
3225,
0,
"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
[
"    own = working_index_own_words() if own_words is None else own_words",
"    bad += [\"%s: its generator writes %r %d times itself\" % (rel, w, n) for rel, c in sorted(own.items()) for w, n in sorted(c.items())]"
]
],
[
"scripts/gates/gates.py",
3230,
2,
"a1782220126c7fdd6d1c849a3cf7c066c5dfb77ffd6f61f1a2a6673f84a586fd",
[
"    return True, \"ok (%d page(s) of the public face read: %d at zero; %d inner word(s) held by page and word as found on 2026-11-13%s; the %d working indices' generators write none themselves)\" % (",
"        len(counts), zero, total, (\"; lower the count of \" + \", \".join(fell)) if fell else \"\", len(own))"
]
],
[
"scripts/views/generate.py",
33,
0,
"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
[
"",
"",
"",
"def quoted(s):",
"    \"\"\"The record's own words as a view quotes them: marked as a quotation, word for word. Added 2026-11-13 (C14, patch",
"    9, main's M25, answer 4): a working index quotes verdict lines, claims and headings; what it writes itself is plain,",
"    and the gate public-face builds each working index with this emptied and counts the words that are left.\"\"\"",
"    return \"\\u201c%s\\u201d\" % s"
]
],
[
"scripts/views/generate.py",
140,
1,
"f6c5cf8b8b1fda9a2eacfcb215600170057cb193ea03bdd91e685b5e3be28fd7",
[
"            L.append(f\"| `{a['id']}` | {quoted(v['claim_one_line'])} | \""
]
],
[
"scripts/views/generate.py",
187,
1,
"51955fb8e58b9a11a2255121b8368762654b06b2942981eb8fff8126ce0793d1",
[
"        L.append(f\"| `{quoted(form)}` | {len(rs)} | {unc or ''} |\")   # a mechanism as the kill graph names it, quoted"
]
],
[
"scripts/views/generate.py",
195,
1,
"18d3b8aca565f01830327b110dc03f24b92dac16d719d68569880b7bef7788a9",
[
"        L.append(f\"| `{r['id']}` | {quoted(r['claim_killed'][:110])} | `{quoted(r['kill_form'])}` |\")"
]
],
[
"scripts/views/generate.py",
243,
1,
"a80f7331a68833d2c3822860b572db63217829487511d415975e74a2b11e896f",
[
"        L.append(f\"| `{quoted(f)}` | {n} |\")"
]
],
[
"scripts/views/generate.py",
257,
1,
"d1d1fd5b5c0aaba56ca798e8afbc1545604c2ca415a4a37570afdbe0d863efd8",
[
"                  f\"{quoted(a['verdict_record']['claim_one_line'])}  \","
]
],
[
"scripts/views/generate.py",
295,
1,
"3cf62a6ada5e6ecc87e2aef07776385701f0c95c80723bb19eb1ec491df515e0",
[
"           \"(runs in flight and unlanded work; gitignored), then the newest CHANGELOG entry. Results of other working lines not yet read in:\","
]
],
[
"scripts/views/generate.py",
312,
2,
"be440025545f378b50bf4c5ee178b219501b9f47a634bca7e9d73caf9925a6b2",
[
"    for k in (\"QUEUED\", \"LEAD\", \"OWNER\", \"DONE\", \"DECLINED\"):     # the register's own labels, quoted (C14, patch 9)",
"        out.append(\"| … %s | %d |\" % (quoted(k), sum(v for d, v in disp.items() if d.startswith(k))))"
]
],
[
"scripts/views/generate.py",
321,
1,
"c1d27597d866e8d334d50983c3334bdda85f7b91ccec411fde778d61f2749be2",
[
"        out.append(\"| %s | %s | %s |\" % (a[\"id\"], vr(a).get(\"verdict\") or \"—\", quoted(clip((vr(a).get(\"claim_one_line\") or a[\"title\"] or \"\").replace(\"|\", \"∣\"), 220))))"
]
],
[
"scripts/views/generate.py",
326,
2,
"85d9683e1b4a29a9789eccb4f75cc1d46cb588eafa7cf092dbc7d79973c7ae40",
[
"    out.append(\"## Awaiting a decision (register rows whose disposition is %s)\\n\" % quoted(\"OWNER\"))",
"    out.extend(\"- **%s** — %s → *%s*\" % (c[0], quoted(clip(c[3], 220)), quoted(clip(c[5], 160))) for c in owner) if owner else out.append(\"- none\")"
]
],
[
"scripts/views/generate.py",
331,
1,
"49a0777c14c1b8813879b55a9a1e7fde0ea71071f846d890bdc0e1e2325d5f6f",
[
"    out.extend(\"- **%s** (%s) — %s\" % (c[0], c[1], quoted(clip(c[3], 200))) for c in sorted(q1, key=lambda c: c[0], reverse=True)[:25])"
]
],
[
"scripts/views/generate.py",
337,
1,
"2efda932711af230313980f9004d34615044f2f2f297a89e9d1a1da9e7bcc1bc",
[
"    out.extend(\"- \" + quoted(clip(h, 200)) for h in ch)"
]
],
[
"scripts/views/generate.py",
340,
1,
"6a40dd1bc99c771470f6a916439aa0351dea1afe7b4c244d0c577c5bd6e97138",
[
"    out.append(quoted(clip(latest.strip(\"*\"), 700)) + \"\\n\")"
]
],
[
"scripts/views/spine.py",
13,
1,
"2c4c5b0ebed3de9b574a3757903571ebf0dcaec6764f9f8d245ce0740a619321",
[
"",
"def quoted(s):",
"    \"\"\"an arc's own claim head, marked as a quotation (2026-11-13, C14, patch 9); the gate public-face empties it\"\"\"",
"    return \"\\u201c%s\\u201d\" % s",
"",
"def main(write=True):"
]
],
[
"scripts/views/spine.py",
56,
1,
"e69a1213d7ac6bc209be2a9d55e010e87de76e1aa24bc0726dfe62ea3d4cd2e8",
[
"        lines.append(f\"- {tag}{vt} `{tf}` {('— ' + quoted(head)) if head else ''}\")",
"    if not write:",
"        return \"\\n\".join(lines) + \"\\n\""
]
],
[
"tests/test_public_face.py",
129,
0,
"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
[
"",
"def test_a_working_index_quotes_the_record_and_its_generator_writes_no_inner_word():",
"    \"\"\"C14, patch 9 (main's M25, answer 4): each working index is built again with its quotations emptied; what is left,",
"    the generator's own words, counts no inner word, and each index marks the record's words it quotes as quotations.",
"    Planted: a generator's own heading in the inner words, and a quotation left unmarked.\"\"\"",
"    g = _gates()",
"    own = g.working_index_own_words()",
"    assert set(own) == set(g.WORKING_INDICES) and all(c == {} for c in own.values()), own",
"    assert g.gate_public_face()[0]",
"    planted = dict(own, **{\"docs/views/CONTEXT_RECOVERY.md\": dict(g.public_face_words(\"## Waiting for the owner\"))})",
"    ok, detail = g.gate_public_face(own_words=planted)",
"    assert not ok and \"its generator writes 'owner' 1 times itself\" in detail",
"    # the quotations are marked on the committed pages: the newest arcs' claims, the ledger's claims, the spine's heads",
"    text = (ROOT / \"docs\" / \"views\" / \"CONTEXT_RECOVERY.md\").read_text(encoding=\"utf-8\")",
"    rows = [l for l in text.split(\"\\n\") if l.startswith(\"| B\") and l.count(\" | \") == 2]",
"    assert rows and all(l.split(\" | \")[2].startswith(\"“\") and l.rstrip(\" |\").endswith(\"”\") for l in rows)",
"    spine = (ROOT / \"docs\" / \"views\" / \"THE_SPINE.md\").read_text(encoding=\"utf-8\")",
"    heads = [l for l in spine.split(\"\\n\") if l.startswith(\"- \") and \"` \\u2014 \" in l]     # a lock's line with its arc's claim head",
"    assert heads and all(l.split(\"` \\u2014 \", 1)[1].startswith(\"\\u201c\") for l in heads)",
"    # the twin of the plant: a quotation with its marks taken off is counted as the generator's own",
"    unmarked = text.replace(\"“\", \"\").replace(\"”\", \"\")",
"    assert sum(g.public_face_words(unmarked).values()) > 0",
""
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
