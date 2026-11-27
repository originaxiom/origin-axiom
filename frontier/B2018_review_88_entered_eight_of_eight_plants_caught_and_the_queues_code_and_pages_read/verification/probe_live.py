"""Review 88 (B2018): main's own probes of the readers' serious findings on the LIVE queue code (origin-axiom at 64cc951b3).
Each probe builds a throwaway repository under a temp dir and prints HOLDS (the finding is real) or NOT (it is not)."""
import hashlib, importlib.util, os, pathlib, subprocess, sys, tempfile

LIVE = pathlib.Path(__file__).resolve().parents[3] / "scripts" / "queue"


def load(name):
    spec = importlib.util.spec_from_file_location("live_" + name, LIVE / (name + ".py"))
    m = importlib.util.module_from_spec(spec); sys.dont_write_bytecode = True; spec.loader.exec_module(m); return m


RR, RC, CU, QS, CF = load("rerun"), load("record_check"), load("custody"), load("queue_schema"), load("card_form")


def git(d, *a):
    return subprocess.run(["git", "-c", "user.name=p", "-c", "user.email=p@localhost", *a], cwd=d, capture_output=True,
                          text=True)


def card(script, out_lines, control, extra=""):
    n, h = RR.decisive(out_lines)
    return ("# CLAIM CARD — a probe\n\n- card id: new\n- seat code: fam2-v1-high-01\n"
            "- seat, branch, commit: fam2-v1-high-01, seat/p, %s\n- kind: computation\n- touches: P-885\n"
            "- effect: supports — P-885\n- scope: frame: none; object: x; reach: single; hypotheses: none\n"
            "- identifications: none\n- definitions: none\n- imports: none\n- premises on main: none\n"
            "- decisive script: %s, SHA-256 %s, depends on the standard library, run as python3 %s, output SHA-256 "
            "0000000000000000\n- decisive lines: %d lines marked \"DECISIVE:\", SHA-256 %s\n- failing control: %s\n"
            "- second computation: none\n- already on main?: topic_sweep ran, nothing close\n- what would make it fail: the control\n%s"
            % ("0" * 40, script, "0" * 16, script, n, h, control, extra))


def repo(files, links=None, attrs=None):
    d = pathlib.Path(tempfile.mkdtemp(prefix="r88probe_"))
    git(d, "init", "-q")
    for k, v in files.items():
        (d / k).parent.mkdir(parents=True, exist_ok=True); (d / k).write_text(v)
    for k, target in (links or {}).items():
        os.symlink(target, d / k)
    if attrs:
        (d / ".gitattributes").write_text(attrs)
    git(d, "add", "-A"); git(d, "commit", "-qm", "c")
    return d, git(d, "rev-parse", "HEAD").stdout.strip()


def say(name, holds, detail):
    print("%-44s %s  %s" % (name, "HOLDS" if holds else "NOT  ", detail))


STATIC = []   # the static guard only: no namespace (as on this machine)

# B8 / C5: the control's imports are never guarded
d, c = repo({"x.py": "print('DECISIVE: v = 1')\n", "c.py": "import socket\nraise SystemExit(1)\n"})
r = RR.rerun(str(d), c, card("x.py", "DECISIVE: v = 1\n", "python3 c.py"), limit=60, prefix=STATIC)
say("B8 the control's imports are not guarded", r["status"] == "REPRODUCED", r["status"])

# B4 / C4: a slow control turns a failed card into HEAVY
d, c = repo({"x.py": "print('DECISIVE: v = 2')\n", "c.py": "import time\ntime.sleep(30)\nraise SystemExit(1)\n"})
r = RR.rerun(str(d), c, card("x.py", "DECISIVE: v = 1\n", "python3 c.py"), limit=5, prefix=STATIC)
say("B4 a slow control masks a failed rerun", r["status"] == "HEAVY", "%s %s" % (r["status"], r["reasons"][:1]))

# B5: a symlinked decisive script runs a file outside the commit
outside = pathlib.Path(tempfile.mkdtemp(prefix="r88out_")) / "evil.py"
outside.write_text("print('DECISIVE: v = 9')\n")
d, c = repo({"c.py": "raise SystemExit(1)\n"}, links={"x.py": str(outside)})
r = RR.rerun(str(d), c, card("x.py", "DECISIVE: v = 9\n", "python3 c.py"), limit=60, prefix=STATIC)
say("B5 a symlinked script runs outside the commit", r["status"] == "REPRODUCED", r["status"])

# B6: git archive's export-subst changes the text that runs
d, c = repo({"x.py": "s = '$Format:%H$'\nprint('DECISIVE: v =', 1 if s.startswith('$') else 2)\n",
             "c.py": "raise SystemExit(1)\n"}, attrs="x.py export-subst\n")
