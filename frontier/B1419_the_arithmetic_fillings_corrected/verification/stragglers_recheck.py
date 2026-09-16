"""Re-run the two grid slopes B740 resolved (degrees 18, 19) that the census's degree-24 pass missed, at higher precision."""
import json, sys
import snappy
from sage.all import *
out=[]
for p,q in [(-7,5),(-3,5),(1,5),(7,5),(-1,5)]:
    M=snappy.Manifold('m004(%d,%d)'%(p,q))
    res=None
    for prec,deg in ((1200,24),(2000,24)):
        try: res=M.invariant_trace_field_gens().find_field(prec=prec,degree=deg,optimize=True)
        except Exception as e: res=None
        if res: break
    if res:
        K=res[0]; row={'slope':[p,q],'degree':int(K.degree()),'signature':[int(x) for x in K.signature()],'field':str(K.polynomial())}
        row['arithmetic']= False if K.signature()[1]!=1 else 'needs Hilbert test'
    else:
        row={'slope':[p,q],'degree':'>24','arithmetic':'undetermined'}
    print(json.dumps(row),flush=True); out.append(row)
json.dump(out,open('stragglers_recheck.json','w'),indent=1)
