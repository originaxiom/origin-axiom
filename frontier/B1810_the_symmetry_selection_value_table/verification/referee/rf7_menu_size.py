"""rf7: the table's effective menu (distinct output vectors after floating-point zeros are set to 0 and values rounded to
5 significant digits), per configuration and in all; with and without the lepton ratios; and the distinct nontrivial
angles among the 40 exceptions."""
import json, collections, math, pathlib
from rf_common import ROOT
rows = json.load(open(pathlib.Path(__file__).resolve().parents[1] / "symmetry_selection_table_second_launch.json"))["rows"]
def cl(x): return 0.0 if abs(x) < 1e-9 else float("%.5g" % x)
def vec(r, lep=True):
    v = [cl(x) for s in (("up", "down", "lepton") if lep else ("up", "down")) for x in r[s]]
    return tuple(v + ([cl(x) for x in r["|V_us|, |V_cb|, |V_ub|"]] if r["V defined"] else ["undef"]))
tot = set(); tot_nl = set()
for cfg in ("(i, 0)", "(omega, 0)", "(i, (1/2, 1/2))", "(omega, (1/3, 2/3))"):
    R = [r for r in rows if r["config"] == cfg]
    a = {vec(r) for r in R}; b = {vec(r, False) for r in R}; tot |= a; tot_nl |= b
    m = {tuple(cl(x) for s in ("up", "down", "lepton") for x in r[s]) for r in R}
    print("%-22s rows %3d  distinct mass patterns %3d  distinct outputs (masses+V) %3d  without leptons %3d" % (cfg, len(R), len(m), len(a), len(b)))
print("all configurations: distinct outputs %d (without leptons %d) of 512 rows" % (len(tot), len(tot_nl)))
exc = [r for r in rows if r["V defined"] and not all(min(abs(x), abs(1 - x)) < 1e-6 for x in r["|V_us|, |V_cb|, |V_ub|"])]
ang = collections.Counter((r["radius"], min(x for x in r["|V_us|, |V_cb|, |V_ub|"] if 1e-6 < x < 1 - 1e-6)) for r in exc)
print("exceptions:", len(exc), " distinct (radius, small nontrivial |V| entry):", len(ang))
for k, v in sorted(ang.items()): print("   ", k, "rows", v, " theta = %.4f rad" % math.asin(min(k[1], math.sqrt(1 - k[1] ** 2))))
