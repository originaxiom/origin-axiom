"""B1419 deep pass: the seven positive slopes whose invariant trace field exceeded degree 24 (their mirrors
(-p,q) are isometric to them by the amphichirality of m004, B740's verified shortcut, so share the field).
Degree cap 32, precision 2000 bits, as B740's b740_deep.py.  Signature decides: more than one complex place
=> not arithmetic.  A one-complex-place field would be sent to the Hilbert-symbol test."""
import json, snappy
from sage.all import *
out=[]
for p,q in [(1,7),(1,8),(3,7),(3,8),(5,7),(5,8),(7,8)]:
    M=snappy.Manifold('m004(%d,%d)'%(p,q)); res=None
    for prec,deg in ((2000,32),(3000,40)):
        try: res=M.invariant_trace_field_gens().find_field(prec=prec,degree=deg,optimize=True)
        except Exception: res=None
        if res: break
    if res:
        K=res[0]; row={'slope':[p,q],'degree':int(K.degree()),'signature':[int(x) for x in K.signature()],'field':str(K.polynomial()),
                       'arithmetic': (False if K.signature()[1]!=1 else 'needs Hilbert test'),'mirror':[-p,q]}
    else:
        row={'slope':[p,q],'degree':'>40','arithmetic':'undetermined','mirror':[-p,q]}
    print(json.dumps(row),flush=True); out.append(row)
json.dump(out,open('deep_stragglers.json','w'),indent=1)
