#!/usr/bin/env python3
"""The peer note: its schema, the runner's check of it, and its grade (the framework's thin path, patch T8; draft 1
§§ 2.3 and 9; main's M54; register row P-885).

A peer offered a card (by hand in the trial; by rotation after it) files one note on its own branch, at
`relays/claims/peer/PEER_<card id>.json`:

    card          the card's id, Q<nnnn>
    card_commit   the full commit of the card the peer read
    peer_code     the peer's seat code (never a name); not the card's own seat
    finding       reproduced | fault | extended
    script        {path, sha256 (16 hex), run_as, control}: the peer's own script, at the commit the note is filed at, and
                  its failing control, which must fail as a card's does (T1b: exit 1, no traceback)
    decisive      {lines, sha256}: the peer's decisive lines, normalised as the rerun normalises them
    note          what the peer found, in a few lines

THE RUNNER'S CHECK. The note is read at the commit that last changed it, on the peer's branch.
  - Its form, and a peer that is not the card's own seat. The peer's lane is not checked yet: the lanes come with § 8's
    identity table, after the trial.
  - The note's commit was first sighted after the card was offered: a note written before the offer is refused.
  - The peer's script is rerun at the note's commit, in T7b's sandbox (its own namespaces, as nobody), with its own failing control.
  - "reproduced" holds only if the peer's decisive lines are the card's, count and hash.

THE GRADE. "re-derived" when the peer's script shares no file with the producer's: the script and every module beside
it that it imports, compared by their content; and when it does not reach for the producer's computation another way:
none of those files names the producer's decisive script, its folder or a file in it, and no file beside the peer's
script is a renamed copy of one of the producer's (`producer_reach`, main's M71 point 1). Otherwise "reran". Only a re-derived note moves a card up the banking
queue (§ 9).

WHAT THE RUNNER CANNOT DO, said plainly. The note sits on a public branch, so the banking seats could read it before they
seal their verdicts. Blindness to the peer note is a rule of the banking seat's charter, measured by plants (a planted
"reproduced" note on a faulty card), not something this check enforces.

    python3 scripts/queue/peer_note.py NOTE.json --record queue/cards/Q0001.json [--root REPO]
Prints the check as JSON; exit 0 when the note holds, 1 when it does not."""
import hashlib
import importlib.util
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


QS = _load("queue_schema_for_peer", HERE / "queue_schema.py")
CF = _load("card_form_for_peer", HERE / "card_form.py")
CU = _load("custody_for_peer", HERE / "custody.py")
RR = _load("rerun_for_peer", HERE / "rerun.py")
PEER_DIR = "relays/claims/peer/"
FIELDS = ("card", "card_commit", "peer_code", "finding", "script", "decisive", "note")
FINDINGS = ("reproduced", "fault", "extended")
HEX16 = re.compile(r"[0-9a-f]{16}")


def note_path(cid):
    return "%sPEER_%s.json" % (PEER_DIR, cid)


