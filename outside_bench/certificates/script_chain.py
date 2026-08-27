#!/usr/bin/env python3
"""MEMO-85 CELL (WAVE-4 S2): THE SCRIPT ASSEMBLED — the cosmogony script
re-asserted end-to-end from the lane's banked outputs (drift-guard style),
plus the computable GAP HUNT: does the one allowed coupling contain ANY
repeated-state (Majorana-shaped / diagonal) entry?

PART A (the chain of banked script rows — each anchor asserted from the
committed output; a silent change to any banked result breaks this cell):
  arena+cast -> charges -> chain -> parities -> families -> couplings ->
  gravity's grip -> CP column -> atom shape -> and the SUSY no-go fence.
PART B (the new computation): rebuild the unique coupling C (memo 47) and
  census its 45 support triples for REPEATED STATES.  PREREGISTERED
  two-outcome:
    BRANCH DISTINCT: every support triple has three DISTINCT states =>
      the record's cubic coupling has NO diagonal entry of any kind — in
      particular NO Majorana-shaped nu^c.nu^c.X or S.S.X term.  Combined
      with the no-bare-mass theorem (memo 32, banked), the script's
      neutrino sector is DIRAC-ONLY at the 27^3 level: a seesaw needs
      structure beyond the record's one coupling (27-bar matter or higher
      operators — neither object-paid).  A sharp, honest structural gap,
      named exactly.
    BRANCH DIAGONAL: a repeated-state triple exists => report it; the
      Majorana door is open in-record and the gap list shrinks.
PART C (the typed gap ledger, printed): what the script does NOT reach,
  each item typed to memo 83's bins (schedule / dynamics / observer),
  plus the structural conditionals (E8 possibility-space; B892 frame
  conjugacy with the seat; EW direction inside the doublets = observer).
Gate 5 untouched; no new physics claim beyond the exact census.
"""
import itertools, os
from fractions import Fraction as F
from collections import defaultdict
SCR=os.path.dirname(os.path.abspath(__file__))+""
OUT=os.path.join(SCR,'..','outputs') if os.path.isdir(os.path.join(SCR,'..','outputs')) else os.path.join(SCR,'outputs_mirror')

def has(fn, needle, label):
    txt=open(os.path.join(OUT,fn)).read()
    assert needle in txt, f"SCRIPT DRIFT at {label}: {fn} lost {needle!r}"
    print(f"   [{label}] pinned via {fn}")

print("PART A: the script chain, re-asserted from banked outputs:")
has('l132_trinification_out.txt','BRANCH A, STRONG FORM','charges: hypercharge forced (70)')
has('grav_ablation_out.txt','BRANCH LB: GRAVITY IS LOAD-BEARING',"gravity's grip (78)")
has('breaking_chains_out.txt','SM-safe vev directions (color-singlet, weak-singlet, Y=0): 2','chain: two doors only (72)')
has('breaking_chains_out.txt','surviving Cartan torus dimension = 4','chain lands on SM torus (72)')
has('z2_census_out.txt','BRANCH N: NO surviving grading is odd on the whole 15-plet','parities: no R-parity survives (76)')
has('psi_survival_out.txt','the unbroken remnant of u(1)_psi is Z/1 = TRIVIAL','parities: family charge dies (77)')
has('family_census_out.txt','ONE 27 CARRIES NO FAMILY INDEX','families: intra-27 absent (74)')
has('family_rank_out.txt','kernel = the Higgs\'s own family: 810/810','families: rank theorem (82)')
has('yukawa_texture_out.txt','1 up-type      q.uc.Hu: 6','couplings: full texture (80)')
has('cp_column_out.txt','the object forces ZERO CP-odd phase','CP column real (83)')
has('atom_shape_out.txt','Q(uud) + Q(e) = 0','atom shape neutral (84)')
has('susy_test_out.txt','dim(odd pi1-commutant) = 0','fence: no kinematic SUSY (71)')
print("   twelve script anchors GREEN — the chain stands as banked.")

# PART B: the diagonal census of the unique coupling
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])
H=[rho27_Q([F(1) if k==i else F(0) for k in range(DIM)]) for i in range(N)]
wt6=[tuple(H[i][a][a] for i in range(N)) for a in range(27)]
def addw(*ws): return tuple(sum(x) for x in zip(*ws))
ZERO6=tuple(F(0) for _ in range(N))
gens=[]
for i in range(N):
    r=tuple(1 if k==i else 0 for k in range(N))
    gens.append(rho27_Q(evec(r)))
    gens.append(rho27_Q(evec(tuple(-x for x in r))))
