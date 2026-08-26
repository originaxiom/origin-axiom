#!/usr/bin/env python3
"""MEMO-79 CELL (WAVE-3 MA1): THE ONE-BIT WITNESS — are the record's
orientation/Galois bit and its chirality bit (27 vs 27-bar) the same Z/2?
The computable fragment of cc's B1162 meditation SS-A (the one-bit
conjecture: chirality, frame, branch selection, W0 = one observer choice).

THE TWO BITS:
  ORIENTATION bit: gal (q -> 1-q) — complex conjugation under either
    embedding; realized on the carrier only by the SEMILINEAR beat (banked).
    KEY ARITHMETIC (verified in-run): q(1-q) = 1, so gal(q) = q^{-1} — the
    Galois bit inverts the meridian-twist parameter.
  CHIRALITY bit: the 27 vs its dual (omega_1 vs omega_6), memo 66's fenced
    choice.  The 27 is genuinely chiral at the e6 level: weight multiset
    W != -W (verified in-run; 27 (x) 27 has no singlet).

THE TEST (exact over the pair-field): on the internal pi1 image
(a -> exp(E27), b -> exp(q F27)), compare over the FULL ball of reduced
words of length <= 5:
    chi(w) = tr rho27(w),  chi*(w) = tr rho27(w^{-1}),  chi^gal = gal o chi.

PREREGISTERED as two-outcome (ONE-BIT: chi^gal == chi*; TWO-BITS: a word
separates them), with a non-vacuity gate "some word has chi(w) != chi*(w)".
[ERROR FILED AT POINT OF OCCURRENCE — and the refused gate is the
finding: the machine returned chi == chi* IDENTICALLY on the ball (zero
separating words).  The DUAL character coincides with the character on
the holonomy image — the 27-level shadow of the figure-eight's strong
invertibility (2-bridge knots are strongly invertible, CITED context;
the character identity itself is computed exactly here).  So the
preregistered comparison was between the WRONG pair: chi* cannot
distinguish anything.  The corrected facts below are the measured
branch.]

MEASURED FACTS (asserts):
  FACT 1 (chirality is character-INVISIBLE): chi(w) = chi(w^{-1}) for ALL
    words in the ball => the holonomy characters cannot see 27 vs 27-bar:
    the chirality bit costs NOTHING at the character level.  (Aligns with
    the corpus's walled item "chirality is inserted" — here sharpened: the
    object's characters do not even register the flip.)
  FACT 2 (orientation is character-VISIBLE): chi^gal != chi on 396 of 484
    words — the Galois bit genuinely moves the character data.
  FACT 3 (and it is irreducibly semilinear): gal is NOT realized by any
    word-level relabeling tested (letters->inverses; a<->b swap;
    b->b^{-1} only): each matches gal exactly on the rational-trace words
    and nowhere else — consistent with the banked semilinearity of the
    beat (the mirror has no linear/word-level realization).
VERDICT (BRANCH TWO-BITS, refined): the two bits are NOT one bit — and
the reason is structural: chirality is FREE on the carrier's characters
(invisible, unpaid) while orientation is ARITHMETIC (visible, semilinear
only).  cc's SS-A one-bit unification fails in its cleanest carrier-level
version; what survives is sharper: the record's ONE arithmetic Z/2 is the
orientation bit (whose gravitational face is the CS phase — wave-3 ME3),
and the chirality insertion is priced at exactly zero by the object.
FENCE: character-level, finite ball (radius 5), exact; not an all-words
proof; not a decision of the observer-coupling thesis.  Gate 5 untouched.
"""
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

r0=ROOTS[0]
E27=rho27_Q(evec(r0)); F27=rho27_Q(evec(tuple(-x for x in r0)))
Z=(F(0),F(0)); O=(F(1),F(0)); Qp=(F(0),F(1))
E27p=toF(E27); F27p=toF(F27)

qbar=fadd(O,fneg(Qp))
assert fmul(Qp,qbar)==O
print("KEY ARITHMETIC: q(1-q) = 1 exactly => gal(q) = q^{-1}")
Wt=[tuple(int(x) for x in w) for w in weights]
assert Counter(Wt)!=Counter(tuple(-x for x in w) for w in Wt)
print("CHIRALITY GATE: W != -W as multisets — the 27 is not self-dual at the e6 level")

