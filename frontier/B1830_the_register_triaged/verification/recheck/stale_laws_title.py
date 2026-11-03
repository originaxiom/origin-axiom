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
out = []
TM = re.compile(r"unearned|withdrawn|not a law|does not hold|property of the median|overst\w*|\bRETRACTED\b", re.I)
for n, l in enumerate(law, 1):
    if not l.startswith("| **"): continue
    title = l.split("|")[1]
    for a in sorted(set(re.findall(r"\bB(\d{3,4})\b", title)), key=int):
        aid = "B" + a
        if aid not in V: continue
        v, d = V[aid]; why = []
        verd = str(v.get("verdict") or v.get("status") or "")
        if re.search(r"RETRACT|SUPERSED|WITHDRAWN", verd, re.I) or v.get("superseded_by"):
            why.append("verdict:%s%s" % (verd[:20], (" sup_by=" + str(v.get("superseded_by"))[:30]) if v.get("superseded_by") else ""))
        rr = [r for r in retr_rows if re.search(r"\b%s\b" % aid, r)]
        if rr: why.append("RETR x%d" % len(rr))
        fd = d / "FINDINGS.md"
        if fd.exists():
            ms = sorted(set(m.group(0).lower() for m in TM.finditer(fd.read_text(encoding="utf-8"))))
            if ms: why.append("F:" + ",".join(ms))
        if why: out.append((n, aid, why, bool(ROWOK.search(l)), title.strip()[:120]))
print(len(out), "title-arc hits;", sum(not o[3] for o in out), "with no correction shown in the row")
for o in out:
    if not o[3]: print("%4d %-6s %s\n      %s" % (o[0], o[1], o[2], o[4]))
json.dump(out, open(pathlib.Path(__file__).with_name("law_hits.json"), "w"), ensure_ascii=False)
