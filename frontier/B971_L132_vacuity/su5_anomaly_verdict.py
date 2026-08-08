#!/usr/bin/env python
"""
B971 / L132 -- the load-bearing anomaly computation, done from scratch.

Everything below is COMPUTED in-sandbox with exact rationals (sympy.Rational).
Nothing is read from B864, B951 or the scout files; the numerical agreements
reported at the end are checked afterwards, as reproductions.

CONSTRUCTION (so that hypercharge is DERIVED, not assigned):

  * SU(5) fundamental 5 = five basis indices; 0,1,2 carry the SU(3) fundamental,
    3,4 carry the SU(2) fundamental.
  * The unique traceless SU(5) Cartan direction commuting with SU(3)xSU(2) is
    diag(a,a,a,b,b) with 3a+2b=0.  Solved here.  Normalisation fixed by the one
    convention Q_em = T3 + Y  (equivalently: Y(weak index) = +1/2).
  * 10 = Lambda^2(5): states are index pairs i<j, Y = Y_i + Y_j, and the
    SU(3)/SU(2) rep labels follow from which indices the pair uses.
  * 5bar = conjugate of 5 (Y -> -Y, 3 -> 3bar, 2 -> 2).
  * 27 of E6 under SO(10)xU(1)_psi then SU(5)xU(1)_chi:
        27 = 16_(psi=1) + 10_(psi=-2) + 1_(psi=4)
        16 = 10_(chi=-1) + 5bar_(chi=3) + 1_(chi=-5)
        10 = 5_(chi=2)  + 5bar_(chi=-2)
        1  = 1_(chi=0)
    (branching pattern: CITED standard E6 group theory, not re-derived.
     The U(1) charge NORMALISATIONS are then checked here for tracelessness,
     which is a genuine consistency test of the assignment.)

ANOMALY FUNCTIONALS (all fermions written as left-handed Weyl; conventions
stated, coefficients computed):

  grav[Q]      = sum_states Q                     (U(1)-gravitational)
  cubic[Q]     = sum_states Q^3                   ([U(1)]^3)
  A33Q[Q]      = sum_states T3(colour) * Q        ([SU(3)]^2 U(1))
  A22Q[Q]      = sum_states T2(weak)   * Q        ([SU(2)]^2 U(1))
  A333         = sum_states A3(colour)            ([SU(3)]^3)
  witten       = (# SU(2) doublets) mod 2         (global SU(2))

with T(3)=T(3bar)=1/2, T(1)=0, T(2)=1/2, A3(3)=+1, A3(3bar)=-1, A3(1)=0.
"""

import json
from itertools import combinations
from fractions import Fraction as F

# ----------------------------------------------------------------- step 0
# The hypercharge generator, DERIVED.
# Traceless diag(a,a,a,b,b); 3a+2b = 0; normalisation b = +1/2 (Q = T3 + Y).
import sympy as sp

a, b = sp.symbols('a b', rational=True)
sol = sp.solve([3*a + 2*b, b - sp.Rational(1, 2)], [a, b], dict=True)[0]
Y5 = [sol[a]]*3 + [sol[b]]*2          # Y on the 5 of SU(5)
assert sum(Y5) == 0
Y5 = [F(int(sp.nsimplify(y).p), int(sp.nsimplify(y).q)) for y in Y5]

COLOUR_IDX = (0, 1, 2)
WEAK_IDX = (3, 4)

# ----------------------------------------------------------------- step 1
# Build the SU(5) irreps as explicit multiplet lists.
# A multiplet = dict(name, c, w, Y) where c in {'3','3b','1'}, w in {'2','1'}.


def five():
    """5 of SU(5) = (3,1)_{-1/3} + (1,2)_{+1/2}  -- labels derived from indices."""
    return [dict(name='D  (3,1)', c='3', w='1', Y=Y5[0]),
            dict(name='Hu (1,2)', c='1', w='2', Y=Y5[3])]


def fivebar():
    return [dict(name=m['name'].replace('D  (3,1)', 'dc (3b,1)')
                 .replace('Hu (1,2)', 'Hd (1,2)'),
                 c={'3': '3b', '3b': '3', '1': '1'}[m['c']],
                 w=m['w'], Y=-m['Y']) for m in five()]


