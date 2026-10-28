"""P-283 (data-free): the neutrino's self-pairings at B1667's canonical end in B1656's frame.  The Majorana pairings
nu^c nu^c (6Y 0, 0; line-free) and L L (-3, -3; the Weinberg operator's pair, partner H H of 6Y 6), against the Dirac
L nu^c (-3, 0), on B1795's 286 lines at its three points, through B1795's sector() (B1726's compute() path; the partner
typed as the frame's Higgs section, S and S~).  Per sector: R1 (the "1"-channel residue), Dn (B1716's det M, normalised),
the coupling's symmetry |Y - Y^T|/|Y|, the spectrum at both horocycles and readings.  Run only after B1795's sealed run.
    python3 -B majorana.py [--workers 8]   -> majorana_rows.jsonl, majorana.json, majorana_run.txt"""
import sys, json, math, argparse, importlib.util, pathlib
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
spec = importlib.util.spec_from_file_location("split", ROOT / "frontier" / "B1795_the_doublet_triplet_split_at_the_canonical_end" / "verification" / "split.py")
SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
HERE = pathlib.Path(__file__).resolve().parent
SECT = {"nucnuc": (0, 0), "LL": (-3, -3), "Lnuc": (-3, 0)}


def sym(t, w, ql, qr, S, Ls):
    B = SP._modules()["B"]
    x, y = B.sector_twists(w, t, ql, qr); R = B.residues(x, y, t); c = B.cA(x, y, t, R); out = {}
    for h, L in Ls.items():
        u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
        Mw = B.weighted_M(u)
        for rn, Sx in S.items():
            Y = B.coupling(Sx, Mw); out["asym|%s|%s" % (h, rn)] = float(np.linalg.norm(Y - Y.T) / np.linalg.norm(Y))
    return out


def task(job):
    k, pk = job
    a, b = SP.lines()[k]; re_t, im_t = SP.POINTS[pk]; t = complex(re_t, im_t); w = float(a) * t + float(b)
    S = SP.higgs(t); Ls = SP.Ls_at(im_t)
    r = {"line": k, "a": str(a), "b": str(b), "order": SP.order(a, b), "point": pk}
    for nm, (ql, qr) in SECT.items():
        if nm == "nucnuc" and k > 0: continue                    # line-free: computed once per point, on line 0
        r[nm] = SP.sector(t, w, ql, qr, S, Ls); r[nm].update(sym(t, w, ql, qr, S, Ls))
    return r


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--workers", type=int, default=1); args = ap.parse_args()
    RJ = HERE / "majorana_rows.jsonl"; done = set()
    if RJ.exists():
        for l in RJ.read_text(encoding="utf-8").splitlines():
            if l.strip(): r = json.loads(l); done.add((r["line"], r["point"]))
    jobs = [(k, pk) for k in range(len(SP.lines())) for pk in SP.POINTS if (k, pk) not in done]
    with open(RJ, "a", encoding="utf-8") as fh:
        if args.workers > 1:
            import multiprocessing as mpc
            with mpc.get_context("fork").Pool(args.workers) as pool:
                for r in pool.imap_unordered(task, jobs, chunksize=2): fh.write(json.dumps(r, default=str) + "\n"); fh.flush()
        else:
            for j in jobs: fh.write(json.dumps(task(j), default=str) + "\n"); fh.flush()
    rows = sorted((json.loads(l) for l in RJ.read_text(encoding="utf-8").splitlines() if l.strip()), key=lambda r: (r["line"], r["point"]))
    def zero(s): return s["Dn"] < 1e-10
    out = {"rows": len(rows)}
    for nm in SECT:
        ss = [r[nm] for r in rows if nm in r]
        out[nm] = {"n": len(ss), "max_R1_rel": max(s["R1_rel"] for s in ss), "min_Dn": min(s["Dn"] for s in ss),
                   "exact_zero_rows": sum(zero(s) for s in ss),
                   "max_asym": max(max(v for k, v in s.items() if k.startswith("asym")) for s in ss),
                   "min_sv3_over_sv1": min(min(s[k][2] / s[k][0] for k in s if k.startswith("sv|")) for s in ss)}
    (HERE / "majorana.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    txt = ["P-283 majorana.py: %d rows" % len(rows)] + ["%s: %s" % (k, v) for k, v in out.items() if k != "rows"] + ["majorana exit 0"]
    (HERE / "majorana_run.txt").write_text("\n".join(txt) + "\n", encoding="utf-8"); print("\n".join(txt))


if __name__ == "__main__":
    main()
