#!/usr/bin/env python3
"""F190-2: WHAT Q11 ASKED AN EXPERT, ANSWERED IN PART FROM WHAT THIS BENCH ALREADY HOLDS --
and the answer is that c_eff = 1 is forced by the SHAPE of Zhat, not by our knot.

Q11 (sent to Prof. Dimofte 2026-08-31) says in its own words:

    "I should say plainly that Z-hat invariants and logarithmic or non-semisimple boundary
     algebras are the obvious tools here and that we have simply not read that literature.
     If the honest answer is 'read GPPV', that alone is worth the email."

THE LITERATURE IS NOW ON THIS BENCH.  Gukov-Manolescu section 10.2, "Relation to log-VOAs",
says three things that bear directly on the question:

  (i)  for closed 3-manifolds the UNREDUCED series should be a character of a 2d chiral
       algebra, "non-strongly-finite for hyperbolic Y" -- i.e. logarithmic, exactly as Q11
       guessed;
  (ii) for BRIESKORN SPHERES the algebra is IDENTIFIED: the logarithmic (1,p) singlet VOA
       with p = b1 b2 b3 and central charge c = 13 - 6(p + 1/p), with Zhat^unred_0 a
       character of an explicit atypical module;
  (iii) for HYPERBOLIC manifolds it is NOT.  GM's own words: "It would be interesting to
       identify log-VOAs that correspond to other types of 3-manifolds, such as the
       hyperbolic surgeries on the figure-eight knot."  That is Q11's target, named OPEN
       by the authors.

And Remark 3.8 gives the bridge exactly:   Zhat^unred_0 = Zhat_0 / (q)_inf .

THE COMPUTATION THIS MAKES POSSIBLE, entirely from series this bench already verified.
Zhat_0 of a Brieskorn sphere is a FALSE THETA -- bounded coefficients.  So

    Zhat^unred  =  (false theta) / (q)_inf

and the bench has already measured both halves: a false theta alone gives c_eff = 0
(memo 174, Sigma(2,3,7)), and 1/(q;q)_inf gives c_eff = 1 (tail_52.py control C3).
The prediction is therefore c_eff(Zhat^unred) = 1 FOR EVERY BRIESKORN SPHERE, with p
cancelling out entirely -- even though c = 13 - 6(p + 1/p) runs to -infinity with p.

PREREGISTERED.
  A  c_eff(Zhat^unred) depends on p  ->  some Brieskorn sphere could reach 6, and the
     search for one is worth running.
  B  it does not -- it is 1 for every p  ->  c_eff = 6 is unreachable on this route for a
     structural reason, and the reason is the SHAPE of Zhat, not our knot.

CONTROLS
  C1  the estimator on 1/(q;q)_inf must give 1        (the bench's own C3)
  C2  the estimator on 1/(q;q)_inf^2 must give 2      -- it is not an instrument that
      always says 1 (memo 164)
  C3  the estimator on a bare false theta must give 0 (bounded coefficients)
  C4  two Brieskorn spheres with DIFFERENT p, both from series verified elsewhere on this
      bench: Sigma(2,3,5) (p=30, GM eq (27)-(28), verified in gm_74_habiro_surgery.py) and
      Sigma(2,3,11) (p=66, verified in park_ahat_erratum.py C5 and again as anchor A2).

Gate 5: exact integer series; floats only in the growth fit.  No measured physical value.
"""
import math, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

N = 20000
def flog(v): return math.log(v)
def fit3(a, lo, hi):
    """the bench's own estimator, as in tail_52.py / ceff_scaling_law.py"""
    X, Y = [], []
    for n in range(lo, hi+1):
        v = abs(a[n])
        if n > 1 and v > 0: X.append((math.sqrt(n), math.log(n), 1.0)); Y.append(flog(v))
    mm = 3
    M = [[sum(X[i][p]*X[i][q] for i in range(len(X))) for q in range(mm)] for p in range(mm)]
    V = [sum(X[i][p]*Y[i] for i in range(len(X))) for p in range(mm)]
    for c in range(mm):
        piv = max(range(c, mm), key=lambda rr: abs(M[rr][c]))
        M[c], M[piv] = M[piv], M[c]; V[c], V[piv] = V[piv], V[c]
        for rr in range(mm):
            if rr == c: continue
            f = M[rr][c]/M[c][c]
            for cc in range(mm): M[rr][cc] -= f*M[c][cc]
            V[rr] -= f*V[c]
    s = [V[i]/M[i][i] for i in range(mm)]
    return 3*s[0]*s[0]/(2*math.pi**2)

def inv_qq(N, power=1):
    a = [0]*(N+1); a[0] = 1
    for _ in range(power):
        b = [0]*(N+1); b[0] = 1
        for n in range(1, N+1):
            for i in range(n, N+1): b[i] += b[i-n]
        c = [0]*(N+1)
        for i, x in enumerate(a):
            if not x: continue
            for j in range(0, N+1-i): c[i+j] += x*b[j]
        a = c
    return a

def false_theta_235(N):
    """GM eq (27)-(28): A(q) = sum chi_+(n) q^{(n^2-1)/120}; Zhat_0 ~ 2 - A(q)"""
    d = [0]*(N+1); d[0] = 2; n = 1
    while (n*n-1)//120 <= N:
        r = n % 60
        ch = 1 if r in (1, 11, 19, 29) else (-1 if r in (31, 41, 49, 59) else 0)
        if ch and (n*n-1) % 120 == 0:
            e = (n*n-1)//120
            if e <= N: d[e] -= ch
        n += 1
    return d