here = subprocess.run([sys.executable, "x.py"], cwd=d, capture_output=True, text=True).stdout
r = RR.rerun(str(d), c, card("x.py", "DECISIVE: v = 2\n", "python3 c.py"), limit=60, prefix=STATIC)
say("B6 export-subst: the run is not the blob", r["status"] == "REPRODUCED" and "v = 1" in here,
    "checkout prints %r, rerun %s" % (here.strip(), r["status"]))

# B7: the static guard lets _socket and exec('import socket') through
for name, src in (("_socket", "import _socket\n"), ("exec", "exec('import socket')\n")):
    d, c = repo({"x.py": src + "print('DECISIVE: v = 1')\n", "c.py": "raise SystemExit(1)\n"})
    r = RR.rerun(str(d), c, card("x.py", "DECISIVE: v = 1\n", "python3 c.py"), limit=60, prefix=STATIC)
    say("B7 the static guard admits " + name, r["status"] == "REPRODUCED", r["status"])

# B15 / C6: a sage import returns HEAVY before the command and control checks
d, c = repo({"x.py": "try:\n    import sage.all\nexcept ImportError:\n    pass\nprint('DECISIVE: v = 1')\n"})
t = card("x.py", "DECISIVE: v = 1\n", "true").replace("run as python3 x.py", "run as python3 x.py; rm -rf y")
r = RR.rerun(str(d), c, t, limit=60, prefix=STATIC)
say("B15 HEAVY before the command and control checks", r["status"] == "HEAVY", "%s %s" % (r["status"], r["reasons"]))

# B10 / A14: effect's code is not one it touches, and the card is then not deciding
t = card("x.py", "DECISIVE: v = 1\n", "python3 c.py").replace("- touches: P-885", "- touches: B2011").replace(
    "supports — P-885", "removes — A03")
say("B10 effect names a code it does not touch", CF.form_problems(t) == [] and RC.deciding(CF.read(t)[1]) is False,
    "form %s, deciding %s" % (CF.form_problems(t), RC.deciding(CF.read(t)[1])))

# B11: the 19 by their common plural names
f = CF.read(card("x.py", "DECISIVE: v = 1\n", "python3 c.py").replace("- touches: P-885", "- touches: the quark Yukawas"))[1]
say("B11 'the quark Yukawas' is not deciding", RC.deciding(f) is False, str(RC.deciding(f)))

# B3 on live: the firewall misses plurals and 'compared to data'
for w in ("the measured values", "compared to data", "1.2 +/- 0.1"):
    say("B3 the firewall misses %r" % w, RC.firewall("we checked %s here" % w) == [], str(RC.firewall(w)))

# A15: a card on a seat's branch may carry main's code
print("%-44s %s  %s" % ("A15 seat code not tied to the branch", "HOLDS", "read in discover.discover: seat_code = the card's own field"))

# A6 / C12: main moves main's own card by the alias 'main'
h = [{"at": "2026-11-27T10:00:00Z", "status": "FILED", "by": "runner", "note": ""},
     {"at": "2026-11-27T10:01:00Z", "status": "REPRODUCED", "by": "runner", "note": ""},
     {"at": "2026-11-27T10:02:00Z", "status": "OFFERED", "by": "runner", "note": ""},
     {"at": "2026-11-27T10:03:00Z", "status": "PEERED", "by": "main", "note": ""}]
say("A6 main peers its own card as 'main'", QS.history_problems(h, "PEERED", QS.MAIN_CODE) == [],
    str(QS.history_problems(h, "PEERED", QS.MAIN_CODE)))

# A7: REPRODUCED -> AT_BANKING skips the offer
say("A7 REPRODUCED -> AT_BANKING is a move", "AT_BANKING" in QS.MOVES["REPRODUCED"], str(QS.MOVES["REPRODUCED"]))

# A11: deciding = 0 passes as a value
rec = {"id": "Q0001", "seat_code": "fam2-v1-high-01", "branch": "seat/p", "commit": "a" * 40,
       "card_path": "relays/claims/CLAIM_x.md", "title": "t", "status": "OFFERED", "deciding": 0, "heavy": False,
       "refiles": [], "history": h[:3]}
say("A11 deciding = 0 is accepted", QS.card_problems(rec, "Q0001") == [], str(QS.card_problems(rec, "Q0001")))

# B12: a card file deleted along the queue's history is not reported
d = pathlib.Path(tempfile.mkdtemp(prefix="r88q_")); git(d, "init", "-q")
(d / "queue/cards").mkdir(parents=True)
good = dict(rec, deciding=False, status="OFFERED")
(d / "queue/cards/Q0001.json").write_text(__import__("json").dumps(good)); git(d, "add", "-A"); git(d, "commit", "-qm", "1")
(d / "queue/cards/Q0001.json").unlink(); git(d, "add", "-A"); git(d, "commit", "-qm", "2")
p = CU.history_problems(str(d), "HEAD")
say("B12 a deleted card is not reported", p == [], str(p[:2]))
