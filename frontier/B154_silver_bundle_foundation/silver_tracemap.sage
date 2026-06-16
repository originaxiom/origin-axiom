# Phase C step 1 (structured): the silver bundle SL(2) character variety via the trace-map fixed locus.
# Fricke coords (x,y,z)=(trA,trB,trAB). Dehn twists on F_2 (matching the toolkit's phi_fig=A->A^2B,B->AB):
#   sigma_R: A->A,  B->AB   induces (x,y,z) -> (x, z, x*z - y)         [trA fixed, trB->trAB, trAB->tr(A^2B)=xz-y]
#   sigma_L: A->AB, B->B    induces (x,y,z) -> (z, y, y*z - x)
# phi_fig    = sigma_R o sigma_L  (figure-eight, M1^2);  phi_silver = sigma_R^2 o sigma_L^2 (silver, M2^2).
# Bundle reps = FIXED POINTS of phi on (x,y,z) (the monodromy preserves the character). kappa=tr[A,B]
# = x^2+y^2+z^2-xyz-2 (Fricke). Compare the figure-eight (known: B67) and silver fixed loci + kappa.
R.<x,y,z> = QQ[]
def sR(p): X,Y,Z=p; return (X, Z, X*Z - Y)
def sL(p): X,Y,Z=p; return (Z, Y, Y*Z - X)
def comp(f,g): return lambda p: f(g(p))
def power(f,k):
    h=lambda p:p
    for _ in range(k): h=comp(f,h)
    return h
# Characters transform CONTRAVARIANTLY: trace map of phi=sigma_R o sigma_L is tsigma_L o tsigma_R (reversed).
phi_fig    = comp(sL, sR)
phi_silver = comp(power(sL,2), power(sR,2))
kappa = x^2+y^2+z^2-x*y*z-2

for label,phi in [("figure-eight (RL)",phi_fig),("silver (R^2L^2)",phi_silver)]:
    p=(x,y,z); img=phi(p)
    print("="*70); print(label)
    print("  trace map (x,y,z) ->")
    for c,e in zip("xyz",img): print(f"     {c}' = {e}")
    fixed=[R(img[i]-p[i]) for i in range(3)]
    I=R.ideal(fixed)
    print("  fixed-locus ideal dim:", I.dimension())
    comps=I.minimal_associated_primes()
    print("  #components:", len(comps))
    for k,P in enumerate(comps):
        d=P.dimension()
        # kappa reduced modulo the component (is it constant / what relation?)
        kred = P.reduce(kappa)
        print(f"    comp[{k}] dim {d}: gens={[g for g in P.gens()]}")
        print(f"        kappa mod comp = {kred}")
