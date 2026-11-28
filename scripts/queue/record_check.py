#!/usr/bin/env python3
"""The record check, "deciding", the premise check and the firewall's flag (the framework's thin path, patch T6; draft 1
§ 9; main's M54 and M55; register row P-885).

For one card, on main's record as it stands in this checkout, the runner computes and attaches:

  terms        the sweep's terms, the runner's own: the codes, register rows, identifications and arcs the card's
               `touches` and `premises on main` name, and the long words of its title. The card's own sweep line
               (`already on main?`) is kept as the producer's claim and is not used.
  topic        scripts/checks/topic_sweep.py on those terms: its VERDICT line, and the arcs and rows it names.
  banked       scripts/checks/already_banked.py on the title's words: whether settled or scheduled material exists.
  retracted    every premise arc whose verdict is RETRACTED or that a later arc supersedes; and every phrase of
               docs/RETRACTED_PHRASES.md the card uses.
  deciding     true when the card touches a code of the inputs scoreboard, an identification row (I-n), a register row
               (P-n) or one of the 19 by name, and its effect is not none (the draft: what moves a register item, a
               row of the record, or one of the 19). Computed here, not declared by the card.
  waits_on     door rule D6: the queue's cards (Q<nnnn>) the card names among its premises that are not VERIFIED. A card
               that waits stays where it is until each is VERIFIED; none of the record's arcs is waited on here, since an
               arc on main is the record (its own verdict is read under `retracted`).
  firewall     the author's rule A3: words of a comparison with data, or of a sealed look, on the card. A FLAG to the
               author, never a return: the runner cannot tell a comparison from a mention, and the plants measure it.

It returns nothing to the seat by itself: the runner (T7) reads `retracted`, `waits_on` and `firewall` and decides the move.

    python3 scripts/queue/record_check.py CARD.md [--queue queue/cards]      # prints the attachment as JSON
"""
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


CF = _load("card_form_for_the_record_check", HERE / "card_form.py")
ARC = re.compile(r"\bB(\d{1,4})\b")
QCARD = re.compile(r"\bQ\d{4,}\b")
# CHANGED 2026-11-27 (T7b; main's M61 and M64 item 15; Review 88's B11, B18): what a card touches is read by the form's own
# codes (scripts/queue/card_form.py `codes`): the scoreboard's codes in any case, identification and register rows, the
# law map's rows, and the 19 by plural and common names too
# words of a comparison with data or of a sealed look (A3); a flag, measured by the plants. CHANGED 2026-11-27 (M64 item
# 16; B3's probes): plurals, "compared to data", "comparison with data", "+/-", "agrees with experiment"
FIREWALL = re.compile(r"\b(PDG|Particle Data|CODATA|measured values?|experimental(ly)?|experiments?|observed values?|"
                      r"compar(e|ed|es|ing|ison)s? (it |them )?(with|to|against) (the )?(data|experiments?|measurements?)|"
                      r"against (the )?data|fit(ted|s)? to (the )?data|agree(s|d|ment)? with (the )?"
                      r"(data|experiments?|measurements?)|sealed look|unseal(ed|ing)?)\b|±|\+/-", re.I)
STOP = {"which", "their", "there", "these", "those", "about", "under", "every", "after", "before", "between", "within",
        "where", "while", "would", "could", "should", "other", "being", "level", "levels"}


WORDS = 6                                         # the title's long words a sweep uses; the rest are said, not used


def terms(fields, title):
    """the runner's sweep terms: (codes and rows and arcs, the title's long words used, the long words left out)"""
    named = fields.get("touches", "") + " " + fields.get("premises on main", "")
    codes = sorted({c for c in CF.codes(named) if not c.startswith("the 19: ")} | {"B%s" % n for n in ARC.findall(named)})
    words = sorted(set(w.lower() for w in re.findall(r"[A-Za-z][A-Za-z-]{4,}", title) if w.lower() not in STOP))
    return codes, words[:WORDS], words[WORDS:]


def deciding(fields):
    """true when the card touches a scoreboard code, an identification row, a register row, a law-map row or one of the
    19, and its effect is not none"""
    touches, effect = fields.get("touches", ""), fields.get("effect", "")
    if touches.strip().lower() == "none" or effect.strip().lower() == "none":
        return False
    return bool(CF.codes(touches))


def _run(root, *argv):
    r = subprocess.run([sys.executable, "-B", *argv], cwd=root, capture_output=True, text=True, timeout=600)
    return r.stdout


