"""B1889 -- the seats, digested from the record: what each one sent, what became of each item, and when it last moved.

Every count on SEATS.md is read from the harvest ledger AS IT STOOD AT ONE COMMIT OF MAIN (the commit is named on the page and
in SEATS.json), so the page is a dated statement that can be recomputed for good and is never stale by construction.  Nothing
is typed by hand but three tables, each marked as main's:

  CLASSES   the classes of outcome, by the leading words of a row's disposition;
  SEATS     the seats, with the names their rows are filed under;
  FIRST     the names that match no registered seat, sorted by what the rows themselves say.

What could fail: a row that no seat claims, or two; a disposition that falls in no class (it is counted as 'other' and listed);
a seat of the gate's registry that this table does not hold; a page that differs from what the builder gives at its commit.

    python3 -B frontier/B1889_the_seats_digested/verification/build_seats.py                 # check the committed pages
    python3 -B frontier/B1889_the_seats_digested/verification/build_seats.py --write COMMIT  # rebuild them as of COMMIT
"""
import collections
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = next(p for p in HERE.parents if (p / "GENESIS.md").is_file())

# the classes, by the leading words of a row's disposition.  Order matters: the first that matches.
CLASSES = [
    ("differed", r"^(VERIFIED-DIFFERS|VERIFIED WITH CORRECTIONS|DISPUTED|REFUTED|AGREES WITH MAIN, AND CORRECTS IT|NOT REPRODUCED)"),
    ("verified", r"^(VERIFIED|REPRODUCED|RE-DERIVED|PARTLY VERIFIED|ALREADY ON MAIN|AGREES|CONFIRMATION|CONSISTENT|READ; VERIFIED|§§1–4 \*\*REPRODUCED)"),
    # "ROWED <date> (<arc>), NOT READ" added 2026-11-12 (Review 79): six rows that say so were sorted as registered by their first word
    ("not read", r"^(SCHEDULED|UNREAD|QUEUED|RECEIVED, NOT READ|REGISTERED; NOT READ|REGISTERED BY FILE NAME; NOT READ|NOT RE-RUN|ROWED [^:]{0,40}NOT READ)"),
    ("closed by triage", r"^(CLOSED-HANDLED|CLOSED-NO-LOAD-NO-LEAD|SUPERSEDED|CARRIED|ALREADY DONE)"),
    ("registered", r"^(REGISTERED|RUN-GREEN, REGISTERED|RUN, REGISTERED|RUN, NOT RE-DERIVED|ROWED|LOGGED|RECORDED)"),
    ("read", r"^(READ|TAKEN|ADOPTED|ANSWERED|BANKED|DIGESTED|REVIEWED|ACCEPTED|BOTH PAGES READ|the rule READ)"),
]
ORDER = ["verified", "differed", "read", "registered", "closed by triage", "not read", "other"]
MEANS = {
    "verified": "main recomputed it, in full or in the part the row names, and it held",
    "differed": "main recomputed it and found a difference, an overstatement or a correction (in some rows the correction is of main)",
    "read": "main read it in full; no recomputation, or a check of a part",
    "registered": "main recorded it; read at headline level or by a cheaper reader; not verified",
    "closed by triage": "closed against other work at a pointer, without a full read",
    "not read": "not read, or queued behind something else",
    "other": "a leading word outside these classes; the rows are listed",
}

