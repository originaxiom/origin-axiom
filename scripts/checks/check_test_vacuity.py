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

A FOURTH CLASS, 2026-11-11 (the closure programme's WP-0.7, the advisor seat's planted case PV24):

  CANNOT-FAIL    a test function in which NO assert can fail: each one is made of hand-written
                 literals alone, and is true.  `assert 1 != 2` as a test's only assert was counted
                 above "for review" and refused by nothing.

One literal assert among real ones is documentation, and stays in the queue above.  A test whose
every assert is one is a NO-ASSERT test with a sentence in it, and is refused like one.  The class
is decided by working the expression out (`_value`), so that `assert False` under an `if`, or
`assert 1 == 0, "unreachable"`, which fail when they are reached, are not in it; and a name counts
as a literal only if nothing else in the test could have changed it (`_fixed_names`).

Since the same day the scan reads every tracked lock: tests/, and the arcs' own (a file named
test_*.py anywhere), which it had never read.

Run:  python3 scripts/checks/check_test_vacuity.py [--both-literal]
"""
import ast
import operator
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
_OK_CALLS = {"raises", "fail", "warns", "approx", "skip", "xfail"}


def _disqualified(fn):
    """Names whose value is not fixed by their literal binding (mutated or reassigned)."""
    bad = set()
    for n in ast.walk(fn):
        # receiver of a method call:  x.append(...)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                and isinstance(n.func.value, ast.Name):
            bad.add(n.func.value.id)
        # augmented assign:  x += ...
        if isinstance(n, ast.AugAssign) and isinstance(n.target, ast.Name):
            bad.add(n.target.id)
        # subscript store:  x[i] = ...
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Subscript) and isinstance(t.value, ast.Name):
                    bad.add(t.value.id)
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


_UNARY = {ast.USub: operator.neg, ast.UAdd: operator.pos, ast.Not: operator.not_, ast.Invert: operator.invert}
_BINARY = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
           ast.FloorDiv: operator.floordiv, ast.Mod: operator.mod, ast.Pow: operator.pow,
           ast.BitAnd: operator.and_, ast.BitOr: operator.or_, ast.BitXor: operator.xor}
_COMPARE = {ast.Eq: operator.eq, ast.NotEq: operator.ne, ast.Lt: operator.lt, ast.LtE: operator.le,
            ast.Gt: operator.gt, ast.GtE: operator.ge, ast.Is: operator.is_, ast.IsNot: operator.is_not,
            ast.In: lambda a, b: a in b, ast.NotIn: lambda a, b: a not in b}


def _value(node, names):
    """The value of an expression made of hand-written literals alone: their arithmetic, their comparisons,
    an entry taken out of one.  Raises on anything else: a call, an attribute, a name that is not in
    `names`.  A call is a computation, whatever it calls, and this function works none out."""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        return names[node.id]
    if isinstance(node, ast.Tuple):
        return tuple(_value(e, names) for e in node.elts)
    if isinstance(node, ast.List):
        return [_value(e, names) for e in node.elts]
    if isinstance(node, ast.Set):
        return {_value(e, names) for e in node.elts}
    if isinstance(node, ast.Dict):
        return {_value(k, names): _value(v, names) for k, v in zip(node.keys, node.values)}
    if isinstance(node, ast.UnaryOp):
        return _UNARY[type(node.op)](_value(node.operand, names))
    if isinstance(node, ast.BinOp):
        a, b = _value(node.left, names), _value(node.right, names)
        numbers = isinstance(a, (int, float, complex)) and isinstance(b, (int, float, complex))
        if isinstance(node.op, ast.Mult) and not numbers:
            raise ValueError("a repeated sequence is not worked out here")
        if isinstance(node.op, ast.Pow) and not (numbers and abs(a) <= 10 ** 6 and abs(b) <= 64):
            raise ValueError("a large power is not worked out here")
        return _BINARY[type(node.op)](a, b)
    if isinstance(node, ast.IfExp):
        return _value(node.body if _value(node.test, names) else node.orelse, names)
    if isinstance(node, ast.Subscript) and not isinstance(node.slice, ast.Slice):
        return _value(node.value, names)[_value(node.slice, names)]
    if isinstance(node, ast.BoolOp):
        for v in node.values:                         # `and` and `or` as Python reads them, left to right
            last = _value(v, names)
            if bool(last) != isinstance(node.op, ast.And):
                return last
        return last
    if isinstance(node, ast.Compare):
        left = _value(node.left, names)
        for op, c in zip(node.ops, node.comparators):
            right = _value(c, names)
            if not _COMPARE[type(op)](left, right):
                return False
            left = right
        return True
    raise ValueError("not a literal")


def _fixed_names(fn):
    """The names of a test whose value nothing in the test can have changed, with those values.

    Stricter than `_literal_names`, because this class refuses where that one only queues.  A name is
    here only if it is bound once, by a plain assignment at the top level of the function, to an
    expression of literals; is not mutated (`_disqualified`); and is used nowhere but inside an assert
    or inside another such binding -- a list handed to a call may come back filled."""
    bad = _disqualified(fn)
    bound = {}
    for n in ast.walk(fn):
        targets = []
        if isinstance(n, ast.Assign):
            targets = n.targets
        elif isinstance(n, (ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
            targets = [n.target]
        elif isinstance(n, (ast.For, ast.AsyncFor, ast.comprehension)):
            targets = [n.target]
        elif isinstance(n, (ast.With, ast.AsyncWith)):
            targets = [i.optional_vars for i in n.items if i.optional_vars is not None]
        elif isinstance(n, ast.ExceptHandler) and n.name:
            bound[n.name] = bound.get(n.name, 0) + 1
        elif isinstance(n, (ast.Global, ast.Nonlocal)):
            bad.update(n.names)
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            bad.update((a.asname or a.name).split(".")[0] for a in n.names)
        elif isinstance(n, ast.Delete):
            targets = n.targets
        for t in targets:
            for x in ast.walk(t):
                if isinstance(x, ast.Name):
                    bound[x.id] = bound.get(x.id, 0) + 1
    bad.update(a.arg for a in ast.walk(fn) if isinstance(a, ast.arg))          # an argument is given, not written
    top = [n for n in fn.body if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)
           and n.targets[0].id not in bad and bound.get(n.targets[0].id) == 1]
    inside = set()                                   # every Name node that sits in an assert, or in one of those bindings
    for n in [a for a in ast.walk(fn) if isinstance(a, ast.Assert)] + top:
        inside.update(id(x) for x in ast.walk(n) if isinstance(x, ast.Name))
    elsewhere = {x.id for x in ast.walk(fn) if isinstance(x, ast.Name) and id(x) not in inside}
    names = {}
    for n in top:                                    # in the order written: a binding may use the ones above it
        name = n.targets[0].id
        if name in elsewhere:
            continue
        try:
            names[name] = _value(n.value, names)
        except Exception:
            pass
    return names


def cannot_fail(fn):
    """True when the test function has asserts and none of them can fail: each is made of literals
    alone, and is true.  An assert that works out false fails when it is reached, and so can fail."""
    asserts = [n for n in ast.walk(fn) if isinstance(n, ast.Assert)]
    calls = {getattr(n.func, "attr", None) or getattr(n.func, "id", None) for n in ast.walk(fn) if isinstance(n, ast.Call)}
    if not asserts or (_OK_CALLS & calls) or any("assert" in str(c).lower() for c in calls):
        return False                                 # pytest.raises and the like, or a call such as assert_allclose, can fail
    if any(isinstance(x, (ast.Call, ast.Attribute)) for a in asserts for x in ast.walk(a.test)):
        return False                                 # the common case, decided before the names are read: something is computed
    names = _fixed_names(fn)
    for a in asserts:
        try:
            if not _value(a.test, names):
                return False
        except Exception:
            return False                             # something is computed: the assert can fail
    return True


def _lock_files():
    """every tracked file the scan reads: tests/*.py as before, and the arcs' own locks, a file named test_*.py anywhere"""
    out = subprocess.run(["git", "-C", ROOT, "ls-files", "tests/*.py", ":(glob)**/test_*.py"],
                         capture_output=True, text=True, timeout=60).stdout
    return sorted(set(out.split()))