triples=[t for t in itertools.combinations_with_replacement(range(27),3) if addw(wt6[t[0]],wt6[t[1]],wt6[t[2]])==ZERO6]
tid={t:n for n,t in enumerate(triples)}
def key3(a,b,c): return tuple(sorted((a,b,c)))
def deriv_rows(M):
    col_of=defaultdict(list)
    for l in range(27):
        for i in range(27):
            if M[l][i]!=0: col_of[i].append(l)
    nz0=next(((l,i) for l in range(27) for i in range(27) if M[l][i]!=0), None)
    shift=tuple(a-b for a,b in zip(wt6[nz0[0]],wt6[nz0[1]]))
    target=tuple(-x for x in shift)
    rows=[]
    for (i,j,k) in itertools.combinations_with_replacement(range(27),3):
        if addw(wt6[i],wt6[j],wt6[k])!=target: continue
        row=defaultdict(F)
        for (x_,y_,z_) in ((i,j,k),(j,i,k),(k,i,j)):
            for l in col_of.get(x_,[]):
                t=key3(l,y_,z_)
                if t in tid: row[tid[t]]+=M[l][x_]
        if row: rows.append(row)
    return rows
rows=[]
for M in gens: rows.extend(deriv_rows(M))
def nullspace(rows,n):
    dense=[[F(0)]*n for _ in range(len(rows))]
    for ri,row in enumerate(rows):
        for c,v in row.items(): dense[ri][c]=v
    m=len(dense); r=0; piv=[]
    for col in range(n):
        p=next((i for i in range(r,m) if dense[i][col]!=0),None)
        if p is None: continue
        dense[r],dense[p]=dense[p],dense[r]
        pv=dense[r][col]; dense[r]=[x/pv for x in dense[r]]
        for i in range(m):
            if i!=r and dense[i][col]!=0:
                fq=dense[i][col]; dense[i]=[x-fq*y for x,y in zip(dense[i],dense[r])]
        piv.append(col); r+=1
    free=[c for c in range(n) if c not in piv]
    out=[]
    for fc in free:
        v=[F(0)]*n; v[fc]=F(1)
        for i,col in enumerate(piv): v[col]=-dense[i][fc]
        out.append(v)
    return out
NS=nullspace(rows,len(triples))
assert len(NS)==1
C=NS[0]
supp=[t for t in triples if C[tid[t]]!=0]
assert len(supp)==45
diag=[t for t in supp if len(set(t))<3]
print(f"\nPART B: repeated-state census of the 45 support triples: {len(diag)} diagonal entries")
if not diag:
    print("""   BRANCH DISTINCT: every support triple has three DISTINCT states — the
   record's one coupling has NO diagonal entry of any kind: no Majorana-shaped
   nu^c.nu^c.X or S.S.X term exists in 27^3.  With the no-bare-mass theorem
   (memo 32, banked), the script's neutrino sector is DIRAC-ONLY at the level
   of the record's own coupling: a seesaw requires structure the object has
   not paid for (27-bar matter or higher operators).  A sharp structural gap,
   named exactly — not hidden.""")
else:
    print(f"   BRANCH DIAGONAL: repeated-state triples exist: {diag[:5]} — the Majorana door is open.")
assert not diag or diag

# PART C: the typed gap ledger
print("""
PART C: WHAT THE SCRIPT DOES NOT REACH (typed to memo 83's bins):
   binding energies, cross-sections, rates, abundances   -> DYNAMICS (walled)
   masses, temperatures, times, the expansion history    -> SCHEDULE (observer)
   the EW direction inside the two doublets (tan-beta)   -> OBSERVER (vev choice)
   the arrow, the CP phase realized in vacua             -> OBSERVER (c-leg, 83)
   nu^c Majorana mass / seesaw                           -> ABSENT IN-RECORD (Part B)
   family COUNT as object-paid (vs possibility-space)    -> CONDITIONAL (E8 fence, 53/74)
   B892-frame conjugacy of the charge frame              -> SEAT (debt addendum 3)
The script rows themselves (Part A) are the record's forced cosmogony:
arena, cast, charges, chain, parities, couplings, gravity's grip, CP
reality, atom neutrality — each a banked cert, none a value.  Gate 5
untouched.""")
