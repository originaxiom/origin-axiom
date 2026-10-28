"""Referee B1799: read-outs from majorana_rows.jsonl (no frame value computed): the Majorana lightest states on B1792's
six carriers at the strip; the Dirac sector on lines of order 1 and 3 (B1703: protected there, N | 3)."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import json, pathlib
from collections import defaultdict
ARC = pathlib.Path(_ROOT + "/frontier/B1799_the_neutrinos_self_pairing_at_the_canonical_end/verification")
rows = [json.loads(l) for l in (ARC / "majorana_rows.jsonl").read_text().splitlines() if l.strip()]
CAR = {("2/5", "11/12"), ("2/5", "29/60"), ("2/5", "41/60"), ("2/5", "47/60"), ("2/5", "49/60"), ("2/5", "7/60")}
nn = {r["point"]: r["nucnuc"] for r in rows if "nucnuc" in r}
def lt(s): return {k: s[k][2] / s[k][0] for k in s if k.startswith("sv|")}
for nm in ("LL", "Lnuc"):
    v = [x for r in rows if r["point"] == "strip" and (r["a"], r["b"]) in CAR for x in lt(r[nm]).values()]
    print("%s on the six's carriers at the strip (24 values): sigma3/sigma1 %.2e - %.2e" % (nm, min(v), max(v)))
v = list(lt(nn["strip"]).values()); print("nucnuc at the strip: sigma3/sigma1 %.2e - %.2e (by reading/horocycle: %s)" % (min(v), max(v), {k: "%.1e" % x for k, x in lt(nn["strip"]).items()}))
for o in (1, 3):
    rs = [r for r in rows if r["order"] == o]
    print("Dirac on order-%d rows (%d): R1_rel max %.1e, |Y-Y^T|/|Y| max %.1e, Dn min %.2e" % (o, len(rs), max(r["Lnuc"]["R1_rel"] for r in rs), max(max(x for k, x in r["Lnuc"].items() if k.startswith("asym")) for r in rs), min(r["Lnuc"]["Dn"] for r in rs)))
sym = [(r["a"], r["b"]) for r in rows if r["point"] == "g1" and max(x for k, x in r["Lnuc"].items() if k.startswith("asym")) < 1e-12]
print("Dirac rows with a symmetric coupling at g1: %d lines %s" % (len(sym), sym[:8]))
