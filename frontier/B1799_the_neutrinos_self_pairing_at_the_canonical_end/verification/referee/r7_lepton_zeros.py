"""Referee B1799, check 3: the seesaw's massless lines against the charged leptons'.  The Dirac L nu^c (-3, 0) and the
charged-lepton sector L e (-3, 6) share the left twist -3w; B1716's law puts both sectors' exact zeros on the lines where -3w
has exact order 4.  Computed here: the charged-lepton sector's Dn on B1795's 286 lines at its three points, against the
Dirac zero set in majorana_rows.jsonl.  Read-only."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import sys, math, json, pathlib, importlib.util
ROOT = pathlib.Path(_ROOT + "")
spec = importlib.util.spec_from_file_location("split", ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification/split.py")
SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
B = SP._modules()["B"]
ARC = ROOT / "frontier/B1799_the_neutrinos_self_pairing_at_the_canonical_end/verification"


def task(job):
    k, pk = job; a, b = SP.lines()[k]; re_t, im_t = SP.POINTS[pk]; t = complex(re_t, im_t); w = float(a) * t + float(b)
    x, y = B.sector_twists(w, t, -3, 6); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
    vals = [abs(v) for v in c.values() if v is not None]; D = sum(c[s] * R[s] ** 2 for s in B.UNITS if c[s] is not None)
    return (k, pk, abs(D) / (max(vals) * B.nR2(R)))


if __name__ == "__main__":
    import multiprocessing as mpc
    with mpc.get_context("fork").Pool(6) as pool:
        res = pool.map(task, [(k, pk) for k in range(len(SP.lines())) for pk in SP.POINTS], chunksize=6)
    rows = {(r["line"], r["point"]): r for r in (json.loads(l) for l in (ARC / "majorana_rows.jsonl").read_text().splitlines() if l.strip())}
    ze = {(k, pk) for k, pk, d in res if d < 1e-10}; zd = {key for key, r in rows.items() if r["Lnuc"]["Dn"] < 1e-10}
    print("charged leptons L e: exact-zero rows %d (lines %d); Dirac L nu^c: %d (lines %d); identical row sets: %s" % (len(ze), len({k for k, _ in ze}), len(zd), len({k for k, _ in zd}), ze == zd))
    print("  charged leptons: Dn at zeros max %.1e, elsewhere min %.2e" % (max(d for k, pk, d in res if d < 1e-10), min(d for k, pk, d in res if d >= 1e-10)))
    print("r7 exit 0")
