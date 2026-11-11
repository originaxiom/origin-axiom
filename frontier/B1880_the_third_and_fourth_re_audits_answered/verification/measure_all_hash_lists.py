"""B1880 -- every list of hashed files on main, whatever it is called, measured before it is gated.

The advisor seat's third re-audit (2026-11-11) planted three cases against the gate for the scripts a seal hashed (B1874) and
all three passed it: a copy standing in for the real file (t3), a frozen entry changed again (t4), and a list under another
name (t7).  This script reproduces the seat's counts on main, measures the lists the gate did not read, and writes the table
that the mended gate holds every frozen entry to.

    python3 -B measure_all_hash_lists.py            # measure, print, write nothing outside this folder
    python3 -B measure_all_hash_lists.py --write    # also write scripts/gates/hash_lists_frozen.json

Nothing here reads a measured value of physics; it reads file names, hashes and the commit graph.
"""
import collections
import fnmatch
import hashlib
import importlib.util
import json
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gates_b1880_measure", ROOT / "scripts" / "gates" / "gates.py")
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)

CANDIDATE_LIST = "frontier/B1841_the_principled_ends_card/ARTIFACT_HASHES.txt"
PAGES = (".md", ".tex")                       # a page goes on being written; a script or an output is an instrument


def git(*a, raw=False):
    return subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=not raw)


def sealed_version(path, h):
    """the newest commit at which the tracked file had the recorded content, or None (B1874's function, unchanged)"""
    for line in git("log", "--follow", "--format=%H %cs", "--", path).stdout.strip().split("\n"):
        if not line:
            continue
        c, d = line.split()
        r = git("show", f"{c}:{path}", raw=True)
        if r.returncode == 0 and hashlib.sha256(r.stdout).hexdigest() == h:
            return c[:9], d
    return None


def named(lst):
    return fnmatch.fnmatch(os.path.basename(lst), G.ARTIFACT_HASH_GLOB)


def where_found(tracked):
    """for the named lists, as the gate of B1874 read them: which of the three places each entry's name was found in first"""
    first = collections.Counter(); by_file = collections.defaultdict(set); cand = []
    for lst in sorted(f for f in tracked if named(f)):
        d = os.path.dirname(lst)
        for line in (ROOT / lst).read_text(encoding="utf-8", errors="replace").split("\n"):
            e = G._hash_list_entry(line.strip())
            if e is None or e[1] is None:
                continue
            every = [os.path.normpath(os.path.join(d, e[1])), os.path.normpath(os.path.join(d, "verification", e[1])), os.path.normpath(e[1])]
            i = next((i for i, c in enumerate(every) if c in tracked), None)
            if i is None:
                continue
            first[("beside the list", "in its verification folder", "from the root")[i]] += 1
            by_file[every[i]].add(i)
            if lst == CANDIDATE_LIST:
                cand.append((every[i], i))
    only_root = sorted(f for f, s in by_file.items() if s == {2})
    return first, only_root, cand


