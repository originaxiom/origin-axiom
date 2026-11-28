#!/usr/bin/env python3
"""The banking verdict files: sealed, then opened; two ACCEPTs bank (the framework's thin path, patch T9; draft 1 §§ 2.4,
4 and 9; docs/roles/BANKING.md; main's M54 to M56; register row P-885).

THE SEATS. `queue/BANKING_SEATS.json` names the two banking seats, V1 and V2, each by its seat code and its branch. Main
and the author fill it; while it names no seat, the runner banks nothing.

THE FILES, on each banking seat's own branch, under `relays/claims/banking/`:
  EXPECT_<card>.md     the seat's expectation, committed before it runs (K3);
  SEAL_<card>.txt      one line: the SHA-256 of the verdict file's exact bytes, committed before either verdict is opened;
  VERDICT_<card>.json  {card, card_commit, seat, verdict, reason, script, decisive, labels}: ACCEPT, RETURN or REFUSE, one
                       paragraph of reasons, the seat's own script {path, sha256, run_as, control}, its decisive lines,
                       and the labels of docs/seats/README.md section 12 for its evidence (main's M60). The three words
                       name results, not rulings: ACCEPT, that the seat's own recomputation agrees with the card's
                       decisive lines; REFUSE, that it does not; RETURN, that the card could not be decided as filed.

THE RUNNER'S CHECK of one verdict:
  - the verdict hashes to its seal, and is the seat's (its code and the card's id and commit);
  - the expectation was sighted no later than the seal (K3);
  - BLIND (K1): the verdict was first sighted in a round after the one in which both seals were in. The sighting log is
    the runner's clock, and this is enforced at the resolution of its rounds: a seat opens its verdict only when the queue
    shows both seals, and a verdict pushed before that is seen in the same round as the last seal and refused;
  - the seat's own script is rerun at the verdict's commit, in T7b's sandbox (its own namespaces, as nobody), with its failing control, and must print the
    decisive lines it gives; it shares no file with the producer's (K2: rerunning the producer's script is reproduction,
    which the intake has done). Nor does it reach for the producer's computation another way (main's M71 point 1): its
    text, and that of the modules beside it that it imports, names neither the producer's decisive script nor its folder
    nor a file in it, and no file beside it is a renamed copy of one of the producer's. That sees only what is written
    plainly; the auditor's sample covers what it cannot see. These checks come before the rerun;
  - a verdict's check is kept, and its script not rerun, while its verdict, seal, expectation and the other seal's
    sighting stay the same (main's M71 point 3).

THE OUTCOME, once both verdicts hold (the runner's move alone, T1b):
  - two ACCEPTs: VERIFIED; but a card of main's own waits for a check from another family (§ 8), which neither banking
    seat gives when both share main's family and the peer's check did not;
  - two RETURNs: RETURNED; two REFUSEs: REFUSED;
  - any two that differ: SPLIT, settled by main on a seat's card, and by the auditor or the author on main's own (T1b).
  Decided here and said for main: RETURN beside REFUSE is a SPLIT, not a RETURN. Both seats said no, but for different
  reasons, and which one stands is a judgement.

A verdict that does not hold is reported, and the card stays AT_BANKING. A sealed verdict cannot be changed, so such a
card waits for main.

THE PEER NOTE is not sealed here: the runner must read it to grade it, and it sits on a public branch (T8). The banking
seats' blindness to it is the charter's rule K1, measured by the plants.

    python3 scripts/queue/banking.py VERDICT.json      # the verdict file's form; exit 0 when it holds
"""
import hashlib
import importlib.util
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


QS = _load("queue_schema_for_banking", HERE / "queue_schema.py")
CF = _load("card_form_for_banking", HERE / "card_form.py")
CU = _load("custody_for_banking", HERE / "custody.py")
RR = _load("rerun_for_banking", HERE / "rerun.py")
PN = _load("peer_note_for_banking", HERE / "peer_note.py")
DIR = "relays/claims/banking/"
SEATS_FILE = ROOT / "queue" / "BANKING_SEATS.json"
VERDICTS = ("ACCEPT", "RETURN", "REFUSE")
FIELDS = ("card", "card_commit", "seat", "verdict", "reason", "script", "decisive", "labels")
# docs/seats/README.md section 12 (main's M60): a verdict names a result, not a ruling, and gives the labels of its evidence
LABELS = ("computed once", "reproduced", "recomputed independently", "recomputed on another family of model",
          "expectations committed first", "tested against planted errors", "checked by a person",
          "checked outside the project", "not independently checked")
