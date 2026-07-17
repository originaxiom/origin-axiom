"""Cell 5 (R21-11): deterministic localization of the b353 suite-order leaker.

Imports every tests/test_*.py module in sorted (pytest collection) order and
records every change to the process-global mpmath precision (mp.mp.dps).
This mirrors what pytest does at COLLECTION time: all module-level code runs
before any test executes, so the LAST module-level dps assignment in sorted
order is the precision every runtime-computing test actually sees (the
tests/conftest.py autouse fixture only guards test-to-test leaks, not
collection-time imports).

Read-only: creates no files, mutates nothing outside the interpreter.
"""
import importlib.util
import pathlib
import sys
import time

import mpmath as mp
import os
_REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

REPO = pathlib.Path(_REPO + "")
TESTS = REPO / "tests"
# mirror pyproject pythonpath = ["src", "."] plus pytest's rootdir insertion of tests/
for p in (str(TESTS), str(REPO / "src"), str(REPO)):
    if p not in sys.path:
        sys.path.insert(0, p)

files = sorted(TESTS.glob("test_*.py"))
print(f"scanning {len(files)} test modules in sorted (collection) order")
print(f"initial mp.mp.dps = {mp.mp.dps}")

changes = []
for f in files:
    before = mp.mp.dps
    t0 = time.time()
    status = "ok"
    try:
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[f.stem] = mod
        spec.loader.exec_module(mod)
    except BaseException as e:  # noqa: BLE001 - record and continue
        status = f"IMPORT-ERROR {type(e).__name__}: {e}"
    dt = time.time() - t0
    after = mp.mp.dps
    if after != before:
        changes.append((f.name, before, after))
        print(f"DPS CHANGE  {f.name}: {before} -> {after}   ({dt:.1f}s) [{status}]")
    elif dt > 5.0 or status != "ok":
        print(f"note        {f.name}: dps {after} unchanged ({dt:.1f}s) [{status}]")

print("\n=== summary ===")
print(f"final mp.mp.dps after full collection-order import sweep: {mp.mp.dps}")
print("all dps transitions in order:")
for name, b, a in changes:
    print(f"  {name}: {b} -> {a}")
