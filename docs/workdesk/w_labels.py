#!/usr/bin/env python3
"""Main's weave_or_thread field for every W arc, under docs/workdesk/THE_LABELS_RULE_2026-10-29.md (committed first).

A label is copied from the record, in this order: the status row ("weave result" or "thread result", exactly one), the
arc's own bold "Weave or thread" paragraph in NOTE, the "Weave or thread" section of its W###_RULE.md. A source gives a
label only when its answer opens with Weave, Weave-type or "A weave result" (weave), Thread or "A thread result"
(thread), or Neither (neither). Only where no source gives one does this seat assign a label, listed in ASSIGNED below
with its reason. Sources that disagree are listed under "conflicts"; the earlier source wins.

    python3 -B docs/workdesk/w_labels.py            # write the register
    python3 -B docs/workdesk/w_labels.py --check    # rebuild in memory and compare with the committed register
"""
import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))
import extract_desk_data as X  # noqa: E402  (NOTE's status table, one row per W arc)

D = REPO / "docs" / "dossiers" / "the_weave_2026-10-07"
OUT = D / "W_VERDICTS.json"
RULE = "docs/workdesk/THE_LABELS_RULE_2026-10-29.md"
OPENS = [("weave", r"(weave-type|weave|a weave result)\b"), ("thread", r"(thread|a thread result)\b"),
         ("neither", r"neither\b")]

