# Replica of the non-blind cells (N0, N3, N4, N5(a,b), N6) at the named points, route A only, using the instrument's own block text.
import os, sys, math, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blocks
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "replica_out"))
g = {"__name__": "replica"}
# docstring block holds the imports and OUT/LOG/dump/say
exec(compile(blocks.BLK[[k for k in blocks.BLK if k.startswith('"""B1654')][0]], "head", "exec"), g)
# order matters: head defines OUT/LOG/say/dump, imports; re-exec route A, B, Yukawa after head
for key in ("route A:", "route B:", "the Yukawa"):
    exec(compile(blocks.get(key), key, "exec"), g)
exec(compile(blocks.get("N0 plumbing"), "N0", "exec"), g)
print("N0:", {k:(float(v) if not isinstance(v,bool) else v) for k,v in g["pl"].items()})
TAUS=g["TAUS"]; cA=g["cA"]
t0=time.time()
g["C"]={name:{r:cA(r,tau,1e-5) for r in (2,3,4)} for name,tau in TAUS.items()}
print("route A c's computed [%.0fs]"%(time.time()-t0))
for name,c in g["C"].items(): print("  ",name,{r:round(v,10) for r,v in c.items()})
exec(compile(blocks.get("N3 symmetry"), "N3", "exec"), g)
exec(compile(blocks.get("N4 the cancellation"), "N4", "exec"), g)
n5src=blocks.get("N5 D's zero")
head=n5src.split("grid = []")[0]
exec(compile(head, "N5head", "exec"), g)
print("N5(a,b):", {k:g["n5"][k] for k in ("omega_abs","away_min_named")}, " D/R2:", {k:(round(v[0],6),round(v[1],6)) for k,v in g["n5"]["D_over_R2"].items()})
exec(compile(blocks.get("N6 the masses"), "N6", "exec"), g)
n6=g["n6"]
print("N6 details: limit_rel_err_at_2560 per dir:")
for name in ("i","t1"):
    for k,rec in enumerate(n6[name]):
        r=rec["rows"]
        print(f"  {name} dir{k}: lim err={abs(r[-1]['L_m1_m3']/rec['limit']-1):.2e}  angL ratio={r[3]['angle']*2560/(r[2]['angle']*640):.5f}  halving={r[3]['angle_over_sqrt_m1_m2']/r[2]['angle_over_sqrt_m1_m2']:.5f}  angle@640={r[2]['angle']:.2e}@2560={r[3]['angle']:.2e}  s2/s1={rec['sigma2_over_sigma1']:.3f}")
