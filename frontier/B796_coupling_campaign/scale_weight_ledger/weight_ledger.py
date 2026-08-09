r"""THE WEIGHT LEDGER — dimensional analysis of the whole programme.

Every hyperbolic quantity the programme banks is computed at curvature
K = -1, which silently fixes the unit of length at the curvature radius R.
Nothing in the corpus asks what that convention is carrying.

This assigns each kind of quantity its scaling weight under

        g  ->  k^2 g        (equivalently  R -> kR)

and derives three consequences. Gate 5-Q: no comparison to any physical
constant is made here. Structure only.

Reproduce: python3 weight_ledger.py
"""
from mpmath import mp, mpf, power, nstr

mp.dps = 50

# ---------------------------------------------------------------- inputs
# Every value below is banked on origin/main. Sources in FINDINGS.md.
VOL = mpf('2.02988321281930725004240510849')   # m004, Humbert / snappy
SYS = mpf('1.08707014499574')                  # B850 shortest geodesic
R2 = mpf('4.9000853730625213014795758050759')  # lambda2, 25 certified digits (B922)
RP = mpf('7.0720041858752050007371941867273')  # parent, landed 2026-08-09

LAM = lambda r: 1 + r * r                      # H^3 convention, lam = 1 + r^2

# ------------------------------------------------------- the weight table
WEIGHTS = [
    ('length  (systole, core length, complex length)', +1),
    ('area    (cusp cross-section, maximal cusp area)', +2),
    ('volume', +3),
    ('Laplace eigenvalue  lambda = 1 + r^2', -2),
    ('volume entropy  h = 2/R', -1),
    ('trace, trace field element, Galois datum', 0),
    ('Chern-Simons invariant, torsion, eta', 0),
    ('cusp SHAPE tau  (not cusp area)', 0),
    ('level, conductor, index, cohomology class', 0),
]

# faces of the anatomy (B738 kill_graph), by the weight of the data they carry
FACES = [
    ('being                 Q(sqrt-3), traces, 2T, E6', 0),
    ('hearing               Q(sqrt5), golden, monodromy', 0),
    ('meeting               Q(sqrt-15), the V4 compositum', 0),
    ('congruence-tower      levels, reductions mod n', 0),
    ('sln-tower             SL(n) reps, Procesi', 0),
    ('coupled-double        amalgam, mirror-double', 0),
    ('mtc-overlay           MTC, WRT, quantum groups at level k', 0),
    ('infinite-hecke        Hecke, Bianchi, newforms', 0),
    ('children              Dehn fillings: closed volumes, core lengths', +3),
    ('emittance-lengths     the voice: geodesic length spectrum', +1),
    ('emittance-eigenvalues the heartbeat: Laplace spectrum', -2),
]


