"""CERTIFICATE -- the "<repo>/" placeholder substituted into executable code.

WHAT WENT WRONG.  The repository forbids absolute machine paths in committed .py files
(tests/test_no_hardcoded_paths.py).  The cleanup that enforced that rule replaced one
bench's absolute checkout path in front of "frontier/X" with the DOCUMENTATION placeholder
"<repo>/frontier/X".  In prose that is exactly right.  In code it is a dead path: Python
opens the literal directory "<repo>", which does not exist.  The guard went green and the
scripts stopped working -- a portability defect converted into a correctness defect,
invisible to the guard that caused it.

Confirmed instance: frontier/B1306_the_older_debt/verification/sliceC/c_e8_types.py died on
  FileNotFoundError: .../sliceC/<repo>/frontier/B1275_e8_family_verified/.../e8_family.py
and with it tests/test_b1306_the_older_debt.py::test_slice_c_own_rederivations_are_pinned.

WHAT THIS CERTIFICATE CHECKS (three cells, each two-outcome, preregistered):

  CELL 1  Does any committed .py still use a "<repo>/..." literal as a path?
          A: yes, at least one remains          B: none remain
  CELL 2  Does every repaired site's _R("...") argument name a path that EXISTS
          in this checkout?
          A: at least one names nothing         B: every one resolves
  CELL 3  Does the _R resolver actually find the checkout root from each file's
          own depth (the files sit 3-6 levels down)?
          A: at least one fails to resolve      B: all resolve to this checkout

CONTROLS
  C1  The detector must FIRE on a planted dead literal (else it proves nothing).
  C2  The detector must NOT fire on a "<repo>/" string inside a docstring or used
      as a provenance label -- those are correct as text.
  C3  The resolver, run from the deepest patched file's directory, must return
      this checkout's root and not something above it.
"""
import ast, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKIP = {".git", "__pycache__", "legacy", ".venv", "venv", "node_modules", "audit", ".tmpwork"}
RES = re.compile(r'_R\((["\'])(.*?)\1\)')


def scan(text, label_lines=()):
    """Every STRING LITERAL (ast.Constant, so never a comment) whose value is "<repo>/" plus
    something -- i.e. a placeholder standing where a path must be -- excluding docstrings and
    the lines listed as deliberate provenance labels.  Returns [(lineno, source line)]."""
    tree = ast.parse(text)
    doc = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            if ast.get_docstring(node, clean=False) is not None:
                b = node.body[0]
                doc.update(range(b.lineno, (b.end_lineno or b.lineno) + 1))
    lines = text.splitlines()
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) \
           and node.value.startswith("<repo>/") and len(node.value) > len("<repo>/"):
            ln = node.lineno
            if ln in doc or ln in label_lines:
                continue
            hits.append((ln, lines[ln - 1].strip()))
    return sorted(set(hits))


def repo_root_from(start):
    d = os.path.dirname(os.path.abspath(start))
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, "frontier")):
        d = os.path.dirname(d)
    return d


# provenance labels and prose that are CORRECT as text (verified by reading them)
KEEP = {"frontier/B660_structure_campaign/packet/s2_cp/s2_cp.py": {7, 446},
        "frontier/B1113_tmeter/b1113_tmeter_verify.py": {868, 871},
        "tests/test_b1207_slow_lane.py": {111}}

print(__doc__)
print("=" * 78)
# print the checkout by NAME, not by absolute path: this output file is tracked, and
# the tracked-text half of the very guard this certificate serves forbids machine paths.
print("checkout:", ROOT.name, f"({len(ROOT.parts)} path components)")

# ---------------------------------------------------------------- controls
PLANT = 'B575 = "<repo>/frontier/B575_bridge_obstruction/l51_obstruction.py"\nopen(B575)\n'
c1 = len(scan(PLANT)) == 1
BENIGN = ('"""doc mentioning <repo>/frontier/X."""\n'
          'r = {"data_source": "<repo>/frontier/B637_corrected_cell3/unbent_table.txt"}\n')
c2 = len(scan(BENIGN, label_lines={2})) == 0
deep = ROOT / "frontier/B670_anatomy_full/packet/loop2/b1_f4/b1_f4.py"
c3 = deep.exists() and pathlib.Path(repo_root_from(str(deep))) == ROOT
for n, ok, what in ((1, c1, "detector fires on a planted dead literal"),
                    (2, c2, "detector silent on a docstring / provenance label"),
                    (3, c3, "resolver finds this checkout from the deepest patched file")):
    print(f"C{n}: {'PASS' if ok else 'FAIL'}  -- {what}")

# ---------------------------------------------------------------- cells
alive, unresolved, files_with_R = [], [], 0
for p in sorted(ROOT.rglob("*.py")):
    if any(part in SKIP for part in p.parts):
        continue
    rel = str(p.relative_to(ROOT))
    if p.resolve() == pathlib.Path(__file__).resolve():
        continue                       # this file quotes the pattern it hunts
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        continue
    if "<repo>/" in text:
        try:
            for ln, s in scan(text, KEEP.get(rel, ())):
                alive.append(f"{rel}:{ln}  {s[:90]}")
        except SyntaxError:
            alive.append(f"{rel}: UNPARSEABLE")
    if "_R(" in text and "_REPO" in text:
        files_with_R += 1
        base = repo_root_from(str(p))
        for m in RES.finditer(text):
            target = os.path.join(base, m.group(2))
            if not os.path.exists(target):
                unresolved.append(f"{rel}: _R({m.group(2)!r}) -> missing")
        if pathlib.Path(base) != ROOT:
            unresolved.append(f"{rel}: resolver returned {base}, not the checkout root")

print()
print(f"CELL 1  live '<repo>/' path literals remaining: {len(alive)}  -> "
      f"{'A (some remain)' if alive else 'B (none remain)'}")
for a in alive[:20]:
    print("   ", a)
print(f"CELL 2  files carrying the derived resolver: {files_with_R}; "
      f"_R() targets that do not exist: {len(unresolved)}  -> "
      f"{'A (some miss)' if unresolved else 'B (all resolve)'}")
for u in unresolved[:20]:
    print("   ", u)
print(f"CELL 3  resolver correct from every patched file: "
      f"{'B (yes)' if not any('resolver returned' in u for u in unresolved) else 'A (no)'}")

ok = c1 and c2 and c3 and not alive and not unresolved
print()
print("ALL CONTROLS PASSED" if (c1 and c2 and c3) else "CONTROL FAILURE")
print("VERDICT:", "CELL 1 = B, CELL 2 = B, CELL 3 = B -- no dead placeholder path remains"
      if ok else "OPEN -- see the listings above")
sys.exit(0 if ok else 1)