def topic(root, codes, words):
    if not codes and not words:
        return {"verdict": "no terms", "matches": []}
    rx = "|".join(re.escape(t) for t in codes + words)
    out = _run(root, "scripts/checks/topic_sweep.py", rx, "--limit", "20")
    lines = out.strip().splitlines()
    verdict = next((l for l in reversed(lines) if l.startswith("VERDICT")), lines[-1] if lines else "no output")
    matches = sorted(set(re.findall(r"\b(B\d{1,4}|P-\d+)\b", out)))
    return {"regex": rx, "verdict": verdict, "matches": matches}


def banked(root, words):
    if not words:
        return {"settled_or_scheduled": None, "lines": []}
    out = _run(root, "scripts/checks/already_banked.py", *words)
    return {"settled_or_scheduled": "SETTLED OR SCHEDULED MATERIAL EXISTS" in out,
            "lines": [l.strip()[:200] for l in out.strip().splitlines()[-3:]]}


def retracted(root, fields, text):
    out = {"premises": [], "phrases": []}
    for n in sorted(set(ARC.findall(fields.get("premises on main", ""))), key=int):
        for v in sorted(pathlib.Path(root, "frontier").glob("B%s_*/arc_verdict.json" % n)):
            try:
                d = json.loads(v.read_text(encoding="utf-8"))
            except ValueError:
                continue
            if d.get("verdict") == "RETRACTED":
                out["premises"].append("B%s is RETRACTED" % n)
            if d.get("superseded_by"):
                out["premises"].append("B%s is superseded by %s" % (n, d["superseded_by"]))
    registry = pathlib.Path(root, "docs", "RETRACTED_PHRASES.md")
    if registry.is_file():                            # B24: the sweep is loaded only where its registry stands
        rs = _load("retraction_sweep_for_the_record_check", pathlib.Path(root) / "scripts" / "checks" / "retraction_sweep.py")
        low = text.lower()
        out["phrases"] = [p for p in rs.phrases_in(registry.read_text(encoding="utf-8")) if p and p.lower() in low]
    return out


def arc_cards(queue, n):
    """the queue's cards that are the record's arc B<n> entering as a card (main's arcs in the trial): a card of main's own
    seat whose title opens with the arc's id, or whose card's name holds it (main's M61)"""
    out = []
    for cid, r in sorted(queue.items()):
        title, path = r.get("title", ""), r.get("card_path", "")
        if r.get("seat_code") == CF.QS.MAIN_CODE and (re.match(r"B%d\b" % n, title) or "_B%d_" % n in path):
            out.append(cid)
    return out


def waits_on(fields, queue, own=None):
    """D6: the queue's cards among the premises that are not VERIFIED (a card the queue does not hold is waited on too),
    and, for a premise arc that has its own card in the queue, that card until it is VERIFIED (main's M61)"""
    premises = fields.get("premises on main", "")
    named = set(QCARD.findall(premises))
    for n in set(ARC.findall(premises)):
        named |= set(arc_cards(queue, int(n)))
    # CHANGED 2026-11-28 (main, at the author's word, after the runner's first round on the workflow, M78 point 3): a card
    # never waits on itself. B2011's card names its own arc in its premises, so it waited on its own id, and every other
    # trial card waited on it. The line as it stood had no `own`: the card's own id was kept among those it waits on.
    named.discard(own)
    return [q for q in sorted(named) if (queue.get(q) or {}).get("status") != "VERIFIED"]


def firewall(text):
    return sorted(set(m.group(0).strip() for m in FIREWALL.finditer(text)))


def check(root, card_text, queue=None, own=None):
    """the attachment for one card; `own` is the card's own queue id, never waited on (M78 point 3)"""
    title, fields, _ = CF.read(card_text)
    codes, words, left = terms(fields, title or "")
    return {"terms": {"codes": codes, "words": words, "words_left_out": left},
            "producer_sweep": fields.get("already on main?", ""),
            "topic": topic(root, codes, words),
            "banked": banked(root, words),
            "retracted": retracted(root, fields, card_text),
            "deciding": deciding(fields),
            "waits_on": waits_on(fields, queue or {}, own),
            "firewall": firewall(card_text)}


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    qdir = pathlib.Path(argv[argv.index("--queue") + 1]) if "--queue" in argv else ROOT / "queue" / "cards"
    queue = {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in sorted(qdir.glob("Q*.json"))} if qdir.is_dir() else {}
    res = check(ROOT, pathlib.Path(argv[0]).read_text(encoding="utf-8"), queue)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
