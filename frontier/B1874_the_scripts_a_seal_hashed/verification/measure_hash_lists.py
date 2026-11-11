#!/usr/bin/env python3
"""B1874 -- the lists of hashed files, measured: every entry of every tracked ARTIFACT_HASHES*.txt against the tracked file it
names, and for each entry that does not verify, what happened to the file (bookkeeping only; no value is computed).

It uses the gate's own reader (scripts/gates/gates.py: _hash_list_entry, the same path rule), so the page it writes and the
gate's frozen keys describe the same entries.

    python3 -B frontier/B1874_the_scripts_a_seal_hashed/verification/measure_hash_lists.py            print the measurement
    python3 -B frontier/B1874_the_scripts_a_seal_hashed/verification/measure_hash_lists.py --write    and write docs/ARTIFACT_HASHES_BROKEN.md
"""
import collections
import fnmatch
import hashlib
import importlib.util
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("gates_for_b1874", ROOT / "scripts" / "gates" / "gates.py")
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)
say = print
MARK = re.compile(r"post[- ]seal|after the sealed run|after the seal|the sealed (file|code|threshold|script)|after its first launch|after it was sealed", re.I)


def git(*a):
    return subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True)


def entries():
    """(key, list, name as written, resolved path or None, recorded hash, state) for every entry, by the gate's own rule"""
    tracked = set(git("ls-files").stdout.split("\n"))
    out = []
    for lst in sorted(f for f in tracked if fnmatch.fnmatch(os.path.basename(f), G.ARTIFACT_HASH_GLOB)):
        d = os.path.dirname(lst)
        for line in (ROOT / lst).read_text(encoding="utf-8", errors="replace").split("\n"):
            e = G._hash_list_entry(line.strip())
            if e is None:
                continue
            h, name = e
            key = hashlib.sha256(f"{lst}|{name}|{h}".encode("utf-8")).hexdigest()[:12]
            if name is None:
                out.append((key, lst, None, None, h, "NO NAME")); continue
            cands = [os.path.normpath(os.path.join(d, name)), os.path.normpath(os.path.join(d, "verification", name)), os.path.normpath(name)]
            hit = next((c for c in cands if c in tracked), None)
            if hit is None:
                out.append((key, lst, name, None, h, "NOT TRACKED" if any((ROOT / c).exists() for c in cands) else "ABSENT")); continue
            now = hashlib.sha256((ROOT / hit).read_bytes()).hexdigest()
            out.append((key, lst, name, hit, h, "VERIFIES" if now == h else "MISMATCH"))
    return out


def sealed_version(path, h):
    """the newest commit at which the tracked file had the recorded content, or None"""
    for line in git("log", "--follow", "--format=%H %cs", "--", path).stdout.strip().split("\n"):
        if not line:
            continue
        c, d = line.split()
        r = subprocess.run(["git", "-C", str(ROOT), "show", f"{c}:{path}"], capture_output=True)
        if r.returncode == 0 and hashlib.sha256(r.stdout).hexdigest() == h:
            return c[:9], d
    return None


