#!/usr/bin/env python3
"""Find test functions that pass unconditionally -- locks that cannot fail.

Instituted 2026-07-29. The programme's own ledger already carries this failure twice (E31
"vacuous verification"; MB12 "check the criterion can pass AND can fail"), so it is worth an
instrument rather than another hand-inspection.

Three classes are reported:

  NO-ASSERT      a test function with no assertion and no pytest.raises/fail/warns/approx.
  TAUTOLOGY      `assert True`, or `assert X == X` with syntactically identical sides.
  BOTH-LITERAL   `assert A == B` where BOTH sides trace back to hand-written literals --
                 the subtle one. A "cross-check" comparing two hand-typed copies of the same
                 value verifies its own transcription and nothing else.

CALIBRATION -- read before trusting the BOTH-LITERAL count. The first version of this check
over-reported badly, and the two causes are now excluded explicitly:
  - MUTATED NAMES. `offenders = []` then `offenders.append(...)` inside a real file scan, then
    `assert offenders == []`. The binding is literal; the value is not. Any name that is the
    receiver of a method call, an augmented assign, a subscript store, or a for-target is now
    disqualified.
  - REASSIGNED NAMES. `c = 1` followed by `c = lcm(c, d*d)` in a loop. A name assigned a
    non-literal ANYWHERE in the function is now disqualified, regardless of order.
Even so, BOTH-LITERAL is a REVIEW QUEUE, not a defect list: a genuine remaining category is the
deliberate data-lock written as arithmetic (`assert 52 + 26 == 78`, recording that E6's adjoint
is F4's plus the 26). Those cannot fail either, but they are documentation of banked dimensions
rather than mistakes. Judge each; do not quote the raw count as a defect total.

Run:  python3 scripts/checks/check_test_vacuity.py [--both-literal]
"""
import ast
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
_OK_CALLS = {"raises", "fail", "warns", "approx", "skip", "xfail"}


def _disqualified(fn):
    """Names whose value is not fixed by their literal binding (mutated, reassigned, or branch-dependent)."""
    bad = set()
    assign_counts = {}
    for n in ast.walk(fn):
        # receiver of a method call:  x.append(...)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                and isinstance(n.func.value, ast.Name):
            bad.add(n.func.value.id)
        # augmented assign:  x += ...
        if isinstance(n, ast.AugAssign) and isinstance(n.target, ast.Name):
            bad.add(n.target.id)
        # subscript store:  x[i] = ...  |  multiple assignments (e.g. ok = False ... ok = True)
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Subscript) and isinstance(t.value, ast.Name):
                    bad.add(t.value.id)
                elif isinstance(t, ast.Name):
                    assign_counts[t.id] = assign_counts.get(t.id, 0) + 1
        # loop target:  for x in ...
        if isinstance(n, (ast.For, ast.AsyncFor)):
            for t in ast.walk(n.target):
                if isinstance(t, ast.Name):
                    bad.add(t.id)
        # bound by with/except/comprehension
        if isinstance(n, ast.comprehension):
            for t in ast.walk(n.target):
                if isinstance(t, ast.Name):
                    bad.add(t.id)
    for name, cnt in assign_counts.items():
        if cnt > 1:
            bad.add(name)
    return bad


def _literal_names(fn, bad):
    """Names bound ONLY to literal expressions, iterating to a fixed point."""
    lit = set()
    for _ in range(4):
        grew = False
        for n in ast.walk(fn):
            if isinstance(n, ast.Assign) and len(n.targets) == 1 \
                    and isinstance(n.targets[0], ast.Name):
                name = n.targets[0].id
                if name in bad or name in lit:
                    continue
                if _is_literal(n.value, lit):
                    lit.add(name)
                    grew = True
        if not grew:
            break
    # a name assigned a NON-literal anywhere is disqualified outright
    for n in ast.walk(fn):
        if isinstance(n, ast.Assign) and len(n.targets) == 1 \
                and isinstance(n.targets[0], ast.Name):
            if not _is_literal(n.value, lit):
                lit.discard(n.targets[0].id)
    return lit


def _is_literal(node, lit):
    if isinstance(node, ast.Constant):
        return True
    if isinstance(node, ast.Name):
        return node.id in lit
    if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
        return all(_is_literal(e, lit) for e in node.elts)
    if isinstance(node, ast.Dict):
        return all(k is None or _is_literal(k, lit) for k in node.keys) and \
               all(_is_literal(v, lit) for v in node.values)
    if isinstance(node, ast.UnaryOp):
        return _is_literal(node.operand, lit)
    if isinstance(node, ast.BinOp):
        return _is_literal(node.left, lit) and _is_literal(node.right, lit)
    return False