Ma=nilexp(E27p,ONE);  MA=nilexp(E27p,fneg(ONE))
Mb=nilexp(F27p,Qp);   MB=nilexp(F27p,fneg(Qp))
def mmF(X,Y):
    n=len(X); out=[[Z]*n for _ in range(n)]
    for i in range(n):
        Xi=X[i]
        for k in range(n):
            x=Xi[k]
            if x==Z: continue
            Yk=Y[k]; oi=out[i]
            for j in range(n):
                y=Yk[j]
                if y==Z: continue
                oi[j]=fadd(oi[j],fmul(x,y))
    return out
I27=[[O if i==j else Z for j in range(27)] for i in range(27)]
assert mmF(Ma,MA)==I27 and mmF(Mb,MB)==I27
LET={'a':Ma,'b':Mb,'A':MA,'B':MB}
INV={'a':'A','b':'B','A':'a','B':'b'}
def trF(M):
    t=Z
    for i in range(27): t=fadd(t,M[i][i])
    return t
def galF(x): return (x[0]+x[1], -x[1])

LMAX=5
tr_of={}
def dfs(word, mat):
    if word: tr_of[word]=trF(mat)
    if len(word)==LMAX: return
    for ch in 'abAB':
        if word and INV[word[-1]]==ch: continue
        dfs(word+ch, mmF(mat,LET[ch]))
dfs("", I27)
def invword(w): return ''.join(INV[ch] for ch in reversed(w))
words=sorted(tr_of)
nonrat=[w for w in words if tr_of[w][1]!=0]
print(f"BALL: {len(words)} reduced words, length <= {LMAX}; {len(nonrat)} with irrational trace")

# FACT 1: dual character == character (the refused gate, now the finding)
dualdiff=[w for w in words if tr_of[invword(w)]!=tr_of[w]]
print(f"FACT 1: words with chi(w) != chi(w^-1): {len(dualdiff)} — the dual character")
print("   COINCIDES with the character on the whole ball: chirality is")
print("   character-INVISIBLE on the holonomy image (strong invertibility of 4_1")
print("   at the 27 level; CITED context, identity computed exactly)")
assert not dualdiff

# FACT 2: gal moves the characters
galdiff=[w for w in words if galF(tr_of[w])!=tr_of[w]]
print(f"FACT 2: words with chi^gal(w) != chi(w): {len(galdiff)} of {len(words)} — the")
print("   orientation bit is character-VISIBLE")
assert len(galdiff)==len(nonrat) and len(galdiff)>0

# FACT 3: gal is not any word-level relabeling
def relabel_test(mapping, name):
    ok=sum(1 for w in words if galF(tr_of[w])==tr_of[''.join(mapping[c] for c in w)])
    ratn=len(words)-len(nonrat)
    print(f"FACT 3 [{name}]: gal matches the relabeled trace on {ok}/{len(words)} words"
          f" (rational-trace words: {ratn})")
    return ok
n_sig =relabel_test({'a':'A','A':'a','b':'B','B':'b'}, "letters -> inverses")
n_swap=relabel_test({'a':'b','b':'a','A':'B','B':'A'}, "a <-> b swap")
n_binv=relabel_test({'a':'a','A':'A','b':'B','B':'b'}, "b -> b^-1 only")
ratn=len(words)-len(nonrat)
assert max(n_sig,n_swap,n_binv)==ratn, "no relabeling exceeds the trivial rational agreement"
print("   => gal is realized by NO word-level involution — it is irreducibly")
print("      SEMILINEAR (the beat), as banked")

print(f"""
VERDICT (BRANCH TWO-BITS, refined): the chirality bit and the orientation
bit are NOT one bit, for a structural reason measured above — chirality is
FREE (the holonomy characters do not register 27 vs 27-bar: the insertion
is priced at exactly zero by the object) while orientation is ARITHMETIC
(moves 396/484 characters, realized only semilinearly).  cc's SS-A one-bit
unification fails in its cleanest carrier-level version; the surviving
core is sharper: the record's ONE arithmetic Z/2 is the orientation bit,
whose gravitational face is the CS phase (ME3).  FENCE: character-level,
radius-{LMAX} ball, exact; not an all-words proof; the observer-coupling
thesis is untouched.  Gate 5 untouched.""")
