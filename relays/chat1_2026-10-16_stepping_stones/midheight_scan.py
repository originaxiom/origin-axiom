"""The per-field thread frame between the low threads and the deep tower (a scoreboard: the data were seen; no claim).

Every closing configuration (tlow_enum.py's rule: a line of exact order N in {9, 11, 12}, fixed up to sign, with
N^2 | Q) on Lyndon words of length <= 16 at height 3 < h <= 6, one representative per class of word reversal with the
L <-> R mirror (classes.py). For the Standard Model and the replication's 112 distinct nulls, the per-field masses in
the five cells, with the sealed instrument tlow2.py unchanged; the point count per period starts at 30 per unit
length and is doubled until every accepted cell's r_calc (largest |d ln s| between n and 1.25 n) is <= 1e-6. Then
S-mass exactly as the low-thread seal defined it. The question: does any assignment fit anywhere between the low
threads (sealed: none) and the deep tower (the 19:41 law: none)?
Usage: python3 -B midheight_scan.py <forms.pkl> > midheight_scan_run.txt   (writes midheight_scan.json)
"""
import json, math, os, pickle, sys, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
REP = os.path.join(HERE, "..", "chat1_2026-10-16_s_shape_replication")
TU = os.path.normpath(os.path.join(HERE, "..", "chat1_2026-10-15_route", "twisted_units"))
sys.path.insert(0, REP); sys.path.insert(0, TU)
from enumerate_fresh import configs
from classes import orbit
import s_shape_seal as S


def jobs_list():
    jobs = []
    for N in (9, 11, 12):
        rows = [r for r in configs(N, lmin=2, lmax=16, hmax=6.0) if r[1] > 3.0]
        cls = {}
        for w, h, key, eps in rows:
            cls.setdefault(orbit(w, key, N), []).append((w, h, key))
        for mem in sorted((sorted(m, key=lambda r: (r[0], r[2])) for m in cls.values()), key=lambda m: (m[0][0], m[0][2])):
            jobs.append({"N": N, "word": mem[0][0], "height": mem[0][1], "line": tuple(mem[0][2]), "members": len(mem)})
    for i, j in enumerate(jobs):
        j["index"] = i
    return jobs


def one(args):
    job, P = args
    import flint, mpmath as mp
    import tlow2 as T2
    t0 = time.time()
    try:
        N, word, line = job["N"], job["word"], job["line"]
        rot, M, rho, k, height = T2.thread_geometry(word)
        flint.ctx.prec = 800; F = T2.Forms(P).prepare(); flint.ctx.prec = T2.bits_for(height)
        a, b, c, d = M; Pl = 2 * math.acosh((a + d) / 2)
        A = S.assignments()
        npp = 30.0
        while True:
            n1, n2 = int(round(Pl * npp)), int(round(Pl * npp * 1.25))
            c1 = T2.configuration(F, word, line, N, A, n1, readings=("per-field",))
            c2 = T2.configuration(F, word, line, N, A, n2, readings=("per-field",))
            m1 = T2.masses(c1, F, A, N, mp); m2 = T2.masses(c2, F, A, N, mp)
            cells, worst = {}, 0.0
            for (name, reading, sec), cl in m1.items():
                for cell, dd in cl.items():
                    d2 = m2.get((name, reading, sec), {}).get(cell)
                    e = None
                    if dd is not None:
                        s = [float(x) for x in dd["s"]]
                        rc = None
                        if d2 is not None and min(s) > 0 and min(float(x) for x in d2["s"]) > 0:
                            rc = max(abs(math.log(s[i] / float(d2["s"][i]))) for i in range(3))
                            if min(s) > 1e-30 * max(s):
                                worst = max(worst, rc)
                        e = {"s": s, "r_calc": rc}
                    cells[f"{name}|{sec}|{cell}"] = e
            if worst <= 1e-6 or npp >= 240:
                break
            npp *= 2
        return {**{k_: (list(v) if isinstance(v, tuple) else v) for k_, v in job.items()}, "npp": npp, "bits": c1["bits"],
                "closure": {f"{t}|{k_}": v for (t, k_), v in c1["closure"].items()},
                "plan": {f"{a_}|{s_}": [list(v[0]), list(v[1])] for (a_, s_), v in c1["plan"].items()},
                "cells": cells, "seconds": round(time.time() - t0, 1)}
    except Exception as e:
        return {**{k_: (list(v) if isinstance(v, tuple) else v) for k_, v in job.items()}, "error": repr(e), "cells": {},
                "closure": {}, "plan": {}, "seconds": round(time.time() - t0, 1)}


if __name__ == "__main__":
    t0 = time.time()
    P = pickle.load(open(sys.argv[1], "rb"))
    jobs = jobs_list()
    print(f"{len(jobs)} classes", flush=True)
    recs = []
    with Pool(2) as pool:
        for r in pool.imap_unordered(one, [(j, P) for j in jobs]):
            recs.append(r)
            print(f"job {r['index']:3d} ({len(recs)}/{len(jobs)}): N={r['N']} {r['word']} h={r['height']} "
                  f"npp {r.get('npp')} {'ERROR ' + r['error'] if r.get('error') else ''}{r['seconds']} s; "
                  f"elapsed {time.time() - t0:.0f} s", flush=True)
    recs.sort(key=lambda r: r["index"])
    json.dump({"records": recs}, open(os.path.join(HERE, "midheight_scan.json"), "w"), default=str)
    print(f"written midheight_scan.json; {time.time() - t0:.0f} s", flush=True)
