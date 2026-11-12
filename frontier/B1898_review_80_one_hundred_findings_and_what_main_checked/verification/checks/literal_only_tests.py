#!/usr/bin/env python3
"""Tests in tests/ whose body uses nothing but literals: every name read is bound inside the test to an expression of
literals, or is one of a few pure builtins.  Such a test computes nothing of the repository and cannot fail unless its
own literals disagree with each other.  Read by the syntax tree at a given commit.  Prints the tests that are of this
shape and are not in the gates' table of tests held by name as found."""
import ast, subprocess, sys, importlib.util
AT = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
PURE = {"len", "sum", "abs", "set", "list", "tuple", "range", "int", "float", "isinstance", "min", "max", "sorted", "all", "any", "str", "bool", "dict", "round", "True", "False", "None"}
def sh(*a): return subprocess.run(["git", *a], capture_output=True, text=True).stdout
files = [f for f in sh("ls-tree", "-r", "--name-only", AT, "tests/").split("\n") if f.endswith(".py")]
def literal_only(fn):
    if fn.args.args or fn.args.kwonlyargs or fn.args.vararg or fn.args.kwarg:
        return False
    bound = set()
    has_assert = False
    for node in ast.walk(fn):
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.Attribute, ast.With, ast.Try, ast.Raise, ast.Global, ast.Nonlocal, ast.Lambda, ast.Await, ast.Yield, ast.YieldFrom)):
            return False
        if isinstance(node, ast.Assert):
            has_assert = True
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            bound.add(node.id)
    for node in ast.walk(fn):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load) and node.id not in bound and node.id not in PURE:
            return False
        if isinstance(node, ast.Call) and not (isinstance(node.func, ast.Name) and node.func.id in PURE):
            return False
    return has_assert
spec = importlib.util.spec_from_file_location("gates", "scripts/gates/gates.py")
g = importlib.util.module_from_spec(spec); sys.modules["gates"] = g; spec.loader.exec_module(g)
held = set(g.CANNOT_FAIL_AS_FOUND)
hits = []
for f in files:
    try:
        tree = ast.parse(sh("show", "%s:%s" % (AT, f)))
    except SyntaxError:
        continue
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name.startswith("test") and literal_only(n):
            hits.append("%s::%s" % (f, n.name))
new = [h for h in hits if h not in held]
print("test files read at %s: %d; tests of this shape: %d; of them held by name as found: %d; not held: %d" % (AT, len(files), len(hits), len(hits) - len(new), len(new)))
for h in new:
    print("  ", h)
