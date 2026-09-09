"""B1306 slice D generator (REPORT mode by default): for every id in every seat's OWN index that has no HARVEST_LEDGER row, find main's evidence and draft a row.
Evidence = the main arcs whose FINDINGS/CHANGELOG text names the id (seat-prefixed grammar), classified: HARVESTED-EARLIER (a main arc names it with
'verif'/'re-run'/'reproduc' within the same line), CITED-EARLIER (named, no verification verb), UNREAD (no main text names it). Rows for UNREAD ids get
disposition SCHEDULED (slice D backlog, visible); nothing is closed unread. Writes rows.md + report.json; --apply appends the rows to the ledger."""
import sys, re, json, subprocess, pathlib, importlib.util
S = pathlib.Path(__file__).resolve().parent; R = next(p for p in [S] + list(S.parents) if (p / "scripts" / "checks" / "harvest_debt.py").is_file())   # the repo root, found relative to this file
sys.path.insert(0, str(R / "scripts/gates")); from gates import _VENDOR_RE
spec = importlib.util.spec_from_file_location("hd", R / "scripts/checks/harvest_debt.py"); hd = importlib.util.module_from_spec(spec); spec.loader.exec_module(hd)
ltext = (R / "docs/HARVEST_LEDGER.md").read_text(encoding="utf-8"); rows = hd.read_rows(ltext); pins = hd.read_pins(ltext)
main_ref = "origin/main"; main_frontier = set(hd._ls(main_ref, "frontier/")); main_docs = set(hd._ls(main_ref, "docs/"))
# main's text corpus for evidence: FINDINGS of every arc + CHANGELOG + the two ledgers, keyed by arc id
def main_corpus():
    corp = {}
    for d in sorted((R / "frontier").iterdir()):
        f = d / "FINDINGS.md"
        if f.is_file(): corp[d.name.split("_")[0]] = f.read_text(encoding="utf-8", errors="ignore")
    corp["CHANGELOG"] = (R / "CHANGELOG.md").read_text(encoding="utf-8", errors="ignore")
    return corp
corp = main_corpus()
VERB = re.compile(r"verif|re-?run|reproduc|re-?deriv|banked|harvest", re.I)
GRAMMAR = {  # seat key -> function id -> list of regexes that name it in main's text (seat-prefixed to avoid main's own numbers)
 "sm": lambda i: [re.escape(i), re.escape(i.replace("sm:B", "sB"))] if i.startswith("sm:B") else [re.escape(i)],
 "fc": lambda i: [rf"\bfc[:' ]?\s*{re.escape(i)}\b", rf"\bfc's {re.escape(i)}\b", rf"physics seat['s]* {re.escape(i)}\b", rf"\b{re.escape(i)}_[A-Z]"] if i[0] in "RH" else [re.escape(i)],
 "codex": lambda i: [rf"\bcodex[:' ]?\s*{re.escape(i)}\b", rf"\b{re.escape(i)}\b(?=[^|]{0,80}codex)", rf"codex[^|]{0,80}\b{re.escape(i)}\b"],
 "cc3": lambda i: [rf"\b{re.escape(i)}\b"],
 "hostile": lambda i: [rf"hostile[^|]{{0,60}}{re.escape(i)}", rf"memo {i.split()[-1]}\b(?=[^|]{{0,60}}(hostile|golden))"] if i.startswith("memo ") else [rf"\b{re.escape(i)}\b"],
 "cloud": lambda i: [rf"\bmemos? {i.split()[-1]}\b", rf"cloud[^|]{{0,60}}\bmemo {i.split()[-1]}\b"],
 "braver": lambda i: [rf"\b{re.escape(i)}\b(?=[^|]{0,80}(braver|cc3))", rf"(braver|cc3)[^|]{0,80}\b{re.escape(i)}\b"],
 "qor5up": lambda i: [rf"\b{re.escape(i)}\b(?=[^|]{0,80}(qor5up|consolidation))", rf"(qor5up|consolidation)[^|]{0,80}\b{re.escape(i)}\b"],
 "audit": lambda i: [rf"\b{re.escape(i)}\b(?=[^|]{0,80}audit)", rf"audit[^|]{0,80}\b{re.escape(i)}\b"],
}
def evidence(key, i):
    pats = [re.compile(p) for p in GRAMMAR[key](i)]; hits = []
    for arc, text in corp.items():
        for line in text.splitlines():
            if any(p.search(line) for p in pats):
                hits.append((arc, bool(VERB.search(line)), line.strip()[:160])); break
    return hits
