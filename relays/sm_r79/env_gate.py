"""SM-R79 (M4): does the environment move what a debt gate reads?  Main's _debt_checker runs a checker as
subprocess.run([python, checker, *args, "--today", DAY]) with no env= argument, so the checker inherits the caller's
environment.  This runs point_debt.py exactly that way at main's head, twice: as it is, and with OA_POINT_REGISTER pointing
at a copy of the register in which one row's disposition is a word the rule refuses.  Usage (from a checkout of main):
env_gate.py OUT.json"""
import json, os, pathlib, subprocess, sys, tempfile
day = subprocess.run(["git", "log", "-1", "--format=%cs", "HEAD"], capture_output=True, text=True).stdout.strip()
run = lambda env: subprocess.run([sys.executable, "scripts/checks/point_debt.py", "--today", day], capture_output=True, text=True, env=env)
base = {k: v for k, v in os.environ.items() if k != "OA_POINT_REGISTER"}
a = run(base)
lines = pathlib.Path("docs/POINT_REGISTER.md").read_text(encoding="utf-8").split("\n")
i = next(k for k, l in enumerate(lines) if l.startswith("| P-002 |"))
cells = lines[i].split("|"); cells[5] = " NOT-A-DISPOSITION "; lines[i] = "|".join(cells)
p = pathlib.Path(tempfile.mkdtemp()) / "REGISTER.md"; p.write_text("\n".join(lines), encoding="utf-8")
b = run(dict(base, OA_POINT_REGISTER=str(p)))
res = {"day": day,
       "as_is": {"exit": a.returncode, "tail": (a.stdout + a.stderr).strip().splitlines()[-1:]},
       "with_OA_POINT_REGISTER_at_a_broken_copy": {"exit": b.returncode, "tail": [l for l in (b.stdout + b.stderr).splitlines() if "P-002" in l][:1]}}
res["the_checker_follows_the_environment"] = a.returncode != b.returncode
pathlib.Path(sys.argv[1]).write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, indent=1))
