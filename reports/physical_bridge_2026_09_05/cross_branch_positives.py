"""R75 bounded independent algebra; no incoming producer import or physics ID."""
from functools import lru_cache
import json
import sympy as s
from sympy.polys.agca.extensions import MonogenicFiniteExtension
from sympy.polys.matrices import DomainMatrix

Q, T = s.symbols('q s')


def clean(a):
    return a.applyfunc(s.cancel) if isinstance(a, s.MatrixBase) else s.cancel(a)


def literal():
    return (s.Matrix([[1,0,1,Q/2-1],[0,1,1,Q/2],
                      [0,0,1,(Q+1)/2],[0,0,0,1]]),
            s.Matrix([[1,0,0,0],[2+2/Q,1,0,0],
                      [2,1,1,0],[1,1,0,1]]))


def inverse_word(w):
    return w[::-1].swapcase()


def reduce_word(w):
    out=[]
    for a in w:
        if out and out[-1] == a.swapcase():
            out.pop()
        else:
            out.append(a)
    return ''.join(out)


def phi(w):
    subst={'x':'y','y':'yXyy'}
    return reduce_word(''.join(subst[a] if a.islower() else
                              inverse_word(subst[a.lower()]) for a in w))


def power_phi(w,n):
    for _ in range(n):
        w=phi(w)
    return w


def sym_word(w,gens):
    n=next(iter(gens.values())).rows
    out=s.eye(n)
    for a in w:
        g=gens[a.lower()]
        out=clean(out*(g if a.islower() else g.inv()))
    return out


def word_jacobian(w,gens):
    """Direct left-cocycle sum, separately from any closed Fox formula."""
    names=list(gens)
    n=next(iter(gens.values())).rows
    out=s.zeros(n,n*len(names)); prefix=s.eye(n)
    for a in w:
        i=names.index(a.lower()); g=gens[a.lower()]
        if a.islower():
            contribution=prefix
            prefix=clean(prefix*g)
        else:
            prefix=clean(prefix*g.inv())
            contribution=-prefix
        out[:,i*n:(i+1)*n]+=contribution
    return clean(out)


def deck(ab):
    a,b=ab
    return b%2,(3*b-a)%2


@lru_cache(None)
def transport(ab):
    m,n=literal()
    rx=clean(n*m.inv()); ry=clean(m*n*m.inv()**2)
    vx=(-1)**ab[0]*rx; vy=(-1)**ab[1]*ry
    gens={'x':vx,'y':vy}
    one=(m.inv()*word_jacobian(phi('x'),gens)).col_join(
         m.inv()*word_jacobian(phi('y'),gens))
    return clean(one)


@lru_cache(None)
def cycle(ab):
    out=s.eye(8); a=ab
    for _ in range(3):
        out=clean(transport(a)*out); a=deck(a)
    assert a == ab
    return out


def rank_reduce(mat):
    """Plain field Gauss-Jordan; no modular rank or fraction-free proxy."""
    a=mat.to_list(); nr,nc=mat.shape; piv=[]; row=0
    for col in range(nc):
        k=next((j for j in range(row,nr) if a[j][col]),None)
        if k is None:
            continue
        a[row],a[k]=a[k],a[row]
        v=a[row][col]
        a[row]=[x/v for x in a[row]]
        for j in range(nr):
            if j != row and a[j][col]:
                v=a[j][col]
                a[j]=[x-v*y for x,y in zip(a[j],a[row])]
        piv.append(col); row+=1
        if row == nr:
            break
    return DomainMatrix(a,mat.shape,mat.domain),piv


def rank(mat):
    return len(rank_reduce(mat)[1])


def kernel(mat):
    rr,piv=rank_reduce(mat); a=rr.to_list(); nc=mat.shape[1]
    free=[j for j in range(nc) if j not in piv]; k=mat.domain
    rows=[[k.zero for _ in free] for _ in range(nc)]
    for b,col in enumerate(free):
        rows[col][b]=k.one
        for i,p in enumerate(piv):
            rows[p][b]=-a[i][col]
    return DomainMatrix(rows,(nc,len(free)),k)


