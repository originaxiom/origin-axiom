"""the table of what can keep a test from running, by the reader as it was and by the reader of series 5, on every lock"""
import importlib.util, os, subprocess, sys
root, old_path = os.path.abspath(sys.argv[1]), sys.argv[2]
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
old, new = load("ctv_old", old_path), load("ctv_new", os.path.join(root, "scripts/checks/check_test_vacuity.py"))
files = sorted({p for p in subprocess.run(["git", "-C", root, "ls-files"], capture_output=True, text=True).stdout.split("\n") if os.path.basename(p).startswith("test_") and p.endswith(".py")})
module_more, tests_more, same, unparsed = [], [], 0, 0
for f in files:
    src = open(os.path.join(root, f), encoding="utf-8", errors="replace").read()
    a, b = old.switches(src), new.switches(src)
    if a is None or b is None:
        unparsed += 1; continue
    assert set(a) == set(b), f
    assert all(b[k] >= a[k] for k in a), (f, "the reader of series 5 counts less somewhere")
    if b[""] > a[""]:
        module_more.append((f, a[""], b[""]))
    more = [k for k in a if k and b[k] > a[k]]
    if more:
        tests_more.append((f, more))
    if a == b:
        same += 1
print("lock files read:", len(files), "; that do not parse:", unparsed)
print("the two readers give the same table:", same)
print("the module's own switches are more by the reader of series 5:", len(module_more), "files")
print("a test's own switches are more (a mark worn by a name, a class marked in its body):", len(tests_more), "files,", sum(len(m) for _f, m in tests_more), "tests")
for f, more in tests_more[:6]:
    print("    ", f, more[:3])
print("nowhere does the reader of series 5 count less than the reader as it was")