# Step 4 of the rule: this seat's labels where no source gives one, each with its reason. They were set after reading
# each arc's status row, section and rule, by one mapping of the record's own words, applied to every arc alike:
#   the row's own tag "(WEAVE ...)" or "a WEAVE census/theorem" (a form the rule's step 1 did not name), or "weave-type"
#   for the arc's whole claim, gives weave;
#   "thread-and-frame" or "thread-frame" gives thread, as main labels its arcs on lines chosen by a stated rule;
#   "frame result", "frozen piece" or "identities of the frame" gives neither, as main labels its frozen pieces;
#   a check or third opinion of another seat's arc, a reading, or a chosen object not forced gives neither;
#   an arc with parts of different kinds is labelled by its headline claim, and the parenthetical names the other parts.
ASSIGNED = {
    "W1": ("weave (three parities, permuted with none distinguished only when the moves act together)",
           "the claim is about the moves acting together on every thread"),
    "W2": ("weave (the common point every thread shares)", "one structure all threads share"),
    "W3": ("weave (the same A4 and 2T on every odd-trace thread)", "a claim about every odd-trace thread at once"),
    "W4": ("weave (one triplet, the same on every odd-trace thread, under the weave's group)",
           "a claim about every odd-trace thread at once"),
    "W5": ("neither (a reading)", "status READING"),
    "W6": ("weave (Theorem G), with thread results inside (the +LR reading and the census)",
           "the row's tags: PROVED (WEAVE); COMPUTED (THREAD)"),
    "W7": ("weave (by rule)", "the row's tag: COMPUTED (WEAVE, by rule)"),
    "W8": ("weave (Lemma V, with the wave)", "the row's tag: PROVED (Lemma V, WEAVE + WAVE)"),
    "W9": ("weave", "the row's tag: COMPUTED (WEAVE, two routes)"),
    "W10": ("weave", "the row's tag: COMPUTED (WEAVE)"),
    "W11": ("weave (with the wave; sm:B1552 sealed)", "the row's tag: PROVED (WEAVE + WAVE)"),
    "W12": ("weave (with the wave)", "the row's tag: PROVED (WEAVE + WAVE)"),
    "W13": ("neither (a check of main's B1434)", "status VERIFIED: main's B1434 read with this seat's code"),
    "W14": ("thread (F-CI's index on each thread, over a census of every odd-trace thread to length 6)",
            "the slope law and the census are each thread's; the arc finds F-CI's content not a weave quantity"),
    "W15": ("weave (Theorem H and the weave's own extension, over a census of 32 states)",
            "the hand is the determinant of the weave's triplet on every odd-trace thread"),
    "W16": ("neither (a check of main's B1601 and B1604)", "status VERIFIED"),
    "W17": ("weave", "the row's tag: COMPUTED (WEAVE, 32 of 32 states)"),
    "W18": ("weave", "the row's tag: COMPUTED (WEAVE, 32 states)"),
    "W19": ("neither (a reading; the facts classical)", "status READING"),
    "W20": ("weave (the weave's own SL(2) and Euler characteristic), a reading for the dictionary",
            "three on the weave, zero on every thread"),
    "W21": ("weave (the hand by Hodge type on the shared fibre, under the weave's group)",
            "the zero modes for the three parities on the fibre every thread shares"),
    "W22": ("weave", "the row's tag: PROVED and COMPUTED (WEAVE)"),
    "W23": ("weave (a census)", "the row's tag: COMPUTED (WEAVE; a census, negative)"),
    "W24": ("weave (a census)", "the row: a WEAVE census, NEGATIVE"),
    "W25": ("weave (a theorem)", "the row: a WEAVE theorem"),
    "W27": ("weave (given the stated link Λ, an input)", "STATED (the link Λ, an input) and COMPUTED"),
    "W29": ("neither (a chosen object, the ℤ₆ flux, not forced)",
            "the arc's own words: the object is chosen, not forced"),
    "W31": ("neither (a weave-type computation on a chosen object, the ℤ₅ flux, not forced)",
            "the arc's own words: a weave-type computation on a chosen structure; the object is chosen, not forced"),
    "W36": ("neither (a check of the audit lane's phase, and a reading)", "status VERIFIED and READING"),
    "W39": ("neither (a reading given Λ)", "status READING, no new computation"),
    "W41": ("weave (the zero modes under all of SL(2, ℤ) at once)", "the rule: the moves, all of SL(2, ℤ) at once"),
    "W42": ("weave (every subgroup of the weave's group, and a census of every thread to length 12)",
            "the rule: Part A weave-type, Part B weave-type as a census; with a check of main's B1620"),
    "W43": ("weave (every subgroup of each frame's group, none chosen)", "the rule: every residual, none chosen"),
    "W44": ("weave (every residual pair in each frame, none chosen)", "the rule: every residual pair, none chosen"),
    "W48": ("weave (the weave's own surface), conditional on a dictionary beyond Λ",
            "the rule: the weave's own surface, read by every move at once"),
    "W58": ("neither (a check of an outside preprint; K1 and K2 on the weave's T)", "an outside claim checked"),
    "W75": ("weave (U1, a census of every thread under a stated rule), U2 to U4 fibre-level",
            "the row: U1 a weave-type census, U2 to U4 fibre-level"),
    "W76": ("weave (a census of thread quantities under a stated rule)", "the row's own words"),
    "W80": ("weave (on the ruled branch, given Λ, under main's ansatz), a test of main's B1637",
            "the rule: as B1637 and W78, a WEAVE result on the ruled branch"),
    "W81": ("neither (a check of the audit lane's character)", "the row's own words"),
    "W82": ("neither (two checks for main's frame tribunal)", "the row's own words"),
    "W83": ("neither (an answer to a tribunal item, in the audit lane's frame)", "the row's own words"),
    "W86": ("neither (a check of chat1's whole branch; each item keeps its own label)", "the arc's own words"),
    "W88": ("neither (a scoreboard of relations against the data, mixed by relation)",
            "the arc's own words: mixed, by relation, each labelled"),
    "W93": ("neither (a fibre-frame result at one τ, a frozen piece, as main's B1658)", "the arc's own words"),
    "W94": ("neither (a fibre-frame result at one τ, a frozen piece)", "the arc's own words"),
    "W96": ("neither (identities of one frame, and a frozen piece at ω, as main's B1659)", "the arc's own words"),
    "W97": ("thread (a thread-frame result on each thread of a stated set, T-low)", "the arc's own words"),
    "W99": ("neither (a paper read; its two proofs are weave statements)",
            "the arc's own words: the read itself is neither"),
    "W107": ("weave", "the rule: a WEAVE question"),
    "W108": ("weave (about the forms)", "the rule: a WEAVE question about the forms"),
    "W109": ("weave (every transvection of every n ≥ 3 records)", "main's B1677 for every n, by hand"),
    "W110": ("weave (every transvection of every n ≥ 3 records, on the word side)", "a claim about every class of F_n"),
    "W111": ("weave (every mapping class at every genus)", "the surface route, by hand"),
    "W112": ("weave (given Λ and W69's hypotheses)", "the row: a WEAVE-type result given Λ and W69's hypotheses"),
    "W128": ("weave (C0, C2 and C4), C1 the Standard Model's group theory, C3 a reading", "the row's own words"),
    "W129": ("neither (a reading across W127, W128 and the record)", "status READING"),
    "W140": ("weave (C1, every move at once), with a census of thread objects (C2 to C4)", "the row: C1 WEAVE"),
    "W151": ("weave (the lemma, Q3, for every pair of sections)", "the rule: the lemma (Q3) is weave-type"),
    "W152": ("weave (K2 and K3, the moves' group on the common point's qubit)", "the row: K2 and K3 weave-type"),
    "W153": ("weave", "the row: L1 to L4 weave-type, every cell"),
    "W154": ("weave", "the row: C0 to C3 weave-type, every cell"),
    "W155": ("weave", "the row: H0 to H3 weave-type, every cell"),
    "W156": ("neither (a check of main's B1749)", "the arc's own words: a check of main's census"),
    "W157": ("neither (a check of main's B1753)", "the arc's own words: a check of main's census"),
    "W158": ("neither (a frame result at the six's strip)", "the arc's own words"),
    "W159": ("neither (a frame result at the six's strip)", "the arc's own words"),
    "W160": ("neither (a frame result, data-free)", "the arc's own words"),
    "W161": ("thread (one line class, four points and ten recipes chosen by their author)",
             "the arc's own words: a thread-and-frame result; with a check of the agy branch's B1762"),
    "W162": ("neither (a frame result on stated lines and a stated grid)", "the arc's own words"),
    "W163": ("neither (a check of main's B1755)", "the arc's own words: a check of main's census"),
    "W164": ("neither (a check of main's B1786)", "the arc's own words: a check of main's census"),
    "W165": ("neither (a check of main's B1792)", "the arc's own words: a check of main's census"),
    "W166": ("thread (one line class, 38 rows the data chose, fitted numbers)",
             "the arc's own words: a thread-and-frame result"),
    "W167": ("neither (a frame result; the potential weave-type)", "the arc's own words"),
    "W168": ("neither (a check of chat1's P-323)", "the arc's own words: a third opinion"),
    "W169": ("neither (a frame result at a counted line; the potential weave-type)", "the arc's own words"),
    "W170": ("neither (a frame result: the potential's own state, given counted choices)", "the arc's own words"),
    "W172": ("neither (a frame result at a counted line; the mirror lemma for every content)", "the arc's own words"),
    "W173": ("thread (a thread-and-frame look at data-chosen rows)", "the arc's own words"),
    "W174": ("neither (a frame census over every census line and every forced pattern on record)",
             "the arc's own words"),
    "W175": ("neither (a frame result on stated classes; the potential weave-type)", "the arc's own words"),
}