def seat_headline(key, seat, head, rid, path):
    """the seat's own first line for the item (<= 25 words), from the item's file on the branch"""
    try:
        if key in ("sm", "cc3", "braver", "qor5up") and path.startswith("frontier/"): txt = hd._show(head, f"{path}/FINDINGS.md")
        elif key == "sm": txt = hd._show(head, path)
        elif key == "fc": txt = hd._show(head, path) if path.endswith(".md") else hd._show(head, f"{path}/FINDINGS.md") or hd._show(head, f"{path}/README.md")
        elif key == "cloud": txt = hd._show(head, path)
        elif key == "hostile": txt = hd._show(head, path)
        elif key == "audit": txt = hd._show(head, path)
        elif key == "codex": txt = ""
        else: txt = ""
    except Exception: txt = ""
    first = next((l.strip("# ").strip() for l in txt.splitlines() if l.strip()), "") if txt else ""
    words = first.split(); out = (" ".join(words[:25]) + (" …" if len(words) > 25 else "")).replace("|", "/")
    return _VENDOR_RE.sub("[vendor]", out).replace("[vendor]/", "origin/")   # the attribution gate's own list (gates.py): no vendor tokens in tracked text
out = {"seats": {}, "rows": []}; nrow = max(r["n"] for r in rows)
for seat in hd.SEATS:
    key = seat["key"]; pin = pins.get(key); head = hd._rev(pin) if pin else None          # the index is read AT THE PIN: items after it are the gate's NEW debt, not backlog
    if not head: continue
    if key == "cloud": hd.CLOUD_INDEX_CACHE["text"] = hd._show(head, "outside_bench/INDEX.md")
    idx = hd.seat_index(seat, head, main_frontier, main_docs); srows = hd.rows_for(seat, rows)
    rowed = set().union(*[hd.row_ids(seat, r, idx) for r in srows]) if srows else set()
    missing = sorted(i for i in idx if i not in rowed); stats = {"index": len(idx), "rowed": len(idx) - len(missing), "HARVESTED-EARLIER": 0, "CITED-EARLIER": 0, "UNREAD": 0}
    for i in missing:
        ev = evidence(key, i); verified = [a for a, v, _ in ev if v and a != "CHANGELOG"]; cited = [a for a, v, _ in ev if a != "CHANGELOG"]
        if verified: disp, arcs = "HARVESTED-EARLIER", verified
        elif cited: disp, arcs = "CITED-EARLIER", cited
        else: disp, arcs = "UNREAD", []
        stats[disp] += 1; nrow += 1
        hl = seat_headline(key, seat, head, i, idx[i]) or "(no first line read)"
        arcs_s = ", ".join(sorted(set(arcs))[:4]) + (" …" if len(set(arcs)) > 4 else "")
        dispo = {"HARVESTED-EARLIER": f"**VERIFIED-EARLIER** (a main arc names it with a verification verb: {arcs_s}; the grade is that arc's — re-read at slice D's pass)",
                 "CITED-EARLIER": f"**REGISTERED-EARLIER** (named on main without a verification verb: {arcs_s}; scheduled for a re-read, slice D)",
                 "UNREAD": "**SCHEDULED** (no main text names it — the slice D backlog, read before Review 57)"}[disp]
        out["rows"].append(f"| {nrow} | {seat['label']} | {i} | \"{hl}\" | `{idx[i]}` @ {head[:8]} | {dispo} | B1306 (D) | 2026-09-09 |")
    out["seats"][key] = stats; print(f"  {key:<8} index {stats['index']:>3} rowed {stats['rowed']:>3} | new rows: verified-earlier {stats['HARVESTED-EARLIER']:>3}, registered-earlier {stats['CITED-EARLIER']:>3}, scheduled {stats['UNREAD']:>3}")
(S / "rows.md").write_text("\n".join(out["rows"]) + "\n", encoding="utf-8"); json.dump(out["seats"], open(S / "report.json", "w"), indent=1)
print("rows drafted:", len(out["rows"]))
if "--apply" in sys.argv:
    p = R / "docs/HARVEST_LEDGER.md"; t = p.read_text(encoding="utf-8"); lines = t.rstrip("\n").split("\n")
    i = max(k for k, l in enumerate(lines) if re.match(r"^\| *\d+ *\|", l)); lines[i + 1:i + 1] = out["rows"]; p.write_text("\n".join(lines) + "\n", encoding="utf-8"); print("APPLIED")
