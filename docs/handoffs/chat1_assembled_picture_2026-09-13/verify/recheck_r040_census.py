#!/usr/bin/env python3
"""Independent re-derivation of R040's census half (B1325 rows it OPEN, not banked).
Claim: every orientation double cover of the nonorientable cusped census has cs = 0 mod 1/2."""
import snappy, json, sys
C = snappy.NonorientableCuspedCensus
N = len(C)
print(f"NonorientableCuspedCensus size: {N}", flush=True)
res = {"n":0,"zero":0,"nonzero":[],"errors":[],"maxres":0.0,
       "ctl_nonorientable":0,"ctl_cover_orientable":0,"ctl_degree2":0,"ctl_cusps_ok":0}
for i, M in enumerate(C):
    try:
        nm = M.name()
        if not M.is_orientable(): res["ctl_nonorientable"] += 1
        D = M.orientation_cover()
        if D.is_orientable(): res["ctl_cover_orientable"] += 1
        if D.volume()/M.volume() > 1.9 and D.volume()/M.volume() < 2.1: res["ctl_degree2"] += 1
        if D.num_cusps() >= M.num_cusps(): res["ctl_cusps_ok"] += 1
        cs = D.chern_simons()
        r = float(cs) % 0.5
        r = min(r, 0.5 - r)                      # distance to 0 mod 1/2
        res["n"] += 1
        res["maxres"] = max(res["maxres"], r)
        if r < 1e-9: res["zero"] += 1
        else: res["nonzero"].append((nm, float(cs), r))
    except Exception as e:
        res["errors"].append((str(nm), str(e)[:80]))
    if (i+1) % 100 == 0:
        print(f"  {i+1}/{N} done  zero={res['zero']}  nonzero={len(res['nonzero'])}"
              f"  err={len(res['errors'])}  maxres={res['maxres']:.2e}", flush=True)
        json.dump(res, open('../out/r040/partial.json','w'))
json.dump(res, open('../out/r040/result.json','w'))
print("\n=== R040 CENSUS RE-DERIVATION ===")
print(f"  computed        : {res['n']}/{N}")
print(f"  cs = 0 mod 1/2  : {res['zero']}")
print(f"  non-zero        : {len(res['nonzero'])}  {res['nonzero'][:5]}")
print(f"  errors          : {len(res['errors'])}  {res['errors'][:3]}")
print(f"  max residue     : {res['maxres']:.3e}")
print(f"  CONTROLS: nonorientable={res['ctl_nonorientable']} cover_orientable="
      f"{res['ctl_cover_orientable']} degree2={res['ctl_degree2']} cusps_ok={res['ctl_cusps_ok']}")
codex_claim = (res['n']==1260 and res['zero']==1260 and len(res['nonzero'])==0)
print(f"\n  REPRODUCES R040's 1260/1260 : {codex_claim}")
