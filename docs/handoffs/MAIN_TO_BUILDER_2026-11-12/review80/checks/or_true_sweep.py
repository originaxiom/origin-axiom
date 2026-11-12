#!/usr/bin/env python3
"""Every assert, in every tracked python file, whose condition holds whatever is computed because a truthy constant is
joined to it by `or` (at any depth of an or-chain), or because the condition is a truthy constant behind `not not`, etc.
Read by the syntax tree, so a line break inside the assert does not hide it.  Prints file:line and the assert."""
import ast, subprocess, sys, json
files = [f for f in subprocess.run(["git", "ls-files", "*.py"], capture_output=True, text=True).stdout.split("\n") if f]
def always_true(node):
    """True when the expression is true whatever its names hold, as far as this reader goes"""
    if isinstance(node, ast.Constant):
        return bool(node.value)
    if isinstance(node, ast.BoolOp) and isinstance(node.op, ast.Or):
        return any(always_true(v) for v in node.values)
    if isinstance(node, ast.BoolOp) and isinstance(node.op, ast.And):
        return all(always_true(v) for v in node.values)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        return isinstance(node.operand, ast.Constant) and not bool(node.operand.value)
    return False
hits, unread = [], []
for f in files:
    try:
        src = open(f, encoding="utf-8").read(); tree = ast.parse(src)
    except Exception as e:
        unread.append(f); continue
    for n in ast.walk(tree):
        if isinstance(n, ast.Assert) and always_true(n.test):
            seg = ast.get_source_segment(src, n) or ""
            hits.append((f, n.lineno, " ".join(seg.split())[:150]))
for f, l, s in sorted(hits):
    print("%s:%d  %s" % (f, l, s))
print("python files read: %d; not parsed: %d; asserts that cannot fail by a constant: %d" % (len(files) - len(unread), len(unread), len(hits)))
if "--json" in sys.argv:
    json.dump({"hits": hits, "unread": unread, "files": len(files)}, open("audit/review80/or_true_sweep.json", "w"), indent=1)