def false_theta_2311(N):
    """chi odd mod 132, support +-{5,17,49,61}, exponent (n^2-25)/264"""
    CH = {5: 1, 17: -1, 49: -1, 61: 1, 71: -1, 83: 1, 115: 1, 127: -1}
    d = [0]*(N+1); n = 1
    while (n*n-25)//264 <= N:
        if (n*n-25) % 264 == 0:
            e = (n*n-25)//264
            if 0 <= e <= N and n % 132 in CH: d[e] += CH[n % 132]
        n += 1
    return d
def conv(a, b, N):
    c = [0]*(N+1)
    for i, x in enumerate(a):
        if not x: continue
        for j in range(0, N+1-i): c[i+j] += x*b[j]
    return c

OK = {}
print("=" * 78); print("CONTROLS"); print("=" * 78)
I1 = inv_qq(N, 1)
c1 = fit3(I1, N//2, N)
print("   C1  c_eff(1/(q;q)_inf)   = %.6f   (must be 1)" % c1)
OK["C1  estimator gives 1 on 1/(q;q)_inf"] = abs(c1-1.0) < 0.02
I2 = inv_qq(N, 2)
c2 = fit3(I2, N//2, N)
print("   C2  c_eff(1/(q;q)_inf^2) = %.6f   (must be 2 -- the estimator is not stuck at 1)" % c2)
OK["C2  estimator gives 2 on the square, so it is not stuck at 1"] = abs(c2-2.0) < 0.05
FT = false_theta_235(N)
c3 = fit3(FT, N//2, N)
print("   C3  c_eff(bare false theta, Sigma(2,3,5)) = %.6f   (must be 0)" % c3)
OK["C3  estimator gives 0 on a bare false theta"] = abs(c3) < 0.02

print(); print("=" * 78)
print("THE CELL  --  Zhat^unred = Zhat / (q)_inf, GM Remark 3.8, for two different p")
print("=" * 78)
vals = []
for name, ft, p in (("Sigma(2,3,5)", FT, 30), ("Sigma(2,3,11)", false_theta_2311(N), 66)):
    U = conv(ft, I1, N)
    c = fit3(U, N//2, N); vals.append(c)
    cc = 13 - 6*(p + 1.0/p)
    print("   %-14s p = %-3d   singlet c = 13 - 6(p+1/p) = %10.3f    c_eff(Zhat^unred) = %.6f"
          % (name, p, cc, c))
spread = max(vals) - min(vals)
print()
print("   c varies by %.1f between these two; c_eff varies by %.4f." % (
      abs((13-6*(30+1/30.)) - (13-6*(66+1/66.))), spread))
print("   CELL -> OUTCOME %s" % ("A" if spread > 0.1 else "B"))
OK["CELL -> B : c_eff is 1 for both, independent of p"] = (spread < 0.1 and
    all(abs(v-1.0) < 0.03 for v in vals))

print(); print("=" * 78); print("CONTROLS AND CELL"); print("=" * 78)
for k, v in OK.items(): print("   %-62s %s" % (k, "PASSED" if v else "FAILED"))
print("""
WHAT THIS ANSWERS OF Q11, AND WHAT IT DOES NOT.

Q11 asked three things.  Two are now decidable from what this bench holds.

  "Is there a KNOWN MECHANISM attaching modular boundary data to the unquantized sector?"
  PARTLY ANSWERED, and the answer is: for BRIESKORN SPHERES yes, and GM name it -- the
  logarithmic (1,p) singlet VOA.  For HYPERBOLIC manifolds, GM themselves name it OPEN, in
  print, and point at the figure-eight surgeries specifically.  So the honest reply to Q11's
  own "if the answer is 'read GPPV', that alone is worth the email" is: reading it says the
  hyperbolic case is open in the literature, not that we failed to find it.

  "Does it carry a character with c_eff = 6?"  ANSWERED, NEGATIVELY, AND STRUCTURALLY.
  Zhat^unred = (false theta)/(q)_inf by Remark 3.8.  A false theta has bounded coefficients
  and contributes 0; 1/(q)_inf contributes 1.  So c_eff = 1, and p cancels out COMPLETELY:
  the two spheres above differ by 216 in c and by less than 0.03 in c_eff.  6 is not
  reachable by choosing a different 3-manifold in this family.

  "Is the obstruction general, or specific to the integer-level attachment?"  NOT ANSWERED
  HERE, and it is the part that genuinely needs the expert.  What is now established is
  narrower and sharper than the original question: the obstruction is not amphichirality
  and not our knot -- it is the SHAPE (false theta)/(q)_inf that Zhat-type invariants have.
  Whether some other boundary object escapes that shape is exactly what remains open.

THIS IS ALSO WHY MEMO 171's "1" WAS RIGHT FOR THE WRONG REASON.  GC-6 read c = 6 as six
cusp-boson units of which the object supplies one, and memo 171 found the 1 was
c_eff(eta^-1) -- a free boson used as a MODEL, never the object.  The 1 is now the object's
own, and it is not a coincidence of modelling: it is what (false theta)/(q)_inf always
gives.  Same number, different standing.""")
assert all(OK.values()), OK