# MAIN'S READING OF CLASS A, entry by entry (added 2026-11-11; B1874 said it was owed, P-772).  For each: what changed after the
# seal, whether the arc's findings disclose it, and whether it bears on how the arc's result was obtained.  Read from the diff
# since the commit that last held the sealed content, and from the arc's findings; nothing was re-run.
READING = {
    "46b056c1d0cd": ("a guard that refuses to count a non-representation", "disclosed (its § 3; a dated note at Review 74)", "no: it changes no count on a representation"),
    "9d9af43f0d7a": ("one line of the mathematics corrected -- the sealed code's block was not a cocycle, and the sealed run's own first-order check read 140 where 0 was due; a third step size added; a stalled seed recorded as an outcome",
                     "disclosed in full (its § 3); the sealed run's output is kept", "YES: every reported number is the corrected instrument's. The predictions and priors were not changed, and the seal's own check is what caught the error"),
    "1425dd14fa31": ("a group's name corrected in the text, and the script's body moved into a function", "disclosed (its § 3 on the two conventions; Review 74)", "no number changed; main has not re-run the moved code here"),
    "5ce1a4764092": ("a note added to the output, saying which group its field counts", "disclosed (as above)", "no: the data lines are identical"),
    "740cbb6a1698": ("the group's name corrected in the text", "disclosed (as above)", "no"),
    "6d730200be1c": ("a note added to the output", "disclosed (as above)", "no: the data lines are identical"),
    "c4c204301962": ("the group's name corrected in the text", "disclosed (as above)", "no"),
    "68f916e3c6ff": ("an import path, one folder off", "NOT disclosed until 2026-11-11: its § 5 tells of a second route added after the seal, and not of this line; a dated note is added", "no, on the mathematics; but the script as sealed could not have imported the module that path names"),
    "c40fd50bc5f9": ("an import path, one folder short", "disclosed (\"corrected before any reading, the only change\")", "no"),
    "ed90ccc5013d": ("the convergence threshold loosened from 1e-40 to 1e-30 after the sealed run stalled at the arithmetic floor; one step size dropped",
                     "disclosed (its § 3); the sealed run's output is kept", "YES: two sealed cells are reported as holding under the loosened criterion, where under the sealed one the instrument skipped the count; the arc's negative rests on that reading. A dated note now marks both cells post hoc"),
    "96d7ceb60570": ("an absolute path made relative", "a hygiene commit; nothing to disclose", "no"),
}


