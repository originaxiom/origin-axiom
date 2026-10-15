import numpy as np, math, json
src=open('run_copy.py').read().split("# ================================================================ S0 plumbing")[0]
import os; os.environ["OA_ROOT"]="."
exec(src)
B=json.load(open('./frontier/B1654_the_norm_of_the_boundary_class/verification/the_norm_of_the_boundary_class.json'))
k="t1"; t=TAUS[k]; R=Rvec(t); cr=np.array([B['N2']['pairs']["%s,%d"%(k,r)]['A'] for r in (2,3,4)])
D=complex(*B['N5']['D_over_R2'][k]); lim=abs(D)/(2*np.pi)
L=2560.; u=np.sqrt(2*np.pi*L+cr)*R
Rn=R/np.linalg.norm(R); nvec=np.cross(Rn.real,Rn.imag); nvec/=np.linalg.norm(nvec)
rng=np.random.default_rng(1)
def cone_point(c1,c2):
    # a = x*Rbar + y*R + z*n with a.a = 2xy + z^2 = 0
    x=1.0; z=c1; y=-z*z/(2*x); return x*Rn.conj()+y*Rn+z*nvec
for z in (0,0.01,0.1,0.5,1.0):
    a=cone_point(z,0); a/=np.linalg.norm(a)
    s=sv(Y(a,u)); print("z=",z," a.a=",abs(a@a)," s3/s1=",s[2]/s[0]," L s2/s1 =",L*s[1]/s[0]," limit =",lim)
# other cone family: a = x R + y Rbar + z n with 2xy + z^2=0, x large
for x in (0.0, 0.3, 1.0):
    z=0.4; y=-z*z/(2*x) if x!=0 else 0
    a=x*Rn+ (1.0 if x==0 else y)*Rn.conj()+z*nvec