def main():
    print('=' * 72)
    print('THE WEIGHT LEDGER   (scaling under g -> k^2 g, i.e. R -> kR)')
    print('=' * 72)
    for name, w in WEIGHTS:
        print(f'  {w:+2}   {name}')

    print()
    print('=' * 72)
    print('CONSEQUENCE 1 — the faces, by whether they can carry a scale at all')
    print('=' * 72)
    zero = [f for f, w in FACES if w == 0]
    nonzero = [(f, w) for f, w in FACES if w != 0]
    for f, w in FACES:
        tag = 'SCALE-BLIND' if w == 0 else 'scale-sensitive'
        print(f'  {w:+2}   {tag:16} {f}')
    print(f'\n  {len(zero)} of {len(FACES)} faces carry ONLY weight-0 data.')
    print('  A weight-0 structure cannot produce a weight-nonzero output.')
    print('  That is the whole content of Hom(G, R+) = 0 for finite/profinite G')
    print('  (the B666 scale-torsor no-go), restated as dimensional analysis:')
    print('  you cannot get a length out of a trace, and no cohomology is needed.')
    print(f'\n  The {len(nonzero)} scale-sensitive faces are exactly:')
    for f, w in nonzero:
        print(f'      weight {w:+2}   {f}')
    print('  — which is why the no-go\'s hypothesis class genuinely excludes')
    print('  emittance, as B738\'s shortlist says. The programme is right there.')

    print()
    print('=' * 72)
    print('CONSEQUENCE 2 — but emittance does not escape, and here is why')
    print('=' * 72)
    print('  A scale exists iff the object forces a relation between quantities')
    print('  of DIFFERENT weight. Such a relation has a unique solution for R.')
    print('  Example of the shape required:  lambda * systole^k = const, k != 2.')
    print()
    print('  Hyperbolic geometry is EXACTLY scale-covariant: R -> kR carries')
    print('  every relation to a relation, preserving weight. So no internal')
    print('  relation can be weight-inhomogeneous, on any face, including')
    print('  emittance. The eigenvalues are weight -2; they are numbers in')
    print('  units of R, exactly as the volume is.')
    print()
    print('  Therefore the anchor cannot come from the spectrum either — not')
    print('  because a theorem forbids it, but because there is nothing for a')
    print('  theorem to forbid. The programme\'s highest-rated escape route')
    print('  (native-continuous-channel, mean revival 3.19) is closed for the')
    print('  DIMENSIONFUL reading of the anchor question.')

    print()
    print('=' * 72)
    print('CONSEQUENCE 3 — the positive statement: ONE input, not a gap')
    print('=' * 72)
    print('  The object is a SHAPE, and a shape has no size. Fix the curvature')
    print('  radius R once, from outside, and EVERY dimensionful quantity is')
    print('  then determined with no further freedom:')
    print()
    print(f'      volume        = {nstr(VOL, 12)} * R^3')
    print(f'      systole       = {nstr(SYS, 12)} * R')
    print(f'      lambda_2      = {nstr(LAM(R2), 12)} / R^2')
    print(f'      lambda_parent = {nstr(LAM(RP), 12)} / R^2')
    print()
    print('  So "zero free parameters" is precisely: zero free SHAPE parameters,')
    print('  one free SCALE parameter. That is not a missing ingredient. It is')
    print('  one number, and it must come from outside — which is what B151')
    print('  already observed ("all dimensionful content carried by hbar<->k ...')
    print('  and none by the invariant"), stated here as a weight identity.')

    print()
    print('=' * 72)
    print('CONSEQUENCE 4 — what needs NO input at all: the weight-0 observables')
    print('=' * 72)
    print('  These are canonical, choice-free, and independent of R. They are')
    print('  the object\'s genuine scale-free numbers, and the dimensionless')
    print('  sector of physics is the only sector they could ever address.')
    print()
    l2, lp = LAM(R2), LAM(RP)
    inv = [
        ('lambda_2 * vol^(2/3)', l2 * power(VOL, mpf(2) / 3), '-2 +2 = 0'),
        ('lambda_parent * vol^(2/3)', lp * power(VOL, mpf(2) / 3), '-2 +2 = 0'),
        ('lambda_2 * systole^2', l2 * SYS ** 2, '-2 +2 = 0'),
        ('lambda_parent * systole^2', lp * SYS ** 2, '-2 +2 = 0'),
        ('systole^3 / vol', SYS ** 3 / VOL, '+3 -3 = 0'),
        ('systole / vol^(1/3)', SYS / power(VOL, mpf(1) / 3), '+1 -1 = 0'),
        ('lambda_parent / lambda_2', lp / l2, '-2 +2 = 0'),
    ]
    for name, val, wsum in inv:
        print(f'  {name:28} = {nstr(val, 22):26} [{wsum}]')
    print()
    print('  Precision note: only lambda_2 (25 digits) and the parent (this')
    print('  seat, gates passed) are certified deep. VOL is exact to the digits')
    print('  shown; SYS is quoted from B850 at 15 figures, so any product with')
    print('  SYS is trustworthy to ~15 figures only. lambda_1 is NOT used: it')
    print('  is not banked at certified depth on origin/main.')

    # the ledger's own consistency check
    assert abs(LAM(R2) - mpf('25.010836663301268558765')) < mpf('1e-20')
    print('\n  self-check: lambda_2 = 1 + r^2 reproduces B922\'s banked value  OK')


if __name__ == '__main__':
    main()
