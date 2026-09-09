"""B1307 section 3, Route A -- the sense census's third pre-registration: the SELF-NAMING EXCLUSION.
Runs B1305's independent implementation of the cloud's memo 172 instrument unchanged, except that every prose file whose
text names the instrument (/sense[ _-]?census/i) is excluded from the scanned set -- computed at run time, never hard-coded,
so a future mention excludes itself. Prints the excluded files, the seven-term table, the two-sided control and the three
planted MB12 controls. PASS (pre-registered) = two-sided PASSED and planted PASS. Usage: sense_census_third.py <tree-root>"""
import importlib.util, json, os, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC = ROOT / "frontier" / "B1305_the_cloud_156_178" / "verification" / "b1305_sense_census.py"
spec = importlib.util.spec_from_file_location("b1305sc", SRC); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
NAME_RE = re.compile(r"sense[ _-]?census", re.I)
_orig = m.prose
def prose(root):
    kept, excl = [], []
    for f in _orig(root):
        try: txt = open(f, encoding="utf-8", errors="replace").read()
        except OSError: continue
        (excl if NAME_RE.search(txt) else kept).append(f)
    prose.excluded = sorted(os.path.relpath(f, root) for f in excl)
    return kept
prose.excluded = []
m.prose = prose
if __name__ == "__main__":
    root = sys.argv[1]
    res = m.census(root); okp, okn = m.two_sided(res); excluded = list(prose.excluded)
    print(f"tree {root}: {res['files']} prose files scanned, {res['mb']} MB; self-naming exclusion removed {len(excluded)} file(s):")
    for e in excluded: print(f"    - {e}")
    for term, v in res["terms"].items():
        print(f"  {term:<16}{v['occurrences']:>8}{v['technical']:>8} ({v['frac']*100:5.1f}%)  {v['verdict']}" + (f"   [{v['kind']}]" if v["kind"] else ""))
    print(f"  CONTROL + (Chern-Simons genuine): {'PASS' if okp else 'FAIL'};  CONTROL - (logarithmic, non-semisimple false comfort): {'PASS' if okn else 'FAIL'};  TWO-SIDED: {'PASSED' if okp and okn else 'FAILED'}")
    pl = m.planted(root)
    print(f"  PLANTED CONTROLS: +1 technical with marker: {pl['technical_marker']['technical'] - pl['base']['technical']}; no marker: +{pl['no_marker']['technical'] - pl['base']['technical']}; marker outside window: +{pl['marker_outside_window']['technical'] - pl['base']['technical']}  -> {'PASS' if pl['ok'] else 'FAIL'}")
    verdict = "PASS" if (okp and okn and pl["ok"]) else "FAIL"
    print(f"  ROUTE A (self-naming exclusion) PRE-REGISTERED VERDICT: {verdict}")
    json.dump(dict(root=root, excluded=excluded, census=res, two_sided=okp and okn, planted=pl, verdict=verdict),
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sense_census_routeA.json"), "w"), indent=1)