def main():
    E = entries()
    lists = sorted({e[1] for e in E})
    state = collections.Counter(e[5] for e in E)
    broken = [e for e in E if e[5] != "VERIFIES"]
    keys = sorted({e[0] for e in broken})
    assert set(keys) == set(G.ARTIFACT_HASHES_BROKEN), "the gate's frozen keys are not the entries this script finds broken"
    verifies = {(e[1], e[3]) for e in E if e[5] == "VERIFIES"}
    rows = collections.OrderedDict((c, []) for c in "ABCDEFG")
    seen = set()
    for key, lst, name, hit, h, st in sorted(broken, key=lambda e: (e[1], e[2] or "")):
        if key in seen:
            continue
        seen.add(key)
        arc = lst.split("/")[1] if lst.startswith("frontier/") else os.path.dirname(lst) or "."
        short = (hit or name or "").split("/", 2)[-1] if (hit or name or "").startswith("frontier/") else (hit or name or "")
        if st == "NO NAME":
            rows["F"].append(f"| `{key}` | {arc} | — | a hash with no file name beside it |"); continue
        if st == "NOT TRACKED":
            rows["D"].append(f"| `{key}` | {arc} | `{name}` | on main's machine, not tracked |"); continue
        if st == "ABSENT":
            rows["E"].append(f"| `{key}` | {arc} | `{name}` | named by the list, not in the repository |"); continue
        if (lst, hit) in verifies:
            rows["G"].append(f"| `{key}` | {arc} | `{short}` | an earlier version's hash: the same list records the current version too, and that entry verifies |"); continue
        sv = sealed_version(hit, h)
        if sv is None:
            rows["C"].append(f"| `{key}` | {arc} | `{short}` | no version with the recorded hash in the file's history |"); continue
        ns = git("diff", "--numstat", sv[0], "HEAD", "--", hit).stdout.strip().split("\t")
        delta = f"+{ns[0]} −{ns[1]} lines" if len(ns) > 1 else "changed"
        if hit.endswith(".md"):
            rows["B"].append(f"| `{key}` | {arc} | `{short}` | sealed version last at `{sv[0]}` ({sv[1]}); since then {delta} |")
        else:
            marked = bool(MARK.search((ROOT / hit).read_text(encoding="utf-8", errors="replace")))
            what, disclosed, bears = READING[key]                                   # a class-A entry with no reading stops the build
            rows["A"].append(f"| `{key}` | {arc} | `{short}` | sealed version last at `{sv[0]}` ({sv[1]}); since then {delta}; "
                             + ("the change is marked in the file" if marked else "the file does not mark the change")
                             + f" | {what} | {disclosed} | {bears} |")
    n = {c: len(v) for c, v in rows.items()}
    arcsA = sorted({r.split(" | ")[1] for r in rows["A"]})
    unmarked = [r for r in rows["A"] if "does not mark" in r]
    say("lists of hashed files: %d; entries: %d; verify: %d; do not: %d (%d distinct)" % (len(lists), len(E), state["VERIFIES"], len(broken), len(keys)))
    say("  A  a script or an output that a seal hashed, changed since:        %d, in %d arcs; the file marks the change in %d and does not in %d" % (n["A"], len(arcsA), n["A"] - len(unmarked), len(unmarked)))
    say("  B  a page that went on being written after its hash was recorded:   %d" % n["B"])
    say("  C  no version with the recorded hash in the file's history:        %d" % n["C"])
    say("  D  the list names a file on main's machine that is not tracked:    %d" % n["D"])
    say("  E  the list names a file that is not in the repository:            %d" % n["E"])
    say("  F  a hash with no file name:                                       %d" % n["F"])
    say("  G  an earlier version's hash beside the current one, which verifies: %d" % n["G"])
    say("the arcs of class A: %s" % ", ".join(a.split("_")[0] for a in arcsA))
    assert sum(n.values()) == len(keys)
    if "--write" in sys.argv:
        head = ["# THE LISTS OF HASHED FILES: THE ENTRIES THAT DID NOT VERIFY ON 2026-11-10", "",
                "*Generated by `frontier/B1874_the_scripts_a_seal_hashed/verification/measure_hash_lists.py --write`. The gate",
                "`artifact-hashes` reads every tracked `ARTIFACT_HASHES*.txt` on every run and requires each entry to verify against the",
                "tracked file it names. The entries below did not verify when the gate was written. They are frozen by key in",
                "`scripts/gates/gates.py` as a ceiling that may only shrink: a new entry that fails is refused, and so is any change to a",
                "list after it is committed.*", "",
                "**Measured:** %d lists, %d entries, %d verify, %d do not (%d distinct keys)." % (len(lists), len(E), state["VERIFIES"], len(broken), len(keys)), "",
                "| | what main found | entries |", "|---|---|---|",
                "| A | a script or an output that a seal hashed, changed since | %d |" % n["A"],
                "| B | a page that went on being written after its hash was recorded | %d |" % n["B"],
                "| C | no version with the recorded hash in the file's history | %d |" % n["C"],
                "| D | the list names a file that is on main's machine and not tracked | %d |" % n["D"],
                "| E | the list names a file that is not in the repository | %d |" % n["E"],
                "| F | a hash with no file name | %d |" % n["F"],
                "| G | an earlier version's hash; the list records the current version too, and that verifies | %d |" % n["G"], "",
                "**What a row means.** It is a fact about a hash and a file, and not a verdict on an arc. Class A is the one that matters",
                "for a result: the instrument on main differs from the one the seal named. The page says whether the file itself marks the",
                "change. **Read on 2026-11-11, entry by entry** (the last three columns of class A): what changed after the seal, whether the",
                "arc's findings disclose it, and whether it bears on how the result was obtained. Two of the eleven do: one corrected line",
                "of mathematics (B1486) and one loosened convergence criterion (B1499). Both are disclosed in their arcs. One change, an",
                "import path (B1494), was not disclosed until this reading. Nothing was re-run for the reading.",
                "Class B is expected of a page that later took a dated note. Class G is an amendment the list itself records.",
                "Classes C to F are entries that never described a tracked file.", ""]
        titles = {"A": "A script or an output that a seal hashed, changed since", "B": "A page that went on being written",
                  "C": "No version with the recorded hash in the file's history", "D": "Named by a list, on main's machine, not tracked",
                  "E": "Named by a list, not in the repository", "F": "A hash with no file name",
                  "G": "An earlier version's hash beside the current one"}
        body = []
        for c in "ABCDEFG":
            cols = ("| key | arc | file | what main found | what changed after the seal | disclosed in the arc's findings | bears on the result |", "|---|---|---|---|---|---|---|") if c == "A" else (
                "| key | arc | file | what main found |", "|---|---|---|---|")
            body += ["## %s. %s (%d)" % (c, titles[c], n[c]), ""] + list(cols) + rows[c] + [""]
        (ROOT / "docs" / "ARTIFACT_HASHES_BROKEN.md").write_text("\n".join(head + body), encoding="utf-8")
        say("written: docs/ARTIFACT_HASHES_BROKEN.md")


if __name__ == "__main__":
    main()
