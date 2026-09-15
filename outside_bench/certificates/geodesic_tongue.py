#!/usr/bin/env python3
"""MEMO-81 CELL (WAVE-3 ME1): THE MOTHER TONGUE SPOKEN EXACTLY — the
beginning of m004's complex-length spectrum as exact algebraic data, and
the mirror's action on it.  (cc's B1162 meditation SS-E: the object's
native language is gravitational/spectral; this cell computes in it.)

The object's intrinsic spectral data is the complex-length spectrum: for a
closed geodesic gamma with loxodromic holonomy g, the complex length is
L(gamma) = 2 arccosh(tr(g)/2) = length + i * torsion.  In 3d gravity terms
(SL(2,C) Chern-Simons; the holonomy IS the gravitational field): length =
the geodesic's metric length, torsion = the rotation angle of parallel
transport around it.

CONSTRUCTION (exact): the banked Riley holonomy a = [[1,1],[0,1]],
b = [[1,0],[-w,1]] with w^2 = w - 1 (w = (1+i sqrt3)/2; the pair-field
(x,y) = x + y w over Q).  Enumerate ALL conjugacy classes of pi1 words up
to length LMAX (reduced cyclic words modulo rotation, inversion, and the
generator-order convention), compute each trace EXACTLY in Z[w], classify
parabolic (real trace in [-2,2] with the peripheral cases) vs loxodromic,
and list the spectrum's beginning.

PREREGISTERED (two-outcome where marked; asserts):
  FACT 1 (integrality): every word trace lies in Z[w] (the Eisenstein
    integers) — traces are algebraic INTEGERS of the trace field Q(sqrt-3)
    (verified on the whole ball; the banked trace field, memos 30/49).
  FACT 2 (the mirror on the spectrum): for every class in the INNER ball
    (word length <= 4) the conjugate trace is realized by some class
    (searched to word length 9) => the spectrum is mirror-symmetric where
    checked: LENGTHS mirror-INVARIANT, TORSION ANGLES mirror-NEGATED.  In
    the gravitational vocabulary: THE INVISIBLE BIT IS THE TORSION SENSE
    OF EVERY GEODESIC; the length spectrum is the mirror-even data.
    [PREREGISTRATION CORRECTED IN-RUN, error filed: the first draft
    asserted multiset closure AT FIXED WORD RADIUS; the machine refused —
    the mirror DISTORTS WORD LENGTH (exhibit: AbAb, trace 1+5w, length-4
    word, mirrors to aabaaBAB, trace 6-5w, length-8 word).  The geometric
    closure is the right statement and is what is asserted; the word-
    length distortion is itself a finding, consistent with MA1: the
    mirror has no word-level (letter-relabeling) realization — its
    geometric realization stretches combinatorial length up to 2x on the
    exhibit.]
  FACT 3 (the bit is nontrivial and near-total): count classes with
    nonreal trace (torsion != 0, the generic case) vs real-trace
    loxodromics (mirror-fixed geodesics, torsion 0 or pi); measured.
  FACT 4 (the spectrum's beginning): the N shortest distinct complex
    lengths with their exact traces (algebraic data) and numeric
    (length, torsion) pairs; the systole's trace reported exactly.
FENCES: lengths are the OBJECT'S own geometry (no SM value — Gate 5
untouched); numerics are display only, every claim is exact trace
arithmetic; conjugacy classes are represented by cyclic reduction (words
of the free-ish presentation; classes beyond LMAX not claimed).
"""
from fractions import Fraction as F
from collections import Counter, defaultdict
import cmath, math

# exact pair-field Z[w], w^2 = w-1
def pmul(A,B):
    (a,b),(c,d)=A,B
    return (a*c-b*d, a*d+b*c+b*d)
def padd(A,B): return (A[0]+B[0],A[1]+B[1])
def pneg(A): return (-A[0],-A[1])
ONEp=(F(1),F(0)); ZEROp=(F(0),F(0)); Wp=(F(0),F(1))
def conjp(A): return (A[0]+A[1], -A[1])     # gal: w -> 1-w = conj(w)
def mm2(X,Y):
    return [[padd(pmul(X[0][0],Y[0][0]),pmul(X[0][1],Y[1][0])), padd(pmul(X[0][0],Y[0][1]),pmul(X[0][1],Y[1][1]))],
            [padd(pmul(X[1][0],Y[0][0]),pmul(X[1][1],Y[1][0])), padd(pmul(X[1][0],Y[0][1]),pmul(X[1][1],Y[1][1]))]]
Ma=[[ONEp,ONEp],[ZEROp,ONEp]]
MA=[[ONEp,pneg(ONEp)],[ZEROp,ONEp]]
Mb=[[ONEp,ZEROp],[pneg(Wp),ONEp]]
MB=[[ONEp,ZEROp],[Wp,ONEp]]
I2=[[ONEp,ZEROp],[ZEROp,ONEp]]
LET={'a':Ma,'A':MA,'b':Mb,'B':MB}
INV={'a':'A','A':'a','b':'B','B':'b'}
def det2(X):
    return padd(pmul(X[0][0],X[1][1]),pneg(pmul(X[0][1],X[1][0])))
for k,M in LET.items(): assert det2(M)==ONEp

def emb(t):   # numeric embedding w -> (1+i sqrt3)/2
    return float(t[0])+complex(t[1])*complex(0.5, math.sqrt(3)/2)

LMAX=7
# conjugacy classes: cyclically reduced words up to rotation and inversion
def cyc_reduced(w):
    return not (w and INV[w[0]]==w[-1])