def inv(mat):
    n=mat.shape[0]; rr,piv=rank_reduce(mat.hstack(eye(n,mat.domain)))
    assert piv[:n] == list(range(n))
    return rr.extract(list(range(n)),list(range(n,2*n)))


def eye(n,k):
    return DomainMatrix.eye((n,n),k)


def zero(n,m,k):
    return DomainMatrix.zeros((n,m),k)


def dm(a,k):
    def conv(x):
        num,den=s.fraction(s.cancel(x))
        return k.convert(s.expand(num))/k.convert(s.expand(den))
    return DomainMatrix([[conv(x) for x in row] for row in a.tolist()],a.shape,k)


def field_word(w,gens):
    names=list(gens); n=gens[names[0]].shape[0]; k=gens[names[0]].domain
    prefix=eye(n,k); jac=zero(n,n*len(names),k); inverse={}
    for a in w:
        idx=names.index(a.lower()); g=gens[a.lower()]
        if a.islower():
            contribution=prefix; prefix=prefix*g
        else:
            if a.lower() not in inverse:
                inverse[a.lower()]=inv(g)
            prefix=prefix*inverse[a.lower()]; contribution=-prefix
        blocks=[zero(n,n,k) for _ in names]; blocks[idx]=contribution
        jac=jac+blocks[0].hstack(*blocks[1:])
    return prefix,jac


def same(a,b):
    return not any(x for row in (a-b).to_list() for x in row)


def cohomology(gens):
    names=list(gens); n=gens[names[0]].shape[0]; k=gens[names[0]].domain
    rels=['zxZ'+inverse_word(power_phi('x',3)),
          'zyZ'+inverse_word(power_phi('y',3))]
    pairs=[field_word(w,gens) for w in rels]
    assert all(same(a,eye(n,k)) for a,_ in pairs)
    j=pairs[0][1].vstack(pairs[1][1])
    b=(gens['x']-eye(n,k)).vstack(gens['y']-eye(n,k),gens['z']-eye(n,k))
    assert same(j*b,zero(2*n,n,k))
    ell,r_ell=field_word('yXYx',gens)
    per={'u':gens['z'],'v':ell}
    comm,jt=field_word('uvUV',per)
    assert same(comm,eye(n,k))
    bt=(per['u']-eye(n,k)).vstack(per['v']-eye(n,k))
    rz=zero(n,n,k).hstack(zero(n,n,k),eye(n,k))
    restrict=rz.vstack(r_ell); z=kernel(j)
    assert same(jt*restrict*z,zero(n,z.shape[1],k))
    rb=rank(b); rbt=rank(bt)
    return {'a0':n-rb,'a1':3*n-rank(j)-rb,'t0':n-rbt,
            't1':2*n-rank(jt)-rbt,
            'r1':rank((restrict*z).hstack(bt))-rbt}


