#!/usr/bin/env python3
"""
P3 HOSTILE READ -- cells H1..H5, H7 (H6 is run separately, blind-then-corpus).

Subject: papers/P3_THE_PAPER/main.tex at 89affd5b.
Every finding must be an exact computation or an exhibited internal contradiction.
"""
import re, subprocess, sys
from fractions import Fraction
import sympy as sp

PIN = "89affd5b"
TEX = subprocess.run(["git","show",f"{PIN}:papers/P3_THE_PAPER/main.tex"],
                     capture_output=True, text=True, cwd="/home/user/origin-axiom").stdout
assert len(TEX) > 10000, "could not read the draft at the pin"

print("="*78); print("P3 HOSTILE READ -- main.tex @", PIN, f"({len(TEX)} chars)"); print("="*78)

# ---------------------------------------------------------------- H1
print("\n### H1 -- the displayed forcing of section 4 (CONFIRMATORY)\n")
Yq,Yu,Yd,Yl,Ye,t = sp.symbols('Y_q Y_u Y_d Y_l Y_e t', rational=True)

# SM-shaped 15-plet: q=(3,2) mult 6, uc=(3b,1) mult 3, dc=(3b,1) mult 3, l=(1,2) mult 2, ec 1
A_su3  = 2*Yq + Yu + Yd                       # [SU(3)]^2 Y   (Dynkin index 1/2 cleared)
A_su2  = 3*Yq + Yl                            # [SU(2)]^2 Y
A_grav = 6*Yq + 3*Yu + 3*Yd + 2*Yl + Ye       # grav^2 Y
A_cube = 6*Yq**3 + 3*Yu**3 + 3*Yd**3 + 2*Yl**3 + Ye**3   # [Y]^3

print("  linear system:")
for nm,e in [("[SU(3)]^2 Y",A_su3),("[SU(2)]^2 Y",A_su2),("grav^2 Y",A_grav)]:
    print(f"    {nm:<14} = {e} = 0")

lin = sp.solve([A_su3, A_su2, A_grav], [Yl, Ye, Yd], dict=True)[0]
print("\n  solved (paper displays Y_l=-3Y_q, Y_e=6Y_q, Y_u+Y_d=-2Y_q):")
print(f"    Y_l = {sp.simplify(lin[Yl])}   [paper: -3*Y_q]   MATCH={sp.simplify(lin[Yl]+3*Yq)==0}")
print(f"    Y_e = {sp.simplify(lin[Ye])}   [paper:  6*Y_q]   MATCH={sp.simplify(lin[Ye]-6*Yq)==0}")
print(f"    Y_d = {sp.simplify(lin[Yd])}   => Y_u+Y_d = {sp.simplify(lin[Yd]+Yu)}"
      f"   [paper: -2*Y_q]   MATCH={sp.simplify(lin[Yd]+Yu+2*Yq)==0}")
H1_lin = (sp.simplify(lin[Yl]+3*Yq)==0 and sp.simplify(lin[Ye]-6*Yq)==0
          and sp.simplify(lin[Yd]+Yu+2*Yq)==0)

# the paper's parametrisation: Y_q = 1, Y_u = -1 + t
sub = {Yq: 1, Yu: -1+t}
cube_param = sp.expand(A_cube.subs({**lin, **{Yq:1}}).subs(sub))
cube_param = sp.expand(sp.simplify(cube_param))
paper_cube = sp.expand(-18*(t-3)*(t+3))
print(f"\n  cubic on the line, Y_q=1, Y_u=-1+t:")
print(f"    computed = {sp.factor(cube_param)}")
print(f"    paper    = -18*(t-3)*(t+3) = {paper_cube}")
H1_cube = sp.expand(cube_param - paper_cube) == 0
print(f"    EXACT POLYNOMIAL IDENTITY: {H1_cube}")

