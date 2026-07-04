"""B416 TW2 -- track the trace-map dynamics to its destination, blind. Name as pure math."""
import json, os, numpy as np

# T1(x,y,z) = (z, x, xz - y); figure-eight monodromy = T1^2. kappa = x^2+y^2+z^2-xyz-2 conserved.
def T1(v):
    x,y,z=v; return np.array([z, x, x*z - y])
def T(v): return T1(T1(v))
def kappa(v):
    x,y,z=v; return x*x+y*y+z*z-x*y*z-2

# T1: fixed points of T on kappa-level sets, and periodic-orbit counts (the dynamical zeta).
# Fixed points of T = T1^2: solve T(v)=v. Over reals near the void and on kappa levels.
# Enumerate SHORT periodic orbits numerically on a kappa-slice, count by period.
def orbit_period(v, maxp=40, tol=1e-6):
    v0=v.copy(); w=v.copy()
    for p in range(1,maxp+1):
        w=T(w)
        if np.max(np.abs(w-v0))<tol: return p
    return None

# sample the dynamics on the kappa = -2 (cusp/geometric) and kappa=+2 (void) slices
res={}
# the void fixed point (2,2,2): confirm banked Jacobian eigenvalues
eps=1e-6
J=np.zeros((3,3))
v=np.array([2.,2.,2.])
for i in range(3):
    dv=v.copy(); dv[i]+=eps
    J[:,i]=(T(dv)-T(v))/eps
ev=sorted(np.linalg.eigvals(J).real)
phi=(1+5**.5)/2
res["void_jacobian_eigs"]=[float(e) for e in ev]
res["banked_phi4_phi-4_1"]=[float(phi**-4), 1.0, float(phi**4)]
print("void Jacobian eigs:", [f"{e:.4f}" for e in ev], " vs {phi^-4,1,phi^4}=",
      [f"{phi**-4:.4f}",f"{1.0}",f"{phi**4:.4f}"])
# the ATTRACTOR + symmetry group: the trace map commutes with the S3-like coordinate perms?
# Test which permutations/sign-changes preserve T (the dynamical symmetry group).
perms=[(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]
signs=[(a,b,c) for a in (1,-1) for b in (1,-1) for c in (1,-1)]
syms=[]
rng=np.random.default_rng(0)
for pm in perms:
    for sg in signs:
        ok=True
        for _ in range(20):
            v=rng.uniform(-3,3,3)
            Pv=np.array([sg[i]*v[pm[i]] for i in range(3)])
            if np.max(np.abs(T(Pv)-np.array([sg[i]*T(v)[pm[i]] for i in range(3)])))>1e-9:
                ok=False;break
        if ok: syms.append((pm,sg))
res["dynamical_symmetry_group_order"]=len(syms)
print("dynamical symmetry group order (perms x signs preserving T):", len(syms))
res["symmetries"]=[[list(pm),list(sg)] for pm,sg in syms]
json.dump(res, open("track_dynamics.json","w"), indent=1)
print("DONE")