@lru_cache(None)
def algebra_controls():
    m,n=literal(); rx=clean(n*m.inv()); ry=clean(m*n*m.inv()**2)
    ell=sym_word('nMNmmNMn',{'m':m,'n':n})
    qpoly=lambda q: T**4-8*T**3-(q+1/q-16)*T**2-8*T+1
    checks={
        'determinants':clean(m.det()-1)==0 and clean(n.det()-1)==0,
        'literal_relator':sym_word('mnMNmNMnmN',{'m':m,'n':n})==s.eye(4),
        'fibre_x':clean(m*rx*m.inv()-ry)==s.zeros(4),
        'fibre_y':clean(m*ry*m.inv()-sym_word('yXyy',{'x':rx,'y':ry}))==s.zeros(4),
        'boundary_word':clean(ell-sym_word('yXYx',{'x':rx,'y':ry}))==s.zeros(4),
        'boundary_fixed':phi('yXYx')=='yXYx',
        'longitude_polynomial':clean(ell.charpoly(T).as_expr()-(T-Q)**3*(T-Q**-3))==0,
        'orbit':deck((0,1))==(1,1) and deck((1,1))==(1,0) and deck((1,0))==(0,1)}
    polys=[]
    for ab in ((0,1),(1,1),(1,0)):
        b=((-1)**ab[0]*rx-s.eye(4)).col_join((-1)**ab[1]*ry-s.eye(4))
        st=cycle(ab)
        checks[f'coboundary_transport_{ab}']=clean(st*b-b*m.inv()**3)==s.zeros(8,4)
        quotient=clean(st.charpoly(T).as_expr()/(T-1)**4)
        polys.append(str(s.factor(quotient)))
        checks[f'quotient_polynomial_{ab}']=clean(quotient-qpoly(Q**3))==0
        checks[f'generic_control_{ab}']=clean(qpoly(Q**3).subs({Q:2,T:-1}))!=0
    return {'checks':checks,'quotients':polys}


@lru_cache(None)
def root_controls():
    g=s.Poly(Q**6-34*Q**3+1,Q,domain=s.QQ)
    assert g.is_irreducible
    k=MonogenicFiniteExtension(g)
    m,n=literal(); rx=clean(n*m.inv()); ry=clean(m*n*m.inv()**2)
    checks={'irreducible':g.is_irreducible,'positive_roots':g.count_roots(0,s.oo)==2,
            'double_factor':clean((T**4-8*T**3-18*T**2-8*T+1)
                                 -(T+1)**2*(T**2-10*T+1))==0}
    nullities=[]
    for ab in ((0,1),(1,1),(1,0)):
        b=dm(((-1)**ab[0]*rx-s.eye(4)).col_join((-1)**ab[1]*ry-s.eye(4)),k)
        st=dm(cycle(ab),k); a=st+eye(8,k); power=eye(8,k); dims=[]
        for _ in range(4):
            power=power*a; dims.append(8-rank(power))
        nullities.append(dims)
        checks[f'coboundary_rank_{ab}']=rank(b)==4
        checks[f'jordan_{ab}']=dims==[1,2,2,2]
        # An eigenvalue outside the quotient and the unipotent coboundaries.
        checks[f'wrong_eigenvalue_{ab}']=rank(st+2*eye(8,k))==8
    return {'checks':checks,'nullities':nullities}


@lru_cache(None)
def index_controls():
    k=MonogenicFiniteExtension(s.Poly(Q**6-34*Q**3+1,Q,domain=s.QQ))
    m,n=literal(); ab=(0,1)
    vx=dm(n*m.inv(),k); vy=dm(-m*n*m.inv()**2,k); vz=dm(-m**3,k)
    c=kernel(dm(cycle(ab),k)+eye(8,k)).extract(list(range(8)),[0])
    cx=c.extract(list(range(4)),[0]); cy=c.extract(list(range(4,8)),[0])
    def lift(v,a):
        return v.hstack(a).vstack(zero(1,4,k).hstack(eye(1,k)))
    w={'x':lift(vx,cx),'y':lift(vy,cy),'z':lift(vz,zero(4,1,k))}
    split={'x':lift(vx,zero(4,1,k)),'y':lift(vy,zero(4,1,k)),
           'z':lift(vz,zero(4,1,k))}
    a=cohomology(w); b=cohomology({name:inv(v).transpose() for name,v in w.items()})
    asp=cohomology(split); bsp=cohomology({name:inv(v).transpose() for name,v in split.items()})
    idx=(a['a1']-a['r1'])-(b['a1']-b['r1'])
    isp=(asp['a1']-asp['r1'])-(bsp['a1']-bsp['r1'])
    ell=sym_word('nMNmmNMn',{'m':m,'n':n})
    # The triangular extension has the same exterior characteristic as V+1.
    ev=[Q,Q,Q,Q**-3,s.S.One]
    extdet=s.prod(ev[i]*ev[j]-1 for i in range(5) for j in range(i+1,5))
    checks={'actual_index':idx==-1,'split_index':isp==0,
            'index_identity':idx==a['a0']-b['a0']+b['t0']-a['r1'],
            'annihilator':a['r1']+b['r1']==a['t1']==b['t1'],
            'exterior_acyclic_at_both_roots':k.convert(s.fraction(s.cancel(extdet))[0])!=k.zero,
            'dual_index':-idx==1,
            'expected_data':a=={'a0':0,'a1':1,'t0':1,'t1':2,'r1':1}
                            and b=={'a0':1,'a1':2,'t0':1,'t1':2,'r1':1}}
    return {'checks':checks,'extension':a,'dual':b,'split':asp,
            'split_dual':bsp,'index':idx,'split_index':isp,
            'exterior_determinant':str(s.factor(extdet))}


