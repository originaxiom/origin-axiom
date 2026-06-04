"""Test 2 redone at filling 1/3 (no commensurate even-r zeros -> clean metric).
Gromov delta-hyperbolicity of emergent metric d(i,j) = -log|C_ij|, controls included.
Also re-confirm Test 1 power-law at this filling so the two tests are consistent."""
import numpy as np, itertools

def chain_H(kind,N,seed=1):
    if kind=="fibonacci":
        a,b="a","b"
        while len(a)<N: a,b=a+b,a
        diag=np.array([0.5 if c=="a" else -0.5 for c in a[:N]])
    elif kind=="periodic": diag=np.zeros(N)
    elif kind=="random": diag=np.random.default_rng(seed).uniform(-3,3,N)
    return np.diag(diag)+np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1)

def corr(H,fill):
    w,U=np.linalg.eigh(H); k=int(round(fill*H.shape[0])); occ=U[:,:k]; return occ@occ.conj().T

def gromov_delta(D):
    n=D.shape[0]; worst=0.0
    for x,y,z,w in itertools.combinations(range(n),4):
        s=sorted([D[x,y]+D[z,w], D[x,z]+D[y,w], D[x,w]+D[y,z]])
        worst=max(worst,(s[2]-s[1])/2.0)
    return worst

N=987; fill=1.0/3.0
print(f"Filling = 1/3 (incommensurate-ish; avoids the half-filling even-r zeros)\n")
print("Re-check Test 1 (power-law => AdS):")
for kind in ("fibonacci","periodic","random"):
    C=np.abs(corr(chain_H(kind,N),fill))
    rs=np.arange(2,160); Cr=np.array([np.mean([C[i,i+r] for i in range(N//4,3*N//4-r)]) for r in rs])
    g=Cr>1e-12; lr,lc=np.log(rs[g]),np.log(Cr[g])
    eta=-np.polyfit(lr,lc,1)[0]; r2p=np.corrcoef(lr,lc)[0,1]**2
    invxi=-np.polyfit(rs[g],lc,1)[0]; r2e=np.corrcoef(rs[g],lc)[0,1]**2
    print(f"  {kind:>9}: power eta={eta:+.3f}(R2={r2p:.3f})  exp 1/xi={invxi:+.4f}(R2={r2e:.3f})  "
          f"-> {'POWER-LAW/AdS' if r2p>r2e else 'EXP/localized'}")

print("\nTest 2 (Gromov delta/diam), clean metric:")
for kind in ("fibonacci","periodic","random"):
    C=np.abs(corr(chain_H(kind,N),fill))
    sites=list(range(60,60+22*16,16)); n=len(sites); D=np.zeros((n,n))
    for a in range(n):
        for b in range(n):
            if a!=b:
                c=C[sites[a],sites[b]]; D[a,b]=-np.log(c) if c>1e-12 else 25.0
    diam=D.max(); delta=gromov_delta(D)
    tag='hyperbolic/AdS-like' if delta/diam<0.25 else ('mildly curved' if delta/diam<0.45 else 'flat/non-geometric')
    print(f"  {kind:>9}: delta={delta:.3f} diam={diam:.3f} delta/diam={delta/diam:.3f} -> {tag}")
print("\n(Euclidean R^1 line has delta/diam that does NOT ->0; a tree has delta=0. AdS3 ~ small delta/diam.)")
