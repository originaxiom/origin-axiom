#!/usr/bin/env python3
"""The coverage-free certificate (answering the audit lane's R92) on the amphichiral cusped census manifolds outside the
family: for every spin structure s = rho (x) chi, is the odd twisted Alexander function real up to a unit at real t?
A mirror-invariant s would force it; so 'no torsion-real spin structure' certifies 'no mirror-invariant spin structure'
without enumerating isometries, and 'R^{(s0)} not real' certifies that no reversing isometry fixes the geometric lift."""
import sys, json, warnings; warnings.filterwarnings("ignore")
import pathlib
F=str(next(p for p in pathlib.Path(__file__).resolve().parents if p.name == "frontier"))+"/"
for d in ("B1471_the_cancellation_is_a_theorem_of_amphichirality","B1474_the_spin_swap_phase_1a_fix_or_swap_by_the_matrix_route","B1475_the_spin_swap_phase_1b_does_the_swap_carry_a_quantity"):
    sys.path.insert(0, F+d+"/verification")
import realness as R, spin_quantity as SQ
from mpmath import mpf
cu=json.load(open(F+"B1476_the_spin_swap_phase_1c_the_quarter_law_the_pin_bit_and_what_a5_chose/verification/census_swap_cusped.json"))
out={}
for nm,v in cu.items():
    pk,err=R.setup(nm)
    if err: out[nm]=dict(error=err, cs=v["cs_class"], verdict=v.get("verdict")); print(nm,"ERR",err); continue
    chars=SQ.characters(pk); gens=pk["gens"]; rows=[]
    for chi in chars:
        pk2=dict(pk); pk2["rho"]={g: chi[g]*pk["rho"][g] for g in gens}
        real=True; vals={}
        for n in (1,3):
            W=R.Wada(pk2,n)
            for t in (mpf(2), mpf(3), mpf("0.6")):
                z=W.value(t)
                if z is None: real=None; break
                z=complex(z); vals["%d@%s"%(n,t)]=z
                if min(abs(z.imag),abs(z.real)) > 1e-9*max(1,abs(z)): real=False
            if real is None: break
        rows.append(dict(chi=tuple(chi[g] for g in gens), real=real, R1_at_2=str(vals.get("1@2.0"))))
    nreal=sum(1 for r in rows if r["real"]); s0=[r for r in rows if all(x==1 for x in r["chi"])][0]
    out[nm]=dict(cs=v["cs_class"], verdict=v.get("verdict"), n_spin=len(rows), torsion_real=nreal, s0_real=s0["real"], rows=rows)
    print("%-6s CS %-7s witness-verdict %-28s | spin %d, torsion-real %d, s0 real: %s" % (nm, v["cs_class"], v.get("verdict"), len(rows), nreal, s0["real"]), flush=True)
json.dump(out, open(pathlib.Path(__file__).resolve().parent / "r92_certificate.json","w"), indent=1, default=str)