def form_problems(note, rec=None):
    if not isinstance(note, dict):
        return ["the note is not a table"]
    missing = [f for f in FIELDS if f not in note]
    extra = sorted(set(note) - set(FIELDS))
    bad = (["fields missing: %s" % ", ".join(missing)] if missing else []) + \
          (["fields not in the schema: %s" % ", ".join(extra)] if extra else [])
    if missing:
        return bad
    if not isinstance(note["card"], str) or not QS.ID.fullmatch(note["card"]):
        bad.append("card %r is not a card's id" % (note["card"],))
    if not isinstance(note["card_commit"], str) or not QS.COMMIT.fullmatch(note["card_commit"]):
        bad.append("card_commit is not a full 40-hex commit")
    bad += QS.code_problems(note["peer_code"], "peer_code")
    if note["finding"] not in FINDINGS:
        bad.append("finding %r is not one of %s" % (note["finding"], ", ".join(FINDINGS)))
    s = note["script"]
    if not isinstance(s, dict) or sorted(s) != ["control", "path", "run_as", "sha256"] \
            or not isinstance(s.get("sha256"), str) or not HEX16.fullmatch(s["sha256"]):
        bad.append("script is not {path, sha256 (16 hex), run_as, control}")
    d = note["decisive"]
    if not isinstance(d, dict) or sorted(d) != ["lines", "sha256"] or not isinstance(d.get("lines"), int) \
            or d["lines"] < 1 or not isinstance(d.get("sha256"), str) or not HEX16.fullmatch(d["sha256"]):
        bad.append("decisive is not {lines (one or more), sha256 (16 hex)}")
    if not isinstance(note["note"], str) or not note["note"].strip() or len(note["note"]) > 2000:
        bad.append("note is not 1 to 2000 characters of text")
    if rec is not None and not bad:
        if note["card"] != rec["id"]:
            bad.append("the note is for %s, not %s" % (note["card"], rec["id"]))
        if note["card_commit"] != rec["commit"]:
            bad.append("the note read the card at %s, not at its sealed commit" % note["card_commit"][:9])
        if note["peer_code"] == rec["seat_code"]:
            bad.append("the peer is the card's own seat")
    return bad


def _files(root, commit, path):
    """the content hashes of the script and of every module beside it that it imports, at a commit, written from their
    blobs as the rerun writes them (T7b: not `git archive`, which a commit's .gitattributes can bend)"""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="peer_"))
    try:
        modes = RR.materialise(root, commit, tmp)
        if modes is None or not (tmp / path).is_file():
            return set()
        seen = set()
        if path.endswith(".py"):
            RR.imports_of(tmp / path, tmp, seen, modes)
        else:
            seen = {tmp / path}
        return {hashlib.sha256(f.read_bytes()).hexdigest() for f in seen if f.is_file()}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def producer_reach(root, producer_commit, producer_script, commit, script):
    """M71 point 1: how a script at `commit` could rerun the producer's computation rather than recompute it, though it
    imports none of the producer's files: the reasons, [] when none is seen.
      - its text, or the text of a module beside it that it imports, names the producer's decisive script (its path or its
        name), the producer's folder, or the path of a file in that folder (the producer's committed output);
      - a file in its own folder has the content of a file in the producer's folder (a copy of the output, renamed).
    It sees only what is written plainly: a path built at run time, or fetched, passes. The auditor's sample covers what
    this cannot see."""
    a = pathlib.Path(tempfile.mkdtemp(prefix="reach_p_"))
    b = pathlib.Path(tempfile.mkdtemp(prefix="reach_s_"))
    try:
        pm, sm = RR.materialise(root, producer_commit, a), RR.materialise(root, commit, b)
        if pm is None or sm is None or not (b / script).is_file():
            return ["the scripts cannot be read at their commits"]
        folder = pathlib.PurePosixPath(producer_script).parent.as_posix()
        folder = "" if folder == "." else folder
        theirs = [p for p in pm if (pathlib.PurePosixPath(p).parent.as_posix() if "/" in p else "") == folder]
        names = {producer_script, pathlib.PurePosixPath(producer_script).name} | set(theirs) | ({folder} if folder else set())
        seen = set()
        if script.endswith(".py"):
            RR.imports_of(b / script, b, seen, sm)
        seen.add(b / script)
        bad = []
        for f in sorted(seen):
            try:
                text = f.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            hit = sorted(n for n in names if n and re.search(r"(?<![\w./-])%s(?![\w-])" % re.escape(n), text))
            if hit:
                bad.append("%s names the producer's %s" % (f.relative_to(b), ", ".join(hit)))
        mine = pathlib.PurePosixPath(script).parent.as_posix()
        mine = "" if mine == "." else mine
        hashes = {hashlib.sha256((a / p).read_bytes()).hexdigest(): p for p in theirs if (a / p).is_file()}
        for p in sorted(sm):
            if (pathlib.PurePosixPath(p).parent.as_posix() if "/" in p else "") == mine and (b / p).is_file():
                h = hashlib.sha256((b / p).read_bytes()).hexdigest()
                if h in hashes and hashes[h] != p:     # the same file at the same path is shared, not copied, and
                    bad.append("%s is the producer's %s, copied" % (p, hashes[h]))      # reading it names its path
        return bad
    finally:
        shutil.rmtree(a, ignore_errors=True)
        shutil.rmtree(b, ignore_errors=True)


