"""the singlets' sup norms: the draft's (double precision, grid + Nelder-Mead) against an independent mpmath search"""
import sys, pathlib, json, time
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(1, str(HERE / "rerun"))
import mpmath as mp
import ref_model as rm
import search as ds
out = {}
for spr in rm.SINGLETS:
    t0 = time.time()
    d = ds.sup_norm(*spr)
    mine, at = rm.sup_norm_singlet(*spr)
    out[str(spr)] = dict(draft=d, referee=float(mine), rel_dev=float(abs(mine - d) / mine), at=at, sec=round(time.time() - t0, 1))
    print(spr, out[str(spr)], flush=True)
(HERE / "t_supnorm.json").write_text(json.dumps(out, indent=1))
