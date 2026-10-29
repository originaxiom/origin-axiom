import json,math,numpy as np
d=json.load(open(next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q/"frontier").is_dir())/"frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json"))["points"]
delta=4*math.log(2)/math.pi; print("delta",delta)
rows=[]
for q in d:
    t=complex(*q["tau"]); c=complex(*q["c"]); x=min(q["traces"][:2]) if False else q["traces"][0]
    l=2*math.acosh(x/2); rows.append((t.imag,t.real,c.real,c.imag,l,q["traces"]))
rows.sort()
for y,xr,cr,ci,l,tr in rows:
    if y>=1: print("y=%.2f x=%.2f Re c=%.5f Im c=%.1e  P=%.4f  3/(y+d)^2=%.4f  3/(pi y)=%.4f  pi/l-y=%.4f traces=%.3f %.3f %.3f"%(y,xr,cr,ci,1-12*cr/math.pi**2,3/(y+delta)**2,3/(math.pi*y),math.pi/l-y,*tr))
