#!/usr/bin/env python3
"""Four planted cases for the agy lane's gate against tests that cannot fail (branch agy/stage4-sync-2026-11-11 at
b4ddb600b), written after reading the lane's edits to twenty older tests and not published before.

The lane made that gate stronger, and the seat's planted cases PV12 and PV24 are caught there.  In the same commits it
rewrote twenty older tests.  Read side by side, many of the rewrites keep a typed number and reach it by one more step:
    main:      assert 73 * 2 == 146
    the lane:  slope = sp.Rational(73, 50); assert int(slope * 100) == 146
Neither can fail, whatever the arc under test does.  The question put here: does the gate tell them apart?

Each case is planted in a scratch clone at the lane's tip, committed there, the gate is run from that clone on the
clean tree, and the clone is reset.  The seat's expectation of each case is written here before the run.
    python3 -B variants_on_the_lanes_vacuity_gate.py CLONE_AT_THE_LANES_TIP MAINS_COMMIT_BEFORE_THE_LANE"""
import sys, os, re, json, importlib.util

C = os.path.abspath(sys.argv[1]); BEFORE = sys.argv[2]
spec = importlib.util.spec_from_file_location("pv", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools", "planted_violations.py"))
pv = importlib.util.module_from_spec(spec); spec.loader.exec_module(pv)
sh, read, write, WHO = pv.sh, pv.read, pv.write, pv.WHO
base = sh(["git", "rev-parse", "HEAD"], C).stdout.strip()
print("variants on the lane's gate against tests that cannot fail: plants at", base[:9], "\n")


def reset():
    sh(["git", "checkout", "-q", "--detach", base], C); sh(["git", "reset", "-q", "--hard", base], C); sh(["git", "clean", "-fdq"], C)
def commit(msg="a planted violation"):
    sh(["git", "add", "-A"], C); sh(["git"] + WHO + ["commit", "-q", "-m", msg], C)
def gate(name="test-vacuity"):
    code = ("import sys, json; sys.path.insert(0, 'scripts/gates'); import gates\n"
            "try:\n    r = gates.GATES[%r](); out = [bool(r[0]), str(r[1])]\n"
            "except Exception as exc:\n    out = [False, 'EXCEPTION ' + repr(exc)]\n"
            "print('@@' + json.dumps(out))\n" % name)
    r = sh([sys.executable, "-B", "-c", code], C)
    m = re.search(r"@@(\[.*\])", r.stdout)
    return json.loads(m.group(1)) if m else [None, "no output: " + (r.stderr or r.stdout)[-300:]]
def show(tag, what, expect):
    r = gate()
    print("%-4s %-11s %s" % (tag, "CAUGHT" if r[0] is False else "NOT CAUGHT", what))
    print("       the gate: %s" % r[1][:260]); print("       expected by the seat before running: %s" % expect)

reset(); r = gate(); print("clean tree: test-vacuity %s  %s\n" % ("FAIL" if r[0] is False else "PASS", r[1][:200]))

# q1: one of the twenty, put back as main has it
old = sh(["git", "show", BEFORE + ":tests/test_b776_b685.py"], C).stdout
assert "assert 73 * 2 == 146" in old
reset(); write(C, "tests/test_b776_b685.py", old); commit()
show("q1", "tests/test_b776_b685.py put back as main has it (it holds: assert 73 * 2 == 146)", "caught: the plain form is what the lane's gate refuses, which is why the lane rewrote it")

# q2: the lane's own rewrite of that line, in a new test of a new name
reset(); write(C, "tests/test_zz_a_planted_dressed_number.py", "import sympy as sp\n\n\ndef test_a_number_reached_by_one_more_step():\n    slope = sp.Rational(73, 50)\n    assert int(slope * 100) == 146\n"); commit()
show("q2", "a new test whose only line is the lane's rewrite: slope = sp.Rational(73, 50); assert int(slope * 100) == 146", "NOT caught: it cannot fail either, and the gate does not see it")

# q3: a control, the plain form in a new test
reset(); write(C, "tests/test_zz_a_planted_plain_number.py", "def test_a_plain_number():\n    assert 73 * 2 == 146\n"); commit()
show("q3", "a new test whose only line is the plain form: assert 73 * 2 == 146", "caught (a control)")

# q4: a second rewrite of the lane's, in a new test
reset(); write(C, "tests/test_zz_a_planted_sum.py", "def test_a_sum_of_typed_numbers():\n    strata = (63, 6, 1, 11)\n    assert sum(strata) == 81 == pow(3, 4)\n"); commit()
show("q4", "a new test whose only lines are another of the lane's rewrites: strata = (63, 6, 1, 11); assert sum(strata) == 81 == pow(3, 4)", "NOT caught")
reset(); print("\nclone reset to", sh(["git", "rev-parse", "--short", "HEAD"], C).stdout.strip(), "| clean:", sh(["git", "status", "--short"], C).stdout.strip() == "")
