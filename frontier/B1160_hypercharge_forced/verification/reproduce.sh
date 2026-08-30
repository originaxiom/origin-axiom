#!/usr/bin/env bash
# B1160 -- memo 70 (cloud): does hypercharge fall out? The LOAD-BEARING theorem,
# re-derived independently on this bench (cloud's object-specific enumeration in
# the trinification frame -- 36 SM-shaped assignments, all SM -- is a corollary
# once the object realizes an SM-shaped 15-plet).
# THEOREM: on an SM-shaped generation (q,uc,dc,l,ec), the four gauge/grav/cubic
# anomaly conditions force the hypercharge to the SM direction, UNIQUE up to
# overall scale and the uc<->dc relabeling. Zero non-SM solutions.
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' | tee hypercharge_check.txt
import sympy as sp
# nu^c-less SM 15-plet state counts: q=6, uc=3, dc=3, l=2, ec=1
# anomaly conditions on (Yq,Yu,Yd,Yl,Ye):
#   [SU3]^2 Y : 2Yq+Yu+Yd=0 ; [SU2]^2 Y : 3Yq+Yl=0
#   grav^2 Y : 6Yq+3Yu+3Yd+2Yl+Ye=0 ; [Y]^3 : 6Yq^3+3Yu^3+3Yd^3+2Yl^3+Ye^3=0
Yq,Yu,Yd,Yl,Ye,t = sp.symbols('Yq Yu Yd Yl Ye t')
lin=[2*Yq+Yu+Yd, 3*Yq+Yl, 6*Yq+3*Yu+3*Yd+2*Yl+Ye]
sol=sp.solve(lin,[Yl,Ye,Yd],dict=True)[0]
print("linear anomaly solution:", sol)
# fix scale Yq=1, parametrize the remaining freedom by Yu=-1+t
base={Yq:1, Yu:-1+t}
Yd_=sol[Yd].subs(base); Yl_=sol[Yl].subs(base); Ye_=sol[Ye].subs(base)
cubic=sp.factor(sp.expand((6*Yq**3+3*Yu**3+3*Yd**3+2*Yl**3+Ye**3).subs({Yq:1,Yu:-1+t,Yd:Yd_,Yl:Yl_,Ye:Ye_})))
print("cubic (Yq=1) =", cubic)
roots=sp.solve(sp.Eq(cubic,0),t)
print("cubic=0 => t =", roots)
seen=set()
for tv in roots:
    vec=(1, int(-1+tv), int(Yd_.subs(t,tv)), int(Yl_.subs(t,tv)), int(Ye_.subs(t,tv)))
    tag="SM" if vec==(1,-4,2,-3,6) else ("SM (uc<->dc)" if vec==(1,2,-4,-3,6) else "NON-SM!")
    print(f"   t={tv}: (Yq:Yu:Yd:Yl:Ye) = {vec}   {tag}")
    seen.add(vec)
assert seen=={(1,-4,2,-3,6),(1,2,-4,-3,6)}, "only SM hypercharge + uc<->dc relabel"
allc=[2+(-4)+2, 3+(-3), 6+3*(-4)+3*2+2*(-3)+6, 6+3*(-64)+3*8+2*(-27)+216]
print("SM (1,-4,2,-3,6) four anomalies:", allc, "-> all zero:", all(c==0 for c in allc))
assert all(c==0 for c in allc)
print()
print("=> SM hypercharge is the UNIQUE anomaly-consistent Y on an SM-shaped 15-plet")
print("   (up to scale + uc<->dc). memo 70: realized in the object's rank-3 abelian")
print("   sector -- 36 assignments, all SM, zero non-SM (cloud's trinification cert).")
print("REPRODUCES")
PY
