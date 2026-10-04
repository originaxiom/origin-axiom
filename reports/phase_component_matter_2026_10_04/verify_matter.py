"""Exact field arithmetic for actual new E and exterior-square coefficients."""
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "global_quotient_admission_2026_09_27"))
import verify_monomial_lifts as lattice
sys.path.insert(0, str(HERE.parent / "monomial_exceptional_locus_2026_09_27"))
import verify_exceptional as ex
from verify_relative_capacity import relative_h1
from verify_global_seed import Rep, eye, kron, zero
from flint import fmpq, fmpq_mat

Z = fmpq_mat([[0,-1],[1,-1]])
TRACE = fmpq_mat([[2,-1],[-1,-1]])
GRAM = fmpq_mat([[1,"-1/2"],["-1/2",1]])


def inputs():
    return json.loads((HERE/"INPUTS.json").read_text())


def phases(number):
    rows = json.loads((HERE.parents[1]/inputs()["component_source"]).read_text())
    assert rows[number]["seed"] == number and rows[number]["residual_component_count"] == 3
    witness = rows[number]["order_three_witnesses"][0]
    assert witness["modulus"] == 3
    return witness["generator_output_phases"]


def coefficient_data(number, component, name):
    permutations, cocycle = lattice.action_and_cocycle(number)
    pp = phases(number)
    base = [(p, tuple(int(x) for x in cocycle[5*j:5*j+5,0]),
             tuple(component*x % 3 for x in pp[j]), (1,)*5) for j,p in enumerate(permutations)]
    if name == "E":
        return base
    assert name == "wedge2E"
    pairs = list(combinations(range(5),2))
    index = {v:i for i,v in enumerate(pairs)}
    out=[]
    for p,v,a,sign in base:
        wp,wv,wa,ws=[0]*10,[0]*10,[0]*10,[0]*10
        for j,(i,k) in enumerate(pairs):
            x,y=p[i],p[k]
            dest=index[tuple(sorted((x,y)))]
            wp[j],wv[dest],wa[dest],ws[dest]=dest,v[x]+v[y],(a[x]+a[y])%3,1 if x<y else -1
        out.append((tuple(wp),tuple(wv),tuple(wa),tuple(ws)))
    return out


def actual_dual_data(gens):
    return [(p,tuple(-x for x in v),tuple(-x%3 for x in a),s) for p,v,a,s in gens]


def matrix(g,t):
    p,v,a,s=g
    result=zero(2*len(p),2*len(p))
    for j,i in enumerate(p):
        block=fmpq(t)**v[i]*s[i]*(Z**a[i])
        for r in range(2):
            for k in range(2):
                result[2*i+r,2*j+k]=block[r,k]
    return result


def representation(number,component,t,name):
    gens=coefficient_data(number,component,name)
    return Rep([matrix(g,t) for g in gens])


def field_block(a,i,j):
    return fmpq_mat([[a[2*i+r,2*j+k] for k in range(2)] for r in range(2)])


def exterior_control(number,component,t):
    e=representation(number,component,t,"E")
    w=representation(number,component,t,"wedge2E")
    pairs=list(combinations(range(5),2))
    for a,b in zip(e.mats,w.mats):
        for i,(r,s) in enumerate(pairs):
            for j,(k,l) in enumerate(pairs):
                expected=field_block(a,r,k)*field_block(a,s,l)-field_block(a,r,l)*field_block(a,s,k)
                assert field_block(b,i,j)==expected
    return True


@lru_cache(None)
def point(number,component,t):
    assert Z**2+Z+eye(2)==zero(2,2)
    assert TRACE.det()!=0 and GRAM.det()>0 and GRAM[0,0]>0
    assert Z.transpose()*GRAM*Z==GRAM
    assert Z.transpose()*TRACE==TRACE*Z
    assert exterior_control(number,component,t)
    result={"seed":number,"component":component,"t":t,"coefficients":{}}
    for name in ("E","wedge2E"):
        gens=coefficient_data(number,component,name)
        rep=representation(number,component,t,name)
        d=len(gens[0][0])
        pairing=kron(eye(d),TRACE)
        literal_dual=Rep([matrix(g,t) for g in actual_dual_data(gens)])
        assert rep.dual().mats==[pairing*a*pairing.inv() for a in literal_dual.mats]
        rels,mu,lam=ex.cover(6)
        assert all(rep.word(r)==eye(rep.d) for r in rels)
        assert rep.word(mu)==eye(rep.d)
        # The new finite phases do not change either marked peripheral matrix.
        reference=representation(number,0,1,name)
        assert rep.word(lam)==reference.word(lam)
        gram=kron(eye(d),GRAM)
        unitary=all(a.transpose()*gram*a==gram for a in rep.mats)
        assert unitary==(abs(t)==1)
        index,_=ex.indexed(rep,6,2)
        actual,_=ex.cohom(literal_dual,6,2)
        assert actual==index["dual"]
        rel=relative_h1(rep,6,2)
        rel_dual=relative_h1(literal_dual,6,2)
        n=index["V"][1]-index["V"][4]
        nd=index["dual"][1]-index["dual"][4]
        assert n==rel["interior"] and nd==rel_dual["interior"] and index["I"]==n-nd
        if unitary:
            assert n==nd and index["I"]==0
        result["coefficients"][name]={"ordinary":index,"n":n,"n_dual":nd,
                                      "relative_n":rel["interior"],"relative_dual_n":rel_dual["interior"],
                                      "unitary":unitary}
    result["selected_point_only"]=True
    result["physical_chirality_derived"]=False
    return result


def controls():
    old=[]
    for number in range(2):
        row=point(number,0,2)
        assert all(x["n"]==x["n_dual"]==0 for x in row["coefficients"].values())
        for name in ("E","wedge2E"):
            assert representation(number,1,2,name).mats!=representation(number,0,2,name).mats
        old.append(row)
    return {"old_component_zero_at2_recovered":True,"phase_input_changes_both_coefficients":True,
            "old_points":old}


def run():
    print("CONTROLS",json.dumps(controls()),flush=True)
    for number in range(2):
        for component in inputs()["classes"]:
            for t in inputs()["parameters"]:
                print("POINT",json.dumps(point(number,component,t)),flush=True)
    print("PASS: exact selected-point spectrum; all-parameter behavior remains unclassified")


if __name__=="__main__":
    run()
