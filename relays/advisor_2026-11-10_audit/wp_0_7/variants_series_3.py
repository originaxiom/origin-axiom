#!/usr/bin/env python3
"""WP-0.7, series 3: this seat's own variants on its own mends, before the series is sent.

Series 3 mends the five planted cases in which a gate read less than it is about (PV16, PV17, PV20, PV21, PV24), and the
gap main's unseen case U9.b found in series 1.  Main verifies with cases this seat has not seen.  These are other shapes of
the same violations, run on the real pages in a scratch clone, where the series' own lock uses small pages of its own.

    python3 variants_series_3.py --src CLONE --work DIR      (CLONE: a clone holding the series at its HEAD)

Nothing is written into CLONE.  DIR is emptied and used for the scratch clone and two exports.

EXPECTATIONS, written before the first run.  "red" = the named gate returns False.  Six of them are PASSES: each is a limit
of a mend, stated in the note, and the variant pins where the limit lies.
  the framing gate
    t1   a banned phrase in a new .tex file under papers/                       framing red, naming the file
    t2   the phrase in another letter case in a new arc's arc_verdict.json      framing red
    t3   the phrase broken over two lines of a page under docs/                 framing red
    t4   the phrase in a data file above 5 MB                                   framing PASSES, and counts one more file not read
    t5   the exempt report copied under another name                            framing red: the exemption is the file's
  the claims gate
    t6   a proven row whose evidence names an arc's folder and no test          claims red, naming the row
    t7   P51 given a lock                                                       claims passes and says the table can be shortened
    t8   a row of the certified data cut to no evidence                         claims red
  the vacuity gate
    t9   the planted test inside an arc's own lock                              test-vacuity red
    t10  a test that is held by name, copied into another file                  test-vacuity red: held by its file and its name
    t11  a test whose only assert is `assert len([1, 2]) == 2`                  test-vacuity PASSES: the class stops at a call
    t12  one of the 26 held tests mended                                        test-vacuity passes and says one of the table is mended
  the retraction sweep
    t13  each of the 17 newly swept phrases, one at a time, on the front page   retraction-sweep red, 17 times of 17
    t14  the two rows named as readings, on the front page                      retraction-sweep PASSES: read and not swept
    t15  a row added to the registry with a bare number and no backticks        retraction-sweep red: in no shape the sweep reads
    t16  a newly swept phrase in capitals in a .tex file                        retraction-sweep red
    t17  a second instance of a held phrase, in the file that holds it          retraction-sweep PASSES: held by file and phrase
  the controls gate
    t18  one gate's control pointed at another real test                        gate-controls red: a control left the register
    t19  one control marked skip where it stands                                gate-controls red
    t20  one control's body replaced by an assert on something else             gate-controls PASSES: reading cannot show it
  the gap of series 1 (main's U9.b)
    t21  the whole tree exported into a folder made a repository, no commit     every gate of the table refused, none passes
    t22  the same, with one commit that holds only a note                       read as untracked: every gate of the table
                                                                                refused, none passes

  t22 AS FIRST WRITTEN expected the folder to be read as full, and counted the gates that pass: a read-out.  The first whole
  run (variants_series_3_first_whole_run_out.txt) read 8 of 24 passing there.  The seat then closed it, in the patch that
  closes main's case, and the expectation above was written before the run that judges it.
"""
import sys, os, re, json, shutil, subprocess

src = os.path.abspath(sys.argv[sys.argv.index("--src") + 1])
work = os.path.abspath(sys.argv[sys.argv.index("--work") + 1])
WHO = ["-c", "user.name=originaxiom", "-c", "user.email=planted@example.invalid"]
FIVE = ["framing", "claims", "test-vacuity", "retraction-sweep", "gate-controls"]
RUN = r'''
import sys, json, importlib.util
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("gates_under_variants", "scripts/gates/gates.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
names = sorted(g.READS_GIT) if sys.argv[1] == "THE-TABLE" else sys.argv[1].split(",")
out = {"_state": [g.checkout_state(), "", ""]}
for name in names:
    try:
        r = g.GATES[name](); d = r[1] if isinstance(r[1], str) else " | ".join(map(str, r[1]))
        out[name] = [bool(r[0]), d[:600], g.result_line(name, bool(r[0]), d).strip()[:600]]
    except Exception as e:
        out[name] = [None, "RAISED %s: %s" % (type(e).__name__, str(e)[:200]), ""]
print(json.dumps(out))
'''


def sh(args, cwd=None, check=True, env=None, binary=False):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=not binary, env=env)
    if check and r.returncode != 0:
        sys.exit("failed: %s\n%s" % (" ".join(map(str, args))[:200], (r.stderr if not binary else r.stderr.decode("utf-8", "replace"))[:400]))
    return r


