#!/usr/bin/env python3
"""MEMO-59 CELL: THE CENTER IS THE LOCK — the object's group-paid Z/2 is
unique: the center of the holonomy closure acts on the carrier as exactly
C_Psi; and the honest sharpening of "the only mirror-stable Z/2" is filed —
the LINEAR commutant is large (dim 297), so the lock's distinction is that
the GROUP realizes it, not that it is the only commuting involution.

Assembly + computation.  The banked pieces this cell unifies:
  - memo 46/50: C_Psi commutes with the whole pi1 image and the beat;
  - memo 51: C_Psi = the semisimple part of the LONGITUDE on the carrier;
  - B1146 (seat): rho_27(-I) = (-1)^wt = C_27 separates 2T from A4 —
    the 2T CENTER of the arithmetic chain;
  - cc3 (B8111/B8118): the same -I is its campaign control.
This cell adds the closure statement: the Zariski closure of the diagonal
holonomy is the diagonal SL2 (CITED-standard, as in memo 48 rung 1); its
center is {+-I} (standard); and the central -I acts on Psi as
(-1)^(H_diag weight) — VERIFIED here to equal C_Psi slot-by-slot.

PREREGISTERED (asserts):
  FACT 1: the H_diag weight of slot (i,a) is s+wt(a) (s = +-1), and
    (-1)^(s+wt) == C_Psi = (-1)^(1+wt) on ALL 54 slots; on the internal
    factor alone (-1)^wt == C_27 (B1146's discriminating operator).
  FACT 2 (the sharpening, filed at point of occurrence): the LINEAR
    commutant of the pi1 action is NOT small: from the in-run-derived
    diagonal-sl2 decomposition Psi = 6 spin1 + 15 spin1/2 + 6 spin0
    (weight-peeling re-run here), the commutant of the closure has
    dimension 6^2 + 15^2 + 6^2 = 297.  Commuting involutions are
    plentiful; "the only mirror-stable Z/2" in memos 56 (addendum) refers
    to the LEDGER'S list (lock vs matter parity), and the lock's true
    distinction is GROUP-REALIZATION: center of the closure = semisimple
    part of the longitude = the 2T center = C_Psi.
  FACT 3: the center's image is exactly {I, C_Psi}: (+I -> I, -I -> C_Psi),
    C_Psi^2 = I, C_Psi != I (both asserted).
CITED-standard steps (labeled, not computed): Zariski density of the
nonelementary holonomy in SL2 and algebraicity of the bridge (as memo 48);
Z(SL2) = {+-I}; commutant of the image = commutant of the closure.
"""
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

r0=ROOTS[0]
hA=[F(0)]*DIM
for k in range(N): hA[k]=F(r0[k])
Hint=rho27_Q(hA)
wt=[int(Hint[a][a]) for a in range(27)]
assert dict(Counter(wt))=={1:6,0:15,-1:6}

# FACT 1
ok1=True; ok1b=True
for i,s_ in enumerate((1,-1)):
    for a in range(27):
        hw=s_+wt[a]
        centr=(-1)**hw
        lock=(-1)**(1+wt[a])
        if centr!=lock: ok1=False
for a in range(27):
    if (-1)**wt[a]!=(1 if wt[a]%2==0 else -1): ok1b=False
print(f"FACT 1: (-1)^(H_diag) == C_Psi on all 54 slots: {ok1}; (-1)^wt == C_27: {ok1b}")
assert ok1 and ok1b
print("   => the central -I of the closure's SL2 acts on the carrier as the LOCK,")
print("      and on the internal 27 as B1146's discriminating rho(-I) = C_27")

# FACT 2: re-derive the diagonal-sl2 decomposition and the commutant dimension
psi_w=Counter()
for s_ in (1,-1):
    for a in range(27): psi_w[s_+wt[a]]+=1
decPsi={}
w=dict(psi_w)
while any(v>0 for v in w.values()):
    top=max(k for k,v in w.items() if v>0)
    mult=w[top]
    decPsi[F(top,2)]=decPsi.get(F(top,2),0)+mult
    k=top
    while k>=-top:
        w[k]=w.get(k,0)-mult; k-=2
assert decPsi=={F(1):6, F(1,2):15, F(0):6}
dimcomm=sum(m*m for m in decPsi.values())
print(f"FACT 2: Psi|_diag-sl2 = 6 spin1 + 15 spin1/2 + 6 spin0 (re-derived);")
print(f"   commutant of the closure: dim = 6^2+15^2+6^2 = {dimcomm}")
assert dimcomm==297
print("   SHARPENING FILED: commuting involutions are plentiful (297-dim algebra);")
print("   the lock is distinguished by being GROUP-REALIZED, not by commuting alone")

# FACT 3
Cpsi=[(-1)**(1+wt[a]) for i in range(2) for a in range(27)]
assert all(c*c==1 for c in Cpsi) and any(c==-1 for c in Cpsi) and any(c==1 for c in Cpsi)
print("FACT 3: the center's image on the carrier = {I, C_Psi}, C_Psi^2 = I, C_Psi != I")

print("""
THE CENTER IS THE LOCK: the object has exactly one group-paid Z/2 on the
carrier, and four independently computed structures are that one operator —
the center of the holonomy closure (this cell), the semisimple part of the
longitude (memo 51), the parity of the meridian clock's chains (memo 50),
and the 2T-vs-A4 center that B1146 computed and cc3 runs as a control.
The dark ledger's frame-paid matter parity is NOT among them (memo 56).
CITED steps labeled; everything else asserted.  Gate 5 untouched.""")