# the seats.  `cells` are the names a row's seat cell is matched against, lower case; the longest match wins.
# `state` is main's, from the last commit on the seat's branch as fetched on the day of the build and from what the owner has said.
SEATS = [
    dict(key="chat1", name="the web seat (chat1)", cells=("web seat", "chat1"), state="working", reads="directly"),
    dict(key="advisor", name="the advisor seat (cld-advisor)", cells=("advisor seat",), state="working", reads="directly"),
    dict(key="agy", name="the agy lane (four branches)", cells=("agy lane",), state="working", reads="through the mask only; its code is never run"),
    dict(key="audit", name="the physical lane (the audit seat)", cells=("audit seat", "audit:"), state="working", reads="its purely mathematical files, through the second mask"),
    dict(key="auditfork", name="the physical lane's fork lane", cells=("audit-fork", "fork lane"), state="quiet since 2026-10-13", reads="as the physical lane"),
    dict(key="explore", name="the explore seat", cells=("explore seat",), state="quiet since 2026-11-07", reads="directly"),
    dict(key="sm", name="the SM-derivation seat", cells=("sm-derivation", "sm seat", "sm-seat"), state="quiet since 2026-11-06", reads="directly"),
    dict(key="independent", name="the independent audit lane", cells=("independent audit lane",), state="quiet since 2026-11-03", reads="directly"),
    dict(key="referee", name="the referee lane", cells=("referee lane",), state="quiet since 2026-10-17", reads="directly"),
    dict(key="weavearchive", name="the weave archive (an import, not a seat)", cells=("archive lane", "weave archive"), state="one import, 2026-10-13", reads="directly"),
    dict(key="banking", name="the owner's other workspace (one handoff)", cells=("banking seat",), state="one handoff, 2026-10-13", reads="directly"),
    dict(key="lp", name="the listening thread", cells=("listening thread", "lp seat"), state="ended 2026-10-06", reads="directly"),
    dict(key="hypatia", name="a session lane (one commit)", cells=("session lane", "hypatia"), state="ended 2026-10-06", reads="directly"),
    dict(key="cloud", name="the cloud seat (the outside bench)", cells=("cloud",), state="ended 2026-09-18", reads="directly"),
    dict(key="cc3", name="cc3 (the paper seat)", cells=("cc3",), state="ended 2026-09", reads="directly"),
    dict(key="braver", name="cc3's braver-questions branch", cells=("braver",), state="ended 2026-09", reads="directly"),
    dict(key="fc", name="the physics seat (fc)", cells=("physics seat (fc)",), state="retired 2026-10-04 at the owner's word", reads="directly"),
    dict(key="codex", name="the codex seat", cells=("codex",), state="ended 2026-09", reads="directly"),
    dict(key="sep16", name="the sep16 seat (xB arcs)", cells=("sep16", "xb"), state="ended 2026-09-29", reads="directly"),
    dict(key="qor5up", name="the consolidation seat", cells=("qor5up", "consolidation"), state="ended 2026-09", reads="directly"),
    dict(key="hostile", name="the hostile-review seat", cells=("hostile",), state="ended 2026-08", reads="directly"),
    dict(key="review", name="the paper-review seat", cells=("review seat",), state="ended 2026-10-01", reads="directly"),
    dict(key="sessionrelay", name="a session relay (one handoff)", cells=("the session-relay seat",), state="one handoff, 2026-09-09", reads="directly"),
]
WORKING = ("chat1", "advisor", "agy", "audit")
# names that match no registered seat or match more than one, sorted by what the rows themselves say.  Tried first, in this order.
FIRST = [
    ("fork lane", "auditfork"), ("hostile", "hostile"), ("referee lane", "referee"), ("independent audit lane", "independent"),
    ("physics seat (fc)", "fc"),
    ("physical-bridge lane", "audit"),      # 24 rows of 2026-11-03/04: the physical lane under its branch's name
    ("the physical lane", "audit"),         # 2 rows of 2026-11-05
    ("audit lane", "audit"),                # 17 rows of 2026-10-27..29: the physical lane's relays, named PHYSICAL_TO_MAIN
    ("the session-relay seat", "sessionrelay"), ("banking seat", "banking"),
]


def klass(d):
    d = re.sub(r"^[\*\s#0-9–\-]+", "", d) if not d.lstrip("* ").startswith("§") else d.lstrip("* ")
    for name, rx in CLASSES:
        if re.match(rx, d):
            return name
    return "other"