HEX64 = re.compile(r"[0-9a-f]{64}")
OUTCOME = {("ACCEPT", "ACCEPT"): "VERIFIED", ("RETURN", "RETURN"): "RETURNED", ("REFUSE", "REFUSE"): "REFUSED"}


def paths(cid):
    return {"expect": "%sEXPECT_%s.md" % (DIR, cid), "seal": "%sSEAL_%s.txt" % (DIR, cid),
            "verdict": "%sVERDICT_%s.json" % (DIR, cid)}


def seats(path=SEATS_FILE):
    """{"V1": {"code", "branch"}, "V2": {...}} when both are named; {} while they are not"""
    try:
        d = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    out = {}
    for v in ("V1", "V2"):
        s = d.get(v) or {}
        if isinstance(s, dict) and isinstance(s.get("code"), str) and not QS.code_problems(s["code"]) \
                and isinstance(s.get("branch"), str) and s["branch"]:
            out[v] = {"code": s["code"], "branch": s["branch"]}
    if len(out) == 2 and out["V1"]["code"] == out["V2"]["code"]:
        return {}
    return out if len(out) == 2 else {}


def form_problems(v, rec=None, code=None):
    if not isinstance(v, dict):
        return ["the verdict is not a table"]
    missing = [f for f in FIELDS if f not in v]
    extra = sorted(set(v) - set(FIELDS))
    bad = (["fields missing: %s" % ", ".join(missing)] if missing else []) + \
          (["fields not in the schema: %s" % ", ".join(extra)] if extra else [])
    if missing:
        return bad
    if v["verdict"] not in VERDICTS:
        bad.append("verdict %r is not one of %s" % (v["verdict"], ", ".join(VERDICTS)))
    if not isinstance(v["labels"], list) or not v["labels"] or any(l not in LABELS for l in v["labels"]):
        bad.append("labels is not a list of one or more of section 12's labels")
    if not isinstance(v["reason"], str) or not v["reason"].strip() or "\n\n" in v["reason"].strip() or len(v["reason"]) > 3000:
        bad.append("reason is not one paragraph of 1 to 3000 characters")
    note_like = {"card": v["card"], "card_commit": v["card_commit"], "peer_code": v["seat"], "finding": "reproduced",
                 "script": v["script"], "decisive": v["decisive"], "note": "x"}
    bad += [b.replace("peer_code", "seat") for b in PN.form_problems(note_like) if "finding" not in b]
    if rec is not None and not bad:
        if v["card"] != rec["id"] or v["card_commit"] != rec["commit"]:
            bad.append("the verdict is not for this card at its sealed commit")
        if code is not None and v["seat"] != code:
            bad.append("the verdict's seat %s is not the banking seat %s" % (v["seat"], code))
        if v["seat"] == rec["seat_code"]:
            bad.append("a banking seat does not bank a card of its own (D8)")
    return bad


def _at(root, ref, path):
    """(the commit that last changed path on ref, the blob) or (None, None)"""
    r = subprocess.run(["git", "log", "-1", "--format=%H", ref, "--", path], cwd=root, capture_output=True, text=True)
    c = r.stdout.strip()
    if r.returncode != 0 or not c:
        return None, None
    b = subprocess.run(["git", "rev-parse", "%s:%s" % (c, path)], cwd=root, capture_output=True, text=True)
    return (c, b.stdout.strip()) if b.returncode == 0 else (None, None)


def sightings(root, entries, cid, the_seats, at):
    """the log's new lines for the banking files of one card on both seats' branches"""
    new = []
    for v, s in sorted(the_seats.items()):
        for kind, path in sorted(paths(cid).items()):
            commit, _ = _at(root, "origin/" + s["branch"], path)
            if commit:
                e = CU.sight(root, entries + new, s["branch"], commit, path, kind, at)
                if e:
                    new.append(e)
    return new


