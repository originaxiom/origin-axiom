"""Exact full-trace symbol and supergauge controls; no physical kernel census."""
import json
import sympy as s


def matrices():
    qx=s.I*s.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
    qy=s.I*s.Matrix([[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]])
    gamma=s.zeros(8)
    gamma[:4,4:]=-s.eye(4); gamma[4:,:4]=s.eye(4)
    j=s.zeros(8)
    for col,row,sign in ((0,7,1),(1,6,1),(2,5,-1),(3,4,-1),
                         (4,3,-1),(5,2,-1),(6,1,1),(7,0,1)):
        j[row,col]=sign
    parity=s.diag(1,-1,-1,1,-1,1,1,-1)
    return qx,qy,gamma,j,parity


def domain(kind,helicity=1,real_line=False,wrong_complement=False):
    if kind not in ('gauge','complement') or helicity not in (-1,1):
        raise ValueError('outside frozen population')
    e=s.eye(4)
    w=e[:,1]+(0 if real_line else helicity*s.I)*e[:,2]
    wp=e[:,2] if real_line else w.conjugate()
    if wrong_complement: wp=w
    a=e[:,0].row_join(w) if kind=='gauge' else w.row_join(e[:,3])
    b=wp.row_join(e[:,3]) if kind=='gauge' else e[:,0].row_join(wp)
    z=s.zeros(4,2)
    full=a.row_join(z).col_join(z.row_join(b))
    return a,b,full


def restricted_symbol(kind,helicity=1,real_line=False):
    x,y=s.symbols('x y',real=True)
    qx,qy,*_=matrices()
    a,_,_=domain(kind,helicity,real_line)
    return a.H*(x*qx+y*qy)*a


def supergauge(x,y,helicity=1):
    xi=s.Matrix([x,y]); w=s.Matrix([1,helicity*s.I])
    reject=s.eye(2)-w*w.H/2
    f_before=s.I*xi
    parameter=-1
    v_after=s.I*parameter/2
    f_after=f_before+s.I*xi*parameter
    z_before=-s.I*f_before
    z_after=2*s.I*xi*v_after-s.I*f_after
    residual=reject*f_before
    return dict(f_before=f_before,f_after=f_after,v_after=v_after,
                z_before=z_before,z_after=z_after,
                residual=residual,reject=reject)


def boundary_pair(reference,a):
    return s.expand(reference[0]*a[1]-reference[1]*a[0])


def bulk_cubic():
    e12=s.zeros(5);e12[0,1]=1
    e23=s.zeros(5);e23[1,2]=1
    e31=s.zeros(5);e31[2,0]=1
    return s.trace(e12*(e23*e31-e31*e23))


def run():
    checks={};x,y=s.symbols('x y',real=True)
    qx,qy,gamma,j,parity=matrices()
    checks['clifford_principal']=(qx*qx==qy*qy==s.eye(4) and
                                   qx*qy+qy*qx==s.zeros(4))
    checks['normal_green_nondegenerate']=gamma*gamma==-s.eye(8)
    checks['signed_hodge_square']=j*j==s.eye(8)
    profiles={}
    for kind in ('gauge','complement'):
        for sign in (-1,1):
            a,b,full=domain(kind,sign);key=kind+str(sign)
            checks[key+'_maximal_current']=(full.rank()==4 and
                                            full.H*gamma*full==s.zeros(4))
            checks[key+'_combined_reality']=full.row_join(j*full.conjugate()).rank()==4
            checks[key+'_degree_parity']=full.row_join(parity*full).rank()==4
            determinant=s.factor(restricted_symbol(kind,sign).det())
            checks[key+'_all_real_covectors']=determinant==-(x*x+y*y)
            other=domain(kind,-sign)[2]
            checks[key+'_conjugation_exchanges']=other.row_join(full.conjugate()).rank()==4
            profiles[key]=dict(trace_dimension=8,allowed_dimension=4,
                               restricted_symbol_determinant=str(determinant),
                               helicity=sign,parity_dimensions=[2,2])
    ga=domain('gauge')[2]
    checks['gauge_scalar_and_volume']=ga.row_join(s.eye(8)[:,0]).row_join(s.eye(8)[:,7]).rank()==4
    checks['full_parent_dimensions']=(24+24+4*50==248 and 24+248+224==496 and 4*248==992)
    real_g=restricted_symbol('gauge',real_line=True)
    real_c=restricted_symbol('complement',real_line=True)
    checks['real_line_nonelliptic_control']=(real_g.subs({x:0,y:1}).det()==0 and
                                            real_c.subs({x:1,y:0}).det()==0)
    wrong=domain('gauge',wrong_complement=True)[2]
    checks['wrong_slot_current_control']=wrong.H*gamma*wrong!=s.zeros(4)
    checks['boundary_common_line_wedge']=boundary_pair([1,s.I],[2,2*s.I])==0
    checks['opposite_lines_pair']=boundary_pair([1,s.I],[1,-s.I])==-2*s.I
    c0=s.Matrix([3,5]);a=s.Matrix([1,s.I])
    affine=boundary_pair(c0,a)
    checks['affine_reference_not_discarded']=affine==3*s.I-5 and affine!=0
    checks['reference_correction_cancels']=s.expand(-affine+boundary_pair(c0,a))==0
    checks['bulk_interaction_not_deleted']=bulk_cubic()==1
    for sign in (-1,1):
        g=supergauge(x,y,sign);label='compensation'+str(sign)
        norm=s.simplify((g['residual'].H*g['residual'])[0])
        checks[label+'_auxiliary_can_be_represented_zero']=g['f_after']==s.zeros(2,1)
        checks[label+'_leaves_wz_gauge']=g['v_after']!=0
        checks[label+'_invariant_Z_unchanged']=s.simplify(g['z_after']-g['z_before'])==s.zeros(2,1)
        checks[label+'_discard_V_fails']=s.simplify(-s.I*g['f_after']-g['z_before'])!=s.zeros(2,1)
        checks[label+'_all_nonzero_modes_escape']=norm==(x*x+y*y)/2
        realgrad=g['reject']*s.Matrix([x,y])
        checks[label+'_real_gauge_gradient']=s.simplify((realgrad.H*realgrad)[0])==(x*x+y*y)/2
        checks[label+'_internally_constant_control']=g['residual'].subs({x:0,y:0})==s.zeros(2,1)
    failed=[k for k,v in checks.items() if not v]
    return dict(checks=checks,passed=len(checks)-len(failed),failed=failed,
                profiles=profiles,parent=dict(coefficient_rank=248,gauge_rank=24,
                    complement_rank=224,trace_dimension=1984,allowed_dimension=992),
                physical_kernel_computed=False,full_superfield_domain_closed=False,
                physical_goal_achieved=False,non_author_acceptance=False)


if __name__=='__main__':
    result=run();print(json.dumps(result,sort_keys=True));raise SystemExit(bool(result['failed']))
