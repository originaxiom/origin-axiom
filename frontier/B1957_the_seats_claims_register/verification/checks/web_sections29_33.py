"""The web seat's sections 29 to 33 (its status page at 2f656508b, each section in its read version): the statements it
makes about main's register, held against the register at the head each section names (git show <head>:...).
Nothing of the seat's is run.
 L1  the lane's counts at 1b6df9753 (29.1), 23b205b21 (30.1), f9818b66b (31.1), c6d3847f7 (32.1) and a6c922f88 (33.1),
     from SUMMARY.json at that head: files, units, statements, the six verdicts, none pending
 L2  29.1: the 1,248 statements of the older deliveries, 7 VERIFIED (web-old-01), 1,210 CONDITIONAL (web-old-02) and
     31 NOTED (web-old-03), at 1b6df9753
 L3  30.1: main's records of section 28 at 23b205b21: web-st28-01 VERIFIED (33), -02 PARTIAL (6), -03 CONDITIONAL (31),
     -04 NOTED (25)
 L4  32.1: the ledger-and-JUNO relay at c6d3847f7: 51 statements, 33 CONDITIONAL, 3 PARTIAL and 15 NOTED
 L5  29.3: at 1b6df9753 the attack note held 50 CONDITIONAL and none verified, the pair sums 216 CONDITIONAL and 1 VERIFIED,
     the first background 26 CONDITIONAL
    python3 -B web_sections29_33.py > web_sections29_33_run.txt"""
import json, subprocess, collections
V = "frontier/B1957_the_seats_claims_register/verification"
show = lambda h, p: subprocess.run(["git", "show", "%s:%s" % (h, p)], capture_output=True, text=True).stdout


def lane(h):
    s = json.loads(show(h, V + "/SUMMARY.json"))["lanes"]["web"]
    return {k: s.get(k) for k in ("files", "units", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")}


def units_of(h, rid):
    t = show(h, V + "/records/%s.json" % rid)
    return json.loads(t)["units"] if t else None


def verdict_counts(h, prefix, file_prefix):
    """statements of one file by their record's verdict, at head h"""
    U = json.loads(show(h, V + "/UNITS.json"))["units"]
    st = {u[0] for u in U if u[0].startswith(file_prefix) and u[2] == "s"}
    names = subprocess.run(["git", "ls-tree", "--name-only", h, V + "/records/"], capture_output=True, text=True).stdout.split()
    c = collections.Counter()
    for d in batch(h, names):                                        # one git process per head (was one per record)
        c[d.get("verdict")] += sum(1 for u in d.get("units", []) if u in st)
    return len(st), dict(c)


_BATCH = {}
def batch(h, names):
    """every record at head h, parsed, read through one git cat-file --batch"""
    if h not in _BATCH:
        out = subprocess.run(["git", "cat-file", "--batch"], input="".join("%s:%s\n" % (h, n) for n in names).encode(), capture_output=True).stdout
        recs, i = [], 0
        while i < len(out):
            j = out.index(b"\n", i); head = out[i:j].split(); i = j + 1
            if len(head) < 3 or head[1] != b"blob": continue
            size = int(head[2]); body = out[i:i + size]; i += size + 1
            try: recs.append(json.loads(body.decode("utf-8")))
            except Exception: pass
        _BATCH[h] = recs
    return _BATCH[h]


STATED = {"1b6df9753": (151, 10347, 9453, 2060, 3, 1374, 780, 59, 5177), "23b205b21": (153, 10646, 9736, 2101, 3, 1576, 790, 59, 5207),
          "f9818b66b": (153, 10646, 9736, 2240, 3, 1058, 808, 59, 5568), "c6d3847f7": (154, 10704, 9787, 2261, 3, 1068, 812, 60, 5583),
          "a6c922f88": (154, 10704, 9787, 2260, 3, 1048, 833, 60, 5583)}
ok = True
for h, st in STATED.items():
    l = lane(h); got = (l["files"], l["units"], l["statements"], l["VERIFIED"], l["REFUTED"], l["CONDITIONAL"], l["PARTIAL"], l["SUPERSEDED"], l["NOTED"])
    print("L1 %s: stated %s; register %s; pending %s; %s" % (h, st, got, l["PENDING"], "HOLDS" if got == st and l["PENDING"] == 0 else "DIFFERS"))
    ok &= got == st and l["PENDING"] == 0
n = [len(units_of("1b6df9753", r) or []) for r in ("web-old-01", "web-old-02", "web-old-03")]
print("L2 1b6df9753: web-old-01, -02, -03 hold %s units (stated 7, 1210, 31): %s" % (n, "HOLDS" if n == [7, 1210, 31] else "DIFFERS")); ok &= n == [7, 1210, 31]
m = [len(units_of("23b205b21", "web-st28-0%d" % i) or []) for i in (1, 2, 3, 4)]
print("L3 23b205b21: web-st28-01 to -04 hold %s units (stated 33, 6, 31, 25): %s" % (m, "HOLDS" if m == [33, 6, 31, 25] else "DIFFERS")); ok &= m == [33, 6, 31, 25]
tot, c = verdict_counts("c6d3847f7", "web-lbl-juno", "web:CHAT1_TO_CC_2026-10-24_THE_LEDGER_ROWS_AND_JUNO:")
good = tot == 51 and c.get("CONDITIONAL") == 33 and c.get("PARTIAL") == 3 and c.get("NOTED") == 15
print("L4 c6d3847f7: the ledger-and-JUNO relay has %d statements, by verdict %s (stated 51: 33 CONDITIONAL, 3 PARTIAL, 15 NOTED): %s" % (tot, c, "HOLDS" if good else "DIFFERS")); ok &= good
for name, pre, want in (("the attack note", "web:chat1_2026-10-23_attack/THE_NEXT_ATTACK:", {"CONDITIONAL": 50, "VERIFIED": 0}),
                        ("the pair sums", "web:CHAT1_TO_CC_2026-11-03_THE_CHANNEL_NORMS_PAIR_SUMS_AND_B1788S_HYPOTHESES:", {"CONDITIONAL": 216, "VERIFIED": 1}),
                        ("the first background", "web:chat1_2026-10-06_first_background/FINDINGS:", {"CONDITIONAL": 26})):
    tot, c = verdict_counts("1b6df9753", None, pre); good = all(c.get(k, 0) == v for k, v in want.items())
    print("L5 1b6df9753: %s: %d statements, by verdict %s (stated %s): %s" % (name, tot, {k: v for k, v in c.items() if v}, want, "HOLDS" if good else "DIFFERS")); ok &= good
print("ALL HOLD:", ok)
