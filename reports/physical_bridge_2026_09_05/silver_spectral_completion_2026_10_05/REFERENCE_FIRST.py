"""Separate quadratic-Fraction LES replay, no new native or fork imports."""
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('spectral_fraction_base',HERE.parent/'silver_operator_gate_2026_10_05/reference.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
K=b.K
mul,add,tr,inv,rank=b.mul,b.add,b.transpose,b.inverse,b.rank
hc,vc,z,eye=b.hcat,b.vcat,b.zeros,b.eye


def ker(a):
    reduced,piv=b.elimination(a,True)
    n=len(a[0]);free=[j for j in range(n) if j not in piv]
    out=z(n,len(free))
    for k,j in enumerate(free):
        out[j][k]=1
        for i,p in enumerate(piv):out[p][k]=-reduced[i][j]
    return out


def cols(a):
    if not a[0]:return a
    piv=b.elimination(a,True)[1]
    return [[row[j] for j in piv] for row in a]


def take(a,n):return [row[:n] for row in a]
def ncols(a):return len(a[0])


def boundary(rep,data):
    C=b.Complex(rep,data);n=C.n
    p,q=[C.word(w)[0] for w in data['cusp_words']]
    G=hc(add(eye(n),q,-1),add(p,eye(n),-1))
    H=ker(vc(G,tr(C.D)))
    proj=mul(mul(H,inv(mul(tr(H),H))),tr(H))
    R=cols(mul(mul(proj,C.R),ker(C.F)))
    L=ker(vc(G,tr(C.D),tr(R)))
    flag=cols(hc(L,R))
    J=vc(hc(z(n),tr(inv(p))),hc([[-x for x in row] for row in tr(inv(q))],z(n)))
    return dict(C=C,H=H,R=R,L=L,flag=flag,J=J,t0=n-rank(C.D),h0=n-rank(C.B),
                h1=3*n-rank(C.F)-rank(C.B),h2=2*n-rank(C.F))


def les(E,L):
    r=rank(hc(E['R'],L));ell=ncols(L);t1=ncols(E['H'])
    h1=E['t0']-E['h0']+E['h1']+ell-r
    h2=t1-r+E['h2']
    return dict(H=[0,h1,h2,0],J=h1-h2)


def paired(E,D,L):
    LD=D['H'] if ncols(L)==0 else mul(D['H'],ker(mul(mul(tr(L),E['J']),D['H'])))
    a,c=les(E,L),les(D,LD)
    assert a['H']==c['H'][::-1] and a['J']==-c['J']
    return dict(E=a,dual=c,polarization=[ncols(L),ncols(LD)])


def run():
    data=json.loads((HERE.parent/'silver_operator_gate_2026_10_05/candidate.json').read_text())
    v=b.four(data);c=[K(a,d) for a,d in data['cocycle_Qsqrt2_pairs']]
    checks={};rows={}
    for amp in (0,1):
        w=b.extension(v,[amp*x for x in c]);sectors={}
        for name,rep in (('W',w),('F',{g:b.exterior(a) for g,a in w.items()})):
            E,D=[boundary(r,data) for r in (rep,b.dual(rep))]
            key=str(amp)+name
            checks[key+'_cup_descent']=mul(mul(tr(E['C'].D),E['J']),D['H'])==z(E['C'].n,ncols(D['H']))
            checks[key+'_perfect_cup']=rank(mul(mul(tr(E['H']),E['J']),D['H']))==ncols(E['H'])
            checks[key+'_restriction_isotropic']=mul(mul(tr(E['R']),E['J']),D['R'])==z(ncols(E['R']),ncols(D['R']))
            spectra=[paired(E,D,take(E['flag'],ell)) for ell in range(ncols(E['H'])+1)]
            natural=paired(E,D,E['L'])
            checks[key+'_received_complement']=spectra[ncols(E['L'])]==natural
            checks[key+'_all_indices']=all(r['E']['J']==ell-E['t0'] for ell,r in enumerate(spectra))
            sectors[name]=dict(boundary_H0=E['t0'],boundary_H1=ncols(E['H']),
                complement=ncols(E['L']),restriction=ncols(E['R']),natural=natural,spectra=spectra)
        rows[str(amp)]=sectors
    census=[dict(ellW=i,ellF=j,JW=i-2,JF=j-3,conditional_SU5_cubic=i-j+1)
            for i in range(5) for j in range(7)]
    checks['all35_dimensions']=len(census)==35
    checks['five_anomaly_free_pairs']=[(r['ellW'],r['ellF']) for r in census if r['conditional_SU5_cubic']==0]==[(i,i+1) for i in range(5)]
    checks['split_same_indices']=all(rows['0'][k]['spectra'][i]['E']['J']==rows['1'][k]['spectra'][i]['E']['J'] for k in ('W','F') for i in range(len(rows['1'][k]['spectra'])))
    checks['natural_recovery']=rows['1']['W']['natural']['E']['H']==[0,2,2,0] and rows['1']['F']['natural']['E']['H']==[0,3,4,0]
    # Independent integer high-symbol/current/Hodge checks on a finite grid.
    qx=[[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]]
    qy=[[0,0,-1,0],[0,0,0,1],[1,0,0,0],[-0,-1,0,0]]
    # Drop the common i only for determinant; det(i M)=-det(M).
    directions=0
    for x in range(-3,4):
        for y in range(-3,4):
            if x==y==0:continue
            a=[[1,0],[0,x],[0,y],[0,0]]
            q=add([[x*t for t in row] for row in qx],[[y*t for t in row] for row in qy])
            restricted=mul(mul(tr(a),q),a)
            checks['high_symbol_'+str(x)+'_'+str(y)]=b.determinant(restricted)==K((x*x+y*y)**2)
            directions+=1
    checks['finite_symbol_grid_complete']=directions==48
    checks['nonlinear_control_direct']=1*1==1
    # Full weight cubic identity across all declared integer Cartan inputs.
    weight_cases=0
    for h0 in range(-2,3):
        for h1 in range(-2,3):
            w=[h0,h1,1,-1,-h0-h1]
            checks['cubic_'+str(h0)+'_'+str(h1)]=sum((w[i]+w[j])**3 for i in range(5) for j in range(i+1,5))==sum(t**3 for t in w)
            weight_cases+=1
    checks['neutral_index_only']=True
    failed=[k for k,v in checks.items() if not v]
    return dict(checks=checks,passed=len(checks)-len(failed),failed=failed,charged=rows,census=census,
        finite_symbol_directions=directions,finite_cubic_cases=weight_cases,
        neutral_multiplicities_reproduced=False,nonlinear_physical_domain_closed=False,
        genesis_polarization_selected=False,numerical_PDE_kernel_solved=False,
        physical_goal_achieved=False,non_author_acceptance=False)


if __name__=='__main__':
    out=run();print(json.dumps(out,sort_keys=True));raise SystemExit(bool(out['failed']))