def seat_of(cell):
    cell = cell.lower()
    for a, k in FIRST:
        if a in cell:
            return [k]
    best = collections.defaultdict(int)
    for s in SEATS:
        for x in s["cells"]:
            if x in cell:
                best[s["key"]] = max(best[s["key"]], len(x))
    if not best:
        return []
    top = max(best.values())
    return sorted(k for k, v in best.items() if v == top)


def rows(text):
    out = []
    for l in text.split("\n"):
        if re.match(r"^\| \d+ \|", l):
            c = [x.strip() for x in l.strip().strip("|").split(" | ")]
            if len(c) >= 8:
                out.append(dict(n=int(c[0]), cell=c[1], item=c[2], disposition=c[5], arc=c[6], date=c[7][:10], klass=klass(c[5])))
            elif len(c) == 6:
                # CORRECTED 2026-11-12 (Review 79; found by a reading on another family of model).  Thirteen rows of the ledger have
                # six cells, with no cell for main's arc and none for the date (633 to 638 and 879 to 885).  This reader asked for
                # eight and dropped them without a word, so the digest counted 1,686 rows of 1,699.  They are read now.  Their date
                # is the first date in their disposition, or that of the last dated row above them.
                m = re.search(r"\d{4}-\d{2}-\d{2}", c[5])
                out.append(dict(n=int(c[0]), cell=c[1], item=c[2], disposition=c[5], arc="", date=(m.group(0) if m else (out[-1]["date"] if out else "")), klass=klass(c[5])))
            else:
                raise ValueError("a numbered row of the ledger with %d cells, which this reader does not know: %s" % (len(c), l[:90]))      # nothing is dropped without a word
    return out


def flagged():
    """the rows each reader flagged as unused and possibly important, read from its report as it was received"""
    out = {}
    for f in sorted((HERE / "readers").glob("reader_G*.txt")):
        t = f.read_text(encoding="utf-8")
        g = f.stem.replace("reader_", "")
        secs = re.findall(r"PART 3.*?(?=PART 4)", t, flags=re.S) if g.startswith("G5") else re.findall(r"UNUSED AND POSSIBLY IMPORTANT.*?(?=TRACK RECORD)", t, flags=re.S)
        rows = []
        for s in secs:
            for line in s.split("\n"):
                m = re.match(r"^(?:-\s*|\d+\.\s*Row\s*)?(\d{1,4})\b", line.strip())
                if m and "\"" in line:
                    rows.append(int(m.group(1)))
        out[g] = rows
    return out


def at(commit, path):
    r = subprocess.run(["git", "-C", str(ROOT), "show", "%s:%s" % (commit, path)], capture_output=True)
    if r.returncode != 0:
        raise SystemExit("cannot read %s at %s: is this a full clone? (%s)" % (path, commit, r.stderr.decode()[:120].strip()))
    return r.stdout.decode("utf-8")