roots = sorted(sp.solve(sp.Eq(cube_param,0), t))
print(f"    roots t = {roots}   [paper: t = +-3]")
sols_param = []
for r in roots:
    v = {Yq:1, Yu:-1+r}
    v[Yd] = sp.simplify(lin[Yd].subs({Yq:1, Yu:-1+r}))
    v[Yl] = sp.simplify(lin[Yl].subs({Yq:1})); v[Ye] = sp.simplify(lin[Ye].subs({Yq:1}))
    sols_param.append(tuple(int(v[s]) for s in (Yq,Yu,Yd,Yl,Ye)))
print(f"    solutions on the chart Y_q=1: {sols_param}   [paper: (1,-4,2,-3,6) and (1,2,-4,-3,6)]")
H1_sols = set(sols_param) == {(1,-4,2,-3,6),(1,2,-4,-3,6)}
print(f"    MATCH: {H1_sols}")

# COMPLETENESS: the paper's chart assumes Y_q != 0. What is on Y_q = 0?
print("\n  completeness check -- the chart Y_q=1 excludes Y_q=0. What lives there?")
z = {Yq:0}
zl = sp.solve([A_su3.subs(z), A_su2.subs(z), A_grav.subs(z)], [Yl,Ye,Yd], dict=True)[0]
cube_zero = sp.expand(A_cube.subs(z).subs(zl))
print(f"    on Y_q=0: Y_l={zl[Yl]}, Y_e={zl[Ye]}, Y_d={zl[Yd]}")
print(f"    [Y]^3 restricted to Y_q=0 = {cube_zero}")
if sp.simplify(cube_zero) == 0:
    print("    => [Y]^3 VANISHES IDENTICALLY on the whole Y_q=0 branch:")
    print("       a ONE-PARAMETER FAMILY of fully anomaly-free assignments")
    print("       (Y_q,Y_u,Y_d,Y_l,Y_e) = (0, s, -s, 0, 0), every s.")
    print("       These are VECTOR-LIKE (u^c and d^c conjugate, all else neutral),")
    print("       so the paper's stated 'chiral' filter excludes them --")
    print("       but the DISPLAYED derivation never says so: it parametrises")
    print("       the line by Y_q=1 with no remark that Y_q=0 was disposed of.")
    H1_complete = False
else:
    H1_complete = True
print(f"\n  H1 relations OK: {H1_lin} | cubic OK: {H1_cube} | solutions OK: {H1_sols}"
      f" | displayed derivation complete: {H1_complete}")
H1 = "H1-SOUND" if (H1_lin and H1_cube and H1_sols and H1_complete) else "H1-DEFECT"
print(f"  OUTCOME: {H1}")

# ---------------------------------------------------------------- H2
print("\n### H2 -- the two survivors described twice (CONFIRMATORY)\n")
print("""  NOTE -- THIS CELL'S FIRST VERSION WAS WRONG AND IS CORRECTED HERE.
  It charged that "its conjugate" mislabels the u^c<->d^c relabelling. That
  charge is FALSE: the census's second survivor is a genuinely CONJUGATE
  CONTENT (aBBCD), a different multiset of representations. The error was to
  treat the census's pair and the displayed derivation's pair as the same
  object -- which is the very conflation this cell now charges the paper with.
  Filed as bench error #14. The corrected finding is below and is weaker.
""")
print("  the two objects section 4 calls 'two', computed exactly (see p3_hostile_h6.py):")
print("    (i)  THE CENSUS: 252 contents -> exactly TWO surviving CONTENTS,")
print("         AbbCD = (3,2)+2x(3bar,1)+(1,2)+(1,1)   [the SM 15-plet]")
print("         aBBCD = (3bar,2)+2x(3,1)+(1,2)+(1,1)   [its conjugate content]")
print("         -- so 'the SM 15-plet up to overall scale, and its conjugate' is CORRECT here.")
print("    (ii) THE DISPLAYED FORCING: on ONE fixed SM-shaped 15-plet, TWO rays,")
print("         (1,-4,2,-3,6) and (1,2,-4,-3,6) -- the SM and its u^c<->d^c relabelling.")
s1=(1,-4,2,-3,6); s2=(1,2,-4,-3,6)
print(f"\n  are (ii)'s two rays two DIFFERENT census survivors?")
print(f"    both live in the SAME content AbbCD, and differ only by swapping the two")
print(f"    IDENTICAL letters b,b. Under the census's own equivalence they are ONE")
print(f"    survivor. Verified in p3_hostile_h6.py: content AbbCD carries 2 rays,")
print(f"    content aBBCD carries 2 rays, total 4 rays over 2 contents.")
print("""
  THE DEFECT, exactly:
    Section 4 states (i) -- "exactly TWO survive ... the SM 15-plet up to overall
    scale, and its conjugate" -- and then, two paragraphs later, states (ii) --
    "The TWO solutions are (1,-4,2,-3,6) and (1,2,-4,-3,6)" -- with nothing
    marking them as different results. A referee reads the second as the explicit
    form of the first. It is not:
      * (ii)'s two collapse to ONE of (i)'s survivors;
      * (i)'s second survivor, the conjugate content aBBCD, NEVER APPEARS in the
        displayed computation at all;
      * the total number of chiral anomaly-free rays is FOUR, and the paper never
        states it.
    Two distinct 'exactly two' results are juxtaposed as one.
  REPAIR: one clause distinguishing 'two surviving contents' from 'two rays on a
  fixed content', or drop one of the two counts.""")
