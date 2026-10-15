import io, os, sys, subprocess, tarfile, tempfile, pathlib, time
import numpy as np
from fractions import Fraction
REPO="<repo>"; SMC="87cf7f55111ec1f4019f302ffaa578376a9143e6"
TMP=pathlib.Path(tempfile.mkdtemp(prefix="plumb_lift_"))
blob=subprocess.run(["git","-C",REPO,"archive",SMC,"docs/dossiers/the_weave_2026-10-07","frontier"],check=True,capture_output=True).stdout
tarfile.open(fileobj=io.BytesIO(blob)).extractall(TMP, filter="data")
DOSS=TMP/"docs"/"dossiers"/"the_weave_2026-10-07"; sys.path.insert(0,str(DOSS)); here=os.getcwd(); os.chdir(DOSS)
import the_surface_yukawa as SY
sys.path.insert(0,here); import b1654_routeA as B
t0=time.time()
terms,r,line=SY.best_section((0,1,0),Fraction(-1,2)); Rser=SY.to_series(terms,SY.E8)
print('R built',time.time()-t0, r)
Rn=SY.np_eval(Rser)
for tau in (1j, 0.13+1.07j, 0.3+1.6j, -0.45+0.95j, 2.2j):
    w=Rn(np.array([tau]))[0]; RA=B.R_A(tau); v=np.array([RA[2],RA[4],RA[3]])
    ratio=w/v
    print(tau, 'W72 R', np.round(w,6), ' ratio comps', np.round(ratio,8), ' W.W', abs(w@w)/np.sum(abs(w)**2))
