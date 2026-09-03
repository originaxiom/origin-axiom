#!/usr/bin/env python3
"""B1245 -- the discriminating fact for C43's group-independence, computed from B915's own code.
Claim: the desert curve has NO group parameter, so the 16-sigma miss cannot depend on which
simple group unifies. Prints REPRODUCES. No measured value is introduced (B915's seal covers them)."""
import ast, os, re, sys
R = os.environ.get("OA_ROOT") or os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..",".."))
src_path = os.path.join(R, "frontier/B915_the_crossing/crossing.py")
src = open(src_path, encoding="utf-8").read()
ok = True
def chk(label, got, want):
    global ok
    good = got == want; ok &= good
    print(f"  {'OK ' if good else 'DIFF'}  {label}: {got}" + ("" if good else f"  (expected {want})"))

tree = ast.parse(src)
fn = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "curve_point")
args = [a.arg for a in fn.args.args]
chk("curve_point's arguments", args, ["MU", "two_loop"])
chk("exactly one PHYSICAL argument (the unification scale)", [a for a in args if a != "two_loop"], ["MU"])

# strip docstrings and comments; then look for any group-specific token in EXECUTABLE code
code_lines = []
for ln in src.split("\n"):
    s = ln.split("#")[0]
    code_lines.append(s)
code = "\n".join(code_lines)
for node in ast.walk(tree):                      # remove docstrings
    if isinstance(node, (ast.Module, ast.FunctionDef, ast.ClassDef)):
        d = ast.get_docstring(node)
        if d: code = code.replace(d, "")
GROUP = ["E6", "E_6", "SO(10)", "so10", "SU(5)", "su5", "E8", "F4", "rank", "Casimir", "dynkin", "adjoint"]
found = sorted({g for g in GROUP if re.search(rf"(?<![\w]){re.escape(g)}(?![\w])", code)})
chk("group-specific tokens in executable code", found, [])
chk("SM one-loop betas present", bool(re.search(r"41/10", code)) and bool(re.search(r"-19/6", code)), True)
chk("GUT normalisation 5/3 present (shared by SU(5) < SO(10) < E6)", "5.0/3.0" in code or "5/3" in code, True)

print("\n  => the desert curve is a function of (SM betas, the 5/3 normalisation, one meeting scale).")
print("     There is NO group parameter to vary, so the 16-sigma miss is group-independent BY")
print("     CONSTRUCTION -- not by running SU(5) and SO(10) and finding the same answer.")
print("REPRODUCES" if ok else "DIFF")
sys.exit(0 if ok else 1)