def clean(text):
    return re.sub(r"\*\*", "", text).strip()


def opening(answer):
    """the label an answer opens with, or None"""
    a = re.sub(r"^[\s:.?—-]+", "", clean(answer))
    for label, pat in OPENS:
        if re.match(pat, a, re.I):
            return label
    return None


def qualifier(answer):
    """what the record attaches to the opening word in the same sentence, or None"""
    a = re.sub(r"^[\s:.?—-]+", "", clean(answer))
    first = re.split(r"(?<=[.;])\s", a, maxsplit=1)[0]
    m = re.match(r"(?:a\s+)?(?:weave|thread|neither)(?:-type)?(?:\s+results?|\s+objects?)?[,:]?\s*(.*)$", first, re.I)
    q = m.group(1).rstrip(".;: ").strip() if m else ""
    q = re.sub(r"^strictly[,:]?\s*", "", q)
    return q or None


def sections(note):
    """{W id: [(first line, last line)]}, 1-based, for every '## W<n>.' heading"""
    heads = [i for i, ln in enumerate(note) if ln.startswith("## ")]
    out = {}
    for k, i in enumerate(heads):
        m = re.match(r"^## (W\d+)[.:]", note[i])
        if m:
            j = heads[k + 1] if k + 1 < len(heads) else len(note)
            out.setdefault(m.group(1), []).append((i + 1, j))
    return out


