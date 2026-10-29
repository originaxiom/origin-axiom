import importlib.util, json, math, pathlib, sys, time, numpy as np
ROOT=next(q for q in pathlib.Path(__file__).resolve().parents if (q/"frontier").is_dir() and (q/"GENESIS.md").is_file())
sp=importlib.util.spec_from_file_location("cc",ROOT/"frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.py")
cc=importlib.util.module_from_spec(sp); sp.loader.exec_module(cc)
ST=[(complex(*q["tau"]),complex(*q["c"])) for q in json.loads((ROOT/"frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text())["points"]]
def solve(t,c0):
    c,f=cc.solve_accessory(t,c0=c0); assert np.max(np.abs(f))<1e-9,(t,f); return c
def fn(t,c):
    _,_,Aa,Ab=cc.monodromy(t,c); x,y,z=(abs(v) for v in cc.traces(Aa,Ab))
    return np.array([2*math.acosh(x/2), 2*math.asinh((2*z-x*y)/(2*x))])
def warm(t):
    # continue from the nearest stored point *along the straight line* in small steps
    s,c=min(ST,key=lambda p:abs(p[0]-t))
    n=max(1,int(abs(t-s)/0.03))
    for k in range(1,n+1): c=solve(s+(t-s)*k/n,c)
    return c,s
def run(t,rels=(2e-3,5e-4)):
    c0,s=warm(t); res={"start":str(s),"c":[c0.real,c0.imag]}
    y=t.imag
    for r in rels:
        h=r*y
        # 5-point stencil, Richardson
        def cs(d): return solve(t+d,c0)
        def D(f,d1,d2):  # derivative along direction
            pass
        out={}
        for name,d in (("x",h),("y",1j*h)):
            f1=lambda s_: (2*cs(s_*d), fn(t+s_*d, cs(s_*d)/1)) 
            vals={}
            for s_ in (-2,-1,1,2):
                c=cs(s_*d); vals[s_]=(2*c, fn(t+s_*d,c))
            dC=(vals[-2][0]-8*vals[-1][0]+8*vals[1][0]-vals[2][0])/(12*h)
            dF=(vals[-2][1]-8*vals[-1][1]+8*vals[1][1]-vals[2][1])/(12*h)
            out[name]=(dC,dF)
        dCdx,Fx=out["x"]; dCdy,Fy=out["y"]
        dCtb=0.5*(dCdx+1j*dCdy)
        J=np.array([[Fx[0],Fy[0]],[Fx[1],Fy[1]]]); det=np.linalg.det(J)
        res[str(r)]={"dCdtb":[dCtb.real,dCtb.imag],"det":det,"half_signed_det":0.5*det,"Im/half|det|":dCtb.imag/(0.5*abs(det)),"Im/half_signed_det":dCtb.imag/(0.5*det),"ReOverAbs":abs(dCtb.real)/abs(dCtb)}
    return res
if __name__=="__main__":
    pts=[complex(p) for p in sys.argv[1:]]
    for t in pts:
        t0=time.time(); r=run(t); r["tau"]=str(t); r["sec"]=time.time()-t0
        print(json.dumps(r,default=float),flush=True)
