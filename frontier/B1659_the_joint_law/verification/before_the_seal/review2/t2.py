import numpy as np, math, pathlib
ROOT=pathlib.Path('.')
src=(ROOT/"frontier/B1656_the_electrons_zero/verification/the_electrons_zero.py").read_text()
NS={"__file__":"x.py","__name__":"h"}; exec(compile(src.split("T0 = time.time()")[0],"h","exec"),NS)
g=lambda k:NS[k]
OM,line_w,st,res,wM,cA,UN,SEC,SIXY,coupling=[g(k) for k in("OM","line_w","sector_twists","residues","weighted_M","cA","UNITS","SECTORS","SIXY","coupling")]
for ln in [(1/9,1/9),(2/9+1/3,2/9+2/3)]:
  w=line_w(*ln,OM)
  for sec,(fl,fr) in SEC.items():
    x,y=st(w,OM,SIXY[fl],SIXY[fr]);R=res(x,y,OM);c=cA(x,y,OM,R,nth=32,ns=24)
    M=wM({k:(math.sqrt(2*np.pi*50+c[k])*R[k] if c[k] is not None else 0j) for k in UN})
    print(ln,sec,abs(np.linalg.det(M))/np.linalg.norm(M)**2, np.linalg.svd(coupling(np.random.randn(2,2)+0j,M),compute_uv=False))
