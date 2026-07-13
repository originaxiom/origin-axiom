from __future__ import annotations
import sys,json,time,multiprocessing as mpool
from pathlib import Path
import mpmath as mp
import numpy as np
sys.path.insert(0,'/mnt/data')
import generic_observer_fixed_point_certificate as g

SYMBOLS,_,EQFUNCS,JACFUNCS=g._build_symbolic_system()
N=16

def mp_from_pair(p):return mp.mpc(str(p[0]),str(p[1]))
def eval_f(x):return mp.matrix([EQFUNCS[i](*x) for i in range(N)])
def eval_j(x):return mp.matrix([[JACFUNCS[i][j](*x) for j in range(N)] for i in range(N)])
def mat_from(x):
 return {'a':[[x[1],mp.mpc(1)],[x[2],x[3]]], 'b':[[x[4],x[5]],[x[6],x[7]]], 'A':[[x[8],x[9]],[x[10],x[11]]], 'B':[[x[12],x[13]],[x[14],x[15]]]}
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def tr(A):return A[0][0]+A[1][1]
def kap(A,B):
 x=tr(A);y=tr(B);z=tr(mm(A,B));return x*x+y*y+z*z-x*y*z-2

def refine(pairs):
 mp.mp.dps=110
 x=[mp_from_pair(p) for p in pairs]
 for it in range(20):
  f=eval_f(x); J=eval_j(x)
  norm=max(abs(f[i]) for i in range(N))
  if norm<mp.mpf('1e-90'):break
  dx=mp.lu_solve(J,-f)
  x=[x[i]+dx[i] for i in range(N)]
 return x,max(abs(eval_f(x)[i]) for i in range(N))

def certify_one(item):
 idx,record=item
 try:
  mp.mp.dps=110;mp.iv.dps=75
  x,fnorm=refine(record['z'])
  J=eval_j(x);Y=J**-1;f=eval_f(x);corr=-Y*f
  best=None
  for rexp in [18,22,26,30,34,38]:
   r=mp.mpf(10)**(-rexp)
   iv=[mp.iv.mpc([v.real-r,v.real+r],[v.imag-r,v.imag+r]) for v in x]
   Jiv=[[JACFUNCS[i][j](*iv) for j in range(N)] for i in range(N)]
   ratios=[]
   for i in range(N):
    rowsum=mp.mpf('0')
    for j in range(N):
     value=mp.iv.mpc([1,1],[0,0]) if i==j else mp.iv.mpc([0,0],[0,0])
     for k in range(N):value-=Y[i,k]*Jiv[k][j]
     rowsum += g._interval_sup_abs(value)
    ratios.append((abs(corr[i])+r*rowsum)/r)
   mx=max(ratios)
   if best is None or mx<best[0]:best=(mx,r,iv)
   if mx<mp.mpf('1e-12'):break
  mx,r,iv=best
  if not mx<1:raise RuntimeError(f'K ratio {mx}')
  Miv=mat_from(iv);M=mat_from(x);gens=['a','b','A','B']
  kiv=[];kc=[]
  for a in range(4):
   for b in range(a+1,4):
    kiv.append(kap(Miv[gens[a]],Miv[gens[b]]));kc.append(kap(M[gens[a]],M[gens[b]]))
  def interval_rec(v):
   return {'re_lo':str(g._interval_endpoint(v.real.a,False)),'re_hi':str(g._interval_endpoint(v.real.b,True)), 'im_lo':str(g._interval_endpoint(v.imag.a,False)),'im_hi':str(g._interval_endpoint(v.imag.b,True))}
  excludes=[]
  for v in kiv:
   rlo=g._interval_endpoint(v.real.a,False);rhi=g._interval_endpoint(v.real.b,True);ilo=g._interval_endpoint(v.imag.a,False);ihi=g._interval_endpoint(v.imag.b,True)
   excludes.append(not (rlo<=2<=rhi and ilo<=0<=ihi))
  return {'index':idx,'success':True,'radius':mp.nstr(r,10),'max_ratio':mp.nstr(mx,30),'function_norm':mp.nstr(fnorm,20), 'center':[[mp.nstr(v.real,70),mp.nstr(v.imag,70)] for v in x], 'kappa_centers':[[mp.nstr(v.real,60),mp.nstr(v.imag,60)] for v in kc], 'kappa_intervals':[interval_rec(v) for v in kiv], 'irreducible_certified':any(excludes)}
 except Exception as e:
  return {'index':idx,'success':False,'error':repr(e)}

def main(n=None):
 D=json.loads(Path(__file__).resolve().parent / 'CELL3_RECOVERED_ROOTS.json'.read_text())['clusters']
 items=[]
 for i,r in enumerate(D):
  if not r['irreducible']:continue
  tr=np.array([complex(*x) for x in r['traces']])
  if np.linalg.norm(tr)<1e-3:continue
  items.append((i,r))
 if n:items=items[:n]
 t=time.time()
 ctx=mpool.get_context('fork')
 with ctx.Pool(8) as p:out=list(p.imap_unordered(certify_one,items,chunksize=1))
 out.sort(key=lambda x:x['index'])
 Path(__file__).resolve().parent / 'CELL3_INTERVAL_CERTIFICATES_REPRODUCED.json'.write_text(json.dumps(out,indent=2))
 print('n',len(out),'success',sum(x['success'] for x in out),'time',time.time()-t)
 for x in out:
  if not x['success']:print(x)
if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else None)
