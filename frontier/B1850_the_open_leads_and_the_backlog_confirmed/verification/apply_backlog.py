"""R76-1, P-616 (S306j, 2026-11-06/07): Review 74's three readers proposed CLOSED-HANDLED or CLOSED-NO-LOAD-NO-LEAD for
240 of the harvest ledger's SCHEDULED rows. Each proposal was checked at its pointer; every quote behind a decision was
found verbatim at its path (checks_backlog_*.json). A confirmed row's disposition becomes the closure, with the old
disposition kept in full inside [was: ...] (its word 'SCHEDULED' written in lower case, so the gate reads the current
disposition only). A row that feeds an open register row is re-pointed to it. An unconfirmed row stays SCHEDULED and
gains a dated note. The 36 rows the readers typed LEAD or DEBT are not touched here. Run from the repository root."""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
LEDGER = ROOT / "docs" / "HARVEST_LEDGER.md"
TAG = "R76-1, B1850"
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
import harvest_debt  # noqa: E402  (is_scheduled: the current disposition, not its history)

# unconfirmed rows that feed an open register row: re-pointed there
REPOINT = {
    248: ("P-613", "B8071's real-form compactness is evidence for the open lead P-613 (B1098 never engaged it)"),
    250: ("P-613", "B8073 is named in the open lead P-613"),
    254: ("P-613", "B8077 is named in the open lead P-613"),
    256: ("P-613", "B8079's 109-flat arrangement is the input to P-613's first computation"),
    309: ("P-613", "Paper II's 109-flat lattice is the one P-613 rests on (via codex R013)"),
    322: ("P-613", "B8149 narrows codex R013's residue, on which P-613 rests"),
    195: ("P-528", "the open debt P-528 owes main's reading of R61/R62 against I-26"),
    200: ("P-606", "R08 recomputed B298/B1161's obstruction, which the open debt P-606 questions"),
    350: ("P-615", "memo 101's time reversal as the γ₅ bit bears on the open lead P-615 (fc R55's γ₅ = T assignment)"),
    419: ("P-492", "the memo's surviving § 1 is memo 171's type error, open under the debt P-492"),
}


def cell(s):
    return s.replace("|", "∣")


def main():
    checks = []
    for name in ("checks_backlog_cloud.json", "checks_backlog_physics.json", "checks_backlog_retired.json"):
        checks += json.load(open(HERE / name, encoding="utf-8"))
    by_row = {}
    for o in checks:
        assert o["row"] not in by_row, o["row"]
        by_row[o["row"]] = o
    lines = LEDGER.read_text(encoding="utf-8").split("\n")
    idx = {}
    for i, ln in enumerate(lines):
        m = re.match(r"\| (\d+) \| ", ln)
        if m and int(m.group(1)) not in idx:
            idx[int(m.group(1))] = i
    n_close = n_repoint = n_keep = 0
    for row, o in sorted(by_row.items()):
        i = idx[row]
        c = lines[i].split(" | ")
        assert len(c) == 8 and c[7].endswith(" |"), (row, len(c))
        old = c[5]
        if not harvest_debt.is_scheduled(old):
            continue      # already off SCHEDULED (rows 13, 15, 44, 623: the word was only in their history)
        hist = re.sub(r"SCHEDULED", "scheduled", old)
        if o["verdict"] == "CONFIRMED":
            word = "CLOSED-HANDLED" if o["proposed"] == "CLOSED-HANDLED" else "CLOSED-NO-LOAD-NO-LEAD"
            c[5] = "**%s** (%s, main's check at the pointer: %s; evidence in %s) [was: %s]" % (
                word, TAG, cell(o["reason"]), o["path"], hist)
            n_close += 1
        elif row in REPOINT:
            host, why = REPOINT[row]
            c[5] = "**CARRIED by %s** (%s: %s) [was: %s]" % (host, TAG, why, hist)
            n_repoint += 1
        else:
            if "SCHEDULED" not in old or "R76-1, B1850" in old:
                raise SystemExit("row %d: unexpected state" % row)
            c[5] = old + " [2026-11-06, %s: the reader's %s not confirmed — %s]" % (TAG, o["proposed"], cell(o["reason"]))
            n_keep += 1
        lines[i] = " | ".join(c)
    LEDGER.write_text("\n".join(lines), encoding="utf-8")
    print("closed %d, re-pointed %d, kept SCHEDULED with a note %d" % (n_close, n_repoint, n_keep))


if __name__ == "__main__":
    main()