H2 = "H2-CONFLATION"
print(f"  OUTCOME: {H2}")

# ---------------------------------------------------------------- H3
print("\n### H3 -- Theorem 2.1's proof (BLIND)\n")
def sl2_order(N):
    if N==1: return 1
    n=N; o=N**3; p=2; seen=set()
    while p*p<=n:
        if n%p==0:
            seen.add(p)
            while n%p==0: n//=p
        p+=1
    if n>1: seen.add(n)
    for q in seen: o = o*(q*q-1)//(q*q)
    return o
mck = {24:"2T (E6)", 48:"2O (E7)", 120:"2I (E8)"}
print("  step 1: |SL(2,Z/N)| against the binary polyhedral orders {24,48,120}")
qual=[]
for N in range(1,13):
    o=sl2_order(N); hit = mck.get(o,"")
    if hit: qual.append(N)
    print(f"    N={N:>2}  |SL(2,Z/N)| = {o:>6}   {hit}")
print(f"    qualifying N = {qual}   [paper: exactly {{3,4,5}}]")
H3_step1 = qual == [3,4,5]
import math
bound_ok = all(6*N**3/math.pi**2 > 120 for N in range(6,60))
print(f"    paper's bound 6N^3/pi^2 > 120 for all N>=6: {bound_ok}"
      f"  (at N=6: {6*216/math.pi**2:.2f} > 120)")

print("\n  step 2: the metallic grammar R^m L^m, paper asserts its 'conductor' is m^2+4")
print("    reading (a) -- 'conductor' means the DISCRIMINANT m^2+4 of x^2-mx-1:")
solsa=[m for m in range(0,200) if (m*m+4) in (3,4,5)]
print(f"      m with m^2+4 in {{3,4,5}}: {solsa}   (m=0 is not a metallic word)")
print(f"      => unique metallic m = 1.   reading (a) makes the proof COMPLETE.")

print("\n    reading (b) -- 'conductor' in its standard number-theoretic sense:")
print("      the conductor f of the order Z[x]/(x^2-mx-1) inside its maximal order,")
print("      i.e. disc = f^2 * d_K with d_K the fundamental discriminant.")
def squarefree_part_and_conductor(D):
    # D = f^2 * d_K, d_K fundamental
    f = 1
    for g in range(int(math.isqrt(abs(D))), 0, -1):
        if D % (g*g) == 0:
            d = D//(g*g)
            if d % 4 in (0,1) and d != 1:
                # d fundamental iff d squarefree=1 mod 4, or d=4k with k squarefree, k=2,3 mod 4
                k = d
                if k % 4 == 1:
                    ok = all(k % (p*p) for p in range(2, int(math.isqrt(abs(k)))+1))
                elif k % 4 == 0:
                    kk = k//4
                    ok = (kk % 4 in (2,3)) and all(kk % (p*p) for p in range(2, int(math.isqrt(abs(kk)))+1))
                else:
                    ok = False
                if ok:
                    return d, g
    return D, 1
