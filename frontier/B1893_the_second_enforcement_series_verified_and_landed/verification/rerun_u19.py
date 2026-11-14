"""U19.a and U19.b of main's unseen cases for series 2, run again with the planted commits made under the repository's own author,
so that the attribution gate can fail only for what was planted.  A control first: an empty commit under that author must leave every gate as it was."""
import json, pathlib, subprocess, sys
T = pathlib.Path(__file__).resolve().parent
src = (T / "run_unseen_s2.py").read_text(encoding="utf-8")
ns = {"__file__": str(T / "run_unseen_s2.py")}
exec(compile(src.split("\nCASES = ")[0], "run_unseen_s2_head", "exec"), ns)
W, HEAD, gates, reset = ns["W"], ns["HEAD"], ns["gates"], ns["reset"]
def git(*a):
    return subprocess.run(["git", "-C", str(W), "-c", "user.name=originaxiom", "-c", "user.email=originaxiom@users.noreply.github.com", *a], capture_output=True, text=True)
reset()
base = gates(); base_fail = sorted(k for k, v in base.items() if v[0] == "FAIL")
print("head", HEAD[:9], "| gates", len(base), "| failing before any plant:", base_fail, flush=True)
OUT = {"head": HEAD, "failing before any plant": base_fail}
c = git("commit", "-q", "--allow-empty", "-m", "control: an empty commit under the repository's author")
res = gates(); new = sorted(k for k, v in res.items() if v[0] == "FAIL" and k not in base_fail)
OUT["control"] = {"committed": c.returncode == 0, "gates newly failing": new}
print("control committed=%s newly failing: %s" % (c.returncode == 0, new), flush=True)
for name in ("U19.a", "U19.b"):
    reset()
    note = ns["u19a" if name.endswith("a") else "u19b"]() or ""
    git("add", "-A"); c = git("commit", "-q", "-m", "planted case " + name)
    # ADDED 2026-11-12 (Review 80; owed by main's word in its third folder for the builder, section 6, item 4).  A PLANT THAT
    # CHANGES NOTHING STOPS THE RUN.  A case is committed in the scratch checkout.  Where the case had changed nothing there was
    # nothing to commit: the gates were then run on the tree as it stood, and the case was written down with "committed": false
    # and "not caught".  No case of the kept output is so; the run now ends there, with a sentence.
    if c.returncode != 0:
        reset()
        raise SystemExit("STOPPED at %s: the planted case changed nothing in the checkout, and no commit was made. Gates that pass on it show nothing: mend the case" % name)
    res = gates(); new = sorted(k for k, v in res.items() if v[0] == "FAIL" and k not in base_fail)
    OUT[name] = {"note": note, "committed": c.returncode == 0, "gates newly failing": {k: res[k][1][:400] for k in new}, "attribution": list(res.get("attribution", ("?", "?"))), "CAUGHT": "attribution" in new}
    print("%-6s committed=%s caught=%s newly failing: %s | attribution: %s %s" % (name, c.returncode == 0, "attribution" in new, new, res.get("attribution", ("?",))[0], res.get("attribution", ("", ""))[1][:300]), flush=True)
reset()
(T / "unseen_s2_u19.json").write_text(json.dumps(OUT, indent=1, ensure_ascii=False))
print("written", flush=True)
