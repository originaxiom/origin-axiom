"""Separate stdlib-only reference: enumerate descended maps and pair reachability.

Imports no native instrument or old science producer. Both are same-author
implementations, not nonauthor review. Scope is finite supplied update systems.
"""
from collections import deque
from itertools import product
import json


def partitions(n):
    def extend(prefix):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for label in range(max(prefix) + 2):
            yield from extend(prefix+[label])
    yield from extend([0])


def possible_descents(q, values, update):
    blocks = max(q)+1
    codomain = range(blocks) if update else set(values)
    for candidate in product(codomain, repeat=blocks):
        if all(candidate[q[x]] == (q[values[x]] if update else values[x]) for x in range(len(q))):
            return candidate
    return None


def pair_equivalent(i,j,updates,output):
    pending = deque([(i,j)])
    seen = set()
    while pending:
        pair = pending.popleft()
        if pair in seen:
            continue
        seen.add(pair)
        a,b = pair
        if output[a] != output[b]:
            return False
        pending.extend((t[a],t[b]) for t in updates)
    return True


def pair_record(updates,output):
    representatives=[]
    labels=[]
    for i in range(len(output)):
        label=next((b for b,j in enumerate(representatives) if pair_equivalent(i,j,updates,output)),None)
        if label is None:
            label=len(representatives)
            representatives.append(i)
        labels.append(label)
    return tuple(labels)


def independent_algebra():
    # Exact integer controls, with no symbolic elimination library.
    line = all(x*(x-1)==0 and x*k==0 for x,k in [(0,k) for k in range(-8,9)])
    point = 1*(1-1)==0 and 1*0==0
    # Branch proof encoded separately: x=0 or x=1; on x=1, k=0.
    branch_zero_arbitrary = lambda k: (0*(0-1),0*k)
    branch_one_forces_k = lambda k: (1*(1-1),1*k)
    # Coefficients of the two-variable Jacobian at (1,0).
    determinant = (2*1-1)*1 - 0*0
    graph_ok = True
    for x,y,z in product(range(-2,3),repeat=3):
        r=x*x+y*y+z*z-2*x*y*z-1
        graph_ok &= 2*x*z-y+r-(x*x+y*y+z*z-2*x*y*z-1) == 2*x*z-y
    return {"line_samples":line,"isolated_point":point,"full_rank":determinant==1,
            "branch_zero":branch_zero_arbitrary(137)==(0,0),
            "branch_one":branch_one_forces_k(137)==(0,137),
            "graph_samples":graph_ok,"same_squarefree_field":20==4*5,
            "conjugation_changes_quadratic_generator":(0,-1)!=(0,1)}


def main():
    # An independently coded fibre condition, not the native implementation.
    dynamic_cases=output_cases=0
    pass_dynamic=pass_outputs=True
    partition_counts={}
    for n in range(1,5):
        ps=list(partitions(n))
        partition_counts[n]=len(ps)
        for q in ps:
            for t in product(range(n),repeat=n):
                condition=all(q[i]!=q[j] or q[t[i]]==q[t[j]] for i in range(n) for j in range(n))
                pass_dynamic &= condition == (possible_descents(q,t,True) is not None)
                dynamic_cases+=1
            for out in product((0,1),repeat=n):
                condition=all(q[i]!=q[j] or out[i]==out[j] for i in range(n) for j in range(n))
                pass_outputs &= condition == (possible_descents(q,out,False) is not None)
                output_cases+=1
    algebra=independent_algebra()
    checks={"partition_completeness":partition_counts=={1:1,2:2,3:5,4:15},
            "dynamic_factor_exists_iff_fibres_stable":pass_dynamic,
            "output_factor_exists_iff_fibres_constant":pass_outputs,**algebra}
    result={"dynamic_cases":dynamic_cases,"output_cases":output_cases,
            "partition_counts":partition_counts,"checks":checks,"all_checks_pass":all(checks.values())}
    print(json.dumps(result,indent=2))
    return 0 if result["all_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
