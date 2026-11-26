#!/usr/bin/env python3
"""The claim card's form check (the framework's thin path, patch T2; draft 1 § 9, main's M54; register row P-885).

The intake's first check on a card: the form of docs/CLAIM_CARD.md, read as the card's author wrote it. A field may run
over several lines; a line that does not open a field continues the one above. Every field is there and filled; a
field that does not apply says "none", and only the fields in MAY_BE_NONE may. Four fields are new with the framework
(§ 9): the card's id, the seat's code, the failing control as a command, and the decisive output lines.

What the form check does not do: it runs nothing and reads nothing of the record. Custody (T4), the rerun and the
failing control (T5) and the record check (T6) are the intake's later steps.

    python3 scripts/queue/card_form.py CARD.md [CARD.md ...]
Exit 0 when every card's form holds, 1 when one does not."""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("queue_schema_for_the_form", HERE / "queue_schema.py")
QS = importlib.util.module_from_spec(_spec)
sys.dont_write_bytecode = True
_spec.loader.exec_module(QS)

TITLE = re.compile(r"# CLAIM CARD — (\S.*)")
FIELDS = ("card id", "seat code", "seat, branch, commit", "kind", "touches", "effect", "imports", "premises on main",
          "decisive script", "decisive lines", "failing control", "second computation", "already on main?",
          "what would make it fail")
MAY_BE_NONE = ("imports", "premises on main", "second computation")
KINDS = ("theorem", "computation", "prediction", "identification", "negative")
EFFECTS = ("removes", "conditions", "adds", "supports", "refutes")
# the packages a decisive script may depend on: the card's list, and python-flint, sage and GAP (main's change, § 9);
# their pinned versions are the rerun's (T5)
ALLOWED = ("the standard library", "mpmath", "sympy", "numpy", "scipy", "python-flint", "sage", "GAP")
FIELD_LINE = re.compile(r"- ([a-z ,?]+):(.*)$")
CARD_ID = re.compile(r"new|refiles (Q\d{4,})")
HEX16 = re.compile(r"SHA-256 ([0-9a-f]{16})\b")
DECISIVE = re.compile(r"(\d+) lines? marked \"DECISIVE:\", SHA-256 ([0-9a-f]{16})")
SCRIPT = re.compile(r"(\S+\.(?:py|sage|g|gap)), SHA-256 [0-9a-f]{16}, depends on (.+?), run as (.+?), output SHA-256 "
                    r"[0-9a-f]{16}\s*$")


def read(text):
    """(title, {field: value}, [problems of layout]) from a card's text; the card's block may stand in a fenced block"""
    lines = [l for l in text.splitlines() if l.strip() != "```"]
    bad = []
    if not lines or not TITLE.fullmatch(lines[0].strip()):
        return None, {}, ["the first line is not '# CLAIM CARD — <the result in one line>'"]
    title = TITLE.fullmatch(lines[0].strip()).group(1).strip()
    fields, current = {}, None
    for line in lines[1:]:
        m = FIELD_LINE.match(line)
        if m and m.group(1).strip() in FIELDS:
            current = m.group(1).strip()
            if current in fields:
                bad.append("the field '%s' stands twice" % current)
            fields[current] = m.group(2).strip()
        elif m:
            bad.append("'%s' is not a field of the card" % m.group(1).strip())
            current = None
        elif line.strip() and current:
            fields[current] = (fields[current] + " " + line.strip()).strip()
        elif not line.strip():
            current = None
    return title, fields, bad


def form_problems(text):
    """every way a card's form fails; [] when it holds"""
    title, f, bad = read(text)
    if title is None:
        return bad
    for name in FIELDS:
        if name not in f:
            bad.append("the field '%s' is missing" % name)
        elif not f[name]:
            bad.append("the field '%s' is empty" % name)
        elif f[name].lower() == "none" and name not in MAY_BE_NONE:
            bad.append("the field '%s' may not be none" % name)
    if bad:
        return bad
    if not CARD_ID.fullmatch(f["card id"]):
        bad.append("card id is not 'new' or 'refiles Q<nnnn>'")
    bad += ["seat code: %s" % p for p in QS.code_problems(f["seat code"], "the code")]
    parts = [p.strip() for p in f["seat, branch, commit"].split(",")]
    if len(parts) != 3 or not QS.COMMIT.fullmatch(parts[2]) or not QS.BRANCH.fullmatch(parts[1]):
        bad.append("'seat, branch, commit' is not three parts with a branch and a full 40-hex commit")
    elif parts[0] != f["seat code"]:
        bad.append("the seat in 'seat, branch, commit' is not the card's seat code")
    if f["kind"] not in KINDS:
        bad.append("kind is not one of %s" % ", ".join(KINDS))
    if f["effect"].split(" ")[0] not in EFFECTS or " — " not in f["effect"]:
        bad.append("effect does not open with one of %s and name its code after ' — '" % ", ".join(EFFECTS))
    m = SCRIPT.match(f["decisive script"])
    if not m:
        bad.append("decisive script is not '<path>, SHA-256 <16 hex>, depends on <...>, run as <command>, output "
                   "SHA-256 <16 hex>'")
    else:
        deps = [d.strip() for d in re.split(r",| and ", m.group(2)) if d.strip()]
        outside = [d for d in deps if d not in ALLOWED]
        if outside:
            bad.append("decisive script depends on what is not allowed: %s" % ", ".join(outside))
    d = DECISIVE.fullmatch(f["decisive lines"])
    if not d or int(d.group(1)) < 1:
        bad.append("decisive lines is not '<n> lines marked \"DECISIVE:\", SHA-256 <16 hex>' with n of one or more")
    control = f["failing control"]
    if m and control == m.group(3).strip():
        bad.append("the failing control is the decisive command itself")
    if len(control.split()) < 2:
        bad.append("the failing control is not a command")
    return bad


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    n_bad = 0
    for path in argv:
        bad = form_problems(pathlib.Path(path).read_text(encoding="utf-8"))
        n_bad += bool(bad)
        print("%s: %s" % (path, "the form holds" if not bad else "; ".join(bad)))
    return 1 if n_bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
