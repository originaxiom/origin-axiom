import sys, io, contextlib, importlib.util, pathlib, json
from fractions import Fraction as F
ROOT=next(q for q in pathlib.Path(__file__).resolve().parents if (q/"frontier").is_dir() and (q/"GENESIS.md").is_file())
spec=importlib.util.spec_from_file_location("c26",ROOT/"frontier/B1726_the_two_ingredients_replicated/verification/census.py")
C=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(C)
C._modules(); B=C._M["B"]
def ch(nc): return {"Q":1,"u":-(nc+1),"d":nc-1,"L":-nc,"e":2*nc,"H":nc}
def nn(x): x=x%1; return min(x,1-x)
def ex(qL,qR,a): return F(1,2)-(nn(2*qL*a)+nn(2*qR*a))/2
def run(nc,a,re,im,b):
    B.SIXY.update(ch(nc)); r=C.compute(re,im,a,b)
    out={}
    for rn in ("S","St"):
        d=r["down|L_max|%s"%rn]; e=r["lep|L_max|%s"%rn]
        out[rn]=(e[0]/d[0], d[1]/e[1])
    return out
if __name__=="__main__":
    cells=[(3,F(1,10)),(3,F(1,12)),(3,F(1,8)),(3,F(2,5)),(3,F(2,23)),(3,F(1,4)),(2,F(1,6)),(4,F(1,14)),(5,F(5,12)),(3,F(1,9))]
    if len(sys.argv)>1: cells=[c for c in cells][int(sys.argv[1])::2]
    for nc,a in cells:
        q=ch(nc); print("nc",nc,"a",a,"eq-exp",ex(q["Q"],q["d"],a)==ex(q["L"],q["e"],a),flush=True)
        for re,im,b in [(1/3,12.0,0.137),(0.1,12.0,0.137),(0.6,12.0,0.137),(1/3,14.0,0.137),(1/3,14.0,0.311)]:
            o=run(nc,a,re,im,b); print("  re %.3f im %g b %.3f  S R2=%.4f R1=%.4g | St R2=%.4f R1=%.4g"%(re,im,b,o["S"][0],o["S"][1],o["St"][0],o["St"][1]),flush=True)