def main():
    write = "--write" in sys.argv
    tracked = set(git("ls-files").stdout.split("\n")); tracked.discard("")
    out = []
    P = lambda *a: (out.append(" ".join(str(x) for x in a)), print(*a))

    # ---- 1. the seat's counts, reproduced
    first, only_root, cand = where_found(tracked)
    old = G.artifact_hash_state()
    old_broken = [e for e in old if e[3] != "VERIFIES"]
    frozen_scripts = sorted({(e[1], e[2]) for e in old_broken if e[3] == "MISMATCH" and str(e[2]).endswith(".py")})
    P("1. THE NAMED LISTS, AS B1874'S GATE READ THEM")
    P("   entries: %d in %d lists; verify %d; do not %d (%d distinct keys)" % (
        len(old), len({e[1] for e in old}), len(old) - len(old_broken), len(old_broken), len({e[0] for e in old_broken})))
    P("   a name first found: %s" % ", ".join("%s %d" % kv for kv in sorted(first.items())))
    P("   files that every list naming them finds only from the root: %d" % len(only_root))
    P("   the candidate's list (%s): %d entries resolved, %d of them from the root" % (CANDIDATE_LIST.split("/")[1], len(cand), sum(1 for _, i in cand if i == 2)))
    alone = sorted(f for f, i in cand if f in set(only_root))
    P("   of those, files that NO other list reads where they stand (found only from the root by every list naming them): %d" % len(alone))
    for f in alone:
        P("      %s" % f)
    P("   frozen entries that are scripts whose hash does not verify: %d entries, %d distinct files" % (
        sum(1 for e in old_broken if e[3] == "MISMATCH" and str(e[2]).endswith(".py")), len(frozen_scripts)))

    # ---- 2. every list, by content
    st = G.hash_list_state()
    lists = sorted({e[1] for e in st})
    others = [l for l in lists if not named(l)]
    P("")
    P("2. EVERY LIST OF HASHED FILES, BY CONTENT")
    P("   lists: %d (%d named %s, %d under another name)" % (len(lists), len(lists) - len(others), G.ARTIFACT_HASH_GLOB, len(others)))
    P("   entries: %d; %s" % (len(st), ", ".join("%s %d" % kv for kv in sorted(collections.Counter(e[3] for e in st).items()))))
    o = [e for e in st if not named(e[1])]
    P("   under another name: %d entries; %s" % (len(o), ", ".join("%s %d" % kv for kv in sorted(collections.Counter(e[3] for e in o).items()))))
    fam = collections.defaultdict(lambda: collections.Counter())
    nlists = collections.Counter(os.path.basename(l) for l in others)
    for e in o:
        fam[os.path.basename(e[1])][e[3]] += 1
    P("   %-28s %5s %7s %7s %8s %9s" % ("family (file name)", "lists", "entries", "verify", "mismatch", "no file"))
    for b in sorted(fam, key=lambda b: -sum(fam[b].values())):
        c = fam[b]
        P("   %-28s %5d %7d %7d %8d %9d" % (b, nlists[b], sum(c.values()), c["VERIFIES"], c["MISMATCH"], c["ABSENT"] + c["NOT TRACKED"]))
    shares = []
    for l in others:
        text = (ROOT / l).read_text(encoding="utf-8", errors="replace")
        lines = [x.strip() for x in text.split("\n") if x.strip() and not x.strip().startswith("#")]
        n = sum(1 for x in lines if (G._hash_list_entry(x) or (None, None))[1] is not None)
        shares.append(n / len(lines))
    not_lists = []
    for f in sorted(tracked):
        b = os.path.basename(f)
        if named(f) or os.path.splitext(b)[1].lower() not in G.HASH_LIST_SUFFIXES or f in set(others):
            continue
        try:
            if os.path.getsize(ROOT / f) > G.HASH_LIST_MAX_BYTES:
                continue
            text = (ROOT / f).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if not G._HEX64.search(text):
            continue
        lines = [x.strip() for x in text.split("\n") if x.strip() and not x.strip().startswith("#")]
        n = sum(1 for x in lines if (G._hash_list_entry(x) or (None, None))[1] is not None)
        if n:
            not_lists.append(n / len(lines))
    P("   the share of a file's lines that are a hash and a name: lowest among the lists %.3f; highest among the %d files that print a hash and are not lists %.3f; the rule's line is %.2f" % (
        min(shares), len(not_lists), max(not_lists) if not_lists else 0.0, G.HASH_LIST_MIN_SHARE))

    # ---- 3. what the entries under other names that do not verify are
    P("")
    P("3. THE ENTRIES UNDER OTHER NAMES THAT DO NOT VERIFY, BY WHAT THE HISTORY SAYS")
    rows = []
    for (k, lst, name, state, sig) in o:
        if state == "VERIFIES":
            continue
        if state != "MISMATCH":
            rows.append((k, lst, name, "E" if state == "ABSENT" else "D", None)); continue
        h = next(G._hash_list_entry(x.strip())[0] for x in (ROOT / lst).read_text(encoding="utf-8", errors="replace").split("\n")
                 if G._hash_list_entry(x.strip()) and hashlib.sha256(f"{lst}|{G._hash_list_entry(x.strip())[1]}|{G._hash_list_entry(x.strip())[0]}".encode()).hexdigest()[:12] == k)
        sv = sealed_version(name, h)
        cls = "C" if sv is None else ("B" if name.endswith(PAGES) else "A")
        rows.append((k, lst, name, cls, sv))
    cc = collections.Counter(r[3] for r in rows)
    what = {"A": "a script or an output whose recorded content was on main at some commit and has changed since",
            "B": "a page whose recorded content was on main at some commit and has been written on since",
            "C": "no version with the recorded hash in the file's history on main",
            "D": "the list names a file that is on main's machine and not tracked",
            "E": "the list names a file that is not in the repository"}
    for c in "ABCDE":
        P("   %s  %4d  %s" % (c, cc[c], what[c]))
    a_rows = sorted(r for r in rows if r[3] == "A")
    P("   class A, by arc: %s" % ", ".join("%s %d" % kv for kv in sorted(collections.Counter(r[1].split("/")[1].split("_")[0] for r in a_rows).items())))
    for (k, lst, name, cls, sv) in a_rows:
        P("      %s  %s  sealed content last at %s (%s)" % (k, name, sv[0], sv[1]))

    b_rows = sorted(r for r in rows if r[3] == "B")
    for (k, lst, name, cls, sv) in b_rows:
        P("   class B: %s  %s  sealed content last at %s (%s)" % (k, name, sv[0], sv[1]))
    # entries that name an uncompressed output which is tracked only as its gzip: the record's own claim can still be checked
    import gzip
    raw_checks = []
    for (k, lst, name, state, sig) in st:
        if state not in ("ABSENT", "NOT TRACKED") or name is None:
            continue
        d = os.path.dirname(lst)
        for base in (os.path.join(d, name), os.path.join(d, "verification", name), os.path.join(d, "..", name), name):
            gz = os.path.normpath(base) + ".gz"
            if gz in tracked:
                h = next(G._hash_list_entry(x.strip())[0] for x in (ROOT / lst).read_text(encoding="utf-8", errors="replace").split("\n")
                         if G._hash_list_entry(x.strip()) and G._hash_list_entry(x.strip())[1] == name)
                raw_checks.append({"list": lst, "names": name, "tracked_gzip": gz, "decompresses_to_the_recorded_hash": hashlib.sha256(gzip.open(ROOT / gz, "rb").read()).hexdigest() == h})
                break
    P("   entries that name an uncompressed file tracked only as its gzip: %d; the gzip decompresses to the recorded hash in %d" % (
        len(raw_checks), sum(1 for r in raw_checks if r["decompresses_to_the_recorded_hash"])))
    for r in raw_checks:
        P("      %s  (%s)" % (r["tracked_gzip"], os.path.basename(r["list"])))

    # ---- 4. the table the gate holds every frozen entry to
    frozen = {}
    for (k, lst, name, state, sig) in st:
        if state in ("VERIFIES", "AMBIGUOUS"):
            continue
        assert frozen.get(k, sig) == sig, (k, frozen[k], sig)
        frozen[k] = sig
    old_keys = set(G.ARTIFACT_HASHES_BROKEN)
    assert old_keys <= set(frozen), sorted(old_keys - set(frozen))
    P("")
    P("4. THE FROZEN TABLE")
    P("   keys: %d (%d of them the 63 of 2026-11-10); by state: %s" % (
        len(frozen), len(old_keys & set(frozen)), ", ".join("%s %d" % kv for kv in sorted(collections.Counter(v[0] for v in frozen.values()).items()))))
    P("   ambiguous entries, declared by name in the gate and not frozen: %d" % sum(1 for e in G.hash_list_state(_resolved={}) if e[3] == "AMBIGUOUS"))
    table = {"what": "the entries of main's lists of hashed files that did not verify, each with the state it was found in: 'M:' and the first 16 hex "
                     "digits of the sha256 of the file's content as found, 'N' where the list names no tracked file, 'X' for a hash with no name. The gate "
                     "artifact-hashes refuses an entry that does not verify and is not here, and an entry here whose state has changed.",
             "found": {"the 63 keys of the named lists": "2026-11-10 (B1874), their states on 2026-11-11", "the rest": "2026-11-11 (B1880)"},
             "frozen": dict(sorted(frozen.items()))}
    body = json.dumps(table, indent=1, sort_keys=False) + "\n"
    P("   sha256 of the table: %s" % hashlib.sha256(body.encode("utf-8")).hexdigest())
    if write:
        (ROOT / G.HASH_LISTS_FROZEN_FILE).write_text(body, encoding="utf-8")
        P("   written: %s" % G.HASH_LISTS_FROZEN_FILE)
    (HERE / "all_hash_lists.json").write_text(json.dumps({
        "named_lists": {"entries": len(old), "lists": len({e[1] for e in old}), "do_not_verify": len(old_broken), "distinct_keys": len({e[0] for e in old_broken}),
                        "first_found": dict(first), "files_found_only_from_the_root": len(only_root),
                        "candidate_entries": len(cand), "candidate_entries_from_the_root": len([1 for f, i in cand if i == 2]), "candidate_files_no_other_list_reads": alone,
                        "frozen_script_entries_that_do_not_verify": sum(1 for e in old_broken if e[3] == "MISMATCH" and str(e[2]).endswith(".py")), "frozen_scripts_that_do_not_verify": len(frozen_scripts)},
        "all_lists": {"lists": len(lists), "under_another_name": len(others), "entries": len(st), "states": dict(collections.Counter(e[3] for e in st)),
                      "under_another_name_states": dict(collections.Counter(e[3] for e in o)),
                      "families": {b: dict(fam[b], lists=nlists[b]) for b in sorted(fam)},
                      "lowest_share_among_lists": round(min(shares), 4), "highest_share_among_files_that_are_not_lists": round(max(not_lists), 4) if not_lists else 0.0},
        "other_names_not_verifying": {"classes": dict(cc), "what": what,
                                      "class_A": [{"key": k, "list": lst, "file": name, "sealed_content_last_at": sv[0], "date": sv[1]} for (k, lst, name, cls, sv) in a_rows],
                                      "class_B": [{"key": k, "list": lst, "file": name, "sealed_content_last_at": sv[0], "date": sv[1]} for (k, lst, name, cls, sv) in sorted(r for r in rows if r[3] == "B")]},
        "raw_hashes_checked_against_the_tracked_gzip": raw_checks,
        "frozen_table": {"keys": len(frozen), "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest()},
    }, indent=1) + "\n", encoding="utf-8")
    (HERE / "measure_all_hash_lists_run.txt").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
