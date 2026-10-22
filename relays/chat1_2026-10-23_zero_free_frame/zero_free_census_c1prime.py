#!/usr/bin/env python3
"""POST HOC control, labelled (written after zero_free_census_controls.json was read): C1 as written compared the
mixing at the sealed census's first three stored rows, which lie on the trivial line (0, 0). There Y_up = Y_down, so
V = 1 and |V_us|, |V_cb|, |V_ub| are rounding noise near 1e-16; its 1.05 in log10 is that noise (every ratio agreed).
C1': the same comparison at three census rows on non-trivial lines (the census's best six-row line (2/5, 1/10) at
0.4 + 2.7i, and two lines of order 7 and 12), every field: ratios and |V| in log10, J absolutely.
    python3 -B zero_free_census_c1prime.py      # writes zero_free_census_c1prime.json"""
import contextlib, importlib.util, io, json, math, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("zfc", HERE / "zero_free_census.py")
zfc = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(zfc)
want = {"(2/5, 1/10)": (0.4, 2.7), "(2/7, 3/7)": (0.1, 3.1), "(5/12, 7/12)": (0.4, 2.3)}
rows = {}
for l in (HERE.parent / "chat1_2026-10-22_selection_map" / "two_ingredients_census.jsonl").read_text().splitlines():
    r = json.loads(l); name = zfc.LINES[r["line"]][2]
    if name in want and (r["Re_tau"], r["Im_tau"]) == want[name]:
        rows[name] = r
out = {"rows found": sorted(rows)}
dr = dv = dj = 0.0
for name, r in rows.items():
    k, re_t, im_t = r["line"], r["Re_tau"], r["Im_tau"]
    a, b, _ = zfc.LINES[k]
    x = zfc.rows_at(zfc.rbs.channels(re_t, im_t, a, b), zfc.direction("dR", re_t, im_t))
    for ih, hor in enumerate(zfc.rbs.HORS):
        j = 0
        for sec in ("up", "down", "lep"):
            for rd in ("S", "St"):
                for q in range(2):
                    dr = max(dr, abs(x[ih, j] - math.log10(r[f"{sec}|{hor}|{rd}"][q]))); j += 1
        for ru, rd in (("S", "S"), ("S", "St"), ("St", "S"), ("St", "St")):
            ref = r[f"ckm|{hor}|{ru}|{rd}"]
            dv = max(dv, max(abs(math.log10(x[ih, j + q] / ref[q])) for q in range(3))); dj = max(dj, abs(x[ih, j + 3] - ref[3])); j += 4
out.update({"C1' max |delta log10| ratios": dr, "C1' max |delta log10| |V|": dv, "C1' max |delta J|": dj})
print(json.dumps(out, indent=1))
(HERE / "zero_free_census_c1prime.json").write_text(json.dumps(out, indent=1) + "\n")
