# Exact group-theory verification for CELL L2 (inert-5 Bianchi rederivation).
# All arithmetic exact (integers / finite fields). No floats used for verdicts.
from sympy import legendre_symbol, isprime, factorint

print("=== (a) 5 inert in Q(sqrt-3), residue field ===")
# O_{-3} = Z[w], w=(1+sqrt-3)/2, min poly x^2 - x + 1 (Eisenstein).
# 5 inert  <=>  x^2 - x + 1 irreducible mod 5  <=> disc(-3) non-residue mod 5.
ls = legendre_symbol(-3, 5)   # (-3/5)
print("  Legendre(-3|5) =", ls, "=> 5", "INERT" if ls==-1 else "SPLIT/RAMIFIED")
# residue field O/(5) = F_5[x]/(x^2-x+1), degree 2 => F_25
roots_mod5 = [x for x in range(5) if (x*x - x + 1) % 5 == 0]
print("  x^2-x+1 roots mod 5:", roots_mod5, "(none => irreducible => O/(5)=F_25)")
print("  3 ramifies: disc(Q(sqrt-3)) = -3, 3 | disc ->", (-3)%3==0)

print("\n=== golden ratio / sqrt5 in characteristic 5 (the CRUX) ===")
# sqrt(5) in F_25: char is 5 so 5 == 0.  sqrt5 = 0 (degenerate).
print("  5 mod 5 =", 5%5, "=> sqrt5 = 0 in char 5 (DEGENERATE, not a genuine sqrt5)")
# golden poly x^2 - x - 1 mod 5: disc = 1+4 = 5 = 0 -> double root
gdisc = (1 + 4) % 5
groots = [x for x in range(5) if (x*x - x - 1) % 5 == 0]
print("  golden disc 1+4=5 mod5 =", gdisc, "; x^2-x-1 roots mod5:", groots,
      "(double root => phi=phibar collapse; 5 RAMIFIES in Q(sqrt5))")

print("\n=== (b) |PSL2(F25)| and A5 | order ===")
q = 25
sl2 = q*(q*q-1)                      # |SL2(F_q)|
psl2 = sl2 // 2                      # gcd(2,q-1)=2 for q odd
print("  |SL2(F25)| =", sl2, "  |PSL2(F25)| =", psl2, " (=25*24*26/2 =", 25*24*26//2, ")")
A5 = 60
print("  |A5| =", A5, " divides |PSL2(25)|? ", psl2 % A5 == 0, " quotient", psl2//A5)
print("  |2I| = 120 divides |SL2(25)|? ", sl2 % 120 == 0, " quotient", sl2//120)

print("\n=== explicit A5 = PSL2(5) < PSL2(25) via subfield F5<F25 ===")
# Build <S,T> in SL2(F5), count classes mod +-I -> must be 60 = A5.
def matmul(a,b,p):
    return ((a[0]*b[0]+a[1]*b[2])%p,(a[0]*b[1]+a[1]*b[3])%p,
            (a[2]*b[0]+a[3]*b[2])%p,(a[2]*b[1]+a[3]*b[3])%p)
def closure(gens,p):
    I=(1,0,0,1); seen={I}; frontier=[I]
    while frontier:
        nf=[]
        for g in frontier:
            for h in gens:
                x=matmul(g,h,p)
                if x not in seen: seen.add(x); nf.append(x)
        frontier=nf
    return seen
p=5
S=(0,4,1,0); T=(1,1,0,1)             # over F5, -1==4
G=closure([S,T],p)
print("  |<S,T>| in SL2(F5) =", len(G))
# project to PSL2: identify M ~ -M
negI=(4,0,0,4)
def neg(m,p): return tuple((-x)%p for x in m)
classes=set(); 
for m in G:
    classes.add(frozenset([m,neg(m,p)]))
print("  |PSL2(F5)| = |<S,T>|/<+-I> =", len(classes), " == A5 (60)?", len(classes)==60)
print("  F5 subset F25 => this A5 sits inside PSL2(F25) as a subfield subgroup.")

print("\n=== (c) congruence quotient of PSL2(O_-3) at (5) ===")
print("  O_-3/(5) = F_25 (5 inert) => congruence quotient = PSL2(F_25), |.|=", psl2)
print("  A5 is a SUBGROUP of that quotient, NOT the quotient itself (7800 != 60).")

print("\n=== BASE RATE: is p=5 special for A5 < PSL2(p^2)? ===")
# A5 < PSL2(q) iff q ≡ 0,+-1 (mod 5)  (Dickson). For q=p^2:
for pr in [2,3,5,7,11,13,17,19,23,29,31]:
    q2=pr*pr
    cond = (q2%5 in (0,1,4))
    mech = "defining-char subfield PSL2(5)" if pr==5 else "sqrt5 exists in F_{p^2}"
    print(f"  p={pr:2d}: p^2 mod5={q2%5} -> A5<PSL2(p^2)? {cond}   [{mech}]")
print("  => A5 embeds in PSL2(p^2) for EVERY prime p (p!=5: p^2==+-1 mod5 always).")
