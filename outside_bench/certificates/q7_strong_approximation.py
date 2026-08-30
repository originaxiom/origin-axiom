#!/usr/bin/env python3
"""Q7 / ROUTE A -- the arithmetic of K, the stabilizer's dimension, and the strong-approximation
hypotheses. Seal: seals/Q7_STRONG_APPROXIMATION_PREREG.md.

BINDING FENCE from the seal: this cell may NOT conclude that Route A crosses. A dimension count is
evidence, not an identification. Gate 5: no measured value.
"""
import sympy as sp, math

print("="*78); print("Q7 -- ROUTE A: THE ARITHMETIC, THE DIMENSION, THE HYPOTHESES"); print("="*78)

# ---------------- R-1: the arithmetic of K ----------------
x = sp.symbols('x')
f = x**3 - 12*x - 5
print("\nR-1  K = Q[x]/(x^3 - 12x - 5)   [B990's classifying cubic etale algebra]")
print(f"     irreducible over Q: {sp.Poly(f, x).is_irreducible}")
disc = sp.discriminant(f, x)
print(f"     discriminant = {disc}   factored = {sp.factorint(int(disc))}   [B1093: 6237 = 3^4*7*11]")
roots = sp.Poly(f, x).all_roots()
nreal = sum(1 for r in roots if r.is_real)
print(f"     roots: {nreal} real, {(3-nreal)//2} complex-conjugate pair(s)")
for r in roots:
    print(f"        {sp.nsimplify(sp.N(r, 12))}" if not r.is_real else f"        {sp.N(r, 12)} (real)")
sig = (nreal, (3-nreal)//2)
print(f"     signature (r1, r2) = {sig}  =>  K (x) R = " +
      ("R x R x R  (totally real)" if sig == (3,0) else "R x C"))
# Galois group via discriminant square-ness
is_sq = sp.sqrt(disc).is_rational
print(f"     disc a rational square: {is_sq}  =>  Galois group = {'C3' if is_sq else 'S3'}")

# ---------------- R-2: the stabilizer's dimension ----------------
print("\nR-2  DIMENSION COUNT along the chain (exact integers, standard Lie dimensions)")
dimE6, dim27, dimF4, dim26, dimD4 = 78, 27, 52, 26, 28
print(f"     dim E6 = {dimE6}, dim 27 = {dim27}, dim F4 = {dimF4}, dim 26 = {dim26}")
print(f"     (a) stabilizer in E6 of a rank-3 (nonzero-norm) element of the 27:")
print(f"         E6 acts with a 1-dim invariant (the cubic norm), so the generic orbit has")
print(f"         dim {dim27} - 1 = {dim27-1};  stabilizer dim = {dimE6} - {dim27-1} = {dimE6-(dim27-1)} = dim F4 = {dimF4}"
      f"   MATCH: {dimE6-(dim27-1) == dimF4}")
print(f"     (b) that F4 then acts on the 26 (trace-zero Albert algebra), with 2 invariants")
print(f"         (a quadratic and a cubic form), so the generic orbit has dim {dim26} - 2 = {dim26-2};")
print(f"         stabilizer dim = {dimF4} - {dim26-2} = {dimF4-(dim26-2)} = dim Spin(8) = {dimD4}"
      f"   MATCH: {dimF4-(dim26-2) == dimD4}")
print(f"\n     => the generic stabilizer of a PAIR (x in 27, y in 27bar) has dimension {dimF4-(dim26-2)},")
print(f"        which is dim D4. **EVIDENCE, NOT AN IDENTIFICATION** (seal clause 2).")

# ---------------- R-3: the hypotheses ----------------
print("\nR-3  STRONG APPROXIMATION (Kneser-Platonov) -- hypotheses, one line each")
print("""
     THE STATEMENT: if H/Q is semisimple, SIMPLY CONNECTED, Q-SIMPLE and H(R) is
     NON-COMPACT, then H(Q) is dense in H(A_f) and the CLASS SET is TRIVIAL --
     i.e. exactly ONE integral orbit inside the rational one.
""")
H = [
 ("simply connected",
  "HOLDS *if* the stabilizer is a form of Spin(8): Spin(8) is the simply connected group of type D4,"
  "\n        and forms of a simply connected group are simply connected.",
  "HOLDS-CONDITIONALLY"),
 ("Q-simple",
  "HOLDS *if* the stabilizer is an OUTER (triality) form twisted by the cubic field K: with K a"
  "\n        FIELD (R-1: irreducible) the twist does not split the group over Q, so it stays Q-simple.",
  "HOLDS-CONDITIONALLY"),
 ("H(R) non-compact",
  f"HOLDS. B904 constructs L(O_split, C'_split) EXPLICITLY OVER Q with ZORN octonions -- the SPLIT"
  f"\n        octonion algebra, not a division algebra. Split octonions => split Albert algebra => SPLIT F4"
  f"\n        and SPLIT Spin(8), whose real points are NON-COMPACT. And K (x) R = {'R^3 (totally real)' if sig==(3,0) else 'R x C'},"
  "\n        the SPLIT etale algebra at R, so the trialitarian twist is inner there and cannot compactify it.",
  "HOLDS"),
 ("the stabilizer IS a form of Spin(8)",
  "UNVERIFIED -- but now with THREE CONVERGING pieces of evidence, none of which is a proof:"
  "\n        (i) the dimension count above gives exactly 28 = dim D4;"
  "\n        (ii) B904 ALREADY CONSTRUCTED tri(O), dimension 28, AS AN EXACT NULLSPACE OVER Q -- the"
  "\n             triality algebra itself is banked, not hypothesised;"
  "\n        (iii) R-1 finds K TOTALLY REAL with Galois group S3, which is EXACTLY the trialitarian"
  "\n             twisting datum (an S3-torsor is a full triality twist of D4)."
  "\n        Convergence is evidence. The stabilizer scheme of the object's OWN pair is still uncomputed.",
  "UNVERIFIED-HERE"),
 ("orbit count = class set of the stabilizer",
  "The Borel-Serre / Bhargava-style bijection requires G(Z) class number one and a coherent integral"
  "\n        model of the stabilizer. NOT CHECKED HERE.",
  "UNVERIFIED-HERE"),
]
for name, why, verdict in H:
    print(f"     [{verdict:<20}] {name}\n        {why}")

nver = sum(1 for _,_,v in H if v == "UNVERIFIED-HERE")
print(f"\n     hypotheses HOLDING conditionally: {sum(1 for _,_,v in H if v.startswith('HOLDS'))}"
      f" | UNVERIFIED-HERE: {nver}")
verdict = "R-ROUTE-NAMED"
print(f"\n{'='*78}")
print(f"VERDICT: {verdict}")
print(f"""
A standard, checkable route exists that B1099's literature floor did not reach: the
counter B1093 asked for -- "WHICH Kato-Yukie/Bhargava quantity counts integral orbits" --
may simply be THE CLASS SET OF THE STABILIZER, and strong approximation may make it
trivial. {nver} of {len(H)} hypotheses are UNVERIFIED HERE and are named exactly.

PER THE SEAL'S BINDING FENCE: this cell does NOT conclude that Route A crosses.
B990's declared UNFAVOURABLE prior stands unrepudiated. The dimension match is
EVIDENCE, NOT AN IDENTIFICATION.
""")
print("="*78)
