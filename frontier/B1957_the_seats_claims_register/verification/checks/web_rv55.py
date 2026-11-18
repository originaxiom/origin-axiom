"""B1957: the web seat's own reading of main's second reading (its relays/chat1_2026-11-18_rv55/rv55_findings.md at
6db7ccca0: 325 rows, each naming a unit, a finding, its evidence and a suggested verdict) and what main did with each row
(second_reading/web_rv55.json).  Nothing of the seat's is run; its findings file is read as text from its branch.
 R1  every unit of the list carries now the verdict the list says main gave it.
 R2  for the rows main restored to VERIFIED, the files of main's the row cites: how many resolve to one file of main's,
     how many cited lines exist, and in how many rows every figure of the unit's text that is not a line number stands in
     a cited file of main's or in the record's ground.  A row that fails this is listed: main read it by its reasoning."""
import json, pathlib, re, glob, collections, subprocess
HERE = pathlib.Path(__file__).resolve().parent; V = HERE.parent; ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
L = json.loads((V / "second_reading" / "web_rv55.json").read_text()); owner = {}; recs = {}
for q in (V / "records").glob("web-*.json"):
    d = json.loads(q.read_text()); recs[d["id"]] = d
    for u in d.get("units", []): owner[u] = d
bad = [e["unit"] for e in L["entries"] if owner.get(e["unit"], {}).get("verdict") != e["verdict_after"]]
print("R1: rows %d, units %d, by main's action %s; units whose record's verdict is not the list's: %d" % (L["rows"], L["units"], dict(sorted(L["by_action"].items())), len(bad)))
units = {u[0]: u for u in json.loads((V / "UNITS.json").read_text())["units"]}
text = {}
for f in set(u.rsplit(":", 1)[0] for u in owner):
    pass
index = collections.defaultdict(list)
for f in glob.glob(str(ROOT / "frontier/**/*.py"), recursive=True) + glob.glob(str(ROOT / "frontier/**/*.txt"), recursive=True) + glob.glob(str(ROOT / "frontier/**/*.json"), recursive=True) + glob.glob(str(ROOT / "frontier/**/*.md"), recursive=True) + glob.glob(str(ROOT / "docs/*.md")) + glob.glob(str(ROOT / "tests/*.py")) + glob.glob(str(ROOT / "scripts/**/*.py"), recursive=True):
    if "/records/" not in f and "__pycache__" not in f: index[pathlib.Path(f).name].append(f)
seat = subprocess.run(["git", "show", "6db7ccca0:relays/chat1_2026-11-18_rv55/rv55_findings.md"], capture_output=True, text=True, cwd=ROOT).stdout.split("\n")
seat_text = {}
for n, l in enumerate(seat, 1): seat_text[n] = l
figs = lambda s: {x.rstrip(".,") for x in re.findall(r"\d[\d,]*\.\d+(?:e-?\d+)?|\d+\.\d+|\d{2,}[\d,]*", s)}
rest, ok_rows, files_ok, lines_ok, lines_all = [], 0, 0, 0, 0
restored = [e for e in L["entries"] if e["main"] == "V"]
for e in restored:
    names = re.findall(r"([A-Za-z0-9_]+\.(?:py|json|txt|md))", e["seat_evidence"]); found = [index[n][0] for n in names if len(index.get(n, [])) == 1]
    found += [index[n.replace(".py", "_run.txt")][0] for n in names if n.endswith(".py") and len(index.get(n.replace(".py", "_run.txt"), [])) == 1]          # a script's committed run
    files_ok += bool(found)
    for m in re.finditer(r"([A-Za-z0-9_]+\.(?:py|json|txt|md))[^;|]{0,30}?l\.? ?(\d+)", e["seat_evidence"]):
        lines_all += 1
        if len(index.get(m.group(1), [])) == 1 and int(m.group(2)) <= len(pathlib.Path(index[m.group(1)][0]).read_text(errors="replace").split("\n")): lines_ok += 1
    hay = " ".join(pathlib.Path(f).read_text(errors="replace") for f in found) + " " + owner.get(e["unit"], {}).get("how", "") + " " + " ".join(recs.get(e["record"], {}).get("how", "") for _ in [0])
    utext = seat_text.get(0, "")
    ev = re.sub(r"(?:\bl\.? ?|\blines? |:|§ ?|\bB|\bP-|\bM|\brow |\brows |\bC|\bS|\b[a-z]+-[a-z0-9]+-)\d+(?:[-/–]\d+)*(?:, ?\d+(?:[-/–]\d+)*)*", " ", e["seat_evidence"])      # line refs, arcs, rows, ids
    ev = re.sub(r"\b[0-9a-f]{9}\b", " ", ev)                                                          # commits
    want = figs(ev)
    for b in set(re.findall(r"\bB(\d{3,4})\b", e["seat_evidence"])):                                   # the arcs a row cites: their pages are main's too
        for f in glob.glob(str(ROOT / ("frontier/B%s_*/FINDINGS.md" % b))) + glob.glob(str(ROOT / ("frontier/B%s_*/verification/**/*run*.txt" % b)), recursive=True): hay += " " + pathlib.Path(f).read_text(errors="replace")
    if all(w in hay or w.replace(",", "") in hay for w in want): ok_rows += 1
    else: rest.append((e["row"], sorted(w for w in want if w not in hay and w.replace(",", "") not in hay)[:4]))
print("R2: rows restored to verified: %d; citing a file of main's that resolves: %d; cited lines that exist: %d of %d; rows whose every evidence figure stands in a cited file or the ground: %d; the rest, read by main by their reasoning: %d %s"
      % (len(restored), files_ok, lines_ok, lines_all, ok_rows, len(rest), rest[:12]))