def read_locks():
    """One pass over every tracked lock.  Returns a table: the four classes, each a list of findings, and
    under "total" the number of test functions read, in tests/ and elsewhere."""
    r = {"NO-ASSERT": [], "TAUTOLOGY": [], "BOTH-LITERAL": [], "CANNOT-FAIL": [], "total": {"tests": 0, "elsewhere": 0}}
    for rel in _lock_files():
        try:
            tree = ast.parse(open(os.path.join(ROOT, rel), encoding="utf-8").read())
        except Exception:
            continue
        for fn in ast.walk(tree):
            if not (isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef))
                    and fn.name.startswith("test")):
                continue
            r["total"]["tests" if rel.startswith("tests/") else "elsewhere"] += 1
            asserts = [n for n in ast.walk(fn) if isinstance(n, ast.Assert)]
            calls = {getattr(getattr(n, "func", None), "attr", None)
                     for n in ast.walk(fn) if isinstance(n, ast.Call)}
            if not asserts and not (_OK_CALLS & calls):
                r["NO-ASSERT"].append(f"{rel}::{fn.name}")
                continue
            if cannot_fail(fn):
                r["CANNOT-FAIL"].append(f"{rel}::{fn.name}")
            bad = _disqualified(fn)
            lit = _literal_names(fn, bad)
            for a in asserts:
                t = a.test
                if isinstance(t, ast.Constant) and bool(t.value):
                    r["TAUTOLOGY"].append(f"{rel}::{fn.name}:{a.lineno}  (assert {t.value!r})")
                    continue
                if isinstance(t, ast.Compare) and len(t.ops) == 1:
                    same = ast.dump(t.left) == ast.dump(t.comparators[0])
                    if isinstance(t.ops[0], ast.Eq) and same:
                        r["TAUTOLOGY"].append(f"{rel}::{fn.name}:{a.lineno}  (assert X == X)")
                    elif isinstance(t.ops[0], (ast.Eq, ast.NotEq)) and \
                            _is_literal(t.left, lit) and _is_literal(t.comparators[0], lit):
                        r["BOTH-LITERAL"].append(f"{rel}::{fn.name}:{a.lineno}")
    return r


def scan():
    """the three first classes over tests/, as this function has always returned them"""
    r = read_locks()
    mine = lambda xs: [x for x in xs if x.startswith("tests/")]
    return r["total"]["tests"], mine(r["NO-ASSERT"]), mine(r["TAUTOLOGY"]), mine(r["BOTH-LITERAL"])


def main():
    r = read_locks()
    total, no_assert, tautology, both_lit = r["total"]["tests"] + r["total"]["elsewhere"], r["NO-ASSERT"], r["TAUTOLOGY"], r["BOTH-LITERAL"]
    print(f"test functions scanned: {total} ({r['total']['elsewhere']} of them in the arcs' own locks)")
    print(f"CANNOT-FAIL (the gate refuses one that is not held by name): {len(r['CANNOT-FAIL'])}")
    for x in r["CANNOT-FAIL"]:
        print("   ", x)
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
