"""R76 supplemental nonzero-frame solver control; original science unchanged."""
import importlib.util
import json
from pathlib import Path
import sympy as s


def run():
    p=Path(__file__).with_name('cross_branch_positives.py')
    spec=importlib.util.spec_from_file_location('r76_control_own_r75',p)
    c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
    k=c.MonogenicFiniteExtension(s.Poly(c.Q**6-34*c.Q**3+1,c.Q,domain=s.QQ))
    m,n=c.literal();v={'x':c.dm(n*m.inv(),k),'y':c.dm(-m*n*m.inv()**2,k),
                      'z':c.dm(-m**3,k)}
    cv=c.kernel(c.dm(c.cycle((0,1)),k)+c.eye(8,k)).extract(list(range(8)),[0])
    original=cv.vstack(c.zero(4,1,k));u0=c.eye(4,k).extract(list(range(4)),[0])
    bs=(v['x']-c.eye(4,k)).vstack(v['y']-c.eye(4,k),v['z']-c.eye(4,k))
    shifted=original+bs*u0
    def lift(mat,col):
        return mat.hstack(col).vstack(c.zero(1,4,k).hstack(c.eye(1,k)))
    def bundle(cs):
        return {g:lift(mat,cs.extract(list(range(i*4,i*4+4)),[0]))
                for i,(g,mat) in enumerate(v.items())}
    ws=bundle(shifted);wo=bundle(original)
    vl,j=c.field_word('yXYx',v);ce=j*shifted;cz=shifted.extract(list(range(8,12)),[0])
    u=c.inv(vl-c.eye(4,k))*ce
    wl,_=c.field_word('yXYx',ws);b=lift(c.eye(4,k),-u);bi=c.inv(b)
    wrong=lift(c.eye(4,k),-2*u)
    rels=['zxZ'+c.inverse_word(c.power_phi('x',3)),
          'zyZ'+c.inverse_word(c.power_phi('y',3))]
    checks={'nonzero_longitude':not c.same(ce,c.zero(4,1,k)),
            'nonzero_stable':not c.same(cz,c.zero(4,1,k)),
            'recovers_nonzero_primitive':c.same(u,u0),
            'stable_primitive':c.same((v['z']-c.eye(4,k))*u,cz),
            'longitude_splits':c.same(bi*wl*b,lift(vl,c.zero(4,1,k))),
            'stable_splits':c.same(bi*ws['z']*b,lift(v['z'],c.zero(4,1,k))),
            'same_global_extension':all(c.same(bi*ws[g]*b,wo[g]) for g in v),
            'global_class_still_nonzero':c.rank(bs.hstack(shifted))==5,
            'both_relations':all(c.same(c.field_word(w,ws)[0],c.eye(5,k)) for w in rels),
            'wrong_primitive_rejected':not c.same(c.inv(wrong)*wl*wrong,
                                                 lift(vl,c.zero(4,1,k)))}
    beta=s.Matrix([[1,0],[0,2],[0,0],[0,0]])
    acc=s.zeros(5)
    for i in range(2):
        z=s.zeros(5);z[:4,4]=beta[:,i]
        a=(z-z.H)/2;psi=(z+z.H)/2
        acc-=a*psi-psi*a
    bb=beta*beta.H;target=s.zeros(5);target[:4,:4]=-bb/2
    target[4,4]=s.trace(bb)/2
    checks['multiform_actual_commutator']=acc==target
    checks['multiform_quartic']=s.trace(acc*acc)==s.Rational(21,2)
    out={'checks':checks,'primitive':[str(x) for row in u.to_list() for x in row],
         'passed':sum(checks.values()),'total':len(checks),'all_checks_pass':all(checks.values())}
    print(json.dumps(out,sort_keys=True),flush=True)
    return out


if __name__=='__main__':
    raise SystemExit(0 if run()['all_checks_pass'] else 1)