def check_verdict(root, cid, rec, card_text, s, entries, other_seal_at, limit=RR.TIME_LIMIT, prefix=None,
                  allow_static=False, cached=None, run=True):
    """{ok, verdict, reasons, rerun, key}: one banking seat's verdict on one card. `cached` is the check a past round made;
    it is kept, and nothing is rerun, while the verdict, the seal, the expectation and the other seal's sighting are the
    same (main's M71 point 3: a filed seat's script runs once, not every round)"""
    out = {"ok": False, "verdict": None, "reasons": [], "rerun": None}
    ref, p = "origin/" + s["branch"], paths(cid)
    found = {k: _at(root, ref, path) for k, path in p.items()}
    if not found["verdict"][0]:
        return dict(out, reasons=["no verdict opened yet"])
    key = [found["verdict"][1], found["seal"][1], found["expect"][1], other_seal_at]
    if isinstance(cached, dict) and cached.get("key") == key:
        return cached
    out["key"] = key
    seen = {k: CU.first_sighting(entries, s["branch"], p[k], blob) for k, (_, blob) in found.items() if blob}
    if "seal" not in seen or seen.get("seal") is None:
        return dict(out, reasons=["the verdict has no seal sighted before it"])
    seal_text = subprocess.run(["git", "show", "%s:%s" % (found["seal"][0], p["seal"])], cwd=root, capture_output=True,
                               text=True).stdout.strip()
    raw = subprocess.run(["git", "cat-file", "blob", found["verdict"][1]], cwd=root, capture_output=True).stdout
    if not HEX64.fullmatch(seal_text) or hashlib.sha256(raw).hexdigest() != seal_text:
        out["reasons"].append("the verdict does not hash to its seal")
    if seen.get("expect") is None:
        out["reasons"].append("no expectation was sighted (K3)")
    elif seen["expect"]["at"] > seen["seal"]["at"]:
        out["reasons"].append("the expectation was sighted after the seal (K3)")
    last_seal = max(seen["seal"]["at"], other_seal_at or "9999")
    if seen.get("verdict") is None or other_seal_at is None or seen["verdict"]["at"] <= last_seal:
        out["reasons"].append("the verdict was opened before both seals were in (K1): it was first sighted in the round "
                              "of the last seal, or before")
    try:
        v = json.loads(raw.decode("utf-8"))
    except ValueError:
        return dict(out, reasons=out["reasons"] + ["the verdict is not JSON"])
    out["verdict"] = v.get("verdict") if isinstance(v, dict) else None
    out["reasons"] += form_problems(v, rec, s["code"])
    if out["reasons"]:
        return out
    blob = subprocess.run(["git", "cat-file", "blob", "%s:%s" % (found["verdict"][0], v["script"]["path"])], cwd=root,
                          capture_output=True)
    if blob.returncode != 0 or hashlib.sha256(blob.stdout).hexdigest()[:16] != v["script"]["sha256"]:
        return dict(out, reasons=["the seat's script at the verdict's commit is not the one the verdict hashes"])
    m = CF.SCRIPT.match(CF.read(card_text)[1].get("decisive script", ""))
    producer = PN._files(root, rec["commit"], m.group(1)) if m else set()
    if PN._files(root, found["verdict"][0], v["script"]["path"]) & producer:
        return dict(out, reasons=["the seat's script shares a file with the producer's (K2)"])
    reach = PN.producer_reach(root, rec["commit"], m.group(1), found["verdict"][0], v["script"]["path"]) if m else []
    if reach:                                     # main's M71 point 1: a rerun passing as a recomputation
        return dict(out, reasons=["the seat's script reaches for the producer's computation (K2): %s" % "; ".join(reach)])
    if not run:                                   # the landing's check (T11, main's M72): the reruns are the runner's
        return dict(out, ok=True, rerun="left to the runner")
    note_like = {"script": v["script"], "decisive": v["decisive"]}
    res = RR.rerun(root, found["verdict"][0], PN._as_card(note_like), limit=limit, prefix=prefix,
                   allow_static=allow_static)
    out["rerun"] = res
    if res["status"] != "REPRODUCED":
        return dict(out, reasons=["the seat's own run: %s" % ("; ".join(res["reasons"]) or res["status"])])
    out["ok"] = True
    return out


def outcome(rec, v1, v2, peer_other_family=None, the_seats=None):
    """the move the two verdicts decide, and its note: (status or None, note)"""
    pair = tuple(sorted((v1, v2)))
    status = OUTCOME.get((v1, v2)) if v1 == v2 else "SPLIT"
    if status == "VERIFIED" and rec["seat_code"] == QS.MAIN_CODE:
        fam = QS.MAIN_CODE.split("-")[0]
        banks_other = any(s["code"].split("-")[0] != fam for s in (the_seats or {}).values())
        if not banks_other and not peer_other_family:
            return None, "two ACCEPTs; a card of main's own waits for a check from another family (section 8)"
    return status, "the banking verdicts: %s and %s" % pair


def main(argv):
    v = json.loads(pathlib.Path(argv[0]).read_text(encoding="utf-8"))
    bad = form_problems(v)
    for b in bad:
        print(b)
    print("%d problem(s)" % len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