@lru_cache(None)
def hopping_controls():
    a1,a2,a3,a4,b1,b2,b3,b4=s.symbols('a1:5 b1:5')
    d1,d2,cp,cm,dp,dm_,e1,e2,Y=s.symbols('d1 d2 cp cm dp dm e1 e2 Y')
    a=s.Matrix([[0,d1*cp*a2,d2*dp*b3,0],
                [d1*cm*a1,0,0,d2*dp*b4],
                [d2*dm_*b1,0,0,d1*cp*a4],
                [0,d2*dm_*b2,d1*cm*a3,0]])
    target=e1**2*a1*a2*a3*a4+e2**2*b1*b2*b3*b4-e1*e2*(a1*b2*a4*b3+b1*a3*b4*a2)
    substitution={e1:-d1**2*cp*cm,e2:-d2**2*dp*dm_}
    spec=target.subs({a1:0,a4:0,b1:Y,b4:Y})
    bad=a.copy(); bad[3,2]=0
    wrong=a.copy(); wrong[0,1]=-wrong[0,1]
    return {'checks':{'square_determinant':s.expand(a.det()-target.subs(substitution))==0,
                     'matched_Y_square':s.expand(spec-Y**2*(e2**2*b2*b3-e1*e2*a2*a3))==0,
                     'delete_edge_detected':s.expand(bad.det()-a.det())!=0,
                     'wrong_sign_detected':s.expand(wrong.det()-a.det())!=0},
            'polynomial':str(target),'matched':str(s.factor(spec))}


def balance_controls():
    b=s.Matrix(s.symbols('b0:4',real=True)); c=s.zeros(5)
    c[:4,4]=b; psi=(c+c.T)/2; a=(c-c.T)/2
    xi=s.diag(1,1,1,1,-4); norm=(b.T*b)[0]
    pairing=s.expand(s.trace(psi*(a*xi-xi*a)))
    return {'checks':{'rank_five_projector':pairing==-s.Rational(5,2)*norm,
                     'zero_offdiagonal_control':pairing.subs(dict.fromkeys(b,0))==0,
                     'nonsplit_cost_not_identically_zero':pairing!=0},
            'pairing':str(pairing)}


def run():
    groups={}
    for name,fn in [('algebra',algebra_controls),('roots',root_controls),
                    ('index',index_controls),('hopping',hopping_controls),
                    ('balance',balance_controls)]:
        groups[name]=fn()
        print(json.dumps({'group':name,**groups[name]},sort_keys=True),flush=True)
    checks=[v for g in groups.values() for v in g['checks'].values()]
    out={'passed':sum(checks),'total':len(checks),'all_checks_pass':all(checks)}
    print(json.dumps(out,sort_keys=True),flush=True)
    return out


if __name__ == '__main__':
    raise SystemExit(0 if run()['all_checks_pass'] else 1)