def ten():
    """10 = Lambda^2(5).  Group the 10 index-pairs by (colour rep, weak rep, Y)."""
    buckets = {}
    for i, j in combinations(range(5), 2):
        Yij = Y5[i] + Y5[j]
        nc = sum(1 for k in (i, j) if k in COLOUR_IDX)
        nw = sum(1 for k in (i, j) if k in WEAK_IDX)
        if nc == 2:      # antisym of 3 x 3 = 3bar
            c, w = '3b', '1'
        elif nc == 1:    # 3 x 2
            c, w = '3', '2'
        else:            # antisym of 2 x 2 = singlet
            c, w = '1', '1'
        buckets.setdefault((c, w, Yij), 0)
        buckets[(c, w, Yij)] += 1
    out = []
    for (c, w, Yv), n in sorted(buckets.items(), key=lambda kv: -kv[0][2]):
        dim = (3 if c in ('3', '3b') else 1) * (2 if w == '2' else 1)
        assert n == dim, (c, w, Yv, n, dim)   # the grouping must fill whole multiplets
        nm = {('3', '2'): 'Q  (3,2)', ('3b', '1'): 'uc (3b,1)',
              ('1', '1'): 'ec (1,1)'}[(c, w)]
        out.append(dict(name=nm, c=c, w=w, Y=Yv))
    return out


def singlet(nm='S  (1,1)'):
    return [dict(name=nm, c='1', w='1', Y=F(0))]


# ----------------------------------------------------------------- step 2
# The 27, assembled with psi (SO(10) grading) and chi (SU(5) grading) charges.
def tag(mults, psi, chi, src):
    out = []
    for m in mults:
        d = dict(m)
        d['psi'] = F(psi)
        d['chi'] = F(chi)
        d['src'] = src
        out.append(d)
    return out


SPECTRUM_27 = (
    tag(ten(),          1, -1, '16 / 10')
    + tag(fivebar(),    1,  3, '16 / 5bar')
    + tag(singlet('N  (1,1) [nu_R]'), 1, -5, '16 / 1')
    + tag([dict(m, name=m['name'].replace('D  (3,1)', 'D  (3,1) [exotic]')
                .replace('Hu (1,2)', 'Hu (1,2) [exotic]')) for m in five()],
          -2, 2, '10 / 5')
    + tag([dict(m, name=m['name'].replace('dc (3b,1)', 'Dc (3b,1) [exotic]')
                .replace('Hd (1,2)', 'Hd (1,2) [exotic]')) for m in fivebar()],
          -2, -2, '10 / 5bar')
    + tag(singlet('S  (1,1) [E6 singlet]'), 4, 0, '1 / 1')
)


def dim(m):
    return (3 if m['c'] in ('3', '3b') else 1) * (2 if m['w'] == '2' else 1)


assert sum(dim(m) for m in SPECTRUM_27) == 27

# ----------------------------------------------------------------- step 3
# Anomaly functionals.
T3 = {'3': F(1, 2), '3b': F(1, 2), '1': F(0)}
A3 = {'3': 1, '3b': -1, '1': 0}
T2 = {'2': F(1, 2), '1': F(0)}
NC = {'3': 3, '3b': 3, '1': 1}
NW = {'2': 2, '1': 1}


def Q_of(m, coef):
    """General abelian direction Q = aY + b*chi + c*psi."""
    A, B, C = coef
    return A*m['Y'] + B*m['chi'] + C*m['psi']


def anomalies(mults, coef=(F(1), F(0), F(0))):
    grav = cubic = a33 = a22 = F(0)
    a333 = 0
    ndoub = 0
    for m in mults:
        q = Q_of(m, coef)
        n = dim(m)
        grav += n*q
        cubic += n*q**3
        a33 += NW[m['w']] * T3[m['c']] * q
        a22 += NC[m['c']] * T2[m['w']] * q
        a333 += NW[m['w']] * A3[m['c']]
        if m['w'] == '2':
            ndoub += NC[m['c']]
    return dict(grav=grav, cubic=cubic, a33Q=a33, a22Q=a22,
                a333=a333, doublets=ndoub, witten_parity=ndoub % 2)


def fmt(d):
    return {k: (str(v) if isinstance(v, F) else v) for k, v in d.items()}


# ----------------------------------------------------------------- step 4
# Report.
RESULT = {}
lines = []


def say(s=''):
    lines.append(s)
    print(s)


say("=" * 78)
say("DERIVED HYPERCHARGE GENERATOR ON THE 5 OF SU(5)")
say("=" * 78)
say(f"  unique traceless diag(a,a,a,b,b) with 3a+2b=0, normalised b=+1/2:")
say(f"     Y(5) = {[str(y) for y in Y5]}   sum = {sum(Y5)}")
RESULT['Y_on_5'] = [str(y) for y in Y5]

