#!/usr/bin/env python3
"""Re-audit 5: the programme's refusals about this seat's verdicts, on main at 16b82acda (its B1880).

Main's builder now reads each verdict in this seat's own file at this seat's commit (its rule 21), in answer to the
planted case j4 of re-audit 3.  The seat's old cases j3 and j4 plant on finding E3.  The seat ACCEPTED E3 in re-audit
4, so on this commit they build, and rightly: they are stale, and that is the seat's.  The cases below plant on X2,
whose verdict in re-audit 4 is "agreed: partly".

Each case appends to the programme's source in a scratch clone, commits, runs main's builder, and the clone is reset.
It is run twice: in a clone that HOLDS this seat's commits (as main's own clone does), and in one that does not (as a
fresh clone of main alone would be).  The seat's expectation of each case is written here before the run.
    python3 -B plants_j.py CLONE_AT_MAINS_TIP LABEL"""
import sys, os, re, importlib.util

C = os.path.abspath(sys.argv[1]); LABEL = sys.argv[2]
spec = importlib.util.spec_from_file_location("pv", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools", "planted_violations.py"))
pv = importlib.util.module_from_spec(spec); spec.loader.exec_module(pv)
sh, read, write, WHO = pv.sh, pv.read, pv.write, pv.WHO
base = sh(["git", "rev-parse", "HEAD"], C).stdout.strip()
holds = sh(["git", "cat-file", "-e", "58ae45c70^{commit}"], C).returncode == 0
print("re-audit 5, the programme's refusals: plants at %s, in a clone that %s this seat's commit 58ae45c70 (%s)\n" % (base[:9], "HOLDS" if holds else "does NOT hold", LABEL))
PS = "frontier/B1861_the_closure_programme/verification/programme_source.py"
BP = "frontier/B1861_the_closure_programme/verification/build_programme.py"


def reset():
    sh(["git", "checkout", "-q", "--detach", base], C); sh(["git", "reset", "-q", "--hard", base], C); sh(["git", "clean", "-fdq"], C)
def build(tag, what, addition, expect):
    reset()
    if addition: write(C, PS, read(C, PS) + "\n# a planted change\n" + addition + "\n"); sh(["git", "add", "-A"], C); sh(["git"] + WHO + ["commit", "-q", "-m", "a planted change"], C)
    r = sh([sys.executable, "-B", BP], C); out = r.stdout + r.stderr
    fails = [l.strip() for l in out.splitlines() if re.search(r"REFUSED|refus|^\s*- |FAIL", l)][:3]
    unchecked = [l.strip() for l in out.splitlines() if re.search(r"NOT CHECKED|not checked", l)][:2]
    print("%-4s %-8s %s" % (tag, "REFUSED" if r.returncode != 0 else "BUILT", what))
    for l in fails + unchecked: print("       %s" % l[:240])
    print("       expected by the seat before running: %s" % expect)

ROW_TRUE = '| **X2** three documents each claim supremacy | PARTLY FIXED | **agreed: partly** |'
ROW_FALSE = '| **X2** three documents each claim supremacy | FIXED | **accepted** |'
build("j0", "the clean tree", "", "built" + ("" if holds else ", and it prints that the seat's re-audits are not checked in this clone"))
build("j3x", "a finding the re-audit did not accept marked FIXED (X2)", 'FINDINGS["X2"]["state"] = "FIXED"', "refused: the seat's verdict on X2 is not an acceptance")
build("j4x", "the same, with the verdict retyped as 'accepted' in main's own file", 'FINDINGS["X2"]["state"] = "FIXED"\nACCEPTED["X2"] = "accepted"',
      "refused: the verdict does not begin with the seat's own words in its row ('agreed: partly')")
build("j4y", "the same, with the seat's ROW retyped as well, to a row the seat never wrote",
      'FINDINGS["X2"]["state"] = "FIXED"\nACCEPTED["X2"] = "accepted"\nVERDICT_ROWS["X2"] = [("REAUDIT_4_2026-11-11.md", %r)]' % ROW_FALSE,
      ("refused: the seat's file does not hold that row" if holds else "BUILT, with 'not checked' printed: the row cannot be read where the seat's commit is absent"))
build("j4z", "the true row kept, the verdict retyped to begin with the seat's words and go on to say more: 'agreed: partly; and accepted'",
      'FINDINGS["X2"]["state"] = "FIXED"\nACCEPTED["X2"] = "agreed: partly; and accepted"', "refused: the finding is marked FIXED and the verdict does not begin with 'accepted'")
reset(); print("\nclone reset to", sh(["git", "rev-parse", "--short", "HEAD"], C).stdout.strip(), "| clean:", sh(["git", "status", "--short"], C).stdout.strip() == "")
