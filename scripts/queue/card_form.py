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
import shlex
import sys

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("queue_schema_for_the_form", HERE / "queue_schema.py")
QS = importlib.util.module_from_spec(_spec)
sys.dont_write_bytecode = True
_spec.loader.exec_module(QS)

TITLE = re.compile(r"# CLAIM CARD — (\S.*)")
# CHANGED 2026-11-26 (T1b, main's M56): `scope` and `identifications` added, so door rule D1 is checked; `touches` may be
# none (such a card decides nothing and goes to the peers only), and then `effect` may be none too.
# 2026-11-26 (main's M60): `definitions` added: the definitions of the objects the claim uses, in words or formulas, so
# that a banking seat can check the claim from the card alone (the first banking seat could not, for want of them)
FIELDS = ("card id", "seat code", "seat, branch, commit", "kind", "touches", "effect", "scope", "identifications",
          "definitions", "imports", "premises on main", "decisive script", "decisive lines", "failing control",
          "second computation", "already on main?", "what would make it fail")
MAY_BE_NONE = ("touches", "identifications", "definitions", "imports", "premises on main", "second computation")
SCOPE_PARTS = ("frame", "object", "reach", "hypotheses")
REACH = ("single", "class", "general")
KINDS = ("theorem", "computation", "prediction", "identification", "negative")
EFFECTS = ("removes", "conditions", "adds", "supports", "refutes")
# the packages a decisive script may depend on: the card's list, and python-flint, sage and GAP (main's change, § 9);
# their pinned versions are the rerun's (T5)
# T7b (Review 88's A3): read from ALLOWED_PACKAGES.json, the rerun's own list, so that the two cannot drift apart
_PINS = __import__("json").loads((HERE / "ALLOWED_PACKAGES.json").read_text(encoding="utf-8"))
ALLOWED = ("the standard library",) + tuple(_PINS["packages"]) + tuple(_PINS["heavy"])
# what a card can touch, read the same way by the form and by the record check (T7b; Review 88's B10, B11, B18, A14 and
# main's M61): the scoreboard's codes in any case, identification rows, register rows, the law map's rows (named in
# capitals with their number, "LISTENING 26"), and the 19 by name, plural and common names among them
SCOREBOARD = re.compile(r"\b(A0[1-9]|A1[0-2]|F[1-4]|S0[1-3]|LAMBDA)\b", re.I)
IDENT = re.compile(r"\bI-\d+\b")
ROW = re.compile(r"\bP-\d+\b")
LAW_ROW = re.compile(r"\b[A-Z][A-Z-]{3,} \d{1,4}\b")
NINETEEN = re.compile(r"\b(masse?s?|mixings?|CKM|PMNS|thetas?|couplings?|Higgs|(weak|Weinberg|mixing|Cabibbo) angles?|"
                      r"Yukawas?|lepton factors?|CP phases?|fine[- ]structure|strong coupling)\b", re.I)


def codes(text):
    """the codes a text names, as one set of normalised names"""
    out = {c.upper() for c in SCOREBOARD.findall(text)} | set(IDENT.findall(text)) | set(ROW.findall(text)) \
        | set(LAW_ROW.findall(text))
    out |= {"the 19: " + _singular(m.group(0)) for m in NINETEEN.finditer(text)}
    return out


def _singular(name):
    w = " ".join(name.lower().split())
    if w.endswith("masses"):
        return w[:-2]
    if w.endswith("s") and not w.endswith(("higgs", "mass")):
        return w[:-1]
    return w


FIELD_LINE = re.compile(r"- ([a-z ,?]+):(.*)$")
CARD_ID = re.compile(r"new|refiles (Q\d{4,})")
HEX16 = re.compile(r"SHA-256 ([0-9a-f]{16})\b")
DECISIVE = re.compile(r"(\d+) lines? marked \"DECISIVE:\", SHA-256 ([0-9a-f]{16})")
# a card may declare its script heavy (main's M58): ", heavy" after the output's hash. It only adds work: the checks stand
SCRIPT = re.compile(r"(\S+\.(?:py|sage|g|gap)), SHA-256 [0-9a-f]{16}, depends on (.+?), run as (.+?), output SHA-256 "
                    r"[0-9a-f]{16}(, heavy)?\s*$")


def _argv(cmd):
    try:
        return shlex.split(cmd)
    except ValueError:
        return None


def declared_heavy(fields):
    m = SCRIPT.match(fields.get("decisive script", ""))
    return bool(m and m.group(4))


def scope_problems(scope):
    """the scope: 'frame: ...; object: ...; reach: single | class | general; hypotheses: ...', each part filled"""
    parts = [p.strip() for p in scope.split(";", 3)]            # the hypotheses may themselves hold ";" (A21)
    keys = [p.split(":", 1)[0].strip() for p in parts]
    if tuple(keys) != SCOPE_PARTS or any(":" not in p or not p.split(":", 1)[1].strip() for p in parts):
        return ["scope is not 'frame: <...>; object: <...>; reach: <single, class or general>; hypotheses: <...>'"]
    reach = parts[2].split(":", 1)[1].strip()
    return [] if reach in REACH else ["scope's reach %r is not one of %s" % (reach, ", ".join(REACH))]


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
        elif line.strip():                                # A21: a line outside any field is said, not dropped
            bad.append("a line stands outside any field: %r" % line.strip()[:80])
        else:
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
        elif f[name].lower() == "none" and name not in MAY_BE_NONE and not (name == "effect"
                                                                            and f.get("touches", "").lower() == "none"):
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
    if f["effect"].lower() == "none":
        pass                                             # allowed only when touches is none (the check above)
    elif f["touches"].lower() == "none":
        bad.append("the card touches none, so its effect is not none: an effect names a code it touches")
    elif f["effect"].split(" ")[0] not in EFFECTS or " — " not in f["effect"]:
        bad.append("effect does not open with one of %s and name its code after ' — '" % ", ".join(EFFECTS))
    else:                                                 # A14, B10: the effect's codes are codes the card touches
        outside = sorted(codes(f["effect"].split(" — ", 1)[1]) - codes(f["touches"]))
        if outside:
            bad.append("the effect names what the card does not touch: %s" % ", ".join(outside))
    bad += scope_problems(f["scope"])
    m = SCRIPT.match(f["decisive script"])
    if not m:
        bad.append("decisive script is not '<path>, SHA-256 <16 hex>, depends on <...>, run as <command>, output "
                   "SHA-256 <16 hex>'")
    else:
        path = m.group(1)
        if path.startswith("/") or ".." in path.split("/"):
            bad.append("the decisive script's path %r leaves the commit" % path)
        run = _argv(m.group(3))
        if not run or len(run) < 2 or run[1] != path:
            bad.append("'run as' does not run the declared script %s" % path)
        deps = [d.strip() for d in re.split(r",| and ", m.group(2)) if d.strip()]
        outside = [d for d in deps if d not in ALLOWED]
        if outside:
            bad.append("decisive script depends on what is not allowed: %s" % ", ".join(outside))
    d = DECISIVE.fullmatch(f["decisive lines"])
    if not d or int(d.group(1)) < 1:
        bad.append("decisive lines is not '<n> lines marked \"DECISIVE:\", SHA-256 <16 hex>' with n of one or more")
    control = f["failing control"]
    if m and _argv(control) and _argv(control) == _argv(m.group(3)):       # A12: compared as commands, not as strings
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
