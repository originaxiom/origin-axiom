"""The SM seat's harvest review and its row listing (its branch at 386973969), held against main's ledger at f1efc59dd (the
commit it read).  Its generator is read as text, not run; the same rule is rebuilt here.
 L1  the rows of main's harvest ledger whose seat cell names the SM seat and whose disposition head (first 120 characters)
     says received, registered, owed or scheduled and not verified: their count, and whether its listing names exactly those
     rows, each with the same cut title and disposition head.
 L2  the rows its review names (1707, 1723, 1747, 1761, 1766, 1767, 1806, 1808, 1819, 1814, 1837) and their disposition heads;
     row 1831 (SM-C15 checked) and the SM-C18 records' verdicts."""
import re, json, subprocess
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
AT = "f1efc59dd"; rows = []
for l in git("show", AT + ":docs/HARVEST_LEDGER.md").split("\n"):
    if not l.startswith("| "): continue
    c = [x.strip() for x in l.split("|")]
    if len(c) < 8 or not c[1].isdigit() or "SM" not in c[2]: continue
    d = c[6]
    if any(k in d[:120] for k in ("RECEIVED", "REGISTERED", "OWED", "owed", "SCHEDULED")) and "VERIFIED" not in d[:120]:
        rows.append((int(c[1]), re.sub(r"\s+", " ", c[3][:70]).replace("|", "/").replace("`", ""), re.sub(r"\s+", " ", d[:110]).replace("|", "/").replace("`", "")))
listing = git("show", "386973969:relays/SM_HARVEST_UNVERIFIED_ROWS.md").split("\n")
listed = [tuple(x.strip() for x in l.strip("|").split(" | ")) for l in listing if re.match(r"\| \d+ \|", l)]
mine = [("%d" % n, t.strip(), d.strip()) for n, t, d in sorted(rows)]
print("L1: rows by the rule at %s: %d; its listing: %d rows; the same rows: %s; the same rows with the same cut texts: %s; its closing count line: %s"
      % (AT, len(rows), len(listed), [x[0] for x in listed] == [x[0] for x in mine], listed == mine, [l for l in listing if l.strip().endswith("rows.")]))
L = {int(c[1]): c for c in ([x.strip() for x in l.split("|")] for l in git("show", AT + ":docs/HARVEST_LEDGER.md").split("\n") if l.startswith("| ")) if len(c) > 7 and c[1].isdigit()}
print("L2: the rows its review names, disposition heads at %s: %s" % (AT, {n: L[n][6][:60] for n in (1707, 1723, 1747, 1761, 1766, 1767, 1806, 1808, 1819, 1814, 1837, 1831)}))
V = "frontier/B1957_the_seats_claims_register/verification/records/"
print("L2: the SM-C18 records' verdicts at %s: %s" % (AT, {f.split("/")[-1][:-5]: json.loads(git("show", AT + ":" + f))["verdict"] for f in git("ls-tree", "--name-only", AT, V).split() if "/sm-c18" in f}))