def note_paragraph(note, spans):
    """the arc's own bold 'Weave or thread' paragraph: (line, answer text) or None"""
    for a, b in spans:
        for n in range(a, b + 1):
            ln = note[n - 1]
            m = re.match(r"^\*\*(?:Weave or thread|Thread or weave)[^*]*\*\*(.*)$", ln, re.I)
            if m:
                return n, paragraph(m.group(1), note, n, b)
    return None


def paragraph(first, lines, n, stop):
    """the answer's text: the rest of line n, or the next non-blank line, joined with its continuation lines"""
    parts, k = [first.strip()] if first.strip() else [], n
    while not parts and k < stop:
        if lines[k].strip():
            parts.append(re.sub(r"^-\s+", "", lines[k].strip()))
        k += 1
    while k < stop and lines[k].strip() and not re.match(r"^\s*(?:-\s|#|\*\*\w|\|)", lines[k]):
        parts.append(lines[k].strip())
        k += 1
    return " ".join(parts)


def rule_section(wid):
    """the 'Weave or thread' section of the arc's rule file: (file:line, answer text) or None"""
    f = D / f"{wid}_RULE.md"
    if not f.exists():
        return None
    lines = f.read_text(encoding="utf-8").splitlines()
    for n, ln in enumerate(lines, 1):
        bold = re.match(r"^\*\*(?:Weave or thread|Thread or weave)[^*]*\*\*(.*)$", ln, re.I)
        head = re.match(r"^#+\s*(?:Weave or thread|Thread or weave)\b", ln, re.I)
        if bold or head:
            return f"{f.name}:{n}", paragraph(bold.group(1) if bold else "", lines, n, len(lines))
    return None


def build():
    note = (D / "NOTE.md").read_text(encoding="utf-8").splitlines()
    secs = sections(note)
    entries, conflicts, counts = [], [], {"copied": 0, "assigned": 0, "missing": 0}
    for row in X.arcs():
        wid, kw, tag, status, line = row[0], row[1], row[2], row[3], row[5]
        found = []
        if tag:
            found.append(("status row", tag.lower(), status[:200], None))
        p = note_paragraph(note, secs.get(wid, []))
        if p and opening(p[1]):
            found.append((f"NOTE.md:{p[0]}", opening(p[1]), clean(p[1])[:200], qualifier(p[1])))
        r = rule_section(wid)
        if r and opening(r[1]):
            found.append((r[0], opening(r[1]), clean(r[1])[:200], qualifier(r[1])))
        if len({f[1] for f in found}) > 1:
            conflicts.append({"id": wid,
                              "sources": [{"source": s, "label": lab, "quote": q} for s, lab, q, _ in found]})
        if found:
            src, lab, quote, qual = found[0]
            wot = f"{lab} ({qual})" if qual else lab
            counts["copied"] += 1
        elif wid in ASSIGNED:
            wot, quote = ASSIGNED[wid]
            src = "assigned"
            counts["assigned"] += 1
        else:
            wot, src, quote = None, "missing", ""
            counts["missing"] += 1
        entries.append({"id": wid, "verdict": kw, "weave_or_thread": wot, "source": src, "quote": quote,
                        "note_row": f"NOTE.md:{line}"})
    entries.sort(key=lambda e: int(e["id"][1:]))
    return {"rule": RULE,
            "field": "weave_or_thread (main's convention: weave, thread or neither, neither with its reason)",
            "counts": counts, "conflicts": conflicts, "arcs": entries}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args()
    reg = build()
    text = json.dumps(reg, ensure_ascii=False, indent=1) + "\n"
    if args.check:
        same = Path(args.out).read_text(encoding="utf-8") == text
        print("register matches the record" if same else "register differs from a rebuild")
        sys.exit(0 if same and reg["counts"]["missing"] == 0 else 1)
    Path(args.out).write_text(text, encoding="utf-8")
    print(json.dumps(reg["counts"]), "conflicts:", len(reg["conflicts"]))


if __name__ == "__main__":
    main()