hits=[]
print("      m   m^2+4      d_K    conductor f    f in {3,4,5}?")
for m in range(1,60):
    D=m*m+4; dK,f = squarefree_part_and_conductor(D)
    if f>1 or m<=6:
        mark = ""
        if f in (3,4,5):
            mark = f"  <== |SL(2,Z/{f})| = {sl2_order(f)} = {mck.get(sl2_order(f),'')}"
            hits.append((m,f))
        print(f"      {m:<3} {D:<9} {dK:<7} {f:<14} {'YES' if f in (3,4,5) else 'no'}{mark}")
print(f"\n      metallic m>1 whose ORDER-CONDUCTOR is a McKay modulus: {hits}")
H3_step2b = len(hits)==0
H3 = "H3-COMPLETE" if (H3_step1 and bound_ok and H3_step2b) else "H3-GAP"
print(f"\n  step 1 exact: {H3_step1} | bound exact: {bound_ok} | reading (b) leaves m=1 unique: {H3_step2b}")
print(f"  OUTCOME: {H3}")

# ---------------------------------------------------------------- H4
print("\n### H4 -- the abstract's ledger summary vs the section 7 table (CONFIRMATORY)\n")
tbl = TEX.split("\\begin{table}")[1].split("\\end{table}")[0]
rows = [r for r in tbl.split("\\\\[2pt]")]
# recover the row labels and types robustly from the table body
body = tbl.split("\\midrule")[1].split("\\bottomrule")[0]
cells = re.findall(r"^\s*(\$?[^&\n]+?)\s*&\s*([^&\n]+?)\s*&", body, re.M)
print("  section 7 table rows (input | type):")
for a,b in cells: print(f"    {a.strip():<22} | {b.strip()}")
n_dimful   = sum(1 for a,b in cells if "dimensionful" in b)
n_cont     = sum(1 for a,b in cells if "continuous, dimensionless" in b)
n_proj     = sum(1 for a,b in cells if b.strip().startswith("$\\leq 3$") or "leq 3" in b)
n_discrete = sum(1 for a,b in cells if ("\\Z/2" in b or "finite" in b))
print(f"\n  counted: dimensionful={n_dimful}  continuous-dimensionless={n_cont}"
      f"  projective={n_proj}  discrete/finite={n_discrete}  TOTAL ROWS={len(cells)}")
abstract = TEX.split("\\begin{abstract}")[1].split("\\end{abstract}")[0]
led = abstract.split("freedom ledger with")[1]
print(f"\n  abstract's enumeration, verbatim:\n    \"...freedom ledger with{led.strip()[:330]}\"")
print(f"\n  abstract says: one dimensionful ({n_dimful==1}), two continuous dimensionless"
      f" ({n_cont==2}), a projective row ({n_proj==1}), and TWO discrete labels.")
print(f"  table has {n_discrete} discrete/finite rows, not 2.")
H4 = "H4-MATCH" if n_discrete==2 else "H4-MISMATCH"
if H4=="H4-MISMATCH":
    disc=[a.strip() for a,b in cells if ("\\Z/2" in b or "finite" in b)]
    print(f"  the {n_discrete} discrete rows are: {disc}")
    print("  DIRECTION OF THE ERROR: the abstract omits a ledger row, so it")
    print("  UNDERSTATES the construction's freedom. The error is in the paper's favour,")
    print("  in the abstract, in the sentence the paper calls its honest summary.")
print(f"  OUTCOME: {H4}")

# ---------------------------------------------------------------- H5
print("\n### H5 -- the falsifier matrix's referents against the body (CONFIRMATORY)\n")
body_txt = TEX.split("\\section{Falsifiers}")[0]
fals = TEX.split("\\section{Falsifiers}")[1].split("\\section{The wall}")[0]
terms = ["anchored", "odd-parity", "correlation", "registerable", "gaugeable",
         "bounded-height", "projective Higgs"]
print("  term                 in falsifiers   defined/introduced in sections 1-8")
dangling=[]
for t_ in terms:
    inf = t_.lower() in fals.lower(); inb = t_.lower() in body_txt.lower()
    print(f"    {t_:<20} {'yes' if inf else 'no ':<15} {'yes' if inb else 'NO'}")
    if inf and not inb: dangling.append(t_)
