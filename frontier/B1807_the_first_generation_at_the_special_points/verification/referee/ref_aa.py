"""a.a in closed form: with R.R = R.dR = 0, R.d2R = -dR.dR, dR.dR = eta6/4, dR.d2R = 0 (eta^6 is Serre-flat at weight 3)
and d2R.d2R = -(5/144) E4 dR.dR (B1806), a.a = (eta6/4) g with g = f1^2 - 2 f0 f2 - (5/144) E4 f2^2 in M_{4n-4}.
Checked at random tau and random sections (own evaluator)."""
import random, json, pathlib
import mpmath as mp
from refkit import basis, dot
from ref_near_i import make_section
taus=[mp.mpc(0.13,1.07), mp.mpc(-0.4,0.95), mp.mpc(0.0,1.0)+mp.mpc(0.003,-0.002), mp.mpc(0.21,1.9)]
res={}
for t in taus:
    R,dR,d2R,eta6,e2,e4,e6=basis(t)
    res[mp.nstr(t,6)]={"|dR.d2R|/|dR|^2": mp.nstr(abs(dot(dR,d2R))/sum(abs(x)**2 for x in dR),3),
        "d2R.d2R / (-(5/144) E4 dR.dR)": mp.nstr(dot(d2R,d2R)/(-(mp.mpf(5)/144)*e4*dot(dR,dR)),20)}
worst=0
for n in range(2,12):
    fs=make_section(n,3)
    for t in taus:
        R,dR,d2R,eta6,e2,e4,e6=basis(t); f=fs(e4,e6)
        a=[f[0]*R[i]+f[1]*dR[i]+f[2]*d2R[i] for i in range(3)]
        g=f[1]**2-2*f[0]*f[2]-(mp.mpf(5)/144)*e4*f[2]**2
        worst=max(worst, abs(dot(a,a)-eta6/4*g)/sum(abs(x)**2 for x in a))
res["max rel |a.a - (eta6/4) g| over n=2..11"]=mp.nstr(worst,3)
pathlib.Path(__file__).resolve().parent.joinpath("ref_aa.json").write_text(json.dumps(res,indent=1)); print(json.dumps(res,indent=1))