say()
say("=" * 78)
say("THE 27, STATE BY STATE  (all left-handed Weyl)")
say("=" * 78)
say(f"  {'source':<12} {'multiplet':<22} {'dim':>4} {'Y':>7} {'chi':>5} {'psi':>5}")
tbl = []
for m in SPECTRUM_27:
    say(f"  {m['src']:<12} {m['name']:<26} {dim(m):>4} {str(m['Y']):>7} "
        f"{str(m['chi']):>5} {str(m['psi']):>5}")
    tbl.append(dict(src=m['src'], name=m['name'], dim=dim(m), Y=str(m['Y']),
                    chi=str(m['chi']), psi=str(m['psi'])))
say(f"  {'':<12} {'TOTAL':<22} {sum(dim(m) for m in SPECTRUM_27):>4}")
RESULT['spectrum_27'] = tbl

# tracelessness consistency checks on the U(1) normalisations
for lab, key in (('chi', 'chi'), ('psi', 'psi')):
    tot = sum(dim(m)*m[key] for m in SPECTRUM_27)
    say(f"  consistency: sum over 27 of {lab} = {tot}")
    RESULT[f'trace_{lab}_over_27'] = str(tot)

# ----------------------------------------------------------------- step 5
say()
say("=" * 78)
say("PART 1 -- THE FOUR SM ANOMALY COEFFICIENTS ON THE COMPLETE 27, Q = Y")
say("=" * 78)

PIECES = {
    'SU(5) 10   (in 16)':   [m for m in SPECTRUM_27 if m['src'] == '16 / 10'],
    'SU(5) 5bar (in 16)':   [m for m in SPECTRUM_27 if m['src'] == '16 / 5bar'],
    'SU(5) 1    (in 16)':   [m for m in SPECTRUM_27 if m['src'] == '16 / 1'],
    'SU(5) 5    (in 10)':   [m for m in SPECTRUM_27 if m['src'] == '10 / 5'],
    'SU(5) 5bar (in 10)':   [m for m in SPECTRUM_27 if m['src'] == '10 / 5bar'],
    'SU(5) 1    (E6 sglt)': [m for m in SPECTRUM_27 if m['src'] == '1 / 1'],
}
hdr = f"  {'piece':<22} {'grav=TrY':>10} {'[U1]^3':>10} {'[SU3]^2Y':>10} {'[SU2]^2Y':>10} {'[SU3]^3':>9} {'doub':>5}"
say(hdr)
say("  " + "-" * (len(hdr) - 2))
per_piece = {}
for k, v in PIECES.items():
    r = anomalies(v)
    per_piece[k] = fmt(r)
    say(f"  {k:<22} {str(r['grav']):>10} {str(r['cubic']):>10} {str(r['a33Q']):>10} "
        f"{str(r['a22Q']):>10} {r['a333']:>9} {r['doublets']:>5}")
tot = anomalies(SPECTRUM_27)
say("  " + "-" * (len(hdr) - 2))
say(f"  {'COMPLETE 27':<22} {str(tot['grav']):>10} {str(tot['cubic']):>10} {str(tot['a33Q']):>10} "
    f"{str(tot['a22Q']):>10} {tot['a333']:>9} {tot['doublets']:>5}")
RESULT['per_su5_piece_Y'] = per_piece
RESULT['complete_27_Y'] = fmt(tot)

# ----------------------------------------------------------------- step 6
say()
say("=" * 78)
say("PART 2 -- THE DISCRIMINATING QUESTION: cancellation, or separately zero?")
say("=" * 78)

SO10 = {
    '16  (SO(10) spinor)': [m for m in SPECTRUM_27 if m['src'].startswith('16')],
    '10  (SO(10) vector)': [m for m in SPECTRUM_27 if m['src'].startswith('10')],
    '1   (SO(10) sglt)':   [m for m in SPECTRUM_27 if m['src'].startswith('1 /')],
}
say(hdr)
say("  " + "-" * (len(hdr) - 2))
so10_res = {}
for k, v in SO10.items():
    r = anomalies(v)
    so10_res[k] = fmt(r)
    say(f"  {k:<22} {str(r['grav']):>10} {str(r['cubic']):>10} {str(r['a33Q']):>10} "
        f"{str(r['a22Q']):>10} {r['a333']:>9} {r['doublets']:>5}")
RESULT['per_so10_piece_Y'] = so10_res