def build(commit, text=None):
    """the digest of the ledger at `commit`; `text` stands in for the ledger in a planted test"""
    RW = rows(at(commit, "docs/HARVEST_LEDGER.md") if text is None else text)
    by, loose, twice = collections.defaultdict(list), [], []
    for r in RW:
        k = seat_of(r["cell"])
        if len(k) == 1:
            r["seat"] = k[0]; by[k[0]].append(r)
        elif not k:
            loose.append(r["n"])
        else:
            twice.append((r["n"], k))
    R = {r["n"]: r for r in RW}
    seats = []
    for s in SEATS:
        mine = by.get(s["key"], [])
        c = collections.Counter(r["klass"] for r in mine)
        v, d = c.get("verified", 0), c.get("differed", 0)
        seats.append(dict(key=s["key"], name=s["name"], state=s["state"], reads=s["reads"], rows=len(mine),
                          by_class={k: c.get(k, 0) for k in ORDER},
                          recomputed=v + d, recomputed_share=round((v + d) / len(mine), 3) if mine else None,
                          first=min((r["date"] for r in mine), default=None), last=max((r["date"] for r in mine), default=None)))
    filed = collections.Counter()
    for r in RW:
        cell = re.sub(r"\s*\(.*$", "", r["cell"]).strip().lower()
        if any(a in r["cell"].lower() for a, _ in FIRST):
            filed[(cell, r.get("seat"))] += 1
    return dict(
        as_of=commit, rows=len(RW), last_row=max(r["n"] for r in RW),
        totals={k: sum(1 for r in RW if r["klass"] == k) for k in ORDER},
        seats=seats, rows_no_seat_claims=loose, rows_two_seats_claim=twice,
        sorted_by_main=[dict(filed_as=a, seat=k, rows=n) for (a, k), n in sorted(filed.items(), key=lambda kv: -kv[1])],
        not_read=[dict(n=r["n"], seat=r.get("seat"), date=r["date"], item=r["item"][:90], says=re.sub(r"\*", "", r["disposition"])[:80])
                  for r in RW if r["klass"] == "not read"],
        other=[dict(n=r["n"], seat=r.get("seat"), leads_with=re.sub(r"\*", "", r["disposition"])[:60]) for r in RW if r["klass"] == "other"],
        differed=[dict(n=r["n"], seat=r.get("seat"), item=r["item"][:70]) for r in RW if r["klass"] == "differed"],
        working=list(WORKING),
        flagged=[dict(n=n, reader=g, seat=R[n].get("seat"), klass=R[n]["klass"], date=R[n]["date"], item=R[n]["item"][:150],
                      carried_by=sorted(set(re.findall(r"P-\d{3,4}", R[n]["disposition"] + " " + R[n]["item"] + " " + R[n]["arc"]))))     # corrected 2026-11-12 (Review 79): the cell for main's arc, where main writes the register row, was not read; ids were cut at three digits; the list was cut at six
                 for g, rows_ in flagged().items() for n in rows_ if n in R])


def plain(s):
    """an item's text as it goes on the page: a path it names is on a seat's branch, not on main, so it is not marked as code"""
    return s.replace("|", "/").replace("`", "")


