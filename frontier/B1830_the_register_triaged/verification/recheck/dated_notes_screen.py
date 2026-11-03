"""S297, second screen: LAW_MAP rows whose headline arc carries a dated note (Sharpened / Scoped / Dated note / Corrected /
Withdrawn, dated) that the row does not show. Benign note families (P-436's input-ledger note) excluded."""
import glob, json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
dirs = {pathlib.Path(f).name.split("_")[0]: pathlib.Path(f) for f in glob.glob(str(ROOT / "frontier/B*_*"))}
NOTE = re.compile(r"^>?\s*\*?\*?(Sharpened|Scoped|Dated note|Corrected|Correction|Withdrawn|Retracted|Narrowed)[^\n]{0,40}20\d\d-\d\d-\d\d", re.I | re.M)
law = (ROOT / "docs/LAW_MAP.md").read_text(encoding="utf-8").splitlines()
done = {50, 150, 154, 164, 172, 234, 256, 293, 298, 305, 322, 329, 330, 334, 335, 344}
hits = []
for n, l in enumerate(law, 1):
    if not l.startswith("| **") or n in done: continue
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