def canon(w):
    cands=[]
    for v in (w, ''.join(INV[c] for c in reversed(w))):
        for i in range(len(v)):
            cands.append(v[i:]+v[:i])
    return min(cands)
classes={}
def gen(word):
    if word and cyc_reduced(word):
        cn=canon(word)
        if cn not in classes: classes[cn]=word
    if len(word)==LMAX: return
    for ch in 'abAB':
        if word and INV[word[-1]]==ch: continue
        gen(word+ch)
gen("")
def wtrace(w):
    M=I2
    for ch in w: M=mm2(M,LET[ch])
    return padd(M[0][0],M[1][1])
tr={cn: wtrace(rep) for cn,rep in classes.items()}
print(f"conjugacy classes (cyclic words, len <= {LMAX}, mod rotation+inversion): {len(classes)}")

# FACT 1: integrality
assert all(t[0].denominator==1 and t[1].denominator==1 for t in tr.values())
print("FACT 1: every class trace lies in Z[w] — the Eisenstein integers: traces are")
print("   algebraic integers of the banked trace field Q(sqrt-3)")

# classify
def is_parab_or_ell(t):
    z=emb(t)
    return abs(z.imag)<1e-12 and -2-1e-12<=z.real<=2+1e-12
lox={cn:t for cn,t in tr.items() if not is_parab_or_ell(t)}
peri={cn:t for cn,t in tr.items() if is_parab_or_ell(t)}
print(f"   loxodromic classes: {len(lox)}; parabolic/elliptic-trace classes: {len(peri)}")

# FACT 2: mirror closure — geometric statement, targeted search
trset=set(tr.values())
inner=[cn for cn in classes if len(cn)<=4]
missing=sorted(set(conjp(tr[cn]) for cn in inner if conjp(tr[cn]) not in trset))
print(f"FACT 2: inner ball (len<=4): {len(inner)} classes; conjugate traces not in the")
print(f"   len<=7 ball: {len(missing)} — targeted search to length 9 for those:")
found={}
LMAX2=9
def gen2(word, mat):
    t=padd(mat[0][0],mat[1][1])
    if word and cyc_reduced(word) and t in set(missing):
        found.setdefault(t, word)
    if len(word)==LMAX2: return
    for ch in 'abAB':
        if word and INV[word[-1]]==ch: continue
        gen2(word+ch, mm2(mat,LET[ch]))
if missing:
    gen2("", I2)
for t in missing:
    assert t in found, f"conjugate trace {t} unrealized to length {LMAX2}"
    print(f"   trace {t[0]}+({t[1]})w realized by [{found[t]}] (length {len(found[t])})")
print("   => EVERY inner-ball class has a mirror partner: the spectrum is mirror-")
print("      symmetric (lengths invariant, torsion negated) — verified, with the")
print("      measured finding that the mirror DISTORTS word length (it is not a")
print("      letter map; cf. MA1's no-word-level-realization)")
# exhibit: equal lengths, opposite torsion
if missing:
    t0=[cn for cn in inner if conjp(tr[cn])==missing[0]][0]
    L1=clen_pair=(cmath.acosh(emb(tr[t0])/2)*2, cmath.acosh(emb(missing[0])/2)*2)
    print(f"   exhibit lengths: {L1[0].real:.6f} vs {L1[1].real:.6f} (equal), torsions "
          f"{L1[0].imag:+.6f} vs {L1[1].imag:+.6f} (negated)")
    assert abs(L1[0].real-L1[1].real)<1e-9 and abs(L1[0].imag+L1[1].imag)<1e-9

# FACT 3: the bit is near-total
nonreal=[cn for cn,t in lox.items() if t[1]!=0]
realtr=[cn for cn,t in lox.items() if t[1]==0]
print(f"FACT 3: loxodromic classes with torsion (nonreal trace): {len(nonreal)};")
print(f"   mirror-fixed (real-trace) loxodromics: {len(realtr)} — real traces: "
      f"{sorted(set(emb(tr[cn]).real for cn in realtr))}")
assert nonreal

# FACT 4: the spectrum's beginning
def clen(t):
    z=emb(t)/2
    L=2*cmath.acosh(z)
    if L.real<0: L=-L
    return L
spec=[]
seen=set()
for cn,t in lox.items():
    key=(t if t>=conjp(t) else conjp(t))
    if key in seen: continue
    seen.add(key)
    L=clen(t)
    spec.append((L.real, abs(L.imag), t, cn))
spec.sort()
print("FACT 4: the spectrum's beginning (distinct up to mirror; length, |torsion|, exact trace):")
for L,th,t,cn in spec[:8]:
    x,y=t
    print(f"   len {L:.6f}  torsion {th:.6f}   tr = {x}{'+' if y>=0 else '-'}{abs(y)}w   [{cn}]")
sysL,sysT,syst,syscn=spec[0]
print(f"   SYSTOLE (in this ball): word class [{syscn}], exact trace {syst[0]}+({syst[1]})w,")
print(f"   complex length {sysL:.6f} + {sysT:.6f} i")

print("""
THE MOTHER TONGUE: the object's native spectral data — the complex-length
spectrum — computed exactly in its trace ring Z[w].  The mirror acts as
complex conjugation: the LENGTH spectrum (the gravitational moduli) is
mirror-even, the TORSION spectrum is mirror-odd.  The record's invisible
bit, spoken gravitationally, is the torsion sense of every geodesic —
the geodesic-side shadow of the (Vol, CS) pair (wave-3 ME3).  Gate 5
untouched (all data are the object's own geometry).""")
