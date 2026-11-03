"""S297: the class of the LAW_MAP 334 miss -- a law-map row whose cited arc carries a later correction the row does not show.
Three screens, data-free: (1) the cited arc's verdict file says RETRACTED / SUPERSEDED / has superseded_by; (2) the arc is
named in RETRACTIONS.md; (3) the arc's FINDINGS carries a correction marker. A hit is printed only if the row itself shows
no sign of the correction."""
import glob, json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
V = {}
for f in glob.glob(str(ROOT / "frontier/*/arc_verdict.json")):
    try: v = json.loads(pathlib.Path(f).read_text(encoding="utf-8"))
    except Exception: continue
    V[v.get("id")] = (v, pathlib.Path(f).parent)
retr = (ROOT / "docs/RETRACTIONS.md").read_text(encoding="utf-8") if (ROOT / "docs/RETRACTIONS.md").exists() else ""
retr_rows = [l for l in retr.splitlines() if l.startswith("| ")]
MARK = re.compile(r"unearned|withdrawn|\bRETRACTED\b|retract(ed|ion)|not a law|overclaim|overst|\bwrong\b|refuted|superseded|"
                  r"Correction|CORRECTED|does not hold|fails (at|on|for)|scoped (since|to)|property of the median", re.I)
ROWOK = re.compile(r"correct|retract|scoped|scope|dated|unearned|withdrawn|supersed|refut|S2\d\d|\(20\d\d-\d\d-\d\d|NEGATIVE|not a law|overst|median", re.I)
law = (ROOT / "docs/LAW_MAP.md").read_text(encoding="utf-8").splitlines()
hits = []
for n, l in enumerate(law, 1):
    if not l.startswith("| **"): continue
    arcs = sorted(set(re.findall(r"\bB(\d{3,4})\b", l)), key=int)
    for a in arcs:
        aid = "B" + a
        if aid not in V: continue
        v, d = V[aid]; why = []
        verd = str(v.get("verdict") or v.get("status") or "")
        if re.search(r"RETRACT|SUPERSED|WITHDRAWN", verd, re.I) or v.get("superseded_by"): why.append("verdict:" + verd[:30] + (" sup_by" if v.get("superseded_by") else ""))
        rr = [r for r in retr_rows if re.search(r"\b%s\b" % aid, r)]
        if rr: why.append("RETRACTIONS x%d" % len(rr))
        fd = d / "FINDINGS.md"
        if fd.exists():
            ms = [m.group(0) for m in MARK.finditer(fd.read_text(encoding="utf-8"))]
            if ms: why.append("findings:" + ",".join(sorted(set(x.lower() for x in ms)))[:80])
        if why: hits.append((n, aid, why, bool(ROWOK.search(l)), l[:160]))
strong = [h for h in hits if any(w.startswith(("verdict", "RETRACTIONS")) for w in h[2])]
print("law rows:", sum(l.startswith("| **") for l in law), "; (row, arc) hits:", len(hits), "; strong (verdict or RETRACTIONS):", len(strong))
for h in strong: print("%4d %-6s %-40s rowshows=%s  %s" % (h[0], h[1], h[2], h[3], h[4][:110]))
print("\nfindings-marker only, row shows nothing:")
for h in hits:
    if h not in strong and not h[3]: print("%4d %-6s %s  %s" % (h[0], h[1], h[2], h[4][:100]))
