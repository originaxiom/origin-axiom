#!/usr/bin/env python3
"""The web seat's finding 10: the test of B448 on the tower of orbit fields, before and after the patch, with planted changes.

    python3 the_test_of_b448_before_and_after.py <a checkout of the patch> <the commit before the patch>

Each case is the test file with one change, written beside the tests under another name, run, and removed.  The checkout is
left as it was found."""
import pathlib, subprocess, sys
root = pathlib.Path(sys.argv[1]); before_commit = sys.argv[2]
new = (root / "tests" / "test_b448.py").read_text(encoding="utf-8")
old = subprocess.run(["git", "-C", str(root), "show", before_commit + ":tests/test_b448.py"], capture_output=True, text=True, check=True).stdout
def run(text):
    p = root / "tests" / "test_b448_planted_by_the_builder.py"; p.write_text(text, encoding="utf-8")
    try:
        r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:randomly", "-p", "no:cacheprovider", str(p), "-k", "orbit_tower"], capture_output=True, text=True, cwd=str(root))
        return r.stdout.strip().splitlines()[-1].split(" in ")[0]
    finally:
        p.unlink()
a = "            assert sp.Integer(d).is_negative or abs(int(d)) % 5 != 0"
assert old.count(a) == 1 and new.count("    f5 = _eliminant_factors(5)\n") == 1
print("BEFORE THE PATCH")
print("  as it is:                                        ", run(old))
print("  the mended assert negated:                       ", run(old.replace(a, "            assert not (sp.Integer(d).is_negative or abs(int(d)) % 5 != 0)")))
print("  the mended assert replaced by `assert False`:    ", run(old.replace(a, "            assert False")))
print("AFTER THE PATCH")
print("  as it is:                                        ", run(new))
print("  a factor t**2 - t - 1 put into the list:         ", run(new.replace("    f5 = _eliminant_factors(5)\n", "    f5 = _eliminant_factors(5)\n    f5 = f5 + [sp.expand(t**2 - t - 1)]\n")))
print("  the list of degrees denied:                      ", run(new.replace("assert sorted(int(sp.degree(f, t)) for f in f5) == [1, 5]", "assert sorted(int(sp.degree(f, t)) for f in f5) != [1, 5]")))
