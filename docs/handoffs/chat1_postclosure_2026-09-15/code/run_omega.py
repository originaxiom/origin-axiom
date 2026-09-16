#!/usr/bin/env python3
"""P-OMEGA-01 --- G-STAB, G-RATE, G-SAME.  Prereg sha256 7e39c494..."""
import snappy, cmath, json
W=complex(-0.5, 3**0.5/2); W2=W.conjugate()
def kappa_of(M):
    G=M.fundamental_group()
    g=G.generators()
    if len(g)<2: return None
    A=G.SL2C(g[0]); B=G.SL2C(g[1])
    tr=lambda X: complex(X[0][0]+X[1][1])
    AB=[[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    x,y,z=tr(A),tr(B),tr(AB)
    return x**2+y**2+z**2-x*y*z-2

print("="*78); print("G-STAB --- is kappa presentation-independent?"); print("="*78)
vals=[]
for k in range(10):
    M=snappy.Manifold('m004')
    if k: M.randomize()
    kp=kappa_of(M)
    if kp is None: continue
    d=kp-2
    tag = 'w' if abs(d-W)<1e-7 else ('w^2' if abs(d-W2)<1e-7 else f'{d:.6f}')
    vals.append(tag)
    print(f"   triangulation {k}: kappa-2 = {d:+.9f}   -> {tag}")
stab = all(v in ('w','w^2') for v in vals) and len(vals)>=8
print(f"\n   G-STAB: {'PASS' if stab else 'FAIL'}   ({len(vals)} triangulations, tags={set(vals)})")
if not stab:
    print("   VERDICT D: VOID -- kappa is presentation-dependent."); raise SystemExit(1)

print("\n"+"="*78); print("G-RATE --- base rate of kappa-2 = w across the census"); print("="*78)
n=0; exact=0; unit=0; ex=[]
for i,M in enumerate(snappy.OrientableCuspedCensus):
    if i>=4000: break
    try:
        kp=kappa_of(M)
        if kp is None: continue
        d=kp-2; n+=1
        if abs(d-W)<1e-7 or abs(d-W2)<1e-7:
            exact+=1
            if len(ex)<10: ex.append(M.name())
        if abs(abs(d)-1.0)<1e-7: unit+=1
    except Exception: pass
    if (i+1)%1000==0: print(f"   ...{i+1} scanned, n={n}, exact={exact}, |.|=1: {unit}", flush=True)
rate=100*exact/max(n,1); urate=100*unit/max(n,1)
print(f"\n   sampled           : {n}")
print(f"   kappa-2 = w or w^2: {exact}   ({rate:.2f}%)   e.g. {ex}")
print(f"   |kappa-2| = 1     : {unit}   ({urate:.2f}%)")
special = rate < 5.0
print(f"   G-RATE: {'PASS (special, <5%)' if special else 'FAIL (generic)'}")

print("\n"+"="*78); print("G-SAME --- does m004 carry a generation Z/3 at all?"); print("="*78)
M=snappy.Manifold('m004')
print(f"   H_1(m004) = {M.homology()}   (no torsion)")
cnt=0
for C in M.covers(3, method='low_index'):
    if C.num_cusps()==3: cnt+=1
print(f"   degree-3 covers with the cusp SPLIT into 3 (= cusp-trivial) : {cnt}")
ctrl={}
for nm in ['s958','t12833']:
    X=snappy.Manifold(nm); c=sum(1 for C in X.covers(3,method='low_index') if C.num_cusps()==3)
    ctrl[nm]=c
    print(f"   CONTROL {nm}: H1={X.homology()}  cusp-trivial degree-3 covers = {c}")
same = (cnt>0)
alive = all(v>0 for v in ctrl.values())
print(f"\n   C-ALIVE (covers DO carry them): {alive}")
print(f"   G-SAME: {'PASS' if same else 'FAIL -- m004 carries NO cusp-trivial Z/3'}")
print("\n"+"="*78)
if not alive: print("   VERDICT: VOID (control failed)"); raise SystemExit(1)
if not special: v='C --- GENERIC, files as a base-rate artefact'
elif same:      v='A --- real and new; needs a second independent derivation'
else:           v='B --- kappa-2 = w is a genuine fact; the Z/3 identification DIES'
print(f"   REGISTERED OUTCOME: {v}")
json.dump({'stab':stab,'n':n,'exact':exact,'rate':rate,'unit_rate':urate,
           'm004_cusp_trivial':cnt,'ctrl':ctrl,'verdict':v}, open('omega_result.json','w'))
