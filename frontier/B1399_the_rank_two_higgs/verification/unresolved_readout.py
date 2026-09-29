#!/usr/bin/env python3
"""B1399 -- POST-SEAL read-out of the seven unresolved members (not part of the sealed verdict; they do not count toward NONE).

For each member the sealed pipeline left unresolved, every rung of the ladder is solved again with both sample seeds and each seed's
forms are read ON THEIR OWN, without the two-seed agreement: the leading shells (for an ambiguous kill, both readings -- the shell
killed and the shell leading), C on V's circle, its maximum |C|, its total variation, and the g it realises with that seed alone (the
same exact linear programs, re-verified with that seed's forms).  This bounds what the unresolved members could hide; it decides
nothing about the sealed prediction.  Usage: python3 unresolved_readout.py"""
import importlib.util
import json
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("b1399_rank_two_higgs", HERE / "rank_two_higgs.py")
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)


def leading_options(shells):
    """the sealed leading shell, or -- where the kill is ambiguous -- both readings"""
    norms = [float(np.linalg.svd(R.real_map(Mj), compute_uv=False)[0]) for _, _, Mj in shells]
    top = max(norms)
    opts = []
    for j, nj in enumerate(norms):
        r = nj / top
        if r < R.AMB_LO:
            continue
        if r >= R.AMB_HI:
            opts.append(j)
            return opts, [round(n / top, 4) for n in norms]
        opts.append(j)                                               # ambiguous: this shell as leading, and the next reading
    return opts, [round(n / top, 4) for n in norms]


def read_seed(S, X):
    sh = R.shell_data(S, X)
    options = {c: leading_options(sh[c]) for c in sh}
    readings = [{}]
    for c, (opts, _) in options.items():
        readings = [{**rd, c: j} for rd in readings for j in opts]
    out = []
    for lead in readings:
        try:
            circ = R.circle(sh, lead, np.eye(2))
            mc = max(abs(x) for x in circ["vals"])
            tv = R.total_variation(circ)
            gs = [g for g in range(1, mc // 2 + 1) if tv >= 12 * g and R.realise([circ], g)["L"] is not None]
            out.append(dict(lead={str(c): [j, len(sh[c][j][1])] for c, j in lead.items()}, breakpoints=len(circ["bps"]),
                            maxC=mc, total_variation=tv, values=sorted(set(circ["vals"])), g=gs))
        except R.Unresolved as e:
            out.append(dict(lead={str(c): [j, len(sh[c][j][1])] for c, j in lead.items()}, error=str(e)))
    return dict(norm_ratios={str(c): options[c][1] for c in options}, readings=out)


def main():
    rows = {}
    for line in open(HERE / "census_partial.jsonl"):
        r = json.loads(line)
        rows[r["label"]] = r
    unresolved = [r for r in rows.values() if r["status"] != "resolved"]
    report = []
    for r in sorted(unresolved, key=lambda r: r["label"]):
        t0 = time.time()
        M = R.manifold(r["label"])
        v, B, G = R.cuspidal_basis(M)
        entry = dict(label=r["label"], parent=r["parent"], degree=r["degree"], cusps=r["cusps"], dim=B.shape[0], reason=r.get("reason"), rungs=[])
        for Kn, tau in R.LADDER:
            for ss in R.SAMPLE_SEEDS:
                try:
                    S, X, st = R.solve_basis(M, v, B.shape[0], Kn, tau, R.CHART_SEED, ss)
                    rd = read_seed(S, X)
                    entry["rungs"].append(dict(Kn=Kn, tau=tau, seed=ss, accepted=R.accepted(st),
                                               fit=round(st["fit residual rms"], 6), test=round(st["test residual rms"], 6), **rd))
                except Exception as e:
                    entry["rungs"].append(dict(Kn=Kn, tau=tau, seed=ss, error=repr(e)[:160]))
        entry["seconds"] = round(time.time() - t0)
        report.append(entry)
        best = [(x.get("maxC"), x.get("total_variation"), x.get("g")) for rg in entry["rungs"] for x in rg.get("readings", [])]
        print("%s (parent %s, %d cusps): %s | per seed and reading (maxC, TV, g): %s" % (r["label"][:26], r["parent"], r["cusps"],
              r.get("reason"), best), flush=True)
    json.dump(report, open(HERE / "unresolved_readout.json", "w"), indent=1, default=float)
    return report


if __name__ == "__main__":
    main()
    print("DONE")