def _is_pure_literal_assertion(node, lit):
    """True when an assertion test expression depends ONLY on constants/literal bindings."""
    if _is_literal(node, lit):
        return True
    if isinstance(node, ast.Compare):
        return (_is_pure_literal_assertion(node.left, lit)
                and all(_is_pure_literal_assertion(c, lit) for c in node.comparators))
    if isinstance(node, ast.BoolOp):
        return all(_is_pure_literal_assertion(v, lit) for v in node.values)
    if isinstance(node, ast.UnaryOp):
        return _is_pure_literal_assertion(node.operand, lit)
    return False


def check_function_node(fn, rel="<memory>"):
    """Inspect one FunctionDef/AsyncFunctionDef; return (no_assert, tautology, both_lit)."""
    no_assert, tautology, both_lit = [], [], []
    asserts = [n for n in ast.walk(fn) if isinstance(n, ast.Assert)]
    calls = {getattr(getattr(n, "func", None), "attr", None)
             for n in ast.walk(fn) if isinstance(n, ast.Call)}
    if not asserts and not (_OK_CALLS & calls):
        no_assert.append(f"{rel}::{fn.name}")
        return no_assert, tautology, both_lit
    bad = _disqualified(fn)
    lit = _literal_names(fn, bad)
    fn_taut_before = len(tautology)
    for a in asserts:
        t = a.test
        if isinstance(t, ast.Constant) and bool(t.value):
            tautology.append(f"{rel}::{fn.name}:{a.lineno}  (assert {t.value!r})")
            continue
        if isinstance(t, ast.Compare) and len(t.ops) == 1:
            same = ast.dump(t.left) == ast.dump(t.comparators[0])
            if isinstance(t.ops[0], ast.Eq) and same:
                tautology.append(f"{rel}::{fn.name}:{a.lineno}  (assert X == X)")
            elif isinstance(t.ops[0], (ast.Eq, ast.NotEq)) and \
                    _is_literal(t.left, lit) and _is_literal(t.comparators[0], lit):
                both_lit.append(f"{rel}::{fn.name}:{a.lineno}")
    # B1879 (L7 / PV24): a test function with no pytest helper call whose EVERY assertion
    # compares only hand-typed literals cannot fail on any code change and is gated as vacuous.
    # Exception: `if computed_cond: assert False` is an idiom for `pytest.fail(...)`, not a tautology.
    has_guarded_fail = any(
        (isinstance(s, ast.If) and not _is_pure_literal_assertion(s.test, lit)
         and any(isinstance(sub, ast.Assert) and isinstance(sub.test, ast.Constant) and sub.test.value is False
                 for sub in ast.walk(s)))
        or (isinstance(s, (ast.For, ast.AsyncFor, ast.While)) and s.orelse
            and any(isinstance(sub, ast.Assert) and isinstance(sub.test, ast.Constant) and sub.test.value is False
                    for part in s.orelse for sub in ast.walk(part)))
        for s in ast.walk(fn)
    )
    if (asserts and not (_OK_CALLS & calls) and not has_guarded_fail and len(tautology) == fn_taut_before
            and all(_is_pure_literal_assertion(a.test, lit) for a in asserts)):
        tautology.append(f"{rel}::{fn.name}:{asserts[0].lineno}  (pure both-literal function)")
    return no_assert, tautology, both_lit


def scan():
    out = subprocess.run(["git", "-C", ROOT, "ls-files", "tests/*.py"],
                         capture_output=True, text=True, timeout=60).stdout
    no_assert, tautology, both_lit, total = [], [], [], 0
    for rel in out.split():
        try:
            tree = ast.parse(open(os.path.join(ROOT, rel), encoding="utf-8").read())
        except Exception:
            continue
        for fn in ast.walk(tree):
            if not (isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef))
                    and fn.name.startswith("test")):
                continue
            total += 1
            na, ta, bl = check_function_node(fn, rel)
            no_assert.extend(na)
            tautology.extend(ta)
            both_lit.extend(bl)
    return total, no_assert, tautology, both_lit


def main():
    total, no_assert, tautology, both_lit = scan()
    print(f"test functions scanned: {total}")
    print(f"NO-ASSERT: {len(no_assert)}")
    for x in no_assert:
        print("   ", x)
    print(f"TAUTOLOGY: {len(tautology)}")
    for x in tautology:
        print("   ", x)
    print(f"BOTH-LITERAL (review queue, NOT a defect list -- see module docstring): "
          f"{len(both_lit)}")
    if "--both-literal" in sys.argv:
        for x in both_lit:
            print("   ", x)
    # only the two hard classes gate; BOTH-LITERAL needs human judgement
    return 1 if (no_assert or tautology) else 0


if __name__ == "__main__":
    sys.exit(main())