def gates(tree, names):
    arg = names if isinstance(names, str) else ",".join(names)
    r = subprocess.run([sys.executable, "-B", "-c", RUN, arg], cwd=tree, capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    try:
        return json.loads(r.stdout.strip().split("\n")[-1])
    except Exception:
        sys.exit("the gates did not run in %s: %s" % (tree, (r.stdout + r.stderr)[-400:]))


if os.path.exists(work):
    shutil.rmtree(work)
os.makedirs(work)
clone = os.path.join(work, "clone")
sh(["git", "clone", "-q", "file://" + src, clone])
tip = sh(["git", "-C", clone, "rev-parse", "HEAD"]).stdout.strip()
print("variants on the series at %s" % tip[:9])
path = lambda rel: os.path.join(clone, rel)
read = lambda rel: open(path(rel), encoding="utf-8").read()


def write(rel, text):
    os.makedirs(os.path.dirname(path(rel)), exist_ok=True)
    with open(path(rel), "w", encoding="utf-8") as fh:
        fh.write(text)


def reset():
    sh(["git", "-C", clone, "reset", "-q", "--hard", tip]); sh(["git", "-C", clone, "clean", "-q", "-fd"])


def commit(text):
    sh(["git", "-C", clone, "add", "-A"]); sh(["git", "-C", clone, *WHO, "commit", "-q", "-m", text])
    return sh(["git", "-C", clone, "rev-parse", "HEAD"]).stdout.strip()


results = []


def line(tag, ok, text):
    results.append(bool(ok)); print("%-4s %-6s %s" % (tag, "HOLDS" if ok else "FAILS", text), flush=True)


def one(name):
    return gates(clone, [name])[name]


control = gates(clone, FIVE)
assert all(control[n][0] for n in FIVE), "the five gates must be green before any variant: %s" % {k: v[1][:80] for k, v in control.items() if k in FIVE and not v[0]}
print("control: the five gates pass on the series as it stands")
sys.path.insert(0, os.path.join(clone, "scripts", "gates")); sys.path.insert(0, os.path.join(clone, "scripts", "checks"))
import gates as G                                            # the series' own tables: the banned phrases, the held names
import retraction_sweep as RS
banned = G.BANNED[1]

# ---- the framing gate
reset(); write("papers/planted_note.tex", "\\section{A note}\nIn this note " + banned + ".\n"); commit("planted: a banned phrase in a .tex")
r = one("framing"); line("t1", r[0] is False and "papers/planted_note.tex" in r[1], "a banned phrase in a .tex under papers/: %s" % r[1][:110])
reset(); write("frontier/B9999_planted_arc/arc_verdict.json", json.dumps({"verdict": "PROVED", "claim_one_line": banned.upper()})); commit("planted: in a verdict file, in capitals")
r = one("framing"); line("t2", r[0] is False and "arc_verdict.json" in r[1], "in capitals in an arc's verdict file: %s" % r[1][:110])
reset(); first, rest = banned.split(" ", 1); write("docs/PLANTED_PAGE.md", "# A page\n\nIt is said that " + first + "\n" + rest + ", and more.\n"); commit("planted: over two lines")
r = one("framing"); line("t3", r[0] is False and "docs/PLANTED_PAGE.md" in r[1], "broken over two lines: %s" % r[1][:110])
reset(); before = re.search(r"not read: (\d+) above", control["framing"][1]).group(1)
# (the first run stopped here: the file was named census.jsonl, an ending the repository's ignore list holds, so the planted
#  commit had nothing in it and failed.  The file has another ending now.  No expectation is changed.)
write("frontier/B9999_planted_arc/census_rows.json", (json.dumps({"row": "x" * 80}) + "\n") * 70000 + banned + "\n"); commit("planted: in a data file above the limit")
r = one("framing"); after = re.search(r"not read: (\d+) above", r[1])
line("t4", r[0] is True and after is not None and int(after.group(1)) == int(before) + 1, "in a %d MB data file: passes; files above the limit %s -> %s" % (
    os.path.getsize(path("frontier/B9999_planted_arc/census_rows.json")) // 1000000, before, after.group(1) if after else "?"))
reset(); shutil.copy(path("frontier/B887_gate_audit/audit_reports.json"), path("frontier/B887_gate_audit/audit_reports_copy.json")); commit("planted: the exempt report under another name")
r = one("framing"); line("t5", r[0] is False and "audit_reports_copy.json" in r[1], "the exempt report copied under another name: %s" % r[1][:110])

# ---- the claims gate
reset(); c = read("CLAIMS.md"); anchor_row = re.search(r"^\| P16 \|.*$", c, re.M).group(0)
write("CLAIMS.md", c.replace(anchor_row, anchor_row + "\n| P998 | A planted proven claim. | `frontier/B575_bridge_obstruction` (exact) ✓ |")); commit("planted: a proven row citing a folder")
r = one("claims"); line("t6", r[0] is False and "P998" in r[1], "a proven row whose evidence is an arc's folder: %s" % r[1][:120])
reset(); p51 = re.search(r"^\| P51 \|.*$", c, re.M).group(0)
write("CLAIMS.md", c.replace(p51, p51.rstrip().rstrip("|").rstrip() + " `tests/test_derived_potential.py` |")); commit("planted: P51 given a lock")
r = one("claims"); line("t7", r[0] is True and "shorten the table" in r[1] and "P51" in r[1], "P51 given a lock: %s" % r[1][:170])
reset(); e_row = [l for l in c.split("## Certified data")[1].split("\n## ")[0].split("\n") if re.match(r"\| E\d+ \|", l)][2]
cells = e_row.split("|"); cells[-2] = " (see the arc) "
write("CLAIMS.md", c.replace(e_row, "|".join(cells))); commit("planted: a certified row with no evidence")
r = one("claims"); line("t8", r[0] is False and re.search(r"\bE\d+\b", r[1]) is not None, "a row of the certified data cut to no evidence: %s" % r[1][:120])

# ---- the vacuity gate
reset(); arcs = sh(["git", "-C", clone, "ls-files", "--", ":(glob)frontier/**/test_*.py"]).stdout.split()
host = arcs[len(arcs) // 2]; write(host, read(host) + "\n\ndef test_planted_orbit_counts_differ():\n    assert 1 != 2\n"); commit("planted: in an arc's own lock")
r = one("test-vacuity"); line("t9", r[0] is False and host in r[1], "the planted test in one of %d arcs' own locks: %s" % (len(arcs), r[1][:120]))
reset(); held = sorted(G.CANNOT_FAIL_AS_FOUND)[0]; hf, hn = held.split("::")
body = re.search(r"^def %s\(.*?(?=^def |\Z)" % re.escape(hn), read(hf), re.M | re.S).group(0)
write("tests/test_zz_planted_copy.py", body.rstrip() + "\n"); commit("planted: a held test copied into another file")
r = one("test-vacuity"); line("t10", r[0] is False and "tests/test_zz_planted_copy.py::" + hn in r[1], "a held test copied under the same name into another file: %s" % r[1][:120])
reset(); write("tests/test_zz_planted_call.py", "def test_planted_length():\n    assert len([1, 2]) == 2\n"); commit("planted: a call on literals")
r = one("test-vacuity"); line("t11", r[0] is True, "`assert len([1, 2]) == 2` as a test's only assert: passes (the class stops at a call)")
reset(); t = read("tests/test_b710_thimbles.py"); assert t.count("    assert 1 != 2\n") == 1
write("tests/test_b710_thimbles.py", t.replace("    assert 1 != 2\n", "    assert len({1, 2}) == 2\n")); commit("planted: one of the held tests given a computed assert")
r = one("test-vacuity"); line("t12", r[0] is True and "1 of that table mended or gone" in r[1], "one of the 26 mended: %s" % r[1][-140:])

# ---- the retraction sweep
reg = read("docs/RETRACTED_PHRASES.md")
old29 = set()
for l in reg.split("\n"):                                     # the two shapes the sweep read before this series
    m = re.match(r"\|\s*\d+\s*\|\s*`([^`]+)`", l) or re.match(r'\|\s*["“]([^"”]+)["”]\s*(\(.*?)?\|', l)
    if m:
        old29.add(m.group(1).strip())
new17 = [p for p in RS.phrases_in(reg) if p not in old29]
readme = read("README.md"); caught = []
for p in new17:
    reset(); write("README.md", readme + "\n" + p[0].upper() + p[1:] + ".\n"); commit("planted: a newly swept phrase on the front page")
    r = one("retraction-sweep")
    if r[0] is False and "README.md" in r[1]:
        caught.append(p)
line("t13", len(new17) == 17 and len(caught) == 17, "%d newly swept phrases, each pasted alone on the front page: %d caught%s" % (
    len(new17), len(caught), "" if len(caught) == len(new17) else "; NOT caught: " + "; ".join(p[:40] for p in new17 if p not in caught)))
reset(); named = [RS._without_its_note(k) for k in RS.NOT_SWEPT_BY_NAME]
write("README.md", readme + "".join("\n" + p[0].upper() + p[1:] + ".\n" for p in named)); commit("planted: the two readings' sentences on the front page")
r = one("retraction-sweep"); line("t14", len(named) == 2 and r[0] is True, "the two rows named as readings, their sentences on the front page: passes (read and not swept)")
reset(); write("docs/RETRACTED_PHRASES.md", reg.rstrip("\n") + "\n\n| # | phrase | arc | why |\n|---|---|---|---|\n| 12 | a planted sentence with no backticks | B9999 | planted |\n"); commit("planted: a row in no shape")
r = one("retraction-sweep"); line("t15", r[0] is False and "in no shape the sweep reads" in r[1], "a row with a bare number and no backticks: %s" % r[1][:120])
reset(); p = next(q for q in new17 if q.startswith("both hands"))
write("papers/planted_note.tex", "\\section{A note}\n\\textbf{" + p.upper() + "}.\n"); commit("planted: a newly swept phrase in capitals in a .tex")
r = one("retraction-sweep"); line("t16", r[0] is False and "papers/planted_note.tex" in r[1], "a newly swept phrase in capitals, in emphasis, in a .tex: %s" % r[1][:120])
reset(); (hfile, hphrase) = sorted(RS.STANDS_AS_FOUND)[0]
write(hfile, read(hfile) + "\nAnd again: " + hphrase + ".\n"); commit("planted: a second instance in the file that holds one")
r = one("retraction-sweep"); line("t17", r[0] is True, "a second instance of a held phrase in the file that holds it: passes (held by file and phrase, not by line)")

# ---- the controls gate
regc = json.loads(read("tests/GATE_CONTROLS.json"))
reset(); moved = dict(regc); moved["framing"] = regc["claims"]
write("tests/GATE_CONTROLS.json", json.dumps(moved, indent=1) + "\n"); commit("planted: one gate's control pointed at another real test")
r = one("gate-controls"); line("t18", r[0] is False and "1 control(s) left" in r[1] and "framing ->" in r[1], "the framing gate pointed at the claims gate's control: %s" % r[1][:130])
reset(); cf, cn = regc["framing"].split("::"); t = read(cf); assert t.count("def %s(" % cn) == 1
write(cf, t.replace("def %s(" % cn, "@pytest.mark.skip(reason='planted')\ndef %s(" % cn)); commit("planted: a control marked skip")
r = one("gate-controls"); line("t19", r[0] is False and "framing" in r[1] and "is skipped" in r[1], "the framing gate's control marked skip where it stands: %s" % r[1][:130])
reset(); old_body = re.search(r"^def %s\(.*?(?=^def |\Z)" % re.escape(cn), t, re.M | re.S).group(0)
head = old_body.split("\n")[0]
write(cf, t.replace(old_body, head + "\n    assert sorted([2, 1])[0] == 1\n\n\n")); commit("planted: a control that asserts something else")
r = one("gate-controls"); line("t20", r[0] is True, "the framing gate's control replaced, under its own name, by an assert on something else: passes (reading cannot show it)")

# ---- the gap of series 1: main's unseen case U9.b, on the whole tree
reset()
for tag, with_commit in (("t21", False), ("t22", True)):
    folder = os.path.join(work, "export_" + tag); os.makedirs(folder)
    tar = sh(["git", "-C", clone, "archive", tip], binary=True).stdout
    subprocess.run(["tar", "-x", "-C", folder], input=tar, check=True)
    sh(["git", "-C", folder, "init", "-q"])
    if with_commit:
        with open(os.path.join(folder, "A_NOTE_OF_ITS_OWN.txt"), "w") as fh:
            fh.write("the only file this repository holds\n")
        sh(["git", "-C", folder, "add", "A_NOTE_OF_ITS_OWN.txt"]); sh(["git", "-C", folder, *WHO, "commit", "-q", "-m", "a note"])
    out = gates(folder, "THE-TABLE"); state = out.pop("_state")[0]
    passing = sorted(n for n, v in out.items() if v[0])
    refused = sorted(n for n, v in out.items() if v[0] is False and "refused" in v[1])
    if not with_commit:
        line(tag, state == "empty" and not passing and len(refused) == len(out), "the whole tree in a folder made a repository, no commit: read as %r; %d of %d gates of the table refused, %d pass" % (
            state, len(refused), len(out), len(passing)))
    else:
        line(tag, state == "untracked" and not passing and len(refused) == len(out), "the same with one commit that holds only a note: read as %r; %d of %d gates of the table refused, %d pass%s" % (
            state, len(refused), len(out), len(passing), (": " + ", ".join(passing)) if passing else ""))
    shutil.rmtree(folder, ignore_errors=True)

print("\n%d of %d expectations hold" % (sum(results), len(results)))