def page(B):
    T = B["totals"]; L = []
    L += ["# The seats, as the record holds them", "",
          "*Generated by `verification/build_seats.py` from the harvest ledger as it stood on main at `%s`: %d rows, the last numbered %d. "
          "Not to be edited by hand. Every number is recomputed from that commit by the lock.*" % (B["as_of"][:9], B["rows"], B["last_row"]), "",
          "## What became of what the seats sent", "",
          "| outcome | rows | what it means |", "|---|---|---|"]
    for k in ORDER:
        L.append("| %s | %d | %s |" % (k, T[k], MEANS[k]))
    L += ["| **all** | **%d** | |" % B["rows"], "",
          "So main has recomputed %d of the %d items (%d%%). The rest it has read, registered or closed, and %d it has not read."
          % (T["verified"] + T["differed"], B["rows"], round(100 * (T["verified"] + T["differed"]) / B["rows"]), T["not read"]), "",
          "## Seat by seat", "",
          "| seat | state | rows | verified | differed | read | registered | closed by triage | not read | other | recomputed | from | to |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    def line(s):
        c = s["by_class"]
        return "| %s | %s | %d | %d | %d | %d | %d | %d | %d | %d | %s | %s | %s |" % (
            s["name"], s["state"], s["rows"], c["verified"], c["differed"], c["read"], c["registered"], c["closed by triage"], c["not read"], c["other"],
            ("%d%%" % round(100 * s["recomputed_share"])) if s["rows"] else "", s["first"] or "", s["last"] or "")
    for s in sorted(B["seats"], key=lambda s: (s["key"] not in B["working"], -s["rows"])):
        if s["rows"] or s["key"] in B["working"]:
            L.append(line(s))
    none = [s["name"] for s in B["seats"] if not s["rows"]]
    L += ["", "No row is filed under: %s." % "; ".join(none) if none else "", "",
          "**The classes read a row's leading words only.** A row that begins READ may go on to say that main reproduced part of the item. Most rows of "
          "the advisor seat and of the agy lane are of that kind, so for them the share recomputed is a floor.", "",
          "**How main reads a working seat.** " + " ".join("%s: %s." % (s["name"].capitalize(), s["reads"]) for s in B["seats"] if s["key"] in B["working"]), "",
          "## Rows filed under a name that matches no registered seat, or more than one, sorted by main", "",
          "| filed as | sorted to | rows |", "|---|---|---|"]
    names = {s["key"]: s["name"] for s in B["seats"]}
    for x in B["sorted_by_main"]:
        L.append("| %s | %s | %d |" % (x["filed_as"], names.get(x["seat"], x["seat"]), x["rows"]))
    L += ["", "Rows that no seat claims: %d. Rows that two seats claim: %d." % (len(B["rows_no_seat_claims"]), len(B["rows_two_seats_claim"])), "",
          "## The %d rows main recomputed and found to differ" % len(B["differed"]), "",
          "| row | seat | item |", "|---|---|---|"]
    for x in B["differed"]:
        L.append("| %d | %s | %s |" % (x["n"], names.get(x["seat"], x["seat"]), plain(x["item"])))
    L += ["", "## The %d rows not read" % len(B["not_read"]), "",
          "| row | seat | dated | item | the row says |", "|---|---|---|---|---|"]
    for x in B["not_read"]:
        L.append("| %d | %s | %s | %s | %s |" % (x["n"], names.get(x["seat"], x["seat"]), x["date"], plain(x["item"]), plain(x["says"])))
    L += ["", "## The %d rows whose leading word is outside the classes" % len(B["other"]), "",
          "| row | seat | leads with |", "|---|---|---|"]
    for x in B["other"]:
        L.append("| %d | %s | %s |" % (x["n"], names.get(x["seat"], x["seat"]), plain(x["leads_with"])))
    L += ["", "## The %d rows the five readers flagged as not used and possibly important" % len(B["flagged"]), "",
          "A reader's flag is a pointer, not a judgement of main's. The last column lists the register rows the harvest row itself names, where it names any.", "",
          "| row | seat | outcome | dated | item, as main registered it | register rows it names |", "|---|---|---|---|---|---|"]
    for x in sorted(B["flagged"], key=lambda x: (x["seat"] or "", x["n"])):
        L.append("| %d | %s | %s | %s | %s | %s |" % (x["n"], names.get(x["seat"], x["seat"]), x["klass"], x["date"], plain(x["item"]), ", ".join(x["carried_by"]) or "none"))
    return "\n".join(L).rstrip() + "\n"


if __name__ == "__main__":
    if "--write" in sys.argv:
        commit = sys.argv[sys.argv.index("--write") + 1]
        commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", commit], capture_output=True, text=True).stdout.strip()
        B = build(commit)
        (ARC / "SEATS.json").write_text(json.dumps(B, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        (ARC / "SEATS.md").write_text(page(B), encoding="utf-8")
    old = json.loads((ARC / "SEATS.json").read_text(encoding="utf-8"))
    B = build(old["as_of"])
    same = json.loads(json.dumps(B, ensure_ascii=False)) == old and page(B) == (ARC / "SEATS.md").read_text(encoding="utf-8")
    print("as of main at %s: %d rows, the last numbered %d" % (B["as_of"][:9], B["rows"], B["last_row"]))
    print("by outcome:", B["totals"])
    print("rows no seat claims: %d; rows two seats claim: %d" % (len(B["rows_no_seat_claims"]), len(B["rows_two_seats_claim"])))
    for s in B["seats"]:
        if s["rows"]:
            print("  %-13s %4d  %s" % (s["key"], s["rows"], s["by_class"]))
    print("THE PAGES ARE WHAT THE BUILDER GIVES AT THAT COMMIT" if same else "THE PAGES DIFFER FROM WHAT THE BUILDER GIVES AT THAT COMMIT")
    sys.exit(0 if same and not B["rows_no_seat_claims"] and not B["rows_two_seats_claim"] else 1)