def _as_card(note):
    """the note's run, written as a card the rerun reads"""
    s, d = note["script"], note["decisive"]
    return ("# CLAIM CARD — the peer's run\n\n"
            "- decisive script: %s, SHA-256 %s, depends on the standard library, run as %s, output SHA-256 %s\n"
            "- decisive lines: %d lines marked \"DECISIVE:\", SHA-256 %s\n- failing control: %s\n"
            % (s["path"], s["sha256"], s["run_as"], "0" * 16, d["lines"], d["sha256"], s["control"]))


def check(root, note, note_commit, peer_branch, rec, card_text, entries, limit=RR.TIME_LIMIT, prefix=None,
          allow_static=False):
    """{ok, grade, reasons, rerun, other_family}: the runner's check of one note"""
    out = {"ok": False, "grade": None, "reasons": form_problems(note, rec), "rerun": None, "other_family": None}
    if out["reasons"]:
        return out
    offered = [e["at"] for e in rec["history"] if e["status"] == "OFFERED"]
    if not offered:
        out["reasons"].append("the card was never offered")
        return out
    rc = subprocess.run(["git", "rev-parse", "%s:%s" % (note_commit, note_path(rec["id"]))], cwd=root,
                        capture_output=True, text=True)
    seen = CU.first_sighting(entries, peer_branch, note_path(rec["id"]), rc.stdout.strip()) if rc.returncode == 0 else None
    if seen is None:
        out["reasons"].append("the note was never sighted by the runner")
    elif seen["at"] < offered[0]:
        out["reasons"].append("the note was sighted (%s) before the card was offered (%s)" % (seen["at"], offered[0]))
    s = note["script"]
    p = subprocess.run(["git", "cat-file", "blob", "%s:%s" % (note_commit, s["path"])], cwd=root, capture_output=True)
    if p.returncode != 0 or hashlib.sha256(p.stdout).hexdigest()[:16] != s["sha256"]:
        out["reasons"].append("the peer's script at the note's commit is not the one the note hashes")
    if out["reasons"]:
        return out
    res = RR.rerun(root, note_commit, _as_card(note), limit=limit, prefix=prefix, allow_static=allow_static)
    out["rerun"] = res
    if res["status"] != "REPRODUCED":
        out["reasons"].append("the peer's run: %s" % ("; ".join(res["reasons"]) or res["status"]))
        return out
    m = CF.SCRIPT.match(CF.read(card_text)[1].get("decisive script", ""))
    d = CF.DECISIVE.fullmatch(CF.read(card_text)[1].get("decisive lines", ""))
    if note["finding"] == "reproduced" and d and (note["decisive"]["lines"], note["decisive"]["sha256"]) != \
            (int(d.group(1)), d.group(2)):
        out["reasons"].append("the note says reproduced, and its decisive lines are not the card's")
        return out
    producer = _files(root, rec["commit"], m.group(1)) if m else set()
    peer = _files(root, note_commit, s["path"])
    out["reach"] = producer_reach(root, rec["commit"], m.group(1), note_commit, s["path"]) if m else []
    out["grade"] = "re-derived" if peer and not (peer & producer) and not out["reach"] else "reran"
    out["other_family"] = note["peer_code"].split("-")[0] != rec["seat_code"].split("-")[0]
    out["ok"] = True
    return out


def main(argv):
    note = json.loads(pathlib.Path(argv[0]).read_text(encoding="utf-8"))
    rec = json.loads(pathlib.Path(argv[argv.index("--record") + 1]).read_text(encoding="utf-8"))
    print(json.dumps({"form": form_problems(note, rec)}, indent=1))
    return 0 if not form_problems(note, rec) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
