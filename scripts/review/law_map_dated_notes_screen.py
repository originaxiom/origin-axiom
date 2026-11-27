"""LANDED 2026-11-27 (P-589, rule 9) from audit/drafts/register_triage/recheck/dated_notes_screen.py. Changed: its root, and
the skip-list of LAW_MAP line numbers judged at S297 is removed, since the rows have moved since; a row mended then shows
its note, which the row test below already reads.
S297, second screen: LAW_MAP rows whose headline arc carries a dated note (Sharpened / Scoped / Dated note / Corrected /
Withdrawn, dated) that the row does not show. Benign note families (P-436's input-ledger note) excluded."""
import glob, json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
dirs = {pathlib.Path(f).name.split("_")[0]: pathlib.Path(f) for f in glob.glob(str(ROOT / "frontier/B*_*"))}
NOTE = re.compile(r"^>?\s*\*?\*?(Sharpened|Scoped|Dated note|Corrected|Correction|Withdrawn|Retracted|Narrowed)[^\n]{0,40}20\d\d-\d\d-\d\d", re.I | re.M)
law = (ROOT / "docs/LAW_MAP.md").read_text(encoding="utf-8").splitlines()
hits = []
for n, l in enumerate(law, 1):
    if not l.startswith("| **"): continue
    title = l.split("|")[1]
    for a in sorted(set(re.findall(r"\bB(\d{3,4})\b", title)), key=int):
        d = dirs.get("B" + a)
        if not d or not (d / "FINDINGS.md").exists(): continue
        t = (d / "FINDINGS.md").read_text(encoding="utf-8")
        ms = [m for m in NOTE.finditer(t) if "P-436" not in t[m.start(): m.start() + 300]]
        if ms and not re.search(r"scoped|sharpened|corrected|dated|S2\d\d|20\d\d-\d\d-\d\d|RETRACT", l, re.I):
            hits.append((n, "B" + a, [t[m.start(): m.start() + 160].replace("\n", " ") for m in ms]))
print(len(hits), "rows")
for n, a, ms in hits:
    print("%4d %s" % (n, a)); [print("      " + m) for m in ms[:3]]
