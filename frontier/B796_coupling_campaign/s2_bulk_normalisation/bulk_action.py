r"""S2 — the bulk normalisation, and the split the weight ledger implies.

THE OWED CHECK
--------------
THE_FRAMEWORK banks the Gukov split k*I_CS + i*sigma*I_grav, with k quantized,
sigma not, G_N = 1/(4 sigma), and CS = 0 exactly on this object -- so the
quantized half vanishes and only the unquantized gravitational term survives.
It carries the note: "(Normalisation check owed before this is a claim rather
than a lead.)"

This does that check, in the cleanest available frame: Euclidean 3d gravity
with Lambda < 0, whose saddle for a closed/cusped hyperbolic 3-manifold is the
hyperbolic metric itself.

THE POINT, and it is not the arithmetic
---------------------------------------
Carrying the units through splits the "one external input" into TWO inputs of
DIFFERENT WEIGHT -- and the weight ledger excludes only one of them.

Gate 5-Q. Structure only; no measured quantity, no value compared to anything.
"""
from mpmath import mp, mpf, pi, nstr

mp.dps = 30

VOL = mpf('2.02988321281930725004240510849')   # m004, at K = -1
CS = mpf(0)                                     # exactly, forced by amphichirality

print('S2  THE BULK NORMALISATION')
print('=' * 64)

print('\n1. THE ON-SHELL ACTION, units carried explicitly')
print('   Euclidean EH with Lambda = -1/l^2 :')
print('     I = -(1/16 pi G) Int d^3x sqrt(g) (R - 2 Lambda)')
print('   on a hyperbolic saddle  R = -6/l^2,  so  R - 2 Lambda = -4/l^2,')
print('   and the geometric volume is  V_g = l^3 * Vol(M)  with Vol(M) the')
print('   K = -1 volume -- a PURE NUMBER (weight-ledger: volume is weight +3,')
print('   and l^3 carries exactly that weight, so Vol(M) is weight 0).')
print()
print('     I = (1/16 pi G)(4/l^2)(l^3 Vol) = (l / 4 pi G) * Vol(M)')

print('\n2. IN BROWN-HENNEAUX VARIABLES')
print('   c = 3l / 2G   (dimensionless)   =>   l/G = 2c/3')
print('     I = (c / 6 pi) * Vol(M)')
coeff = VOL / (6 * pi)
print(f'   for m004:  I = c * {nstr(coeff, 18)}')
print(f'              (Vol = {nstr(VOL, 20)})')

print('\n3. THE QUANTIZED HALF IS GONE')
print(f'   Gukov: S = k*I_CS + i*sigma*I_grav,  k in Z,  sigma not quantized.')
print(f'   m004 has CS = {int(CS)} EXACTLY (amphichirality: Z_k = Z_-k).')
print('   So the k-term vanishes identically and only the sigma-term survives.')
print('   The object deletes the quantized half of its own action.')

print('\n4. THE SPLIT -- and this is the result')
print('   Two independent external data hide inside "one input":')
print()
print('     c = 3l/2G   : WEIGHT 0   -- a ratio of two lengths.')
print('                   NOT excluded by the weight ledger. It lives in the')
print('                   dimensionless sector, the one sector the object CAN')
print('                   in principle speak to.')
print('     l           : WEIGHT +1  -- a length.')
print('                   EXCLUDED. Hom(G,R+) = 0 and scale-covariance forbid')
print('                   any internal relation from fixing it, on any face.')
print()
print('   So the honest statement is not "the object needs one external input".')
print('   It is:')
print('     * the object needs exactly ONE dimensionful input (l), forever;')
print('     * and ONE dimensionless input (c) which is NOT forbidden to it.')

print('\n5. WHAT WOULD DISCHARGE THE SECOND HALF')
print('   Any weight-0 route to c. The object has weight-0 faces (8 of 11) and')
print('   a boundary; c is a boundary central charge. This does NOT compute it')
print('   and does not claim it is computable -- it establishes only that the')
print('   weight ledger does not forbid it, which was previously assumed.')

# the one assertion: the coefficient is the object's own volume over 6 pi
assert abs(coeff * 6 * pi - VOL) < mpf('1e-25')
print('\n   self-check: I/c * 6 pi == Vol(m004)   OK')
print('=' * 64)