# the SM generation (15) vs the twelve exotics
GEN15 = [m for m in SPECTRUM_27 if m['src'] in ('16 / 10', '16 / 5bar')]
EXO12 = [m for m in SPECTRUM_27 if m['src'] not in ('16 / 10', '16 / 5bar')]
assert sum(dim(m) for m in GEN15) == 15 and sum(dim(m) for m in EXO12) == 12
say("  " + "-" * (len(hdr) - 2))
for k, v in (('SM generation (15)', GEN15), ('the twelve exotics', EXO12)):
    r = anomalies(v)
    RESULT[('gen15' if '15' in k else 'exotics12') + '_Y'] = fmt(r)
    say(f"  {k:<22} {str(r['grav']):>10} {str(r['cubic']):>10} {str(r['a33Q']):>10} "
        f"{str(r['a22Q']):>10} {r['a333']:>9} {r['doublets']:>5}")

# Is the exotic set a REAL (vector-like) SM representation?  Computed by pairing.
CONJ = {'3': '3b', '3b': '3', '1': '1'}


def is_real_rep(mults):
    """True iff every (c,w,Y) multiplet is matched by its conjugate (c*,w,-Y)."""
    from collections import Counter
    cnt = Counter((m['c'], m['w'], m['Y']) for m in mults)
    for (c, w, Yv), n in cnt.items():
        if cnt.get((CONJ[c], w, -Yv), 0) != n:
            return False
    return True


say()
say(f"  exotic 12 is a REAL (vector-like) rep of SU(3)xSU(2)xU(1)?  "
    f"{is_real_rep(EXO12)}")
say(f"  SM generation 15 is a REAL rep?                            "
    f"{is_real_rep(GEN15)}")
say(f"  complete 27 is a REAL rep?                                 "
    f"{is_real_rep(SPECTRUM_27)}")
RESULT['exotics12_is_real_rep'] = is_real_rep(EXO12)
RESULT['gen15_is_real_rep'] = is_real_rep(GEN15)
RESULT['full27_is_real_rep'] = is_real_rep(SPECTRUM_27)

# ----------------------------------------------------------------- step 7
say()
say("=" * 78)
say("PART 3 -- MB12: CAN THE CHECK FAIL?  (live controls)")
say("=" * 78)
controls = {
    'lone SU(5) 10':            [m for m in SPECTRUM_27 if m['src'] == '16 / 10'],
    'lone SU(5) 5bar':          [m for m in SPECTRUM_27 if m['src'] == '16 / 5bar'],
    '27 minus e^c':             [m for m in SPECTRUM_27 if m['name'] != 'ec (1,1)'],
    '27 minus the 5 of the 10': [m for m in SPECTRUM_27 if m['src'] != '10 / 5'],
    '16 minus nu_R (=15)':      GEN15,
    'exotics only (12)':        EXO12,
}
say(hdr)
say("  " + "-" * (len(hdr) - 2))
ctrl = {}
for k, v in controls.items():
    r = anomalies(v)
    ctrl[k] = fmt(r)
    flag = "  <-- FAILS (nonzero)" if any(
        r[x] != 0 for x in ('grav', 'cubic', 'a33Q', 'a22Q', 'a333')) or r['witten_parity'] else ""
    say(f"  {k:<22} {str(r['grav']):>10} {str(r['cubic']):>10} {str(r['a33Q']):>10} "
        f"{str(r['a22Q']):>10} {r['a333']:>9} {r['doublets']:>5}{flag}")
RESULT['controls'] = ctrl

# ----------------------------------------------------------------- step 8
say()
say("=" * 78)
say("PART 4 -- DOES Y FALL OUT?  general Q = aY + b*chi + c*psi")
say("=" * 78)
A, B, C = sp.symbols('A B C', rational=True)


def sym_anom(mults):
    grav = cubic = a33 = a22 = sp.Integer(0)
    for m in mults:
        q = A*sp.Rational(m['Y'].numerator, m['Y'].denominator) \
            + B*sp.Rational(m['chi'].numerator, m['chi'].denominator) \
            + C*sp.Rational(m['psi'].numerator, m['psi'].denominator)
        n = dim(m)
        grav += n*q
        cubic += n*q**3
        a33 += NW[m['w']] * sp.Rational(T3[m['c']].numerator, T3[m['c']].denominator) * q
        a22 += NC[m['c']] * sp.Rational(T2[m['w']].numerator, T2[m['w']].denominator) * q
    return [sp.expand(grav), sp.expand(cubic), sp.expand(a33), sp.expand(a22)]


