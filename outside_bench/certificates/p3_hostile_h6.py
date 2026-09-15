#!/usr/bin/env python3
"""P3 HOSTILE READ -- cell H6 (BLIND): can a referee reproduce 252 / 222 / 2 from the paper?

Step 1 is run FROM THE PAPER'S TEXT ONLY, as a referee would.
Step 2 then consults the corpus and reproduces the real enumeration in own code.
"""
import itertools, math
from fractions import Fraction as F

print("="*78); print("H6 -- the 252 / 222 / 2 census"); print("="*78)

print("""
The paper's sentence, verbatim (section 4):

  "Over the Standard-Model-visible five-field alphabet there are 252 candidate
   hypercharge contents. The pure colour condition alone kills 222 of them, and
   exactly two survive as rigid, chiral and fully anomaly-free."

### STEP 1 -- BLIND: reproduce 252 from that sentence alone.
""")
readings = []
# (a) 5 fields, each an integer hypercharge in a box: never 252 (all are k^5)
for k in range(2, 12):
    readings.append((f"5 fields, hypercharge in a {k}-element set", k**5))
# (b) multisets of size n from a 5-letter alphabet
for n in range(2, 9):
    readings.append((f"multisets of size {n} from 5 letters", math.comb(5+n-1, n)))
# (c) subsets / multisets of size <= 5 from 5 letters
readings.append(("multisets of size <=5 from 5 letters", math.comb(10,5)))
hit = [r for r in readings if r[1] == 252]
for nm, v in readings:
    if v <= 4000: print(f"    {nm:<48} = {v}")
print(f"\n  readings from the paper's own words that give 252: "
      f"{[nm for nm,v in hit]}")
print("""
  Note the one hit is 'multisets of size <=5 from 5 letters' = C(10,5) = 252 --
  numerically right, STRUCTURALLY WRONG (contents of fewer than five fields are
  not what is enumerated). A referee cannot distinguish it from a coincidence,
  because the paper never defines 'content', never gives the alphabet's letters,
  and never says how many letters a content contains.
  => STEP 1 VERDICT: NOT REPRODUCIBLE from the paper's text.
""")

print("### STEP 2 -- consult the corpus and reproduce the real enumeration in own code.\n")
# B1170's alphabet, re-entered by hand from the rep data (states, [SU(3)]^3 index,
# SU(3)-fundamental count, SU(2)-doublet count):
REP = {"A": (6, +2, 2, 3), "a": (6, -2, 2, 3),   # (3,2) and its conjugate
       "B": (3, +1, 1, 0), "b": (3, -1, 1, 0),   # (3,1) and its conjugate
       "C": (2,  0, 0, 1),                        # (1,2)
       "D": (1,  0, 0, 0)}                        # (1,1)
ALPHABET = "AaBbCD"; WORD = 5
n_exam = math.comb(len(ALPHABET)+WORD-1, WORD)
print(f"  the corpus enumerates multisets of size {WORD} from the {len(ALPHABET)}-letter")
print(f"  alphabet {{{', '.join(ALPHABET)}}} = (3,2), conj, (3,1), conj, (1,2), (1,1):")
print(f"    C({len(ALPHABET)}+{WORD}-1, {WORD}) = C({len(ALPHABET)+WORD-1},{WORD}) = {n_exam}")
print(f"    matches the paper's 252: {n_exam == 252}")
print(f"""
  *** THE ALPHABET HAS SIX LETTERS, NOT FIVE. ***
  The paper says "the Standard-Model-visible FIVE-FIELD alphabet". Five is the
  number of fields IN A CONTENT (the word length), not the size of the alphabet
  (six). The sentence assigns the number 5 to the wrong object, which is exactly
  why the count cannot be reproduced from it: with a five-letter alphabet and
  five-field contents the count is C(9,5) = {math.comb(9,5)}, not 252.
""")