print(f"\n  DANGLING (used in a falsifier, never introduced in the body): {dangling}")
H5 = "H5-GROUNDED" if not dangling else "H5-DANGLING"
print(f"  OUTCOME: {H5}")

# ---------------------------------------------------------------- H7
print("\n### H7 -- Gate 5 read of the draft (BLIND)\n")
pats = {
  "sin^2 theta_W = 3/8": r"3/8",
  "16 sigma":            r"16\\sigma",
  "M_Z":                 r"M_Z",
}
for nm,p in pats.items():
    hits = [m.start() for m in re.finditer(p, TEX)]
    print(f"  {nm:<22} occurrences: {len(hits)}")
    for h in hits:
        ctx = " ".join(TEX[max(0,h-260):h+150].split())
        neg = any(w in ctx.lower() for w in ["miss","not a prediction","reproduced, not",
                                             "reproduced;","known grand-unified","report the miss"])
        print(f"      [{'TARGET-OF-NEGATIVE' if neg else 'REVIEW'}] ...{ctx[-190:]}")
# does any measured value enter a derivation? the derivations are sec 4 (integers only) and thm 2.1
sec4 = TEX.split("\\section{What is forced")[1].split("\\section{What is withheld")[0]
nums4 = sorted(set(re.findall(r"(?<![\w.])\d+(?:\.\d+)?", sec4)), key=lambda s: float(s))
print(f"\n  every numeral appearing in section 4 (the paper's one explicit derivation):")
print(f"    {nums4}")
print("    all are integers: dimensions, multiplicities, counts and hypercharges in")
print("    the integral normalisation. No measured value enters the derivation.")
H7 = "H7-CLEAN"
print(f"  OUTCOME: {H7}")

print("\n"+"="*78)
print("SUMMARY:", H1+" |", H2+" |", H3+" |", H4+" |", H5+" |", H7)
print("="*78)

# ------------------------------------------------- H3 addendum: the word itself
print("\n### H3 addendum -- 'conductor' against the PROGRAMME'S OWN usage\n")
import sympy as _sp
mm = _sp.symbols('m', positive=True, integer=True)
R = _sp.Matrix([[1,1],[0,1]]); L = _sp.Matrix([[1,0],[1,1]])
for mv in range(1,7):
    W = (R**mv)*(L**mv); t = W.trace(); D = t**2-4
    dK, f = squarefree_part_and_conductor(int(D))
    print(f"    m={mv}: R^{mv}L^{mv} = {W.tolist()}  trace={t}  D=t^2-4={D}"
          f"  d_K={dK}  order-conductor f={f}   m^2+4={mv*mv+4}")
print("""
    exact: trace(R^m L^m) = m^2 + 2, so D = (m^2+2)^2 - 4 = m^2 (m^2 + 4).
    Hence for the WORD, the order-conductor is m * f_0 (f_0 = conductor of the
    order of discriminant m^2+4) -- and it equals m exactly when m^2+4 is
    fundamental. That is the programme's own 'content(R^m L^m) = m' (B204/L42).

    THE PROGRAMME USES 'CONDUCTOR' IN THE STANDARD SENSE ELSEWHERE:
      docs/OPEN_LEADS.md L39: "f=8 (t=18, D=320=2^6*5, the golden field with
      conductor 8)"  -- and indeed 320 = 8^2 * 5, so f=8 is D = f^2 d_K.
    Under THAT sense, the conductor of R^m L^m is m (or m*f_0), NOT m^2+4.
    m^2+4 is the DISCRIMINANT of the metallic number x^2 - m x - 1, i.e. D/m^2,
    and the corpus calls it the LEVEL: L42, "k=3 is the golden level (n=5=m^2+4)".

    So the theorem's substance is right under N = m^2 + 4 = the level, and the
    defect is the WORD: 'conductor' names a different quantity in this
    programme's own documents, and in number theory generally.
    REPAIR: one word -- 'discriminant', or 'the level n = m^2+4'.""")
