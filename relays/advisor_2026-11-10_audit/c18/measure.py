#!/usr/bin/env python3
"""Card C18's measurement: the six historical folders and the ten copies of notes between sessions.

    python3 measure.py <a checkout>        # prints the measurement in Markdown

For each folder: its tracked files; the tracked code outside it that names a path in it (gates, tests, arcs' scripts,
other scripts, data the generators read), file by file; the seal files that name a path in it; and the tracked pages
outside it that cite a path in it, split into living pages and dated records. For each copy of a note: the code that
names it. A text search: a reader that builds a path at run time is not seen, and the move is to be tried on a clean
checkout with the full suite before it is sent (the card's point 1)."""
import os, re, subprocess, sys

root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
FOLDERS = ("legacy", "story", "philosophy", "speculations", "paths", "outside_bench")
NOTES = ("frontier/B702_metallic_hearing_law/CC2_TO_CC_2026-07-19_EQ_results.md",
         "frontier/B1297_the_spectral_cover_index/CC_TO_ALL_SEATS_2026-09-08_HARVEST_NUMBERING.md",
         "frontier/B1303_the_sm_closings_z_prime/CC_TO_CHAT1_2026-09-08_B1303_DISPOSITIONS_HELD.md",
         "frontier/B1303_the_sm_closings_z_prime/CHAT1_TO_CC_2026-09-08_SESSION_RELAY.md",
         "frontier/B1305_the_cloud_156_178/CC_TO_CLOUD_2026-09-08_Q1_ANSWERED_AND_SHARPENED_HELD.md",
         "frontier/B1306_the_older_debt/CC_TO_CHAT1_2026-09-09_HANDOFF_BANKED_HELD.md",
         "frontier/B1306_the_older_debt/CC_TO_SM_2026-09-09_THE_TOWER_HARVESTED_AND_THE_RANGES_HELD.md",
         "frontier/B1306_the_older_debt/inputs/chat1_handoff_2026-09-08/CHAT1_TO_CC_2026-09-08_HANDOFF_ARROW_CHIRALITY.md",
         "frontier/B1454_genesis_v1_verified_and_adopted/received/SM_TO_CC_2026-10-02_GENESIS_V1.md",
         "outside_bench/CLOUD_TO_CC_2026-09-08_Q1_THE_QUANTUM_FACE.md")
DATED = re.compile(r"^(frontier/|relays/|docs/progress/|docs/handoffs/|CHANGELOG\.md$|PROGRESS_LOG\.md$|docs/(POINT_REGISTER|HARVEST_LEDGER|"
                   r"RELAY_LEDGER|REORGANIZATIONS|CAMPAIGN_STATUS)\.md$)|\d{4}-\d{2}-\d{2}|/received/|_v\d")
CODE = (".py", ".sh", ".json", ".yml", ".yaml", ".toml", ".cfg", ".ini")


def tracked():
    out = subprocess.run(["git", "-C", root, "ls-files"], capture_output=True, text=True, check=True).stdout.split("\n")
    return [p for p in out if p]


def read(p):
    try:
        with open(os.path.join(root, p), encoding="utf-8", errors="ignore") as f:
            return f.read()
    except OSError:
        return ""


files = tracked()
texts = {p: read(p) for p in files if p.endswith(CODE + (".md", ".sha256", ".txt", ".tex"))}


def kind(p):
    if p.startswith("scripts/gates/"): return "gate"
    if p.startswith("tests/") or "/verification/test_" in p: return "test"
    if p.startswith("frontier/"): return "arc's script or data"
    if p.startswith("scripts/"): return "script"
    return "other"


print("# Card C18's measurement\n")
print("Made by `relays/advisor_2026-11-10_audit/c18/measure.py` on the checkout given; a text search for each folder's name"
      " followed by a slash.\n")
print("| folder | tracked files | code outside it that names a path in it | seal files naming it | pages citing it: living / dated |")
print("|---|---|---|---|---|")
detail = []
for d in FOLDERS:
    mine = [p for p in files if p.startswith(d + "/")]
    pat = re.compile(r"(?<![\w/.-])%s/" % re.escape(d))
    code = sorted(p for p, t in texts.items() if not p.startswith(d + "/") and p.endswith(CODE) and pat.search(t))
    seals = sorted(p for p, t in texts.items() if p.endswith(".sha256") and pat.search(t))
    pages = [p for p, t in texts.items() if not p.startswith(d + "/") and p.endswith((".md", ".tex")) and pat.search(t)]
    dated = [p for p in pages if DATED.search(p)]
    living = sorted(set(pages) - set(dated))
    print("| `%s/` | %d | %d | %d | %d / %d |" % (d, len(mine), len(code), len(seals), len(living), len(dated)))
    detail.append((d, code, seals, living))
print()
for d, code, seals, living in detail:
    print("## `%s/`\n" % d)
    if code:
        print("Code that names a path in it, by kind:\n")
        for k in ("gate", "test", "script", "arc's script or data", "other"):
            ks = [p for p in code if kind(p) == k]
            if ks:
                print("- %s (%d): %s" % (k, len(ks), ", ".join("`%s`" % p for p in ks[:12]) + (" …" if len(ks) > 12 else "")))
        print()
    if seals:
        print("Seal files naming it: " + ", ".join("`%s`" % p for p in seals) + "\n")
    if living:
        print("Living pages citing it (%d): " % len(living) + ", ".join("`%s`" % p for p in living[:20]) + (" …" if len(living) > 20 else "") + "\n")
print("## The ten copies of notes between sessions\n")
print("| copy | tracked | code that names it |")
print("|---|---|---|")
for n in NOTES:
    base = os.path.basename(n)
    code = sorted(p for p, t in texts.items() if p.endswith(CODE) and base in t)
    print("| `%s` | %s | %s |" % (n, "yes" if n in files else "NO", ", ".join("`%s`" % p for p in code) or "—"))