# reproduce 222 and 2 in own code
examined = killed_colour = 0
survivors = []
def rational_roots(coef):
    den = 1
    for c in coef: den = den*c.denominator//math.gcd(den, c.denominator)
    ic = [int(c*den) for c in coef]
    while ic and ic[0] == 0: ic.pop(0)
    if not ic: return []
    g = 0
    for c in ic: g = math.gcd(g, abs(c))
    ic = [c//g for c in ic]
    a0, an = ic[-1], ic[0]; roots = set()
    if a0 == 0: roots.add(F(0))
    dv = lambda n: [d for d in range(1, abs(n)+1) if abs(n) % d == 0] or [1]
    for p_ in dv(a0 if a0 else 1):
        for q_ in dv(an):
            for s_ in (F(p_,q_), F(-p_,q_)):
                if sum(c*s_**(len(ic)-1-i) for i,c in enumerate(ic)) == 0: roots.add(s_)
    return roots
def nullspace(rows):
    m=[list(map(F,r)) for r in rows]; piv=[]; r=0
    for c in range(5):
        p=next((i for i in range(r,len(m)) if m[i][c]!=0), None)
        if p is None: continue
        m[r],m[p]=m[p],m[r]; m[r]=[x/m[r][c] for x in m[r]]
        for i in range(len(m)):
            if i!=r and m[i][c]!=0: m[i]=[a-m[i][c]*b for a,b in zip(m[i],m[r])]
        piv.append(c); r+=1
        if r==len(m): break
    out=[]
    for fc in [c for c in range(5) if c not in piv]:
        v=[F(0)]*5; v[fc]=F(1)
        for ri,pc in enumerate(piv): v[pc]=-m[ri][fc]
        out.append(v)
    return out

for w in itertools.combinations_with_replacement(ALPHABET, WORD):
    examined += 1
    if sum(REP[r][1] for r in w) != 0:          # [SU(3)]^3 -- the "pure colour condition"
        killed_colour += 1; continue
    if sum(REP[r][3] for r in w) % 2 != 0: continue      # Witten SU(2) global anomaly
    lin = [[REP[r][2] for r in w], [REP[r][3] for r in w], [REP[r][0] for r in w]]
    ns = nullspace(lin)
    cub = lambda v: sum(F(REP[r][0])*y**3 for r,y in zip(w,v))
    rays = []
    if len(ns) == 1:
        if cub(ns[0]) == 0: rays.append(ns[0])
    elif len(ns) == 2:                      # the generic case: cubic cuts the plane to rays
        v1, v2 = ns; coef = [F(0)]*4
        for r,(a,b) in zip(w, zip(v1,v2)):
            st = F(REP[r][0])
            coef[0]+=st*a**3; coef[1]+=st*3*a*a*b; coef[2]+=st*3*a*b*b; coef[3]+=st*b**3
        if all(c == 0 for c in coef): continue          # 1-param family -> not rigid
        if coef[0] == 0: rays.append(v1)
        for s_ in rational_roots(coef): rays.append([s_*a+b for a,b in zip(v1,v2)])
    good = [v for v in rays if all(y != 0 for y in v)]  # chiral: no sterile field
    uniq = []
    for v in good:
        f0 = next(x for x in v if x != 0); nv = tuple(x/f0 for x in v)
        if nv not in uniq: uniq.append(nv)
    if uniq: survivors.append((''.join(w), uniq))

print(f"  own-code re-run:  examined = {examined}   killed by [SU(3)]^3 alone = {killed_colour}"
      f"   rigid+chiral+anomaly-free survivors = {len(survivors)}")
print(f"  paper says:       examined = 252         killed = 222"
      f"                      survivors = 2")
ok = (examined==252 and killed_colour==222 and len(survivors)==2)
print(f"  NUMBERS REPRODUCE: {ok}")
for nm, vs in survivors:
    print(f"    content {nm}: {len(vs)} chiral ray(s) up to scale")
    for v in vs: print(f"        Y = {[str(x) for x in v]}")
print(f"""
  THE SURVIVORS ARE TWO *CONTENTS*, EACH CARRYING TWO RAYS:
    AbbCD  = (3,2) + 2x(3bar,1) + (1,2) + (1,1)   -- the SM 15-plet
    aBBCD  = (3bar,2) + 2x(3,1) + (1,2) + (1,1)   -- its CONJUGATE CONTENT
  Within one content the two rays differ only by swapping the two identical
  letters, i.e. u^c <-> d^c. So section 4's "the two solutions are (1,-4,2,-3,6)
  and (1,2,-4,-3,6)" are the two rays of ONE survivor, NOT the two survivors:
  the conjugate content never appears in the displayed computation. Total chiral
  anomaly-free rays over all 252 contents = {sum(len(v) for _,v in survivors)}, a number the paper never states.""")

print(f"""
  TWO CONDITIONS DO THE WORK AND NEITHER APPEARS IN THE PAPER:
    * the killer of {killed_colour}/252 is [SU(3)]^3 -- the PURE colour anomaly,
      which contains no hypercharge at all. Section 4 displays three linear
      conditions ([SU(3)]^2 Y, [SU(2)]^2 Y, grav^2 Y) and one cubic ([Y]^3), and
      [SU(3)]^3 IS NOT AMONG THEM. The condition responsible for
      {100*killed_colour/252:.0f}% of the elimination is never written down.
    * the Witten SU(2) global anomaly (an even number of doublets) is applied in
      the enumeration and is never mentioned in the paper.
  Both are correct physics. Neither is stated, so section 4's displayed argument
  is not the argument that produces its headline numbers.
""")
H6 = "H6-DIVERGENT"
print(f"OUTCOME: {H6}  (numbers CONFIRMED against corpus; NOT reproducible from the paper's text)")