def solution_space(mults, label):
    eqs = sym_anom(mults)
    names = ['grav', '[U1]^3', '[SU3]^2 Q', '[SU2]^2 Q']
    say(f"\n  --- {label} ---")
    for n, e in zip(names, eqs):
        say(f"     {n:<10} = {e}")
    sols = sp.solve(eqs, [A, B, C], dict=True)
    # dimension of the solution variety: count free params in the generic branch
    identically_zero = all(sp.simplify(e) == 0 for e in eqs)
    if identically_zero:
        dimn = 3
        note = "EVERY abelian direction is anomaly-free  ==>  NO SELECTION (vacuous)"
    else:
        # characterise: solve the linear ones, then impose the cubic
        lin = [e for e, n in zip(eqs, names) if n != '[U1]^3']
        linsol = sp.linsolve(lin, [A, B, C])
        pars = sorted((set().union(*[e.free_symbols for e in list(linsol)[0]]) & {A, B, C}),
                      key=str)
        dimn = len(pars)
        note = f"solution space dimension {dimn} over the linear conditions: {list(linsol)[0]}"
        # check the cubic on that space
        sub = list(linsol)[0]
        cub = sp.expand(eqs[1].subs({A: sub[0], B: sub[1], C: sub[2]}))
        note += f"   |  cubic there = {sp.simplify(cub)}"
    say(f"     => {note}")
    return dict(equations={n: str(e) for n, e in zip(names, eqs)},
                identically_zero=identically_zero, dim=dimn, note=note,
                raw_solve=str(sols))


RESULT['general_direction'] = {
    'complete_27': solution_space(SPECTRUM_27, "over the COMPLETE 27"),
    'SO10_16': solution_space([m for m in SPECTRUM_27 if m['src'].startswith('16')],
                              "over the complete 16 (SO(10) spinor)"),
    'SM_generation_15': solution_space(GEN15, "over the chiral 15 (SM generation)"),
}

# ----------------------------------------------------------------- step 9
say()
say("=" * 78)
say("PART 5 -- REPRODUCTIONS OF PRIOR IN-CORPUS ARITHMETIC (checked after the fact)")
say("=" * 78)
psi_only = (F(0), F(0), F(1))
chi_only = (F(0), F(1), F(0))
rep = {}
for lab, mults, coef in (
    ('psi over full 27', SPECTRUM_27, psi_only),
    ('psi over the 16', [m for m in SPECTRUM_27 if m['src'].startswith('16')], psi_only),
    ('chi over the 16', [m for m in SPECTRUM_27 if m['src'].startswith('16')], chi_only),
    ('chi over 10+5bar (=15)', GEN15, chi_only),
):
    r = anomalies(mults, coef)
    rep[lab] = fmt(r)
    say(f"  {lab:<24} Tr = {str(r['grav']):>6}   Tr^3 = {str(r['cubic']):>8}   "
        f"[SU3]^2 = {str(r['a33Q']):>6}   [SU2]^2 = {str(r['a22Q']):>6}")
RESULT['reproductions'] = rep

# ----------------------------------------------------------------- step 10
say()
say("=" * 78)
say("PART 6 -- HOW BLIND IS THE CHECK TO THE EXOTIC SECTOR?")
say("=" * 78)
say("  Replace the exotics' E6 hypercharges by FREE parameters y1 (the colour")
say("  triplet pair) and y2 (the doublet pair), keeping only the vector-like")
say("  pairing.  If the anomaly coefficients are identically zero in y1,y2 the")
say("  check carries no information about the exotic sector whatsoever.")
y1, y2 = sp.symbols('y1 y2', rational=True)
free_exotics = [
    dict(name='D', c='3',  w='1', Y=y1), dict(name='Dc', c='3b', w='1', Y=-y1),
    dict(name='Hu', c='1', w='2', Y=y2), dict(name='Hd', c='1', w='2', Y=-y2),
]
g = c3 = s3 = s2 = sp.Integer(0)
for m in free_exotics:
    n = (3 if m['c'] in ('3', '3b') else 1) * (2 if m['w'] == '2' else 1)
    q = m['Y']
    g += n*q
    c3 += n*q**3
    s3 += NW[m['w']] * sp.Rational(T3[m['c']].numerator, T3[m['c']].denominator) * q
    s2 += NC[m['c']] * sp.Rational(T2[m['w']].numerator, T2[m['w']].denominator) * q
blind = dict(grav=str(sp.expand(g)), cubic=str(sp.expand(c3)),
             a33Q=str(sp.expand(s3)), a22Q=str(sp.expand(s2)))
for k, v in blind.items():
    say(f"     {k:<8} = {v}")
say(f"  => all identically zero in y1,y2: the four SM anomaly conditions are")
say(f"     COMPLETELY BLIND to the exotic sector, for ANY vector-like charges.")
RESULT['exotic_blindness'] = blind

with open('work.json', 'w') as f:
    json.dump(RESULT, f, indent=2)
with open('su5_anomaly_verdict_out.txt', 'w') as f:
    f.write("\n".join(lines) + "\n")
print("\n[wrote work.json + su5_anomaly_verdict_out.txt]")
